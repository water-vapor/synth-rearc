from synth_rearc.core import *

from .helpers import barrier_orientations_7e2bad24, trace_extension_7e2bad24


def verify_7e2bad24(I: Grid) -> Grid:
    x0 = objects(I, T, T, T)
    x1 = colorfilter(x0, ONE)
    x2 = first(x1)
    x3 = toindices(x2)
    x4 = tuple(
        x5
        for x5 in x3
        if equality(size(intersection(x3, ineighbors(x5))), ONE)
    )
    x5 = tuple(first(intersection(x3, ineighbors(x6))) for x6 in x4)
    x6 = tuple(subtract(x7, x8) for x7, x8 in zip(x4, x5))
    x7 = pair(x4, x6)
    x8 = barrier_orientations_7e2bad24(I, TWO)
    x9 = I
    for x10, x11 in x7:
        x12, _, _ = trace_extension_7e2bad24(I, x10, x11, x8)
        x13 = recolor(ONE, frozenset(x12))
        x9 = paint(x9, x13)
    return x9
