from synth_rearc.core import *

from .helpers import (
    BG_963C33F8,
    FG_963C33F8,
    HI_963C33F8,
    LO_963C33F8,
    MOTIF_PATTERNS_963C33F8,
    distractor_shapes_963c33f8,
    fits_963c33f8,
    paint_patch_963c33f8,
    reserve_columns_963c33f8,
    shift_patch_963c33f8,
    support_shapes_963c33f8,
)
from .verifier import verify_963c33f8


def _paint_motif_963c33f8(grid: Grid, left: int, pattern: tuple[int, int, int]) -> Grid:
    x0 = [list(row) for row in grid]
    for x1 in range(3):
        x0[ZERO][left + x1] = HI_963C33F8
        x0[ONE][left + x1] = HI_963C33F8
        x0[TWO][left + x1] = pattern[x1]
    return tuple(tuple(row) for row in x0)


def _try_paint_patch_963c33f8(
    grid: Grid,
    patch: Indices,
    occupied: Indices,
) -> tuple[Grid, Indices] | None:
    x0 = shape(grid)
    if not fits_963c33f8(patch, x0, occupied):
        return None
    x1 = paint_patch_963c33f8(grid, patch)
    x2 = occupied | patch
    return x1, x2


def _add_support_object_963c33f8(
    grid: Grid,
    occupied: Indices,
    row: int,
    col: int,
) -> tuple[Grid, Indices]:
    x0 = sorted(support_shapes_963c33f8(row, col), key=size, reverse=True)
    x1 = list(x0[:4]) + list(x0[4:])
    shuffle(x1)
    x0 = tuple(x1)
    for x1 in x0:
        x2 = _try_paint_patch_963c33f8(grid, x1, occupied)
        if x2 is not None:
            return x2
    x3 = frozenset({(row, col)})
    x4 = paint_patch_963c33f8(grid, x3)
    return x4, occupied | x3


def _scatter_distractors_963c33f8(
    grid: Grid,
    occupied: Indices,
    reserved_cols: tuple[int, int, int],
    count: int,
) -> tuple[Grid, Indices]:
    x0, x1 = shape(grid)
    x2 = grid
    x3 = occupied
    x4 = ZERO
    x5 = ZERO
    while x4 < count and x5 < 50:
        x5 += ONE
        x6 = randint(4, x0 - 2)
        x7 = randint(ZERO, x1 - 3)
        if any(col in reserved_cols for col in range(x7, x7 + 3)):
            continue
        x8 = sorted(distractor_shapes_963c33f8(x6, x7), key=size, reverse=True)
        x8 = list(x8[:6]) + list(x8[6:])
        shuffle(x8)
        for x9 in x8:
            x10 = _try_paint_patch_963c33f8(x2, x9, x3)
            if x10 is None:
                continue
            x2, x3 = x10
            x4 += ONE
            break
    return x2, x3


def _compose_output_963c33f8(
    gi: Grid,
    left: int,
    pattern: tuple[int, int, int],
    placements: tuple[tuple[int, int, tuple[int, int, int]], ...],
    cleanup: tuple[int, ...],
) -> Grid:
    x0 = [list(row) for row in gi]
    for x1 in range(3):
        for x2 in range(left, left + 3):
            x0[x1][x2] = BG_963C33F8
    for x3, x4, x5 in placements:
        for x6, x7 in enumerate(x5):
            x0[x4 + x6][x3] = x7
    if cleanup:
        x8 = len(x0) - ONE
        for x9 in cleanup:
            if x9 + ONE < len(x0[ZERO]) and x0[x8][x9 + ONE] == FG_963C33F8:
                x0[x8][x9 + ONE] = BG_963C33F8
            if x9 + TWO < len(x0[ZERO]) and x0[x8][x9 + TWO] == FG_963C33F8:
                x0[x8][x9 + TWO] = BG_963C33F8
    return tuple(tuple(row) for row in x0)


