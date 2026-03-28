from synth_rearc.core import *


def verify_22806e14(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = compose(size, backdrop)
    x2 = fork(equality, size, x1)
    x3 = compose(flip, x2)
    x4 = extract(x0, x3)
    x5 = remove(x4, x0)
    x6 = compose(flip, even)
    x7 = compose(x6, height)
    x8 = compose(x6, width)
    x9 = fork(both, x7, x8)
    x10 = sfilter(x5, x9)
    x11 = apply(centerofmass, x10)
    x12 = greater(size(x4), size(x10))
    x13 = branch(x12, cover(I, x4), I)
    x14 = color(x4)
    x15 = fill(x13, x14, x11)
    return x15
