"""
Module xsequence.lattice
------------------
:author: Felix Carlier (fcarlier@cern.ch)
This is a Python3 module containing base Lattice class to manipulate accelerator sequences.
"""

from ast import Raise
import xdeps

from cpymad.madx import Madx
from collections import defaultdict
from lark import Lark, Transformer, v_args

from xsequence.lattice import Lattice
from xsequence.lattice_baseclasses import Node, NodesList
import xsequence.elements_dataclasses as xed
from xconverters.cpymad_utils import convert_cpymad_elements
from xsequence.lattice_baseclasses import Beam

calc_grammar = """
    ?start: sum
        | NAME "=" sum      -> assign_var

    ?sum: product
        | sum "+" product   -> add
        | sum "-" product   -> sub

    ?product: power
        | product "*" atom  -> mul
        | product "/" atom  -> div

    ?power: atom
        | power "^" atom    -> pow

    ?atom: NUMBER           -> number
         | "-" atom         -> neg
         | "+" atom         -> pos
         | NAME             -> var
         | NAME "->" NAME   -> get
         | NAME "(" sum ("," sum)* ")" -> call
         | "(" sum ")"

    NAME: /[a-z_\.][a-z0-9_\.%]*/
    %import common.NUMBER
    %import common.WS_INLINE
    %ignore WS_INLINE
"""

@v_args(inline=True)
class XSequenceMadxEval(Transformer):
    from operator import add, sub, mul, truediv as div
    from operator import neg, pos, pow
    number = float

    def __init__(self, variables, functions, elements):
        self.variables = variables
        self.functions = functions
        self.elements  = elements
        self.eval=Lark(calc_grammar, parser='lalr',
                         transformer=self).parse

    def assign_var(self, name, value):
        self.variables[name] = value
        return value

    def call(self,name,*args):
        ff=getattr(self.functions,name)
        return ff(*args)

    def get(self,name,key):
        return getattr(self.elements.sequence[name[1]], key)

    def var(self, name):
        try:
            return self.variables[name.value]
        except KeyError:
            raise Exception("Variable not found: %s" % name)


def from_madx_seqfile(seq_file, seq_name, energy: float, particle_type: str = 'electron') -> Madx:
    """ Import lattice from MAD-X sequence file """
    madx = Madx()
    madx.option(echo=False, info=False, debug=False)
    madx.call(file=seq_file)
    madx.command.beam(particle=particle_type, energy=energy)
    madx.use(seq_name)
    madx.input('SET, FORMAT="25.20e";')
    return madx


def find_reference_node_idx(sequence, reference):
    if reference == '':
        return 0
    else:
        matching_nodes = [idx for idx, node in enumerate(sequence) if node.element_name == reference]
        if len(matching_nodes) > 1:
            raise Exception(f"Too many nodes with reference element name for positions: {reference}")
        elif len(matching_nodes) == 0:
            raise Exception(f"No nodes with reference element name for positions: {reference}")
        else:
            return matching_nodes[0]


def from_cpymad(madx: Madx, seq_name: str):
    variables=defaultdict(lambda :0)
    for name,par in madx.globals.cmdpar.items():
        variables[name]=par.value

    sequence = NodesList()
    elements_dict = {}
    for element in madx.sequence[seq_name].elements:
        element_data={}
        for parname, par in element.cmdpar.items():
            element_data[parname]=par.value
        elements_dict[element.name] = convert_cpymad_elements.from_cpymad(element)
        sequence.append(Node(element_name=element.name, location=element['at'], reference_element=element['from']))

    for el in sequence:
        reference_node_idx = find_reference_node_idx(sequence, el.reference_element)
        if reference_node_idx != 0:
            el.reference = sequence[reference_node_idx].position
        else:
            el.reference = 0

    return variables, sequence, elements_dict


def from_cpymad_with_dependencies(madx: Madx, seq_name: str, energy: float, particle: str, dependencies: bool = False):
    from xdeps.madxutils import MadxEval

    variables, sequence, elements_dict = from_cpymad(madx, seq_name)
    beam = Beam(energy=energy, particle=particle)
    lattice = Lattice(seq_name, elements=elements_dict, sequence=sequence, global_variables=variables, beam=beam)

    madeval = MadxEval(lattice._globals, lattice._math, lattice._elements).eval

    for name,par in madx.globals.cmdpar.items():
        if par.expr is not None:
            lattice._globals[name]=madeval(par.expr)
    print('dep start')

    for elem in madx.sequence[seq_name].elements:
        name = elem.name
        for parname, par in elem.cmdpar.items():
            if parname in convert_cpymad_elements.REQ_ATTR_INVERTED:
                parname = convert_cpymad_elements.REQ_ATTR_INVERTED[parname]
            if parname in lattice.elements[name].REQUIREMENTS:
                if par.expr is not None:
                    if par.dtype==12: # handle lists
                        for ii,ee in enumerate(par.expr):
                            if ee is not None:
                                lattice._elements[name]._set_from_key(parname, madeval(ee))
                    else:
                        setattr(lattice._elements[name], parname, madeval(par.expr))

    print('dep location nodes')
    for node in lattice.sequence:
        ref_element = node.reference_element
        if ref_element != '':
            node.reference = lattice.sequence[find_reference_node_idx(sequence, ref_element)].location
    print('dep end')

    return lattice


def to_cpymad(lattice):
    madx = Madx()
    madx.option(echo=False, info=False, debug=False)
    seq_command = ''

    for node in lattice.sequence[1:-1]:
        convert_cpymad_elements.to_cpymad(madx, lattice.elements[node.element_name])
        if len(node.reference_element) > 0:
            seq_command += f'{node.element_name}, at={node.location}, from={node.reference_element}  ;\n'
        else:
            seq_command += f'{node.element_name}, at={node.location} ;\n'

    madx.input(f'{lattice.name}: sequence, refer=centre, l={lattice.sequence[-1].end};')
    madx.input(seq_command)
    madx.input('endsequence;')
    madx.command.beam(particle='electron', energy=lattice.beam.energy)
    return madx
