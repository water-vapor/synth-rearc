from synth_rearc.core import *


def verify_4acc7107(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = objects(I, T, F, T)
    x3 = remove(ZERO, palette(I))
    x4 = lbind(colorfilter, x2)
    x5 = fork(astuple, leftmost, uppermost)
    x6 = rbind(argmin, x5)
    x7 = compose(x6, x4)
    x8 = compose(x5, x7)
    x9 = order(x3, x8)
    x10 = canvas(ZERO, astuple(x0, x1))
    x11 = ZERO
    x12 = x10
    for x13 in x9:
        x14 = x4(x13)
        x15 = order(x14, x5)
        x16 = first(x15)
        x17 = last(x15)
        x18 = normalize(x16)
        x19 = normalize(x17)
        x20 = maximum((width(x18), width(x19)))
        x21 = subtract(x0, height(x18))
        x22 = subtract(x21, increment(height(x19)))
        x23 = shift(x19, astuple(x22, x11))
        x24 = shift(x18, astuple(x21, x11))
        x12 = paint(x12, x23)
        x12 = paint(x12, x24)
        x11 = add(x11, increment(x20))
    return x12
