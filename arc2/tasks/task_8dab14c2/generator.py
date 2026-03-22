from arc2.core import *


BG_8DAB14C2 = EIGHT
FG_8DAB14C2 = ONE


def _paint_rect_8dab14c2(
    grid: Grid,
    value: Integer,
    r0: Integer,
    r1: Integer,
    c0: Integer,
    c1: Integer,
) -> Grid:
    x0 = interval(r0, add(r1, ONE), ONE)
    x1 = interval(c0, add(c1, ONE), ONE)
    return fill(grid, value, product(x0, x1))


def _paint_cell_8dab14c2(
    grid: Grid,
    value: Integer,
    loc: IntegerTuple,
) -> Grid:
    return fill(grid, value, frozenset({loc}))


def _project_defects_8dab14c2(
    grid: Grid,
    h_rect: tuple[Integer, Integer, Integer, Integer],
    v_rect: tuple[Integer, Integer, Integer, Integer],
) -> Grid:
    x0, x1, x2, x3 = h_rect
    x4, x5, x6, x7 = v_rect
    x8 = width(grid)
    x9 = height(grid)
    x10 = tuple(j for j in range(x2, add(x3, ONE)) if not x6 <= j <= x7)
    x11 = tuple(i for i in range(x4, add(x5, ONE)) if not x0 <= i <= x1)
    x12 = grid
    for x13 in range(x0, add(x1, ONE)):
        if x2 > ZERO and grid[x13][decrement(x2)] == FG_8DAB14C2:
            x12 = _paint_cell_8dab14c2(x12, BG_8DAB14C2, (x13, x3))
        if grid[x13][x2] == BG_8DAB14C2:
            x12 = _paint_cell_8dab14c2(x12, FG_8DAB14C2, (x13, increment(x3)))
        if increment(x3) < x8 and grid[x13][increment(x3)] == FG_8DAB14C2:
            x12 = _paint_cell_8dab14c2(x12, BG_8DAB14C2, (x13, x2))
        if grid[x13][x3] == BG_8DAB14C2:
            x12 = _paint_cell_8dab14c2(x12, FG_8DAB14C2, (x13, decrement(x2)))
    for x13 in x10:
        if x0 > ZERO and grid[decrement(x0)][x13] == FG_8DAB14C2:
            x12 = _paint_cell_8dab14c2(x12, BG_8DAB14C2, (x1, x13))
        if grid[x0][x13] == BG_8DAB14C2:
            x12 = _paint_cell_8dab14c2(x12, FG_8DAB14C2, (increment(x1), x13))
        if increment(x1) < x9 and grid[increment(x1)][x13] == FG_8DAB14C2:
            x12 = _paint_cell_8dab14c2(x12, BG_8DAB14C2, (x0, x13))
        if grid[x1][x13] == BG_8DAB14C2:
            x12 = _paint_cell_8dab14c2(x12, FG_8DAB14C2, (decrement(x0), x13))
    for x13 in range(x6, add(x7, ONE)):
        if x4 > ZERO and grid[decrement(x4)][x13] == FG_8DAB14C2:
            x12 = _paint_cell_8dab14c2(x12, BG_8DAB14C2, (x5, x13))
        if grid[x4][x13] == BG_8DAB14C2:
            x12 = _paint_cell_8dab14c2(x12, FG_8DAB14C2, (increment(x5), x13))
        if increment(x5) < x9 and grid[increment(x5)][x13] == FG_8DAB14C2:
            x12 = _paint_cell_8dab14c2(x12, BG_8DAB14C2, (x4, x13))
        if grid[x5][x13] == BG_8DAB14C2:
            x12 = _paint_cell_8dab14c2(x12, FG_8DAB14C2, (decrement(x4), x13))
    for x13 in x11:
        if x6 > ZERO and grid[x13][decrement(x6)] == FG_8DAB14C2:
            x12 = _paint_cell_8dab14c2(x12, BG_8DAB14C2, (x13, x7))
        if grid[x13][x6] == BG_8DAB14C2:
            x12 = _paint_cell_8dab14c2(x12, FG_8DAB14C2, (x13, increment(x7)))
        if increment(x7) < x8 and grid[x13][increment(x7)] == FG_8DAB14C2:
            x12 = _paint_cell_8dab14c2(x12, BG_8DAB14C2, (x13, x6))
        if grid[x13][x7] == BG_8DAB14C2:
            x12 = _paint_cell_8dab14c2(x12, FG_8DAB14C2, (x13, decrement(x6)))
    return x12


