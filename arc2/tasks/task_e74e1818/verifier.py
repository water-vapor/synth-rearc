from arc2.core import *


def verify_e74e1818(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = fgpartition(I)
    x2 = apply(hmirror, x1)
    x3 = merge(x2)
    x4 = canvas(x0, shape(I))
    x5 = paint(x4, x3)
    return x5
