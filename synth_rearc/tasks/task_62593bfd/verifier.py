from synth_rearc.core import *


def verify_62593bfd(
    I: Grid,
) -> Grid:
    x0 = objects(I, T, T, T)
    x1 = sizefilter(x0, THREE)
    x2 = sizefilter(x0, SEVEN)
    x3 = sizefilter(x0, NINE)
    x4 = combine(x1, x2)
    x5 = combine(x4, x3)
    x6 = difference(x0, x5)
    x7 = height(I)
    x8 = lambda x9: shift(x9, toivec(invert(uppermost(x9))))
    x9 = lambda x10: shift(x10, toivec(subtract(decrement(x7), lowermost(x10))))
    x10 = mapply(x8, x5)
    x11 = mapply(x9, x6)
    x12 = canvas(mostcolor(I), shape(I))
    x13 = paint(x12, combine(x10, x11))
    return x13
