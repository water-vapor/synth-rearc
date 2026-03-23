from arc2.core import *


def frontier_layout_2546ccf6(
    grid: Grid,
) -> tuple[tuple[Integer, ...], tuple[Integer, ...], Integer]:
    x0 = frontiers(grid)
    x1 = order(sfilter(x0, hline), uppermost)
    x2 = order(sfilter(x0, vline), leftmost)
    x3 = tuple(uppermost(obj) for obj in x1)
    x4 = tuple(leftmost(obj) for obj in x2)
    x5 = color(x1[ZERO] if len(x1) > ZERO else x2[ZERO])
    return x3, x4, x5


def cell_spans_2546ccf6(
    length: Integer,
    frontiers_: tuple[Integer, ...],
) -> tuple[tuple[Integer, Integer], ...]:
    spans = []
    start = ZERO
    for frontier in frontiers_:
        spans.append((start, frontier))
        start = increment(frontier)
    spans.append((start, length))
    return tuple(spans)


def cell_layout_2546ccf6(
    grid: Grid,
) -> tuple[tuple[tuple[Integer, Integer], ...], tuple[tuple[Integer, Integer], ...], Integer]:
    x0, x1, x2 = frontier_layout_2546ccf6(grid)
    x3 = cell_spans_2546ccf6(len(grid), x0)
    x4 = cell_spans_2546ccf6(len(grid[ZERO]), x1)
    return x3, x4, x2


def cell_origin_2546ccf6(
    row_spans: tuple[tuple[Integer, Integer], ...],
    col_spans: tuple[tuple[Integer, Integer], ...],
    row_index: Integer,
    col_index: Integer,
) -> tuple[Integer, Integer]:
    return row_spans[row_index][ZERO], col_spans[col_index][ZERO]


def crop_cell_2546ccf6(
    grid: Grid,
    row_spans: tuple[tuple[Integer, Integer], ...],
    col_spans: tuple[tuple[Integer, Integer], ...],
    row_index: Integer,
    col_index: Integer,
) -> Grid:
    x0, x1 = row_spans[row_index]
    x2, x3 = col_spans[col_index]
    return crop(grid, (x0, x2), (subtract(x1, x0), subtract(x3, x2)))


def paint_cell_patch_2546ccf6(
    grid: Grid,
    row_spans: tuple[tuple[Integer, Integer], ...],
    col_spans: tuple[tuple[Integer, Integer], ...],
    row_index: Integer,
    col_index: Integer,
    value: Integer,
    patch: frozenset[tuple[Integer, Integer]],
) -> Grid:
    x0 = cell_origin_2546ccf6(row_spans, col_spans, row_index, col_index)
    x1 = shift(patch, x0)
    return fill(grid, value, x1)


def paint_cell_grid_2546ccf6(
    grid: Grid,
    row_spans: tuple[tuple[Integer, Integer], ...],
    col_spans: tuple[tuple[Integer, Integer], ...],
    row_index: Integer,
    col_index: Integer,
    cell_grid: Grid,
) -> Grid:
    x0 = cell_origin_2546ccf6(row_spans, col_spans, row_index, col_index)
    x1 = grid
    for value in sorted(v for v in palette(cell_grid) if v != ZERO):
        x2 = shift(ofcolor(cell_grid, value), x0)
        x1 = fill(x1, value, x2)
    return x1


def rot180_patch_2546ccf6(
    height_value: Integer,
    width_value: Integer,
    patch: frozenset[tuple[Integer, Integer]],
) -> frozenset[tuple[Integer, Integer]]:
    return frozenset(
        (subtract(decrement(height_value), i), subtract(decrement(width_value), j))
        for i, j in patch
    )


def separator_positions_2546ccf6(
    lengths: tuple[Integer, ...],
) -> tuple[Integer, ...]:
    positions = []
    cursor = lengths[ZERO]
    for length in lengths[ONE:]:
        positions.append(cursor)
        cursor = add(cursor, increment(length))
    return tuple(positions)


def build_lattice_2546ccf6(
    row_heights: tuple[Integer, ...],
    col_widths: tuple[Integer, ...],
    separator_color: Integer,
) -> Grid:
    x0 = add(sum(row_heights), subtract(len(row_heights), ONE))
    x1 = add(sum(col_widths), subtract(len(col_widths), ONE))
    x2 = canvas(ZERO, (x0, x1))
    for row_value in separator_positions_2546ccf6(row_heights):
        x2 = fill(x2, separator_color, connect((row_value, ZERO), (row_value, decrement(x1))))
    for col_value in separator_positions_2546ccf6(col_widths):
        x2 = fill(x2, separator_color, connect((ZERO, col_value), (decrement(x0), col_value)))
    return x2
