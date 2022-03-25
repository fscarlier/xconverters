"""
Module tests.test_lattice_conversions/test_pyat_xsequence_pyat
------------------
:author: Felix Carlier (fcarlier@cern.ch)
This is a test module to test consistency for converting back and forth from pyat.
"""

from xsequence.helpers.pyat_functions import get_optics_pyat
from xconverters import convert_lattices  
from xconverters import conv_utils
import pytest
from pathlib import Path

TEST_SEQ_DIR = Path(__file__).parent.parent / "test_sequences"

@pytest.fixture(scope="module")
def example_pyat_xsequence_pyat():
    """
    Create pyat instance from import and export through xsequence
    
    Returns:
        Old and new twiss data arrays
        Old and new s position arrays
    """
    pyat_lattice = conv_utils.create_pyat_from_file(TEST_SEQ_DIR / "fcch_norad.mat")
    xsequence_lattice = convert_lattices.from_pyat(pyat_lattice)
    pyat_lattice_new = convert_lattices.to_pyat(xsequence_lattice)
    lin, s = get_optics_pyat(pyat_lattice, radiation=False)
    lin_new, s_new = get_optics_pyat(pyat_lattice_new, radiation=False)
    return lin, lin_new, s, s_new

def test_pyat_xsequence_pyat_s(example_pyat_xsequence_pyat):
    lin, lin_new, s, s_new = example_pyat_xsequence_pyat
    assert sum(abs(s - s_new)) == 0

def test_pyat_xsequence_pyat_orbit(example_pyat_xsequence_pyat):
    lin, lin_new, _, _ = example_pyat_xsequence_pyat
    assert sum(abs(lin.closed_orbit[:,0] - lin_new.closed_orbit[:,0])) == 0 and\
           sum(abs(lin.closed_orbit[:,1] - lin_new.closed_orbit[:,1])) == 0 and\
           sum(abs(lin.closed_orbit[:,2] - lin_new.closed_orbit[:,2])) == 0 and\
           sum(abs(lin.closed_orbit[:,3] - lin_new.closed_orbit[:,3])) == 0 and\
           sum(abs(lin.closed_orbit[:,4] - lin_new.closed_orbit[:,4])) == 0 and\
           sum(abs(lin.closed_orbit[:,5] - lin_new.closed_orbit[:,5])) == 0

def test_pyat_xsequence_pyat_beta_x(example_pyat_xsequence_pyat):
    lin, lin_new, _, _ = example_pyat_xsequence_pyat
    assert max(abs((lin.beta[:,0] - lin_new.beta[:,0])/lin_new.beta[:,0])) == 0 

def test_pyat_xsequence_pyat_beta_y(example_pyat_xsequence_pyat):
    lin, lin_new, _, _ = example_pyat_xsequence_pyat
    assert max(abs((lin.beta[:,1] - lin_new.beta[:,1])/lin_new.beta[:,1])) == 0

def test_pyat_xsequence_pyat_disp(example_pyat_xsequence_pyat):
    lin, lin_new, _, _ = example_pyat_xsequence_pyat
    assert sum(abs(lin.dispersion[:,0] - lin_new.dispersion[:,0])) == 0 and\
           sum(abs(lin.dispersion[:,1] - lin_new.dispersion[:,1])) == 0

def test_pyat_xsequence_pyat_alfa(example_pyat_xsequence_pyat):
    lin, lin_new, _, _ = example_pyat_xsequence_pyat
    assert sum(abs(lin.alpha[:,0] - lin_new.alpha[:,0])) == 0 and\
           sum(abs(lin.alpha[:,1] - lin_new.alpha[:,1])) == 0

def test_pyat_xsequence_pyat_phase(example_pyat_xsequence_pyat):
    lin, lin_new, _, _ = example_pyat_xsequence_pyat
    assert sum(abs(lin.mu[:,0] - lin_new.mu[:,0])) == 0 and\
           sum(abs(lin.mu[:,1] - lin_new.mu[:,1])) == 0

