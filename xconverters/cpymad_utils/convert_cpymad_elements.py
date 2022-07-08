# copyright #################################### #
# This file is part of the Xconverters Package.  #
# Copyright (c) CERN, 2022.                      #
# ############################################## #

import cpymad.madx as Madx
import xsequence.elements as xe

# Element attribute dicts; {xsequence:cpymad}
# Currently used for dependency translation

REQ_ATTR = {'length':'l',
            'reference_element':'from',
            'location':'at',
            'aperture_size':'aperture',
            'aperture_type':'apertype',
            'radiation_length':'lrad',
            'angle': 'angle',
            'e1': 'e1',
            'e2': 'e2',
            'edge_angle': 'e1',
            'h': 'h',
            'k0': 'k0',
            'k1': 'k1',
            'k1s': 'k1s',
            'k2': 'k2',
            'k2s': 'k2s',
            'k3': 'k3',
            'k3s': 'k3s',
            'knl': 'knl',
            'ksl': 'ksl',
            'ks': 'ks',
            'ksi': 'ksi',
            'voltage': 'volt',
            'frequency': 'freq',
            'lag': 'lag',
            'kick': 'kick',
            'hkick': 'hkick',
            'vkick': 'vkick'}

REQ_ATTR_INVERTED = {val: key for key, val in REQ_ATTR.items()}


"""
Import functions from cpymad
"""

def get_base_dict_from_cpymad(cpymad_element):
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


def convert_marker_from_cpymad(cpymad_element, kw):
    return xe.Marker(cpymad_element.name, **kw)


def convert_drift_from_cpymad(cpymad_element, kw):
    return xe.Drift(cpymad_element.name, **kw)


def convert_collimator_from_cpymad(cpymad_element, kw):
    return xe.Collimator(cpymad_element.name, **kw)


def convert_monitor_from_cpymad(cpymad_element, kw):
    return xe.Monitor(cpymad_element.name, **kw)


def convert_placeholder_from_cpymad(cpymad_element, kw):
    return xe.Placeholder(cpymad_element.name, **kw)


def convert_instrument_from_cpymad(cpymad_element, kw):
    return xe.Instrument(cpymad_element.name, **kw)


def convert_sectorbend_from_cpymad(cpymad_element, kw):
    kw.update({
                'angle': cpymad_element.angle,
                'k0': cpymad_element.k0,
                'k1': cpymad_element.k1,
                'e1': cpymad_element.e1,
                'e2': cpymad_element.e2,
                })
    return xe.SectorBend(cpymad_element.name, **kw)


def convert_rectangularbend_from_cpymad(cpymad_element, kw):
    kw.update({
                'angle': cpymad_element.angle,
                'k0': cpymad_element.k0,
                'k1': cpymad_element.k1,
                'e1': cpymad_element.e1,
                'e2': cpymad_element.e2,
                })
    return xe.RectangularBend(cpymad_element.name, **kw)


def convert_dipoleedge_from_cpymad(cpymad_element, kw):
    kw.update({
                'h': cpymad_element.h,
                'edge_angle': cpymad_element.e1,
                })
    return xe.DipoleEdge(cpymad_element.name, **kw)


def convert_solenoid_from_cpymad(cpymad_element, kw):
    kw.update({
                'ks': cpymad_element.ks,
                'ksi': cpymad_element.ksi,
                })
    return xe.Solenoid(cpymad_element.name, **kw)


def convert_multipole_from_cpymad(cpymad_element, kw):
    kw.update({
               'knl': cpymad_element.knl,
               'ksl': cpymad_element.ksl,
               })
    return xe.ThinMultipole(cpymad_element.name, **kw)


def convert_quadrupole_from_cpymad(cpymad_element, kw):
    kw.update({
               'k1': cpymad_element.k1,
               'k1s': cpymad_element.k1s,
               })
    return xe.Quadrupole(cpymad_element.name, **kw)


def convert_sextupole_from_cpymad(cpymad_element, kw):
    kw.update({
               'k2': cpymad_element.k2,
               'k2s': cpymad_element.k2s,
               })
    return xe.Sextupole(cpymad_element.name, **kw)


def convert_octupole_from_cpymad(cpymad_element, kw):
    kw.update({
               'k3': cpymad_element.k3,
               'k3s': cpymad_element.k3s,
               })
    return xe.Octupole(cpymad_element.name, **kw)


def convert_rfcavity_from_cpymad(cpymad_element, kw):
    kw.update({
               'voltage': cpymad_element.volt,
               'frequency': cpymad_element.freq,
               'lag': cpymad_element.lag,
               })
    return xe.RFCavity(cpymad_element.name, **kw)


def convert_hkicker_from_cpymad(cpymad_element, kw):
    kw.update({
               'kick': cpymad_element.kick,
               })
    return xe.HKicker(cpymad_element.name, **kw)


def convert_vkicker_from_cpymad(cpymad_element, kw):
    kw.update({
               'kick': cpymad_element.kick,
               })
    return xe.VKicker(cpymad_element.name, **kw)


