from synth_rearc.core import *


def verify_2a5f8217(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, ONE)
    x2 = difference(x0, x1)
    x3 = compose(toindices, normalize)
    x4 = lbind(matcher, x3)
    x5 = compose(x4, x3)
    x6 = lbind(extract, x2)
    x7 = compose(x6, x5)
    x8 = compose(color, x7)
    x9 = fork(recolor, x8, identity)
    x10 = mapply(x9, x1)
    x11 = paint(I, x10)
    return x11
