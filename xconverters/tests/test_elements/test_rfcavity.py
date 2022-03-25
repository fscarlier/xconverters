import xsequence.elements as xe
import xsequence.elements_dataclasses as xed
from xconverters.cpymad import cpymad_element_conversion
from xconverters.pyat import pyat_element_conversion
from pytest import mark
from cpymad.madx import Madx



@mark.parametrize('name,    l,   voltage, frequency, lag, energy',
                 [( 'el1', 1.2,     -1.3,       123, 0.2,   320),
                  ( 'el2', 0.2,      1.1,       193, 0.5,   3e9)])
def test_rfcavity(name, l, voltage, frequency, lag, energy):
    q = xe.RFCavity(name, length=l, voltage=voltage, frequency=frequency, lag=lag)
    assert q.name == name
    assert q.length == l
    assert q.voltage == voltage
    assert q.frequency == frequency
    assert q.lag == lag
    
    #CPYMAD
    md = Madx()
    q_conv = cpymad_element_conversion.convert_cpymad_element(cpymad_element_conversion.to_cpymad(q, md))
    assert q == q_conv

    #PYAT
    q = xe.RFCavity(name, length=l, voltage=voltage, frequency=frequency, lag=lag, energy=energy, pyat_data=xed.PyatData(NumIntSteps=10, PassMethod='StrMPoleSymplectic4Pass'))
    pyat_rf = pyat_element_conversion.to_pyat(q)
    assert pyat_rf.FamName == q.name
    assert pyat_rf.Length == q.length
    assert pyat_rf.Voltage == q.voltage * 1e6
    assert pyat_rf.Frequency == q.frequency * 1e6
    assert pyat_rf.TimeLag == q.lag
    assert pyat_rf.Energy == energy * 1e9
    q_pyat = pyat_element_conversion.convert_pyat_element(pyat_rf)
    assert q == q_pyat
