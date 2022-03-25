%load_ext autoreload
%autoreload 2

import numpy as np
from xsequence.helpers.pyat_functions import get_optics_pyat
from xconverters import convert_lattices  
from xconverters import conv_utils
import pytest
from pathlib import Path

def check_attributes(el1, el2):
    el1_dict = el1.__dict__
    el2_dict = el2.__dict__
    for key in el1_dict:
        if isinstance(el1_dict[key], np.ndarray):
            array_1 = np.trim_zeros(el1_dict[key], trim='b')
            array_2 = np.trim_zeros(el2_dict[key], trim='b')
            if len(array_1) != len(array_2):
                answer = False
            arr_eq = np.isclose(array_1, array_2, rtol=1e-10)
            if False in arr_eq:
                answer = False
        elif el1_dict[key] != el2_dict[key]:
            diff = (el2_dict[key] - el1_dict[key])/el1_dict[key]
            if diff > 1e-13:
                answer = False
            else: 
                answer = True
        else:
            answer = True
    return answer
    
madx_lattice = conv_utils.create_cpymad_from_file("../test_sequences/lattice.seq", energy=120)
madx_lattice.command.beam(particle='electron', energy=120)
madx_lattice.use('l000013')

xsequence_lattice = convert_lattices.from_cpymad(madx_lattice, 'l000013', energy=120)
pyat_lattice = convert_lattices.to_pyat(xsequence_lattice)
xsequence_lattice_new = convert_lattices.from_pyat(pyat_lattice)
pyat_lattice_new = convert_lattices.to_pyat(xsequence_lattice_new)

for idx, element in enumerate(pyat_lattice):
    if element.__class__.__name__ != 'Drift':
        assert check_attributes(pyat_lattice[idx], pyat_lattice_new[idx])
