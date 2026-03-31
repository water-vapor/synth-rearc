from synth_rearc.core import *

from .helpers import (
    diagonal_components_7b80bb43,
    stair_cells_7b80bb43,
    staircase_col_7b80bb43,
    staircase_row_7b80bb43,
)


def verify_7b80bb43(I: Grid) -> Grid:
    x0, x1, x2 = stair_cells_7b80bb43(I)
    x3 = diagonal_components_7b80bb43(x2)
    x4 = set()
    x5 = set()
    x6 = ofcolor(I, x1)
    x7 = height(I)
    x8 = width(I)
    x9 = set(x3)
    for x10 in range(x7):
        x11 = sorted(j for i, j in x6 if i == x10)
        x12 = []
        for x13 in x11:
            if len(x12) == ZERO or x13 > x12[-ONE][-ONE] + ONE:
                x12.append([x13, x13])
            else:
                x12[-ONE][-ONE] = x13
        for x13, x14 in zip(x12, x12[ONE:]):
            x15 = x14[ZERO] - x13[ONE] - ONE
            if x15 <= ONE:
                continue
            x16 = staircase_row_7b80bb43(x10, x13[ONE], x14[ZERO], "left")
            x17 = staircase_row_7b80bb43(x10, x13[ONE], x14[ZERO], "right")
            x18 = both(x16.issubset(x6), greater(x13[ONE] - x13[ZERO] + ONE, ONE))
            x19 = both(x17.issubset(x6), greater(x14[ONE] - x14[ZERO] + ONE, ONE))
            if x18 or x19:
                x20 = frozenset((x10, j) for j in range(x13[ONE] + ONE, x14[ZERO]))
                x4 |= set(x20)
                x5 |= set((x10, j) for j in range(x13[ZERO], x13[ONE] + ONE))
                x5 |= set((x10, j) for j in range(x14[ZERO], x14[ONE] + ONE))
    for x10 in range(x8):
        x11 = sorted(i for i, j in x6 if j == x10)
        x12 = []
        for x13 in x11:
            if len(x12) == ZERO or x13 > x12[-ONE][-ONE] + ONE:
                x12.append([x13, x13])
            else:
                x12[-ONE][-ONE] = x13
        for x13, x14 in zip(x12, x12[ONE:]):
            x15 = x14[ZERO] - x13[ONE] - ONE
            if x15 <= ONE:
                continue
            x16 = staircase_col_7b80bb43(x13[ONE], x14[ZERO], x10, "left", "top")
            x17 = staircase_col_7b80bb43(x13[ONE], x14[ZERO], x10, "right", "top")
            x18 = staircase_col_7b80bb43(x13[ONE], x14[ZERO], x10, "left", "bottom")
            x19 = staircase_col_7b80bb43(x13[ONE], x14[ZERO], x10, "right", "bottom")
            x20 = (
                both(x16.issubset(x6), greater(x13[ONE] - x13[ZERO] + ONE, ONE)),
                both(x17.issubset(x6), greater(x13[ONE] - x13[ZERO] + ONE, ONE)),
                both(x18.issubset(x6), greater(x14[ONE] - x14[ZERO] + ONE, ONE)),
                both(x19.issubset(x6), greater(x14[ONE] - x14[ZERO] + ONE, ONE)),
            )
            if any(x20):
                x21 = frozenset((i, x10) for i in range(x13[ONE] + ONE, x14[ZERO]))
                x4 |= set(x21)
                x5 |= set((i, x10) for i in range(x13[ZERO], x13[ONE] + ONE))
                x5 |= set((i, x10) for i in range(x14[ZERO], x14[ONE] + ONE))
    x19 = set()
    for x20 in x9:
        x21 = x20 - frozenset(x5)
        x19 |= set(x21)
    x22 = fill(I, x0, frozenset(x19))
    x23 = fill(x22, x1, frozenset(x4))
    return x23
