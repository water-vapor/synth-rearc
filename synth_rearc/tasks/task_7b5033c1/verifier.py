from synth_rearc.core import *


def verify_7b5033c1(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = tuple(x0)
    x2 = {}
    for x3 in x1:
        x4 = remove(x3, x0)
        x5 = sfilter(x4, lbind(adjacent, x3))
        x2[x3] = order(x5, ulcorner)
    x6 = tuple(x7 for x7 in x1 if len(x2[x7]) <= ONE)
    x7 = first(order(x6, ulcorner))
    x8 = []
    x9 = None
    x10 = x7
    while True:
        x8.append(x10)
        x11 = tuple(x12 for x12 in x2[x10] if x12 != x9)
        if len(x11) == ZERO:
            break
        x9 = x10
        x10 = first(x11)
    x13 = sum(size(x14) for x14 in x8)
    x14 = canvas(ZERO, (x13, ONE))
    x15 = ZERO
    for x16 in x8:
        x17 = connect((x15, ZERO), (add(x15, decrement(size(x16))), ZERO))
        x14 = fill(x14, color(x16), x17)
        x15 = add(x15, size(x16))
    return x14
