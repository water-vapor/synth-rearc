from synth_rearc.core import *

from .helpers import transform_rectangle_8cb8642d


def verify_8cb8642d(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = I
    for x2 in x0:
        x3 = backdrop(x2)
        x4 = mostcolor(x2)
        x5 = leastcolor(x2)
        x1 = transform_rectangle_8cb8642d(x1, x3, x4, x5)
    return x1
