from synth_rearc.core import *

from .helpers import GRID_SIZE_4AAB4007, full_cycle_visible_4aab4007, render_output_4aab4007


DENSE_PERIODS_4AAB4007 = (SEVEN, NINE)
ODD_PERIODS_4AAB4007 = (FOUR, FIVE)


def _rotate_cycle_4aab4007(
    values: tuple[int, ...],
    offset: Integer,
) -> tuple[int, ...]:
    return values[offset:] + values[:offset]


def _sample_cycle_4aab4007(
    diff_lb: float,
    diff_ub: float,
) -> tuple[int, ...]:
    x0 = unifint(diff_lb, diff_ub, (ZERO, THREE))
    x1 = DENSE_PERIODS_4AAB4007 if x0 >= TWO else ODD_PERIODS_4AAB4007
    x2 = choice(x1)
    if x2 in ODD_PERIODS_4AAB4007:
        x3 = tuple(range(ONE, add(add(x2, x2), NEG_ONE), TWO))
    else:
        x3 = tuple(range(ONE, increment(x2)))
        x4 = tuple(x3[::TWO]) + tuple(x3[ONE::TWO])
        x3 = x4
    x5 = randint(ZERO, subtract(len(x3), ONE))
    return _rotate_cycle_4aab4007(x3, x5)


def _rect_patch_4aab4007(
    top: Integer,
    left: Integer,
    height: Integer,
    width: Integer,
):
    x0 = interval(top, min(add(top, height), GRID_SIZE_4AAB4007), ONE)
    x1 = interval(left, min(add(left, width), GRID_SIZE_4AAB4007), ONE)
    return product(x0, x1)


def _sample_mask_4aab4007(
    diff_lb: float,
    diff_ub: float,
):
    x0 = frozenset()
    x1 = unifint(diff_lb, diff_ub, (FOUR, EIGHT))
    x2 = unifint(diff_lb, diff_ub, (SIX, TEN))
    x0 = combine(x0, _rect_patch_4aab4007(randint(ONE, FOUR), randint(EIGHT, 12), x1, x2))
    if choice((T, F)):
        x3 = unifint(diff_lb, diff_ub, (FIVE, TEN))
        x4 = unifint(diff_lb, diff_ub, (FOUR, EIGHT))
        x0 = combine(x0, _rect_patch_4aab4007(randint(SIX, 12), randint(ZERO, THREE), x3, x4))
    if choice((T, F)):
        x5 = unifint(diff_lb, diff_ub, (THREE, SEVEN))
        x6 = unifint(diff_lb, diff_ub, (SIX, TEN))
        x0 = combine(x0, _rect_patch_4aab4007(randint(13, 18), randint(SEVEN, 12), x5, x6))
    x7 = unifint(diff_lb, diff_ub, (ZERO, TWO))
    for _ in range(x7):
        x8 = unifint(diff_lb, diff_ub, (THREE, SEVEN))
        x9 = unifint(diff_lb, diff_ub, (THREE, EIGHT))
        x10 = randint(ONE, subtract(GRID_SIZE_4AAB4007, x8))
        x11 = randint(ONE, subtract(GRID_SIZE_4AAB4007, x9))
        x0 = combine(x0, _rect_patch_4aab4007(x10, x11, x8, x9))
    return x0


def generate_4aab4007(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _sample_cycle_4aab4007(diff_lb, diff_ub)
        x1 = render_output_4aab4007(x0)
        x2 = _sample_mask_4aab4007(diff_lb, diff_ub)
        x3 = fill(x1, ZERO, x2)
        x4 = colorcount(x3, ZERO)
        if x3 == x1:
            continue
        if not full_cycle_visible_4aab4007(x3, len(x0)):
            continue
        if x4 < 60 or x4 > 170:
            continue
        return {"input": x3, "output": x1}
