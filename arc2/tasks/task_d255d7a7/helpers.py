from arc2.core import *


def _window_object_d255d7a7(
    grid: Grid,
    top: int,
    left: int,
) -> Object:
    x0 = []
    for x1 in range(top, top + THREE):
        for x2 in range(left, left + THREE):
            x3 = grid[x1][x2]
            if x3 != SEVEN:
                x0.append((x3, (x1, x2)))
    return frozenset(x0)


def build_horizontal_cap_d255d7a7(
    top: int,
    left: int,
    attach_side: str,
    far_value: int,
    inner_value: int,
) -> Object:
    x0 = {
        (ZERO, (top, left)),
        (ZERO, (top, left + ONE)),
        (ZERO, (top, left + TWO)),
        (ZERO, (top + TWO, left)),
        (ZERO, (top + TWO, left + ONE)),
        (ZERO, (top + TWO, left + TWO)),
    }
    if attach_side == "right":
        x1 = (top + ONE, left + TWO)
        x2 = (top + ONE, left + ONE)
        x3 = (top + ONE, left)
    else:
        x1 = (top + ONE, left)
        x2 = (top + ONE, left + ONE)
        x3 = (top + ONE, left + TWO)
    x0.add((ZERO, x1))
    if inner_value != SEVEN:
        x0.add((inner_value, x2))
    if far_value != SEVEN:
        x0.add((far_value, x3))
    return frozenset(x0)


def build_vertical_cap_d255d7a7(
    top: int,
    left: int,
    attach_side: str,
    far_value: int,
    inner_value: int,
) -> Object:
    x0 = {
        (ZERO, (top, left)),
        (ZERO, (top + ONE, left)),
        (ZERO, (top + TWO, left)),
        (ZERO, (top, left + TWO)),
        (ZERO, (top + ONE, left + TWO)),
        (ZERO, (top + TWO, left + TWO)),
    }
    if attach_side == "top":
        x1 = (top, left + ONE)
        x2 = (top + ONE, left + ONE)
        x3 = (top + TWO, left + ONE)
    else:
        x1 = (top + TWO, left + ONE)
        x2 = (top + ONE, left + ONE)
        x3 = (top, left + ONE)
    x0.add((ZERO, x1))
    if inner_value != SEVEN:
        x0.add((inner_value, x2))
    if far_value != SEVEN:
        x0.add((far_value, x3))
    return frozenset(x0)


def find_movable_caps_d255d7a7(
    grid: Grid,
) -> tuple[tuple[Object, IntegerTuple], ...]:
    x0 = height(grid)
    x1 = width(grid)
    x2 = []
    for x3 in range(x0 - TWO):
        for x4 in range(x1 - TWO):
            x5 = all(grid[x3 + x6][x4 + x7] == ZERO for x6 in (ZERO, TWO) for x7 in range(THREE))
            if x5 and grid[x3 + ONE][x4 + TWO] == ZERO:
                x8 = add(x4, THREE)
                x9 = x4 > ZERO and grid[x3 + ONE][x4 - ONE] == ZERO
                if x8 < x1 and grid[x3 + ONE][x8] == ZERO and not x9:
                    x10 = x4 + TWO
                    while x10 + ONE < x1 and grid[x3 + ONE][x10 + ONE] == ZERO:
                        x10 += ONE
                    x11 = _window_object_d255d7a7(grid, x3, x4)
                    x12 = astuple(ZERO, x10 - (x4 + TWO))
                    x2.append((x11, x12))
            x13 = x4 > ZERO and grid[x3 + ONE][x4 - ONE] == ZERO
            x14 = x4 + THREE < x1 and grid[x3 + ONE][x4 + THREE] == ZERO
            if x5 and grid[x3 + ONE][x4] == ZERO and x13 and not x14:
                x15 = x4
                while x15 - ONE >= ZERO and grid[x3 + ONE][x15 - ONE] == ZERO:
                    x15 -= ONE
                x16 = _window_object_d255d7a7(grid, x3, x4)
                x17 = astuple(ZERO, x15 - x4)
                x2.append((x16, x17))
            x18 = all(grid[x3 + x6][x4 + x7] == ZERO for x6 in range(THREE) for x7 in (ZERO, TWO))
            if x18 and grid[x3 + TWO][x4 + ONE] == ZERO:
                x19 = add(x3, THREE)
                x20 = x3 > ZERO and grid[x3 - ONE][x4 + ONE] == ZERO
                if x19 < x0 and grid[x19][x4 + ONE] == ZERO and not x20:
                    x21 = x3 + TWO
                    while x21 + ONE < x0 and grid[x21 + ONE][x4 + ONE] == ZERO:
                        x21 += ONE
                    x22 = _window_object_d255d7a7(grid, x3, x4)
                    x23 = astuple(x21 - (x3 + TWO), ZERO)
                    x2.append((x22, x23))
            x24 = x3 > ZERO and grid[x3 - ONE][x4 + ONE] == ZERO
            x25 = x3 + THREE < x0 and grid[x3 + THREE][x4 + ONE] == ZERO
            if x18 and grid[x3][x4 + ONE] == ZERO and x24 and not x25:
                x26 = x3
                while x26 - ONE >= ZERO and grid[x26 - ONE][x4 + ONE] == ZERO:
                    x26 -= ONE
                x27 = _window_object_d255d7a7(grid, x3, x4)
                x28 = astuple(x26 - x3, ZERO)
                x2.append((x27, x28))
    x29 = []
    x30 = set()
    for x31 in x2:
        x32, x33 = x31
        x34 = (frozenset(x35 for _, x35 in x32), x33)
        if x34 in x30:
            continue
        x30.add(x34)
        x29.append(x31)
    return tuple(x29)
