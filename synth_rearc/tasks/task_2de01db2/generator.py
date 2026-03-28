from synth_rearc.core import *


TARGET_COLORS_2DE01DB2 = (FOUR, SIX, EIGHT)
GRID_STYLE_OPTIONS_2DE01DB2 = ("mixed", "mixed", "blocks", "blocks", "alternating")
ROW_STYLE_OPTIONS_2DE01DB2 = ("edge", "edge", "center", "double", "alternate")
NOISE_COLORS_2DE01DB2 = (SEVEN, SEVEN, SEVEN, TWO, THREE)


def _paint_columns_2de01db2(
    grid: Grid,
    value: Integer,
    cols: tuple[Integer, ...],
) -> Grid:
    x0 = product((ZERO,), cols)
    return fill(grid, value, x0)


def _row_pair_2de01db2(
    color_value: Integer,
    cols: tuple[Integer, ...],
) -> tuple[Grid, Grid]:
    x0 = canvas(ZERO, (ONE, TEN))
    x1 = _paint_columns_2de01db2(x0, color_value, cols)
    x2 = canvas(color_value, (ONE, TEN))
    x3 = _paint_columns_2de01db2(x2, ZERO, cols)
    return x1, x3


def _edge_support_2de01db2() -> tuple[Integer, ...]:
    x0 = choice((THREE, FOUR, FIVE, SIX, SIX, SEVEN))
    x1 = choice((ZERO, subtract(TEN, x0)))
    return interval(x1, add(x1, x0), ONE)


def _center_support_2de01db2() -> tuple[Integer, ...]:
    x0 = choice((FOUR, FIVE, SIX, SIX))
    x1 = TEN - x0
    x2 = choice((x1 // TWO, x1 - x1 // TWO))
    return interval(x2, x2 + x0, ONE)


def _double_support_2de01db2() -> tuple[Integer, ...]:
    while True:
        x0 = choice((TWO, THREE, FOUR))
        x1 = choice((TWO, THREE, FOUR))
        if add(x0, x1) <= SEVEN:
            x2 = interval(ZERO, x0, ONE)
            x3 = interval(subtract(TEN, x1), TEN, ONE)
            return x2 + x3


def _alternate_support_2de01db2() -> tuple[Integer, ...]:
    x0 = choice((ZERO, ONE))
    return interval(x0, TEN, TWO)


def _support_for_style_2de01db2(
    style: str,
) -> tuple[Integer, ...]:
    if style == "edge":
        return _edge_support_2de01db2()
    if style == "center":
        return _center_support_2de01db2()
    if style == "double":
        return _double_support_2de01db2()
    return _alternate_support_2de01db2()


def _zero_columns_2de01db2(
    cols: tuple[Integer, ...],
) -> tuple[Integer, ...]:
    x0 = set(cols)
    return tuple(j for j in range(TEN) if j not in x0)


def _column_runs_2de01db2(
    cols: tuple[Integer, ...],
) -> tuple[tuple[Integer, ...], ...]:
    if len(cols) == ZERO:
        return tuple()
    x0 = []
    x1 = [cols[ZERO]]
    for x2 in cols[ONE:]:
        if x2 == x1[-ONE] + ONE:
            x1.append(x2)
        else:
            x0.append(tuple(x1))
            x1 = [x2]
    x0.append(tuple(x1))
    return tuple(x0)


def _noise_columns_2de01db2(
    zero_cols: tuple[Integer, ...],
    count: Integer,
) -> tuple[Integer, ...]:
    x0 = tuple(x1 for x1 in _column_runs_2de01db2(zero_cols) if len(x1) >= count)
    if len(x0) > ZERO and choice((T, T, F)):
        x1 = choice(x0)
        x2 = randint(ZERO, len(x1) - count)
        return x1[x2:x2 + count]
    return tuple(sorted(sample(zero_cols, count)))


def _inject_noise_2de01db2(
    row: Grid,
    zero_cols: tuple[Integer, ...],
    count: Integer,
) -> Grid:
    x0 = _noise_columns_2de01db2(zero_cols, count)
    x1 = row
    for x2 in x0:
        x1 = _paint_columns_2de01db2(x1, choice(NOISE_COLORS_2DE01DB2), (x2,))
    return x1


def _row_styles_2de01db2() -> tuple[str, ...]:
    x0 = choice(GRID_STYLE_OPTIONS_2DE01DB2)
    if x0 == "alternating":
        return ("alternate", "alternate", "alternate")
    if x0 == "blocks":
        return tuple(choice(("edge", "edge", "center", "double")) for _ in range(THREE))
    return tuple(choice(ROW_STYLE_OPTIONS_2DE01DB2) for _ in range(THREE))


def generate_2de01db2(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = tuple(sample(TARGET_COLORS_2DE01DB2, THREE))
    x1 = _row_styles_2de01db2()
    x2 = tuple(_support_for_style_2de01db2(x3) for x3 in x1)
    x3 = tuple(_row_pair_2de01db2(x4, x5) for x4, x5 in zip(x0, x2))
    x4 = [x5 for x5, _ in x3]
    x5 = [x6 for _, x6 in x3]
    if x1 == ("alternate", "alternate", "alternate") and choice((T, T, F)):
        x6 = ZERO
    else:
        x6 = unifint(diff_lb, diff_ub, (ZERO, THREE))
    x7 = tuple(sample(interval(ZERO, THREE, ONE), x6)) if x6 > ZERO else tuple()
    for x8 in x7:
        x9 = _zero_columns_2de01db2(x2[x8])
        x10 = min(THREE, len(x9))
        x11 = unifint(diff_lb, diff_ub, (ONE, x10))
        x4[x8] = _inject_noise_2de01db2(x4[x8], x9, x11)
    x12 = merge(tuple(x4))
    x13 = merge(tuple(x5))
    return {"input": x12, "output": x13}
