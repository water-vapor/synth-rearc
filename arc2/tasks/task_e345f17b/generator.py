from arc2.core import *


PANEL_SHAPE_E345F17B = (FOUR, FOUR)
PANEL_AREA_E345F17B = FOUR * FOUR


def _panel_e345f17b(
    color: Integer,
    holes: Indices,
) -> Grid:
    x0 = canvas(color, PANEL_SHAPE_E345F17B)
    x1 = fill(x0, ZERO, holes)
    return x1


def generate_e345f17b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = canvas(ZERO, PANEL_SHAPE_E345F17B)
    x1 = tuple(asindices(x0))
    while True:
        x2 = unifint(diff_lb, diff_ub, (TWO, SEVEN))
        x3 = frozenset(sample(x1, x2))
        x4 = tuple(difference(x1, x3))
        x5 = unifint(diff_lb, diff_ub, (ZERO, min(FIVE, len(x4))))
        x6 = frozenset(sample(x4, x5))
        x7 = tuple(difference(x4, x6))
        x8 = unifint(diff_lb, diff_ub, (ZERO, min(FIVE, len(x7))))
        x9 = frozenset(sample(x7, x8))
        x10 = combine(x3, x6)
        x11 = combine(x3, x9)
        x12 = subtract(PANEL_AREA_E345F17B, size(x10))
        x13 = subtract(PANEL_AREA_E345F17B, size(x11))
        x14 = both(greater(x12, FIVE), greater(x13, FIVE))
        x15 = add(TEN, THREE)
        x16 = both(greater(x15, x12), greater(x15, x13))
        x17 = greater(add(size(x6), size(x9)), ZERO)
        x18 = both(x14, x16)
        x19 = both(x17, x18)
        if not x19:
            continue
        x20 = _panel_e345f17b(SIX, x10)
        x21 = _panel_e345f17b(FIVE, x11)
        x22 = hconcat(x20, x21)
        x23 = fill(x0, FOUR, x3)
        return {"input": x22, "output": x23}
