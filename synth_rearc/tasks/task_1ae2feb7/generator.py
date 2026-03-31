from synth_rearc.core import *

from .helpers import make_input_grid_1ae2feb7
from .helpers import projection_object_1ae2feb7
from .helpers import source_values_from_blocks_1ae2feb7
from .verifier import verify_1ae2feb7


COLORS_1ae2feb7 = (ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)


def _sample_side_width_1ae2feb7(
    diff_lb: float,
    diff_ub: float,
) -> Integer:
    if choice((ZERO, ZERO, ONE)) == ZERO:
        return unifint(diff_lb, diff_ub, (TWO, SIX))
    return unifint(diff_lb, diff_ub, (SEVEN, 12))


def _sample_active_rows_1ae2feb7(
    divider_top: Integer,
    divider_bottom: Integer,
    count: Integer,
) -> tuple[int, ...]:
    x0 = list(range(divider_top, increment(divider_bottom)))
    shuffle(x0)
    x1 = []
    for x2 in x0:
        if any(abs(x2 - x3) <= ONE for x3 in x1):
            continue
        x1.append(x2)
        if len(x1) == count:
            break
    return tuple(sorted(x1))


def _sample_blocks_1ae2feb7(
    diff_lb: float,
    diff_ub: float,
    side_width: Integer,
    sep_color: Integer,
) -> tuple[tuple[tuple[int, int], ...], int, int]:
    while True:
        x0 = choice((ONE, ONE, ONE, TWO if side_width > ONE else ONE))
        if x0 == ONE:
            x1 = unifint(diff_lb, diff_ub, (ONE, min(side_width, FIVE)))
            x2 = ((choice(COLORS_1ae2feb7), x1),)
        else:
            x1 = min(subtract(side_width, ONE), FOUR)
            x2 = unifint(diff_lb, diff_ub, (ONE, x1))
            x3 = min(subtract(side_width, x2), FOUR)
            if x3 < ONE:
                continue
            x4 = unifint(diff_lb, diff_ub, (ONE, x3))
            x5, x6 = sample(COLORS_1ae2feb7, TWO)
            x2 = ((x5, x2), (x6, x4))
        x7 = sum(x8 for _, x8 in x2)
        x9 = subtract(side_width, x7)
        x10 = randint(ZERO, x9)
        x11 = subtract(x9, x10)
        if x10 == ZERO and x2[ZERO][ZERO] == sep_color:
            continue
        return x2, x10, x11


def generate_1ae2feb7(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((True, True, False))
        x1 = _sample_side_width_1ae2feb7(diff_lb, diff_ub)
        x2 = unifint(diff_lb, diff_ub, (TWO, 14))
        x3 = unifint(diff_lb, diff_ub, (EIGHT, 14))
        x4 = choice((ZERO, ZERO, ZERO, ONE))
        x5 = subtract(decrement(x3), x4)
        x6 = increment(x5)
        x7 = min(FIVE, divide(add(x6, ONE), TWO))
        x8 = unifint(diff_lb, diff_ub, (TWO, x7))
        x9 = _sample_active_rows_1ae2feb7(ZERO, x5, x8)
        if len(x9) != x8:
            continue
        x10 = choice(COLORS_1ae2feb7)
        x11 = add(add(x1, x2), ONE)
        x12 = x1 if x0 else x2
        x13 = {}
        x14 = False
        x15 = set()
        for x16 in x9:
            x17, x18, x19 = _sample_blocks_1ae2feb7(diff_lb, diff_ub, x1, x10)
            x20 = source_values_from_blocks_1ae2feb7(x1, x17, x18, x19, x0)
            x13[x16] = x20
            x14 = x14 or len(x17) == TWO
            x15 |= {x21 for x21, _ in x17}
        if not x14 and choice((ZERO, ONE)) == ONE:
            continue
        if len(x15) == ONE:
            continue
        x21 = make_input_grid_1ae2feb7(x3, x11, x12, x10, ZERO, x5, x13, x0)
        x22 = projection_object_1ae2feb7(x21, x12)
        x23 = paint(x21, x22)
        if verify_1ae2feb7(x21) != x23:
            continue
        return {"input": x21, "output": x23}
