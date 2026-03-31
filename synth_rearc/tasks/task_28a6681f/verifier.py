from synth_rearc.core import *

from .helpers import (
    donor_indices_28a6681f,
    infer_side_mode_28a6681f,
    ordered_target_mask_28a6681f,
    scaffold_indices_28a6681f,
)


def verify_28a6681f(I: Grid) -> Grid:
    x0 = donor_indices_28a6681f(I)
    x1 = scaffold_indices_28a6681f(I)
    x2 = infer_side_mode_28a6681f(I)
    x3 = ordered_target_mask_28a6681f(x1, width(I), x2)
    x4 = size(x0)
    x5 = frozenset(x3[:x4])
    x6 = fill(I, ZERO, x0)
    x7 = fill(x6, ONE, x5)
    return x7
