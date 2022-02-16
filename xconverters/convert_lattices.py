from xsequence.lattice import Lattice
from xconverters.cpymad import cpymad_lattice_conversion
from xconverters.pyat import pyat_lattice_conversion
from xconverters.sad import sad_lattice_conversion
from xconverters.pyat import pyat_lattice_conversion
from xconverters.bmad import bmad_lattice_conversion
from xconverters.xtrack import xtrack_lattice_conversion


def from_cpymad(madx, seq_name, energy=None, dependencies=False):
    if dependencies:
        xdeps_manager, vref, mref, sref, element_seq = cpymad_lattice_conversion.from_cpymad_with_dependencies(madx, seq_name)
        return Lattice(seq_name, element_seq, energy=energy, key='sequence', vref=vref, mref=mref, sref=sref, xdeps_manager=xdeps_manager) 
    else:
        _, element_seq = cpymad_lattice_conversion.from_cpymad(madx, seq_name)
        return Lattice(seq_name, element_seq, energy=energy, key='sequence') 


def from_madx_seqfile(seq_file, seq_name, energy=None, dependencies=False, particle_type='electron'):
    madx = cpymad_lattice_conversion.from_madx_seqfile(seq_file, energy, particle_type)
    return from_cpymad(madx, seq_name, energy=energy, dependencies=dependencies)


def from_sad(sad_lattice, seq_name, energy=None):
    madx = sad_lattice_conversion.from_sad_to_madx(sad_lattice, energy)
    return from_cpymad(madx, seq_name, energy=energy)


def from_pyat(pyat_lattice):
    seq = pyat_lattice_conversion.from_pyat(pyat_lattice)
    return Lattice(pyat_lattice.name, seq, energy=pyat_lattice.energy*1e-9) 


def to_cpymad(lattice):
    return cpymad_lattice_conversion.to_cpymad(lattice.name, lattice.beam.energy, lattice.sequence)


def to_pyat(lattice):
    lattice._update_cavity_energy()
    lattice._update_harmonic_number()
    return pyat_lattice_conversion.to_pyat(lattice.name, lattice.beam.energy*1e9, lattice.line)


def to_bmad(lattice, file_path=None):
    if file_path:
        f = open(file_path, "w")
        f.write(bmad_lattice_conversion.to_bmad(lattice.name, lattice.beam, lattice.line))
        f.close()
    else:
        return bmad_lattice_conversion.to_bmad(lattice.name, lattice.beam, lattice.line) 


def to_xtrack(lattice):
    xtrack_lattice_conversion.to_xtrack(lattice.sliced.line) 

