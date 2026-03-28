from synth_rearc.core import *

from .helpers import ordered_objects_d017b73f, pack_objects_d017b73f


def verify_d017b73f(I: Grid) -> Grid:
    x0 = ordered_objects_d017b73f(I)
    x1 = pack_objects_d017b73f(x0)
    x2 = merge(x1)
    x3 = height(I)
    x4 = increment(rightmost(x2))
    x5 = astuple(x3, x4)
    x6 = canvas(ZERO, x5)
    x7 = paint(x6, x2)
    return x7
