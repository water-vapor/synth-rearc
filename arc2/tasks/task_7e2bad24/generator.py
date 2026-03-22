from arc2.core import *

from .helpers import GRID_SHAPE_7E2BAD24, barrier_orientations_7e2bad24, trace_extension_7e2bad24
from .verifier import verify_7e2bad24


def _line_cells_7e2bad24(spec: tuple[int, str, int, int, int]) -> Indices:
    color, orient, fixed, start, length = spec
    if orient == "v":
        return frozenset((i, fixed) for i in range(start, start + length))
    return frozenset((fixed, j) for j in range(start, start + length))


def _place_line_7e2bad24(grid: Grid, spec: tuple[int, str, int, int, int]) -> Grid:
    x0 = spec[0]
    x1 = _line_cells_7e2bad24(spec)
    x2 = fill(grid, x0, x1)
    return x2


def _start_bounds_7e2bad24(total: int, length: int) -> tuple[int, int]:
    x0 = total - length
    if x0 > TWO:
        return (ONE, x0 - ONE)
    return (ZERO, x0)


def _same_color_touch_7e2bad24(
    spec: tuple[int, str, int, int, int],
    occupied: dict[tuple[int, int], int],
) -> bool:
    x0 = spec[0]
    x1 = _line_cells_7e2bad24(spec)
    for x2 in x1:
        if contained(x2, occupied):
            return T
        for x3 in dneighbors(x2):
            if x3 in x1:
                continue
            if x3 in occupied and occupied[x3] == x0:
                return T
    return F


def _random_line_spec_7e2bad24(
    diff_lb: float,
    diff_ub: float,
) -> tuple[int, str, int, int, int]:
    x0, x1 = GRID_SHAPE_7E2BAD24
    x2 = choice((TWO, TWO, THREE))
    x3 = choice(("v", "h"))
    x4 = unifint(diff_lb, diff_ub, (4, 14))
    if x3 == "v":
        x5 = randint(ZERO, x1 - ONE)
        x6, x7 = _start_bounds_7e2bad24(x0, x4)
        x8 = randint(x6, x7)
        return (x2, x3, x5, x8, x4)
    x5 = randint(ZERO, x0 - ONE)
    x6, x7 = _start_bounds_7e2bad24(x1, x4)
    x8 = randint(x6, x7)
    return (x2, x3, x5, x8, x4)


def _random_border_seed_7e2bad24() -> tuple[tuple[int, int], tuple[int, int]]:
    x0, x1 = GRID_SHAPE_7E2BAD24
    x2 = choice(("top", "bottom", "left", "right"))
    if x2 == "top":
        x3 = randint(ZERO, x1 - ONE)
        x4 = choice((-ONE, ONE))
        if not (ZERO <= x3 + x4 < x1):
            x4 = invert(x4)
        return (ZERO, x3), (ONE, x4)
    if x2 == "bottom":
        x3 = randint(ZERO, x1 - ONE)
        x4 = choice((-ONE, ONE))
        if not (ZERO <= x3 + x4 < x1):
            x4 = invert(x4)
        return (x0 - ONE, x3), (-ONE, x4)
    if x2 == "left":
        x3 = randint(ZERO, x0 - ONE)
        x4 = choice((-ONE, ONE))
        if not (ZERO <= x3 + x4 < x0):
            x4 = invert(x4)
        return (x3, ZERO), (x4, ONE)
    x3 = randint(ZERO, x0 - ONE)
    x4 = choice((-ONE, ONE))
    if not (ZERO <= x3 + x4 < x0):
        x4 = invert(x4)
    return (x3, x1 - ONE), (x4, -ONE)


def _simulate_path_7e2bad24(
    grid: Grid,
    start: tuple[int, int],
    direction: tuple[int, int],
) -> tuple[tuple[tuple[int, int], ...], int, bool]:
    x0 = barrier_orientations_7e2bad24(grid, TWO)
    x1, x2, x3 = trace_extension_7e2bad24(grid, start, direction, x0)
    if flip(x3):
        return tuple(), x2, F
    x4 = combine((start,), x1)
    return x4, x2, T


def _prefix_budget_7e2bad24(
    grid: Grid,
    path: tuple[tuple[int, int], ...],
) -> int:
    x0 = ZERO
    for x1 in path:
        if index(grid, x1) != ZERO:
            break
        x0 = increment(x0)
    return x0


def _paint_path_7e2bad24(
    grid: Grid,
    path: tuple[tuple[int, int], ...],
) -> Grid:
    x0 = recolor(ONE, frozenset(path))
    x1 = paint(grid, x0)
    return x1


def generate_7e2bad24(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0, x1 = GRID_SHAPE_7E2BAD24
    while True:
        x2 = canvas(ZERO, GRID_SHAPE_7E2BAD24)
        x3 = {}
        x4 = unifint(diff_lb, diff_ub, (ONE, FIVE))
        x5 = []
        for _ in range(x4):
            x6 = None
            for _ in range(100):
                x7 = _random_line_spec_7e2bad24(diff_lb, diff_ub)
                if _same_color_touch_7e2bad24(x7, x3):
                    continue
                x6 = x7
                break
            if x6 is None:
                continue
            x5.append(x6)
            for x7 in _line_cells_7e2bad24(x6):
                x3[x7] = x6[0]
            x2 = _place_line_7e2bad24(x2, x6)
        x6, x7 = _random_border_seed_7e2bad24()
        if index(x2, x6) != ZERO:
            continue
        x8, x9, x10 = _simulate_path_7e2bad24(x2, x6, x7)
        if flip(x10):
            continue
        if len(x8) < 7:
            continue
        if x9 == ZERO:
            continue
        x11 = _prefix_budget_7e2bad24(x2, x8)
        x12 = min(FIVE, x11, len(x8) - ONE)
        if x12 < THREE:
            continue
        x13 = randint(THREE, x12)
        x14 = x8[:x13]
        x15 = _paint_path_7e2bad24(x2, x14)
        x16 = _paint_path_7e2bad24(x2, x8)
        if x15 == x16:
            continue
        if verify_7e2bad24(x15) != x16:
            continue
        if width(x15) != x1:
            continue
        if height(x15) != x0:
            continue
        return {"input": x15, "output": x16}
