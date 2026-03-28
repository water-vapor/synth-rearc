from arc2.core import *


def verify_5587a8d0(I: Grid) -> Grid:
    x0 = fgpartition(I)
    x1 = tuple(sorted(x0, key=lambda x2: (-size(x2), uppermost(x2), leftmost(x2), color(x2))))
    x2 = size(x1)
    x3 = decrement(double(x2))
    x4 = astuple(x3, x3)
    x5 = color(last(x1))
    x6 = canvas(x5, x4)
    for x7, x8 in enumerate(x1[:-1]):
        x9 = subtract(x3, x7)
        x10 = interval(x7, x9, ONE)
        x11 = product(x10, x10)
        x12 = box(x11)
        x13 = color(x8)
        x6 = fill(x6, x13, x12)
    return x6
