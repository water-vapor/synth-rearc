from synth_rearc.core import *
from itertools import combinations


def _normalize_mask_15113be4(
    cells: frozenset[IntegerTuple],
) -> frozenset[IntegerTuple]:
    mini = min(i for i, _ in cells)
    minj = min(j for _, j in cells)
    return frozenset((i - mini, j - minj) for i, j in cells)


def _transform_mask_15113be4(
    mask: frozenset[IntegerTuple],
    rot: Integer,
    flip: Boolean,
) -> frozenset[IntegerTuple]:
    cells = mask
    if flip:
        cells = frozenset((i, TWO - j) for i, j in cells)
    for _ in range(rot):
        cells = frozenset((j, TWO - i) for i, j in cells)
    return _normalize_mask_15113be4(cells)


def _mask_family_15113be4() -> tuple[frozenset[IntegerTuple], ...]:
    bases = (
        frozenset({(ZERO, TWO), (ONE, ZERO), (ONE, ONE), (TWO, ONE)}),
        frozenset({(ZERO, ZERO), (ZERO, TWO), (ONE, ONE)}),
        frozenset({(ZERO, ZERO), (ONE, ONE), (TWO, TWO)}),
    )
    family = set()
    for base in bases:
        for rot in range(FOUR):
            for flip in (False, True):
                family.add(_transform_mask_15113be4(base, rot, flip))
    return tuple(sorted(family, key=lambda shape: (len(shape), tuple(sorted(shape)))))


MASK_FAMILY_15113be4 = _mask_family_15113be4()


def _apply_mask_15113be4(
    grid: Grid,
    color: Integer,
    mask: frozenset[IntegerTuple],
) -> Grid:
    go = grid
    for i in interval(ZERO, 23, FOUR):
        for j in interval(ZERO, 23, FOUR):
            tile = crop(grid, (i, j), THREE_BY_THREE)
            ones = ofcolor(tile, ONE)
            if mask.issubset(ones):
                go = fill(go, color, shift(mask, (i, j)))
    return go


def _count_matches_15113be4(
    grid: Grid,
    mask: frozenset[IntegerTuple],
) -> Integer:
    total = ZERO
    for i in interval(ZERO, 23, FOUR):
        for j in interval(ZERO, 23, FOUR):
            tile = crop(grid, (i, j), THREE_BY_THREE)
            if mask.issubset(ofcolor(tile, ONE)):
                total += ONE
    return total


def _match_tiles_15113be4(
    grid: Grid,
    mask: frozenset[IntegerTuple],
) -> frozenset[IntegerTuple]:
    matches = set()
    for tile_i, i in enumerate(interval(ZERO, 23, FOUR)):
        for tile_j, j in enumerate(interval(ZERO, 23, FOUR)):
            tile = crop(grid, (i, j), THREE_BY_THREE)
            if mask.issubset(ofcolor(tile, ONE)):
                matches.add((tile_i, tile_j))
    return frozenset(matches)


def _has_edge_adjacency_15113be4(
    tiles: frozenset[IntegerTuple],
) -> Boolean:
    for ai, aj in tiles:
        for bi, bj in tiles:
            if (ai, aj) != (bi, bj) and abs(ai - bi) + abs(aj - bj) == ONE:
                return True
    return False


def _sample_mask_15113be4(
    diff_lb: float,
    diff_ub: float,
) -> frozenset[IntegerTuple]:
    target = unifint(diff_lb, diff_ub, (THREE, FOUR))
    options = tuple(mask for mask in MASK_FAMILY_15113be4 if len(mask) == target)
    return choice(options)


def _random_tile_15113be4(
    mask: frozenset[IntegerTuple],
    density: float,
    force_match: Boolean,
) -> list[list[Integer]]:
    tile = [
        [ONE if uniform(0.0, 1.0) < density else ZERO for _ in range(THREE)]
        for _ in range(THREE)
    ]
    if force_match:
        for i, j in mask:
            tile[i][j] = ONE
    return tile


def generate_15113be4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    colors = (THREE, SIX, SEVEN, EIGHT)
    panel_origins = ((ZERO, ZERO), (ZERO, FOUR), (FOUR, ZERO), (FOUR, FOUR))
    tile_origins = tuple(product(interval(ZERO, SIX, ONE), interval(ZERO, SIX, ONE)))
    while True:
        color = choice(colors)
        mask = _sample_mask_15113be4(diff_lb, diff_ub)
        density = unifint(diff_lb, diff_ub, (35, 60)) / 100
        block_i, block_j = choice(panel_origins)
        reserved = frozenset({
            (block_i, block_j),
            (block_i + ONE, block_j),
            (block_i, block_j + ONE),
            (block_i + ONE, block_j + ONE),
        })
        ordinary_tiles = tuple((i, j) for i, j in tile_origins if (i, j) not in reserved)
        n_targets = min(len(ordinary_tiles), unifint(diff_lb, diff_ub, (TWO, FOUR)))
        target_options = tuple(
            tiles for tiles in combinations(ordinary_tiles, n_targets)
            if not _has_edge_adjacency_15113be4(frozenset(tiles))
        )
        targets = frozenset(choice(target_options))
        gi = [[ZERO for _ in range(23)] for _ in range(23)]
        for idx in range(THREE, 23, FOUR):
            for jdx in range(23):
                gi[idx][jdx] = FOUR
                gi[jdx][idx] = FOUR
        for tile_i, tile_j in ordinary_tiles:
            tile = _random_tile_15113be4(mask, density, (tile_i, tile_j) in targets)
            base_i = tile_i * FOUR
            base_j = tile_j * FOUR
            for i in range(THREE):
                for j in range(THREE):
                    gi[base_i + i][base_j + j] = tile[i][j]
        frame_i = block_i * FOUR - ONE if block_i > ZERO else ZERO
        frame_j = block_j * FOUR - ONE if block_j > ZERO else ZERO
        for i in range(EIGHT):
            for j in range(EIGHT):
                gi[frame_i + i][frame_j + j] = FOUR if i in (ZERO, 7) or j in (ZERO, 7) else ZERO
        start_i = frame_i + ONE
        start_j = frame_j + ONE
        for i, j in mask:
            for di in range(TWO):
                for dj in range(TWO):
                    gi[start_i + i * TWO + di][start_j + j * TWO + dj] = color
        gi = format_grid(gi)
        match_tiles = _match_tiles_15113be4(gi, mask)
        match_count = len(match_tiles)
        if not TWO <= match_count <= FOUR:
            continue
        if _has_edge_adjacency_15113be4(match_tiles):
            continue
        go = _apply_mask_15113be4(gi, color, mask)
        if gi == go:
            continue
        return {"input": gi, "output": go}
