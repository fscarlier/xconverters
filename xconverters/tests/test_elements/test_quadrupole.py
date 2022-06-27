import xsequence.elements as xe
import xsequence.elements_dataclasses as xed
from xconverters.cpymad import convert_cpymad_elements
from xconverters.pyat import convert_pyat_elements
from pytest import mark
from cpymad.madx import Madx

@mark.parametrize('name,    l',
                 [( 'q1', 1.2),
                  ( 'q2', 0.2)])
def test_quadrupole_length(name, l):
    q = xe.Quadrupole(name, length=l)
    assert q.name == name
    assert q.length == l

    #CPYMAD
    md = Madx()
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv

    #PYAT
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
    q = xe.Quadrupole(name, length=l, k1=k1)
    assert q.name == name
    assert q.length == l
    assert q.k1 == k1

    #CPYMAD
    md = Madx()
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv

    #PYAT
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
    q = xe.Quadrupole(name, length=l, k1s=k1s)
    assert q.name == name
    assert q.length == l
    assert q.k1s == k1s

    #CPYMAD
    md = Madx()
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv

    #PYAT
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
    q = xe.Quadrupole(name, length=l, k1=k1, k1s=k1s)
    assert q.name == name
    assert q.length == l
    assert q.k1 == k1
    assert q.k1s == k1s

    #CPYMAD
    md = Madx()
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv

    #PYAT
    q = xe.Quadrupole(name, length=l, k1=k1, k1s=k1s, pyat_data=xed.PyatData(NumIntSteps=10, PassMethod='StrMPoleSymplectic4Pass'))
    pyat_quad = convert_pyat_elements.to_pyat(q)
    assert pyat_quad.FamName == q.name
    assert pyat_quad.Length == q.length
    assert pyat_quad.K == q.k1
    q_pyat = convert_pyat_elements.from_pyat(pyat_quad)
    assert q == q_pyat

