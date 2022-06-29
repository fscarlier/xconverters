"""
Module cpymad.element_to_cpymad
------------------
This is a Python3 module with functions for importing and exporting elements from and to cpymad

use:
    madx = to_cpymad(madx, xsequence_element)
"""

import cpymad.madx as Madx
import xsequence.elements as xe
from xconverters.cpymad_utils import element_from_cpymad, element_to_cpymad


TO_CPYMAD = {'Monitor':         element_to_cpymad.convert_monitor         ,
             'Marker':          element_to_cpymad.convert_marker          ,
             'Drift':           element_to_cpymad.convert_drift           ,
             'SectorBend':      element_to_cpymad.convert_sectorbend      ,
             'RectangularBend': element_to_cpymad.convert_rectangularbend ,
             'Quadrupole':      element_to_cpymad.convert_quadrupole      ,
             'Sextupole':       element_to_cpymad.convert_sextupole       ,
             'Octupole':        element_to_cpymad.convert_octupole        ,
             'ThinMultipole':   element_to_cpymad.convert_thinmultipole   ,
             'Collimator':      element_to_cpymad.convert_collimator      ,
             'HKicker':         element_to_cpymad.convert_hkicker         ,
             'VKicker':         element_to_cpymad.convert_vkicker         ,
             'TKicker':         element_to_cpymad.convert_tkicker         ,
             'RFCavity':        element_to_cpymad.convert_rfcavity        ,
             'Placeholder':     element_to_cpymad.convert_placeholder     ,
             'Instrument':      element_to_cpymad.convert_instrument      ,
             'Dipedge':         element_to_cpymad.convert_dipoleedge      ,
             'Solenoid':        element_to_cpymad.convert_solenoid        ,
             'Multipole':       element_to_cpymad.convert_multipole   ,
             'ThinSolenoid':    element_to_cpymad.convert_thinsolenoid    ,
             'ThinRFMultipole': element_to_cpymad.convert_thinrfmultipole ,
            }


FROM_CPYMAD = {'monitor':         element_from_cpymad.convert_monitor         ,
               'marker':          element_from_cpymad.convert_marker          ,
               'drift':           element_from_cpymad.convert_drift           ,
               'sbend':           element_from_cpymad.convert_sectorbend      ,
               'rbend':           element_from_cpymad.convert_rectangularbend ,
               'quadrupole':      element_from_cpymad.convert_quadrupole      ,
               'sextupole':       element_from_cpymad.convert_sextupole       ,
               'octupole':        element_from_cpymad.convert_octupole        ,
               'collimator':      element_from_cpymad.convert_collimator      ,
               'hkicker':         element_from_cpymad.convert_hkicker         ,
               'vkicker':         element_from_cpymad.convert_vkicker         ,
               'tkicker':         element_from_cpymad.convert_tkicker         ,
               'rfcavity':        element_from_cpymad.convert_rfcavity        ,
               'placeholder':     element_from_cpymad.convert_placeholder     ,
               'instrument':      element_from_cpymad.convert_instrument      ,
               'dipedge':         element_from_cpymad.convert_dipoleedge      ,
               'solenoid':        element_from_cpymad.convert_solenoid        ,
               'multipole':       element_from_cpymad.convert_multipole   ,
               'thinsolenoid':    element_from_cpymad.convert_thinsolenoid    ,
               'thinrfmultipole': element_from_cpymad.convert_thinrfmultipole ,
            }


def to_cpymad(madx: Madx, xe_element: xe.BaseElement):
    kw = element_to_cpymad.get_base_dict(xe_element)
    return TO_CPYMAD[xe_element.__class__.__name__](madx, kw, xe_element)


def from_cpymad(cpymad_element):
    kw = element_from_cpymad.get_base_dict(cpymad_element)
    return FROM_CPYMAD[cpymad_element.base_type.name](cpymad_element, kw)


