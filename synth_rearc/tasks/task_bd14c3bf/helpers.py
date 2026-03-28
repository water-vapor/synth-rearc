from synth_rearc.core import *


SYMMETRIES_BD14C3BF = (
    identity,
    rot90,
    rot180,
    rot270,
    hmirror,
    vmirror,
    lambda x: rot90(hmirror(x)),
    lambda x: rot90(vmirror(x)),
)


def binary_shape_bd14c3bf(grid: Grid) -> Grid:
    return tuple(tuple(ONE if value != ZERO else ZERO for value in row) for row in grid)


def _collapse_adjacent_rows_bd14c3bf(grid: Grid) -> Grid:
    x0 = []
    x1 = None
    for row in grid:
        x2 = tuple(row)
        if x2 != x1:
            x0.append(x2)
        x1 = x2
    return tuple(x0)


def collapse_adjacent_repeats_bd14c3bf(grid: Grid) -> Grid:
    x0 = binary_shape_bd14c3bf(grid)
    x1 = None
    while x0 != x1:
        x1 = x0
        x0 = _collapse_adjacent_rows_bd14c3bf(x0)
        x0 = dmirror(_collapse_adjacent_rows_bd14c3bf(dmirror(x0)))
    return x0


def template_variants_bd14c3bf(grid: Grid) -> tuple[Grid, ...]:
    x0 = binary_shape_bd14c3bf(grid)
    x1 = []
    for x2 in SYMMETRIES_BD14C3BF:
        x3 = collapse_adjacent_repeats_bd14c3bf(x2(x0))
        if x3 not in x1:
            x1.append(x3)
    return tuple(x1)


def matches_template_bd14c3bf(candidate: Grid, template: Grid) -> Boolean:
    x0 = collapse_adjacent_repeats_bd14c3bf(candidate)
    x1 = template_variants_bd14c3bf(template)
    return x0 in x1


def expand_binary_shape_bd14c3bf(
    grid: Grid,
    row_factors: tuple[int, ...],
    col_factors: tuple[int, ...],
) -> Grid:
    x0 = binary_shape_bd14c3bf(grid)
    x1 = []
    for row, count in zip(x0, row_factors):
        for _ in range(count):
            x1.append(row)
    x2 = []
    for row in x1:
        x3 = []
        for value, count in zip(row, col_factors):
            x3.extend((value,) * count)
        x2.append(tuple(x3))
    return tuple(x2)


def shape_indices_bd14c3bf(
    grid: Grid,
    origin: IntegerTuple,
) -> Indices:
    x0 = binary_shape_bd14c3bf(grid)
    return frozenset(
        (origin[0] + i, origin[1] + j)
        for i, row in enumerate(x0)
        for j, value in enumerate(row)
        if value != ZERO
    )
