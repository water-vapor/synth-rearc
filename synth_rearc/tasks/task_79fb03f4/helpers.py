import json
from functools import lru_cache
from pathlib import Path
from random import choice, randint, random, sample, shuffle

from synth_rearc.core import *


REFERENCE_TASK_PATH_79FB03F4 = Path("data/official/arc1/evaluation/79fb03f4.json")
BLOCKER_COLORS_79FB03F4 = (FIVE, EIGHT)
HEIGHT_BOUNDS_79FB03F4 = (SEVEN, 20)
WIDTH_BOUNDS_79FB03F4 = (EIGHT, 26)
SEED_COUNT_CHOICES_79FB03F4 = (ONE, ONE, TWO, TWO, THREE)
MIN_SEED_GAP_79FB03F4 = THREE


def _tuple_grid_79fb03f4(
    grid,
) -> Grid:
    return tuple(tuple(row) for row in grid)


@lru_cache(maxsize=ONE)
def _reference_pairs_79fb03f4() -> tuple[tuple[Grid, Grid], ...]:
    x0 = json.loads(REFERENCE_TASK_PATH_79FB03F4.read_text())
    x1 = tuple(
        (
            _tuple_grid_79fb03f4(x2["input"]),
            _tuple_grid_79fb03f4(x2["output"]),
        )
        for x2 in x0["train"] + x0["test"]
    )
    return x1


def reference_output_79fb03f4(
    grid: Grid,
) -> Grid | None:
    for x0, x1 in _reference_pairs_79fb03f4():
        if grid == x0:
            return x1
    return None


def _free_79fb03f4(
    blockers: frozenset[tuple[int, int]],
    loc: tuple[int, int],
    dims: tuple[int, int],
) -> bool:
    x0, x1 = loc
    return 0 <= x0 < dims[ZERO] and 0 <= x1 < dims[ONE] and loc not in blockers


def _bypass_79fb03f4(
    blockers: frozenset[tuple[int, int]],
    dims: tuple[int, int],
    painted: set[tuple[int, int]],
    row: int,
    col: int,
    goal: int,
    trail: frozenset[tuple[int, int, int]],
) -> tuple[bool, bool, int]:
    x0 = (row, col, goal)
    if x0 in trail:
        return (False, False, col)
    if not _free_79fb03f4(blockers, (row, col), dims):
        return (False, False, col)
    painted.add((row, col))
    x1 = col
    x2 = trail | frozenset({x0})
    while x1 < goal:
        x3 = x1 + ONE
        if x3 >= dims[ONE]:
            return (True, x1 == goal, x1)
        if _free_79fb03f4(blockers, (row, x3), dims):
            x1 = x3
            painted.add((row, x1))
            continue
        x4 = []
        for x5 in (row - ONE, row + ONE):
            if not _free_79fb03f4(blockers, (x5, x1), dims):
                continue
            x6 = _bypass_79fb03f4(blockers, dims, painted, x5, x1, x1 + TWO, x2)
            if x6[ZERO]:
                x4.append((x5, x6))
        if len(x4) == ZERO:
            return (False, False, x1)
        if x1 + TWO < dims[ONE] and any(x6[ONE] for _, x6 in x4) and _free_79fb03f4(blockers, (row, x1 + TWO), dims):
            x1 += TWO
            painted.add((row, x1))
            continue
        x7 = max(x6[TWO] for _, x6 in x4)
        return (True, False, x7)
    return (True, x1 == goal, x1)


def _trace_79fb03f4(
    blockers: frozenset[tuple[int, int]],
    dims: tuple[int, int],
    painted: set[tuple[int, int]],
    row: int,
    col: int,
    goal: int,
    trail: frozenset[tuple[int, int, int]],
) -> bool:
    x0 = (row, col, goal)
    if x0 in trail:
        return False
    if not _free_79fb03f4(blockers, (row, col), dims):
        return False
    painted.add((row, col))
    x1 = col
    x2 = trail | frozenset({x0})
    while x1 < goal:
        x3 = x1 + ONE
        if x3 >= dims[ONE]:
            return True
        if _free_79fb03f4(blockers, (row, x3), dims):
            x1 = x3
            painted.add((row, x1))
            continue
        x4 = []
        for x5 in (row - ONE, row + ONE):
            if not _free_79fb03f4(blockers, (x5, x1), dims):
                continue
            x6 = _bypass_79fb03f4(blockers, dims, painted, x5, x1, x1 + TWO, x2)
            if x6[ZERO]:
                x4.append((x5, x6))
        if len(x4) == ZERO:
            return False
        for x5, x6 in x4:
            if not x6[ONE]:
                _trace_79fb03f4(blockers, dims, painted, x5, x1, goal, x2)
        if x1 + TWO >= dims[ONE]:
            return False
        if any(x6[ONE] for _, x6 in x4) and _free_79fb03f4(blockers, (row, x1 + TWO), dims):
            x1 += TWO
            painted.add((row, x1))
            continue
        return True
    return True


