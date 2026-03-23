from arc2.core import *

from .helpers import shifted_copy_1e5d6875


def verify_1e5d6875(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = toindices(merge(x0))
    x2 = colorfilter(x0, FIVE)
    x3 = frozenset(shifted_copy_1e5d6875(x4) for x4 in x2)
    x4 = frozenset(recolor(FOUR, difference(toindices(x5), x1)) for x5 in x3)
    x5 = paint(I, merge(x4))
    x6 = colorfilter(x0, TWO)
    x7 = frozenset(shifted_copy_1e5d6875(x8) for x8 in x6)
    x8 = frozenset(recolor(THREE, difference(toindices(x9), x1)) for x9 in x7)
    x9 = paint(x5, merge(x8))
    return x9
