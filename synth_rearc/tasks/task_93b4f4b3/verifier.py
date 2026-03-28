from synth_rearc.core import *


def verify_93b4f4b3(
    I: Grid,
) -> Grid:
    x0 = lefthalf(I)
    x1 = righthalf(I)
    x2 = objects(x0, T, F, F)
    x3 = colorfilter(x2, ZERO)
    x4 = objects(x1, T, F, T)
    x5 = compose(normalize, toindices)
    x6 = lbind(matcher, x5)
    x7 = compose(x6, x5)
    x8 = lbind(extract, x4)
    x9 = compose(x8, x7)
    x10 = compose(color, x9)
    x11 = fork(recolor, x10, identity)
    x12 = apply(x11, x3)
    x13 = merge(x12)
    x14 = paint(x0, x13)
    return x14
