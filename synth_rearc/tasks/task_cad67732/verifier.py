from synth_rearc.core import *


def _direction_cad67732(
    grid: Grid,
) -> Integer:
    rows = tuple(i for i, row in enumerate(grid) if any(value != ZERO for value in row))
    top = first(rows)
    bottom = last(rows)
    left_top = next(j for j, value in enumerate(grid[top]) if value != ZERO)
    left_bottom = next(j for j, value in enumerate(grid[bottom]) if value != ZERO)
    return branch(greater(left_bottom, left_top), ONE, NEG_ONE)


def _period_cad67732(
    grid: Grid,
) -> Integer:
    height_ = len(grid)
    width_ = len(grid[0])
    cells = tuple(
        (i, j, value)
        for i, row in enumerate(grid)
        for j, value in enumerate(row)
        if value != ZERO
    )
    for step in range(ONE, height_):
        seen = False
        valid = True
        for i, j, value in cells:
            a = i + step
            b = j + step
            if a < height_ and b < width_:
                seen = True
                if grid[a][b] != value:
                    valid = False
                    break
        if valid and seen:
            return step
    return height_


def _base_object_cad67732(
    grid: Grid,
    step: Integer,
) -> Object:
    cells = set()
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == ZERO:
                continue
            a = i - step
            b = j - step
            if a < ZERO or b < ZERO or grid[a][b] != value:
                cells.add((value, (i, j)))
    return frozenset(cells)


def _render_main_cad67732(
    base: Object,
    step: Integer,
    dims: IntegerTuple,
) -> Grid:
    grid = canvas(ZERO, dims)
    limit = max(dims) + max(height(base), width(base))
    offset = astuple(step, step)
    for k in range(limit):
        grid = paint(grid, shift(base, multiply(k, offset)))
    return grid


def verify_cad67732(I: Grid) -> Grid:
    x0 = _direction_cad67732(I)
    x1 = equality(x0, NEG_ONE)
    x2 = branch(x1, vmirror(I), I)
    x3 = _period_cad67732(x2)
    x4 = _base_object_cad67732(x2, x3)
    x5 = normalize(x4)
    x6 = shape(x2)
    x7 = double(x6)
    x8 = _render_main_cad67732(x5, x3, x7)
    x9 = branch(x1, vmirror(x8), x8)
    return x9
