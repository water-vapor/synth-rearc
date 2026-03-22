from arc2.core import *


INPUT_SHAPE_95755FF2 = (11, 11)
MID_95755FF2 = FIVE
SOURCE_COLORS_95755FF2 = tuple(x0 for x0 in interval(ONE, TEN, ONE) if x0 != TWO)
FRAME_95755FF2 = frozenset(
    {
        (x0, subtract(TEN, abs(subtract(x0, MID_95755FF2))))
        for x0 in range(INPUT_SHAPE_95755FF2[ZERO])
    }
    | {
        (x1, abs(subtract(x1, MID_95755FF2)))
        for x1 in range(INPUT_SHAPE_95755FF2[ZERO])
    }
)
TOP_LEFT_SOURCE_COLUMNS_95755FF2 = (ZERO, ONE, TWO, THREE, FOUR)
TOP_RIGHT_SOURCE_COLUMNS_95755FF2 = (SIX, SEVEN, EIGHT, NINE, TEN)
LEFT_TOP_SOURCE_ROWS_95755FF2 = (ONE, TWO, THREE, FOUR)
LEFT_BOTTOM_SOURCE_ROWS_95755FF2 = (SIX, SEVEN, EIGHT, NINE)


def _apply_rule_95755ff2(grid: Grid) -> Grid:
    x0 = height(grid)
    x1 = width(grid)
    x2 = [list(x3) for x3 in grid]
    x3 = tuple(tuple(x4 for x4, x5 in enumerate(x6) if x5 == TWO) for x6 in grid)
    x4 = tuple((x5[ZERO], x5[-ONE]) for x5 in x3)
    x5 = tuple(tuple(x6 for x6 in range(x0) if grid[x6][x7] == TWO) for x7 in range(x1))
    x6 = tuple((x7[ZERO], x7[-ONE]) for x7 in x5)
    for x8, x9 in enumerate(grid[ZERO]):
        if x9 not in (ZERO, TWO):
            x10, x11 = x6[x8]
            for x12 in range(x10 + ONE, x11):
                if x2[x12][x8] != ZERO:
                    break
                x2[x12][x8] = x9
    for x13, x14 in enumerate(grid[-ONE]):
        if x14 not in (ZERO, TWO):
            x15, x16 = x6[x13]
            for x17 in range(x16 - ONE, x15, -ONE):
                if x2[x17][x13] != ZERO:
                    break
                x2[x17][x13] = x14
    for x18, x19 in enumerate(grid):
        x20 = x19[ZERO]
        if x20 not in (ZERO, TWO):
            x21, x22 = x4[x18]
            for x23 in range(x21 + ONE, x22):
                if x2[x18][x23] != ZERO:
                    break
                x2[x18][x23] = x20
        x24 = x19[-ONE]
        if x24 not in (ZERO, TWO):
            x25, x26 = x4[x18]
            for x27 in range(x26 - ONE, x25, -ONE):
                if x2[x18][x27] != ZERO:
                    break
                x2[x18][x27] = x24
    return tuple(tuple(x28) for x28 in x2)


def _contiguous_span_95755ff2(values: tuple[int, ...], length: int) -> tuple[int, ...]:
    x0 = randint(ZERO, len(values) - length)
    x1 = x0 + length
    return values[x0:x1]


