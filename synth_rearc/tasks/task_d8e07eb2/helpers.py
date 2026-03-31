from synth_rearc.core import *


QUERY_TILE_STARTS_D8E07EB2 = (
    (ONE, TWO),
    (ONE, SEVEN),
    (ONE, 12),
    (ONE, 17),
)

LIBRARY_TILE_STARTS_D8E07EB2 = (
    ((EIGHT, TWO), (EIGHT, SEVEN), (EIGHT, 12), (EIGHT, 17)),
    ((13, TWO), (13, SEVEN), (13, 12), (13, 17)),
    ((18, TWO), (18, SEVEN), (18, 12), (18, 17)),
    ((23, TWO), (23, SEVEN), (23, 12), (23, 17)),
)

LIBRARY_TILES_D8E07EB2 = (
    (
        ((TWO, EIGHT, TWO), (EIGHT, TWO, EIGHT), (TWO, EIGHT, TWO)),
        ((ZERO, EIGHT, EIGHT), (ZERO, ZERO, ZERO), (ZERO, EIGHT, ZERO)),
        ((EIGHT, EIGHT, SEVEN), (EIGHT, EIGHT, SEVEN), (SEVEN, SEVEN, SEVEN)),
        ((NINE, EIGHT, NINE), (NINE, NINE, EIGHT), (NINE, NINE, NINE)),
    ),
    (
        ((SEVEN, EIGHT, EIGHT), (SEVEN, SEVEN, SEVEN), (SEVEN, EIGHT, EIGHT)),
        ((ONE, ONE, ONE), (EIGHT, ONE, EIGHT), (ONE, ONE, ONE)),
        ((EIGHT, SIX, SIX), (EIGHT, EIGHT, SIX), (EIGHT, SIX, SIX)),
        ((ZERO, ZERO, ZERO), (ZERO, ZERO, ZERO), (ZERO, ZERO, ZERO)),
    ),
    (
        ((FOUR, EIGHT, FOUR), (FOUR, EIGHT, FOUR), (FOUR, FOUR, FOUR)),
        ((TWO, TWO, EIGHT), (TWO, TWO, TWO), (EIGHT, TWO, EIGHT)),
        ((FIVE, FIVE, EIGHT), (FIVE, EIGHT, EIGHT), (FIVE, FIVE, EIGHT)),
        ((ONE, EIGHT, ONE), (ONE, ONE, EIGHT), (ONE, EIGHT, ONE)),
    ),
    (
        ((NINE, EIGHT, EIGHT), (NINE, NINE, NINE), (EIGHT, EIGHT, NINE)),
        ((SIX, SIX, SIX), (SIX, EIGHT, SIX), (SIX, EIGHT, SIX)),
        ((EIGHT, FOUR, EIGHT), (FOUR, FOUR, FOUR), (EIGHT, FOUR, EIGHT)),
        ((TWO, TWO, TWO), (TWO, EIGHT, TWO), (TWO, TWO, TWO)),
    ),
)

LIBRARY_POSITIONS_D8E07EB2 = tuple(
    (ri, ci)
    for ri in interval(ZERO, FOUR, ONE)
    for ci in interval(ZERO, FOUR, ONE)
)

LIBRARY_LOOKUP_D8E07EB2 = {
    LIBRARY_TILES_D8E07EB2[ri][ci]: (ri, ci)
    for ri, ci in LIBRARY_POSITIONS_D8E07EB2
}


def rectangle_patch_d8e07eb2(
    top: Integer,
    left: Integer,
    height_: Integer,
    width_: Integer,
) -> Indices:
    x0 = interval(top, top + height_, ONE)
    x1 = interval(left, left + width_, ONE)
    x2 = product(x0, x1)
    return x2


HEADER_PATCH_D8E07EB2 = rectangle_patch_d8e07eb2(ZERO, ZERO, FIVE, 22)
FOOTER_PATCH_D8E07EB2 = rectangle_patch_d8e07eb2(28, ZERO, TWO, 22)
DIVIDER_TOP_PATCH_D8E07EB2 = rectangle_patch_d8e07eb2(FIVE, ZERO, ONE, 22)
DIVIDER_BOTTOM_PATCH_D8E07EB2 = rectangle_patch_d8e07eb2(27, ZERO, ONE, 22)
LIBRARY_PANEL_PATCHES_D8E07EB2 = {
    (ri, ci): rectangle_patch_d8e07eb2(SEVEN + FIVE * ri, ONE + FIVE * ci, FIVE, FIVE)
    for ri, ci in LIBRARY_POSITIONS_D8E07EB2
}


def stamp_tile_d8e07eb2(
    grid: Grid,
    tile: Grid,
    start: IntegerTuple,
) -> Grid:
    x0 = shift(asobject(tile), start)
    x1 = paint(grid, x0)
    return x1


def render_input_d8e07eb2(
    query_tiles: tuple[Grid | None, ...],
) -> Grid:
    x0 = canvas(EIGHT, (30, 22))
    x1 = fill(x0, SIX, DIVIDER_TOP_PATCH_D8E07EB2)
    x2 = fill(x1, SIX, DIVIDER_BOTTOM_PATCH_D8E07EB2)
    x3 = x2
    for x4 in interval(ZERO, FOUR, ONE):
        for x5 in interval(ZERO, FOUR, ONE):
            x6 = LIBRARY_TILES_D8E07EB2[x4][x5]
            x7 = LIBRARY_TILE_STARTS_D8E07EB2[x4][x5]
            x3 = stamp_tile_d8e07eb2(x3, x6, x7)
    for x4, x5 in zip(query_tiles, QUERY_TILE_STARTS_D8E07EB2):
        if x4 is None:
            continue
        x3 = stamp_tile_d8e07eb2(x3, x4, x5)
    return x3


def query_matches_d8e07eb2(
    grid: Grid,
) -> tuple[tuple[int, int], ...]:
    x0 = tuple()
    for x1 in QUERY_TILE_STARTS_D8E07EB2:
        x2 = crop(grid, x1, (THREE, THREE))
        x3 = all(x4 == EIGHT for x5 in x2 for x4 in x5)
        if x3:
            continue
        x4 = LIBRARY_LOOKUP_D8E07EB2[x2]
        if x4 not in x0:
            x0 = x0 + (x4,)
    return x0


def is_complete_line_d8e07eb2(
    positions: tuple[tuple[int, int], ...],
) -> Boolean:
    x0 = len(positions)
    if x0 != FOUR:
        return False
    x1 = {x2 for x2, _ in positions}
    x2 = {x3 for _, x3 in positions}
    x3 = len(x1) == ONE and len(x2) == FOUR
    x4 = len(x1) == FOUR and len(x2) == ONE
    return x3 or x4


def render_output_d8e07eb2(
    grid: Grid,
) -> Grid:
    x0 = query_matches_d8e07eb2(grid)
    x1 = grid
    for x2 in x0:
        x3 = LIBRARY_PANEL_PATCHES_D8E07EB2[x2]
        x1 = underfill(x1, THREE, x3)
    x4 = is_complete_line_d8e07eb2(x0)
    x5 = underfill(x1, branch(x4, THREE, TWO), FOOTER_PATCH_D8E07EB2)
    x6 = branch(x4, underfill(x5, THREE, HEADER_PATCH_D8E07EB2), x5)
    return x6
