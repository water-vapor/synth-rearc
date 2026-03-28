from arc2.core import *


def verify_5289ad53(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = size(colorfilter(x0, THREE))
    x2 = size(colorfilter(x0, TWO))
    x3 = repeat(THREE, x1)
    x4 = repeat(TWO, x2)
    x5 = repeat(ZERO, subtract(SIX, add(x1, x2)))
    x6 = combine(combine(x3, x4), x5)
    return (x6[:THREE], x6[THREE:SIX])
