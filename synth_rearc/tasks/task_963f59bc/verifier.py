from synth_rearc.core import *


def verify_963f59bc(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, ONE)
    x2 = merge(x1)
    x3 = difference(x0, x1)
    x4 = vmirror(x2)
    x5 = hmirror(x2)
    x6 = rightmost(x2)
    x7 = I
    x8 = compose(first, last)
    x9 = compose(last, last)
    for x10 in x3:
        x11 = first(x10)
        x12 = first(x11)
        x13 = last(x11)
        x14 = last(x13)
        x15 = greater(x14, x6)
        if x15:
            x16 = first(x13)
            x17 = sfilter(x4, matcher(x8, x16))
            x18 = argmax(x17, x9)
            x19 = shift(x4, subtract(x13, last(x18)))
        else:
            x20 = sfilter(x5, matcher(x9, x14))
            x21 = argmax(x20, x8)
            x19 = shift(x5, subtract(x13, last(x21)))
        x22 = recolor(x12, x19)
        x7 = paint(x7, x22)
    return x7
