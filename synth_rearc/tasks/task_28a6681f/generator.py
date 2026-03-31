from synth_rearc.core import *

from .helpers import ordered_target_mask_28a6681f, target_prefix_28a6681f
from .verifier import verify_28a6681f


GRID_SIZE_28A6681F = TEN
BACKGROUND_28A6681F = ZERO
DONOR_COLOR_28A6681F = ONE
SCAFFOLD_COLORS_28A6681F = (TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)


def _u_patch_28a6681f(
    top: Integer,
    bottom: Integer,
    left: Integer,
    right: Integer,
    right_start: Integer,
) -> Indices:
    x0 = set()
    for x1 in range(top, bottom + ONE):
        x0.add((x1, left))
    for x1 in range(right_start, bottom + ONE):
        x0.add((x1, right))
    for x1 in range(left, right + ONE):
        x0.add((bottom, x1))
    return frozenset(x0)


def _hook_patch_28a6681f(
    top: Integer,
    bottom: Integer,
    left: Integer,
    right: Integer,
    spine_side: str,
    opposite_rows: tuple[Integer, ...],
) -> Indices:
    x0 = set((bottom, x1) for x1 in range(left, right + ONE))
    x1 = left if spine_side == "left" else right
    x2 = right if spine_side == "left" else left
    for x3 in range(top, bottom + ONE):
        x0.add((x3, x1))
    for x3 in opposite_rows:
        x0.add((x3, x2))
    return frozenset(x0)


def _diag_strip_28a6681f(
    top: Integer,
    anchor: Integer,
    length: Integer,
    mirrored: Boolean,
) -> Indices:
    x0 = set()
    for x1 in range(length):
        x2 = top + x1
        if mirrored:
            x3 = anchor - x1
        else:
            x3 = anchor + x1
        x0.add((x2, x3))
        x0.add((x2, x3 + ONE))
    return frozenset(x0)


def _bbox_cells_28a6681f(
    top: Integer,
    left: Integer,
    height_: Integer,
    width_: Integer,
    right_align: Boolean = False,
) -> tuple[IntegerTuple, ...]:
    x0 = []
    for x1 in range(height_):
        x2 = range(width_ - ONE, -ONE, -ONE) if right_align else range(width_)
        for x3 in x2:
            x0.append((top + x1, left + x3))
    return tuple(x0)


def _top_right_blob_28a6681f(
    count: Integer,
    top: Integer,
    left: Integer,
    height_: Integer,
    width_: Integer,
) -> Indices:
    x0 = _bbox_cells_28a6681f(top, left, height_, width_, right_align=T)
    return frozenset(x0[:count])


def _upper_gap_blob_28a6681f(
    cells: tuple[IntegerTuple, ...],
    count: Integer,
) -> Indices:
    x0 = sorted(cells, key=lambda x1: (x1[ZERO], x1[ONE]))
    return frozenset(x0[:count])


def _paint_objects_28a6681f(
    grid: Grid,
    pieces: tuple[tuple[Integer, Indices], ...],
) -> Grid:
    x0 = grid
    for x1, x2 in pieces:
        x0 = fill(x0, x1, x2)
    return x0


def _union_patches_28a6681f(
    *patches: Indices,
) -> Indices:
    x0 = set()
    for x1 in patches:
        x0 |= set(x1)
    return frozenset(x0)


def _family_single_right_28a6681f(
    diff_lb: float,
    diff_ub: float,
) -> dict | None:
    x0 = canvas(BACKGROUND_28A6681F, (GRID_SIZE_28A6681F, GRID_SIZE_28A6681F))
    x1 = unifint(diff_lb, diff_ub, (ONE, THREE))
    x2 = NINE
    x3 = unifint(diff_lb, diff_ub, (FOUR, SIX))
    x4 = unifint(diff_lb, diff_ub, (x3 + TWO, SEVEN))
    x5 = unifint(diff_lb, diff_ub, (x1 + TWO, x2 - ONE))
    x6 = _u_patch_28a6681f(x1, x2, x3, x4, x5)
    x7 = choice((T, F))
    if x7:
        x8 = max(ZERO, x3 - unifint(diff_lb, diff_ub, (THREE, FOUR)))
        x9 = max(x8 + ONE, x3 - ONE)
        x10 = _hook_patch_28a6681f(EIGHT, NINE, x8, x9, "right", ())
        if len(intersection(x6, x10)) > ZERO:
            return None
        x11 = (x6, x10)
    else:
        x11 = (x6,)
    x12 = _union_patches_28a6681f(*x11)
    x13 = ordered_target_mask_28a6681f(x12, GRID_SIZE_28A6681F, "right")
    x14 = size(x13)
    if x14 < SIX or x14 > 20:
        return None
    x15 = choice((ONE, TWO))
    x16 = x14 // x15
    if x14 % x15 != ZERO:
        x16 += ONE
    if x16 > GRID_SIZE_28A6681F:
        return None
    x17 = unifint(diff_lb, diff_ub, (ZERO, GRID_SIZE_28A6681F - x16))
    x18 = GRID_SIZE_28A6681F - x15
    x19 = _top_right_blob_28a6681f(x14, x17, x18, x16, x15)
    if len(intersection(x12, x19)) > ZERO:
        return None
    x20 = tuple(sample(SCAFFOLD_COLORS_28A6681F, len(x11)))
    x21 = tuple(pair(x20, x11))
    x22 = _paint_objects_28a6681f(x0, x21)
    x23 = fill(x22, DONOR_COLOR_28A6681F, x19)
    x24 = fill(x22, DONOR_COLOR_28A6681F, frozenset(x13))
    return {"input": x23, "output": x24}


