from synth_rearc.core import *

from .helpers import decompose_input_3a25b0d8, recolor_scaffold_regions_3a25b0d8


def verify_3a25b0d8(
    I: Grid,
) -> Grid:
    x0 = decompose_input_3a25b0d8(I)
    x1 = x0[ZERO]
    x2 = x0[ONE]
    x3 = x0[TWO]
    x4 = x0[THREE]
    x5 = recolor_scaffold_regions_3a25b0d8(x3, x4, x1, x2)
    return x5
