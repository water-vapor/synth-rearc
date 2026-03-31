from __future__ import annotations

from collections import Counter, deque

from synth_rearc.core import *


Rectangle13E47133 = tuple[Integer, Integer, Integer, Integer]
Corner13E47133 = tuple[IntegerTuple, str]

CORNER_RULES_13E47133 = (
    ("ul", (-ONE, ZERO), (ZERO, -ONE), (ONE, ONE)),
    ("ur", (-ONE, ZERO), (ZERO, ONE), (ONE, -ONE)),
    ("ll", (ONE, ZERO), (ZERO, -ONE), (-ONE, ONE)),
    ("lr", (ONE, ZERO), (ZERO, ONE), (-ONE, -ONE)),
)


def wall_color_13e47133(
    grid: Grid,
) -> Integer:
    values = tuple(value for row in grid for value in row)
    x0 = mostcommon(values)
    x1 = Counter(values)
    x2 = max((value for value in x1 if value != x0), key=lambda value: x1[value])
    return x2


def component_cells_13e47133(
    grid: Grid,
    wall: Integer | None = None,
) -> tuple[Indices, ...]:
    x0 = wall_color_13e47133(grid) if wall is None else wall
    x1 = len(grid)
    x2 = len(grid[ZERO])
    x3 = set()
    x4 = []
    for x5 in range(x1):
        for x6 in range(x2):
            x7 = (x5, x6)
            if grid[x5][x6] == x0 or x7 in x3:
                continue
            x8 = deque([x7])
            x3.add(x7)
            x9 = set()
            while len(x8) > ZERO:
                x10 = x8.popleft()
                x9.add(x10)
                for x11 in dneighbors(x10):
                    x12, x13 = x11
                    if not (ZERO <= x12 < x1 and ZERO <= x13 < x2):
                        continue
                    if grid[x12][x13] == x0 or x11 in x3:
                        continue
                    x3.add(x11)
                    x8.append(x11)
            x4.append(frozenset(x9))
    return tuple(x4)


def component_background_13e47133(
    grid: Grid,
    component: Indices,
) -> Integer:
    x0 = tuple(grid[i][j] for i, j in component)
    x1 = mostcommon(x0)
    return x1


def convex_corners_13e47133(
    grid: Grid,
    component: Indices,
) -> tuple[Corner13E47133, ...]:
    x0 = len(grid)
    x1 = len(grid[ZERO])
    x2 = set(component)
    x3 = []
    for x4 in component:
        i, j = x4
        for x5, x6, x7, _ in CORNER_RULES_13E47133:
            x8 = add(x4, x6)
            x9 = add(x4, x7)
            x10, x11 = x8
            x12, x13 = x9
            if ZERO <= x10 < x0 and ZERO <= x11 < x1 and x8 in x2:
                continue
            if ZERO <= x12 < x0 and ZERO <= x13 < x1 and x9 in x2:
                continue
            x3.append((x4, x5))
    x4 = tuple(sorted(set(x3)))
    return x4


def corner_diagonal_13e47133(
    component: Indices,
    corner: IntegerTuple,
    orientation: str,
) -> tuple[IntegerTuple, ...]:
    x0 = {name: step for name, _, _, step in CORNER_RULES_13E47133}
    x1 = x0[orientation]
    x2 = []
    x3 = corner
    x4 = set(component)
    while x3 in x4:
        x2.append(x3)
        x3 = add(x3, x1)
    return tuple(x2)


def cycle_from_corner_13e47133(
    grid: Grid,
    component: Indices,
    corner: IntegerTuple,
    orientation: str,
) -> tuple[Integer, ...]:
    x0 = component_background_13e47133(grid, component)
    x1 = corner_diagonal_13e47133(component, corner, orientation)
    x2 = [grid[x1[ZERO][ZERO]][x1[ZERO][ONE]]]
    x3 = x2[ZERO] != x0
    for x4 in x1[ONE:]:
        x5 = grid[x4[ZERO]][x4[ONE]]
        if not x3:
            if x5 == x0:
                break
            x2.append(x5)
            x3 = T
            continue
        if x5 == x0:
            break
        x2.append(x5)
    return tuple(x2)


