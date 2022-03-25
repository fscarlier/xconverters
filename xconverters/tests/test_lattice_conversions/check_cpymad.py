"""
Module tests.test_lattice_conversions.test_cpymad_xsequence_cpymad
------------------
:author: Felix Carlier (fcarlier@cern.ch)
This is a test module to test consistency for converting back and forth from cpymad.
"""

from cpymad.madx import Madx
from xconverters import convert_lattices  
from xconverters import conv_utils

# FCC TEST

mad = conv_utils.create_cpymad_from_file("../test_sequences/lattice.seq", energy=120)
mad.command.beam(particle='electron', energy=120)
mad.use('l000013')

xlat = convert_lattices.from_cpymad(mad, 'l000013', energy=120)

mad_new = convert_lattices.to_cpymad(xlat)
mad_new.command.beam(particle='electron', energy=120)
mad_new.use('l000013')

twiss = mad.twiss(sequence='l000013')
twiss_new = mad_new.twiss(sequence='l000013')

    
# LHC TEST
    
seq_name = 'lhcb1'
mad=Madx(stdout=False)
mad.call("../test_sequences/lhc.seq")
mad.call("../test_sequences/optics.madx")
mad.options.rbarc = True
mad.command.beam(particle='proton')
mad.use(seq_name)

xlat = convert_lattices.from_cpymad(mad, seq_name, dependencies=True)

mad_new = convert_lattices.to_cpymad(xlat)
mad_new.command.beam(particle='proton')
mad_new.use(seq_name)

twiss = mad.twiss(sequence=seq_name)
twiss_new = mad_new.twiss(sequence=seq_name)
