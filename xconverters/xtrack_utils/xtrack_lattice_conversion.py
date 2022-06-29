"""
Module xsequence.lattice
------------------
:author: Felix Carlier (fcarlier@cern.ch)
This is a Python3 module containing base Lattice class to manipulate accelerator sequences.
"""

import xtrack
from xsequence.lattice import Lattice


def to_xtrack(lattice: Lattice) -> xtrack.Line: 
    names =  lattice._thin_sequence.names
    line = [lattice._thin_elements[node.element_name].to_xtrack() for node in lattice._thin_sequence]
    xtrack_lattice = xtrack.Line(elements=line, element_names=names)
    return xtrack_lattice