def generate_8dab14c2(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    from .verifier import verify_8dab14c2

    while True:
        x0 = choice((T, F))
        x1 = choice((T, F))
        x2 = choice((THREE, FOUR, FIVE))
        x3 = choice((THREE, FOUR))
        x4 = unifint(diff_lb, diff_ub, (add(x2, FOUR), 13))
        x5 = unifint(diff_lb, diff_ub, (add(x3, FOUR), 13))
        x6 = choice((ONE, ONE, TWO))
        x7 = choice((ONE, ONE, TWO))
        x8 = choice((ONE, ONE, TWO))
        x9 = choice((ONE, ONE, TWO))
        x10 = add(add(x4, x6), x7)
        x11 = add(add(x5, x8), x9)
        if either(greater(x10, 17), greater(x11, 17)):
            continue
        if x0:
            x12 = x6
            x13 = subtract(add(x6, x2), ONE)
            x14 = x12
            x15 = subtract(add(x12, x4), ONE)
        else:
            x14 = x6
            x15 = subtract(add(x6, x4), ONE)
            x12 = subtract(add(x15, ONE), x2)
            x13 = x15
        if x1:
            x16 = x8
            x17 = subtract(add(x8, x3), ONE)
            x18 = x16
            x19 = subtract(add(x16, x5), ONE)
        else:
            x18 = x8
            x19 = subtract(add(x8, x5), ONE)
            x16 = subtract(add(x19, ONE), x3)
            x17 = x19
        x20 = canvas(BG_8DAB14C2, (x10, x11))
        x21 = _paint_rect_8dab14c2(x20, FG_8DAB14C2, x12, x13, x18, x19)
        x22 = _paint_rect_8dab14c2(x21, FG_8DAB14C2, x14, x15, x16, x17)
        x23 = tuple(j for j in range(x18, add(x19, ONE)) if not x16 <= j <= x17)
        x24 = tuple(i for i in range(x14, add(x15, ONE)) if not x12 <= i <= x13)
        x25 = []
        x26 = []
        for x27 in range(x12, add(x13, ONE)):
            x25.append((BG_8DAB14C2, (x27, x18)))
            x25.append((BG_8DAB14C2, (x27, x19)))
            x25.append((FG_8DAB14C2, (x27, decrement(x18))))
            x25.append((FG_8DAB14C2, (x27, increment(x19))))
        for x27 in x23:
            x25.append((BG_8DAB14C2, (x12, x27)))
            x25.append((BG_8DAB14C2, (x13, x27)))
            x25.append((FG_8DAB14C2, (decrement(x12), x27)))
            x25.append((FG_8DAB14C2, (increment(x13), x27)))
        for x27 in range(x16, add(x17, ONE)):
            x26.append((BG_8DAB14C2, (x14, x27)))
            x26.append((BG_8DAB14C2, (x15, x27)))
            x26.append((FG_8DAB14C2, (decrement(x14), x27)))
            x26.append((FG_8DAB14C2, (increment(x15), x27)))
        for x27 in x24:
            x26.append((BG_8DAB14C2, (x27, x16)))
            x26.append((BG_8DAB14C2, (x27, x17)))
            x26.append((FG_8DAB14C2, (x27, decrement(x16))))
            x26.append((FG_8DAB14C2, (x27, increment(x17))))
        x25 = tuple({x27 for x27 in x25 if 0 <= x27[1][0] < x10 and 0 <= x27[1][1] < x11})
        x26 = tuple({x27 for x27 in x26 if 0 <= x27[1][0] < x10 and 0 <= x27[1][1] < x11})
        if either(len(x25) == ZERO, len(x26) == ZERO):
            continue
        x27 = {choice(x25), choice(x26)}
        x28 = tuple(x29 for x29 in tuple({*x25, *x26}) if x29 not in x27)
        x29 = min(len(x28), choice((ZERO, ONE, ONE, TWO, TWO, THREE)))
        if x29 > ZERO:
            x30 = tuple(sample(x28, x29))
        else:
            x30 = tuple()
        x31 = tuple(x27) + x30
        x32 = x22
        for x33, x34 in x31:
            x32 = _paint_cell_8dab14c2(x32, x33, x34)
        x35 = _project_defects_8dab14c2(x32, (x12, x13, x18, x19), (x14, x15, x16, x17))
        if x32 == x35:
            continue
        x36 = tuple(sum(v == FG_8DAB14C2 for v in row) for row in x32)
        x37 = tuple(sum(x32[i][j] == FG_8DAB14C2 for i in range(x10)) for j in range(x11))
        x38 = min(x36[x12:add(x13, ONE)])
        x39 = max(x40 for x41, x40 in enumerate(x36) if not x12 <= x41 <= x13)
        x40 = min(x37[x16:add(x17, ONE)])
        x41 = max(x42 for x43, x42 in enumerate(x37) if not x16 <= x43 <= x17)
        if x38 <= add(x39, ONE):
            continue
        if x40 <= add(x41, ONE):
            continue
        if verify_8dab14c2(x32) != x35:
            continue
        return {"input": x32, "output": x35}
