from xconverters.pyat import element_from_pyat, element_to_pyat


TO_PYAT = {'Monitor':         element_to_pyat.convert_monitor         ,
           'Marker':          element_to_pyat.convert_marker          ,
           'Drift':           element_to_pyat.convert_drift           ,
           'SectorBend':      element_to_pyat.convert_sectorbend      ,
           'RectangularBend': element_to_pyat.convert_rectangularbend ,
           'Quadrupole':      element_to_pyat.convert_quadrupole      ,
           'Sextupole':       element_to_pyat.convert_sextupole       ,
           'Octupole':        element_to_pyat.convert_octupole        ,
           'ThinMultipole':   element_to_pyat.convert_thinmultipole   ,
           'Collimator':      element_to_pyat.convert_collimator      ,
           'HKicker':         element_to_pyat.convert_hkicker         ,
           'VKicker':         element_to_pyat.convert_vkicker         ,
           'TKicker':         element_to_pyat.convert_tkicker         ,
           'RFCavity':        element_to_pyat.convert_rfcavity        }


FROM_PYAT = {'Monitor':        element_from_pyat.convert_monitor       ,
             'Marker':         element_from_pyat.convert_marker        ,
             'Drift':          element_from_pyat.convert_drift         ,
             'Dipole':         element_from_pyat.convert_dipole        ,
             'Quadrupole':     element_from_pyat.convert_quadrupole    ,
             'Sextupole':      element_from_pyat.convert_sextupole     ,
             'Octupole':       element_from_pyat.convert_octupole      ,
             'ThinMultipole':  element_from_pyat.convert_thinmultipole ,
             'Corrector':      element_from_pyat.convert_corrector     ,
             'RFCavity':       element_from_pyat.convert_rfcavity      }



def to_pyat(xe_element):
    return TO_PYAT[xe_element.__class__.__name__](xe_element)


def from_pyat(pyat_element):
    pyat_dict = pyat_element.__dict__
    return FROM_PYAT[pyat_element.__class__.__name__](pyat_dict)
