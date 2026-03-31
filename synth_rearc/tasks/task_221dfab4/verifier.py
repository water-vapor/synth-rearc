from __future__ import annotations

from synth_rearc.core import *


def _render_horizontal_221dfab4(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, F, T)
    x2 = first(colorfilter(x1, FOUR))
    x3 = uppermost(x2)
    x4 = leftmost(x2)
    x5 = rightmost(x2)
    x6 = I
    x7 = height(I)
    for x8 in range(x7):
        x9 = connect((x8, x4), (x8, x5))
        x10 = abs(x8 - x3)
        if x10 % TWO == ONE:
            x6 = fill(x6, x0, x9)
            continue
        x11 = x10 // TWO
        if x11 % THREE == TWO:
            x12 = frozenset((x8, x13) for x13, x14 in enumerate(I[x8]) if x14 != x0)
            x13 = combine(x12, x9)
            x6 = fill(x6, THREE, x13)
        else:
            x6 = fill(x6, FOUR, x9)
    return x6


def verify_221dfab4(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = first(colorfilter(x0, FOUR))
    if hline(x1):
        return _render_horizontal_221dfab4(I)
    x2 = rot90(I)
    x3 = _render_horizontal_221dfab4(x2)
    return rot270(x3)
