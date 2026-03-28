from arc2.core import *


def verify_5b37cb25(I: Grid) -> Grid:
    x0 = trim(I)
    x1 = mostcolor(x0)
    x2 = leastcolor(x0)
    x3 = decrement(height(I))
    x4 = decrement(width(I))
    x5 = index(I, (ZERO, ONE))
    x6 = index(I, (x3, ONE))
    x7 = index(I, (ONE, ZERO))
    x8 = index(I, (ONE, x4))
    x9 = lbind(index, I)
    x10 = ofcolor(I, x1)
    x11 = I
    for x12 in x10:
        x13 = insert(x12, dneighbors(x12))
        x14 = sfilter(x13, matcher(x9, x1))
        x15 = equality(size(x14), FIVE)
        if x15:
            x16 = add(x12, UP)
            x17 = add(x12, DOWN)
            x18 = add(x12, LEFT)
            x19 = add(x12, RIGHT)
            x20 = add(x16, UP)
            x21 = add(x17, DOWN)
            x22 = add(x18, LEFT)
            x23 = add(x19, RIGHT)
            x24 = index(I, x20)
            x25 = index(I, x21)
            x26 = index(I, x22)
            x27 = index(I, x23)
            x28 = equality(x24, x2)
            x29 = equality(x25, x2)
            x30 = equality(x26, x2)
            x31 = equality(x27, x2)
            x32 = x28 + x29 + x30 + x31
            if equality(x32, THREE):
                x33 = branch(
                    flip(x28),
                    x5,
                    branch(flip(x29), x6, branch(flip(x30), x7, x8)),
                )
                x11 = fill(x11, x33, x13)
    return x11
