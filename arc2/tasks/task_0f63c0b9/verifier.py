from arc2.core import *


def verify_0f63c0b9(I: Grid) -> Grid:
    x0 = order(objects(I, T, F, T), uppermost)
    x1 = apply(color, x0)
    x2 = apply(uppermost, x0)
    x3 = tuple((a + b) // TWO for a, b in zip(x2, x2[ONE:]))
    x4 = (ZERO,) + tuple(a + ONE for a in x3)
    x5 = x3 + (height(I) - ONE,)
    x6 = width(I) - ONE
    x7 = height(I) - ONE
    x8 = canvas(ZERO, shape(I))
    for x9, x10, x11, x12 in zip(x1, x4, x5, x2):
        x13 = product(interval(x10, x11 + ONE, ONE), (ZERO, x6))
        x8 = fill(x8, x9, x13)
        x14 = connect((x12, ZERO), (x12, x6))
        x8 = fill(x8, x9, x14)
    x15 = connect((ZERO, ZERO), (ZERO, x6))
    x16 = fill(x8, x1[ZERO], x15)
    x17 = connect((x7, ZERO), (x7, x6))
    x18 = fill(x16, x1[NEG_ONE], x17)
    return x18
