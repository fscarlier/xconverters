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
        if el1_dict[key] != el2_dict[key]:
            diff = (el2_dict[key] - el1_dict[key])/el1_dict[key]
            if diff > 1e-13:
                return False
            else: 
                print(diff)
        else:
            return True

def test_pyat_sequence():
    madx_lattice = conv_utils.create_cpymad_from_file(str(TEST_SEQ_DIR / "lattice.seq"), energy=120)
    madx_lattice.command.beam(particle='electron', energy=120)
    madx_lattice.use('l000013')

    xsequence_lattice = convert_lattices.from_cpymad(madx_lattice, 'l000013', energy=120)
    pyat_lattice = convert_lattices.to_pyat(xsequence_lattice)
    
    xsequence_lattice_new = convert_lattices.from_pyat(pyat_lattice)
    pyat_lattice_new = convert_lattices.to_pyat(xsequence_lattice_new)
    for idx, element in enumerate(pyat_lattice):
        if element.__class__.__name__ != 'Drift':
            assert check_attributes(pyat_lattice[idx], pyat_lattice_new[idx])
