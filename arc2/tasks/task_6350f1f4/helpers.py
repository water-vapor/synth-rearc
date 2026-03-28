from arc2.core import *


def split_tiles_6350f1f4(grid: Grid) -> tuple[tuple[Grid, ...], ...]:
    x0 = replace(grid, FIVE, ZERO)
    x1 = frontiers(x0)
    x2 = sfilter(x1, hline)
    x3 = increment(size(x2))
    x4 = sfilter(x1, vline)
    x5 = increment(size(x4))
    x6 = compress(x0)
    x7 = vsplit(x6, x3)
    x8 = rbind(hsplit, x5)
    x9 = apply(x8, x7)
    return x9


def compose_tiles_6350f1f4(tiles: tuple[tuple[Grid, ...], ...]) -> Grid:
    row_grids = []
    for row in tiles:
        joined = row[ZERO]
        for tile in row[ONE:]:
            joined = hconcat(joined, canvas(ZERO, (height(joined), ONE)))
            joined = hconcat(joined, tile)
        row_grids.append(joined)
    joined = row_grids[ZERO]
    for row_grid in row_grids[ONE:]:
        joined = vconcat(joined, canvas(ZERO, (ONE, width(joined))))
        joined = vconcat(joined, row_grid)
    return joined
