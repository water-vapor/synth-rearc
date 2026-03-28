from __future__ import annotations

from synth_rearc.core import *


Patch4E45F183 = frozenset[tuple[int, int]]


def _transpose_patch_4e45f183(patch: Patch4E45F183) -> Patch4E45F183:
    return frozenset((j, i) for i, j in patch)

GRID_SIZE_4E45F183 = 19
STEP_4E45F183 = SIX
TILE_SIZE_4E45F183 = FIVE
NONZERO_COLORS_4E45F183 = tuple(range(ONE, TEN))
BUCKETS_4E45F183 = tuple((i, j) for i in range(THREE) for j in range(THREE))
SEPARATORS_4E45F183 = frozenset(
    (i, j)
    for i in range(GRID_SIZE_4E45F183)
    for j in range(GRID_SIZE_4E45F183)
    if i % STEP_4E45F183 == ZERO or j % STEP_4E45F183 == ZERO
)

CORNER_PROTOTYPES_4E45F183 = (
    frozenset({(0, 0)}),
    frozenset({(0, 0), (1, 1)}),
    frozenset({(0, 0), (0, 1), (1, 0)}),
    frozenset({(0, 0), (1, 0), (1, 1)}),
    frozenset({(0, 0), (0, 1), (1, 0), (1, 1)}),
    frozenset({(0, 0), (0, 1), (0, 2), (1, 0)}),
)
EDGE_PROTOTYPES_4E45F183 = (
    frozenset({(0, 2), (1, 2)}),
    frozenset({(0, 1), (0, 2), (0, 3)}),
    frozenset({(0, 2), (1, 2), (2, 2)}),
    frozenset({(0, 1), (0, 2), (0, 3), (1, 2)}),
    frozenset({(0, 0), (0, 1), (0, 3), (0, 4), (1, 0), (1, 4)}),
    frozenset({(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)}),
)
CENTER_PROTOTYPES_4E45F183 = (
    frozenset({(2, 2)}),
    frozenset({(1, 2), (2, 1), (2, 2), (2, 3), (3, 2)}),
    frozenset({(1, 1), (1, 3), (2, 2), (3, 1), (3, 3)}),
    frozenset({(1, 2), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 2)}),
    frozenset({(0, 0), (0, 4), (1, 1), (1, 3), (3, 1), (3, 3), (4, 0), (4, 4)}),
    frozenset(
        {
            (0, 0),
            (0, 1),
            (0, 3),
            (0, 4),
            (1, 0),
            (1, 4),
            (3, 0),
            (3, 4),
            (4, 0),
            (4, 1),
            (4, 3),
            (4, 4),
        }
    ),
    frozenset(
        {
            (0, 2),
            (1, 2),
            (2, 0),
            (2, 1),
            (2, 2),
            (2, 3),
            (2, 4),
            (3, 2),
            (4, 2),
        }
    ),
)
SYMMETRIC_CORNER_PROTOTYPES_4E45F183 = tuple(
    x0 for x0 in CORNER_PROTOTYPES_4E45F183 if x0 == _transpose_patch_4e45f183(x0)
)
SYMMETRIC_CENTER_PROTOTYPES_4E45F183 = tuple(
    x0 for x0 in CENTER_PROTOTYPES_4E45F183 if x0 == _transpose_patch_4e45f183(x0)
)


def _vmirror_patch_4e45f183(patch: Patch4E45F183) -> Patch4E45F183:
    return frozenset((i, FOUR - j) for i, j in patch)


def _hmirror_patch_4e45f183(patch: Patch4E45F183) -> Patch4E45F183:
    return frozenset((FOUR - i, j) for i, j in patch)


def _rot90_patch_4e45f183(patch: Patch4E45F183) -> Patch4E45F183:
    return frozenset((j, FOUR - i) for i, j in patch)


def _rot180_patch_4e45f183(patch: Patch4E45F183) -> Patch4E45F183:
    return frozenset((FOUR - i, FOUR - j) for i, j in patch)


def _rot270_patch_4e45f183(patch: Patch4E45F183) -> Patch4E45F183:
    return frozenset((FOUR - j, i) for i, j in patch)


