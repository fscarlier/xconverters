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
    q = xe.SectorBend(name, length=length, angle=angle, e1=e1, e2=e2, pyat_data=xed.PyatData(NumIntSteps=10, PassMethod='StrMPoleSymplectic4Pass'))
    pyat_quad = convert_pyat_elements.to_pyat(q)
    assert pyat_quad.FamName == q.name
    assert pyat_quad.Length == q.length
    assert pyat_quad.BendingAngle == q.angle
    assert pyat_quad.EntranceAngle == q.e1
    assert pyat_quad.ExitAngle == q.e2
    q_pyat = convert_pyat_elements.from_pyat(pyat_quad)
    assert q == q_pyat


@mark.parametrize('name,  length,   angle,   e1,  e2',
                 [( 'q1',    1.2,    -1.3,  0.3, 0.2),
                  ( 'q2',    1.4,     9.3, -0.3, 0.2),
                  ( 'q3',    1.2,    -1.1, -0.3, 0.2),
                  ( 'q4',    0.2,     0.0,  0.3, 0.2)])
def test_rectangularbend(name, length, angle, e1, e2):
    q = xe.SectorBend(name, length=length, angle=angle, e1=e1, e2=e2, pyat_data=xed.PyatData(NumIntSteps=10, PassMethod='StrMPoleSymplectic4Pass'))
    pyat_quad = convert_pyat_elements.to_pyat(q)
    assert pyat_quad.FamName == q.name
    assert pyat_quad.Length == q.length
    assert pyat_quad.BendingAngle == q.angle
    assert pyat_quad.EntranceAngle == q.e1
    assert pyat_quad.ExitAngle == q.e2
    q_pyat = convert_pyat_elements.from_pyat(pyat_quad)
    assert q == q_pyat


@mark.parametrize('name,    l',
                 [( 'q1', 1.2),
                  ( 'q2', 0.2)])
def test_quadrupole_length(name, l):
    q = xe.Quadrupole(name, length=l, pyat_data=xed.PyatData(NumIntSteps=10, PassMethod='StrMPoleSymplectic4Pass'))
    pyat_quad = convert_pyat_elements.to_pyat(q)
    assert pyat_quad.FamName == q.name
    assert pyat_quad.Length == q.length
    q_pyat = convert_pyat_elements.from_pyat(pyat_quad)
    assert q == q_pyat


@mark.parametrize('name,    l,   k1',
                 [( 'q1', 1.2, -1.3),
                  ( 'q2', 0.2,  1.1)])
def test_quadrupole_length_k1(name, l, k1):
    q = xe.Quadrupole(name, length=l, k1=k1, pyat_data=xed.PyatData(NumIntSteps=10, PassMethod='StrMPoleSymplectic4Pass'))
    pyat_quad = convert_pyat_elements.to_pyat(q)
    assert pyat_quad.FamName == q.name
    assert pyat_quad.Length == q.length
    assert pyat_quad.K == q.k1
    q_pyat = convert_pyat_elements.from_pyat(pyat_quad)
    assert q == q_pyat


@mark.parametrize('name,    l,  k1s',
                 [( 'q1', 1.2, -1.3),
                  ( 'q2', 0.2,  1.1)])
def test_quadrupole_length_k1s(name, l, k1s):
    q = xe.Quadrupole(name, length=l, k1s=k1s, pyat_data=xed.PyatData(NumIntSteps=10, PassMethod='StrMPoleSymplectic4Pass'))
    pyat_quad = convert_pyat_elements.to_pyat(q)
    assert pyat_quad.FamName == q.name
    assert pyat_quad.Length == q.length
    assert pyat_quad.PolynomA[1] == q.k1s
    q_pyat = convert_pyat_elements.from_pyat(pyat_quad)
    assert q == q_pyat


@mark.parametrize('name,    l,   k1,  k1s',
                 [( 'q1', 1.2, -1.3,  1.3),
                  ( 'q2', 1.2,  1.3, -1.3),
                  ( 'q3', 1.2, -1.1, -1.3),
                  ( 'q4', 0.2,  1.1,  1.3)])
def test_quadrupole_length_k1_k1s(name, l, k1, k1s):
    q = xe.Quadrupole(name, length=l, k1=k1, k1s=k1s, pyat_data=xed.PyatData(NumIntSteps=10, PassMethod='StrMPoleSymplectic4Pass'))
    pyat_quad = convert_pyat_elements.to_pyat(q)
    assert pyat_quad.FamName == q.name
    assert pyat_quad.Length == q.length
    assert pyat_quad.K == q.k1
    q_pyat = convert_pyat_elements.from_pyat(pyat_quad)
    assert q == q_pyat


@mark.parametrize('name,    l',
                 [( 'q1', 1.2),
                  ( 'q2', 0.2)])
def test_sextupole_length(name, l):
    q = xe.Sextupole(name, length=l, pyat_data=xed.PyatData(NumIntSteps=10, PassMethod='StrMPoleSymplectic4Pass'))
    pyat_sext = convert_pyat_elements.to_pyat(q)
    assert pyat_sext.FamName == q.name
    assert pyat_sext.Length == q.length
    q_pyat = convert_pyat_elements.from_pyat(pyat_sext)
    assert q == q_pyat


@mark.parametrize('name,    l,   k2',
                 [( 'q1', 1.2, -1.3),
                  ( 'q2', 0.2,  1.1)])
def test_sextupole_length_k2(name, l, k2):
    q = xe.Sextupole(name, length=l, k2=k2, pyat_data=xed.PyatData(NumIntSteps=10, PassMethod='StrMPoleSymplectic4Pass'))
    pyat_sext = convert_pyat_elements.to_pyat(q)
    assert pyat_sext.FamName == q.name
    assert pyat_sext.Length == q.length
    assert pyat_sext.H*2. == q.k2
    q_pyat = convert_pyat_elements.from_pyat(pyat_sext)
    assert q == q_pyat


