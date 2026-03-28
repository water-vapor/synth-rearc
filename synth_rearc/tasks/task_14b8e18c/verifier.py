from synth_rearc.core import *


def verify_14b8e18c(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = compose(square, backdrop)
    x2 = sfilter(x0, x1)
    x3 = matcher(height, ONE)
    x4 = compose(flip, x3)
    x5 = sfilter(x2, x4)
    x6 = lbind(mapply, dneighbors)
    x7 = compose(x6, corners)
    x8 = fork(intersection, x7, outbox)
    x9 = lbind(recolor, TWO)
    x10 = compose(x9, x8)
    x11 = mapply(x10, x5)
    x12 = underpaint(I, x11)
    return x12
