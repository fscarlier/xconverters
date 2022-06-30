from xsequence.lattice import Lattice
from xsequence.lattice_baseclasses import Beam
from xconverters.cpymad_utils import convert_cpymad_lattices
from xconverters.pyat_utils import convert_pyat_lattices
from xconverters.xtrack_utils import convert_xtrack_lattices

from xconverters.sad_utils import convert_sad_lattices
from xconverters.pyat_utils import convert_pyat_lattices
from xconverters.bmad_utils import convert_bmad_lattices



""" MADX """

def from_cpymad(madx, seq_name, energy=None, particle='electron', dependencies=False):
    if dependencies:
        lattice = convert_cpymad_lattices.from_cpymad_with_dependencies(madx, seq_name, energy, particle)
        return lattice
    else:
        variables, sequence, elements_dict = convert_cpymad_lattices.from_cpymad(madx, seq_name)
        beam = Beam(energy=energy, particle=particle)
        return Lattice(seq_name, sequence=sequence, elements=elements_dict, beam=beam, key='sequence')


def to_cpymad(lattice):
    return convert_cpymad_lattices.to_cpymad(lattice)


def from_madx_seqfile(seq_file, seq_name, energy=None, dependencies=False, particle_type='electron'):
    madx = convert_cpymad_lattices.from_madx_seqfile(seq_file, energy, particle_type)
    return from_cpymad(madx, seq_name, energy=energy, dependencies=dependencies)


def from_sad(sad_lattice, seq_name, energy=None):
    madx = convert_sad_lattices.from_sad_to_madx(sad_lattice, energy)
    return from_cpymad(madx, seq_name, energy=energy)


""" PYAT """

def from_pyat(pyat_lattice):
    sequence, elements = convert_pyat_lattices.from_pyat(pyat_lattice)
    beam = Beam(energy=pyat_lattice.energy*1e-9, particle='electron')
    return Lattice(pyat_lattice.name, sequence=sequence, elements=elements, key='line', beam=beam)


def to_pyat(lattice: Lattice):
    lattice._update_cavity_energy(force=False)
    lattice._update_harmonic_number(force=False)
    lattice._set_line()
    return convert_pyat_lattices.to_pyat(lattice)


""" BMAD """

def to_bmad(lattice, file_path=None):
    if file_path:
        f = open(file_path, "w")
        f.write(convert_bmad_lattices.to_bmad(lattice.name, lattice.beam, lattice.line))
        f.close()
    else:
        return convert_bmad_lattices.to_bmad(lattice.name, lattice.beam, lattice.line)


""" XTRACK """

def to_xtrack(lattice):
    convert_xtrack_lattices.to_xtrack(lattice.sliced.line)

