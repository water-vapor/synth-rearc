from synth_rearc.core import *


def _segments_e760a62e(
    grid: Grid,
) -> tuple[tuple[tuple[int, int], ...], tuple[tuple[int, int], ...]]:
    h, w = shape(grid)
    row_frontiers = tuple(i for i, row in enumerate(grid) if all(v == EIGHT for v in row))
    col_frontiers = tuple(j for j in range(w) if all(grid[i][j] == EIGHT for i in range(h)))

    row_segments = []
    start = ZERO
    for stop in row_frontiers:
        if start < stop:
            row_segments.append((start, stop - ONE))
        start = stop + ONE
    if start < h:
        row_segments.append((start, h - ONE))

    col_segments = []
    start = ZERO
    for stop in col_frontiers:
        if start < stop:
            col_segments.append((start, stop - ONE))
        start = stop + ONE
    if start < w:
        col_segments.append((start, w - ONE))

    return tuple(row_segments), tuple(col_segments)


def _seed_blocks_e760a62e(
    grid: Grid,
    value: int,
    row_segments: tuple[tuple[int, int], ...],
    col_segments: tuple[tuple[int, int], ...],
) -> frozenset[tuple[int, int]]:
    out = set()
    for i, (r0, r1) in enumerate(row_segments):
        for j, (c0, c1) in enumerate(col_segments):
            patch = crop(grid, (r0, c0), (r1 - r0 + ONE, c1 - c0 + ONE))
            if contained(value, palette(patch)):
                out.add((i, j))
    return frozenset(out)


def _expand_blocks_e760a62e(
    seed_blocks: frozenset[tuple[int, int]],
) -> frozenset[tuple[int, int]]:
    out = set(seed_blocks)
    rows = {}
    cols = {}
    for i, j in seed_blocks:
        rows.setdefault(i, []).append(j)
        cols.setdefault(j, []).append(i)
    for i, js in rows.items():
        if len(js) > ONE:
            out.update((i, j) for j in range(min(js), max(js) + ONE))
    for j, iset in cols.items():
        if len(iset) > ONE:
            out.update((i, j) for i in range(min(iset), max(iset) + ONE))
    return frozenset(out)


def _block_patch_e760a62e(
    loc: tuple[int, int],
    row_segments: tuple[tuple[int, int], ...],
    col_segments: tuple[tuple[int, int], ...],
) -> Indices:
    i, j = loc
    r0, r1 = row_segments[i]
    c0, c1 = col_segments[j]
    return frozenset((a, b) for a in range(r0, r1 + ONE) for b in range(c0, c1 + ONE))


def _paint_blocks_e760a62e(
    grid: Grid,
    value: int,
    blocks: frozenset[tuple[int, int]],
    row_segments: tuple[tuple[int, int], ...],
    col_segments: tuple[tuple[int, int], ...],
) -> Grid:
    out = grid
    for loc in blocks:
        out = fill(out, value, _block_patch_e760a62e(loc, row_segments, col_segments))
    return out


def verify_e760a62e(I: Grid) -> Grid:
    x0 = replace(I, TWO, ZERO)
    x1 = replace(x0, THREE, ZERO)
    x2 = _segments_e760a62e(I)
    x3, x4 = x2
    x5 = _seed_blocks_e760a62e(I, TWO, x3, x4)
    x6 = _seed_blocks_e760a62e(I, THREE, x3, x4)
    x7 = _expand_blocks_e760a62e(x5)
    x8 = _expand_blocks_e760a62e(x6)
    x9 = difference(x7, x8)
    x10 = difference(x8, x7)
    x11 = intersection(x7, x8)
    x12 = _paint_blocks_e760a62e(x1, TWO, x9, x3, x4)
    x13 = _paint_blocks_e760a62e(x12, THREE, x10, x3, x4)
    x14 = _paint_blocks_e760a62e(x13, SIX, x11, x3, x4)
    return x14
