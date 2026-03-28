from synth_rearc.core import *


def verify_5a5a2103(
    I: Grid,
) -> Grid:
    x0 = frontiers(I)
    x1 = first(x0)
    x2 = color(x1)
    x3 = sfilter(x0, hline)
    x4 = sfilter(x0, vline)
    x5 = minimum(apply(uppermost, x3))
    x6 = minimum(apply(leftmost, x4))
    x7 = increment(x5)
    x8 = increment(x6)
    x9 = objects(I, T, T, T)
    x10 = matcher(color, x2)
    x11 = compose(flip, x10)
    x12 = sfilter(x9, x11)
    x13 = sizefilter(x12, FOUR)
    x14 = sfilter(x13, square)
    x15 = difference(x12, x14)
    x16 = argmax(x15, size)
    x17 = divide(uppermost(x16), x7)
    x18 = divide(leftmost(x16), x8)
    x19 = astuple(multiply(x17, x7), multiply(x18, x8))
    x20 = subtract(ulcorner(x16), x19)
    x21 = normalize(x16)
    x22 = order(x14, uppermost)
    x23 = width(I)
    x24 = interval(ZERO, x23, x8)
    x25 = canvas(ZERO, shape(I))
    x26 = paint(x25, merge(x0))
    x27 = x26
    for x28 in x22:
        x29 = divide(uppermost(x28), x7)
        x30 = multiply(x29, x7)
        x31 = color(x28)
        for x32 in x24:
            x33 = astuple(x30, x32)
            x34 = add(x33, x20)
            x35 = shift(x21, x34)
            x36 = recolor(x31, x35)
            x27 = paint(x27, x36)
    return x27
