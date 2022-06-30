# copyright #################################### #
# This file is part of the Xconverters Package.  #
# Copyright (c) CERN, 2022.                      #
# ############################################## #


import at
import numpy as np
import xsequence.elements as xe
import xsequence.elements_dataclasses as xed
from scipy.special import factorial


FACTORIAL = factorial(np.arange(21), exact=True)


"""
Export elements to pyat
"""


def get_aperture_kwargs_from_pyat(pyat_dict):
    kw = dict()
    if 'EApertures' in pyat_dict:
        kw['aperture_data'] = xed.EllipticalAperture(aperture_size=pyat_dict['EApertures'],
                                                             aperture_type='ellipse')
    elif 'RApertures' in pyat_dict:
        kw['aperture_data'] = xed.RectangularAperture(aperture_size=pyat_dict['RApertures'],
                                                             aperture_type='rectangular')
    return kw


def get_methods_from_pyat(pyat_dict):
    method_dict = dict()
    try: method_dict['PassMethod'] = pyat_dict['PassMethod']
    except: AttributeError
    try: method_dict['NumIntSteps'] = pyat_dict['NumIntSteps']
    except: AttributeError
    method = xed.PyatData(**method_dict)
    return method


def convert_marker_from_pyat(pyat_dict):
    kw = get_aperture_kwargs_from_pyat(pyat_dict)
    return xe.Marker(name=pyat_dict['FamName'],
                     **kw)


def convert_drift_from_pyat(pyat_dict):
    kw = get_aperture_kwargs_from_pyat(pyat_dict)
    kw['pyat_data'] = get_methods_from_pyat(pyat_dict)
    return xe.Drift(name=pyat_dict['FamName'],
                    length=pyat_dict['Length'],
                    **kw)


def convert_monitor_from_pyat(pyat_dict):
    kw = get_aperture_kwargs_from_pyat(pyat_dict)
    return xe.Monitor(name=pyat_dict['FamName'],
                     **kw)


def convert_dipole_from_pyat(pyat_dict):
    kw = get_aperture_kwargs_from_pyat(pyat_dict)
    kw['pyat_data'] = get_methods_from_pyat(pyat_dict)
    return xe.SectorBend(name=pyat_dict['FamName'],
                     length=pyat_dict['Length'],
                     angle=pyat_dict['BendingAngle'],
                     e1=pyat_dict['EntranceAngle'],
                     e2=pyat_dict['ExitAngle'],
                     k1=pyat_dict['PolynomB'][1],
                     **kw)


def convert_multipole_from_pyat(pyat_dict):
    knl = pyat_dict['Length'] * pyat_dict['PolynomB']*FACTORIAL[:len(pyat_dict['PolynomB'])]
    ksl = pyat_dict['Length'] * pyat_dict['PolynomA']*FACTORIAL[:len(pyat_dict['PolynomA'])]
    kw = get_aperture_kwargs_from_pyat(pyat_dict)
    kw['pyat_data'] = get_methods_from_pyat(pyat_dict)
    return xe.Multipole(name=pyat_dict['FamName'],
                        length=pyat_dict['Length'],
                        knl=knl,
                        ksl=ksl,
                        **kw)


def convert_quadrupole_from_pyat(pyat_dict):
    kn = pyat_dict['PolynomB']*FACTORIAL[:len(pyat_dict['PolynomB'])]
    ks = pyat_dict['PolynomA']*FACTORIAL[:len(pyat_dict['PolynomA'])]
    kw = get_aperture_kwargs_from_pyat(pyat_dict)
    kw['pyat_data'] = get_methods_from_pyat(pyat_dict)
    return xe.Quadrupole(name=pyat_dict['FamName'],
                        length=pyat_dict['Length'],
                        k1 =kn[1],
                        k1s=ks[1],
                        **kw)


