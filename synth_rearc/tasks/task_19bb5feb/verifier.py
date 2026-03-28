from synth_rearc.core import *


def verify_19bb5feb(I: Grid) -> Grid:
    x0 = ofcolor(I, EIGHT)
    x1 = subgrid(x0, I)
    x2 = vsplit(x1, TWO)
    x3 = tuple(hsplit(x4, TWO) for x4 in x2)
    x4 = []
    for x5 in x3:
        x6 = []
        for x7 in x5:
            x8 = remove(EIGHT, palette(x7))
            x9 = ZERO if equality(size(x8), ZERO) else first(x8)
            x6.append(x9)
        x4.append(tuple(x6))
    return tuple(x4)
