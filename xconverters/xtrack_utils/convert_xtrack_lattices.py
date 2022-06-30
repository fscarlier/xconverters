# copyright ############################### #
# This file is part of the Xtrack Package.  #
# Copyright (c) CERN, 2021.                 #
# ######################################### #

import xtrack
from xsequence.lattice import Lattice


def to_xtrack(lattice: Lattice) -> xtrack.Line: 
    names =  lattice._thin_sequence.names
    line = [lattice._thin_elements[node.element_name].to_xtrack() for node in lattice._thin_sequence]
    xtrack_lattice = xtrack.Line(elements=line, element_names=names)
    return xtrack_lattice
