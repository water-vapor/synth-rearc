from arc2.core import *


def verify_55059096(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, THREE)
    x2 = apply(centerofmass, x1)
    x3 = prapply(connect, x2, x2)
    x4 = fork(equality, height, width)
    x5 = matcher(size, ONE)
    x6 = compose(flip, x5)
    x7 = fork(both, x4, x6)
    x8 = mfilter(x3, x7)
    x9 = underfill(I, TWO, x8)
    return x9
