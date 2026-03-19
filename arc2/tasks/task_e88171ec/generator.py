from arc2.core import *

from .helpers import largest_zero_rectangle_info_e88171ec, rectangle_patch_e88171ec
from .verifier import verify_e88171ec


def generate_e88171ec(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = remove(EIGHT, interval(ONE, TEN, ONE))
    while True:
        x1 = unifint(diff_lb, diff_ub, (12, 24))
        x2 = unifint(diff_lb, diff_ub, (12, 24))
        if max(x1, x2) > min(x1, x2) + max(THREE, min(x1, x2) // THREE):
            continue
        x3 = choice(x0)
        x4 = choice(remove(x3, x0))
        x5 = astuple(x1, x2)
        x6 = min(NINE, max(FOUR, x1 // TWO))
        x7 = min(NINE, max(FOUR, x2 // TWO))
        x8 = unifint(diff_lb, diff_ub, (FOUR, x6))
        x9 = unifint(diff_lb, diff_ub, (FOUR, x7))
        if x1 - x8 < THREE or x2 - x9 < THREE:
            continue
        x10 = randint(ONE, x1 - x8 - ONE)
        x11 = randint(ONE, x2 - x9 - ONE)
        x12 = astuple(x10, x11)
        x13 = astuple(x10 + x8 - ONE, x11 + x9 - ONE)
        x14 = rectangle_patch_e88171ec(x12, x13)
        x15 = canvas(x3, x5)
        x16 = fill(x15, ZERO, x14)
        x17 = difference(asindices(x16), x14)
        x18 = unifint(diff_lb, diff_ub, (22, 42))
        x19 = frozenset(x20 for x20 in x17 if randint(ZERO, 99) < x18)
        x21 = fill(x16, ZERO, x19)
        x22 = tuple(x23 for x23 in difference(x17, x19))
        x23 = unifint(diff_lb, diff_ub, (ZERO, min(len(x22), max(TWO, x1 * x2 // 18))))
        x24 = frozenset(sample(x22, x23)) if x23 > ZERO else frozenset()
        x25 = fill(x21, x4, x24)
        x26, x27, _, x28 = largest_zero_rectangle_info_e88171ec(x25)
        if x28 != ONE:
            continue
        if x26 != x12 or x27 != x13:
            continue
        x29 = verify_e88171ec(x25)
        if x25 == x29:
            continue
        return {"input": x25, "output": x29}
