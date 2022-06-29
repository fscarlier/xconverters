"""
Module tests.test_elements.test_element_cpymad
------------------
:author: Felix Carlier (fcarlier@cern.ch)
This is a test module to test correct element imports from cpymad.
"""

import pytest
import xsequence.elements as xe
from xconverters.cpymad_utils import convert_cpymad_elements
from xconverters.cpymad_utils import convert_cpymad_elements
from cpymad.madx import Madx
from pathlib import Path
from xconverters import conv_utils
TEST_SEQ_DIR = Path(__file__).parent.parent / "test_sequences"


"""
Element by element tests cpymad back to cpymad (FCC-ee lattice)
"""

@pytest.fixture(scope="module")
def example_madx_lattice():
    NRJ = 2.4
    seq_name = 'ring'
    madx_lattice = conv_utils.create_cpymad_from_file(str(TEST_SEQ_DIR / "elettra_thick.seq"), energy=NRJ)
    madx_lattice.command.beam(particle='electron', energy=NRJ)
    madx_lattice.use(seq_name)
    return madx_lattice



def test_marker(example_madx_lattice):
    madx_lattice = example_madx_lattice
    md = Madx()
    results = []
    for idx in range(len(madx_lattice.sequence.ring.elements)):
        el = madx_lattice.sequence.ring.elements[idx]
        if el.base_type.name == 'marker':
            xseq_el = convert_cpymad_elements.from_cpymad(el)
            convert_cpymad_elements.to_cpymad(md, xseq_el)
            if el == md.elements[el.name]:
                results.append(True)
    assert all(results)


def test_multipole(example_madx_lattice):
    madx_lattice = example_madx_lattice
    md = Madx()
    results = []
    for idx in range(len(madx_lattice.sequence.ring.elements)):
        el = madx_lattice.sequence.ring.elements[idx]
        if el.base_type.name == 'multipole':
            xseq_el = convert_cpymad_elements.from_cpymad(el)
            convert_cpymad_elements.to_cpymad(md, xseq_el)
            if el == md.elements[el.name]:
                results.append(True)
    assert all(results)


def test_quadrupole(example_madx_lattice):
    madx_lattice = example_madx_lattice
    md = Madx()
    results = []
    for idx in range(len(madx_lattice.sequence.ring.elements)):
        el = madx_lattice.sequence.ring.elements[idx]
        if el.base_type.name == 'quadrupole':
            xseq_el = convert_cpymad_elements.from_cpymad(el)
            convert_cpymad_elements.to_cpymad(md, xseq_el)
            if el == md.elements[el.name]:
                results.append(True)
    assert all(results)


def test_sextupoles(example_madx_lattice):
    madx_lattice = example_madx_lattice
    md = Madx()
    results = []
    for idx in range(len(madx_lattice.sequence.ring.elements)):
        el = madx_lattice.sequence.ring.elements[idx]
        if el.base_type.name == 'sextupole':
            xseq_el = convert_cpymad_elements.from_cpymad(el)
            convert_cpymad_elements.to_cpymad(md, xseq_el)
            if el == md.elements[el.name]:
                results.append(True)
    assert all(results)


def test_octupole(example_madx_lattice):
    madx_lattice = example_madx_lattice
    md = Madx()
    results = []
    for idx in range(len(madx_lattice.sequence.ring.elements)):
        el = madx_lattice.sequence.ring.elements[idx]
        if el.base_type.name == 'octupole':
            xseq_el = convert_cpymad_elements.from_cpymad(el)
            convert_cpymad_elements.to_cpymad(md, xseq_el)
            if el == md.elements[el.name]:
                results.append(True)
    assert all(results)


def test_rfcavity(example_madx_lattice):
    madx_lattice = example_madx_lattice
    md = Madx()
    results = []
    for idx in range(len(madx_lattice.sequence.ring.elements)):
        el = madx_lattice.sequence.ring.elements[idx]
        if el.base_type.name == 'rfcavity':
            xseq_el = convert_cpymad_elements.from_cpymad(el)
            convert_cpymad_elements.to_cpymad(md, xseq_el)
            if el == md.elements[el.name]:
                results.append(True)
    assert all(results)


def test_sbend(example_madx_lattice):
    madx_lattice = example_madx_lattice
    md = Madx()
    results = []
    for idx in range(len(madx_lattice.sequence.ring.elements)):
        el = madx_lattice.sequence.ring.elements[idx]
        if el.base_type.name == 'sbend':
            xseq_el = convert_cpymad_elements.from_cpymad(el)
            convert_cpymad_elements.to_cpymad(md, xseq_el)
            if el == md.elements[el.name]:
                results.append(True)
    assert all(results)


def test_rbend(example_madx_lattice):
    madx_lattice = example_madx_lattice
    md = Madx()
    results = []
    for idx in range(len(madx_lattice.sequence.ring.elements)):
        el = madx_lattice.sequence.ring.elements[idx]
        if el.base_type.name == 'rbend':
            xseq_el = convert_cpymad_elements.from_cpymad(el)
            convert_cpymad_elements.to_cpymad(md, xseq_el)
            if el == md.elements[el.name]:
                results.append(True)
    assert all(results)


def test_monitor(example_madx_lattice):
    madx_lattice = example_madx_lattice
    md = Madx()
    results = []
    for idx in range(len(madx_lattice.sequence.ring.elements)):
        el = madx_lattice.sequence.ring.elements[idx]
        if el.base_type.name == 'monitor':
            xseq_el = convert_cpymad_elements.from_cpymad(el)
            convert_cpymad_elements.to_cpymad(md, xseq_el)
            if el == md.elements[el.name]:
                results.append(True)
    assert all(results)
