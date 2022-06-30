# copyright #################################### #
# This file is part of the Xconverters Package.  #
# Copyright (c) CERN, 2022.                      #
# ############################################## #

import xtrack
from xsequence.lattice import Lattice


def from_xtrack(xt_line: xtrack.Line) -> Lattice:
    names =  xt_line._thin_sequence.names
    line = [xt_line._thin_elements[node.element_name].to_xtrack() for node in lattice._thin_sequence]
    xtrack_lattice = xtrack.Line(elements=line, element_names=names)
    return Lattice(lattice_name, sequence=sequence, elements=elements, key='line', beam=beam)


def to_xtrack(lattice: Lattice) -> xtrack.Line:
    names =  lattice._thin_sequence.names
    line = [lattice._thin_elements[node.element_name].to_xtrack() for node in lattice._thin_sequence]
    xtrack_lattice = xtrack.Line(elements=line, element_names=names)
    return xtrack_lattice
