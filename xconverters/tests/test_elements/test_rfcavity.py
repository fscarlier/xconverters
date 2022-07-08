import xsequence.elements as xe
import xsequence.elements_dataclasses as xed
from xconverters.cpymad_utils import convert_cpymad_elements
from xconverters.pyat_utils import convert_pyat_elements
from pytest import mark
from cpymad.madx import Madx



@mark.parametrize('name,    l,   voltage, frequency, lag, energy',
                 [( 'el1', 1.2,     -1.3,       123, 0.2,   320),
                  ( 'el2', 0.2,      1.1,       193, 0.5,   3e9)])
def test_rfcavity(name, l, voltage, frequency, lag, energy):
    #CPYMAD
    md = Madx()
    q = xe.RFCavity(name, length=l, voltage=voltage, frequency=frequency, lag=lag)
    q_conv = convert_cpymad_elements.from_cpymad(convert_cpymad_elements.to_cpymad(md, q))
    assert q == q_conv

    #PYAT
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
