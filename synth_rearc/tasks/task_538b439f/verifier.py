from synth_rearc.core import *


def verify_538b439f(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = frontiers(I)
    x2 = compose(flip, matcher(color, x0))
    x3 = sfilter(x1, x2)
    x4 = first(x3)
    x5 = color(x4)
    x6 = objects(I, T, F, T)
    x7 = remove(x4, x6)
    x8 = lambda x: both(greater(size(x), THREE), equality(size(x), size(backdrop(x))))
    x9 = sfilter(x7, x8)
    x10 = vline(x4)
    x11 = I
    for x12 in x9:
        if x10:
            x13 = vmirror(x12)
            x14 = add(leftmost(x12), rightmost(x12))
            x15 = multiply(TWO, leftmost(x4))
            x16 = subtract(x15, x14)
            x17 = shift(x13, (ZERO, x16))
        else:
            x13 = hmirror(x12)
            x14 = add(uppermost(x12), lowermost(x12))
            x15 = multiply(TWO, uppermost(x4))
            x16 = subtract(x15, x14)
            x17 = shift(x13, (x16, ZERO))
        x18 = combine(x12, x17)
        x19 = backdrop(x18)
        x11 = fill(x11, x5, x19)
        x11 = paint(x11, x12)
        x11 = paint(x11, x17)
    return x11
