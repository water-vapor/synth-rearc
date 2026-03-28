from synth_rearc.core import *


def verify_50c07299(I: Grid) -> Grid:
    x0 = objects(I, T, T, T)
    x1 = merge(x0)
    x2 = size(x1)
    x3 = increment(x2)
    x4 = urcorner(x1)
    x5 = multiply(x3, UP_RIGHT)
    x6 = add(x4, x5)
    x7 = add(x4, UP_RIGHT)
    x8 = connect(x6, x7)
    x9 = recolor(color(x1), x8)
    x10 = canvas(mostcolor(I), shape(I))
    x11 = paint(x10, x9)
    return x11
