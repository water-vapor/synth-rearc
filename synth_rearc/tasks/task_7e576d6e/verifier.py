from synth_rearc.core import *


def verify_7e576d6e(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = leastcolor(I)
    x2 = replace(I, x1, x0)
    x3 = leastcolor(x2)
    x4 = objects(I, T, F, T)
    x5 = order(colorfilter(x4, x3), leftmost)
    x6 = vline(first(x5))
    x7 = leftmost if x6 else uppermost
    x8 = order(colorfilter(x4, x3), x7)
    x9 = order(colorfilter(x4, x1), x7)
    x10 = tuple(center(x11) for x11 in x8)
    x11 = tuple(center(x12) for x12 in x9)
    x12 = (x11[0],) + x10 + (x11[1],)
    x13 = set()
    x14 = len(x12) - ONE
    for x15 in range(x14):
        x16 = x12[x15]
        x17 = x12[x15 + ONE]
        x18 = x15 == x14 - ONE
        if x6:
            if x18:
                x19 = (x16[0], x17[1])
                x13 |= connect(x16, x19)
                x13 |= connect(x19, x17)
            else:
                x19 = ONE if x17[1] > x16[1] else NEG_ONE
                x20 = x17[1] - x19
                x21 = (x16[0], x20)
                x22 = (x17[0], x20)
                x13 |= connect(x16, x21)
                x13 |= connect(x21, x22)
                x13 |= connect(x22, x17)
        else:
            if x18:
                x19 = (x17[0], x16[1])
                x13 |= connect(x16, x19)
                x13 |= connect(x19, x17)
            else:
                x19 = ONE if x17[0] > x16[0] else NEG_ONE
                x20 = x17[0] - x19
                x21 = (x20, x16[1])
                x22 = (x20, x17[1])
                x13 |= connect(x16, x21)
                x13 |= connect(x21, x22)
                x13 |= connect(x22, x17)
    x23 = fill(I, x1, frozenset(x13))
    return x23
