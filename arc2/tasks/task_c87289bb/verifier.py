from arc2.core import *


def verify_c87289bb(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, TWO)
    x2 = ofcolor(I, EIGHT)
    x3 = tuple(sorted(j for i, j in x2 if i == ZERO))
    x4 = decrement(uppermost(merge(x1)))
    x5 = decrement(height(I))
    x6 = width(I)
    x7 = {
        j: (
            r + ONE
            if l == ZERO
            else l - ONE
            if r == x6 - ONE
            else l - ONE
            if j - l < r - j
            else r + ONE
        )
        for x8 in x1
        for l, r in ((leftmost(x8), rightmost(x8)),)
        for j in range(l, r + ONE)
    }
    x8 = tuple(
        combine(
            connect((x4, j), (x4, x7.get(j, j))),
            connect((x4, x7.get(j, j)), (x5, x7.get(j, j))),
        )
        for j in x3
    )
    x9 = fill(I, EIGHT, merge(x8))
    return x9
