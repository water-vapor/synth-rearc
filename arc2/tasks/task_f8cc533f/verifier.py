from arc2.core import *


def verify_f8cc533f(I: Grid) -> Grid:
    x0 = fgpartition(I)
    x1 = compose(toindices, normalize)
    x2 = mapply(x1, x0)
    x3 = I
    for x4 in x0:
        x5 = color(x4)
        x6 = ulcorner(x4)
        x7 = recolor(x5, shift(x2, x6))
        x3 = paint(x3, x7)
    return x3