def _bucket_of_patch_4e45f183(patch: Patch4E45F183) -> tuple[int, int]:
    x0 = centerofmass(patch)
    x1 = ZERO if x0[0] < TWO else ONE if x0[0] == TWO else TWO
    x2 = ZERO if x0[1] < TWO else ONE if x0[1] == TWO else TWO
    return (x1, x2)


def _slot_origin_4e45f183(bucket: tuple[int, int]) -> tuple[int, int]:
    return (ONE + STEP_4E45F183 * bucket[0], ONE + STEP_4E45F183 * bucket[1])


def _blank_board_4e45f183(background: int) -> Grid:
    x0 = canvas(background, (GRID_SIZE_4E45F183, GRID_SIZE_4E45F183))
    return fill(x0, ZERO, SEPARATORS_4E45F183)


def _corner_patches_4e45f183() -> dict[tuple[int, int], Patch4E45F183]:
    x0 = {
        (0, 0): identity,
        (0, 2): _vmirror_patch_4e45f183,
        (2, 0): _hmirror_patch_4e45f183,
        (2, 2): _rot180_patch_4e45f183,
    }
    x1 = choice(SYMMETRIC_CORNER_PROTOTYPES_4E45F183)
    return {x2: x3(x1) for x2, x3 in x0.items()}


def _edge_patches_4e45f183() -> dict[tuple[int, int], Patch4E45F183]:
    x0 = {
        (0, 1): identity,
        (1, 2): _rot90_patch_4e45f183,
        (2, 1): _rot180_patch_4e45f183,
        (1, 0): _rot270_patch_4e45f183,
    }
    x1 = choice(EDGE_PROTOTYPES_4E45F183)
    return {x2: x3(x1) for x2, x3 in x0.items()}


def _board_cells_4e45f183(
    patches: dict[tuple[int, int], Patch4E45F183],
) -> frozenset[tuple[int, int]]:
    x0 = set()
    for x1, x2 in patches.items():
        x3 = _slot_origin_4e45f183(x1)
        for x4 in x2:
            x0.add(add(x3, x4))
    return frozenset(x0)


def _has_full_board_symmetry_4e45f183(
    patches: dict[tuple[int, int], Patch4E45F183],
) -> bool:
    x0 = _board_cells_4e45f183(patches)
    x1 = (
        frozenset((i, GRID_SIZE_4E45F183 - ONE - j) for i, j in x0),
        frozenset((GRID_SIZE_4E45F183 - ONE - i, j) for i, j in x0),
        frozenset((j, i) for i, j in x0),
        frozenset((GRID_SIZE_4E45F183 - ONE - j, GRID_SIZE_4E45F183 - ONE - i) for i, j in x0),
    )
    return all(x2 == x0 for x2 in x1)


def _canonical_patches_4e45f183() -> dict[tuple[int, int], Patch4E45F183]:
    x1 = _corner_patches_4e45f183()
    x2 = _edge_patches_4e45f183()
    x3 = choice(SYMMETRIC_CENTER_PROTOTYPES_4E45F183)
    x4 = {**x1, **x2, (1, 1): x3}
    for x5, x6 in x4.items():
        if _bucket_of_patch_4e45f183(x6) != x5:
            raise ValueError(f"invalid patch bucket {x5}: {x6}")
    if not _has_full_board_symmetry_4e45f183(x4):
        raise ValueError("canonical patches must form a board with full dihedral symmetry")
    return x4


def generate_4e45f183(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = diff_lb
    x1 = diff_ub
    x2, x3 = sample(NONZERO_COLORS_4E45F183, TWO)
    x4 = _canonical_patches_4e45f183()
    x5 = _blank_board_4e45f183(x2)
    for x6 in BUCKETS_4E45F183:
        x7 = _slot_origin_4e45f183(x6)
        x8 = shift(recolor(x3, x4[x6]), x7)
        x5 = paint(x5, x8)
    x9 = list(BUCKETS_4E45F183)
    while tuple(x9) == BUCKETS_4E45F183:
        shuffle(x9)
    x10 = _blank_board_4e45f183(x2)
    for x11, x12 in zip(BUCKETS_4E45F183, x9):
        x13 = _slot_origin_4e45f183(x12)
        x14 = shift(recolor(x3, x4[x11]), x13)
        x10 = paint(x10, x14)
    return {"input": x10, "output": x5}
