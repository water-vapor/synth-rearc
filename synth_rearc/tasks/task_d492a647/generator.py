from synth_rearc.core import *

from .verifier import verify_d492a647


ACTIVE_COLORS_D492A647 = (ONE, TWO, THREE)
HEIGHT_BOUNDS_D492A647 = (12, 18)
WIDTH_BOUNDS_D492A647 = (13, 19)


def _rect_patch_d492a647(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    x0 = interval(top, top + height_value, ONE)
    x1 = interval(left, left + width_value, ONE)
    return product(x0, x1)


def _phase_patch_d492a647(
    gi: Grid,
    seed_loc: IntegerTuple,
) -> Indices:
    x0 = first(seed_loc)
    x1 = last(seed_loc)
    x2 = branch(even(x0), ZERO, ONE)
    x3 = branch(even(x1), ZERO, ONE)
    x4 = interval(x2, height(gi), TWO)
    x5 = interval(x3, width(gi), TWO)
    x6 = product(x4, x5)
    x7 = ofcolor(gi, ZERO)
    return intersection(x6, x7)


def generate_d492a647(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, HEIGHT_BOUNDS_D492A647)
        x1 = unifint(diff_lb, diff_ub, WIDTH_BOUNDS_D492A647)
        x2 = max(FIVE, x0 - FOUR)
        x3 = max(SIX, x1 - SIX)
        x4 = unifint(diff_lb, diff_ub, (x2, x0 - TWO))
        x5 = unifint(diff_lb, diff_ub, (x3, x1 - TWO))
        x6 = randint(ONE, x0 - x4 - ONE)
        x7 = randint(ONE, x1 - x5 - ONE)
        x8 = _rect_patch_d492a647(x6, x7, x4, x5)
        x9 = asindices(canvas(ZERO, (x0, x1)))
        x10 = difference(x9, x8)
        x11 = unifint(diff_lb, diff_ub, (25, 55))
        x12 = frozenset(x13 for x13 in x10 if randint(ZERO, 99) < x11)
        x14 = canvas(ZERO, (x0, x1))
        x15 = fill(x14, FIVE, x12)
        x16 = randint(x6 + ONE, x6 + x4 - TWO)
        x17 = randint(x7 + ONE, x7 + x5 - TWO)
        x18 = astuple(x16, x17)
        x19 = choice(ACTIVE_COLORS_D492A647)
        x20 = fill(x15, x19, frozenset({x18}))
        x21 = _phase_patch_d492a647(x20, x18)
        x22 = fill(x20, x19, x21)
        x23 = difference(x21, x8)
        if colorcount(x20, ZERO) <= colorcount(x20, FIVE):
            continue
        if size(x21) < max(SEVEN, (x4 * x5) // FOUR):
            continue
        if size(x23) < TWO:
            continue
        if verify_d492a647(x20) != x22:
            continue
        return {"input": x20, "output": x22}
