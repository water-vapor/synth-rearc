from synth_rearc.core import *


def verify_423a55dc(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = first(x0)
    x2 = lowermost(x1)
    x3 = apply(initset, x1)
    x4 = rbind(subtract, x2)
    x5 = chain(tojvec, x4, uppermost)
    x6 = fork(shift, identity, x5)
    x7 = mapply(x6, x3)
    x8 = canvas(ZERO, shape(I))
    x9 = paint(x8, x7)
    return x9
