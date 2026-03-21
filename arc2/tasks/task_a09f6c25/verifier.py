from arc2.core import *


def verify_a09f6c25(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = sizefilter(x0, ONE)
    x2 = difference(x0, x1)
    x3 = compose(normalize, vmirror)
    x4 = fork(equality, normalize, x3)
    x5 = compose(normalize, hmirror)
    x6 = fork(equality, normalize, x5)
    x7 = totuple(x2)
    x8 = apply(x4, x7)
    x9 = apply(x6, x7)

    def x10(a: Boolean, b: Boolean) -> Integer:
        return branch(a, THREE, branch(b, ONE, SIX))

    x11 = papply(x10, x8, x9)
    x12 = mpapply(recolor, x11, x7)
    x13 = canvas(mostcolor(I), shape(I))
    x14 = paint(x13, x12)
    return x14
