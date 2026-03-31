from synth_rearc.core import *


def verify_b99e7126(
    I: Grid,
) -> Grid:
    x0 = I
    x1 = interval(ONE, height(x0), FOUR)
    x2 = interval(ONE, width(x0), FOUR)
    x3 = tuple(tuple(crop(x0, (i, j), (THREE, THREE)) for j in x2) for i in x1)
    x4 = tuple(block for row in x3 for block in row)
    x5 = mostcommon(x4)
    x6 = tuple(block for block in x4 if block != x5)
    x7 = mostcommon(x6)
    x8 = next(iter(difference(palette(x7), palette(x5))))
    x9 = ofcolor(x7, x8)
    x10 = frozenset((i, j) for i, row in enumerate(x3) for j, block in enumerate(row) if block == x7)
    x11 = None
    for x12 in range(FIVE):
        for x13 in range(FIVE):
            x14 = shift(x9, (x12, x13))
            if x10.issubset(x14):
                x11 = (x12, x13)
                break
        if x11 is not None:
            break
    x15 = shift(x9, x11)
    x16 = asobject(x7)
    x17 = x0
    for x18, x19 in x15:
        x20 = shift(x16, (ONE + FOUR * x18, ONE + FOUR * x19))
        x17 = paint(x17, x20)
    return x17