def route_output_79fb03f4(
    grid: Grid,
) -> Grid:
    x0 = shape(grid)
    x1 = tuple(sorted(ofcolor(grid, ONE)))
    x2 = frozenset((i, j) for i, row in enumerate(grid) for j, value in enumerate(row) if value not in (ZERO, ONE))
    x3 = set(x1)
    for x4, x5 in x1:
        _trace_79fb03f4(x2, x0, x3, x4, x5, decrement(x0[ONE]), frozenset())
    return fill(grid, ONE, frozenset(x3))


def _unambiguous_output_79fb03f4(
    input_grid: Grid,
    output_grid: Grid,
) -> bool:
    x0 = shape(output_grid)
    x1 = decrement(x0[ONE])
    x2 = tuple(sorted(ofcolor(input_grid, ONE)))
    x3 = frozenset(ofcolor(output_grid, ONE))
    x4 = {}
    x5 = set()
    for x6 in x3:
        if x6 in x5:
            continue
        x7 = {x6}
        x8 = [x6]
        x5.add(x6)
        while x8:
            x9, x10 = x8.pop()
            for x11 in ((x9 - ONE, x10), (x9 + ONE, x10), (x9, x10 - ONE), (x9, x10 + ONE)):
                if x11 not in x3 or x11 in x5:
                    continue
                x5.add(x11)
                x7.add(x11)
                x8.append(x11)
        x12 = frozenset(x7)
        for x13 in x12:
            x4[x13] = x12
    for x6 in x2:
        x7 = x4.get(x6)
        if x7 is None or not any(x8[ONE] == x1 for x8 in x7):
            return False
    for x6 in x3:
        x7, x8 = x6
        x9 = sum(
            ((x7 + x10, x8 + x11) in x3)
            for x10, x11 in ((ONE, ZERO), (-ONE, ZERO), (ZERO, ONE), (ZERO, -ONE))
        )
        if x9 == ONE and x6 not in x2 and x8 != x1:
            return False
    return True


def _seed_rows_79fb03f4(
    height_value: int,
) -> tuple[int, ...]:
    x0 = []
    x1 = choice(SEED_COUNT_CHOICES_79FB03F4)
    x2 = list(range(ONE, decrement(height_value)))
    shuffle(x2)
    for x3 in x2:
        if any(abs(x3 - x4) < MIN_SEED_GAP_79FB03F4 for x4 in x0):
            continue
        x0.append(x3)
        if len(x0) == x1:
            break
    if len(x0) == ZERO:
        x0.append(randint(ONE, decrement(height_value) - ONE))
    return tuple(sorted(x0))


def _scatter_noise_79fb03f4(
    grid: list[list[int]],
    blocker_color: int,
    budget: int,
) -> None:
    x0 = len(grid)
    x1 = len(grid[ZERO])
    x2 = [(i, j) for i in range(x0) for j in range(ONE, x1) if grid[i][j] == ZERO]
    shuffle(x2)
    x3 = ZERO
    for x4, x5 in x2:
        if x3 >= budget:
            break
        if random() > 0.25:
            continue
        grid[x4][x5] = blocker_color
        x3 += ONE


def _add_route_blockers_79fb03f4(
    grid: list[list[int]],
    seed_row: int,
    blocker_color: int,
) -> None:
    x0 = len(grid)
    x1 = len(grid[ZERO])
    x2 = list(range(TWO, x1 - ONE))
    shuffle(x2)
    x3 = sample(x2, k=min(len(x2), randint(ONE, max(ONE, x1 // FIVE))))
    x3 = sorted(x3)
    for x4 in x3:
        grid[seed_row][x4] = blocker_color
        if random() < 0.55:
            x5 = choice((-ONE, ONE))
            x6 = seed_row + x5
            x7 = x4 + choice((ZERO, ONE))
            if 0 <= x6 < x0 and x7 < x1:
                grid[x6][x7] = blocker_color
                if random() < 0.3:
                    x8 = x6 + x5
                    x9 = min(x1 - ONE, x7 + ONE)
                    if 0 <= x8 < x0:
                        grid[x8][x9] = blocker_color


def build_example_79fb03f4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, HEIGHT_BOUNDS_79FB03F4)
        x1 = unifint(diff_lb, diff_ub, WIDTH_BOUNDS_79FB03F4)
        x2 = choice(BLOCKER_COLORS_79FB03F4)
        x3 = [list(row) for row in canvas(ZERO, (x0, x1))]
        x4 = _seed_rows_79fb03f4(x0)
        for x5 in x4:
            x3[x5][ZERO] = ONE
            _add_route_blockers_79fb03f4(x3, x5, x2)
        _scatter_noise_79fb03f4(x3, x2, randint(x0, x0 + x1 // THREE))
        x6 = _tuple_grid_79fb03f4(x3)
        x7 = route_output_79fb03f4(x6)
        if x6 == x7:
            continue
        if colorcount(x7, ONE) <= len(x4) + x1:
            continue
        if not _unambiguous_output_79fb03f4(x6, x7):
            continue
        if any(reference_output_79fb03f4(x6) is not None for _ in (ZERO,)):
            continue
        return {"input": x6, "output": x7}
