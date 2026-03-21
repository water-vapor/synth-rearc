from arc2.core import *


def verify_ac3e2b04(I: Grid) -> Grid:
    x0 = width(I)
    x1 = ofcolor(I, ZERO)
    x2 = tuple(
        x3
        for x3 in range(x0)
        if equality(size(intersection(x1, vfrontier((ZERO, x3)))), ZERO)
    )
    x3 = equality(size(x2), ZERO)
    x4 = branch(x3, rot90(I), I)
    x5 = width(x4)
    x6 = ofcolor(x4, ZERO)
    x7 = tuple(
        x8
        for x8 in range(x5)
        if equality(size(intersection(x6, vfrontier((ZERO, x8)))), ZERO)
    )
    x8 = objects(x4, T, F, T)
    x9 = colorfilter(x8, THREE)
    x10 = sfilter(
        x9,
        lambda x11: both(
            equality(size(x11), EIGHT),
            equality(size(backdrop(x11)), NINE),
        ),
    )
    x11 = apply(center, x10)
    x12 = ofcolor(x4, THREE)
    x13 = x4
    for x14 in x11:
        x15 = hfrontier(toivec(x14[ZERO]))
        x13 = underfill(x13, ONE, x15)
        for x16 in x7:
            x17 = initset((x14[ZERO], x16))
            x18 = difference(outbox(x17), x12)
            x13 = fill(x13, ONE, x18)
    x19 = branch(x3, rot270(x13), x13)
    return x19
