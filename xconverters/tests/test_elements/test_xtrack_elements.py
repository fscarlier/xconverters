import numpy as np
import xsequence.elements as xe
from xconverters.xtrack_utils import convert_xtrack_elements
from pytest import mark
from cpymad.madx import Madx

def equal_arrays(array_1, array_2):
    array_1 = np.trim_zeros(array_1, trim='b')
    array_2 = np.trim_zeros(array_2, trim='b')
    if len(array_1) != len(array_2):
        return False
    arr_eq = np.isclose(array_1, array_2, rtol=1e-8)
    if False in arr_eq:
        return False

    return True


@mark.parametrize('length',
                 [(   1.2),
                  (   1.4),
                  (   1.2),
                  (   0.2)])
def test_drift(length):
    el = xe.Drift('drift', length=length)
    xtrack_element = convert_xtrack_elements.to_xtrack(el)
    assert xtrack_element.length == el.length
    el_xtrack = convert_xtrack_elements.from_xtrack(xtrack_element)
    assert el_xtrack.length == el.length


@mark.parametrize('knl,                 ksl,                 rad_length'            ,
                 [(np.random.random(4), np.random.random(4), np.random.random(1)[0]),
                  (np.random.random(4), np.random.random(4), np.random.random(1)[0]),
                  (np.random.random(6), np.random.random(4), np.random.random(1)[0]),
                  (np.random.random(2), np.random.random(3), np.random.random(1)[0])])
def test_multipole(knl, ksl, rad_length):
    el = xe.ThinMultipole('mult', knl=knl, ksl=ksl, radiation_length=rad_length)
    xtrack_element = convert_xtrack_elements.to_xtrack(el)
    assert xtrack_element.length == el.radiation_length
    assert equal_arrays(xtrack_element.knl, el.knl)
    assert equal_arrays(xtrack_element.ksl, el.ksl)
    el_xtrack = convert_xtrack_elements.from_xtrack(xtrack_element)
    assert el_xtrack.radiation_length == el.radiation_length
    assert equal_arrays(el_xtrack.knl, el.knl)
    assert equal_arrays(el_xtrack.ksl, el.ksl)


@mark.parametrize('h,  edge_angle ',
                 [( 1.2,  0.4),
                  ( 0.2, -0.4),
                  (-1.2,  2.4),
                  ( 3.2,  2.3)])
def test_dipedge(h, edge_angle):
    el = xe.DipoleEdge('dipedge', h=h, edge_angle=edge_angle)
    xtrack_element = convert_xtrack_elements.to_xtrack(el)
    assert xtrack_element.h == el.h
    assert xtrack_element.e1 == el.edge_angle
    el_xtrack = convert_xtrack_elements.from_xtrack(xtrack_element)
    assert el_xtrack.h == el.h
    assert el_xtrack.edge_angle == el.edge_angle


