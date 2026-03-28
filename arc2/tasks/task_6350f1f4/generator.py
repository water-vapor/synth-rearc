from arc2.core import *

from .helpers import compose_tiles_6350f1f4


NONZERO_COLORS_6350F1F4 = tuple(value for value in range(ONE, TEN) if value != FIVE)


def _sample_reference_6350f1f4(
    span: int,
    diff_lb: float,
    diff_ub: float,
    majority: int,
    minority: int,
) -> Grid:
    x0 = [(i, j) for i in range(span) for j in range(span)]
    x1 = min((span * span - ONE) // TWO, span + ONE)
    while True:
        x2 = unifint(diff_lb, diff_ub, (ONE, x1))
        x3 = frozenset(sample(x0, x2))
        if x2 > ONE:
            x4 = {i for i, _ in x3}
            x5 = {j for _, j in x3}
            if len(x4) == ONE or len(x5) == ONE:
                continue
        x6 = canvas(majority, (span, span))
        x7 = fill(x6, minority, x3)
        return x7


def _noise_ok_6350f1f4(cells: Indices, span: int) -> bool:
    row_counts = [ZERO] * span
    col_counts = [ZERO] * span
    for i, j in cells:
        row_counts[i] += ONE
        col_counts[j] += ONE
    return all(count < span for count in row_counts) and all(count < span for count in col_counts)


def _corrupt_tile_6350f1f4(
    tile: Grid,
    protected: tuple[tuple[int, int], ...],
    max_noise: int,
) -> Grid:
    span = height(tile)
    x0 = {(i, j) for i in range(span) for j in range(span)}
    x1 = tuple(cell for cell in x0 if cell not in protected)
    x2 = min(max_noise, len(x1))
    if x2 == ZERO:
        return tile
    for _ in range(24):
        x3 = randint(ZERO, x2)
        x4 = frozenset(sample(x1, x3))
        if _noise_ok_6350f1f4(x4, span):
            return fill(tile, FIVE, x4)
    return tile


def _separator_cells_6350f1f4(span: int) -> tuple[tuple[int, int], ...]:
    size_value = span * span + span - ONE
    cuts = tuple(k * (span + ONE) - ONE for k in range(ONE, span))
    cells = {
        (i, j)
        for i in range(size_value)
        for j in range(size_value)
        if i in cuts or j in cuts
    }
    return tuple(cells)


def generate_6350f1f4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    span = unifint(diff_lb, diff_ub, (TWO, FIVE))
    majority, minority = sample(NONZERO_COLORS_6350F1F4, TWO)
    reference = _sample_reference_6350f1f4(span, diff_lb, diff_ub, majority, minority)
    majority_tile = canvas(majority, (span, span))
    minority_tile = canvas(minority, (span, span))

    positions = [(i, j) for i in range(span) for j in range(span)]
    outlier_count = ONE if span == TWO else randint(span - ONE, span)
    outliers = frozenset(sample(positions, outlier_count))
    mixed_positions = tuple(position for position in positions if position not in outliers)
    clean_reference_pos = choice(mixed_positions)

    majority_cells = tuple((i, j) for i in range(span) for j in range(span) if reference[i][j] == majority)
    minority_cells = tuple((i, j) for i in range(span) for j in range(span) if reference[i][j] == minority)

    input_tiles = []
    output_tiles = []
    for i in range(span):
        input_row = []
        output_row = []
        for j in range(span):
            pos = (i, j)
            is_outlier = pos in outliers
            base_input = minority_tile if is_outlier else reference
            output_tile = reference if is_outlier else majority_tile
            if pos == clean_reference_pos:
                input_tile = base_input
            else:
                protected = (choice(minority_cells if is_outlier else majority_cells),)
                max_noise = span + ONE if is_outlier else span
                input_tile = _corrupt_tile_6350f1f4(base_input, protected, max_noise)
            input_row.append(input_tile)
            output_row.append(output_tile)
        input_tiles.append(tuple(input_row))
        output_tiles.append(tuple(output_row))

    gi = compose_tiles_6350f1f4(tuple(input_tiles))
    x0 = _separator_cells_6350f1f4(span)
    x1 = min(len(x0), span + span)
    x2 = unifint(diff_lb, diff_ub, (ZERO, x1))
    x3 = frozenset(sample(x0, x2))
    gi = fill(gi, FIVE, x3)
    go = compose_tiles_6350f1f4(tuple(output_tiles))
    return {"input": gi, "output": go}
