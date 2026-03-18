from arc2.core import *


def verify_09c534e7(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = order(x0, ulcorner)
    x2 = apply(toindices, x1)
    x3 = apply(rbind(shift, NEG_UNITY), x2)
    x4 = papply(intersection, x2, x3)
    x5 = apply(rbind(shift, UP), x2)
    x6 = papply(intersection, x4, x5)
    x7 = apply(rbind(shift, UP_RIGHT), x2)
    x8 = papply(intersection, x6, x7)
    x9 = apply(rbind(shift, LEFT), x2)
    x10 = papply(intersection, x8, x9)
    x11 = apply(rbind(shift, RIGHT), x2)
    x12 = papply(intersection, x10, x11)
    x13 = apply(rbind(shift, DOWN_LEFT), x2)
    x14 = papply(intersection, x12, x13)
    x15 = apply(rbind(shift, DOWN), x2)
    x16 = papply(intersection, x14, x15)
    x17 = apply(rbind(shift, UNITY), x2)
    x18 = papply(intersection, x16, x17)
    x19 = compose(rbind(other, ONE), palette)
    x20 = apply(x19, x1)
    x21 = mpapply(recolor, x20, x18)
    x22 = paint(I, x21)
    return x22
