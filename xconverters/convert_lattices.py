from xsequence.lattice import Lattice
from xsequence.lattice_baseclasses import Beam
from xconverters.cpymad_utils import cpymad_lattice_conversion
from xconverters.pyat_utils import pyat_lattice_conversion
from xconverters.sad_utils import sad_lattice_conversion
from xconverters.pyat_utils import pyat_lattice_conversion
from xconverters.bmad_utils import bmad_lattice_conversion
from xconverters.xtrack_utils import xtrack_lattice_conversion


""" MADX """

def from_cpymad(madx, seq_name, energy=None, particle='electron', dependencies=False):
    if dependencies:
        lattice = cpymad_lattice_conversion.from_cpymad_with_dependencies(madx, seq_name, energy, particle)
        return lattice
    else:
        variables, sequence, elements_dict = cpymad_lattice_conversion.from_cpymad(madx, seq_name)
        beam = Beam(energy=energy, particle=particle)
        return Lattice(seq_name, sequence=sequence, elements=elements_dict, beam=beam, key='sequence')


def to_cpymad(lattice):
    return cpymad_lattice_conversion.to_cpymad(lattice)


def from_madx_seqfile(seq_file, seq_name, energy=None, dependencies=False, particle_type='electron'):
    madx = cpymad_lattice_conversion.from_madx_seqfile(seq_file, energy, particle_type)
    return from_cpymad(madx, seq_name, energy=energy, dependencies=dependencies)


def from_sad(sad_lattice, seq_name, energy=None):
    madx = sad_lattice_conversion.from_sad_to_madx(sad_lattice, energy)
    return from_cpymad(madx, seq_name, energy=energy)


""" PYAT """

def from_pyat(pyat_lattice):
    sequence, elements = pyat_lattice_conversion.from_pyat(pyat_lattice)
    beam = Beam(energy=pyat_lattice.energy*1e-9, particle='electron')
    return Lattice(pyat_lattice.name, sequence=sequence, elements=elements, key='line', beam=beam)


def to_pyat(lattice: Lattice):
    lattice._update_cavity_energy(force=False)
    lattice._update_harmonic_number(force=False)
    lattice._set_line()
    return pyat_lattice_conversion.to_pyat(lattice)


""" BMAD """

def to_bmad(lattice, file_path=None):
    if file_path:
        f = open(file_path, "w")
        f.write(bmad_lattice_conversion.to_bmad(lattice.name, lattice.beam, lattice.line))
        f.close()
    else:
        return bmad_lattice_conversion.to_bmad(lattice.name, lattice.beam, lattice.line)


""" XTRACK """

def to_xtrack(lattice):
    xtrack_lattice_conversion.to_xtrack(lattice.sliced.line)

