from arc2.core import *


def verify_64a7c07e(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, T, T)
    x2 = compose(tojvec, width)
    x3 = fork(shift, identity, x2)
    x4 = mapply(x3, x1)
    x5 = canvas(x0, shape(I))
    x6 = paint(x5, x4)
    return x6
