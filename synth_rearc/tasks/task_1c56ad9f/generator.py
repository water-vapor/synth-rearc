from synth_rearc.core import *


def _horizontal_rows_1c56ad9f(
    span: Integer,
    count: Integer,
) -> tuple[Integer, ...]:
    if count == TWO:
        return (ZERO, span - ONE)
    return tuple(round(idx * (span - ONE) / (count - ONE)) for idx in range(count))


def _vertical_cols_1c56ad9f(
    span: Integer,
    count: Integer,
) -> tuple[Integer, ...]:
    if count == TWO:
        return (ZERO, span - ONE)
    if count == FOUR and span >= SEVEN and choice((T, F)):
        x0 = span // TWO
        return (ZERO, x0 - ONE, x0, span - ONE)
    return tuple(round(idx * (span - ONE) / (count - ONE)) for idx in range(count))


def _wobble_cells_1c56ad9f(
    cells: frozenset[IntegerTuple],
    top: Integer,
    bottom: Integer,
) -> frozenset[IntegerTuple]:
    x0 = set()
    x1 = set(cells)
    x2 = NEG_ONE
    for row in range(bottom - ONE, top - ONE, NEG_TWO):
        x3 = {(i, j) for i, j in cells if i == row}
        x0.update(x3)
        x1.difference_update(x3)
        x1.update({(i, j + x2) for i, j in x3})
        x2 = -x2
    return frozenset(x1)


def generate_1c56ad9f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((13, 14, 15, 15))
        x1 = choice((13, 14, 15, 15))
        x2 = unifint(diff_lb, diff_ub, (SEVEN, x0 - TWO))
        x3 = unifint(diff_lb, diff_ub, (FIVE, min(NINE, x1 - TWO)))
        x4 = randint(ONE, x0 - x2 - ONE)
        x5 = randint(ONE, x1 - x3 - ONE)
        x6 = choice((TWO, TWO, THREE, THREE, FOUR if x2 >= TEN else THREE))
        x7 = choice((TWO, THREE, THREE, FOUR if x3 >= SEVEN else THREE))
        x8 = _horizontal_rows_1c56ad9f(x2, x6)
        x9 = _vertical_cols_1c56ad9f(x3, x7)
        x10 = choice(remove(ZERO, interval(ZERO, TEN, ONE)))
        x11 = frozenset(
            (x4 + i, x5 + j)
            for i in range(x2)
            for j in range(x3)
            if i in x8 or j in x9
        )
        x12 = _wobble_cells_1c56ad9f(x11, x4, x4 + x2 - ONE)
        x13 = canvas(ZERO, (x0, x1))
        x14 = fill(x13, x10, x11)
        x15 = fill(x13, x10, x12)
        if x14 != x15:
            return {"input": x14, "output": x15}
