"""
Module cpymad.element_to_cpymad
------------------
This is a Python3 module with functions for importing and exporting elements from and to cpymad

use: 
    madx = to_cpymad(madx, xsequence_element)


"""

import cpymad.madx as Madx
import xsequence.elements as xe


def get_base_dict(xel: xe.BaseElement):
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


def convert_marker(madx: Madx, kw: dict, xel: xe.Marker):
    kw.pop('lrad')
    return madx.command['marker'].clone(xel.name, **kw)


def convert_drift(madx: Madx, kw: dict, xel: xe.Drift):
    return madx.command['drift'].clone(xel.name, **kw)


def convert_collimator(madx: Madx, kw: dict, xel: xe.Collimator):
    return madx.command['collimator'].clone(xel.name, **kw)


def convert_monitor(madx: Madx, kw: dict, xel: xe.Monitor):
    return madx.command['monitor'].clone(xel.name, **kw)

def convert_placeholder(madx: Madx, kw: dict, xel: xe.Placeholder):
    return madx.command['placeholder'].clone(xel.name, **kw)


def convert_instrument(madx: Madx, kw: dict, xel: xe.Instrument):
    return madx.command['instrument'].clone(xel.name, **kw)


def convert_sectorbend(madx: Madx, kw: dict, xel: xe.SectorBend):
    kw.update({
                'angle': xel.angle,
                'k0': xel.k0,
                'k1': xel.k1,
                'e1': xel.e1,
                'e2': xel.e2,
                })
    return madx.command['sbend'].clone(xel.name, **kw)


def convert_rectangularbend(madx: Madx, kw: dict, xel: xe.RectangularBend):
    kw.update({
                'angle': xel.angle,
                'k0': xel.k0,
                'k1': xel.k1,
                'e1': xel._rbend_e1,
                'e2': xel._rbend_e2,
                })
    kw['l'] = xel._chord_length
    return madx.command['rbend'].clone(xel.name, **kw)


def convert_dipoleedge(madx: Madx, kw: dict, xel: xe.DipoleEdge):
    kw.update({
                'h': xel.h,
                'e1': xel.edge_angle,
                })
    return madx.command['dipedge'].clone(xel.name, **kw)


def convert_solenoid(madx: Madx, kw: dict, xel: xe.Solenoid):
    kw.update({
                'ks': xel.ks,
                'ksi': xel.ksi,
                })
    return madx.command['solenoid'].clone(xel.name, **kw)


def convert_multipole(madx: Madx, kw: dict, xel: xe.Multipole):
    kw.update({
               'knl': xel.knl,
               'ksl': xel.ksl,
               })
    return madx.command['multipole'].clone(xel.name, **kw)


def convert_quadrupole(madx: Madx, kw: dict, xel: xe.Quadrupole):
    kw.update({
               'k1': xel.k1,
               'k1s': xel.k1s,
               })
    return madx.command['quadrupole'].clone(xel.name, **kw)


def convert_sextupole(madx: Madx, kw: dict, xel: xe.Sextupole):
    kw.update({
               'k2': xel.k2,
               'k2s': xel.k2s,
               })
    return madx.command['sextupole'].clone(xel.name, **kw)


def convert_octupole(madx: Madx, kw: dict, xel: xe.Octupole):
    kw.update({
               'k3': xel.k3,
               'k3s': xel.k3s,
               })
    return madx.command['octupole'].clone(xel.name, **kw)


def convert_rfcavity(madx: Madx, kw: dict, xel: xe.RFCavity):
    kw.update({
               'volt': xel.voltage,
               'freq': xel.frequency, 
               'lag': xel.lag, 
               })
    return madx.command['rfcavity'].clone(xel.name, **kw)


def convert_hkicker(madx: Madx, kw: dict, xel: xe.HKicker):
    kw.update({
               'kick': xel.kick,
               })
    return madx.command['hkicker'].clone(xel.name, **kw)


def convert_vkicker(madx: Madx, kw: dict, xel: xe.VKicker):
    kw.update({
               'kick': xel.kick,
               })
    return madx.command['vkicker'].clone(xel.name, **kw)


def convert_tkicker(madx: Madx, kw: dict, xel: xe.TKicker):
    kw.update({
               'hkick': xel.hkick,
               'vkick': xel.vkick,
               })
    return madx.command['tkicker'].clone(xel.name, **kw)


def convert_thinmultipole(madx: Madx, kw: dict, xel: xe.ThinMultipole):
    kw.update({
               'knl': xel.knl, 
               'ksl': xel.ksl,
               })
    return madx.command['multipole'].clone(xel.name, **kw)


def convert_thinsolenoid(madx: Madx, kw: dict, xel: xe.ThinSolenoid):
    kw.update({
               'ks': xel.ks,  
               'ksi': xel.ksi,
               })
    return madx.command['thinsolenoid'].clone(xel.name, **kw)


def convert_thinrfmultipole(madx: Madx, kw: dict, xel: xe.ThinRFMultipole):
    return madx.command['thinrfmultipole'].clone(xel.name, **kw)