def _family_dual_right_28a6681f(
    diff_lb: float,
    diff_ub: float,
) -> dict | None:
    x0 = canvas(BACKGROUND_28A6681F, (GRID_SIZE_28A6681F, GRID_SIZE_28A6681F))
    x1 = unifint(diff_lb, diff_ub, (ZERO, TWO))
    x2 = unifint(diff_lb, diff_ub, (ONE, TWO))
    x3 = unifint(diff_lb, diff_ub, (FOUR, FIVE))
    x4 = unifint(diff_lb, diff_ub, (x1 + FOUR, SEVEN))
    x5 = _u_patch_28a6681f(x1, NINE, x2, x3, x4)
    x6 = unifint(diff_lb, diff_ub, (FIVE, SIX))
    x7 = choice((SIX, SEVEN))
    x8 = NINE
    x9 = _u_patch_28a6681f(x6, NINE, x7, x8, x6)
    if len(intersection(x5, x9)) > ZERO:
        return None
    x10 = _union_patches_28a6681f(x5, x9)
    x11 = ordered_target_mask_28a6681f(x10, GRID_SIZE_28A6681F, "right")
    x12 = size(x11)
    if x12 < 12:
        return None
    x13 = unifint(diff_lb, diff_ub, (max(SIX, x12 // THREE), x12 - ONE))
    x14 = min(FOUR, x13 // THREE)
    x15 = randint(ZERO, x14)
    x16 = frozenset(x11[:x15])
    x17 = x13 - x15
    x18 = max(x1 + ONE, ONE)
    x19 = x6 - x18
    if x19 <= ZERO:
        return None
    x20 = FOUR
    x21 = x19 * x20
    if x17 > x21:
        return None
    x22 = _top_right_blob_28a6681f(x17, x18, SIX, x19, x20)
    if len(intersection(x10, x22)) > ZERO:
        return None
    x23 = combine(x16, x22)
    x24 = tuple(sample(SCAFFOLD_COLORS_28A6681F, TWO))
    x25 = _paint_objects_28a6681f(x0, ((x24[ZERO], x5), (x24[ONE], x9)))
    x26 = fill(x25, DONOR_COLOR_28A6681F, x23)
    x27 = fill(x25, DONOR_COLOR_28A6681F, frozenset(x11[:x13]))
    return {"input": x26, "output": x27}


def _family_gap_only_28a6681f(
    diff_lb: float,
    diff_ub: float,
) -> dict | None:
    x0 = canvas(BACKGROUND_28A6681F, (GRID_SIZE_28A6681F, GRID_SIZE_28A6681F))
    x1 = unifint(diff_lb, diff_ub, (ZERO, ONE))
    x2 = _hook_patch_28a6681f(SEVEN, NINE, x1, x1 + TWO, "left", (EIGHT,))
    x3 = _hook_patch_28a6681f(SIX, NINE, x1 + THREE, x1 + FIVE, "right", (SEVEN, EIGHT))
    if len(intersection(x2, x3)) > ZERO:
        return None
    x4 = choice((ONE, TWO))
    x5 = choice((ZERO, ONE))
    x6 = _diag_strip_28a6681f(x4, x5, FOUR, F)
    x7 = _diag_strip_28a6681f(x4, EIGHT, FOUR, T)
    if len(intersection(x6, x7)) > ZERO:
        return None
    x8 = _union_patches_28a6681f(x2, x3, x6, x7)
    x9 = ordered_target_mask_28a6681f(x8, GRID_SIZE_28A6681F, "none")
    x10 = ordered_target_mask_28a6681f(_union_patches_28a6681f(x2, x3), GRID_SIZE_28A6681F, "none")
    x11 = size(x10)
    x12 = unifint(diff_lb, diff_ub, (ONE, x11))
    x13 = set()
    for x14 in range(x4, x4 + FOUR):
        x15 = tuple(x16 for x16 in range(GRID_SIZE_28A6681F) if (x14, x16) not in x8)
        for x16 in x15:
            x13.add((x14, x16))
    x17 = tuple(sorted(x18 for x18 in x13 if x18[ZERO] < SIX))
    if len(x17) < x12:
        return None
    x19 = _upper_gap_blob_28a6681f(x17, x12)
    x20 = tuple(sample(SCAFFOLD_COLORS_28A6681F, THREE))
    x21 = _paint_objects_28a6681f(
        x0,
        ((x20[ZERO], x2), (x20[ONE], x3), (x20[TWO], _union_patches_28a6681f(x6, x7))),
    )
    x22 = fill(x21, DONOR_COLOR_28A6681F, x19)
    x23 = fill(x21, DONOR_COLOR_28A6681F, frozenset(x9[:x12]))
    return {"input": x22, "output": x23}


def generate_28a6681f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = (
        _family_single_right_28a6681f,
        _family_single_right_28a6681f,
        _family_dual_right_28a6681f,
        _family_gap_only_28a6681f,
    )
    while True:
        x1 = choice(x0)
        x2 = x1(diff_lb, diff_ub)
        if x2 is None:
            continue
        x3 = x2["input"]
        x4 = x2["output"]
        if x3 == x4:
            continue
        if verify_28a6681f(x3) != x4:
            continue
        return x2
