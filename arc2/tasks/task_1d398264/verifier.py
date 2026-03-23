from arc2.core import *


def verify_1d398264(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = first(x0)
    x2 = center(x1)
    x3 = initset(x2)
    x4 = toindices(x1)
    x5 = difference(x4, x3)
    x6 = lbind(index, I)
    x7 = rbind(subtract, x2)
    x8 = fork(shoot, identity, x7)
    x9 = fork(recolor, x6, x8)
    x10 = apply(x9, x5)
    x11 = merge(x10)
    x12 = paint(I, x11)
    return x12
