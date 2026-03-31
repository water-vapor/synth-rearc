from collections import deque

from synth_rearc.core import *


def _color_cells_89565ca0(
    grid: Grid,
    color: int,
) -> frozenset[tuple[int, int]]:
    return ofcolor(grid, color)


def _bbox_89565ca0(
    cells: frozenset[tuple[int, int]],
) -> tuple[int, int, int, int]:
    x0 = ulcorner(cells)
    x1 = lrcorner(cells)
    return (x0[0], x0[1], x1[0], x1[1])


def _max_component_89565ca0(
    grid: Grid,
    color: int,
) -> int:
    x0 = _color_cells_89565ca0(grid, color)
    x1 = set()
    x2 = ZERO
    for x3 in x0:
        if x3 in x1:
            continue
        x4 = deque((x3,))
        x1.add(x3)
        x5 = ZERO
        while len(x4) > ZERO:
            x6 = x4.popleft()
            x5 += ONE
            x7 = tuple(
                x8 for x8 in dneighbors(x6)
                if both(x8 in x0, x8 not in x1)
            )
            for x8 in x7:
                x1.add(x8)
                x4.append(x8)
        x2 = max(x2, x5)
    return x2


def _noise_color_89565ca0(grid: Grid) -> int:
    x0 = tuple(sorted({x1 for x2 in grid for x1 in x2 if x1 != ZERO}))
    x1 = tuple((_max_component_89565ca0(grid, x2), x2) for x2 in x0)
    x2 = min(x1)
    return x2[1]


def _repair_color_89565ca0(
    grid: Grid,
    color: int,
) -> frozenset[tuple[int, int]]:
    x0 = set(_color_cells_89565ca0(grid, color))
    x1, x2, x3, x4 = _bbox_89565ca0(frozenset(x0))
    x5 = min(SIX, min(x3 - x1 + ONE, x4 - x2 + ONE) - ONE)
    x6 = T
    while x6:
        x6 = F
        for x7 in range(x1, x3 + ONE):
            x8 = sum((x7, x9) in x0 for x9 in range(x2, x4 + ONE))
            if x8 < x5:
                continue
            x9 = sorted(x10 for x11, x10 in x0 if x11 == x7)
            for x10, x11 in zip(x9, x9[1:]):
                if x11 - x10 <= ONE:
                    continue
                x12 = all(grid[x7][x13] != ZERO for x13 in range(x10, x11 + ONE))
                if not x12:
                    continue
                for x13 in range(x10, x11 + ONE):
                    x14 = (x7, x13)
                    if x14 not in x0:
                        x0.add(x14)
                        x6 = T
        for x7 in range(x2, x4 + ONE):
            x8 = sum((x9, x7) in x0 for x9 in range(x1, x3 + ONE))
            if x8 < x5:
                continue
            x9 = sorted(x10 for x10, x11 in x0 if x11 == x7)
            for x10, x11 in zip(x9, x9[1:]):
                if x11 - x10 <= ONE:
                    continue
                x12 = all(grid[x13][x7] != ZERO for x13 in range(x10, x11 + ONE))
                if not x12:
                    continue
                for x13 in range(x10, x11 + ONE):
                    x14 = (x13, x7)
                    if x14 not in x0:
                        x0.add(x14)
                        x6 = T
    return frozenset(x0)


def _room_count_89565ca0(
    cells: frozenset[tuple[int, int]],
) -> int:
    x0, x1, x2, x3 = _bbox_89565ca0(cells)
    x4 = x2 - x0 + ONE
    x5 = x3 - x1 + ONE
    x6 = frozenset((x7 - x0, x8 - x1) for x7, x8 in cells)
    x7 = set()
    x8 = ZERO
    for x9 in range(x4):
        for x10 in range(x5):
            x11 = (x9, x10)
            if either(x11 in x6, x11 in x7):
                continue
            x12 = deque((x11,))
            x7.add(x11)
            x13 = F
            while len(x12) > ZERO:
                x14 = x12.popleft()
                if either(
                    either(x14[0] == ZERO, x14[1] == ZERO),
                    either(x14[0] == x4 - ONE, x14[1] == x5 - ONE),
                ):
                    x13 = T
                x15 = tuple(
                    x16 for x16 in dneighbors(x14)
                    if both(
                        both(0 <= x16[0] < x4, 0 <= x16[1] < x5),
                        both(x16 not in x6, x16 not in x7),
                    )
                )
                for x16 in x15:
                    x7.add(x16)
                    x12.append(x16)
            if not x13:
                x8 += ONE
    return x8


def verify_89565ca0(I: Grid) -> Grid:
    x0 = tuple(sorted({x1 for x2 in I for x1 in x2 if x1 != ZERO}))
    x1 = _noise_color_89565ca0(I)
    x2 = tuple(x3 for x3 in x0 if x3 != x1)
    x3 = tuple((_room_count_89565ca0(_repair_color_89565ca0(I, x4)), x4) for x4 in x2)
    x4 = max(x5 for x5, x6 in x3)
    x5 = tuple(sorted(x3))
    x6 = tuple(
        tuple([x7] * x8 + [x1] * (x4 - x8))
        for x8, x7 in x5
    )
    return x6
