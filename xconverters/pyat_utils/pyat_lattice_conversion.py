"""
Module xsequence.lattice
------------------
:author: Felix Carlier (fcarlier@cern.ch)
This is a Python3 module containing base Lattice class to manipulate accelerator sequences.
"""

import at
import scipy.constants
import xsequence.elements as xe
from xsequence.lattice import Lattice
from xsequence.lattice_baseclasses import Node, NodesList
from xconverters.pyat_utils import convert_pyat_elements
from typing import List, Tuple, Dict


def from_pyat(pyat_lattice: at.Lattice) -> Tuple[NodesList, Dict[str, xe.BaseElement]]:
    """ Import lattice from pyat to create xsequence of Nodes and dict of elements """
    sequence = NodesList()
    elements = {}
    for el in pyat_lattice:
        name = el.FamName
        elements[name] = convert_pyat_elements.from_pyat(el)
        sequence.append(Node(element_name=name, length=el.Length))
    return sequence, elements


def to_pyat(lattice: Lattice) -> at.Lattice:
    """ Export xsequence Lattice to pyat Lattice instance """
    line = [convert_pyat_elements.to_pyat(lattice._line_elements[node.element_name]) for node in lattice._line]
    pyat_lattice = at.Lattice(line, name=lattice.name, key='ring', energy=lattice.beam.energy*1e9)
    for cav in at.get_elements(pyat_lattice, at.RFCavity):
        cav.Frequency = cav.HarmNumber*scipy.constants.c/pyat_lattice.circumference
    return pyat_lattice