def convert_tkicker_from_cpymad(cpymad_element, kw):
    kw.update({
               'hkick': cpymad_element.hkick,
               'vkick': cpymad_element.vkick,
               })
    return xe.TKicker(cpymad_element.name, **kw)


def convert_thinmultipole_from_cpymad(cpymad_element, kw):
    kw.update({
               'knl': cpymad_element.knl,
               'ksl': cpymad_element.ksl,
               })
    return xe.ThinMultipole(cpymad_element.name, **kw)


def convert_thinsolenoid_from_cpymad(cpymad_element, kw):
    kw.update({
               'ks': cpymad_element.ks,
               'ksi': cpymad_element.ksi,
               })
    return xe.ThinSolenoid(cpymad_element.name, **kw)


def convert_thinrfmultipole_from_cpymad(cpymad_element, kw):
    kw.update({
               'voltage': cpymad_element.volt,
               'frequency': cpymad_element.freq,
               'lag': cpymad_element.lag,
               })
    return xe.ThinRFMultipole(cpymad_element.name, **kw)


FROM_CPYMAD = {'monitor':         convert_monitor_from_cpymad         ,
               'marker':          convert_marker_from_cpymad          ,
               'drift':           convert_drift_from_cpymad           ,
               'sbend':           convert_sectorbend_from_cpymad      ,
               'rbend':           convert_rectangularbend_from_cpymad ,
               'quadrupole':      convert_quadrupole_from_cpymad      ,
               'sextupole':       convert_sextupole_from_cpymad       ,
               'octupole':        convert_octupole_from_cpymad        ,
               'collimator':      convert_collimator_from_cpymad      ,
               'hkicker':         convert_hkicker_from_cpymad         ,
               'vkicker':         convert_vkicker_from_cpymad         ,
               'tkicker':         convert_tkicker_from_cpymad         ,
               'rfcavity':        convert_rfcavity_from_cpymad        ,
               'placeholder':     convert_placeholder_from_cpymad     ,
               'instrument':      convert_instrument_from_cpymad      ,
               'dipedge':         convert_dipoleedge_from_cpymad      ,
               'solenoid':        convert_solenoid_from_cpymad        ,
               'multipole':       convert_multipole_from_cpymad       ,
               'thinsolenoid':    convert_thinsolenoid_from_cpymad    ,
               'thinrfmultipole': convert_thinrfmultipole_from_cpymad ,
            }


def from_cpymad(cpymad_element):
    kw = get_base_dict_from_cpymad(cpymad_element)
    return FROM_CPYMAD[cpymad_element.base_type.name](cpymad_element, kw)


"""
Export functions to cpymad
"""


def get_base_dict_to_cpymad(xel: xe.BaseElement):
    base_dict = {
                'l' : xel.length,
                }

    try: base_dict.update({'lrad' : xel.radiation_length})
    except: KeyError
    try: base_dict.update({'aperture' : xel.aperture_size})
    except: KeyError
    try: base_dict.update({'apertype' : xel.aperture_type})
    except: KeyError
    return base_dict


def convert_marker_to_cpymad(madx: Madx, kw: dict, xel: xe.Marker):
    kw.pop('lrad')
    return madx.command['marker'].clone(xel.name, **kw)


def convert_drift_to_cpymad(madx: Madx, kw: dict, xel: xe.Drift):
    return madx.command['drift'].clone(xel.name, **kw)


def convert_collimator_to_cpymad(madx: Madx, kw: dict, xel: xe.Collimator):
    return madx.command['collimator'].clone(xel.name, **kw)


def convert_monitor_to_cpymad(madx: Madx, kw: dict, xel: xe.Monitor):
    return madx.command['monitor'].clone(xel.name, **kw)

def convert_placeholder_to_cpymad(madx: Madx, kw: dict, xel: xe.Placeholder):
    return madx.command['placeholder'].clone(xel.name, **kw)


def convert_instrument_to_cpymad(madx: Madx, kw: dict, xel: xe.Instrument):
    return madx.command['instrument'].clone(xel.name, **kw)


def convert_sectorbend_to_cpymad(madx: Madx, kw: dict, xel: xe.SectorBend):
    kw.update({
                'angle': xel.angle,
                'k0': xel.k0,
                'k1': xel.k1,
                'e1': xel.e1,
                'e2': xel.e2,
                })
    return madx.command['sbend'].clone(xel.name, **kw)


def convert_rectangularbend_to_cpymad(madx: Madx, kw: dict, xel: xe.RectangularBend):
    kw.update({
                'angle': xel.angle,
                'k0': xel.k0,
                'k1': xel.k1,
                'e1': xel._rbend_e1,
                'e2': xel._rbend_e2,
                })
    kw['l'] = xel._chord_length
    return madx.command['rbend'].clone(xel.name, **kw)


