from synth_rearc.core import *

from .helpers import valid_plus_center_14754a24


def verify_14754a24(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = frozenset()
    for x3 in range(x0):
        for x4 in range(x1):
            x5 = valid_plus_center_14754a24(I, (x3, x4))
            if x5 is None:
                continue
            x2 = combine(x2, x5)
    x6 = fill(I, TWO, x2)
    return x6
