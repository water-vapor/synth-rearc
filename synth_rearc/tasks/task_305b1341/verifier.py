from synth_rearc.core import *

from .helpers import legend_pairs_305b1341, marker_patch_305b1341, paint_region_305b1341


def verify_305b1341(I: Grid) -> Grid:
    x0 = legend_pairs_305b1341(I)
    x1 = size(x0)
    x2 = canvas(ZERO, shape(I))
    for x3, x4 in reversed(x0):
        x5 = marker_patch_305b1341(I, x3, x1)
        x2 = paint_region_305b1341(x2, x5, x3, x4)
    return x2
