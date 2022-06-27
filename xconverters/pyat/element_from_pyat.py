import at
import numpy as np
import xsequence.elements_dataclasses as xed
import xsequence.elements as xe
from scipy.special import factorial


FACTORIAL = factorial(np.arange(21), exact=True)


def get_aperture_kwargs(pyat_dict):
    kw = dict()
    if 'EApertures' in pyat_dict:
        kw['aperture_data'] = xed.EllipticalAperture(aperture_size=pyat_dict['EApertures'],
                                                             aperture_type='ellipse')
    elif 'RApertures' in pyat_dict:
        kw['aperture_data'] = xed.RectangularAperture(aperture_size=pyat_dict['RApertures'],
                                                             aperture_type='rectangular')
    return kw


def get_methods(pyat_dict):
    method_dict = dict()
    try: method_dict['PassMethod'] = pyat_dict['PassMethod']
    except: AttributeError
    try: method_dict['NumIntSteps'] = pyat_dict['NumIntSteps']
    except: AttributeError
    method = xed.PyatData(**method_dict)
    return method


def convert_marker(pyat_dict):
    kw = get_aperture_kwargs(pyat_dict)
    return xe.Marker(name=pyat_dict['FamName'],
                     **kw)


def convert_drift(pyat_dict):
    kw = get_aperture_kwargs(pyat_dict)
    kw['pyat_data'] = get_methods(pyat_dict)
    return xe.Drift(name=pyat_dict['FamName'],
                    length=pyat_dict['Length'],
                    **kw)


def convert_monitor(pyat_dict):
    kw = get_aperture_kwargs(pyat_dict)
    return xe.Monitor(name=pyat_dict['FamName'],
                     **kw)


def convert_dipole(pyat_dict):
    kw = get_aperture_kwargs(pyat_dict)
    kw['pyat_data'] = get_methods(pyat_dict)
    return xe.SectorBend(name=pyat_dict['FamName'],
                     length=pyat_dict['Length'],
                     angle=pyat_dict['BendingAngle'],
                     e1=pyat_dict['EntranceAngle'],
                     e2=pyat_dict['ExitAngle'],
                     k1=pyat_dict['PolynomB'][1],
                     **kw)


def convert_multipole(pyat_dict):
    knl = pyat_dict['Length'] * pyat_dict['PolynomB']*FACTORIAL[:len(pyat_dict['PolynomB'])]
    ksl = pyat_dict['Length'] * pyat_dict['PolynomA']*FACTORIAL[:len(pyat_dict['PolynomA'])]
    kw = get_aperture_kwargs(pyat_dict)
    kw['pyat_data'] = get_methods(pyat_dict)
    return xe.Multipole(name=pyat_dict['FamName'],
                        length=pyat_dict['Length'],
                        knl=knl,
                        ksl=ksl,
                        **kw)


def convert_quadrupole(pyat_dict):
    kn = pyat_dict['PolynomB']*FACTORIAL[:len(pyat_dict['PolynomB'])]
    ks = pyat_dict['PolynomA']*FACTORIAL[:len(pyat_dict['PolynomA'])]
    kw = get_aperture_kwargs(pyat_dict)
    kw['pyat_data'] = get_methods(pyat_dict)
    return xe.Quadrupole(name=pyat_dict['FamName'],
                        length=pyat_dict['Length'],
                        k1 =kn[1],
                        k1s=ks[1],
                        **kw)


def convert_sextupole(pyat_dict):
    kn = pyat_dict['PolynomB']*FACTORIAL[:len(pyat_dict['PolynomB'])]
    ks = pyat_dict['PolynomA']*FACTORIAL[:len(pyat_dict['PolynomA'])]
    kw = get_aperture_kwargs(pyat_dict)
    kw['pyat_data'] = get_methods(pyat_dict)
    return xe.Sextupole(name=pyat_dict['FamName'],
                        length=pyat_dict['Length'],
                        k2 =kn[2],
                        k2s=ks[2],
                        **kw)


def convert_octupole(pyat_dict):
    kn = pyat_dict['PolynomB']*FACTORIAL[:len(pyat_dict['PolynomB'])]
    ks = pyat_dict['PolynomA']*FACTORIAL[:len(pyat_dict['PolynomA'])]
    kw = get_aperture_kwargs(pyat_dict)
    kw['pyat_data'] = get_methods(pyat_dict)
    return xe.Octupole(name=pyat_dict['FamName'],
                       length=pyat_dict['Length'],
                       k3 =kn[3],
                       k3s=ks[3],
                       **kw)


def convert_rfcavity(pyat_dict):
    kw = get_aperture_kwargs(pyat_dict)
    kw['pyat_data'] = get_methods(pyat_dict)
    return xe.RFCavity(name=pyat_dict['FamName'],
                       length=pyat_dict['Length'],
                       frequency=pyat_dict['Frequency'] / 1e6,
                       voltage=pyat_dict['Voltage'] / 1e6,
                       energy=pyat_dict['Energy'] / 1e9,
                       harmonic_number=pyat_dict['HarmNumber'],
                       lag=pyat_dict['TimeLag'],
                       **kw)


def convert_corrector(pyat_dict):
    kw = get_aperture_kwargs(pyat_dict)
    kw['pyat_data'] = get_methods(pyat_dict)
    return xe.TKicker(name=pyat_dict['FamName'],
                      length=pyat_dict['Length'],
                      hkick=np.sin(pyat_dict['KickAngle'][0]),
                      vkick=np.sin(pyat_dict['KickAngle'][1]),
                      **kw)


def convert_thinmultipole(pyat_dict):
    knl = pyat_dict['PolynomB']*FACTORIAL[:len(pyat_dict['PolynomB'])]
    ksl = pyat_dict['PolynomA']*FACTORIAL[:len(pyat_dict['PolynomA'])]
    kw = get_aperture_kwargs(pyat_dict)
    kw['pyat_data'] = get_methods(pyat_dict)
    return xe.ThinMultipole(name=pyat_dict['FamName'],
                            length=pyat_dict['Length'],
                            knl=knl,
                            ksl=ksl,
                            **kw)

