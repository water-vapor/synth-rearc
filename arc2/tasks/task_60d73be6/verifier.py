from arc2.core import *


def verify_60d73be6(I: Grid) -> Grid:
    x0 = frontiers(I)
    x1 = extract(x0, hline)
    x2 = extract(x0, vline)
    x3 = merge(x0)
    x4 = cover(I, x3)
    x5 = objects(x4, F, F, T)
    x6 = merge(x5)
    x7 = leftmost(x2)
    x8 = add(leftmost(x6), rightmost(x6))
    x9 = subtract(double(x7), x8)
    x10 = vmirror(x6)
    x11 = shift(x10, tojvec(x9))
    x12 = uppermost(x1)
    x13 = add(uppermost(x6), lowermost(x6))
    x14 = subtract(double(x12), x13)
    x15 = hmirror(x6)
    x16 = shift(x15, toivec(x14))
    x17 = hmirror(x11)
    x18 = shift(x17, toivec(x14))
    x19 = combine(x6, x11)
    x20 = combine(x16, x18)
    x21 = combine(x19, x20)
    x22 = paint(I, x21)
    return x22
