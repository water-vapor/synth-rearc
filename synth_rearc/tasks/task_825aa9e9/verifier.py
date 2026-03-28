from synth_rearc.core import *


def verify_825aa9e9(I: Grid) -> Grid:
    x0 = palette(I)
    x1 = last(I)
    x2 = tuple(x3 for x3 in x0 if flip(contained(x3, x1)))
    x3 = lbind(colorcount, I)
    x4 = argmin(x2, x3)
    x5 = remove(x4, x0)
    x6 = extract(x5, lambda x7: contained(x7, x1))
    x7 = other(x5, x6)
    x8 = objects(I, T, F, T)
    x9 = colorfilter(x8, x4)
    x10 = ofcolor(I, x6)
    x11 = shift(x10, UP)
    x12 = decrement(height(I))
    x13 = frozenset((x12, x14) for x14 in interval(ZERO, width(I), ONE))
    x14 = combine(x10, combine(x11, x13))
    x15 = fill(I, x7, mapply(toindices, x9))
    x16 = order(x9, lowermost)
    x17 = x15
    x18 = x14
    for x19 in x16[::-1]:
        x20 = x19
        while True:
            x21 = shift(x20, DOWN)
            x22 = intersection(toindices(x21), x18)
            x23 = positive(size(x22))
            if x23:
                break
            x20 = x21
        x17 = paint(x17, x20)
        x18 = combine(x18, toindices(x20))
    return x17