def convert_sextupole_from_pyat(pyat_dict):
    kn = pyat_dict['PolynomB']*FACTORIAL[:len(pyat_dict['PolynomB'])]
    ks = pyat_dict['PolynomA']*FACTORIAL[:len(pyat_dict['PolynomA'])]
    kw = get_aperture_kwargs_from_pyat(pyat_dict)
    kw['pyat_data'] = get_methods_from_pyat(pyat_dict)
    return xe.Sextupole(name=pyat_dict['FamName'],
                        length=pyat_dict['Length'],
                        k2 =kn[2],
                        k2s=ks[2],
                        **kw)


def convert_octupole_from_pyat(pyat_dict):
    kn = pyat_dict['PolynomB']*FACTORIAL[:len(pyat_dict['PolynomB'])]
    ks = pyat_dict['PolynomA']*FACTORIAL[:len(pyat_dict['PolynomA'])]
    kw = get_aperture_kwargs_from_pyat(pyat_dict)
    kw['pyat_data'] = get_methods_from_pyat(pyat_dict)
    return xe.Octupole(name=pyat_dict['FamName'],
                       length=pyat_dict['Length'],
                       k3 =kn[3],
                       k3s=ks[3],
                       **kw)


def convert_rfcavity_from_pyat(pyat_dict):
    kw = get_aperture_kwargs_from_pyat(pyat_dict)
    kw['pyat_data'] = get_methods_from_pyat(pyat_dict)
    return xe.RFCavity(name=pyat_dict['FamName'],
                       length=pyat_dict['Length'],
                       frequency=pyat_dict['Frequency'] / 1e6,
                       voltage=pyat_dict['Voltage'] / 1e6,
                       energy=pyat_dict['Energy'] / 1e9,
                       harmonic_number=pyat_dict['HarmNumber'],
                       lag=pyat_dict['TimeLag'],
                       **kw)


def convert_corrector_from_pyat(pyat_dict):
    kw = get_aperture_kwargs_from_pyat(pyat_dict)
    kw['pyat_data'] = get_methods_from_pyat(pyat_dict)
    return xe.TKicker(name=pyat_dict['FamName'],
                      length=pyat_dict['Length'],
                      hkick=np.sin(pyat_dict['KickAngle'][0]),
                      vkick=np.sin(pyat_dict['KickAngle'][1]),
                      **kw)


def convert_thinmultipole_from_pyat(pyat_dict):
    knl = pyat_dict['PolynomB']*FACTORIAL[:len(pyat_dict['PolynomB'])]
    ksl = pyat_dict['PolynomA']*FACTORIAL[:len(pyat_dict['PolynomA'])]
    kw = get_aperture_kwargs_from_pyat(pyat_dict)
    kw['pyat_data'] = get_methods_from_pyat(pyat_dict)
    return xe.ThinMultipole(name=pyat_dict['FamName'],
                            length=pyat_dict['Length'],
                            knl=knl,
                            ksl=ksl,
                            **kw)



FROM_PYAT = {'Monitor':        convert_monitor_from_pyat       ,
             'Marker':         convert_marker_from_pyat        ,
             'Drift':          convert_drift_from_pyat         ,
             'Dipole':         convert_dipole_from_pyat        ,
             'Quadrupole':     convert_quadrupole_from_pyat    ,
             'Sextupole':      convert_sextupole_from_pyat     ,
             'Octupole':       convert_octupole_from_pyat      ,
             'ThinMultipole':  convert_thinmultipole_from_pyat ,
             'Corrector':      convert_corrector_from_pyat     ,
             'RFCavity':       convert_rfcavity_from_pyat      }


def from_pyat(pyat_element):
    pyat_dict = pyat_element.__dict__
    return FROM_PYAT[pyat_element.__class__.__name__](pyat_dict)


"""
Export elements to pyat
"""


def get_aperture_kwargs_to_pyat(xel):
    kw = dict()
    if xel.aperture_data is not None:
        if isinstance(xel.aperture_data, xed.EllipticalAperture):
            kw['EApertures']=xel.aperture_data.aperture_size
        elif isinstance(xel.aperture_data, xed.RectangularAperture):
            kw['RApertures']=xel.aperture_data.get_4_array()
        else:
            print('Aperture type not yet convertible to pyat. Please implement..')
    return kw



