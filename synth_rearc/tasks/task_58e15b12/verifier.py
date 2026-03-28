from synth_rearc.core import *


def verify_58e15b12(I: Grid) -> Grid:
    x0 = remove(ZERO, palette(I))
    x1 = height(I)
    x2 = width(I)
    x3 = {}
    for x4 in x0:
        x5 = ofcolor(I, x4)
        x6 = uppermost(x5)
        x7 = height(x5)
        x8 = leftmost(x5)
        x9 = rightmost(x5)
        x10 = set()
        x11 = max(x1, x2)
        for x12 in range(x11):
            x13 = (ZERO,) if x12 == ZERO else (-ONE, ONE)
            for x14 in x13:
                x15 = x6 + (x14 * x12 * x7)
                x16 = max(ZERO, x15)
                x17 = min(x1, x15 + x7)
                if x16 >= x17:
                    continue
                for x18 in (x8 - x12, x9 + x12):
                    if ZERO <= x18 < x2:
                        x19 = connect((x16, x18), (decrement(x17), x18))
                        x10 |= set(x19)
        x3[x4] = frozenset(x10)
    x4 = {}
    for x5, x6 in x3.items():
        for x7 in x6:
            x4.setdefault(x7, set()).add(x5)
    x5 = canvas(ZERO, (x1, x2))
    x6 = frozenset({x7 for x7, x8 in x4.items() if len(x8) > ONE})
    x7 = difference(frozenset(x4.keys()), x6)
    x8 = frozenset({x9 for x9 in x7 if first(x4[x9]) == THREE})
    x9 = frozenset({x10 for x10 in x7 if first(x4[x10]) == EIGHT})
    x10 = fill(x5, THREE, x8)
    x11 = fill(x10, EIGHT, x9)
    x12 = fill(x11, SIX, x6)
    return x12
