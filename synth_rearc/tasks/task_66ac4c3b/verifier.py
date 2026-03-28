from synth_rearc.core import *


def verify_66ac4c3b(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = palette(I)
    x2 = remove(x0, x1)
    x3 = totuple(x2)
    x4 = lbind(colorcount, I)
    x5 = order(x3, x4)
    x6 = first(x5)
    x7 = last(x5)
    x8 = ofcolor(I, x6)
    x9 = frozenset(x10 for x10, x11 in x8)
    x10 = frozenset(x11 for x12, x11 in x8)
    x11 = equality(size(x9), ONE)
    x12 = ofcolor(I, x7)
    if x11:
        x13 = first(x9)
        x14 = {}
        for x15, x16 in x12:
            x14.setdefault(x15, set()).add(x16)
        x17 = tuple(x15 for x15, x16 in x14.items() if frozenset(x16) == x10)
        x18 = x13 <= len(I) - ONE - x13
        if x18:
            x19 = minimum(tuple(x20 for x20 in x17 if x20 > x13))
            x21 = frozenset((x22, x23) for x22, x23 in x12 if x22 < x13)
            x22 = subgrid(x21, I)
            x23 = hmirror(x22)
            x24 = subtract(subtract(x13, lowermost(x21)), ONE)
            x25 = add(increment(x19), x24)
            x26 = astuple(x25, leftmost(x21))
        else:
            x19 = maximum(tuple(x20 for x20 in x17 if x20 < x13))
            x21 = frozenset((x22, x23) for x22, x23 in x12 if x22 > x13)
            x22 = subgrid(x21, I)
            x23 = hmirror(x22)
            x24 = subtract(uppermost(x21), increment(x13))
            x25 = subtract(subtract(x19, x24), height(x22))
            x26 = astuple(x25, leftmost(x21))
        x27 = shift(ofcolor(x23, x7), x26)
        x28 = fill(I, x6, x27)
        return x28
    x13 = first(x10)
    x14 = {}
    for x15, x16 in x12:
        x14.setdefault(x16, set()).add(x15)
    x17 = tuple(x15 for x15, x16 in x14.items() if frozenset(x16) == x9)
    x18 = x13 <= len(I[ZERO]) - ONE - x13
    if x18:
        x19 = minimum(tuple(x20 for x20 in x17 if x20 > x13))
        x21 = frozenset((x22, x23) for x22, x23 in x12 if x23 < x13)
        x22 = subgrid(x21, I)
        x23 = vmirror(x22)
        x24 = subtract(subtract(x13, rightmost(x21)), ONE)
        x25 = add(increment(x19), x24)
        x26 = astuple(uppermost(x21), x25)
    else:
        x19 = maximum(tuple(x20 for x20 in x17 if x20 < x13))
        x21 = frozenset((x22, x23) for x22, x23 in x12 if x23 > x13)
        x22 = subgrid(x21, I)
        x23 = vmirror(x22)
        x24 = subtract(leftmost(x21), increment(x13))
        x25 = subtract(subtract(x19, x24), width(x22))
        x26 = astuple(uppermost(x21), x25)
    x27 = shift(ofcolor(x23, x7), x26)
    x28 = fill(I, x6, x27)
    return x28
