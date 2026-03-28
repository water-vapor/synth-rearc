from synth_rearc.core import *


def verify_42f83767(I: Grid) -> Grid:
    x0 = ofcolor(I, FIVE)
    x1 = height(x0)
    x2 = leftmost(x0)
    x3 = I[ZERO][:x2]
    x4 = tuple(
        v
        for j, v in enumerate(x3)
        if v not in (ZERO, FIVE) and (j == ZERO or x3[decrement(j)] != v)
    )
    x5 = size(x4)
    x6 = increment(x1)
    x7 = tuple(crop(I, (ZERO, add(x2, multiply(k, x6))), (x1, x1)) for k in range(x5))
    x8 = tuple(ofcolor(x9, FIVE) for x9 in x7)
    x9 = dict(zip(x4, x8))
    x10 = tuple(i for i in range(x1, height(I)) if any(v != ZERO for v in I[i]))
    x11 = first(x10)
    x12 = size(x10)
    x13 = minimum(tuple(j for i in x10 for j, v in enumerate(I[i]) if v != ZERO))
    x14 = crop(I, (x11, x13), (x12, x12))
    x15 = canvas(ZERO, (multiply(x1, x12), multiply(x1, x12)))
    x16 = x15
    for i, x17 in enumerate(x14):
        for j, x18 in enumerate(x17):
            x19 = shift(x9[x18], (multiply(i, x1), multiply(j, x1)))
            x16 = fill(x16, x18, x19)
    return x16