@mark.parametrize('name,    l,  k2s',
                 [( 'q1', 1.2, -1.3),
                  ( 'q2', 0.2,  1.1)])
def test_sextupole_length_k2s(name, l, k2s):
    q = xe.Sextupole(name, length=l, k2s=k2s, pyat_data=xed.PyatData(NumIntSteps=10, PassMethod='StrMPoleSymplectic4Pass'))
    pyat_sext = convert_pyat_elements.to_pyat(q)
    assert pyat_sext.FamName == q.name
    assert pyat_sext.Length == q.length
    assert pyat_sext.PolynomA[2]*2. == q.k2s
    q_pyat = convert_pyat_elements.from_pyat(pyat_sext)
    assert q == q_pyat


@mark.parametrize('name,    l,   k2,  k2s',
                 [( 'q1', 1.2, -1.3,  1.3),
                  ( 'q2', 1.2,  1.3, -1.3),
                  ( 'q3', 1.2, -1.1, -1.3),
                  ( 'q4', 0.2,  1.1,  1.3)])
def test_sextupole_length_k2_k2s(name, l, k2, k2s):
    q = xe.Sextupole(name, length=l, k2=k2, k2s=k2s, pyat_data=xed.PyatData(NumIntSteps=10, PassMethod='StrMPoleSymplectic4Pass'))
    pyat_sext = convert_pyat_elements.to_pyat(q)
    assert pyat_sext.FamName == q.name
    assert pyat_sext.Length == q.length
    assert pyat_sext.H*2. == q.k2
    q_pyat = convert_pyat_elements.from_pyat(pyat_sext)
    assert q == q_pyat


@mark.parametrize('name,    l',
                 [( 'q1', 1.2),
                  ( 'q2', 0.2)])
def test_octupole_length(name, l):
    q = xe.Octupole(name, length=l, pyat_data=xed.PyatData(NumIntSteps=10, PassMethod='StrMPoleSymplectic4Pass'))
    pyat_oct = convert_pyat_elements.to_pyat(q)
    assert pyat_oct.FamName == q.name
    assert pyat_oct.Length == q.length
    q_pyat = convert_pyat_elements.from_pyat(pyat_oct)
    assert q == q_pyat



@mark.parametrize('name,    l,   k3',
                 [( 'q1', 1.2, -1.3),
                  ( 'q2', 0.2,  1.1)])
def test_octupole_length_k3(name, l, k3):
    q = xe.Octupole(name, length=l, k3=k3, pyat_data=xed.PyatData(NumIntSteps=10, PassMethod='StrMPoleSymplectic4Pass'))
    pyat_oct = convert_pyat_elements.to_pyat(q)
    assert pyat_oct.FamName == q.name
    assert pyat_oct.Length == q.length
    q_pyat = convert_pyat_elements.from_pyat(pyat_oct)
    assert q == q_pyat



@mark.parametrize('name,    l,  k3s',
                 [( 'q1', 1.2, -1.3),
                  ( 'q2', 0.2,  1.1)])
def test_octupole_length_k3s(name, l, k3s):
    q = xe.Octupole(name, length=l, k3s=k3s, pyat_data=xed.PyatData(NumIntSteps=10, PassMethod='StrMPoleSymplectic4Pass'))
    pyat_oct = convert_pyat_elements.to_pyat(q)
    assert pyat_oct.FamName == q.name
    assert pyat_oct.Length == q.length
    assert pyat_oct.PolynomA[3]*6. == q.k3s
    q_pyat = convert_pyat_elements.from_pyat(pyat_oct)
    assert q == q_pyat



@mark.parametrize('name,    l,   k3,  k3s',
                 [( 'q1', 1.2, -1.3,  1.3),
                  ( 'q2', 1.2,  1.3, -1.3),
                  ( 'q3', 1.2, -1.1, -1.3),
                  ( 'q4', 0.2,  1.1,  1.3)])
def test_octupole_length_k3_k3s(name, l, k3, k3s):
    q = xe.Octupole(name, length=l, k3=k3, k3s=k3s, pyat_data=xed.PyatData(NumIntSteps=10, PassMethod='StrMPoleSymplectic4Pass'))
    pyat_oct = convert_pyat_elements.to_pyat(q)
    assert pyat_oct.FamName == q.name
    assert pyat_oct.Length == q.length
    q_pyat = convert_pyat_elements.from_pyat(pyat_oct)
    assert q == q_pyat


@mark.parametrize('name,    l,   voltage, frequency, lag, energy',
                 [( 'el1', 1.2,     -1.3,       123, 0.2,   320),
                  ( 'el2', 0.2,      1.1,       193, 0.5,   3e9)])
def test_rfcavity(name, l, voltage, frequency, lag, energy):
    q = xe.RFCavity(name, length=l, voltage=voltage, frequency=frequency, lag=lag, energy=energy, pyat_data=xed.PyatData(NumIntSteps=10, PassMethod='StrMPoleSymplectic4Pass'))
    pyat_rf = convert_pyat_elements.to_pyat(q)
    assert pyat_rf.FamName == q.name
    assert pyat_rf.Length == q.length
    assert pyat_rf.Voltage == q.voltage * 1e6
    assert pyat_rf.Frequency == q.frequency * 1e6
    assert pyat_rf.TimeLag == q.lag
    assert pyat_rf.Energy == energy * 1e9
    q_pyat = convert_pyat_elements.from_pyat(pyat_rf)
    assert q == q_pyat
