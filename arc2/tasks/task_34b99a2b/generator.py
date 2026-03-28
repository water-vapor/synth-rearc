from arc2.core import *

from .verifier import verify_34b99a2b


PANEL_SHAPE_34B99A2B = (FIVE, FOUR)
SEPARATOR_SHAPE_34B99A2B = (FIVE, ONE)
PANEL_CELLS_34B99A2B = tuple(product(interval(ZERO, FIVE, ONE), interval(ZERO, FOUR, ONE)))
OVERLAP_RANGE_34B99A2B = (THREE, SEVEN)
SIDE_ONLY_RANGE_34B99A2B = (FOUR, EIGHT)
MAX_ACTIVE_CELLS_34B99A2B = 17


def generate_34b99a2b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = canvas(ZERO, PANEL_SHAPE_34B99A2B)
    x1 = canvas(FOUR, SEPARATOR_SHAPE_34B99A2B)
    while True:
        x2 = unifint(diff_lb, diff_ub, OVERLAP_RANGE_34B99A2B)
        x3 = unifint(diff_lb, diff_ub, SIDE_ONLY_RANGE_34B99A2B)
        x4 = unifint(diff_lb, diff_ub, SIDE_ONLY_RANGE_34B99A2B)
        x5 = add(add(x2, x3), x4)
        if greater(x5, MAX_ACTIVE_CELLS_34B99A2B):
            continue
        x6 = tuple(sample(PANEL_CELLS_34B99A2B, x5))
        x7 = add(x2, x3)
        x8 = frozenset(x6[:x2])
        x9 = frozenset(x6[x2:x7])
        x10 = frozenset(x6[x7:])
        x11 = combine(x8, x9)
        x12 = combine(x8, x10)
        x13 = fill(x0, EIGHT, x11)
        x14 = fill(x0, FIVE, x12)
        x15 = hconcat(hconcat(x13, x1), x14)
        x16 = combine(x9, x10)
        x17 = fill(x0, TWO, x16)
        if verify_34b99a2b(x15) != x17:
            continue
        return {"input": x15, "output": x17}
