from synth_rearc.core import *


def verify_1a6449f1(I: Grid) -> Grid:
    x0 = remove(ZERO, palette(I))
    x1 = height(I)
    x2 = width(I)
    x3 = None
    x4 = NEG_ONE
    for x5 in x0:
        x6 = [[ZERO for _ in range(x2)] for _ in range(x1 + ONE)]
        for x7 in range(x1):
            for x8 in range(x2):
                x9 = branch(equality(I[x7][x8], x5), ONE, ZERO)
                x10 = add(x7, ONE)
                x6[x10][x8] = add(x6[x7][x8], x9)
        for x7 in range(x1 - TWO):
            for x8 in range(x7 + TWO, x1):
                x9 = add(subtract(x8, x7), ONE)
                x10 = F
                x11 = None
                x12 = None
                for x13 in range(x2 + ONE):
                    x14 = (
                        x13 < x2
                        and equality(I[x7][x13], x5)
                        and equality(I[x8][x13], x5)
                    )
                    if both(x14, flip(x10)):
                        x10 = T
                        x11 = None
                        x12 = None
                    if x14:
                        x15 = subtract(x6[x8 + ONE][x13], x6[x7][x13])
                        x16 = equality(x15, x9)
                        if x16:
                            if x11 is None:
                                x11 = x13
                            x12 = x13
                    if both(flip(x14), x10):
                        if x11 is not None and greater(subtract(x12, x11), ONE):
                            x17 = frozenset({(x7, x11), (x8, x12)})
                            x18 = size(backdrop(x17))
                            if greater(x18, x4):
                                x3 = x17
                                x4 = x18
                        x10 = F
    if x3 is None:
        raise RuntimeError("no rectangular frame found for 1a6449f1")
    x19 = add(ulcorner(x3), UNITY)
    x20 = subtract(shape(x3), TWO_BY_TWO)
    x21 = crop(I, x19, x20)
    return x21
