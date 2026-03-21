from arc2.core import *

from .helpers import (
    checkerboard_object_d282b262,
    has_ambiguous_order_d282b262,
    has_row_interaction_d282b262,
    pack_objects_right_d282b262,
    place_squares_d282b262,
)


SIDE_D282B262 = 15
COUNTS_D282B262 = (FOUR, FOUR, FIVE, FIVE)
BASE_SIZES_D282B262 = (TWO, TWO, TWO, THREE, THREE, THREE)


def _sample_sizes_d282b262(
    count: Integer,
) -> Tuple:
    x0 = [choice(BASE_SIZES_D282B262) for _ in range(count)]
    if choice((ZERO, ZERO, ZERO, ZERO, ZERO, ONE)) == ONE:
        x1 = choice(tuple(range(count)))
        x0[x1] = FIVE
    return tuple(x0)


def _build_grid_d282b262(
    objects_seq: Tuple,
) -> Grid:
    x0 = canvas(ZERO, (SIDE_D282B262, SIDE_D282B262))
    for x1 in objects_seq:
        x0 = paint(x0, x1)
    return x0


def generate_d282b262(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        x1 = choice(COUNTS_D282B262)
        x2 = _sample_sizes_d282b262(x1)
        x3 = unifint(diff_lb, diff_ub, (EIGHT, 12))
        x4 = place_squares_d282b262(x2, SIDE_D282B262, x3)
        if x4 is None:
            continue
        if not has_row_interaction_d282b262(x4, x2):
            continue
        if has_ambiguous_order_d282b262(x4, x2):
            continue
        x5 = []
        for x6, x7 in pair(x2, x4):
            x8 = tuple(sample(x0, TWO))
            x9 = checkerboard_object_d282b262(x6, x8, x7)
            x5.append(x9)
        x10 = tuple(x5)
        x11 = pack_objects_right_d282b262(x10, SIDE_D282B262)
        if x11 is None:
            continue
        x12 = tuple(leftmost(x14) - leftmost(x13) for x13, x14 in pair(x10, x11))
        if max(x12) < TWO:
            continue
        gi = _build_grid_d282b262(x10)
        go = _build_grid_d282b262(x11)
        if gi == go:
            continue
        return {"input": gi, "output": go}
