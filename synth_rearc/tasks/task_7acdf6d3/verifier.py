from synth_rearc.core import *

from .helpers import row_hole_mask_7acdf6d3


def verify_7acdf6d3(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = remove(x0, palette(I))
    x2 = first(x1)
    x3 = other(x1, x2)
    x4 = objects(I, T, T, T)
    x5 = matcher(color, x2)
    x6 = sfilter(x4, x5)
    x7 = matcher(color, x3)
    x8 = sfilter(x4, x7)
    x9 = colorcount(I, x2)
    x10 = colorcount(I, x3)
    x11 = compose(size, row_hole_mask_7acdf6d3)
    x12 = matcher(x11, x9)
    x13 = sfilter(x8, x12)
    x14 = matcher(x11, x10)
    x15 = sfilter(x6, x14)
    x16 = equality(size(x13), ONE)
    x17 = branch(x16, x2, x3)
    x18 = branch(x16, x13, x15)
    x19 = first(x18)
    x20 = ofcolor(I, x17)
    x21 = fill(I, x0, x20)
    x22 = row_hole_mask_7acdf6d3(x19)
    x23 = fill(x21, x17, x22)
    return x23
