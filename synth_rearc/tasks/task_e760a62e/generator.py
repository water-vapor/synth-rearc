from synth_rearc.core import *


PATTERNS = ("pair_h", "pair_h", "pair_v", "pair_v", "elbow", "elbow", "staple")


def _segments_e760a62e(
    cell_size: int,
    full_blocks: int,
    remainder: int,
) -> tuple[tuple[tuple[int, int], ...], tuple[int, ...], int]:
    segments = tuple(
        (i * (cell_size + ONE), i * (cell_size + ONE) + cell_size - ONE)
        for i in range(full_blocks)
    )
    if remainder > ZERO:
        tail = full_blocks * (cell_size + ONE)
        segments = segments + ((tail, tail + remainder - ONE),)
        size = tail + remainder
    else:
        size = full_blocks * (cell_size + ONE)
    frontiers = tuple(i * (cell_size + ONE) + cell_size for i in range(full_blocks))
    return segments, frontiers, size


def _base_grid_e760a62e(
    size: int,
    frontiers: tuple[int, ...],
) -> Grid:
    grid = canvas(ZERO, (size, size))
    for idx in frontiers:
        grid = fill(grid, EIGHT, hfrontier((idx, ZERO)))
        grid = fill(grid, EIGHT, vfrontier((ZERO, idx)))
    return grid


def _center_offsets_e760a62e(
    cell_size: int,
) -> tuple[tuple[int, int], ...]:
    if even(cell_size):
        a = cell_size // TWO - ONE
        b = cell_size // TWO
        return ((a, a), (a, b), (b, a), (b, b))
    a = cell_size // TWO
    return ((a, a),)


def _seed_patch_e760a62e(
    loc: tuple[int, int],
    row_segments: tuple[tuple[int, int], ...],
    col_segments: tuple[tuple[int, int], ...],
    offset: tuple[int, int],
) -> Indices:
    i, j = loc
    di, dj = offset
    r0, _ = row_segments[i]
    c0, _ = col_segments[j]
    return frozenset({(r0 + di, c0 + dj)})


def _block_patch_e760a62e(
    loc: tuple[int, int],
    row_segments: tuple[tuple[int, int], ...],
    col_segments: tuple[tuple[int, int], ...],
) -> Indices:
    i, j = loc
    r0, r1 = row_segments[i]
    c0, c1 = col_segments[j]
    return frozenset((a, b) for a in range(r0, r1 + ONE) for b in range(c0, c1 + ONE))


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


def _pair_h_e760a62e(n: int) -> frozenset[tuple[int, int]]:
    row = randint(ZERO, n - ONE)
    c0 = randint(ZERO, n - THREE)
    c1 = randint(c0 + TWO, n - ONE)
    return frozenset({(row, c0), (row, c1)})


def _pair_v_e760a62e(n: int) -> frozenset[tuple[int, int]]:
    col = randint(ZERO, n - ONE)
    r0 = randint(ZERO, n - THREE)
    r1 = randint(r0 + TWO, n - ONE)
    return frozenset({(r0, col), (r1, col)})


def _elbow_e760a62e(n: int) -> frozenset[tuple[int, int]]:
    r0 = randint(ZERO, n - THREE)
    r1 = randint(r0 + TWO, n - ONE)
    c0 = randint(ZERO, n - THREE)
    c1 = randint(c0 + TWO, n - ONE)
    if choice((T, F)):
        return frozenset({(r0, c0), (r0, c1), (r1, c0)})
    return frozenset({(r0, c0), (r0, c1), (r1, c1)})


def _staple_e760a62e(n: int) -> frozenset[tuple[int, int]]:
    if choice((T, F)):
        c0 = randint(ZERO, n - THREE)
        c1 = randint(c0 + TWO, n - ONE)
        r2 = randint(TWO, n - ONE)
        r0 = randint(ZERO, r2 - TWO)
        r1 = randint(r0 + ONE, r2 - ONE)
        return frozenset({(r0, c0), (r2, c0), (r1, c1), (r2, c1)})
    r0 = randint(ZERO, n - THREE)
    r1 = randint(r0 + TWO, n - ONE)
    c2 = randint(TWO, n - ONE)
    c0 = randint(ZERO, c2 - TWO)
    c1 = randint(c0 + ONE, c2 - ONE)
    return frozenset({(r0, c0), (r0, c2), (r1, c1), (r1, c2)})


def _pattern_e760a62e(
    name: str,
    n: int,
) -> frozenset[tuple[int, int]]:
    if name == "pair_h":
        return _pair_h_e760a62e(n)
    if name == "pair_v":
        return _pair_v_e760a62e(n)
    if name == "elbow":
        return _elbow_e760a62e(n)
    return _staple_e760a62e(n)


def generate_e760a62e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        cell_size = unifint(diff_lb, diff_ub, (TWO, FIVE))
        max_full = min(EIGHT, 30 // (cell_size + ONE))
        max_total = min(EIGHT, 31 // (cell_size + ONE))
        if max_full < FIVE:
            continue

        if both(greater(cell_size, TWO), choice((T, F))):
            total_blocks = unifint(diff_lb, diff_ub, (FIVE, max_total))
            full_blocks = total_blocks - ONE
            if full_blocks < FOUR:
                continue
            remainder = randint(TWO, cell_size - ONE)
            size = full_blocks * (cell_size + ONE) + remainder
            if size > 30:
                continue
        else:
            full_blocks = unifint(diff_lb, diff_ub, (FIVE, max_full))
            remainder = ZERO

        row_segments, frontiers, size = _segments_e760a62e(cell_size, full_blocks, remainder)
        if size < 22 or size > 28 or not even(size):
            continue
        col_segments = row_segments
        offset = choice(_center_offsets_e760a62e(cell_size))
        want_overlap = choice((T, T, F))

        for _ in range(100):
            seed2 = _pattern_e760a62e(choice(PATTERNS), full_blocks)
            seed3 = _pattern_e760a62e(choice(PATTERNS), full_blocks)
            if seed2 & seed3:
                continue

            fill2 = _expand_blocks_e760a62e(seed2)
            fill3 = _expand_blocks_e760a62e(seed3)
            overlap = intersection(fill2, fill3)
            colored = combine(fill2, fill3)
            if want_overlap and len(overlap) == ZERO:
                continue
            if flip(want_overlap) and len(overlap) > FOUR:
                continue
            if len(colored) > (full_blocks * full_blocks * THREE) // FIVE:
                continue

            gi = _base_grid_e760a62e(size, frontiers)
            for loc in seed2:
                gi = fill(gi, TWO, _seed_patch_e760a62e(loc, row_segments, col_segments, offset))
            for loc in seed3:
                gi = fill(gi, THREE, _seed_patch_e760a62e(loc, row_segments, col_segments, offset))

            go = _base_grid_e760a62e(size, frontiers)
            go = _paint_blocks_e760a62e(go, TWO, difference(fill2, fill3), row_segments, col_segments)
            go = _paint_blocks_e760a62e(go, THREE, difference(fill3, fill2), row_segments, col_segments)
            go = _paint_blocks_e760a62e(go, SIX, overlap, row_segments, col_segments)
            return {"input": gi, "output": go}
