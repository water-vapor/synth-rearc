from synth_rearc.core import *

from .helpers import (
    attached_rectangle_b25e450b,
    corridor_b25e450b,
    interval_is_clear_b25e450b,
    move_to_opposite_border_b25e450b,
)
from .verifier import verify_b25e450b


SIDES_B25E450B = ("top", "bottom", "left", "right")


def _background_b25e450b(
    diff_lb: float,
    diff_ub: float,
    grid_shape: IntegerTuple,
) -> Grid:
    x0 = canvas(SEVEN, grid_shape)
    x1 = totuple(asindices(x0))
    x2 = size(x1)
    x3 = max(ONE, x2 // FIVE)
    x4 = max(x3, x2 // TWO)
    x5 = unifint(diff_lb, diff_ub, (x3, x4))
    x6 = sample(x1, x5)
    return fill(x0, FIVE, x6)


def _candidate_rectangle_b25e450b(
    diff_lb: float,
    diff_ub: float,
    side: str,
    grid_shape: IntegerTuple,
) -> tuple[Object, tuple[int, int]] | None:
    h, w = grid_shape
    if side in ("top", "bottom"):
        x0 = min(SIX, w - TWO)
        x1 = min(SIX, h - TWO)
        if x0 < ONE or x1 < ONE:
            return None
        x2 = unifint(diff_lb, diff_ub, (ONE, x0))
        x3 = unifint(diff_lb, diff_ub, (ONE, x1))
        x4 = interval(ONE, w - x2, ONE)
        if size(x4) == ZERO:
            return None
        x5 = choice(x4)
        x6 = attached_rectangle_b25e450b(side, x5, x2, x3, grid_shape)
        return x6, (x5, x5 + x2 - ONE)
    x0 = min(SIX, h - TWO)
    x1 = min(SIX, w - TWO)
    if x0 < ONE or x1 < ONE:
        return None
    x2 = unifint(diff_lb, diff_ub, (ONE, x0))
    x3 = unifint(diff_lb, diff_ub, (ONE, x1))
    x4 = interval(ONE, h - x2, ONE)
    if size(x4) == ZERO:
        return None
    x5 = choice(x4)
    x6 = attached_rectangle_b25e450b(side, x5, x2, x3, grid_shape)
    return x6, (x5, x5 + x2 - ONE)


def generate_b25e450b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = multiply(TWO, unifint(diff_lb, diff_ub, (THREE, NINE)))
        w = multiply(TWO, unifint(diff_lb, diff_ub, (FOUR, SEVEN)))
        x0 = (h, w)
        x1 = _background_b25e450b(diff_lb, diff_ub, x0)
        x2 = min(EIGHT, max(ONE, (h * w) // 28))
        x3 = unifint(diff_lb, diff_ub, (ONE, x2))
        x4: list[Object] = []
        x5: list[Object] = []
        x6 = {x7: [] for x7 in SIDES_B25E450B}
        x7 = 0
        while len(x4) < x3 and x7 < 400:
            x7 += 1
            x8 = choice(SIDES_B25E450B)
            x9 = _candidate_rectangle_b25e450b(diff_lb, diff_ub, x8, x0)
            if x9 is None:
                continue
            x10, x11 = x9
            if not interval_is_clear_b25e450b(x11[0], x11[1] - x11[0] + ONE, x6[x8]):
                continue
            x12 = toindices(x10)
            if any(x12 & toindices(x13) or adjacent(x10, x13) for x13 in x4):
                continue
            x14 = move_to_opposite_border_b25e450b(x10, x0)
            x15 = toindices(x14)
            if any(x15 & toindices(x16) or adjacent(x14, x16) for x16 in x5):
                continue
            x4.append(x10)
            x5.append(x14)
            x6[x8].append(x11)
        if size(x4) == ZERO:
            continue
        x8 = sum(size(x9) for x9 in x4)
        if x8 < max(ONE, (h * w) // 12):
            continue
        x9 = paint(x1, merge(tuple(x4)))
        x10 = merge(tuple(corridor_b25e450b(x11, x12) for x11, x12 in zip(x4, x5)))
        x11 = fill(x9, SEVEN, x10)
        x12 = paint(x11, merge(tuple(x5)))
        if x9 == x12:
            continue
        if verify_b25e450b(x9) != x12:
            continue
        return {"input": x9, "output": x12}
