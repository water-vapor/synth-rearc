from arc2.core import *


_COUNT_CHOICES_0c9aba6e = tuple(
    (n00, n20, n06, 24 - n00 - n20 - n06)
    for n00 in range(SIX, TEN)
    for n20 in range(THREE, TEN)
    for n06 in range(FOUR, EIGHT)
    if FIVE <= 24 - n00 - n20 - n06 <= NINE
    if TEN <= n20 + 24 - n00 - n20 - n06 <= 14
    if NINE <= n06 + 24 - n00 - n20 - n06 <= 13
)

_STATE_VALUES_0c9aba6e = (
    (ZERO, ZERO, EIGHT),
    (TWO, ZERO, ZERO),
    (ZERO, SIX, ZERO),
    (TWO, SIX, ZERO),
)


def _reshape_states_0c9aba6e(codes: tuple[int, ...]) -> Grid:
    return tuple(
        tuple(codes[FOUR * i + j] for j in range(FOUR))
        for i in range(SIX)
    )


def _render_panels_0c9aba6e(codes: Grid) -> tuple[Grid, Grid, Grid]:
    top = []
    bottom = []
    output = []
    for row in codes:
        top_row = []
        bottom_row = []
        output_row = []
        for code in row:
            tval, bval, oval = _STATE_VALUES_0c9aba6e[code]
            top_row.append(tval)
            bottom_row.append(bval)
            output_row.append(oval)
        top.append(tuple(top_row))
        bottom.append(tuple(bottom_row))
        output.append(tuple(output_row))
    return tuple(top), tuple(bottom), tuple(output)


def _row_counts_0c9aba6e(grid: Grid, color: Integer) -> tuple[int, ...]:
    return tuple(sum(value == color for value in row) for row in grid)


def _col_counts_0c9aba6e(grid: Grid, color: Integer) -> tuple[int, ...]:
    return tuple(sum(row[j] == color for row in grid) for j in range(FOUR))


def _valid_panels_0c9aba6e(
    top: Grid,
    bottom: Grid,
    output: Grid,
) -> bool:
    top_rows = _row_counts_0c9aba6e(top, TWO)
    bottom_rows = _row_counts_0c9aba6e(bottom, SIX)
    output_rows = _row_counts_0c9aba6e(output, EIGHT)
    top_cols = _col_counts_0c9aba6e(top, TWO)
    bottom_cols = _col_counts_0c9aba6e(bottom, SIX)
    if min(top_rows) == ZERO:
        return False
    if bottom_rows.count(ZERO) > ONE:
        return False
    if min(top_cols) == ZERO or min(bottom_cols) == ZERO:
        return False
    if max(output_rows) > THREE:
        return False
    if sum(count > ZERO for count in output_rows) < FOUR:
        return False
    if len(set(top)) < FOUR or len(set(bottom)) < FOUR:
        return False
    if top == hmirror(top) or top == vmirror(top) or top == rot180(top):
        return False
    if bottom == hmirror(bottom) or bottom == vmirror(bottom) or bottom == rot180(bottom):
        return False
    return True


def generate_0c9aba6e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (ZERO, len(_COUNT_CHOICES_0c9aba6e) - ONE))
    x1 = _COUNT_CHOICES_0c9aba6e[x0]
    while True:
        x2 = (
            (ZERO,) * x1[ZERO]
            + (ONE,) * x1[ONE]
            + (TWO,) * x1[TWO]
            + (THREE,) * x1[THREE]
        )
        x3 = list(x2)
        shuffle(x3)
        x4 = _reshape_states_0c9aba6e(tuple(x3))
        x5, x6, go = _render_panels_0c9aba6e(x4)
        if not _valid_panels_0c9aba6e(x5, x6, go):
            continue
        x7 = canvas(SEVEN, (ONE, FOUR))
        gi = vconcat(vconcat(x5, x7), x6)
        return {"input": gi, "output": go}
