from synth_rearc.core import *


def verify_cfb2ce5a(I: Grid) -> Grid:
    x0 = crop(I, UNITY, (FOUR, FOUR))
    x1 = crop(I, (ONE, FIVE), (FOUR, FOUR))
    x2 = crop(I, (FIVE, ONE), (FOUR, FOUR))
    x3 = crop(I, (FIVE, FIVE), (FOUR, FOUR))
    x4 = vmirror(x0)
    x5 = hmirror(x0)
    x6 = rot180(x0)
    x7 = (x1, x2, x3)
    x8 = (x4, x5, x6)
    x9 = ()
    for x10, x11 in zip(x7, x8):
        x12 = {x13: ZERO for x14 in x11 for x13 in x14}
        for x13 in range(FOUR):
            for x14 in range(FOUR):
                x15 = x10[x13][x14]
                if x15 != ZERO:
                    x12[x11[x13][x14]] = x15
        x16 = tuple(tuple(x12[x17] for x17 in x18) for x18 in x11)
        x9 = x9 + (x16,)
    x17 = hconcat(x0, x9[ZERO])
    x18 = hconcat(x9[ONE], x9[TWO])
    x19 = vconcat(x17, x18)
    x20 = canvas(ZERO, shape(I))
    x21 = shift(asobject(x19), UNITY)
    x22 = paint(x20, x21)
    return x22
