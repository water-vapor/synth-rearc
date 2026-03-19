from arc2.core import *


def rectangle_patch_e88171ec(
    ul: IntegerTuple,
    lr: IntegerTuple,
) -> Indices:
    x0 = frozenset({ul, lr})
    return backdrop(x0)


def rectangle_interior_e88171ec(
    ul: IntegerTuple,
    lr: IntegerTuple,
) -> Indices:
    x0, x1 = ul
    x2, x3 = lr
    if x2 - x0 < TWO or x3 - x1 < TWO:
        return frozenset()
    return frozenset(
        (x4, x5)
        for x4 in range(x0 + ONE, x2)
        for x5 in range(x1 + ONE, x3)
    )


def largest_zero_rectangle_info_e88171ec(
    grid: Grid,
) -> tuple[IntegerTuple, IntegerTuple, Integer, Integer]:
    x0, x1 = shape(grid)
    x2 = None
    x3 = None
    x4 = -ONE
    x5 = ZERO
    for x6 in range(x0):
        x7 = [True] * x1
        for x8 in range(x6, x0):
            x9 = grid[x8]
            for x10 in range(x1):
                x7[x10] = x7[x10] and x9[x10] == ZERO
            x11 = None
            for x12 in range(x1 + ONE):
                x13 = x12 < x1 and x7[x12]
                if x13 and x11 is None:
                    x11 = x12
                    continue
                if x13 or x11 is None:
                    continue
                x14 = (x8 - x6 + ONE) * (x12 - x11)
                x15 = astuple(x6, x11)
                x16 = astuple(x8, x12 - ONE)
                if x14 > x4:
                    x2 = x15
                    x3 = x16
                    x4 = x14
                    x5 = ONE
                elif x14 == x4:
                    x5 = x5 + ONE
                    if x2 is None or (x15, x16) < (x2, x3):
                        x2 = x15
                        x3 = x16
                x11 = None
    if x2 is None or x3 is None:
        raise ValueError("e88171ec requires at least one zero cell")
    return x2, x3, x4, x5


def largest_zero_rectangle_bounds_e88171ec(
    grid: Grid,
) -> tuple[IntegerTuple, IntegerTuple]:
    x0, x1, _, _ = largest_zero_rectangle_info_e88171ec(grid)
    return x0, x1
