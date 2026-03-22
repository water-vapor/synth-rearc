from arc2.core import *

from .helpers import spiral_mask_8b28cd80


def generate_8b28cd80(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = interval(ONE, TEN, ONE)
    while True:
        x1 = unifint(diff_lb, diff_ub, (THREE, EIGHT))
        x2 = choice(x0)
        x3 = randint(ZERO, decrement(x1))
        x4 = randint(ZERO, decrement(x1))
        x5 = canvas(ZERO, (x1, x1))
        x6 = fill(x5, x2, frozenset({(x3, x4)}))
        x7 = subtract(multiply(x1, FOUR), THREE)
        x8 = spiral_mask_8b28cd80((x7, x7))
        x9 = multiply(subtract(decrement(x1), x3), FOUR)
        x10 = multiply(subtract(decrement(x1), x4), FOUR)
        x11 = crop(x8, (x9, x10), (x7, x7))
        x12 = ofcolor(x11, ONE)
        x13 = canvas(ZERO, (x7, x7))
        x14 = fill(x13, x2, x12)
        return {"input": x6, "output": x14}
