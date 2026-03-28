from synth_rearc.core import *


def verify_358ba94e(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = totuple(x0)
    x2 = apply(size, x1)
    x3 = leastcommon(x2)
    x4 = matcher(size, x3)
    x5 = extract(x1, x4)
    x6 = subgrid(x5, I)
    return x6
