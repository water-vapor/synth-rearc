from arc2.core import *

from .helpers import projected_strip_d93c6891


def verify_d93c6891(I: Grid) -> Grid:
    x0 = replace(I, FIVE, FOUR)
    x1 = replace(I, FIVE, SEVEN)
    x2 = objects(x1, T, F, F)
    x3 = colorfilter(x2, SEVEN)
    x4 = x0
    x5 = matcher(first, SEVEN)
    x6 = matcher(first, FIVE)
    for x7 in x3:
        x8 = toobject(x7, I)
        x9 = sfilter(x8, x5)
        x10 = sfilter(x8, x6)
        x11 = projected_strip_d93c6891(x9, x10)
        x4 = fill(x4, FIVE, x11)
    return x4
