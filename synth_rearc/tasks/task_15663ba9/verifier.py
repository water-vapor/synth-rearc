from synth_rearc.core import *

from .helpers import corner_mark_15663ba9, exterior_background_15663ba9


def verify_15663ba9(I: Grid) -> Grid:
    x0 = palette(I)
    x1 = remove(ZERO, x0)
    x2 = first(x1)
    x3 = ofcolor(I, x2)
    x4 = exterior_background_15663ba9(I)
    x5 = frozenset(
        x6 for x6 in x3 if equality(corner_mark_15663ba9(I, x6, x2, x4), FOUR)
    )
    x6 = frozenset(
        x7 for x7 in x3 if equality(corner_mark_15663ba9(I, x7, x2, x4), TWO)
    )
    x7 = fill(I, FOUR, x5)
    x8 = fill(x7, TWO, x6)
    return x8
