"""
Module tests.test_lattice_conversions.test_cpymad_xsequence_cpymad
------------------
:author: Felix Carlier (fcarlier@cern.ch)
This is a test module to test consistency for converting back and forth from cpymad.
"""

import pytest
from cpymad.madx import Madx
from xconverters import convert_lattices
from xconverters import conv_utils
from pathlib import Path

TEST_SEQ_DIR = Path(__file__).parent.parent / "test_sequences"

@pytest.fixture(scope="module")
def example_cpymad_xsequence_cpymad():
    """
    Create cpymad instance from import and export through xsequence

    Returns:
        Old and new twiss tables from cpymad
    """


    seq_name = 'lhcb1'
    madx_lattice=Madx(stdout=False)
    madx_lattice.call(str(TEST_SEQ_DIR / "lhc.seq"))
    madx_lattice.call(str(TEST_SEQ_DIR / "optics.madx"))
    madx_lattice.options.rbarc = True
    xsequence_lattice = convert_lattices.from_cpymad(madx_lattice, seq_name, dependencies=True)
    return xsequence_lattice


def test_mqxa1r1(example_cpymad_xsequence_cpymad):
    xlat = example_cpymad_xsequence_cpymad
    # k1 = kqx.r1 + ktqx1.r1
    assert xlat.elements['mqxa.1r1'].k1 == xlat.globals['kqx.r1'] + xlat.globals['ktqx1.r1']
    xlat.globals['ktqx1.r1'] = 0.01
    assert xlat.elements['mqxa.1r1'].k1 == xlat.globals['kqx.r1'] + xlat.globals['ktqx1.r1']
    xlat.globals['ktqx1.r1'] = -0.01
    assert xlat.elements['mqxa.1r1'].k1 == xlat.globals['kqx.r1'] + xlat.globals['ktqx1.r1']
    xlat.globals['kqx.r1'] = 0.02
    assert xlat.elements['mqxa.1r1'].k1 == xlat.globals['kqx.r1'] + xlat.globals['ktqx1.r1']


def test_mqxba2r1(example_cpymad_xsequence_cpymad):
    xlat = example_cpymad_xsequence_cpymad
    # k1 = -kqx.r1 - ktqx2.r1
    assert xlat.elements['mqxb.a2r1'].k1 == -xlat.globals['kqx.r1'] - xlat.globals['ktqx2.r1']
    xlat.globals['ktqx2.r1'] = 0.01
    assert xlat.elements['mqxb.a2r1'].k1 == -xlat.globals['kqx.r1'] - xlat.globals['ktqx2.r1']
    xlat.globals['ktqx2.r1'] = -0.01
    assert xlat.elements['mqxb.a2r1'].k1 == -xlat.globals['kqx.r1'] - xlat.globals['ktqx2.r1']
    xlat.globals['kqx.r1'] = 0.02
    assert xlat.elements['mqxb.a2r1'].k1 == -xlat.globals['kqx.r1'] - xlat.globals['ktqx2.r1']


def test_mqsx3r1(example_cpymad_xsequence_cpymad):
    xlat = example_cpymad_xsequence_cpymad
    # k1 = -kqx.r1 - ktqx2.r1
    assert xlat.elements['mqsx.3r1'].k1s == xlat.globals['kqsx3.r1']
    xlat.globals['kqsx3.r1'] = 0.01
    assert xlat.elements['mqsx.3r1'].k1s == xlat.globals['kqsx3.r1']
    xlat.globals['kqsx3.r1'] = -0.01
    assert xlat.elements['mqsx.3r1'].k1s == xlat.globals['kqsx3.r1']
    xlat.globals['kqsx3.r1'] = xlat.globals['kqsx3.r1'] + 0.01
    assert xlat.elements['mqsx.3r1'].k1s == xlat.globals['kqsx3.r1']


