"""
Module conversion_utils.cpymad_element_conversion
------------------
:author: Felix Carlier (fcarlier@cern.ch)
This is a Python3 module with functions for importing and exporting elements from and to cpymad
"""

import xsequence.elements as xe


def get_base_dict(cpymad_element):
    base_dict = {
                'length' : cpymad_element.l,
                'reference_element' : getattr(cpymad_element, 'from'),
                }
    
    if cpymad_element.at < 1e12:
        base_dict.update({
                          'location' : getattr(cpymad_element, 'at'),
                         }) 
    
    if cpymad_element.aperture[0] > 0:
        base_dict.update({
                    'aperture_size' : cpymad_element.aperture,
                    'aperture_type' : cpymad_element.apertype,
                    }) 
    try: 
        lrad = cpymad_element.lrad
        if lrad > 0:
            base_dict.update({
                        'radiation_length' : lrad,
                        }) 
    except: AttributeError

    
    return base_dict 


def convert_marker(cpymad_element, kw):
    return xe.Marker(cpymad_element.name, **kw)
    

def convert_drift(cpymad_element, kw):
    return xe.Drift(cpymad_element.name, **kw)


def convert_collimator(cpymad_element, kw):
    return xe.Collimator(cpymad_element.name, **kw)


def convert_monitor(cpymad_element, kw):
    return xe.Monitor(cpymad_element.name, **kw)


def convert_placeholder(cpymad_element, kw):
    return xe.Placeholder(cpymad_element.name, **kw)


def convert_instrument(cpymad_element, kw):
    return xe.Instrument(cpymad_element.name, **kw)


def convert_sectorbend(cpymad_element, kw):
    kw.update({
                'angle': cpymad_element.angle,
                'k0': cpymad_element.k0,
                'k1': cpymad_element.k1,
                'e1': cpymad_element.e1,
                'e2': cpymad_element.e2,
                })
    return xe.SectorBend(cpymad_element.name, **kw)


def convert_rectangularbend(cpymad_element, kw):
    kw.update({
                'angle': cpymad_element.angle,
                'k0': cpymad_element.k0,
                'k1': cpymad_element.k1,
                'e1': cpymad_element.e1,
                'e2': cpymad_element.e2,
                })
    return xe.RectangularBend(cpymad_element.name, **kw)
    

def convert_dipoleedge(cpymad_element, kw):
    kw.update({
                'h': cpymad_element.h,
                'edge_angle': cpymad_element.e1,
                })
    return xe.DipoleEdge(cpymad_element.name, **kw)


def convert_solenoid(cpymad_element, kw):
    kw.update({
                'ks': cpymad_element.ks,
                'ksi': cpymad_element.ksi,
                })
    return xe.Solenoid(cpymad_element.name, **kw)


def convert_multipole(cpymad_element, kw):
    kw.update({
               'knl': cpymad_element.knl,
               'ksl': cpymad_element.ksl,
               })
    return xe.ThinMultipole(cpymad_element.name, **kw)


def convert_quadrupole(cpymad_element, kw):
    kw.update({
               'k1': cpymad_element.k1,
               'k1s': cpymad_element.k1s,
               })
    return xe.Quadrupole(cpymad_element.name, **kw)


def convert_sextupole(cpymad_element, kw):
    kw.update({
               'k2': cpymad_element.k2,
               'k2s': cpymad_element.k2s,
               })
    return xe.Sextupole(cpymad_element.name, **kw)


def convert_octupole(cpymad_element, kw):
    kw.update({
               'k3': cpymad_element.k3,
               'k3s': cpymad_element.k3s,
               })
    return xe.Octupole(cpymad_element.name, **kw)


def convert_rfcavity(cpymad_element, kw):
    kw.update({
               'voltage': cpymad_element.volt,
               'frequency': cpymad_element.freq, 
               'lag': cpymad_element.lag, 
               })
    return xe.RFCavity(cpymad_element.name, **kw)


def convert_hkicker(cpymad_element, kw):
    kw.update({
               'kick': cpymad_element.kick,
               })
    return xe.HKicker(cpymad_element.name, **kw)


def convert_vkicker(cpymad_element, kw):
    kw.update({
               'kick': cpymad_element.kick,
               })
    return xe.VKicker(cpymad_element.name, **kw)


def convert_tkicker(cpymad_element, kw):
    kw.update({
               'hkick': cpymad_element.hkick,
               'vkick': cpymad_element.vkick,
               })
    return xe.TKicker(cpymad_element.name, **kw)


def convert_thinmultipole(cpymad_element, kw):
    kw.update({
               'knl': cpymad_element.knl, 
               'ksl': cpymad_element.ksl,
               })
    return xe.ThinMultipole(cpymad_element.name, **kw)


def convert_thinsolenoid(cpymad_element, kw):
    kw.update({
               'ks': cpymad_element.ks,  
               'ksi': cpymad_element.ksi,
               })
    return xe.ThinSolenoid(cpymad_element.name, **kw)


def convert_thinrfmultipole(cpymad_element, kw):
    kw.update({
               'voltage': cpymad_element.volt,
               'frequency': cpymad_element.freq, 
               'lag': cpymad_element.lag, 
               })
    return xe.ThinRFMultipole(cpymad_element.name, **kw)


    
