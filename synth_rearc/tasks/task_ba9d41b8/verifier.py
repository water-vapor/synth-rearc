from synth_rearc.core import *


def _checkerboard_rectangle_ba9d41b8(
    x0: Object,
) -> Object:
    x1 = color(x0)
    x2 = ulcorner(x0)
    x3 = fork(add, first, last)
    x4 = x3(x2)
    x5 = even(x4)
    x6 = toindices(x0)
    x7 = box(x0)
    x8 = difference(x6, x7)
    x9 = compose(even, x3)
    x10 = matcher(x9, flip(x5))
    x11 = sfilter(x8, x10)
    x12 = combine(x7, x11)
    x13 = recolor(x1, x12)
    return x13


def verify_ba9d41b8(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, F, T)
    x2 = canvas(x0, shape(I))
    x3 = apply(_checkerboard_rectangle_ba9d41b8, x1)
    x4 = merge(x3)
    x5 = paint(x2, x4)
    return x5
