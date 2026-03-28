from synth_rearc.core import *


def verify_94be5b80(I: Grid) -> Grid:
    x0 = tuple(tuple(x1) for x1 in I)
    x1 = tuple(
        x2
        for x2 in range(subtract(height(I), TWO))
        if both(equality(x0[x2], x0[add(x2, ONE)]), equality(x0[x2], x0[add(x2, TWO)]))
    )
    x2 = max(x1, key=lambda x3: sum(x4 != ZERO for x4 in x0[x3]))
    x3 = tuple(x4 for x4 in x0[x2] if x4 != ZERO)
    x4 = frozenset((x5, x6) for x5 in range(x2, add(x2, THREE)) for x6 in range(width(I)))
    x5 = fill(I, ZERO, x4)
    x6 = fgpartition(x5)
    x7 = argmax(x6, size)
    x8 = normalize(toindices(x7))
    x9 = argmin(x6, uppermost)
    x10 = color(x9)
    x11 = x3.index(x10)
    x12 = height(x8)
    x13 = uppermost(x9)
    x14 = subtract(x13, multiply(x11, x12))
    x15 = leftmost(x9)
    x16 = canvas(ZERO, shape(I))
    for x17, x18 in enumerate(x3):
        x19 = shift(x8, (add(x14, multiply(x17, x12)), x15))
        x20 = recolor(x18, x19)
        x16 = paint(x16, x20)
    return x16
