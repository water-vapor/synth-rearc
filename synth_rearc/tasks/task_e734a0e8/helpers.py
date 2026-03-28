from synth_rearc.core import *


def split_tiles_e734a0e8(grid: Grid) -> tuple[tuple[Grid, ...], ...]:
    x0 = frontiers(grid)
    x1 = sfilter(x0, hline)
    x2 = increment(size(x1))
    x3 = sfilter(x0, vline)
    x4 = increment(size(x3))
    x5 = compress(grid)
    x6 = vsplit(x5, x2)
    x7 = rbind(hsplit, x4)
    return apply(x7, x6)


def compose_tiles_e734a0e8(tiles: tuple[tuple[Grid, ...], ...]) -> Grid:
    row_grids = []
    for row in tiles:
        joined = row[0]
        for tile in row[1:]:
            joined = hconcat(joined, canvas(ZERO, (height(joined), ONE)))
            joined = hconcat(joined, tile)
        row_grids.append(joined)
    joined = row_grids[0]
    for row_grid in row_grids[1:]:
        joined = vconcat(joined, canvas(ZERO, (ONE, width(joined))))
        joined = vconcat(joined, row_grid)
    return joined


def blank_tile_e734a0e8(tile_span: Integer) -> Grid:
    return canvas(SEVEN, (tile_span, tile_span))


def bbox_midpoint_e734a0e8(patch: Patch) -> IntegerTuple:
    return divide(add(ulcorner(patch), lrcorner(patch)), TWO)


def tile_is_motif_e734a0e8(tile: Grid) -> bool:
    return any(value not in (ZERO, SEVEN) for row in tile for value in row)


def tile_is_target_e734a0e8(tile: Grid, marker: IntegerTuple) -> bool:
    return index(tile, marker) == ZERO and all(value in (ZERO, SEVEN) for row in tile for value in row)


def motif_center_e734a0e8(tile: Grid) -> IntegerTuple:
    motif_color = next(value for value in palette(tile) if value not in (ZERO, SEVEN))
    motif_patch = ofcolor(tile, motif_color)
    return bbox_midpoint_e734a0e8(motif_patch)


def make_motif_patch_e734a0e8(
    diff_lb: float,
    diff_ub: float,
    tile_span: Integer,
) -> Indices:
    min_cells = THREE
    max_cells = min(tile_span * tile_span - ONE, tile_span * tile_span // TWO + tile_span)
    target_size = unifint(diff_lb, diff_ub, (min_cells, max_cells))
    tile_center = astuple(tile_span // TWO, tile_span // TWO)
    while True:
        patch = frozenset({(randint(ZERO, tile_span - ONE), randint(ZERO, tile_span - ONE))})
        while size(patch) < target_size:
            frontier = set()
            for cell in patch:
                frontier |= {
                    neighbor
                    for neighbor in dneighbors(cell)
                    if ZERO <= neighbor[0] < tile_span
                    and ZERO <= neighbor[1] < tile_span
                    and neighbor not in patch
                }
            if not frontier:
                break
            patch = insert(choice(totuple(frozenset(frontier))), patch)
        if size(patch) < min_cells:
            continue
        patch = normalize(patch)
        patch = shift(patch, subtract(tile_center, bbox_midpoint_e734a0e8(patch)))
        if size(patch) < tile_span * tile_span:
            return patch
