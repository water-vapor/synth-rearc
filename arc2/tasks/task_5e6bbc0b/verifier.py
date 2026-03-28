from arc2.core import *


def verify_5e6bbc0b(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = ulcorner(ofcolor(I, EIGHT))
    x3 = x2[0]
    x4 = x2[1]
    x5 = decrement(x0)
    x6 = decrement(x1)
    x7 = either(equality(x4, ZERO), equality(x4, x6))
    x8 = canvas(ZERO, shape(I))
    if x7:
        x9 = equality(x4, ZERO)
        for x10 in range(x0):
            x11 = sum(ONE for x12 in range(x1) if I[x10][x12] != ZERO)
            x13 = (
                frozenset((x10, x12) for x12 in range(x11))
                if x9
                else frozenset((x10, x12) for x12 in range(x1 - x11, x1))
            )
            x8 = fill(x8, ONE, x13)
            if equality(x10, x3):
                x14 = (
                    frozenset((x10, x12) for x12 in range(x11, x11 + x11 - ONE))
                    if x9
                    else frozenset((x10, x12) for x12 in range(x1 - x11 - x11 + ONE, x1 - x11))
                )
                x15 = (x10, ZERO) if x9 else (x10, x6)
                x8 = fill(x8, NINE, x14)
                x8 = fill(x8, EIGHT, frozenset({x15}))
        return x8
    x16 = equality(x3, ZERO)
    for x17 in range(x1):
        x18 = sum(ONE for x19 in range(x0) if I[x19][x17] != ZERO)
        x20 = (
            frozenset((x19, x17) for x19 in range(x18))
            if x16
            else frozenset((x19, x17) for x19 in range(x0 - x18, x0))
        )
        x8 = fill(x8, ONE, x20)
        if equality(x17, x4):
            x21 = (
                frozenset((x19, x17) for x19 in range(x18, x18 + x18 - ONE))
                if x16
                else frozenset((x19, x17) for x19 in range(x0 - x18 - x18 + ONE, x0 - x18))
            )
            x22 = (ZERO, x17) if x16 else (x5, x17)
            x8 = fill(x8, NINE, x21)
            x8 = fill(x8, EIGHT, frozenset({x22}))
    return x8
