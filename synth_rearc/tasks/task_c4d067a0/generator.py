from __future__ import annotations

from collections import Counter

from synth_rearc.core import *

from .helpers import block_patch_c4d067a0, paint_macro_c4d067a0, paint_source_c4d067a0


GRID_SIDES_C4D067A0 = (23, 23, 27, 27, 29)


def _sample_matrix_c4d067a0(
    diff_lb: float,
    diff_ub: float,
    bg: Integer,
) -> tuple[Grid, int, int]:
    x0 = tuple(value for value in range(TEN) if value != bg)
    while True:
        x1 = unifint(diff_lb, diff_ub, (THREE, FOUR))
        x2 = unifint(diff_lb, diff_ub, (TWO, THREE))
        x3 = unifint(diff_lb, diff_ub, (TWO, min(FOUR, len(x0))))
        x4 = sample(x0, x3)
        x5 = []
        for _ in range(x1):
            x6 = randint(ONE, x2)
            x7 = randint(ZERO, x2 - x6)
            x8 = [bg for _ in range(x2)]
            for x9 in range(x7, x7 + x6):
                x8[x9] = choice(x4)
            x5.append(x8)
        if any(all(x5[x10][x11] == bg for x10 in range(x1)) for x11 in range(x2)):
            continue
        x12 = sum(value != bg for row in x5 for value in row)
        if x12 <= TWO:
            continue
        if len({value for row in x5 for value in row if value != bg}) < TWO:
            continue
        x13 = []
        for x14, x15 in enumerate(x5):
            for x16 in range(x2 - ONE):
                x17 = (x15[x16], x15[x16 + ONE])
                if bg in x17:
                    continue
                x13.append((x17, x14, x16))
        if len(x13) == ZERO:
            continue
        x18 = Counter(x19 for x19, _, _ in x13)
        x20 = [(x21, x22, x23) for x21, x22, x23 in x13 if x18[x21] == ONE]
        if len(x20) == ZERO:
            continue
        x24, x25, x26 = choice(x20)
        return tuple(tuple(row) for row in x5), x25, x26


def _grid_side_c4d067a0(
    req: Integer,
) -> Integer:
    x0 = tuple(side for side in GRID_SIDES_C4D067A0 if side >= req)
    if len(x0) == ZERO:
        return min(30, req)
    return choice(x0)


def generate_c4d067a0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(range(TEN))
        x1, x2, x3 = _sample_matrix_c4d067a0(diff_lb, diff_ub, x0)
        x4 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x5 = tuple(value for value in {x4 + ONE, x4 + TWO, FIVE} if value > x4)
        x6 = choice(x5)
        x7 = len(x1)
        x8 = len(x1[ZERO])
        x9 = (x7 - ONE) * x6 + x4
        x10 = (x8 - ONE) * x6 + x4
        x11 = max(TWO * x7 + THREE, x9 + THREE, x10 + THREE)
        x12 = _grid_side_c4d067a0(x11)
        x13 = max(SEVEN, TWO * x8 + FOUR)
        if x12 - x10 - ONE < x13:
            continue
        x14 = randint(ONE, x12 - x9 - ONE)
        x15 = randint(x13, x12 - x10 - ONE)
        x16 = canvas(x0, (x12, x12))
        x17 = paint_source_c4d067a0(x16, x1, x0)
        x18 = x14 + x2 * x6
        x19 = x15 + x3 * x6
        x20 = block_patch_c4d067a0(x18, x19, x4)
        x21 = block_patch_c4d067a0(x18, x19 + x6, x4)
        x22 = fill(x17, x1[x2][x3], x20)
        x23 = fill(x22, x1[x2][x3 + ONE], x21)
        x24 = paint_macro_c4d067a0(x17, x1, x0, x14, x15, x6, x4)
        if x23 == x24:
            continue
        return {"input": x23, "output": x24}
