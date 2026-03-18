from arc2.core import *

from .helpers import settle_left_objects_f0100645, settle_right_objects_f0100645


def verify_f0100645(I: Grid) -> Grid:
    x0 = shape(I)
    x1 = first(I)
    x2 = first(x1)
    x3 = last(x1)
    x4 = mostcolor(I)
    x5 = height(I)
    x6 = width(I)
    x7 = decrement(x6)
    x8 = frozenset((i, ZERO) for i in range(x5))
    x9 = frozenset((i, x7) for i in range(x5))
    x10 = objects(I, T, T, F)
    x11 = tuple(obj for obj in colorfilter(x10, x2) if leftmost(obj) > ZERO)
    x12 = tuple(obj for obj in colorfilter(x10, x3) if rightmost(obj) < x7)
    x13 = settle_left_objects_f0100645(x11, x8, x6)
    x14 = settle_right_objects_f0100645(x12, x9, x6)
    x15 = canvas(x4, x0)
    x16 = fill(x15, x2, x8)
    x17 = fill(x16, x3, x9)
    x18 = paint(x17, merge(x13))
    x19 = paint(x18, merge(x14))
    return x19
