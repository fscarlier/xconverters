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
    l = [el.Length for el in pyat_lattice]
    l_new = [el.Length for el in pyat_lattice_new]
    return s, s_new, l, l_new


def test_pyat_xsequence_pyat_s(example_pyat_xsequence_pyat):
    s, s_new, l, l_new = example_pyat_xsequence_pyat
    assert sum(abs(s - s_new)) < 1e-4


def test_pyat_xsequence_pyat_tot_L(example_pyat_xsequence_pyat):
    s, s_new, l, l_new = example_pyat_xsequence_pyat
    assert (sum(l)-sum(l_new))/sum(l) < 1e-10