def _simple_family_963c33f8(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = choice((14, 16))
    x1 = canvas(BG_963C33F8, (x0, x0))
    x2 = choice(MOTIF_PATTERNS_963C33F8)
    x3 = unifint(diff_lb, diff_ub, (2, x0 - 5))
    x4 = reserve_columns_963c33f8(x3)
    x5 = frozenset((i, j) for i in range(3) for j in x4)
    x6 = x1
    x7 = x5
    x8 = []
    for x9, x10 in enumerate(x4):
        if x2[x9] != LO_963C33F8:
            x8.append((x10, x0 - 3, (HI_963C33F8, HI_963C33F8, HI_963C33F8)))
            continue
        x11 = randint(3, x0 - 6)
        x12 = x11 + 3
        x6, x7 = _add_support_object_963c33f8(x6, x7, x12, x10)
        x8.append((x10, x11, (HI_963C33F8, HI_963C33F8, LO_963C33F8)))
    x13 = unifint(diff_lb, diff_ub, (3, 7))
    x6, x7 = _scatter_distractors_963c33f8(x6, x7, x4, x13)
    x14 = _paint_motif_963c33f8(x6, x3, x2)
    x15 = _compose_output_963c33f8(x14, x3, x2, tuple(x8), ())
    return {"input": x14, "output": x15}


def _shifted_right_family_963c33f8(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = choice((14, 16))
    x1 = canvas(BG_963C33F8, (x0, x0))
    x2 = choice(((LO_963C33F8, LO_963C33F8, HI_963C33F8), (LO_963C33F8, HI_963C33F8, HI_963C33F8)))
    x3 = unifint(diff_lb, diff_ub, (2, x0 - 6))
    x4 = reserve_columns_963c33f8(x3)
    x5 = frozenset((i, j) for i in range(3) for j in x4)
    x6 = x1
    x7 = x5
    x8 = []
    for x9, x10 in enumerate(x4):
        if x2[x9] != LO_963C33F8:
            continue
        x11 = randint(3, x0 - 7)
        x12 = x11 + 3
        x6, x7 = _add_support_object_963c33f8(x6, x7, x12, x10)
        x8.append((x10, x11, (HI_963C33F8, HI_963C33F8, LO_963C33F8)))
    x13 = x4[TWO]
    x14 = shift_patch_963c33f8(frozenset({(x0 - 3, ZERO), (x0 - 2, ZERO), (x0 - 2, -1)}), (0, x13 + 1))
    x15 = frozenset((i, j) for i, j in x14 if 0 <= i < x0 and 0 <= j < x0)
    x16 = _try_paint_patch_963c33f8(x6, x15, x7)
    if x16 is not None:
        x6, x7 = x16
    x8.append((x13 + 1, x0 - 3, (HI_963C33F8, HI_963C33F8, HI_963C33F8)))
    x17 = unifint(diff_lb, diff_ub, (2, 6))
    x6, x7 = _scatter_distractors_963c33f8(x6, x7, x4, x17)
    x18 = _paint_motif_963c33f8(x6, x3, x2)
    x19 = _compose_output_963c33f8(x18, x3, x2, tuple(x8), ())
    return {"input": x18, "output": x19}


def _bar_cleanup_family_963c33f8(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = 14
    x1 = canvas(BG_963C33F8, (x0, x0))
    x2 = (HI_963C33F8, LO_963C33F8, HI_963C33F8)
    x3 = unifint(diff_lb, diff_ub, (2, x0 - 7))
    x4 = reserve_columns_963c33f8(x3)
    x5 = frozenset((i, j) for i in range(3) for j in x4)
    x6 = x1
    x7 = x5
    x8 = randint(5, 8)
    x9 = x8 + 3
    x6, x7 = _add_support_object_963c33f8(x6, x7, x9, x4[ONE])
    x10 = frozenset((x0 - ONE, j) for j in range(x4[TWO], x4[TWO] + 5))
    x11 = _try_paint_patch_963c33f8(x6, x10, x7)
    if x11 is not None:
        x6, x7 = x11
    x12 = (
        (x4[ZERO], x0 - 3, (HI_963C33F8, HI_963C33F8, HI_963C33F8)),
        (x4[ONE], x8, (HI_963C33F8, HI_963C33F8, LO_963C33F8)),
        (x4[TWO], x0 - 3, (HI_963C33F8, HI_963C33F8, HI_963C33F8)),
    )
    x13 = unifint(diff_lb, diff_ub, (2, 5))
    x6, x7 = _scatter_distractors_963c33f8(x6, x7, x4, x13)
    x14 = _paint_motif_963c33f8(x6, x3, x2)
    x15 = _compose_output_963c33f8(x14, x3, x2, x12, (x4[TWO],))
    return {"input": x14, "output": x15}


def generate_963c33f8(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = (
        _simple_family_963c33f8,
        _simple_family_963c33f8,
        _shifted_right_family_963c33f8,
        _bar_cleanup_family_963c33f8,
    )
    while True:
        x1 = choice(x0)(diff_lb, diff_ub)
        if x1["input"] == x1["output"]:
            continue
        if verify_963c33f8(x1["input"]) != x1["output"]:
            continue
        return x1
