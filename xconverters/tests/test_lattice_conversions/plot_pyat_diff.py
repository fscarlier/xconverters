"""
Module tests.test_lattice_conversions/test_pyat_xsequence_pyat
------------------
:author: Felix Carlier (fcarlier@cern.ch)
This is a test module to test consistency for converting back and forth from pyat.
"""

import pytest
import numpy as np
from xconverters import convert_lattices  
from xconverters import conv_utils
from pathlib import Path
from xsequence.helpers.pyat_functions import get_optics_pyat
from xsequence.helpers.fcc_plots import fcc_axes
import matplotlib.pyplot as plt

madx_lattice = conv_utils.create_cpymad_from_file("../test_sequences/lattice.seq", energy=120)
madx_lattice.command.beam(particle='electron', energy=120)
madx_lattice.use('l000013')

xsequence_lattice = convert_lattices.from_cpymad(madx_lattice, 'l000013', energy=120)
pyat_lattice = convert_lattices.to_pyat(xsequence_lattice)

xsequence_lattice_new = convert_lattices.from_pyat(pyat_lattice)
pyat_lattice_new = convert_lattices.to_pyat(xsequence_lattice_new)

lin, s = get_optics_pyat(pyat_lattice, radiation=False)
lin_new, s_new = get_optics_pyat(pyat_lattice_new, radiation=False)


fig1, ax1 = fcc_axes(y_label='ds')
ax1.plot(s, s-s_new)

fig2 , ax2  = fcc_axes(y_label='dcox')
ax2 .plot(s, lin.closed_orbit[:,0] - lin_new.closed_orbit[:,0]) 

fig3 , ax3  = fcc_axes(y_label='dcopx')
ax3 .plot(s, lin.closed_orbit[:,1] - lin_new.closed_orbit[:,1]) 

fig4 , ax4  = fcc_axes(y_label='dcoy')
ax4 .plot(s, lin.closed_orbit[:,2] - lin_new.closed_orbit[:,2]) 

fig5 , ax5  = fcc_axes(y_label='dcopy')
ax5 .plot(s, lin.closed_orbit[:,3] - lin_new.closed_orbit[:,3]) 

fig6 , ax6  = fcc_axes(y_label='dcot')
ax6 .plot(s, lin.closed_orbit[:,4] - lin_new.closed_orbit[:,4]) 

fig7 , ax7  = fcc_axes(y_label='dcopt')
ax7 .plot(s, lin.closed_orbit[:,5] - lin_new.closed_orbit[:,5])

fig8 , ax8  = fcc_axes(y_label='dbetx')
ax8 .plot(s, (lin.beta[:,0] - lin_new.beta[:,0])/lin.beta[:,0]) 

fig9 , ax9  = fcc_axes(y_label='dbety')
ax9 .plot(s, (lin.beta[:,1] - lin_new.beta[:,1])/lin.beta[:,0])

fig10, ax10 = fcc_axes(y_label='dDx')
ax10.plot(s, lin.dispersion[:,0] - lin_new.dispersion[:,0]) 

fig11, ax11 = fcc_axes(y_label='dDy')
ax11.plot(s, lin.dispersion[:,1] - lin_new.dispersion[:,1])

fig12, ax12 = fcc_axes(y_label='dalfx')
ax12.plot(s, lin.alpha[:,0] - lin_new.alpha[:,0]) 

fig13, ax13 = fcc_axes(y_label='dalfy')
ax13.plot(s, lin.alpha[:,1] - lin_new.alpha[:,1])

fig14, ax14 = fcc_axes(y_label='dmux')
ax14.plot(s, lin.mu[:,0] - lin_new.mu[:,0]) 

fig15, ax15 = fcc_axes(y_label='dmuy')
ax15.plot(s, lin.mu[:,1] - lin_new.mu[:,1])

plt.show()





