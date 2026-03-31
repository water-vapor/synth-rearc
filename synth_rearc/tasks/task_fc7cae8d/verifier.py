from synth_rearc.core import *


def verify_fc7cae8d(
    I: Grid,
) -> Grid:
    x0 = partition(I)
    x1 = rbind(bordering, I)
    x2 = compose(flip, x1)
    x3 = sfilter(x0, x2)
    x4 = argmax(x3, size)
    x5 = subgrid(x4, I)
    x6 = square(x5)
    x7 = rot270(x5)
    x8 = portrait(x5)
    x9 = cmirror(x5)
    x10 = dmirror(x5)
    x11 = branch(x8, x9, x10)
    x12 = branch(x6, x7, x11)
    return x12
