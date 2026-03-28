from synth_rearc.core import *


def _motif_patch_1c0d0a4b(rows: tuple[tuple[int, int, int], ...]) -> Indices:
    return frozenset(
        (i, j)
        for i, row in enumerate(rows)
        for j, value in enumerate(row)
        if value != ZERO
    )


def _rot90_patch_1c0d0a4b(patch: Indices) -> Indices:
    return frozenset((j, TWO - i) for i, j in patch)


def _vmirror_patch_1c0d0a4b(patch: Indices) -> Indices:
    return frozenset((i, TWO - j) for i, j in patch)


def _motif_variants_1c0d0a4b(patch: Indices) -> tuple[Indices, ...]:
    variants = []
    current = patch
    for _ in range(FOUR):
        for variant in (current, _vmirror_patch_1c0d0a4b(current)):
            if variant not in variants:
                variants.append(variant)
        current = _rot90_patch_1c0d0a4b(current)
    return tuple(variants)


BASE_MOTIFS_1C0D0A4B = (
    _motif_patch_1c0d0a4b(((1, 0, 1), (0, 1, 0), (1, 0, 1))),
    _motif_patch_1c0d0a4b(((1, 0, 1), (1, 1, 1), (1, 0, 1))),
    _motif_patch_1c0d0a4b(((1, 0, 0), (1, 1, 0), (0, 1, 1))),
    _motif_patch_1c0d0a4b(((1, 1, 1), (1, 0, 1), (0, 1, 0))),
    _motif_patch_1c0d0a4b(((1, 1, 1), (0, 0, 0), (1, 1, 1))),
    _motif_patch_1c0d0a4b(((1, 1, 0), (0, 0, 1), (1, 1, 0))),
    _motif_patch_1c0d0a4b(((1, 0, 1), (1, 0, 1), (1, 1, 1))),
    _motif_patch_1c0d0a4b(((1, 0, 0), (0, 1, 0), (1, 1, 1))),
    _motif_patch_1c0d0a4b(((1, 1, 0), (0, 1, 0), (0, 1, 1))),
    _motif_patch_1c0d0a4b(((1, 1, 1), (0, 0, 0), (0, 1, 0))),
    _motif_patch_1c0d0a4b(((1, 0, 1), (0, 1, 1), (1, 0, 1))),
    _motif_patch_1c0d0a4b(((1, 1, 0), (0, 1, 1), (1, 0, 0))),
    _motif_patch_1c0d0a4b(((1, 0, 0), (1, 1, 1), (0, 1, 0))),
)

_motif_pool_1c0d0a4b = []
for x0 in BASE_MOTIFS_1C0D0A4B:
    for x1 in _motif_variants_1c0d0a4b(x0):
        if x1 not in _motif_pool_1c0d0a4b:
            _motif_pool_1c0d0a4b.append(x1)
MOTIFS_1C0D0A4B = tuple(_motif_pool_1c0d0a4b)

BLOCK_LAYOUTS_1C0D0A4B = (
    (ONE, THREE),
    (TWO, TWO),
    (TWO, THREE),
    (TWO, THREE),
    (THREE, THREE),
)
BLOCK_BOX_1C0D0A4B = asindices(canvas(ZERO, (THREE, THREE)))


def _frontier_rows_1c0d0a4b(grid: Grid) -> tuple[int, ...]:
    return tuple(i for i, row in enumerate(grid) if len(set(row)) == ONE and row[ZERO] == ZERO)


def _frontier_cols_1c0d0a4b(grid: Grid) -> tuple[int, ...]:
    h = len(grid)
    w = len(grid[ZERO])
    return tuple(
        j
        for j in range(w)
        if len({grid[i][j] for i in range(h)}) == ONE and grid[ZERO][j] == ZERO
    )


def generate_1c0d0a4b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        block_rows, block_cols = choice(BLOCK_LAYOUTS_1C0D0A4B)
        nblocks = block_rows * block_cols
        motifs = sample(MOTIFS_1C0D0A4B, nblocks)
        h = FOUR * block_rows + ONE
        w = FOUR * block_cols + ONE
        gi = canvas(ZERO, (h, w))
        go = canvas(ZERO, (h, w))
        for index, motif in enumerate(motifs):
            block_i = index // block_cols
            block_j = index % block_cols
            offset = (FOUR * block_i + ONE, FOUR * block_j + ONE)
            x0 = shift(motif, offset)
            x1 = shift(BLOCK_BOX_1C0D0A4B, offset)
            gi = fill(gi, EIGHT, x0)
            go = fill(go, TWO, x1)
            go = fill(go, ZERO, x0)
        if choice((T, F)):
            gi = hmirror(gi)
            go = hmirror(go)
        if choice((T, F)):
            gi = vmirror(gi)
            go = vmirror(go)
        x2 = tuple(range(ZERO, h, FOUR))
        x3 = tuple(range(ZERO, w, FOUR))
        if _frontier_rows_1c0d0a4b(gi) != x2:
            continue
        if _frontier_cols_1c0d0a4b(gi) != x3:
            continue
        return {"input": gi, "output": go}