def get_pass_method_to_pyat(xel):
    method = dict()
    if xel.pyat_data != None:
        if xel.pyat_data.PassMethod:
            method['PassMethod'] = xel.pyat_data.PassMethod
        if xel.pyat_data.NumIntSteps:
            method['NumIntSteps'] = xel.pyat_data.NumIntSteps
    return method


def convert_marker_to_pyat(xel: xe.Marker):
    kw = get_aperture_kwargs_to_pyat(xel)
    return at.Marker(family_name=xel.name,
                     **kw)


def convert_drift_to_pyat(xel: xe.Drift):
    kw = get_aperture_kwargs_to_pyat(xel)
    return at.Drift(family_name=xel.name,
                    length=xel.length,
                    **kw)


def convert_collimator_to_pyat(xel: xe.Collimator):
    kw = get_aperture_kwargs_to_pyat(xel)
    kw.update(get_pass_method_to_pyat(xel))
    return at.Drift(family_name=xel.name,
                    length=xel.length,
                    **kw)


def convert_monitor_to_pyat(xel: xe.Monitor):
    kw = get_aperture_kwargs_to_pyat(xel)
    return at.Monitor(family_name=xel.name,
                      **kw)


def convert_placeholder_to_pyat(xel: xe.Placeholder):
    return convert_drift(xel)


def convert_instrument_to_pyat(xel: xe.Instrument):
    return convert_drift(xel)


def convert_sectorbend_to_pyat(xel: xe.SectorBend):
    kw = get_aperture_kwargs_to_pyat(xel)
    kw.update(get_pass_method_to_pyat(xel))
    return at.Dipole(family_name=xel.name,
                     length=xel.length,
                     BendingAngle=xel.angle,
                     EntranceAngle=xel.e1,
                     ExitAngle=xel.e2,
                     k=xel.k1,
                     **kw)


def convert_rectangularbend_to_pyat(xel: xe.RectangularBend):
    kw = get_aperture_kwargs_to_pyat(xel)
    kw.update(get_pass_method_to_pyat(xel))
    return at.Dipole(family_name=xel.name,
                     length=xel.length,
                     BendingAngle=xel.angle,
                     EntranceAngle=xel.e1,
                     ExitAngle=xel.e2,
                     k=xel.k1,
                     **kw)


def convert_dipoleedge_to_pyat(xel: xe.DipoleEdge):
    pass


def convert_solenoid_to_pyat(xel: xe.Solenoid):
    pass


def convert_multipole_to_pyat(xel: xe.Multipole):
    poly_a = xel.ks/FACTORIAL[:len(xel.ks)]
    poly_b = xel.kn/FACTORIAL[:len(xel.kn)]
    kw = get_aperture_kwargs_to_pyat(xel)
    kw.update(get_pass_method_to_pyat(xel))
    return at.Multipole(family_name=xel.name,
                        length=xel.length,
                        PolynomA=poly_a,
                        PolynomB=poly_b,
                        **kw)


def convert_quadrupole_to_pyat(xel: xe.Quadrupole):
    poly_a = xel.ks/FACTORIAL[:len(xel.ks)]
    poly_b = xel.kn/FACTORIAL[:len(xel.kn)]
    kw = get_aperture_kwargs_to_pyat(xel)
    kw.update(get_pass_method_to_pyat(xel))
    return at.Quadrupole(family_name=xel.name,
                        length=xel.length,
                        PolynomA=poly_a,
                        PolynomB=poly_b,
                        **kw)


def convert_sextupole_to_pyat(xel: xe.Sextupole):
    poly_a = xel.ks/FACTORIAL[:len(xel.ks)]
    poly_b = xel.kn/FACTORIAL[:len(xel.kn)]
    kw = get_aperture_kwargs_to_pyat(xel)
    kw.update(get_pass_method_to_pyat(xel))
    return at.Sextupole(family_name=xel.name,
                        length=xel.length,
                        PolynomA=poly_a,
                        PolynomB=poly_b,
                        **kw)