def component_cycle_13e47133(
    grid: Grid,
    component: Indices,
) -> tuple[Integer, ...]:
    x0 = component_background_13e47133(grid, component)
    x1 = None
    for x2, x3 in convex_corners_13e47133(grid, component):
        x4 = cycle_from_corner_13e47133(grid, component, x2, x3)
        x5 = (
            len(x4),
            sum(value != x0 for value in x4),
            x4[ZERO] != x0,
            -x2[ZERO],
            -x2[ONE],
        )
        if x1 is None or x5 > x1[ZERO]:
            x1 = (x5, x4)
    if x1 is None:
        return (x0,)
    return x1[ONE]


def _interval_runs_13e47133(
    mask: Integer,
    width: Integer,
) -> tuple[tuple[Integer, Integer], ...]:
    out = []
    j = ZERO
    while j < width:
        if ((mask >> j) & ONE) == ZERO:
            j += ONE
            continue
        start = j
        while j + ONE < width and ((mask >> (j + ONE)) & ONE) == ONE:
            j += ONE
        out.append((start, j))
        j += ONE
    return tuple(out)


def maximal_rectangles_13e47133(
    component: Indices,
) -> tuple[Rectangle13E47133, ...]:
    x0 = tuple(sorted(i for i, _ in component))
    x1 = tuple(sorted(j for _, j in component))
    x2 = minimum(x0)
    x3 = maximum(x0)
    x4 = minimum(x1)
    x5 = maximum(x1)
    x6 = x3 - x2 + ONE
    x7 = x5 - x4 + ONE
    x8 = [ZERO for _ in range(x6)]
    for x9, x10 in component:
        x8[x9 - x2] |= ONE << (x10 - x4)
    x9 = []
    for x10 in range(x6):
        x11 = x8[x10]
        for x12 in range(x10, x6):
            x11 &= x8[x12]
            if x11 == ZERO:
                break
            for x13, x14 in _interval_runs_13e47133(x11, x7):
                x15 = ((ONE << (x14 - x13 + ONE)) - ONE) << x13
                x16 = x10 > ZERO and (x8[x10 - ONE] & x15) == x15
                x17 = x12 + ONE < x6 and (x8[x12 + ONE] & x15) == x15
                x18 = x13 > ZERO and all((x8[x19] >> (x13 - ONE)) & ONE for x19 in range(x10, x12 + ONE))
                x20 = x14 + ONE < x7 and all((x8[x19] >> (x14 + ONE)) & ONE for x19 in range(x10, x12 + ONE))
                if x16 or x17 or x18 or x20:
                    continue
                x21 = (x2 + x10, x2 + x12, x4 + x13, x4 + x14)
                x9.append(x21)
    x10 = tuple(sorted(set(x9)))
    return x10


def rectangle_depths_13e47133(
    component: Indices,
) -> dict[IntegerTuple, Integer]:
    x0 = {cell: ZERO for cell in component}
    for x1, x2, x3, x4 in maximal_rectangles_13e47133(component):
        for x5 in range(x1, x2 + ONE):
            for x6 in range(x3, x4 + ONE):
                x7 = min(x5 - x1, x2 - x5, x6 - x3, x4 - x6)
                x8 = (x5, x6)
                if x7 > x0[x8]:
                    x0[x8] = x7
    return x0


def render_output_13e47133(
    grid: Grid,
) -> Grid:
    x0 = wall_color_13e47133(grid)
    x1 = [list(row) for row in grid]
    for x2 in component_cells_13e47133(grid, x0):
        x3 = component_cycle_13e47133(grid, x2)
        x4 = rectangle_depths_13e47133(x2)
        for x5, x6 in x4.items():
            i, j = x5
            x1[i][j] = x3[x6 % len(x3)]
    return tuple(tuple(row) for row in x1)
