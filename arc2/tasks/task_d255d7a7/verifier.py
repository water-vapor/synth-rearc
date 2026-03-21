from arc2.core import *

from .helpers import find_movable_caps_d255d7a7


def verify_d255d7a7(I: Grid) -> Grid:
    x0 = shape(I)
    x1 = canvas(SEVEN, x0)
    x2 = find_movable_caps_d255d7a7(I)
    x3 = frozenset()
    x4 = x1
    for x5, x6 in x2:
        x7 = toindices(x5)
        x3 = combine(x3, x7)
        x8 = shift(x5, x6)
        x4 = paint(x4, x8)
    x9 = ofcolor(I, NINE)
    x10 = difference(x9, x3)
    x11 = fill(x4, NINE, x10)
    return x11
