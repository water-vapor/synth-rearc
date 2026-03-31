from __future__ import annotations

from synth_rearc.core import *

from .helpers import (
    horizontal_run_7b80bb43,
    patch_in_bounds_7b80bb43,
    reserve_with_margin_7b80bb43,
    staircase_col_7b80bb43,
    staircase_row_7b80bb43,
    vertical_run_7b80bb43,
)
from .verifier import verify_7b80bb43


def _horizontal_gadget_7b80bb43(
    dims: IntegerTuple,
) -> tuple[Indices, Indices, Indices] | None:
    x0, x1 = dims
    for _ in range(300):
        x2 = randint(TWO, min(EIGHT, x1 - SIX))
        x3 = randint(ONE, min(SIX, x1 - x2 - FOUR))
        x4 = randint(THREE, FIVE)
        x5 = x2 + x4 + x3
        if x5 >= x1:
            continue
        x6 = randint(ZERO, x1 - x5)
        x7 = randint(THREE, x0 - FIVE)
        x8 = x6
        x9 = x8 + x2
        x10 = x9 + x4
        x11 = horizontal_run_7b80bb43(x7, x8, x2)
        x12 = horizontal_run_7b80bb43(x7, x10, x3)
        x13 = staircase_row_7b80bb43(x7, x9 - ONE, x10, choice(("left", "right")))
        x14 = x11 | x12 | x13
        x15 = x11 | x12 | frozenset((x7, j) for j in range(x9, x10))
        if choice((T, F)):
            x16 = choice((x9 - ONE, x10))
            x17 = randint(TWO, max(TWO, min(SIX, x0 - x7 - ONE)))
            x18 = vertical_run_7b80bb43(x7 + ONE, x16, x17)
            x14 |= x18
            x15 |= x18
        if choice((T, F, F)):
            x16 = choice((x8, x9 - ONE, x10, x10 + x3 - ONE))
            x17 = randint(TWO, max(TWO, min(FIVE, x7)))
            x18 = vertical_run_7b80bb43(x7 - x17 + ONE, x16, x17)
            x14 |= x18
            x15 |= x18
        if not patch_in_bounds_7b80bb43(x14, dims):
            continue
        return x14, x15, reserve_with_margin_7b80bb43(x14 | x15, ONE)
    return None


def _vertical_gadget_7b80bb43(
    dims: IntegerTuple,
) -> tuple[Indices, Indices, Indices] | None:
    x0, x1 = dims
    for _ in range(300):
        x2 = randint(TWO, min(EIGHT, x0 - SIX))
        x3 = randint(TWO, min(EIGHT, x0 - x2 - FOUR))
        x4 = randint(THREE, FIVE)
        x5 = x2 + x4 + x3
        if x5 >= x0:
            continue
        x6 = randint(ZERO, x0 - x5)
        x7 = randint(TWO, x1 - THREE)
        x8 = x6
        x9 = x8 + x2
        x10 = x9 + x4
        x11 = vertical_run_7b80bb43(x8, x7, x2)
        x12 = vertical_run_7b80bb43(x10, x7, x3)
        x13 = staircase_col_7b80bb43(x9 - ONE, x10, x7, choice(("left", "right")), choice(("top", "bottom")))
        x14 = x11 | x12 | x13
        x15 = x11 | x12 | frozenset((i, x7) for i in range(x9, x10))
        if choice((T, F)):
            x16 = choice((x8, x9 - ONE, x10, x10 + x3 - ONE))
            x17 = randint(TWO, max(TWO, min(SIX, x1 - x7 - ONE)))
            x18 = horizontal_run_7b80bb43(x16, x7 + ONE, x17)
            x14 |= x18
            x15 |= x18
        if choice((T, F, F)):
            x16 = choice((x8, x9 - ONE, x10, x10 + x3 - ONE))
            x17 = randint(TWO, max(TWO, min(FIVE, x7)))
            x18 = horizontal_run_7b80bb43(x16, x7 - x17 + ONE, x17)
            x14 |= x18
            x15 |= x18
        if not patch_in_bounds_7b80bb43(x14, dims):
            continue
        return x14, x15, reserve_with_margin_7b80bb43(x14 | x15, ONE)
    return None


