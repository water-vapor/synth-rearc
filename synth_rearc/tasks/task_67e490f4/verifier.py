from synth_rearc.core import *

from .helpers import (
    connected_components_67e490f4,
    free_shape_key_67e490f4,
)


def verify_67e490f4(
    I: Grid,
) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = argmax(x0, size)
    x2 = color(x1)
    x3 = delta(x1)
    x4 = connected_components_67e490f4(x3)
    x5 = difference(x0, initset(x1))
    x6 = {}
    for x7 in x5:
        x8 = free_shape_key_67e490f4(x7)
        x9 = color(x7)
        x6.setdefault(x8, []).append(x9)
    x10 = canvas(x2, shape(x1))
    x11 = invert(ulcorner(x1))
    for x12 in x4:
        x13 = free_shape_key_67e490f4(x12)
        x14 = mostcommon(tuple(x6[x13]))
        x15 = shift(x12, x11)
        x10 = fill(x10, x14, x15)
    return x10
