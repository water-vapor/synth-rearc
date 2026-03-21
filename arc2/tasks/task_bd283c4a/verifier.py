from arc2.core import *

from .helpers import pack_histogram_bottom_up


def verify_bd283c4a(I: Grid) -> Grid:
    x0 = order(palette(I), identity)
    x1 = lbind(colorcount, I)
    x2 = compose(invert, x1)
    x3 = order(x0, x2)
    x4 = apply(x1, x3)
    x5 = pack_histogram_bottom_up(shape(I), x3, x4)
    return x5
