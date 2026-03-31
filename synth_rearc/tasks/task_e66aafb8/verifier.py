from synth_rearc.core import *


def verify_e66aafb8(I: Grid) -> Grid:
    x0 = ofcolor(I, ZERO)
    x1 = ulcorner(x0)
    x2 = shape(x0)
    x3 = (
        I,
        rot90(I),
        rot180(I),
        rot270(I),
        hmirror(I),
        vmirror(I),
        dmirror(I),
        cmirror(I),
    )
    x4 = height(I)
    x5 = width(I)
    x6 = []
    for x7 in range(x4):
        x8 = []
        for x9 in range(x5):
            x10 = []
            for x11 in x3:
                x12 = x11[x7][x9]
                if x12 != ZERO:
                    x10.append(x12)
            x8.append(x10[0])
        x6.append(tuple(x8))
    x13 = tuple(x6)
    return crop(x13, x1, x2)
