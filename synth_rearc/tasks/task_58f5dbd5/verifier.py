from synth_rearc.core import *


def verify_58f5dbd5(
    I: Grid,
) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, F, T)
    x2 = multiply(FIVE, FIVE)
    x3 = sfilter(x1, matcher(size, x2))
    x4 = sfilter(x3, square)
    x5 = merge(apply(toindices, x4))
    x6 = outbox(x5)
    x7 = canvas(x0, shape(x6))
    x8 = fgpartition(I)
    x9 = invert(ulcorner(x6))
    x10 = x7
    for x11 in x4:
        x12 = color(x11)
        x13 = first(colorfilter(x8, x12))
        x14 = difference(x13, x11)
        x15 = normalize(x14)
        x16 = delta(x15)
        x17 = add(ulcorner(x11), UNITY)
        x18 = shift(x16, x17)
        x19 = combine(box(x11), x18)
        x20 = recolor(x12, x19)
        x21 = shift(x20, x9)
        x10 = paint(x10, x21)
    return x10
