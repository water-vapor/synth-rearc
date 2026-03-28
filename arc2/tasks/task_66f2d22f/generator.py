from arc2.core import *


PANEL_SHAPE_66F2D22F = (FOUR, SEVEN)
PANEL_AREA_66F2D22F = FOUR * SEVEN
LEFT_COLOR_66F2D22F = THREE
RIGHT_COLOR_66F2D22F = TWO
OUTPUT_COLOR_66F2D22F = FIVE


def _panel_66f2d22f(
    color: Integer,
    holes: Indices,
) -> Grid:
    x0 = canvas(color, PANEL_SHAPE_66F2D22F)
    x1 = fill(x0, ZERO, holes)
    return x1


def _row_hole_counts_66f2d22f(
    holes: Indices,
) -> tuple[int, ...]:
    return tuple(sum(x0[ZERO] == x1 for x0 in holes) for x1 in interval(ZERO, FOUR, ONE))


def generate_66f2d22f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = canvas(ZERO, PANEL_SHAPE_66F2D22F)
    x1 = tuple(asindices(x0))
    while True:
        x2 = unifint(diff_lb, diff_ub, (11, 17))
        x3 = unifint(diff_lb, diff_ub, (11, 17))
        x4 = max(FIVE, add(add(x2, x3), -PANEL_AREA_66F2D22F))
        x5 = min(12, subtract(min(x2, x3), TWO))
        if x4 > x5:
            continue
        x6 = unifint(diff_lb, diff_ub, (x4, x5))
        x7 = frozenset(sample(x1, x6))
        x8 = tuple(difference(x1, x7))
        x9 = subtract(x2, x6)
        x10 = frozenset(sample(x8, x9))
        x11 = tuple(difference(x8, x10))
        x12 = subtract(x3, x6)
        x13 = frozenset(sample(x11, x12))
        x14 = combine(x7, x10)
        x15 = combine(x7, x13)
        x16 = _row_hole_counts_66f2d22f(x14)
        x17 = _row_hole_counts_66f2d22f(x15)
        if min(x16) < TWO or min(x17) < TWO:
            continue
        if max(x16) > SIX or max(x17) > SIX:
            continue
        x18 = _panel_66f2d22f(LEFT_COLOR_66F2D22F, x14)
        x19 = _panel_66f2d22f(RIGHT_COLOR_66F2D22F, x15)
        x20 = hconcat(x18, x19)
        x21 = fill(x0, OUTPUT_COLOR_66F2D22F, x7)
        return {"input": x20, "output": x21}
