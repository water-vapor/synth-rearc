from arc2.core import *


def verify_0becf7df(I: Grid) -> Grid:
    x0 = index(I, ORIGIN)
    x1 = index(I, RIGHT)
    x2 = index(I, DOWN)
    x3 = index(I, UNITY)
    x4 = switch(I, x0, x1)
    x5 = switch(x4, x2, x3)
    x6 = fill(x5, x0, initset(ORIGIN))
    x7 = fill(x6, x1, initset(RIGHT))
    x8 = fill(x7, x2, initset(DOWN))
    x9 = fill(x8, x3, initset(UNITY))
    return x9