def convert_dipoleedge_to_cpymad(madx: Madx, kw: dict, xel: xe.DipoleEdge):
    kw.update({
                'h': xel.h,
                'e1': xel.edge_angle,
                })
    return madx.command['dipedge'].clone(xel.name, **kw)


def convert_solenoid_to_cpymad(madx: Madx, kw: dict, xel: xe.Solenoid):
    kw.update({
                'ks': xel.ks,
                'ksi': xel.ksi,
                })
    return madx.command['solenoid'].clone(xel.name, **kw)


def convert_multipole_to_cpymad(madx: Madx, kw: dict, xel: xe.Multipole):
    kw.update({
               'knl': xel.knl,
               'ksl': xel.ksl,
               })
    return madx.command['multipole'].clone(xel.name, **kw)


def convert_quadrupole_to_cpymad(madx: Madx, kw: dict, xel: xe.Quadrupole):
    kw.update({
               'k1': xel.k1,
               'k1s': xel.k1s,
               })
    return madx.command['quadrupole'].clone(xel.name, **kw)


def convert_sextupole_to_cpymad(madx: Madx, kw: dict, xel: xe.Sextupole):
    kw.update({
               'k2': xel.k2,
               'k2s': xel.k2s,
               })
    return madx.command['sextupole'].clone(xel.name, **kw)


def convert_octupole_to_cpymad(madx: Madx, kw: dict, xel: xe.Octupole):
    kw.update({
               'k3': xel.k3,
               'k3s': xel.k3s,
               })
    return madx.command['octupole'].clone(xel.name, **kw)


def convert_rfcavity_to_cpymad(madx: Madx, kw: dict, xel: xe.RFCavity):
    kw.update({
               'volt': xel.voltage,
               'freq': xel.frequency,
               'lag': xel.lag,
               })
    return madx.command['rfcavity'].clone(xel.name, **kw)


def convert_hkicker_to_cpymad(madx: Madx, kw: dict, xel: xe.HKicker):
    kw.update({
               'kick': xel.kick,
               })
    return madx.command['hkicker'].clone(xel.name, **kw)


def convert_vkicker_to_cpymad(madx: Madx, kw: dict, xel: xe.VKicker):
    kw.update({
               'kick': xel.kick,
               })
    return madx.command['vkicker'].clone(xel.name, **kw)


def convert_tkicker_to_cpymad(madx: Madx, kw: dict, xel: xe.TKicker):
    kw.update({
               'hkick': xel.hkick,
               'vkick': xel.vkick,
               })
    return madx.command['tkicker'].clone(xel.name, **kw)


def convert_thinmultipole_to_cpymad(madx: Madx, kw: dict, xel: xe.ThinMultipole):
    kw.update({
               'knl': xel.knl,
               'ksl': xel.ksl,
               })
    return madx.command['multipole'].clone(xel.name, **kw)


def convert_thinsolenoid_to_cpymad(madx: Madx, kw: dict, xel: xe.ThinSolenoid):
    kw.update({
               'ks': xel.ks,
               'ksi': xel.ksi,
               })
    return madx.command['thinsolenoid'].clone(xel.name, **kw)


def convert_thinrfmultipole_to_cpymad(madx: Madx, kw: dict, xel: xe.ThinRFMultipole):
    return madx.command['thinrfmultipole'].clone(xel.name, **kw)


TO_CPYMAD = {'Monitor':         convert_monitor_to_cpymad         ,
             'Marker':          convert_marker_to_cpymad          ,
             'Drift':           convert_drift_to_cpymad           ,
             'SectorBend':      convert_sectorbend_to_cpymad      ,
             'RectangularBend': convert_rectangularbend_to_cpymad ,
             'Quadrupole':      convert_quadrupole_to_cpymad      ,
             'Sextupole':       convert_sextupole_to_cpymad       ,
             'Octupole':        convert_octupole_to_cpymad        ,
             'ThinMultipole':   convert_thinmultipole_to_cpymad   ,
             'Collimator':      convert_collimator_to_cpymad      ,
             'HKicker':         convert_hkicker_to_cpymad         ,
             'VKicker':         convert_vkicker_to_cpymad         ,
             'TKicker':         convert_tkicker_to_cpymad         ,
             'RFCavity':        convert_rfcavity_to_cpymad        ,
             'Placeholder':     convert_placeholder_to_cpymad     ,
             'Instrument':      convert_instrument_to_cpymad      ,
             'Dipedge':         convert_dipoleedge_to_cpymad      ,
             'Solenoid':        convert_solenoid_to_cpymad        ,
             'Multipole':       convert_multipole_to_cpymad       ,
             'ThinSolenoid':    convert_thinsolenoid_to_cpymad    ,
             'ThinRFMultipole': convert_thinrfmultipole_to_cpymad ,
            }


def to_cpymad(madx: Madx, xe_element: xe.BaseElement):
    kw = get_base_dict_to_cpymad(xe_element)
    return TO_CPYMAD[xe_element.__class__.__name__](madx, kw, xe_element)
