from synth_rearc.core import *


def verify_50a16a69(I: Grid) -> Grid:
    x0 = compress(I)
    x1 = asobject(x0)
    x2 = vperiod(x1)
    x3 = hperiod(x1)
    x4 = crop(x0, ORIGIN, (x2, x3))
    x5 = height(I)
    x6 = width(I)
    x7 = tuple(
        tuple(x4[i % x2][(j + ONE) % x3] for j in range(x6))
        for i in range(x5)
    )
    return x7
