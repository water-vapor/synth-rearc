from synth_rearc.core import *

from .helpers import blue_patch_c97c0139


def verify_c97c0139(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, TWO)
    x2 = mapply(blue_patch_c97c0139, x1)
    x3 = fill(I, EIGHT, x2)
    return x3
