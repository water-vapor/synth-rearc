from synth_rearc.core import *

from .helpers import render_spiral_08573cc6


def verify_08573cc6(I: Grid) -> Grid:
    x0 = shape(I)
    x1 = first(ofcolor(I, ONE))
    x2 = index(I, ORIGIN)
    x3 = index(I, (ZERO, ONE))
    x4 = render_spiral_08573cc6(x0, x1, x2, x3)
    return x4
