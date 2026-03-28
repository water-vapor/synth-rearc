from arc2.core import *


def _step_options_5ad8a7c0(
    level: int,
    target: int,
) -> tuple[int, ...]:
    x0 = [level]
    if positive(level):
        x0.append(decrement(level))
    if greater(target, level):
        x0.append(increment(level))
    return tuple(dict.fromkeys(x0))


def _sample_levels_5ad8a7c0(
    count: int,
    target: int,
) -> tuple[int, ...]:
    x0 = tuple(range(target + ONE))
    while True:
        x1 = [choice(x0)]
        while len(x1) < count:
            x2 = _step_options_5ad8a7c0(x1[-ONE], target)
            x1.append(choice(x2))
        x3 = tuple(x1)
        x4 = contained(target, x3)
        x5 = branch(equality(target, ZERO), T, greater(target, min(x3)))
        if both(x4, x5):
            return x3


def _row_patch_5ad8a7c0(
    row: int,
    inset: int,
    width: int,
    filled: bool,
) -> Indices:
    x0 = (row, inset)
    x1 = (row, subtract(width, increment(inset)))
    if filled:
        return connect(x0, x1)
    x2 = initset(x0)
    x3 = initset(x1)
    return combine(x2, x3)


def _render_rows_5ad8a7c0(
    rows: tuple[int | None, ...],
    width: int,
    target: int,
) -> tuple[Grid, Grid]:
    x0 = (len(rows), width)
    x1 = canvas(ZERO, x0)
    x2 = canvas(ZERO, x0)
    for x3, x4 in enumerate(rows):
        if x4 is None:
            continue
        x5 = _row_patch_5ad8a7c0(x3, x4, width, F)
        x1 = fill(x1, TWO, x5)
        x6 = equality(x4, target)
        x7 = _row_patch_5ad8a7c0(x3, x4, width, x6)
        x2 = fill(x2, TWO, x7)
    return x1, x2


def generate_5ad8a7c0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (THREE, NINE))
        x1 = double(x0)
        x2 = unifint(diff_lb, diff_ub, (FOUR, TEN))
        x3 = subtract(x0, ONE)
        x4 = unifint(diff_lb, diff_ub, (ZERO, x3))
        x5 = branch(equality(x4, ZERO), TWO, THREE)
        x6 = unifint(diff_lb, diff_ub, (x5, x2))
        x7 = _sample_levels_5ad8a7c0(x6, x4)
        x8 = sorted(sample(tuple(range(x2)), x6))
        x9 = [None] * x2
        for x10, x11 in zip(x8, x7):
            x9[x10] = x11
        x12 = tuple(x9)
        x13, x14 = _render_rows_5ad8a7c0(x12, x1, x4)
        return {"input": x13, "output": x14}
