from synth_rearc.core import *

from .helpers import (
    corner_mark_15663ba9,
    exterior_background_15663ba9,
    sample_component_outline_15663ba9,
)
from .verifier import verify_15663ba9


ACTIVE_COLORS_15663BA9 = remove(FOUR, remove(TWO, interval(ONE, TEN, ONE)))
COMPONENT_COUNT_POOL_15663BA9 = (TWO, TWO, THREE)


def _marked_output_15663ba9(
    I: Grid,
    color_value: Integer,
) -> Grid:
    x0 = ofcolor(I, color_value)
    x1 = exterior_background_15663ba9(I)
    x2 = frozenset(
        x3 for x3 in x0 if equality(corner_mark_15663ba9(I, x3, color_value, x1), FOUR)
    )
    x3 = frozenset(
        x4 for x4 in x0 if equality(corner_mark_15663ba9(I, x4, color_value, x1), TWO)
    )
    x4 = fill(I, FOUR, x2)
    x5 = fill(x4, TWO, x3)
    return x5


def generate_15663ba9(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(COMPONENT_COUNT_POOL_15663BA9)
        x1 = unifint(diff_lb, diff_ub, (16, 22))
        x2 = unifint(diff_lb, diff_ub, (16, 22))
        x3 = choice(ACTIVE_COLORS_15663BA9)
        x4 = canvas(ZERO, (x1, x2))
        x5 = set()
        x6 = T
        x7 = T
        for _ in range(x0):
            x8 = F
            for _ in range(80):
                x9 = branch(x6, SEVEN, FOUR)
                x10 = min(10, x1 - THREE)
                x11 = min(10, x2 - THREE)
                if x10 < x9 or x11 < x9:
                    break
                x12 = randint(x9, x10)
                x13 = randint(x9, x11)
                x14, x15 = sample_component_outline_15663ba9(x12, x13, x6)
                x16 = randint(ONE, x1 - x12 - ONE)
                x17 = randint(ONE, x2 - x13 - ONE)
                x18 = frozenset(
                    (x19, x20)
                    for x19 in range(x16 - ONE, x16 + x12 + ONE)
                    for x20 in range(x17 - ONE, x17 + x13 + ONE)
                    if 0 <= x19 < x1 and 0 <= x20 < x2
                )
                if any(x19 in x5 for x19 in x18):
                    continue
                x20 = shift(x14, (x16, x17))
                x4 = fill(x4, x3, x20)
                x5 |= set(x18)
                x6 = both(x6, flip(x15))
                x8 = T
                break
            if not x8:
                x7 = F
                break
        if not x7 or x6:
            continue
        x17 = _marked_output_15663ba9(x4, x3)
        if colorcount(x17, TWO) == ZERO:
            continue
        if verify_15663ba9(x4) != x17:
            continue
        return {"input": x4, "output": x17}
