from arc2.core import *


def _swap_segment_f0f8a26d(
    x0: Object,
) -> Object:
    x1 = center(x0)
    x2 = halve(size(x0))
    x3 = subtract(x1, toivec(x2))
    x4 = add(x1, toivec(x2))
    x5 = connect(x3, x4)
    x6 = subtract(x1, tojvec(x2))
    x7 = add(x1, tojvec(x2))
    x8 = connect(x6, x7)
    x9 = branch(hline(x0), x5, x8)
    x10 = recolor(color(x0), x9)
    return x10


def verify_f0f8a26d(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, F, T)
    x2 = canvas(x0, shape(I))
    x3 = apply(_swap_segment_f0f8a26d, x1)
    x4 = merge(x3)
    x5 = paint(x2, x4)
    return x5
