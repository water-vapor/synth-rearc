from synth_rearc.core import *

from .helpers import (
    CORNERS_AC0C5833,
    MOTIF_POOL_AC0C5833,
    extract_seed_data_ac0c5833,
    find_markers_ac0c5833,
    footprint_patch_ac0c5833,
    marker_patch_ac0c5833,
    padded_bbox_ac0c5833,
    place_canonical_patch_ac0c5833,
)


def _candidate_anchors_ac0c5833(
    patch: Indices,
    corner: str,
    dims: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    x0 = footprint_patch_ac0c5833(patch, ORIGIN, corner)
    x1 = -uppermost(x0)
    x2 = -leftmost(x0)
    x3 = subtract(dims[0], lowermost(x0))
    x4 = subtract(dims[1], rightmost(x0))
    return tuple((i, j) for i in range(x1, x3) for j in range(x2, x4))


def generate_ac0c5833(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (20, 30))
        x1 = (x0, x0)
        x2 = choice(MOTIF_POOL_AC0C5833)
        x3 = unifint(diff_lb, diff_ub, (4, 7))
        x4 = [choice(CORNERS_AC0C5833) for _ in range(x3)]
        shuffle(x4)
        x5 = []
        x6 = frozenset()
        for x7 in x4:
            x8 = list(_candidate_anchors_ac0c5833(x2, x7, x1))
            shuffle(x8)
            x9 = F
            for x10 in x8:
                x11 = footprint_patch_ac0c5833(x2, x10, x7)
                if len(intersection(x11, x6)) != ZERO:
                    continue
                x5.append((x10, x7))
                x6 = combine(x6, padded_bbox_ac0c5833(x11, x1))
                x9 = T
                break
            if flip(x9):
                x5 = None
                break
        if equality(x5, None):
            continue
        x12 = randint(ZERO, subtract(len(x5), ONE))
        x13 = canvas(ZERO, x1)
        x14 = x13
        for x15, x16 in x5:
            x17 = marker_patch_ac0c5833(x15, x16)
            x13 = fill(x13, FOUR, x17)
            x14 = fill(x14, FOUR, x17)
        x18, x19 = x5[x12]
        x20 = place_canonical_patch_ac0c5833(x2, x18, x19)
        x13 = fill(x13, TWO, x20)
        for x21, x22 in x5:
            x23 = place_canonical_patch_ac0c5833(x2, x21, x22)
            x14 = fill(x14, TWO, x23)
        x24 = find_markers_ac0c5833(x13)
        x25 = extract_seed_data_ac0c5833(x13)
        if len(x24) != x3:
            continue
        if x25[ONE] != x18 or x25[TWO] != x19:
            continue
        if equality(x13, x14):
            continue
        return {"input": x13, "output": x14}
