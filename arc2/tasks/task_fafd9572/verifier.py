from arc2.core import *


def verify_fafd9572(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, ONE)
    x2 = difference(x0, x1)
    x3 = objects(I, T, T, T)
    x4 = colorfilter(x3, ONE)
    x5 = fork(astuple, uppermost, leftmost)
    x6 = order(x2, x5)
    x7 = apply(color, x6)
    x8 = order(x4, x5)
    x9 = mpapply(recolor, x7, x8)
    x10 = paint(I, x9)
    return x10
