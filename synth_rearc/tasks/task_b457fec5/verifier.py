from synth_rearc.core import *

from .helpers import recolor_band_patch_b457fec5


def verify_b457fec5(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, FIVE)
    x2 = difference(x0, x1)
    x3 = order(x2, ulcorner)
    x4 = apply(color, x3)
    x5 = mapply(lbind(recolor_band_patch_b457fec5, x4), x1)
    x6 = paint(I, x5)
    return x6
