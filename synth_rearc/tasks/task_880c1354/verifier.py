from synth_rearc.core import *

from .helpers import ordered_outer_objects_880c1354


def verify_880c1354(I: Grid) -> Grid:
    x0 = ordered_outer_objects_880c1354(I)
    x1 = apply(color, x0)
    x2 = x1[-ONE:] + x1[:-ONE]
    x3 = frozenset(
        x4
        for x5, x6 in zip(x2, x0)
        for x4 in recolor(x5, x6)
    )
    x4 = paint(I, x3)
    return x4
