from synth_rearc.core import *


def verify_fea12743(I: Grid) -> Grid:
    x0 = crop(I, (ONE, ONE), (FOUR, FOUR))
    x1 = crop(I, (ONE, SIX), (FOUR, FOUR))
    x2 = crop(I, (SIX, ONE), (FOUR, FOUR))
    x3 = crop(I, (SIX, SIX), (FOUR, FOUR))
    x4 = crop(I, (11, ONE), (FOUR, FOUR))
    x5 = crop(I, (11, SIX), (FOUR, FOUR))
    x6 = (x0, x1, x2, x3, x4, x5)
    x7 = tuple(ofcolor(x8, TWO) for x8 in x6)
    x8 = None
    for x9 in range(SIX):
        x10 = x7[x9]
        for x11 in range(SIX):
            for x12 in range(x11 + ONE, SIX):
                if x9 in (x11, x12):
                    continue
                x13 = x7[x11]
                x14 = x7[x12]
                if x13 == x14 or x13 == x10 or x14 == x10:
                    continue
                if combine(x13, x14) == x10:
                    x8 = (x11, x12, x9)
                    break
            if x8 is not None:
                break
        if x8 is not None:
            break
    if x8 is None:
        return I
    x15 = ((ONE, ONE), (ONE, SIX), (SIX, ONE), (SIX, SIX), (11, ONE), (11, SIX))
    x16, x17, x18 = x8
    x19 = shift(x7[x16], x15[x16])
    x20 = shift(x7[x17], x15[x17])
    x21 = shift(x7[x18], x15[x18])
    x22 = fill(I, EIGHT, x19)
    x23 = fill(x22, EIGHT, x20)
    x24 = fill(x23, THREE, x21)
    return x24
