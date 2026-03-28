from synth_rearc.core import *


def verify_22a4bbc2(I: Grid) -> Grid:
    x0 = objects(I, T, F, F)
    x1 = matcher(color, ZERO)
    x2 = compose(flip, x1)
    x3 = sfilter(x0, x2)
    x4 = fork(astuple, uppermost, leftmost)
    x5 = order(x3, x4)
    x6 = interval(ZERO, size(x5), ONE)
    x7 = pair(x6, x5)
    x8 = compose(rbind(divide, THREE), first)
    x9 = compose(lbind(multiply, THREE), x8)
    x10 = fork(equality, first, x9)
    x11 = sfilter(x7, x10)
    x12 = apply(last, x11)
    x13 = mapply(lbind(recolor, TWO), x12)
    x14 = paint(I, x13)
    return x14
