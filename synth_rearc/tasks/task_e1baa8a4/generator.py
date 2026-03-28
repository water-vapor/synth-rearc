from synth_rearc.core import *

from .verifier import verify_e1baa8a4


COLORS_E1BAA8A4 = interval(ONE, TEN, ONE)


def _sample_parts_e1baa8a4(
    total: Integer,
    n_parts: Integer,
    minimum: Integer,
) -> tuple[Integer, ...]:
    remaining = total
    slots = n_parts
    parts = []
    for _ in range(n_parts - ONE):
        upper = remaining - minimum * (slots - ONE)
        part = randint(minimum, upper)
        parts.append(part)
        remaining -= part
        slots -= ONE
    parts.append(remaining)
    shuffle(parts)
    return tuple(parts)


def _recoverable_e1baa8a4(
    grid: Grid,
) -> Boolean:
    h = len(grid)
    w = len(grid[ZERO])
    rows_ok = all(grid[i] != grid[i + ONE] for i in range(h - ONE))
    cols_ok = all(
        tuple(grid[i][j] for i in range(h)) != tuple(grid[i][j + ONE] for i in range(h))
        for j in range(w - ONE)
    )
    return rows_ok and cols_ok


def _sample_macro_grid_e1baa8a4(
    h: Integer,
    w: Integer,
    ncolors: Integer,
) -> Grid:
    palette_ = sample(COLORS_E1BAA8A4, ncolors)
    ncells = h * w
    mandatory_positions = sample(interval(ZERO, ncells, ONE), ncolors)
    cells = [choice(palette_) for _ in range(ncells)]
    for idx, color_ in zip(mandatory_positions, palette_):
        cells[idx] = color_
    return tuple(tuple(cells[i * w:(i + ONE) * w]) for i in range(h))


def _expand_macro_grid_e1baa8a4(
    grid: Grid,
    row_heights: tuple[Integer, ...],
    col_widths: tuple[Integer, ...],
) -> Grid:
    rows = []
    for row, row_height in zip(grid, row_heights):
        expanded = tuple(
            value
            for value, col_width in zip(row, col_widths)
            for _ in range(col_width)
        )
        rows.extend([expanded] * row_height)
    return tuple(rows)


def generate_e1baa8a4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        oh = unifint(diff_lb, diff_ub, (TWO, FIVE))
        ow = unifint(diff_lb, diff_ub, (TWO, FOUR))
        h_total = unifint(diff_lb, diff_ub, (max(12, oh * TWO), min(18, oh * EIGHT)))
        w_total = unifint(diff_lb, diff_ub, (max(12, ow * TWO), min(18, ow * EIGHT)))
        row_heights = _sample_parts_e1baa8a4(h_total, oh, TWO)
        col_widths = _sample_parts_e1baa8a4(w_total, ow, TWO)
        min_colors = min(NINE, max(FOUR, oh * ow // TWO + TWO))
        max_colors = min(NINE, oh * ow)
        ncolors = unifint(diff_lb, diff_ub, (min_colors, max_colors))
        go = _sample_macro_grid_e1baa8a4(oh, ow, ncolors)
        if not _recoverable_e1baa8a4(go):
            continue
        gi = _expand_macro_grid_e1baa8a4(go, row_heights, col_widths)
        if verify_e1baa8a4(gi) != go:
            continue
        return {"input": gi, "output": go}
