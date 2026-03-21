from arc2.core import *


def _sample_top_row_bae5c565(
    n: Integer,
    center: Integer,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, ...]:
    colors = [value for value in range(TEN) if value != FIVE]
    while True:
        palette_size = unifint(diff_lb, diff_ub, (THREE, min(SEVEN, len(colors))))
        palette = sample(colors, palette_size)
        if choice((T, F, F)) and EIGHT not in palette:
            palette[randint(ZERO, decrement(len(palette)))] = EIGHT
        row = [FIVE for _ in range(n)]
        if choice((T, F, F, F)):
            left = [choice(palette) for _ in range(center)]
            row[:center] = left
            row[increment(center):] = list(reversed(left))
        else:
            for idx in range(n):
                if equality(idx, center):
                    continue
                row[idx] = choice(palette)
        if len(set(row) - {FIVE}) < THREE:
            continue
        return tuple(row)


def _render_output_bae5c565(
    top_row: tuple[Integer, ...],
    start_row: Integer,
) -> Grid:
    n = len(top_row)
    center = n // TWO
    dropped = list(top_row)
    dropped[center] = EIGHT
    go = canvas(FIVE, (n, n))
    for row in range(start_row, n):
        radius = row - start_row
        left = max(ZERO, center - radius)
        right = min(n - ONE, center + radius)
        cells = frozenset((dropped[col], (row, col)) for col in range(left, right + ONE))
        go = paint(go, cells)
    return go


def generate_bae5c565(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        center = unifint(diff_lb, diff_ub, (FOUR, 12))
        n = add(double(center), ONE)
        start_row = choice((decrement(center), center))
        top_row = _sample_top_row_bae5c565(n, center, diff_lb, diff_ub)

        gi = canvas(FIVE, (n, n))
        x0 = frozenset((value, (ZERO, idx)) for idx, value in enumerate(top_row))
        x1 = connect((start_row, center), (decrement(n), center))
        gi = paint(gi, x0)
        gi = fill(gi, EIGHT, x1)

        go = _render_output_bae5c565(top_row, start_row)
        if equality(gi, go):
            continue

        from .verifier import verify_bae5c565

        if verify_bae5c565(gi) != go:
            continue
        return {"input": gi, "output": go}
