from synth_rearc.core import *


def verify_7d419a02(I: Grid) -> Grid:
    x0 = greater(height(I), width(I))
    x1 = branch(x0, I, rot90(I))
    x2 = objects(x1, T, F, T)
    x3 = colorfilter(x2, SIX)
    x4 = extract(x3, matcher(size, FOUR))
    x5 = uppermost(x4)
    x6 = lowermost(x4)
    x7 = leftmost(x4)
    x8 = rightmost(x4)
    x9 = ofcolor(x1, EIGHT)
    x10 = frozenset(
        (x11, x12)
        for x11, x12 in x9
        if (
            ((x5 - x11 + TWO) // THREE if x11 < x5 else (x11 - x6 + TWO) // THREE if x11 > x6 else ZERO)
            <= ((x7 - x12 + ONE) // TWO if x12 < x7 else (x12 - x8 + ONE) // TWO if x12 > x8 else ZERO)
            and positive((x5 - x11 + TWO) // THREE if x11 < x5 else (x11 - x6 + TWO) // THREE if x11 > x6 else ZERO)
        )
    )
    x11 = fill(x1, FOUR, x10)
    x12 = branch(x0, x11, rot270(x11))
    return x12
