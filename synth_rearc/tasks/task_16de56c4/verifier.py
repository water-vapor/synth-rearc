from synth_rearc.core import *

from .helpers import render_axis_16de56c4


def verify_16de56c4(I: Grid) -> Grid:
    x0, x1, x2 = render_axis_16de56c4(I, "h")
    x3, x4, x5 = render_axis_16de56c4(I, "v")
    x6 = greater(x2, x5)
    x7 = branch(x6, x0, x3)
    x8 = equality(x2, x5)
    x9 = greater(x1, x4)
    x10 = branch(x9, x0, x3)
    x11 = branch(x8, x10, x7)
    return x11
