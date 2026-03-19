from arc2.core import *


def verify_df8cc377(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = lambda x: both(greater(height(x), TWO), greater(width(x), TWO))
    x2 = lambda x: equality(toindices(x), box(x))
    x3 = fork(both, x1, x2)
    x4 = sfilter(x0, x3)
    x5 = apply(color, x4)
    x6 = fgpartition(I)
    x7 = lambda x: not contained(color(x), x5)
    x8 = sfilter(x6, x7)
    x9 = {size(x10): color(x10) for x10 in x8}
    x10 = canvas(ZERO, shape(I))
    for x11 in x4:
        x12 = ulcorner(x11)
        x13 = frozenset(
            x14 for x14 in delta(x11)
            if equality(even(x14[0] + x14[1]), even(x12[0] + x12[1]))
        )
        x15 = x9[size(x13)]
        x10 = fill(x10, x15, x13)
    x16 = merge(x4)
    x17 = paint(x10, x16)
    return x17
