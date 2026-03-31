from synth_rearc.core import *

from .helpers import projection_object_1ae2feb7


def verify_1ae2feb7(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = sfilter(x0, vline)
    x2 = argmax(x1, size)
    x3 = leftmost(x2)
    x4 = projection_object_1ae2feb7(I, x3)
    x5 = paint(I, x4)
    return x5
