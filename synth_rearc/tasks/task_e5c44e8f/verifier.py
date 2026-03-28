from synth_rearc.core import *

from .helpers import spiral_path_e5c44e8f


def verify_e5c44e8f(I: Grid) -> Grid:
    x0 = ofcolor(I, THREE)
    x1 = first(x0)
    x2 = ofcolor(I, TWO)
    x3 = spiral_path_e5c44e8f(x1, shape(I))
    x4 = I
    for x5 in x3:
        if contained(x5, x2):
            break
        x4 = fill(x4, THREE, initset(x5))
    return x4
