from synth_rearc.core import *

from .helpers import resize_object_465b7d93


def verify_465b7d93(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, SIX)
    x2 = argmax(x1, size)
    x3 = remove(x2, x0)
    x4 = merge(x3)
    x5 = uppermost(x2)
    x6 = leftmost(x2)
    x7 = lowermost(x2)
    x8 = rightmost(x2)
    x9 = subtract(x7, x5)
    x10 = subtract(x8, x6)
    x11 = decrement(x9)
    x12 = decrement(x10)
    x13 = astuple(x11, x12)
    x14 = resize_object_465b7d93(x4, x13)
    x15 = astuple(increment(x5), increment(x6))
    x16 = shift(x14, x15)
    x17 = cover(I, x4)
    x18 = paint(x17, x16)
    return x18
