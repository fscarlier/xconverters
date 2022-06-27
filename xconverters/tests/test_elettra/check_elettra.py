import pytest
from xconverters import convert_lattices  
from xconverters import conv_utils
from pathlib import Path


NRJ = 2.4
seq_name = 'ring'
madx_lattice = conv_utils.create_cpymad_from_file("../test_sequences/elettra_thick.seq", energy=NRJ)
madx_lattice.command.beam(particle='electron', energy=NRJ)
madx_lattice.use(seq_name)

xsequence_lattice = convert_lattices.from_cpymad(madx_lattice, seq_name, energy=NRJ, dependencies=False)
madx_lattice_new = convert_lattices.to_cpymad(xsequence_lattice)
madx_lattice_new.command.beam(particle='electron', energy=NRJ)
madx_lattice_new.use(seq_name)
twiss = madx_lattice.twiss(sequence=seq_name)
twiss_new = madx_lattice_new.twiss(sequence=seq_name)
