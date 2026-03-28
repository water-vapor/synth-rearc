from arc2.core import *

from .verifier import verify_506d28a5


HALF_SHAPE_506D28A5 = (FOUR, FIVE)
DIVIDER_506D28A5 = canvas(FOUR, (ONE, FIVE))
HALF_CELLS_506D28A5 = tuple(product(interval(ZERO, FOUR, ONE), interval(ZERO, FIVE, ONE)))


def _span_506d28a5(
    patch,
):
    x0 = frozenset(x1 for x1, _ in patch)
    x2 = frozenset(x3 for _, x3 in patch)
    return (len(x0), len(x2))


def _rich_enough_506d28a5(
    patch,
    min_rows,
    min_cols,
):
    x0, x1 = _span_506d28a5(patch)
    return x0 >= min_rows and x1 >= min_cols


def _paint_half_506d28a5(
    color_value,
    patch,
):
    x0 = canvas(ZERO, HALF_SHAPE_506D28A5)
    x1 = fill(x0, color_value, patch)
    return x1


def generate_506d28a5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (TWO, SIX))
        x1 = unifint(diff_lb, diff_ub, (THREE, EIGHT))
        x2 = unifint(diff_lb, diff_ub, (THREE, EIGHT))
        x3 = x0 + x1 + x2
        if x3 < TEN or x3 > 18:
            continue
        x4 = x0 + x1
        x5 = x0 + x2
        if x4 < SIX or x4 > 14:
            continue
        if x5 < SIX or x5 > 14:
            continue
        x6 = frozenset(sample(HALF_CELLS_506D28A5, x0))
        x7 = tuple(x8 for x8 in HALF_CELLS_506D28A5 if x8 not in x6)
        x9 = frozenset(sample(x7, x1))
        x10 = tuple(x11 for x11 in x7 if x11 not in x9)
        x12 = frozenset(sample(x10, x2))
        x13 = combine(x6, x9)
        x14 = combine(x6, x12)
        x15 = combine(x13, x12)
        if not _rich_enough_506d28a5(x13, THREE, THREE):
            continue
        if not _rich_enough_506d28a5(x14, THREE, THREE):
            continue
        if not _rich_enough_506d28a5(x15, FOUR, FOUR):
            continue
        x16 = _paint_half_506d28a5(TWO, x13)
        x17 = _paint_half_506d28a5(ONE, x14)
        x18 = _paint_half_506d28a5(THREE, x15)
        x19 = vconcat(vconcat(x16, DIVIDER_506D28A5), x17)
        if verify_506d28a5(x19) != x18:
            continue
        return {"input": x19, "output": x18}