def _loose_stair_7b80bb43(
    dims: IntegerTuple,
) -> tuple[Indices, Indices, Indices] | None:
    x0, x1 = dims
    for _ in range(300):
        x2 = randint(TWO, FOUR)
        x3 = choice((ONE, NEG_ONE))
        x4 = randint(ONE, x0 - x2 - ONE)
        if x3 == ONE:
            x5 = randint(ONE, x1 - x2 - ONE)
        else:
            x5 = randint(x2, x1 - TWO)
        x6 = frozenset((x4 + k, x5 + x3 * k) for k in range(x2))
        if not patch_in_bounds_7b80bb43(x6, dims):
            continue
        return x6, frozenset({}), reserve_with_margin_7b80bb43(x6, TWO)
    return None


def _attached_stair_7b80bb43(
    dims: IntegerTuple,
) -> tuple[Indices, Indices, Indices] | None:
    x0, x1 = dims
    for _ in range(300):
        x2 = randint(FIVE, max(FIVE, x1 - TWO))
        x3 = randint(FOUR, x0 - FOUR)
        x4 = randint(ZERO, x1 - x2)
        x5 = horizontal_run_7b80bb43(x3, x4, x2)
        x6 = randint(TWO, min(THREE, x2 - TWO))
        x7 = randint(x4 + ONE, x4 + x2 - x6 - ONE)
        x8 = choice((ONE, NEG_ONE))
        if x8 == ONE:
            x9 = frozenset((x3 + ONE + k, x7 + k) for k in range(x6))
        else:
            x9 = frozenset((x3 + ONE + k, x7 - k) for k in range(x6))
        x10 = x5 | x9
        if not patch_in_bounds_7b80bb43(x10, dims):
            continue
        return x10, x5, reserve_with_margin_7b80bb43(x10, ONE)
    return None


def generate_7b80bb43(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = randint(16, 30)
        x1 = randint(16, 30)
        x2 = [x3 for x3 in range(TEN)]
        shuffle(x2)
        x3 = x2.pop()
        x4 = x2.pop()
        x5 = frozenset({})
        x6 = set()
        x7 = set()
        x8 = []

        x9 = randint(TWO, FOUR)
        x10 = randint(ONE, THREE)
        x11 = randint(ONE, THREE)
        for _ in range(x9):
            x12 = choice(("h", "v"))
            x13 = _horizontal_gadget_7b80bb43((x0, x1)) if x12 == "h" else _vertical_gadget_7b80bb43((x0, x1))
            if x13 is None:
                continue
            x14, x15, x16 = x13
            if len(intersection(x16, x5)) > ZERO:
                continue
            x6 |= set(x14)
            x7 |= set(x15)
            x5 |= x16
            x8.append(x12)

        for _ in range(x10):
            x12 = choice((_loose_stair_7b80bb43, _attached_stair_7b80bb43))
            x13 = x12((x0, x1))
            if x13 is None:
                continue
            x14, x15, x16 = x13
            if len(intersection(x16, x5)) > ZERO:
                continue
            x6 |= set(x14)
            x7 |= set(x15)
            x5 |= x16

        for _ in range(x11):
            if choice((T, F)):
                x12 = randint(TWO, x0 - THREE)
                x13 = randint(ONE, min(FOUR, x1 - ONE))
                x14 = randint(ZERO, x1 - x13)
                x15 = horizontal_run_7b80bb43(x12, x14, x13)
            else:
                x12 = randint(TWO, x1 - THREE)
                x13 = randint(ONE, min(FOUR, x0 - ONE))
                x14 = randint(ZERO, x0 - x13)
                x15 = vertical_run_7b80bb43(x14, x12, x13)
            x16 = reserve_with_margin_7b80bb43(x15, ONE)
            if len(intersection(x16, x5)) > ZERO:
                continue
            x6 |= set(x15)
            x7 |= set(x15)
            x5 |= x16

        if len(x8) == ZERO:
            continue
        x17 = canvas(x3, (x0, x1))
        x18 = fill(x17, x4, frozenset(x6))
        x19 = fill(x17, x4, frozenset(x7))
        if x18 == x19:
            continue
        if verify_7b80bb43(x18) != x19:
            continue
        return {"input": x18, "output": x19}
