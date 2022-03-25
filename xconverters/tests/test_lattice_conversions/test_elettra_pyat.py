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

    madx_lattice = conv_utils.create_cpymad_from_file("../test_sequences/elettra_thick.seq", energy=NRJ)
    madx_lattice.command.beam(particle='electron', energy=NRJ)
    madx_lattice.use(seq_name)

    xsequence_lattice = convert_lattices.from_cpymad(madx_lattice, seq_name, energy=NRJ, dependencies=False)
    pyat_lattice = convert_lattices.to_pyat(xsequence_lattice)

    xsequence_lattice_new = convert_lattices.from_pyat(pyat_lattice)
    pyat_lattice_new = convert_lattices.to_pyat(xsequence_lattice_new)
    return pyat_lattice, pyat_lattice_new


def test_drift(example_pyat_xsequence_pyat):
    lat, lat_new = example_pyat_xsequence_pyat
    for idx, element in enumerate(lat):
        if element.__class__.__name__ == 'Drift':
            if lat[idx] != lat_new[idx]:
                if not check_attributes(lat[idx], lat_new[idx]):
                    print(lat[idx])
                    print(lat_new[idx])
                    pytest.fail(f"Relative deviation larger than 1e-12 tolerance")
            else:
                return True   


def test_quadrupole(example_pyat_xsequence_pyat):
    lat, lat_new = example_pyat_xsequence_pyat
    for idx, element in enumerate(lat):
        if element.__class__.__name__ == 'Quadrupole':
            if lat[idx] != lat_new[idx]:
                if not check_attributes(lat[idx], lat_new[idx]):
                    pytest.fail(f"Relative deviation larger than 1e-12 tolerance")
            else:
                return True   


def test_sextupole(example_pyat_xsequence_pyat):
    lat, lat_new = example_pyat_xsequence_pyat
    for idx, element in enumerate(lat):
        if element.__class__.__name__ == 'Sextupole':
            if lat[idx] != lat_new[idx]:
                if not check_attributes(lat[idx], lat_new[idx]):
                    pytest.fail(f"Relative deviation larger than 1e-12 tolerance")
            else:
                return True   


def test_rfcavity(example_pyat_xsequence_pyat):
    lat, lat_new = example_pyat_xsequence_pyat
    for idx, element in enumerate(lat):
        if element.__class__.__name__ == 'RFCavity':
            if lat[idx] != lat_new[idx]:
                if not check_attributes(lat[idx], lat_new[idx]):
                    pytest.fail(f"Relative deviation larger than 1e-12 tolerance")
            else:
                return True   


@pytest.mark.xfail(reason="Drift calculation suffers from float precision in Python")
def test_drifts_fail(example_pyat_xsequence_pyat):
    lat, lat_new = example_pyat_xsequence_pyat
    for idx, element in enumerate(lat):
        if element.__class__.__name__ == 'Drift':
            assert lat[idx] == lat_new[idx]
