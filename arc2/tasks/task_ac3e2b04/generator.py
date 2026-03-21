from arc2.core import *

from .verifier import verify_ac3e2b04


DIM_BOUNDS_AC3E2B04 = (10, 18)
MAX_LINE_COUNT_AC3E2B04 = FOUR
MAX_TARGET_COUNT_AC3E2B04 = TWO


def _axis_capacity_ac3e2b04(limit: int) -> int:
    return max(ONE, (limit + ONE) // FOUR)


def _sample_spaced_positions_ac3e2b04(
    limit: int,
    count: int,
) -> tuple[int, ...] | None:
    for _ in range(20):
        x0 = list(range(ONE, limit - ONE))
        x1 = []
        while x0 and len(x1) < count:
            x2 = choice(tuple(x0))
            x1.append(x2)
            x0 = [x3 for x3 in x0 if abs(x3 - x2) >= FOUR]
        if len(x1) == count:
            return tuple(sorted(x1))
    return None


def _render_input_vertical_ac3e2b04(
    dims: IntegerTuple,
    line_cols: tuple[int, ...],
    target_rows: tuple[int, ...],
    target_cols: tuple[int, ...],
) -> Grid:
    x0 = canvas(ZERO, dims)
    for x1 in line_cols:
        x0 = fill(x0, TWO, vfrontier((ZERO, x1)))
    for x2, x3 in zip(target_rows, target_cols):
        x4 = initset((x2, x3))
        x5 = outbox(x4)
        x0 = fill(x0, THREE, x5)
        x0 = fill(x0, TWO, x4)
    return x0


def _render_output_vertical_ac3e2b04(
    gi: Grid,
    line_cols: tuple[int, ...],
    target_rows: tuple[int, ...],
) -> Grid:
    x0 = gi
    x1 = ofcolor(gi, THREE)
    for x2 in target_rows:
        x3 = hfrontier((x2, ZERO))
        x0 = underfill(x0, ONE, x3)
        for x4 in line_cols:
            x5 = difference(outbox(initset((x2, x4))), x1)
            x0 = fill(x0, ONE, x5)
    return x0


def _rotate_ac3e2b04(
    grid: Grid,
    turns: int,
) -> Grid:
    if turns == ZERO:
        return grid
    if turns == ONE:
        return rot90(grid)
    if turns == TWO:
        return rot180(grid)
    return rot270(grid)


def generate_ac3e2b04(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, DIM_BOUNDS_AC3E2B04)
        x1 = unifint(diff_lb, diff_ub, DIM_BOUNDS_AC3E2B04)
        x2 = min(MAX_LINE_COUNT_AC3E2B04, _axis_capacity_ac3e2b04(x1))
        x3 = min(MAX_TARGET_COUNT_AC3E2B04, _axis_capacity_ac3e2b04(x0))
        x4 = randint(ONE, x2)
        x5 = min(x3, x4)
        x6 = ONE if x5 == ONE else choice((ONE, TWO, TWO))
        x6 = min(x6, x5)
        x7 = _sample_spaced_positions_ac3e2b04(x1, x4)
        x8 = _sample_spaced_positions_ac3e2b04(x0, x6)
        if either(equality(x7, None), equality(x8, None)):
            continue
        x9 = tuple(sample(x7, x6))
        x10 = _render_input_vertical_ac3e2b04((x0, x1), x7, x8, x9)
        x11 = _render_output_vertical_ac3e2b04(x10, x7, x8)
        x12 = choice((ZERO, ONE, TWO, THREE))
        x13 = _rotate_ac3e2b04(x10, x12)
        x14 = _rotate_ac3e2b04(x11, x12)
        if equality(x13, x14):
            continue
        if verify_ac3e2b04(x13) != x14:
            continue
        return {"input": x13, "output": x14}