def _vertical_blocker_cells_95755ff2(top_cols: tuple[int, ...], bottom_cols: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    x0 = set()
    for x1 in top_cols + bottom_cols:
        x2 = abs(subtract(x1, MID_95755FF2))
        x3 = x2 + ONE
        x4 = subtract(TEN, x2)
        for x5 in range(x3, x4):
            x0.add((x5, x1))
    return tuple(sorted(x0))


def _horizontal_blocker_cells_95755ff2(left_rows: tuple[int, ...], right_rows: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    x0 = set()
    for x1 in left_rows + right_rows:
        x2 = abs(subtract(x1, MID_95755FF2))
        x3 = x2 + ONE
        x4 = subtract(TEN, x2)
        for x5 in range(x3, x4):
            x0.add((x1, x5))
    return tuple(sorted(x0))


def _paint_singleton_blockers_95755ff2(grid: Grid, cells: tuple[tuple[int, int], ...], count: int) -> Grid:
    x0 = grid
    if not cells or count == ZERO:
        return x0
    x1 = min(count, len(cells))
    x2 = sample(cells, x1)
    for x3 in x2:
        x4 = choice(SOURCE_COLORS_95755FF2)
        x0 = fill(x0, x4, initset(x3))
    return x0


def _paint_pair_blockers_95755ff2(grid: Grid, cells: tuple[tuple[int, int], ...], count: int) -> Grid:
    x0 = grid
    if len(cells) < TWO or count == ZERO:
        return x0
    x1 = set(cells)
    x2 = []
    for x3, x4 in cells:
        x5 = (x3, x4 + ONE)
        x6 = (x3 + ONE, x4)
        if x5 in x1:
            x2.append(((x3, x4), x5))
        if x6 in x1:
            x2.append(((x3, x4), x6))
    if not x2:
        return x0
    x7 = min(count, len(x2))
    for x8 in sample(tuple(x2), x7):
        x9 = choice(SOURCE_COLORS_95755FF2)
        x0 = fill(x0, x9, frozenset(x8))
    return x0


def generate_95755ff2(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = fill(canvas(ZERO, INPUT_SHAPE_95755FF2), TWO, FRAME_95755FF2)
        x1 = choice((ZERO, ONE, TWO, THREE))
        if x1 != THREE:
            x2 = branch(equality(x1, ZERO), TOP_LEFT_SOURCE_COLUMNS_95755FF2, TOP_RIGHT_SOURCE_COLUMNS_95755FF2)
            x3 = branch(equality(x1, ZERO), TOP_RIGHT_SOURCE_COLUMNS_95755FF2, TOP_LEFT_SOURCE_COLUMNS_95755FF2)
            x4 = unifint(diff_lb, diff_ub, (ONE, len(x2)))
            x5 = unifint(diff_lb, diff_ub, (ONE, len(x3)))
            x6 = _contiguous_span_95755ff2(x2, x4)
            x7 = _contiguous_span_95755ff2(x3, x5)
            for x8 in x6:
                x9 = choice(SOURCE_COLORS_95755FF2)
                x0 = fill(x0, x9, initset((ZERO, x8)))
            for x10 in x7:
                x11 = choice(SOURCE_COLORS_95755FF2)
                x0 = fill(x0, x11, initset((TEN, x10)))
            x12 = _vertical_blocker_cells_95755ff2(x6, x7)
        else:
            x13 = choice((ZERO, ONE))
            x14 = branch(equality(x13, ZERO), LEFT_TOP_SOURCE_ROWS_95755FF2, LEFT_BOTTOM_SOURCE_ROWS_95755FF2)
            x15 = branch(equality(x13, ZERO), LEFT_BOTTOM_SOURCE_ROWS_95755FF2, LEFT_TOP_SOURCE_ROWS_95755FF2)
            x16 = unifint(diff_lb, diff_ub, (ONE, len(x14)))
            x17 = unifint(diff_lb, diff_ub, (ONE, len(x15)))
            x18 = _contiguous_span_95755ff2(x14, x16)
            x19 = _contiguous_span_95755ff2(x15, x17)
            for x20 in x18:
                x21 = choice(SOURCE_COLORS_95755FF2)
                x0 = fill(x0, x21, initset((x20, ZERO)))
            for x22 in x19:
                x23 = choice(SOURCE_COLORS_95755FF2)
                x0 = fill(x0, x23, initset((x22, TEN)))
            x12 = _horizontal_blocker_cells_95755ff2(x18, x19)
        x24 = unifint(diff_lb, diff_ub, (ZERO, min(FOUR, len(x12))))
        x25 = _paint_singleton_blockers_95755ff2(x0, x12, x24)
        x26 = branch(greater(len(x12), ONE), unifint(diff_lb, diff_ub, (ZERO, TWO)), ZERO)
        x27 = _paint_pair_blockers_95755ff2(x25, x12, x26)
        x28 = _apply_rule_95755ff2(x27)
        if x27 != x28:
            return {"input": x27, "output": x28}
