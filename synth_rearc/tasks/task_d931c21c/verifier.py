from synth_rearc.core import *

from .helpers import cycle_bands_d931c21c
from .helpers import is_cycle_d931c21c


def verify_d931c21c(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = ofcolor(I, ZERO)
    x2 = I
    for x3 in x0:
        if not is_cycle_d931c21c(x3):
            continue
        x4, x5 = cycle_bands_d931c21c(x3)
        x6 = ulcorner(x3)
        x7 = shift(x4, x6)
        x8 = shift(x5, x6)
        x9 = intersection(x7, x1)
        x10 = difference(intersection(x8, x1), x9)
        x2 = fill(x2, THREE, x9)
        x2 = fill(x2, TWO, x10)
    return x2
