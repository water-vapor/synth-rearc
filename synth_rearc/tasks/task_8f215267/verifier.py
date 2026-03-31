from synth_rearc.core import *


FRAME_CELL_COUNT_8F215267 = 28
FRAME_WIDTH_8F215267 = 11


def verify_8f215267(
    I: Grid,
) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, F, T)
    x2 = tuple(
        x3 for x3 in x1
        if size(x3) == FRAME_CELL_COUNT_8F215267 and height(x3) == FIVE and width(x3) == FRAME_WIDTH_8F215267
    )
    x3 = tuple(sorted(x2, key=lambda x4: (uppermost(x4), leftmost(x4))))
    x4 = tuple(x5 for x5 in x1 if x5 not in x2)
    x5 = canvas(x0, shape(I))
    for x6 in x3:
        x5 = paint(x5, x6)
    for x7 in x3:
        x8 = color(x7)
        x9 = tuple(x10 for x10 in x4 if color(x10) == x8)
        x10 = len(x9)
        if x10 == ZERO:
            continue
        x11 = uppermost(x7) + TWO
        x12 = rightmost(x7)
        x13 = frozenset((x11, x12 - TWO * x14) for x14 in range(ONE, x10 + ONE))
        x5 = fill(x5, x8, x13)
    return x5
