from arc2.core import *

from .helpers import color_for_holes_0a2355a6, hole_count_0a2355a6


def verify_0a2355a6(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = totuple(x0)
    x2 = apply(hole_count_0a2355a6, x1)
    x3 = apply(color_for_holes_0a2355a6, x2)
    x4 = mpapply(recolor, x3, x1)
    x5 = canvas(ZERO, shape(I))
    x6 = paint(x5, x4)
    return x6
