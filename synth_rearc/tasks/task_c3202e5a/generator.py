from synth_rearc.core import *


COLORS_C3202E5A = (ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)
LAYOUTS_C3202E5A = (
    (THREE, SIX),
    (FIVE, FOUR),
    (FIVE, FIVE),
)


def _tile_indices_c3202e5a(tile_span: Integer) -> tuple[IntegerTuple, ...]:
    x0 = canvas(ZERO, (tile_span, tile_span))
    x1 = asindices(x0)
    return tuple(sorted(x1))


def _scattered_patch_c3202e5a(
    tile_span: Integer,
    n_cells: Integer,
) -> frozenset[IntegerTuple]:
    x0 = _tile_indices_c3202e5a(tile_span)
    x1 = sample(x0, n_cells)
    return frozenset(x1)


def _multicolor_tile_c3202e5a(
    diff_lb: float,
    diff_ub: float,
    tile_span: Integer,
    colors: tuple[Integer, ...],
) -> Grid:
    x0 = canvas(ZERO, (tile_span, tile_span))
    x1 = _tile_indices_c3202e5a(tile_span)
    x2 = {value: set() for value in colors}
    x3 = sample(x1, len(colors))
    x4 = set()
    for value, loc in zip(colors, x3):
        x2[value].add(loc)
        x4.add(loc)
    x5 = THREE if tile_span == THREE else NINE
    x6 = unifint(diff_lb, diff_ub, (len(colors), x5))
    while len(x4) < x6:
        x7 = choice(colors)
        x8 = []
        for loc in x2[x7]:
            for nbr in dneighbors(loc):
                if 0 <= nbr[0] < tile_span and 0 <= nbr[1] < tile_span and nbr not in x4:
                    x8.append(nbr)
        if x8 and randint(ZERO, ONE) == ONE:
            x9 = choice(x8)
        else:
            x10 = tuple(loc for loc in x1 if loc not in x4)
            x9 = choice(x10)
        x2[x7].add(x9)
        x4.add(x9)
    x11 = x0
    for value in colors:
        x12 = frozenset(x2[value])
        x11 = fill(x11, value, x12)
    return x11


def _target_tile_c3202e5a(
    diff_lb: float,
    diff_ub: float,
    tile_span: Integer,
    value: Integer,
) -> Grid:
    x0 = FOUR if tile_span == THREE else SIX
    x1 = THREE if tile_span == THREE else FOUR
    x2 = unifint(diff_lb, diff_ub, (x1, x0))
    x3 = _scattered_patch_c3202e5a(tile_span, x2)
    x4 = canvas(ZERO, (tile_span, tile_span))
    x5 = fill(x4, value, x3)
    return x5


def _assemble_c3202e5a(
    tiles: tuple[tuple[Grid, ...], ...],
    separator_color: Integer,
) -> Grid:
    rows = []
    for row in tiles:
        joined = row[ZERO]
        for tile in row[ONE:]:
            joined = hconcat(joined, canvas(separator_color, (height(joined), ONE)))
            joined = hconcat(joined, tile)
        rows.append(joined)
    joined = rows[ZERO]
    for row in rows[ONE:]:
        joined = vconcat(joined, canvas(separator_color, (ONE, width(joined))))
        joined = vconcat(joined, row)
    return joined


def generate_c3202e5a(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        tile_span, ntiles = choice(LAYOUTS_C3202E5A)
        separator_color = choice(COLORS_C3202E5A)
        target_color = choice(tuple(value for value in COLORS_C3202E5A if value != separator_color))
        target_loc = (randint(ZERO, ntiles - ONE), randint(ZERO, ntiles - ONE))
        if tile_span == THREE:
            max_colors = THREE
        else:
            max_colors = SIX
        target_tile = _target_tile_c3202e5a(diff_lb, diff_ub, tile_span, target_color)
        tiles = []
        for i in range(ntiles):
            row = []
            for j in range(ntiles):
                if (i, j) == target_loc:
                    row.append(target_tile)
                    continue
                ncolors = unifint(diff_lb, diff_ub, (TWO, max_colors))
                colors = tuple(sample(COLORS_C3202E5A, ncolors))
                tile = _multicolor_tile_c3202e5a(diff_lb, diff_ub, tile_span, colors)
                row.append(tile)
            tiles.append(tuple(row))
        gi = _assemble_c3202e5a(tuple(tiles), separator_color)
        if mostcolor(gi) != ZERO:
            continue
        x0 = frontiers(gi)
        x1 = sfilter(x0, hline)
        x2 = sfilter(x0, vline)
        if size(x1) != ntiles - ONE:
            continue
        if size(x2) != ntiles - ONE:
            continue
        if numcolors(target_tile) != TWO:
            continue
        return {"input": gi, "output": target_tile}
