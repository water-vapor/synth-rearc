from synth_rearc.core import *


def verify_ac0c2ac3(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = center(asindices(I))
    x2 = initset(x1)
    x3 = order(
        x0,
        lambda x4: decrement(maximum(shape(combine(toindices(x4), x2)))),
    )
    x4 = canvas(mostcolor(I), shape(I))
    x5 = x4
    for x6 in x3[::-1]:
        x7 = color(x6)
        x8 = decrement(maximum(shape(combine(toindices(x6), x2))))
        x9 = astuple(x8, x8)
        x10 = subtract(x1, x9)
        x11 = add(x1, x9)
        x12 = insert(x10, initset(x11))
        x13 = backdrop(x12)
        x5 = fill(x5, x7, x13)
    return x5
