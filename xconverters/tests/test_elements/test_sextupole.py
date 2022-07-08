import xsequence.elements as xe
import xsequence.elements_dataclasses as xed
from xconverters.cpymad_utils import convert_cpymad_elements
from xconverters.pyat_utils import convert_pyat_elements
from pytest import mark
from cpymad.madx import Madx

@mark.parametrize('name,    l',
                 [( 'q1', 1.2),
                  ( 'q2', 0.2)])
def test_sextupole_length(name, l):
    #CPYMAD
    md = Madx()
    q = xe.Sextupole(name, length=l)
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv

    #PYAT
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
    #CPYMAD
    md = Madx()
    q = xe.Sextupole(name, length=l, k2=k2)
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv

    #PYAT
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
    #CPYMAD
    md = Madx()
    q = xe.Sextupole(name, length=l, k2s=k2s)
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv

    #PYAT
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
    #CPYMAD
    md = Madx()
    q = xe.Sextupole(name, length=l, k2=k2, k2s=k2s)
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv

    #PYAT
    q = xe.Sextupole(name, length=l, k2=k2, k2s=k2s, pyat_data=xed.PyatData(NumIntSteps=10, PassMethod='StrMPoleSymplectic4Pass'))
    pyat_sext = convert_pyat_elements.to_pyat(q)
    assert pyat_sext.FamName == q.name
    assert pyat_sext.Length == q.length
    assert pyat_sext.H*2. == q.k2
    q_pyat = convert_pyat_elements.from_pyat(pyat_sext)
    assert q == q_pyat


