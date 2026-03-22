from arc2.core import *


def verify_9344f635(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = sizefilter(x0, TWO)
    x2 = sfilter(x1, vline)
    x3 = sfilter(x1, hline)
    x4 = mostcolor(I)
    x5 = canvas(x4, shape(I))
    x6 = compose(vfrontier, ulcorner)
    x7 = fork(recolor, color, x6)
    x8 = mapply(x7, x2)
    x9 = paint(x5, x8)
    x10 = compose(hfrontier, ulcorner)
    x11 = fork(recolor, color, x10)
    x12 = mapply(x11, x3)
    x13 = paint(x9, x12)
    return x13