def convert_octupole_to_pyat(xel: xe.Octupole):
    poly_a = xel.ks/FACTORIAL[:len(xel.ks)]
    poly_b = xel.kn/FACTORIAL[:len(xel.kn)]
    kw = get_aperture_kwargs_to_pyat(xel)
    kw.update(get_pass_method_to_pyat(xel))
    return at.Octupole(family_name=xel.name,
                       length=xel.length,
                       poly_a=poly_a,
                       poly_b=poly_b,
                       **kw)


def convert_rfcavity_to_pyat(xel: xe.RFCavity):
    kw = get_aperture_kwargs_to_pyat(xel)
    kw.update(get_pass_method_to_pyat(xel))
    return at.RFCavity(family_name=xel.name,
                       length=xel.length,
                       frequency=xel.frequency * 1e6,
                       voltage=xel.voltage * 1e6,
                       energy=xel.energy * 1e9,
                       harmonic_number=xel.harmonic_number,
                       TimeLag=xel.lag,
                        **kw)


def convert_hkicker_to_pyat(xel: xe.HKicker):
    kick_angle = (np.arcsin(xel.kick), 0.0)
    kw = get_aperture_kwargs_to_pyat(xel)
    kw.update(get_pass_method_to_pyat(xel))
    return at.Corrector(family_name=xel.name,
                        length=xel.length,
                        kick_angle=kick_angle,
                        **kw)


def convert_vkicker_to_pyat(xel: xe.VKicker):
    kick_angle = (0.0, np.arcsin(xel.kick))
    kw = get_aperture_kwargs_to_pyat(xel)
    kw.update(get_pass_method_to_pyat(xel))
    return at.Corrector(family_name=xel.name,
                        length=xel.length,
                        kick_angle=kick_angle,
                        **kw)


def convert_tkicker_to_pyat(xel: xe.TKicker):
    kick_angle = (np.arcsin(xel.hkick), np.arcsin(xel.vkick))
    kw = get_aperture_kwargs_to_pyat(xel)
    kw.update(get_pass_method_to_pyat(xel))
    return at.Corrector(family_name=xel.name,
                        length=xel.length,
                        kick_angle=kick_angle,
                        **kw)


def convert_thinmultipole_to_pyat(xel: xe.ThinMultipole):
    poly_a = xel.ksl/FACTORIAL[:len(xel.ksl)]
    poly_b = xel.knl/FACTORIAL[:len(xel.knl)]
    kw = get_aperture_kwargs_to_pyat(xel)
    kw.update(get_pass_method_to_pyat(xel))
    return at.ThinMultipole(family_name=xel.name,
                            length=xel.length,
                            poly_a=poly_a,
                            poly_b=poly_b,
                            **kw)


def convert_thinsolenoid_to_pyat(xel: xe.ThinSolenoid):
    pass


def convert_thinrfmultipole_to_pyat(xel: xe.ThinRFMultipole):
    pass


TO_PYAT = {'Monitor':         convert_monitor_to_pyat         ,
           'Marker':          convert_marker_to_pyat          ,
           'Drift':           convert_drift_to_pyat           ,
           'SectorBend':      convert_sectorbend_to_pyat      ,
           'RectangularBend': convert_rectangularbend_to_pyat ,
           'Quadrupole':      convert_quadrupole_to_pyat      ,
           'Sextupole':       convert_sextupole_to_pyat       ,
           'Octupole':        convert_octupole_to_pyat        ,
           'ThinMultipole':   convert_thinmultipole_to_pyat   ,
           'Collimator':      convert_collimator_to_pyat      ,
           'HKicker':         convert_hkicker_to_pyat         ,
           'VKicker':         convert_vkicker_to_pyat         ,
           'TKicker':         convert_tkicker_to_pyat         ,
           'RFCavity':        convert_rfcavity_to_pyat        }


def to_pyat(xe_element):
    return TO_PYAT[xe_element.__class__.__name__](xe_element)
