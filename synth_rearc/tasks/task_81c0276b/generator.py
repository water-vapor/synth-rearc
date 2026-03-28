from synth_rearc.core import *


NONZERO_COLORS_81C0276B = remove(ZERO, interval(ZERO, TEN, ONE))
COUNT_POOL_81C0276B = interval(ONE, FIVE, ONE)


def _shape_81c0276b(
    nrows: Integer,
    ncols: Integer,
) -> tuple[Integer, Integer]:
    h = 5 * nrows + (ONE if nrows == THREE else -ONE)
    w = 5 * ncols + (ONE if nrows == ncols else -TWO)
    return h, w


def _sample_ncolors_81c0276b(total_cells: Integer) -> Integer:
    feasible = tuple(
        k
        for k in range(TWO, FIVE)
        if (k * (k + ONE)) // TWO < total_cells
    )
    return choice(feasible)


def _sample_counts_81c0276b(
    total_cells: Integer,
    ncolors: Integer,
) -> tuple[Integer, ...]:
    while True:
        counts = tuple(sorted(sample(COUNT_POOL_81C0276B, ncolors)))
        divider_count = total_cells - sum(counts)
        if divider_count < ONE:
            continue
        if divider_count == total_cells:
            continue
        return counts


def _render_output_81c0276b(
    specs: tuple[tuple[Integer, Integer], ...],
) -> Grid:
    widths = tuple(count for _, count in specs)
    go = canvas(ZERO, (size(specs), maximum(widths)))
    for row, (value, count) in enumerate(specs):
        patch = connect((row, ZERO), (row, count - ONE))
        go = fill(go, value, patch)
    return go


def _render_input_81c0276b(
    nrows: Integer,
    ncols: Integer,
    divider: Integer,
    cells: tuple[Integer, ...],
) -> Grid:
    h, w = _shape_81c0276b(nrows, ncols)
    gi = canvas(ZERO, (h, w))
    for row in interval(FOUR, h, FIVE):
        gi = fill(gi, divider, connect((row, ZERO), (row, w - ONE)))
    for col in interval(FOUR, w, FIVE):
        gi = fill(gi, divider, connect((ZERO, col), (h - ONE, col)))
    idx = ZERO
    for row in interval(ONE, h, FIVE):
        for col in interval(ONE, w, FIVE):
            patch = frozenset(
                {
                    (row, col),
                    (row, col + ONE),
                    (row + ONE, col),
                    (row + ONE, col + ONE),
                }
            )
            gi = fill(gi, cells[idx], patch)
            idx += ONE
    return gi


def generate_81c0276b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        nrows = unifint(diff_lb, diff_ub, (THREE, FOUR))
        ncols = unifint(diff_lb, diff_ub, (THREE, FOUR))
        total_cells = nrows * ncols
        ncolors = _sample_ncolors_81c0276b(total_cells)
        divider = choice(NONZERO_COLORS_81C0276B)
        colors = sample(remove(divider, NONZERO_COLORS_81C0276B), ncolors)
        counts = _sample_counts_81c0276b(total_cells, ncolors)
        specs = tuple(zip(colors, counts))
        divider_count = total_cells - sum(counts)
        cells = [divider] * divider_count
        for value, count in specs:
            cells.extend(repeat(value, count))
        shuffle(cells)
        gi = _render_input_81c0276b(nrows, ncols, divider, tuple(cells))
        go = _render_output_81c0276b(specs)
        if gi == go:
            continue
        return {"input": gi, "output": go}
