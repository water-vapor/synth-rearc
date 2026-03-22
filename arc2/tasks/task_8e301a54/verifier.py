from arc2.core import *


def verify_8e301a54(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = compose(toivec, size)
    x2 = fork(shift, identity, x1)
    x3 = mapply(x2, x0)
    x4 = mostcolor(I)
    x5 = shape(I)
    x6 = canvas(x4, x5)
    x7 = paint(x6, x3)
    return x7
