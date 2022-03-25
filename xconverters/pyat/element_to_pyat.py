import at
import numpy as np
import xsequence.elements_dataclasses as xed
import xsequence.elements as xe
from scipy.special import factorial


FACTORIAL = factorial(np.arange(21), exact=True)
    

def get_aperture_kwargs(xel):
    kw = dict()
    if xel.aperture_data is not None: 
        if isinstance(xel.aperture_data, xed.EllipticalAperture):
            kw['EApertures']=xel.aperture_data.aperture_size 
        elif isinstance(xel.aperture_data, xed.RectangularAperture):
            kw['RApertures']=xel.aperture_data.get_4_array()
        else:
            print('Aperture type not yet convertible to pyat. Please implement..')
    return kw


def convert_marker(xel: xe.Marker):
    kw = get_aperture_kwargs(xel)
    return at.Marker(family_name=xel.name,
                     **kw) 


def convert_drift(xel: xe.Drift):
    kw = get_aperture_kwargs(xel)
    return at.Drift(family_name=xel.name, 
                    length=xel.length,
                    **kw) 


def convert_collimator(xel: xe.Collimator):
    kw = get_aperture_kwargs(xel)
    return at.Drift(family_name=xel.name, 
                    length=xel.length, 
                    **kw) 


def convert_monitor(xel: xe.Monitor):
    kw = get_aperture_kwargs(xel)
    return at.Monitor(family_name=xel.name,
                      **kw) 


def convert_placeholder(xel: xe.Placeholder):
    return convert_drift(xel)


def convert_instrument(xel: xe.Instrument):
    return convert_drift(xel)


def convert_sectorbend(xel: xe.SectorBend):
    kw = get_aperture_kwargs(xel)
    return at.Dipole(family_name=xel.name, 
                     length=xel.length,
                     BendingAngle=xel.angle,
                     EntranceAngle=xel.e1,
                     ExitAngle=xel.e2,
                     k=xel.k1,
                     **kw) 


def convert_rectangularbend(xel: xe.RectangularBend):   
    kw = get_aperture_kwargs(xel)
    return at.Dipole(family_name=xel.name, 
                     length=xel.length,
                     BendingAngle=xel.angle,
                     EntranceAngle=xel.e1,
                     ExitAngle=xel.e2,
                     k=xel.k1,
                     **kw) 


def convert_dipoleedge(xel: xe.DipoleEdge):
    pass


def convert_solenoid(xel: xe.Solenoid):
    pass


def convert_multipole(xel: xe.Multipole):
    poly_a = xel.ks/FACTORIAL[:len(xel.ks)]
    poly_b = xel.kn/FACTORIAL[:len(xel.kn)]
    kw = get_aperture_kwargs(xel)
    return at.Multipole(family_name=xel.name, 
                        length=xel.length,
                        PolynomA=poly_a,
                        PolynomB=poly_b,
                        **kw) 


def convert_quadrupole(xel: xe.Quadrupole):
    poly_a = xel.ks/FACTORIAL[:len(xel.ks)]
    poly_b = xel.kn/FACTORIAL[:len(xel.kn)]
    kw = get_aperture_kwargs(xel)
    return at.Quadrupole(family_name=xel.name, 
                        length=xel.length,
                        PolynomA=poly_a,
                        PolynomB=poly_b,
                        **kw) 


def convert_sextupole(xel: xe.Sextupole):
    poly_a = xel.ks/FACTORIAL[:len(xel.ks)]
    poly_b = xel.kn/FACTORIAL[:len(xel.kn)]
    kw = get_aperture_kwargs(xel)
    return at.Sextupole(family_name=xel.name, 
                        length=xel.length,
                        PolynomA=poly_a,
                        PolynomB=poly_b,
                        **kw) 


def convert_octupole(xel: xe.Octupole):
    poly_a = xel.ks/FACTORIAL[:len(xel.ks)]
    poly_b = xel.kn/FACTORIAL[:len(xel.kn)]
    kw = get_aperture_kwargs(xel)
    return at.Octupole(family_name=xel.name, 
                       length=xel.length,
                       poly_a=poly_a,
                       poly_b=poly_b,
                       **kw) 


def convert_rfcavity(xel: xe.RFCavity):
    kw = get_aperture_kwargs(xel)
    return at.RFCavity(family_name=xel.name, 
                       length=xel.length,
                       frequency=xel.frequency * 1e6,
                       voltage=xel.voltage * 1e6,
                       energy=xel.energy * 1e9,
                       harmonic_number=xel.harmonic_number,
                       TimeLag=xel.lag,
                        **kw) 


def convert_hkicker(xel: xe.HKicker):
    kick_angle = (np.arcsin(xel.kick), 0.0)
    kw = get_aperture_kwargs(xel)
    return at.Corrector(family_name=xel.name, 
                        length=xel.length,
                        kick_angle=kick_angle,
                        **kw) 


def convert_vkicker(xel: xe.VKicker):
    kick_angle = (0.0, np.arcsin(xel.kick))
    kw = get_aperture_kwargs(xel)
    return at.Corrector(family_name=xel.name, 
                        length=xel.length,
                        kick_angle=kick_angle,
                        **kw) 


def convert_tkicker(xel: xe.TKicker):
    kick_angle = (np.arcsin(xel.hkick), np.arcsin(xel.vkick))
    kw = get_aperture_kwargs(xel)
    return at.Corrector(family_name=xel.name, 
                        length=xel.length,
                        kick_angle=kick_angle,
                        **kw) 


def convert_thinmultipole(xel: xe.ThinMultipole):
    poly_a = xel.ksl/FACTORIAL[:len(xel.ksl)]
    poly_b = xel.knl/FACTORIAL[:len(xel.knl)]
    kw = get_aperture_kwargs(xel)
    return at.ThinMultipole(family_name=xel.name, 
                            length=xel.length,
                            poly_a=poly_a,
                            poly_b=poly_b,
                            **kw) 


def convert_thinsolenoid(xel: xe.ThinSolenoid):
    pass


def convert_thinrfmultipole(xel: xe.ThinRFMultipole):
    pass


TO_PYAT = {'Monitor':        convert_monitor         ,          
           'Marker':         convert_marker          ,           
           'Drift':          convert_drift           ,         
           'SectorBend':     convert_sectorbend      ,       
           'RectangularBend':convert_rectangularbend ,  
           'Quadrupole':     convert_quadrupole      , 
           'Sextupole':      convert_sextupole       , 
           'Octupole':       convert_octupole        , 
           'ThinMultipole':  convert_thinmultipole   , 
           'Collimator':     convert_collimator      , 
           'HKicker':        convert_hkicker         , 
           'VKicker':        convert_vkicker         , 
           'TKicker':        convert_tkicker         , 
           'RFCavity':       convert_rfcavity        } 


def to_pyat(xe_element):
    return TO_PYAT[xe_element.__class__.__name__](xe_element)
