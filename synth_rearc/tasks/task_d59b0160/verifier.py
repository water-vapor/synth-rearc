from synth_rearc.core import *


def verify_d59b0160(I: Grid) -> Grid:
    x0 = interval(ZERO, FOUR, ONE)
    x1 = product(x0, x0)
    x2 = crop(I, ORIGIN, (FOUR, FOUR))
    x3 = palette(x2)
    x4 = difference(x3, initset(THREE))
    x5 = difference(x4, initset(SEVEN))
    x6 = difference(palette(I), initset(SEVEN))
    x7 = I
    for x8 in x6:
        x7 = replace(x7, x8, ONE)
    x9 = replace(x7, SEVEN, ZERO)
    x10 = canvas(ZERO, (30, 30))
    x11 = paint(x10, asobject(x9))
    x12 = objects(x11, T, F, T)
    x13 = lbind(intersection, x1)
    x14 = chain(size, x13, toindices)
    x15 = matcher(x14, ZERO)
    x16 = sfilter(x12, x15)
    x17 = rbind(toobject, I)
    x18 = compose(palette, x17)
    x19 = lbind(intersection, x5)
    x20 = compose(x19, x18)
    x21 = matcher(x20, x5)
    x22 = sfilter(x16, x21)
    x23 = merge(x22)
    x24 = fill(I, SEVEN, x23)
    return x24
