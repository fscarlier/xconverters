"""
Module conversion_utils.cpymad_element_conversion
------------------
:author: Felix Carlier (fcarlier@cern.ch)
This is a Python3 module with functions for importing and exporting elements from and to cpymad
"""

import xsequence.elements as xe
import xconverters.cpymad.cpymad_properties as cpymad_properties


def attr_mapping_from_cpymad(cpymad_element):
    for key in cpymad_properties.DIFF_ATTRIBUTE_MAP_CPYMAD:
        try: cpymad_element[key] = cpymad_element.pop(cpymad_properties.DIFF_ATTRIBUTE_MAP_CPYMAD[key]) 
        except: KeyError 
    return cpymad_element


def from_cpymad(xs_cls, cpymad_element, name=None):
    if not isinstance(cpymad_element, dict):
        name = cpymad_element.name
        elemdata={'base_type':cpymad_element.base_type.name}
        for parname, par in cpymad_element.cmdpar.items():
            elemdata[parname]=par.value
        cpymad_element = elemdata
    mapped_attr = attr_mapping_from_cpymad(cpymad_element)
    if mapped_attr['location'] > 1e19:
        mapped_attr.pop('location')
    return xs_cls(name, **mapped_attr)


def attr_mapping_to_cpymad(element_dict):
    for key in cpymad_properties.DIFF_ATTRIBUTE_MAP_CPYMAD:
        try: element_dict[cpymad_properties.DIFF_ATTRIBUTE_MAP_CPYMAD[key]] = element_dict.pop(key) 
        except: KeyError

    if 'kn' in element_dict:
        element_dict['knl'] = list(element_dict.pop('kn')*element_dict['l'])
    if 'ks' in element_dict:
        element_dict['ksl'] = list(element_dict.pop('ks')*element_dict['l'])
    return element_dict


def to_cpymad(xs_element, madx):
    print(xs_element)
    base_type = xs_element.__class__.__name__
    madx_base_type = base_type.lower()
    if base_type == 'SectorBend':
        madx_base_type = 'sbend'
    if base_type == 'RectangularBend':
        madx_base_type = 'rbend'
    if base_type == 'ThinMultipole':
        madx_base_type = 'multipole'
    
    el_dict = xs_element.get_dict()
    
    if base_type == 'Quadrupole':
        el_dict['k1'] = xs_element.k1
        el_dict['k1s'] = xs_element.k1s
    elif base_type == 'Sextupole':
        el_dict['k2'] = xs_element.k2
        el_dict['k2s'] = xs_element.k2s
    elif base_type == 'Octupole':
        el_dict['k3'] = xs_element.k3
        el_dict['k3s'] = xs_element.k3s

    el_dict = attr_mapping_to_cpymad(el_dict)
    mapped_attr = {k:el_dict[k] for k in cpymad_properties.ELEM_DICT[madx_base_type] if k in el_dict}
    if madx_base_type == 'rbend':
        mapped_attr['l'] = xs_element._chord_length
        mapped_attr['e1'] = xs_element._rbend_e1
        mapped_attr['e2'] = xs_element._rbend_e2
    
    if 'reference' in mapped_attr:
        mapped_attr.pop('reference')
    return madx.command[madx_base_type].clone(xs_element.name, **mapped_attr)


CPYMAD_TO_XSEQUENCE_MAP = { 
                           'marker'          : xe.Marker         ,  
                           'drift'           : xe.Drift          ,  
                           'collimator'      : xe.Collimator     ,  
                           'monitor'         : xe.Monitor        ,  
                           'placeholder'     : xe.Placeholder    ,  
                           'instrument'      : xe.Instrument     ,  
                           'sbend'           : xe.SectorBend     ,  
                           'rbend'           : xe.RectangularBend,     
                           'dipedge'         : xe.DipoleEdge     ,  
                           'solenoid'        : xe.Solenoid       ,  
                           'multipole'       : xe.ThinMultipole      ,  
                           'quadrupole'      : xe.Quadrupole     ,  
                           'sextupole'       : xe.Sextupole      ,  
                           'octupole'        : xe.Octupole       ,  
                           'rfcavity'        : xe.RFCavity       ,  
                           'hkicker'         : xe.HKicker        ,  
                           'vkicker'         : xe.VKicker        ,  
                           'tkicker'         : xe.TKicker        ,  
                           'thinmultipole'   : xe.ThinMultipole  ,  
                           'thinsolenoid'    : xe.ThinSolenoid   ,  
                           'thinrfmultipole' : xe.ThinRFMultipole, 
                           }


def convert_cpymad_element(cpymad_element):
    return from_cpymad(CPYMAD_TO_XSEQUENCE_MAP[cpymad_element.base_type.name], cpymad_element)
