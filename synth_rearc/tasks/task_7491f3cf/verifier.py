from synth_rearc.core import *

from .helpers import panel_mask_7491f3cf


def verify_7491f3cf(I: Grid) -> Grid:
    x0 = astuple(ONE, ONE)
    x1 = astuple(FIVE, FIVE)
    x2 = crop(I, x0, x1)
    x3 = crop(I, (ONE, 7), x1)
    x4 = crop(I, (ONE, 13), x1)
    x5 = panel_mask_7491f3cf(x2)
    x6 = difference(asindices(x3), x5)
    x7 = toobject(x5, x3)
    x8 = toobject(x6, x4)
    x9 = canvas(mostcolor(x3), x1)
    x10 = paint(x9, combine(x7, x8))
    x11 = shift(asobject(x10), (ONE, 19))
    x12 = paint(I, x11)
    return x12
