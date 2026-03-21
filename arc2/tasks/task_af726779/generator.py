from arc2.core import *


def _next_columns_af726779(cols: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((a + b) // TWO for a, b in zip(cols, cols[1:]) if b - a == TWO)


def _derive_levels_af726779(cols: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    x0 = []
    x1 = cols
    while True:
        x1 = _next_columns_af726779(x1)
        if len(x1) == ZERO:
            return tuple(x0)
        x0.append(x1)


def _make_runs_af726779(
    diff_lb: float,
    diff_ub: float,
) -> tuple[int, ...]:
    while True:
        x0 = unifint(diff_lb, diff_ub, (THREE, NINE))
        x1 = [ONE] * x0
        x2 = choice((ZERO, ONE, ONE, ONE, TWO, TWO, TWO))
        if x2 == ZERO:
            pass
        elif x2 == ONE:
            x3 = unifint(diff_lb, diff_ub, (ONE, max(ONE, x0 // TWO)))
            x4 = sample(interval(ZERO, x0, ONE), x3)
            for x5 in x4:
                x1[x5] = choice((TWO, TWO, THREE))
        else:
            x3 = choice(interval(ZERO, x0, ONE))
            x1[x3] = unifint(diff_lb, diff_ub, (FOUR, SEVEN))
            x4 = tuple(i for i in range(x0) if i != x3)
            x5 = min(len(x4), max(ONE, x0 // THREE))
            x6 = randint(ZERO, x5)
            x7 = sample(x4, x6)
            for x8 in x7:
                x1[x8] = choice((TWO, TWO, THREE))
        x9 = add(sum(x1), subtract(x0, ONE))
        if 11 <= x9 <= 24:
            return tuple(x1)


def _source_columns_af726779(
    left: int,
    runs: tuple[int, ...],
) -> tuple[int, ...]:
    x0 = []
    x1 = left
    for x2, x3 in enumerate(runs):
        x0.extend(range(x1, x1 + x3))
        x1 += x3
        if x2 != len(runs) - 1:
            x1 += ONE
    return tuple(x0)


def _paint_levels_af726779(
    grid: Grid,
    src_row: int,
    levels: tuple[tuple[int, ...], ...],
) -> Grid:
    x0 = grid
    x1 = SIX
    for x2, x3 in enumerate(levels, start=ONE):
        x4 = add(src_row, multiply(TWO, x2))
        x5 = product((x4,), x3)
        x0 = fill(x0, x1, x5)
        x1 = branch(equality(x1, SIX), SEVEN, SIX)
    return x0


def generate_af726779(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _make_runs_af726779(diff_lb, diff_ub)
        x1 = add(sum(x0), subtract(len(x0), ONE))
        x2 = randint(ZERO, min(THREE, 30 - x1))
        x3 = randint(ZERO, min(THREE, 30 - x1 - x2))
        x4 = _source_columns_af726779(x2, x0)
        x5 = _derive_levels_af726779(x4)
        x6 = len(x5)
        if x6 == ZERO:
            continue
        x7 = unifint(diff_lb, diff_ub, (ONE, FOUR))
        x8 = unifint(diff_lb, diff_ub, (ONE, FOUR))
        x9 = add(add(add(x7, multiply(TWO, x6)), x8), ONE)
        x10 = add(add(x1, x2), x3)
        if x9 > 30 or x10 > 30:
            continue
        x11 = canvas(THREE, (x9, x10))
        x12 = fill(x11, SEVEN, product((x7,), x4))
        x13 = _paint_levels_af726779(x12, x7, x5)
        return {"input": x12, "output": x13}
