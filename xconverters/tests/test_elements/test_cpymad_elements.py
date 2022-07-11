import xsequence.elements as xe
import xsequence.elements_dataclasses as xed
from xconverters.cpymad_utils import convert_cpymad_elements
from xconverters.pyat_utils import convert_pyat_elements
from pytest import mark
from cpymad.madx import Madx





@mark.parametrize('name,  length,   angle,   e1,  e2',
                 [( 'q1',    1.2,    -1.3,  0.3, 0.2),
                  ( 'q2',    1.4,     9.3, -0.3, 0.2),
                  ( 'q3',    1.2,    -1.1, -0.3, 0.2),
                  ( 'q4',    0.2,     0.0,  0.3, 0.2)])
def test_sectorbend(name, length, angle, e1, e2):
    #CPYMAD
    md = Madx()
    q = xe.SectorBend(name, length=length, angle=angle, e1=e1, e2=e2)
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv


@mark.parametrize('name,  length,   angle,   e1,  e2',
                 [( 'q1',    1.2,    -1.3,  0.3, 0.2),
                  ( 'q2',    1.4,     9.3, -0.3, 0.2),
                  ( 'q3',    1.2,    -1.1, -0.3, 0.2),
                  ( 'q4',    0.2,     0.0,  0.3, 0.2)])
def test_rectangularbend(name, length, angle, e1, e2):
    #CPYMAD
    md = Madx()
    q = xe.RectangularBend(name, length=length, angle=angle, e1=e1, e2=e2)
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv


@mark.parametrize('name,    l',
                 [( 'q1', 1.2),
                  ( 'q2', 0.2)])
def test_quadrupole_length(name, l):
    md = Madx()
    q = xe.Quadrupole(name, length=l)
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv


@mark.parametrize('name,    l,   k1',
                 [( 'q1', 1.2, -1.3),
                  ( 'q2', 0.2,  1.1)])
def test_quadrupole_length_k1(name, l, k1):
    md = Madx()
    q = xe.Quadrupole(name, length=l, k1=k1)
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv


@mark.parametrize('name,    l,  k1s',
                 [( 'q1', 1.2, -1.3),
                  ( 'q2', 0.2,  1.1)])
def test_quadrupole_length_k1s(name, l, k1s):
    md = Madx()
    q = xe.Quadrupole(name, length=l, k1s=k1s)
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv


@mark.parametrize('name,    l,   k1,  k1s',
                 [( 'q1', 1.2, -1.3,  1.3),
                  ( 'q2', 1.2,  1.3, -1.3),
                  ( 'q3', 1.2, -1.1, -1.3),
                  ( 'q4', 0.2,  1.1,  1.3)])
def test_quadrupole_length_k1_k1s(name, l, k1, k1s):
    md = Madx()
    q = xe.Quadrupole(name, length=l, k1=k1, k1s=k1s)
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv


@mark.parametrize('name,    l',
                 [( 'q1', 1.2),
                  ( 'q2', 0.2)])
def test_sextupole_length(name, l):
    md = Madx()
    q = xe.Sextupole(name, length=l)
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv


@mark.parametrize('name,    l,   k2',
                 [( 'q1', 1.2, -1.3),
                  ( 'q2', 0.2,  1.1)])
def test_sextupole_length_k2(name, l, k2):
    md = Madx()
    q = xe.Sextupole(name, length=l, k2=k2)
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv


@mark.parametrize('name,    l,  k2s',
                 [( 'q1', 1.2, -1.3),
                  ( 'q2', 0.2,  1.1)])
def test_sextupole_length_k2s(name, l, k2s):
    md = Madx()
    q = xe.Sextupole(name, length=l, k2s=k2s)
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv


@mark.parametrize('name,    l,   k2,  k2s',
                 [( 'q1', 1.2, -1.3,  1.3),
                  ( 'q2', 1.2,  1.3, -1.3),
                  ( 'q3', 1.2, -1.1, -1.3),
                  ( 'q4', 0.2,  1.1,  1.3)])
def test_sextupole_length_k2_k2s(name, l, k2, k2s):
    md = Madx()
    q = xe.Sextupole(name, length=l, k2=k2, k2s=k2s)
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv


@mark.parametrize('name,    l',
                 [( 'q1', 1.2),
                  ( 'q2', 0.2)])
def test_octupole_length(name, l):
    md = Madx()
    q = xe.Octupole(name, length=l)
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv


@mark.parametrize('name,    l,   k3',
                 [( 'q1', 1.2, -1.3),
                  ( 'q2', 0.2,  1.1)])
def test_octupole_length_k3(name, l, k3):
    md = Madx()
    q = xe.Octupole(name, length=l, k3=k3)
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv


@mark.parametrize('name,    l,  k3s',
                 [( 'q1', 1.2, -1.3),
                  ( 'q2', 0.2,  1.1)])
def test_octupole_length_k3s(name, l, k3s):
    md = Madx()
    q = xe.Octupole(name, length=l, k3s=k3s)
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv


@mark.parametrize('name,    l,   k3,  k3s',
                 [( 'q1', 1.2, -1.3,  1.3),
                  ( 'q2', 1.2,  1.3, -1.3),
                  ( 'q3', 1.2, -1.1, -1.3),
                  ( 'q4', 0.2,  1.1,  1.3)])
def test_octupole_length_k3_k3s(name, l, k3, k3s):
    md = Madx()
    q = xe.Octupole(name, length=l, k3=k3, k3s=k3s)
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv


@mark.parametrize('name,    l,   voltage, frequency, lag, energy',
                 [( 'el1', 1.2,     -1.3,       123, 0.2,   320),
                  ( 'el2', 0.2,      1.1,       193, 0.5,   3e9)])
def test_rfcavity(name, l, voltage, frequency, lag, energy):
    md = Madx()
    q = xe.RFCavity(name, length=l, voltage=voltage, frequency=frequency, lag=lag)
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv


