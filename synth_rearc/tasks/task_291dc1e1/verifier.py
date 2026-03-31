from synth_rearc.core import *


def verify_291dc1e1(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = extract(x0, lambda x: contained(ZERO, palette(x)))
    x2 = remove(x1, x0)
    x3 = ulcorner(ofcolor(I, ZERO))
    x4 = equality(last(x3), ZERO)
    x5 = add(x3, branch(x4, (ZERO, ONE), (ZERO, -ONE)))
    x6 = index(I, x5)
    if equality(x6, ONE):
        x7 = order(
            x2,
            lambda x8: (uppermost(x8), leftmost(x8) if x4 else -leftmost(x8)),
        )
        x8 = tuple(subgrid(x9, I) for x9 in x7)
    else:
        x7 = order(
            x2,
            lambda x8: (leftmost(x8) if x4 else -leftmost(x8), uppermost(x8)),
        )
        x8 = tuple(rot270(subgrid(x9, I)) for x9 in x7)
    x9 = maximum(tuple(width(x10) for x10 in x8))
    x10 = tuple()
    for x11 in x8:
        x12 = width(x11)
        x13 = (x9 - x12) // TWO
        x14 = canvas(EIGHT, (height(x11), x9))
        x15 = shift(asobject(x11), (ZERO, x13))
        x16 = paint(x14, x15)
        x10 = x10 + x16
    return x10
