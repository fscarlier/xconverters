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


def drift_from_xtrack(element: xl.Drift):
    if element.length == 0:
        return xe.Marker('Marker')
    else:
        kwargs = {'length':element.length}
        return xe.Drift(**kwargs)


def thin_multipole_from_xtrack(element: xl.Multipole):
    kwargs = {'knl':element.knl,
              'ksl':element.ksl,
# NEED TO ADD
#               'hxl':element.hxl,
#               'hyl':element.hyl,
              'radiation_length':element.length}
    return xe.Multipole(**kwargs)


def rfcavity_from_xtrack(element: xl.Cavity):
    kwargs = {'voltage':element.voltage/1e6,
              'frequency':element.frequency/1e6,
              'lag':element.lag}
    return xe.RFCavity(**kwargs)


def dipole_edge_from_xtrack(element: xl.DipoleEdge):
    kwargs = {'h':element.h,
              'edge_angle':element.e1}
# NEED TO ADD
#               'hgap'  [m]: Equivalent gap.
#               'fint'  [] : Fringe integral.
    return xe.DipoleEdge(**kwargs)


def rfmultipole_from_xtrack(element: xl.RFMultipole):
    kwargs = {'voltage':element.voltage/1e6,
              'frequency':element.frequency/1e6,
              'knl':element.knl,
              'ksl':element.ksl,
              'pn':element.pn,
              'ps':element.ps,
              'lag':element.lag}
    return xe.ThinRFMultipole(**kwargs)


def convert_element_from_xtrack(xtrack_element: xe.BaseElement):
    return FROM_XTRACK_CONV[xtrack_element.__class__.__name__](xtrack_element)


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
              'hxl':element.hxl,
              'hyl':element.hyl,
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


def convert_element_to_xtrack(xe_element: xe.BaseElement):
    return TO_XTRACK_CONV[xe_element.__class__.__name__](xe_element)


TO_XTRACK_CONV = {'Marker':          marker_to_xtrack        ,
                  'Drift':           drift_to_xtrack         ,
                  'ThinMultipole':   thin_multipole_to_xtrack,
                  'RFCavity':        rfcavity_to_xtrack      ,
                  'ThinRFMultipole': rfcavity_to_xtrack      ,
                  'DipoleEdge':      dipole_edge_to_xtrack   }
