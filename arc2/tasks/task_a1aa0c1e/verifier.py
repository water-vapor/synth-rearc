from arc2.core import *


def verify_a1aa0c1e(I: Grid) -> Grid:
    x0 = frontiers(I)
    x1 = sfilter(x0, hline)
    x2 = matcher(color, ZERO)
    x3 = compose(flip, x2)
    x4 = sfilter(x1, x3)
    x5 = order(x4, uppermost)
    x6 = apply(color, x5)
    x7 = x6[:THREE]
    x8 = x6[NEG_ONE]
    x9 = apply(uppermost, x5)
    x10 = uppermost(ofcolor(I, FIVE))
    x11 = tuple((len({i for i, j in ofcolor(I, x12)}) - ONE) // TWO for x12 in x7)
    x12 = tuple(
        x13
        for x13, (x14, x15) in enumerate(zip(x9[:THREE], x9[ONE:]))
        if x14 < x10 < x15
    )[ZERO]
    x13 = tuple(x14 for x14 in x11 if x14 > ZERO)
    x14 = min(x13)
    x15 = tuple(x16 for x16, x17 in enumerate(x11) if x17 == x14)
    x16 = x12 if x12 in x15 else x15[ZERO]
    x17 = canvas(ZERO, (THREE, FIVE))
    for x18, x19, x20 in zip(interval(ZERO, THREE, ONE), x7, x11):
        x21 = product(initset(x18), interval(ZERO, x20, ONE))
        x17 = fill(x17, x19, x21)
    x22 = product(interval(ZERO, THREE, ONE), initset(THREE))
    x23 = fill(x17, x8, x22)
    x24 = fill(x23, FIVE, initset((x16, FOUR)))
    return x24
