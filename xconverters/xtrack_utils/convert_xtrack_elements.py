# copyright #################################### #
# This file is part of the Xconverters Package.  #
# Copyright (c) CERN, 2022.                      #
# ############################################## #

"""
Converting xsequence elements to and from xtrack elements.
"""

import xtrack as xl
import xsequence.elements as xe


"""
Import xtrack element to xsequence
"""


def drift_from_xtrack(element: xl.Drift, ele_name: str):
    if not ele_name:
        ele_name = 'drift'

    if element.length == 0:
        return xe.Marker('Marker')
    else:
        kwargs = {'length':element.length}
        return xe.Drift(ele_name, **kwargs)


def thin_multipole_from_xtrack(element: xl.Multipole, ele_name: str):
    if not ele_name:
        ele_name = 'multipole'

    knl = element.knl
    ksl = element.ksl
    knl[0] = element.hxl
    ksl[0] = element.hyl

    kwargs = {'knl':knl,
              'ksl':ksl,
              'radiation_length':element.length}
    return xe.ThinMultipole(ele_name, **kwargs)


def rfcavity_from_xtrack(element: xl.Cavity, ele_name: str):
    if not ele_name:
        ele_name = 'rfcavity'

    kwargs = {'voltage':element.voltage/1e6,
              'frequency':element.frequency/1e6,
              'lag':element.lag}
    return xe.RFCavity(ele_name, **kwargs)


def dipole_edge_from_xtrack(element: xl.DipoleEdge, ele_name: str):
    if not ele_name:
        ele_name = 'dipedge'

    kwargs = {'h':element.h,
              'edge_angle':element.e1}
# NEED TO ADD
#               'hgap'  [m]: Equivalent gap.
#               'fint'  [] : Fringe integral.
    return xe.DipoleEdge(ele_name, **kwargs)


def rfmultipole_from_xtrack(element: xl.RFMultipole, ele_name: str):
    if not ele_name:
        ele_name = 'rfmultipole'

    kwargs = {'voltage':element.voltage/1e6,
              'frequency':element.frequency/1e6,
              'knl':element.knl,
              'ksl':element.ksl,
              'pn':element.pn,
              'ps':element.ps,
              'lag':element.lag}
    return xe.ThinRFMultipole(ele_name, **kwargs)


def from_xtrack(xtrack_element: xe.BaseElement, ele_name: str = None):
    return FROM_XTRACK_CONV[xtrack_element.__class__.__name__](xtrack_element, ele_name)


FROM_XTRACK_CONV = {'Drift':       drift_from_xtrack         ,
                    'Multipole':   thin_multipole_from_xtrack,
                    'Cavity':      rfcavity_from_xtrack      ,
                    'RFMultipole': rfmultipole_from_xtrack   ,
                    'DipoleEdge':  dipole_edge_from_xtrack   }


"""
Export xsequence element to xtrack
"""


def marker_to_xtrack(element: xe.Marker):
    assert element.length == 0
    kwargs = {'length':element.length}
    return xl.Drift(**kwargs)


def drift_to_xtrack(element: xe.Drift):
    kwargs = {'length':element.length}
    return xl.Drift(**kwargs)


def thin_multipole_to_xtrack(element: xe.ThinMultipole):
    kwargs = {'knl':element.knl,
              'ksl':element.ksl,
              'hxl':element.knl[0],
              'hyl':element.ksl[0],
              'length':element.radiation_length}
    return xl.Multipole(**kwargs)


def rfcavity_to_xtrack(element: xe.RFCavity):
    kwargs = {'voltage':element.voltage*1e6,
              'frequency':element.frequency*1e6,
              'lag':element.lag}
    return xl.Cavity(**kwargs)


def dipole_edge_to_xtrack(element: xe.DipoleEdge):
    kwargs = {'h':element.h,
              'e1':element.edge_angle}
# NEED TO ADD
#             'hgap'  [m]: Equivalent gap.
#             'fint'  [] : Fringe integral.
    return xl.DipoleEdge(**kwargs)


def rfmultipole_to_xtrack(element: xe.ThinRFMultipole):
    kwargs = {'voltage':element.voltage*1e6,
              'frequency':element.frequency*1e6,
              'knl':element.knl,
              'ksl':element.ksl,
              'pn':element.pn,
              'ps':element.ps,
              'lag':element.lag}
    return xl.RFMultipole(**kwargs)


def to_xtrack(xe_element: xe.BaseElement):
    return TO_XTRACK_CONV[xe_element.__class__.__name__](xe_element)


TO_XTRACK_CONV = {'Marker':          marker_to_xtrack        ,
                  'Drift':           drift_to_xtrack         ,
                  'ThinMultipole':   thin_multipole_to_xtrack,
                  'RFCavity':        rfcavity_to_xtrack      ,
                  'ThinRFMultipole': rfcavity_to_xtrack      ,
                  'DipoleEdge':      dipole_edge_to_xtrack   }
