from synth_rearc.core import *


DRAW_COLOR_DA515329 = EIGHT


def clockwise_direction_da515329(
    direction: IntegerTuple,
) -> IntegerTuple:
    x0, x1 = direction
    return (x1, -x0)


def infer_cross_center_k_da515329(
    grid: Grid,
) -> tuple[IntegerTuple, Integer]:
    x0 = ofcolor(grid, DRAW_COLOR_DA515329)
    x1 = tuple(sorted({x2[ZERO] for x2 in x0}))
    x2 = tuple(sorted({x3[ONE] for x3 in x0}))
    x3 = (x1[len(x1) // TWO], x2[len(x2) // TWO])
    x4 = sum(x5[ONE] == x3[ONE] and x5[ZERO] < x3[ZERO] for x5 in x0)
    return x3, x4


def input_cells_da515329(
    center: IntegerTuple,
    arm_length: Integer,
) -> frozenset[IntegerTuple]:
    x0, x1 = center
    x2 = set()
    for x3 in range(ONE, arm_length + ONE):
        x2.add((x0 - x3, x1))
        x2.add((x0 + x3, x1))
        x2.add((x0, x1 - x3))
        x2.add((x0, x1 + x3))
    return frozenset(x2)


def make_input_da515329(
    dimensions: IntegerTuple,
    center: IntegerTuple,
    arm_length: Integer,
) -> Grid:
    x0 = canvas(ZERO, dimensions)
    x1 = input_cells_da515329(center, arm_length)
    x2 = fill(x0, DRAW_COLOR_DA515329, x1)
    return x2


def arm_cells_da515329(
    start: IntegerTuple,
    initial_direction: IntegerTuple,
    arm_length: Integer,
    dimensions: IntegerTuple,
) -> frozenset[IntegerTuple]:
    x0, x1 = dimensions
    x2 = []
    x3 = start
    x2.append(x3)
    x4 = ONE if arm_length == ONE else arm_length - ONE
    for _ in range(x4):
        x3 = (x3[ZERO] + initial_direction[ZERO], x3[ONE] + initial_direction[ONE])
        x2.append(x3)
    x5 = clockwise_direction_da515329(initial_direction)
    x6 = max(dimensions) + arm_length + FOUR
    for x7 in range(ONE, x6 + ONE):
        x8 = FOUR * x7
        if arm_length == ONE:
            x9 = ((x5, x8),)
        else:
            x9 = [(x5, x8 - TWO)]
            if arm_length > TWO:
                x9.append((clockwise_direction_da515329(x5), arm_length - TWO))
            x9.append((x5, arm_length))
        for x10, x11 in x9:
            for _ in range(x11):
                x3 = (x3[ZERO] + x10[ZERO], x3[ONE] + x10[ONE])
                x2.append(x3)
        x5 = clockwise_direction_da515329(x5)
    x12 = frozenset(
        x13 for x13 in x2 if ZERO <= x13[ZERO] < x0 and ZERO <= x13[ONE] < x1
    )
    return x12


def render_output_da515329(
    dimensions: IntegerTuple,
    center: IntegerTuple,
    arm_length: Integer,
) -> Grid:
    x0 = canvas(ZERO, dimensions)
    x1, x2 = center
    x3 = (
        ((x1 - ONE, x2), UP),
        ((x1, x2 + ONE), RIGHT),
        ((x1 + ONE, x2), DOWN),
        ((x1, x2 - ONE), LEFT),
    )
    x4 = set()
    for x5, x6 in x3:
        x7 = arm_cells_da515329(x5, x6, arm_length, dimensions)
        x4.update(x7)
    x8 = fill(x0, DRAW_COLOR_DA515329, frozenset(x4))
    return x8
