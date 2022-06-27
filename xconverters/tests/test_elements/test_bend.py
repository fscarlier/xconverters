import xsequence.elements as xe
import xsequence.elements_dataclasses as xed
from xconverters.cpymad import convert_cpymad_elements
from xconverters.pyat import convert_pyat_elements
from pytest import mark
from cpymad.madx import Madx





@mark.parametrize('name,  length,   angle,   e1,  e2',
                 [( 'q1',    1.2,    -1.3,  0.3, 0.2),
                  ( 'q2',    1.4,     9.3, -0.3, 0.2),
                  ( 'q3',    1.2,    -1.1, -0.3, 0.2),
                  ( 'q4',    0.2,     0.0,  0.3, 0.2)])
def test_sectorbend(name, length, angle, e1, e2):
    q = xe.SectorBend(name, length=length, angle=angle, e1=e1, e2=e2)
    assert q.name == name
    assert q.length == length
    assert q.angle == angle
    assert q.e1 == e1
    assert q.e2 == e2

    #CPYMAD
    md = Madx()
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv

    #PYAT
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
    q = xe.RectangularBend(name, length=length, angle=angle, e1=e1, e2=e2)
    assert q.name == name
    assert q._chord_length == length
    assert q.angle == angle
    assert q._rbend_e1 == e1
    assert q._rbend_e2 == e2

    #CPYMAD
    md = Madx()
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv

    #PYAT
    q = xe.SectorBend(name, length=length, angle=angle, e1=e1, e2=e2, pyat_data=xed.PyatData(NumIntSteps=10, PassMethod='StrMPoleSymplectic4Pass'))
    pyat_quad = convert_pyat_elements.to_pyat(q)
    assert pyat_quad.FamName == q.name
    assert pyat_quad.Length == q.length
    assert pyat_quad.BendingAngle == q.angle
    assert pyat_quad.EntranceAngle == q.e1
    assert pyat_quad.ExitAngle == q.e2
    q_pyat = convert_pyat_elements.from_pyat(pyat_quad)
    assert q == q_pyat

