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

TEST_SEQ_DIR = Path(__file__).parent.parent / "test_sequences"

def check_attributes(el1, el2):
    el1_dict = el1.__dict__
    el2_dict = el2.__dict__
    for key in el1_dict:
        if isinstance(el1_dict[key], np.ndarray):
            array_1 = np.trim_zeros(el1_dict[key], trim='b')
            array_2 = np.trim_zeros(el2_dict[key], trim='b')
            if len(array_1) != len(array_2):
                return False
            arr_eq = np.isclose(array_1, array_2, rtol=1e-10)
            if False in arr_eq:
                return False
        elif el1_dict[key] != el2_dict[key]:
            diff = (el2_dict[key] - el1_dict[key])/el1_dict[key]
            if abs(diff) > 1e-9:
                print(diff)
                return False
    return True


@pytest.fixture(scope="module")
def example_pyat_xsequence_pyat():
    """
    Create pyat instance from import and export through xsequence

    Returns:
        Old and new twiss data arrays
        Old and new s position arrays
    """
    NRJ = 2.4
    seq_name = 'ring'

    madx_lattice = conv_utils.create_cpymad_from_file(str(TEST_SEQ_DIR / "elettra_thick.seq"), energy=NRJ)
    madx_lattice.command.beam(particle='electron', energy=NRJ)
    madx_lattice.use(seq_name)

    xsequence_lattice = convert_lattices.from_cpymad(madx_lattice, seq_name, energy=NRJ, dependencies=False)
    pyat_lattice = convert_lattices.to_pyat(xsequence_lattice)

    xsequence_lattice = convert_lattices.from_pyat(pyat_lattice)
    pyat_lattice_new = convert_lattices.to_pyat(xsequence_lattice)
    for ii, el in enumerate(pyat_lattice):
        pyat_lattice_new[ii].Length = el.Length

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

