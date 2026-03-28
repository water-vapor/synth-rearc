from synth_rearc.core import *


def verify_05a7bcf2(I: Grid) -> Grid:
    x0 = ofcolor(I, EIGHT)
    x1 = vline(x0)
    x2 = height(I)
    x3 = width(I)
    if x1:
        x4 = leftmost(x0)
        x5 = crop(I, ORIGIN, (x2, x4))
        x6 = colorcount(x5, FOUR)
        if positive(x6):
            x7 = I
            x8 = identity
        else:
            x7 = vmirror(I)
            x8 = vmirror
    else:
        x4 = uppermost(x0)
        x5 = crop(I, ORIGIN, (x4, x3))
        x6 = colorcount(x5, FOUR)
        if positive(x6):
            x7 = rot270(I)
            x8 = rot90
        else:
            x7 = rot90(I)
            x8 = rot270
    x9 = leftmost(ofcolor(x7, EIGHT))
    x10 = [list(row) for row in x7]
    x11 = len(x10)
    x12 = len(x10[ZERO])
    for x13 in range(x11):
        x14 = [x15 for x15 in range(x9) if x10[x13][x15] == FOUR]
        if len(x14) == ZERO:
            continue
        x16 = sum(x10[x13][x15] == TWO for x15 in range(x9 + ONE, x12))
        for x15 in x14:
            x10[x13][x15] = THREE
        for x15 in range(max(x14) + ONE, x9):
            x10[x13][x15] = FOUR
        for x15 in range(x9, x12 - x16):
            x10[x13][x15] = EIGHT
        for x15 in range(x12 - x16, x12):
            x10[x13][x15] = TWO
    x17 = tuple(tuple(row) for row in x10)
    x18 = x8(x17)
    return x18
