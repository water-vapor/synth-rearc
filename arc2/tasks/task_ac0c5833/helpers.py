from arc2.core import *


TOP_LEFT_AC0C5833 = "tl"
TOP_RIGHT_AC0C5833 = "tr"
BOTTOM_LEFT_AC0C5833 = "bl"
BOTTOM_RIGHT_AC0C5833 = "br"

CORNERS_AC0C5833 = (
    TOP_LEFT_AC0C5833,
    TOP_RIGHT_AC0C5833,
    BOTTOM_LEFT_AC0C5833,
    BOTTOM_RIGHT_AC0C5833,
)

CORNER_BY_MISSING_OFFSET_AC0C5833 = {
    (ZERO, ZERO): TOP_LEFT_AC0C5833,
    (ZERO, TWO): TOP_RIGHT_AC0C5833,
    (TWO, ZERO): BOTTOM_LEFT_AC0C5833,
    (TWO, TWO): BOTTOM_RIGHT_AC0C5833,
}

CANONICAL_MARKER_PATCH_AC0C5833 = frozenset({(ZERO, TWO), (TWO, ZERO), (TWO, TWO)})

MOTIF_POOL_AC0C5833 = (
    frozenset({(-TWO, -TWO), (-TWO, -ONE), (-ONE, -TWO), (-ONE, ZERO), (ZERO, -ONE), (ZERO, ZERO)}),
    frozenset({(-ONE, -ONE), (-ONE, ZERO), (ZERO, -ONE), (ZERO, ZERO)}),
    frozenset({
        (-TWO, -TWO),
        (-TWO, -ONE),
        (-TWO, ZERO),
        (-ONE, -TWO),
        (-ONE, ZERO),
        (ZERO, -TWO),
        (ZERO, -ONE),
        (ZERO, ZERO),
    }),
    frozenset({(-TWO, -TWO), (-TWO, ZERO), (-ONE, ZERO), (ZERO, -TWO), (ZERO, -ONE), (ZERO, ZERO)}),
    frozenset({(-TWO, -TWO), (-TWO, -ONE), (-ONE, -TWO), (ZERO, -TWO), (ZERO, -ONE), (ZERO, ZERO)}),
    frozenset({(-TWO, -TWO), (-TWO, ZERO), (-ONE, -ONE), (-ONE, ZERO), (ZERO, -TWO), (ZERO, ZERO)}),
)


def transform_canonical_patch_ac0c5833(
    patch: Indices,
    corner: str,
) -> Indices:
    out = set()
    for i, j in patch:
        ni = i if corner in (TOP_LEFT_AC0C5833, TOP_RIGHT_AC0C5833) else -i
        nj = j if corner in (TOP_LEFT_AC0C5833, BOTTOM_LEFT_AC0C5833) else -j
        out.add((ni, nj))
    return frozenset(out)


def marker_patch_ac0c5833(
    anchor: IntegerTuple,
    corner: str,
) -> Indices:
    x0 = transform_canonical_patch_ac0c5833(CANONICAL_MARKER_PATCH_AC0C5833, corner)
    x1 = shift(x0, anchor)
    return x1


def place_canonical_patch_ac0c5833(
    patch: Indices,
    anchor: IntegerTuple,
    corner: str,
) -> Indices:
    x0 = transform_canonical_patch_ac0c5833(patch, corner)
    x1 = shift(x0, anchor)
    return x1


def footprint_patch_ac0c5833(
    patch: Indices,
    anchor: IntegerTuple,
    corner: str,
) -> Indices:
    x0 = place_canonical_patch_ac0c5833(patch, anchor, corner)
    x1 = marker_patch_ac0c5833(anchor, corner)
    x2 = combine(x0, x1)
    return x2


def padded_bbox_ac0c5833(
    patch: Indices,
    dims: IntegerTuple,
    pad: int = 1,
) -> Indices:
    h, w = dims
    si = max(ZERO, uppermost(patch) - pad)
    sj = max(ZERO, leftmost(patch) - pad)
    ei = min(subtract(h, ONE), lowermost(patch) + pad)
    ej = min(subtract(w, ONE), rightmost(patch) + pad)
    return frozenset((i, j) for i in range(si, ei + ONE) for j in range(sj, ej + ONE))


def find_markers_ac0c5833(
    grid: Grid,
) -> tuple[tuple[IntegerTuple, str, Indices], ...]:
    x0 = ofcolor(grid, FOUR)
    x1, x2 = shape(grid)
    out = []
    for i in range(x1 - TWO):
        for j in range(x2 - TWO):
            x3 = ((i, j), (i, j + TWO), (i + TWO, j), (i + TWO, j + TWO))
            x4 = tuple(loc for loc in x3 if loc in x0)
            if len(x4) != THREE:
                continue
            x5 = next(loc for loc in x3 if loc not in x0)
            x6 = CORNER_BY_MISSING_OFFSET_AC0C5833[(x5[0] - i, x5[1] - j)]
            out.append((x5, x6, frozenset(x4)))
    return tuple(out)


def extract_seed_data_ac0c5833(
    grid: Grid,
) -> tuple[Indices, IntegerTuple, str, tuple[tuple[IntegerTuple, str, Indices], ...]]:
    x0 = ofcolor(grid, TWO)
    x1 = find_markers_ac0c5833(grid)
    x2 = []
    for x3, x4, _ in x1:
        x5 = frozenset((i - x3[0], j - x3[1]) for i, j in x0)
        if x4 in (BOTTOM_LEFT_AC0C5833, BOTTOM_RIGHT_AC0C5833):
            x5 = frozenset((-i, j) for i, j in x5)
        if x4 in (TOP_RIGHT_AC0C5833, BOTTOM_RIGHT_AC0C5833):
            x5 = frozenset((i, -j) for i, j in x5)
        x6 = valmax(x5, first)
        x7 = valmax(x5, last)
        if both(equality(x6, ZERO), equality(x7, ZERO)):
            x2.append((x5, x3, x4))
    if len(x2) != ONE:
        raise ValueError("expected exactly one seed marker")
    x8, x9, x10 = x2[ZERO]
    return x8, x9, x10, x1
