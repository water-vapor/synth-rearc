from synth_rearc.core import *


def verify_4c3d4a41(
    I: Grid,
) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = extract(x0, lambda x: both(equality(color(x), FIVE), greater(NINE, leftmost(x))))
    x2 = shift(x1, (ZERO, TEN))
    x3 = sfilter(x0, lambda x: color(x) != FIVE)
    x4 = cover(I, x1)
    x5 = frozenset((i, j) for i in range(ONE, SIX) for j in range(11, 19))
    x6 = fill(x4, ZERO, x5)
    x7 = frozenset((i, leftmost(x8)) for x8 in x3 for i in range(ONE, SIX))
    x9 = fill(x6, FIVE, x7)
    x10 = fill(x9, FIVE, x2)
    for x11 in x3:
        x12 = leftmost(x11)
        x13 = frozenset((i, j) for i, j in toindices(x2) if j == x12)
        x14 = uppermost(x13)
        x15 = maximum((ONE, subtract(x14, height(x11))))
        x16 = frozenset((i, x12) for i in range(x15, x14))
        x17 = recolor(color(x11), x16)
        x10 = paint(x10, x17)
    return x10
