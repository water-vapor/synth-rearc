from synth_rearc.core import *

from .helpers import trace_guides_36a08778


def _can_place_36a08778(
    row_spans: dict[Integer, list[tuple[Integer, Integer]]],
    row: Integer,
    left: Integer,
    right: Integer,
) -> Boolean:
    x0 = row_spans.get(row, [])
    for x1, x2 in x0:
        if not (right < x1 - TWO or left > x2 + TWO):
            return F
    return T


def _register_36a08778(
    row_spans: dict[Integer, list[tuple[Integer, Integer]]],
    row: Integer,
    left: Integer,
    right: Integer,
) -> None:
    row_spans.setdefault(row, []).append((left, right))


def _paint_run_36a08778(
    grid: Grid,
    row: Integer,
    left: Integer,
    right: Integer,
) -> Grid:
    return fill(grid, TWO, connect((row, left), (row, right)))


def _grow_branch_36a08778(
    grid: Grid,
    row_spans: dict[Integer, list[tuple[Integer, Integer]]],
    col: Integer,
    min_row: Integer,
    budget: list[Integer],
    depth: Integer,
    dims: tuple[Integer, Integer],
) -> Grid:
    h, w = dims
    if budget[ZERO] <= ZERO or min_row >= h or depth > SEVEN:
        return grid
    if depth > ZERO and choice((T, F, F)):
        return grid
    x0 = []
    if min_row < h:
        x0.extend(("solid", "solid", "solid"))
    if ONE < col < w - TWO and min_row + ONE < h:
        x0.extend(("gap", "gap"))
    x0.extend(("stop", "stop"))
    for _ in range(18):
        kind = choice(tuple(x0))
        if kind == "stop":
            return grid
        if kind == "solid":
            row_ub = h - ONE
            if min_row > row_ub:
                continue
            x1 = min(FIVE, row_ub - min_row)
            row = min_row + randint(ZERO, x1)
            x2 = min(SEVEN, col)
            x3 = min(SEVEN, w - col - ONE)
            left_extra = randint(ZERO, x2)
            right_extra = randint(ZERO, x3)
            left = col - left_extra
            right = col + right_extra
            if not _can_place_36a08778(row_spans, row, left, right):
                continue
            grid = _paint_run_36a08778(grid, row, left, right)
            _register_36a08778(row_spans, row, left, right)
            budget[ZERO] -= ONE
            if left > ZERO:
                grid = _grow_branch_36a08778(grid, row_spans, left - ONE, row + ONE, budget, depth + ONE, dims)
            if right + ONE < w:
                grid = _grow_branch_36a08778(grid, row_spans, right + ONE, row + ONE, budget, depth + ONE, dims)
            return grid
        row_ub = h - TWO
        if min_row + ONE > row_ub:
            continue
        x1 = min(FOUR, row_ub - min_row)
        row = min_row + randint(ONE, x1)
        x2 = min(SIX, col - ONE)
        x3 = min(SIX, w - col - TWO)
        if x2 < ONE or x3 < ONE:
            continue
        left = col - randint(ONE, x2)
        right = col + randint(ONE, x3)
        if left <= ZERO or right >= w - ONE:
            continue
        if not _can_place_36a08778(row_spans, row, left, right):
            continue
        grid = _paint_run_36a08778(grid, row, left, col - ONE)
        grid = _paint_run_36a08778(grid, row, col + ONE, right)
        _register_36a08778(row_spans, row, left, col - ONE)
        _register_36a08778(row_spans, row, col + ONE, right)
        budget[ZERO] -= ONE
        grid = _grow_branch_36a08778(grid, row_spans, left - ONE, row + TWO, budget, depth + ONE, dims)
        grid = _grow_branch_36a08778(grid, row_spans, right + ONE, row + TWO, budget, depth + ONE, dims)
        return grid
    return grid


def generate_36a08778(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (EIGHT, 30))
        x1 = unifint(diff_lb, diff_ub, (FIVE, 30))
        x2 = choice((ONE, ONE, TWO, TWO, TWO))
        if x2 == TWO and x1 < 12:
            x2 = ONE
        if x2 == ONE:
            x3 = (unifint(diff_lb, diff_ub, (ONE, x1 - TWO)),)
        else:
            x4 = unifint(diff_lb, diff_ub, (THREE, x1 - EIGHT))
            x5 = unifint(diff_lb, diff_ub, (x4 + SIX, x1 - TWO))
            x3 = (x4, x5)
        x6 = canvas(SEVEN, (x0, x1))
        for x7 in x3:
            x8 = connect((ZERO, x7), (ONE, x7))
            x6 = fill(x6, SIX, x8)
        x9: dict[Integer, list[tuple[Integer, Integer]]] = {}
        x10 = [unifint(diff_lb, diff_ub, (TWO, min(11, x0 + len(x3))))]
        for x11 in x3:
            x6 = _grow_branch_36a08778(x6, x9, x11, TWO, x10, ZERO, (x0, x1))
        if x10[ZERO] > ONE:
            continue
        x12 = colorcount(x6, TWO)
        if x12 < THREE:
            continue
        x13 = trace_guides_36a08778(x6)
        if x13 == x6:
            continue
        x14 = colorcount(x13, SIX) - colorcount(x6, SIX)
        if x14 < THREE:
            continue
        return {"input": x6, "output": x13}
