from synth_rearc.core import *


def verify_d94c3b52(I: Grid) -> Grid:
    x0 = interval(ONE, height(I), FOUR)
    x1 = interval(ONE, width(I), FOUR)
    x2 = []
    x3 = None
    for x4 in x0:
        for x5 in x1:
            x6 = crop(I, (x4, x5), THREE_BY_THREE)
            x7 = difference(asindices(x6), ofcolor(x6, ZERO))
            x8 = divide(subtract(x4, ONE), FOUR)
            x9 = divide(subtract(x5, ONE), FOUR)
            x10 = shift(x7, (x4, x5))
            x11 = (x8, x9)
            x2.append((x11, x7, x10))
            if x3 is None and positive(colorcount(x6, EIGHT)):
                x3 = x7
    if x3 is None:
        return I
    x12 = frozenset(x13 for x13, x14, x15 in x2 if x14 == x3)
    x16 = I
    for x17, x18, x19 in x2:
        if x18 == x3:
            x16 = fill(x16, EIGHT, x19)
    x20 = frozenset()
    x21 = tuple(x12)
    for x22, x23 in enumerate(x21):
        for x24 in x21[x22 + ONE:]:
            x25 = equality(x23[ZERO], x24[ZERO])
            x26 = equality(x23[ONE], x24[ONE])
            if either(x25, x26):
                x27 = frozenset({x23, x24})
                x28 = difference(connect(x23, x24), x27)
                x20 = combine(x20, x28)
    for x29, x30, x31 in x2:
        if x29 in x12:
            continue
        if x29 in x20:
            x16 = fill(x16, SEVEN, x31)
    return x16
