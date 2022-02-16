"""
Module tests.test_elements.test_element_cpymad
------------------
:author: Felix Carlier (fcarlier@cern.ch)
This is a test module to test correct element imports from cpymad.
"""

import pytest
import xsequence.elements as xe
from xconverters.cpymad import cpymad_element_conversion
from cpymad.madx import Madx
from pathlib import Path
TEST_SEQ_DIR = Path(__file__).parent.parent / "test_sequences"


"""
Element by element tests cpymad back to cpymad (FCC-ee lattice)
"""

@pytest.fixture(scope="module")
def example_madx_lattice():
    madx_lattice = Madx()
    madx_lattice.call(str(TEST_SEQ_DIR / "lhc.seq"))
    madx_lattice.call(str(TEST_SEQ_DIR / "optics.madx"))
    return madx_lattice    



def test_quadrupoles(example_madx_lattice):
    madx_lattice = example_madx_lattice
    md = Madx()
    results = []
    for idx in range(292,len(madx_lattice.elements)):
        el = madx_lattice.elements[idx]
        if el.base_type.name == 'quadrupole':
            xseq_el = cpymad_element_conversion.convert_cpymad_element(el)
            cpymad_element_conversion.to_cpymad(xseq_el, md)
            if el == md.elements[el.name]:
                results.append(True)
    assert all(results)


def test_sextupoles(example_madx_lattice):
    madx_lattice = example_madx_lattice
    md = Madx()
    results = []
    for idx in range(292,len(madx_lattice.elements)):
        el = madx_lattice.elements[idx]
        if el.base_type.name == 'sextupole':
            xseq_el = cpymad_element_conversion.convert_cpymad_element(el)
            cpymad_element_conversion.to_cpymad(xseq_el, md)
            if el == md.elements[el.name]:
                results.append(True)
    assert all(results)


def test_marker(example_madx_lattice):
    madx_lattice = example_madx_lattice
    md = Madx()
    results = []
    for idx in range(292,len(madx_lattice.elements)):
        el = madx_lattice.elements[idx]
        if el.base_type.name == 'marker':
            xseq_el = cpymad_element_conversion.convert_cpymad_element(el)
            cpymad_element_conversion.to_cpymad(xseq_el, md)
            if el == md.elements[el.name]:
                results.append(True)
    assert all(results)


def test_rbend(example_madx_lattice):
    madx_lattice = example_madx_lattice
    md = Madx()
    results = []
    for idx in range(292,len(madx_lattice.elements)):
        el = madx_lattice.elements[idx]
        if el.base_type.name == 'rbend':
            xseq_el = cpymad_element_conversion.convert_cpymad_element(el)
            cpymad_element_conversion.to_cpymad(xseq_el, md)
            if el == md.elements[el.name]:
                results.append(True)
    assert all(results)

