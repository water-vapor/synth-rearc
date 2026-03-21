from arc2.core import *


def verify_c62e2108(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = sfilter(x0, compose(flip, matcher(color, ONE)))
    x2 = order(x1, ulcorner)
    x3 = ofcolor(I, ONE)
    x4 = canvas(ZERO, shape(I))
    x5 = height(I)
    x6 = width(I)
    for x7 in x2:
        x8 = ulcorner(x7)
        x9 = lrcorner(x7)
        x10 = connect((ZERO, x8[1]), (ZERO, x9[1]))
        x11 = connect((decrement(x5), x8[1]), (decrement(x5), x9[1]))
        x12 = connect((x8[0], ZERO), (x9[0], ZERO))
        x13 = connect((x8[0], decrement(x6)), (x9[0], decrement(x6)))
        x14 = equality(intersection(x3, x10), x10)
        x15 = equality(intersection(x3, x11), x11)
        x16 = equality(intersection(x3, x12), x12)
        x17 = equality(intersection(x3, x13), x13)
        x4 = paint(x4, x7)
        if x14:
            x18 = -FOUR
            while lowermost(shift(x7, (x18, ZERO))) >= ZERO:
                x4 = paint(x4, shift(x7, (x18, ZERO)))
                x18 = subtract(x18, FOUR)
        if x15:
            x19 = FOUR
            while uppermost(shift(x7, (x19, ZERO))) < x5:
                x4 = paint(x4, shift(x7, (x19, ZERO)))
                x19 = add(x19, FOUR)
        if x16:
            x20 = -FOUR
            while rightmost(shift(x7, (ZERO, x20))) >= ZERO:
                x4 = paint(x4, shift(x7, (ZERO, x20)))
                x20 = subtract(x20, FOUR)
        if x17:
            x21 = FOUR
            while leftmost(shift(x7, (ZERO, x21))) < x6:
                x4 = paint(x4, shift(x7, (ZERO, x21)))
                x21 = add(x21, FOUR)
    return x4
