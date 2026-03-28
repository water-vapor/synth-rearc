from synth_rearc.core import *

from .helpers import hole_count_8ba14f53


def verify_8ba14f53(I: Grid) -> Grid:
    x0 = objects(I, T, F, F)
    x1 = sfilter(x0, lambda x2: color(x2) != ZERO)
    x2 = order(x1, lambda x3: (leftmost(x3), uppermost(x3), color(x3)))
    x3 = apply(hole_count_8ba14f53, x2)
    x4 = canvas(ZERO, (THREE, THREE))
    x5 = ZERO
    for x6, x7 in zip(x2, x3):
        x8 = color(x6)
        x9 = divide(add(x7, TWO), THREE)
        x10 = x7
        for x11 in range(x9):
            x12 = branch(greater(x10, THREE), THREE, x10)
            x13 = frozenset((add(x5, x11), x14) for x14 in range(x12))
            x4 = fill(x4, x8, x13)
            x10 = subtract(x10, x12)
        x5 = add(x5, x9)
    return x4
