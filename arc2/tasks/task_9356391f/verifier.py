from arc2.core import *


def verify_9356391f(
    I: Grid,
) -> Grid:
    x0 = height(I)
    x1 = I[ZERO]
    x2 = tuple(j for j, x3 in enumerate(x1) if x3 != ZERO)
    x3 = maximum(x2)
    x4 = x1[: increment(x3)]
    x5 = None
    for x6 in range(TWO, x0):
        for x7, x8 in enumerate(I[x6]):
            if x8 != ZERO:
                x5 = (x6, x7)
                break
        if x5 is not None:
            break
    x9 = x5[ONE]
    x10 = index(I, (ZERO, x9))
    x11 = frozenset(((ZERO, x9),))
    x12 = branch(equality(x10, ZERO), I, fill(I, FIVE, x11))
    x13 = x12
    for x14, x15 in enumerate(x4):
        if x15 == ZERO:
            continue
        x16 = interval(subtract(x5[ZERO], x14), increment(add(x5[ZERO], x14)), ONE)
        x17 = interval(subtract(x5[ONE], x14), increment(add(x5[ONE], x14)), ONE)
        x18 = product(x16, x17)
        x19 = box(x18)
        x13 = fill(x13, x15, x19)
    return x13
