from arc2.core import *

from .helpers import (
    bbox_midpoint_e734a0e8,
    blank_tile_e734a0e8,
    compose_tiles_e734a0e8,
    make_motif_patch_e734a0e8,
)


def generate_e734a0e8(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = double(choice((ONE, TWO))) + ONE
        x1 = unifint(diff_lb, diff_ub, (THREE, FIVE))
        x2 = unifint(diff_lb, diff_ub, (THREE, FIVE))
        x3 = x1 * x2
        x4 = make_motif_patch_e734a0e8(diff_lb, diff_ub, x0)
        x5 = bbox_midpoint_e734a0e8(x4)
        x6 = blank_tile_e734a0e8(x0)
        x7 = choice(tuple(value for value in interval(ONE, TEN, ONE) if value != SEVEN))
        x8 = fill(x6, x7, x4)
        x9 = fill(x6, ZERO, frozenset({x5}))
        x10 = tuple((i, j) for i in range(x1) for j in range(x2))
        x11 = choice(x10)
        x12 = tuple(position for position in x10 if position != x11)
        x13 = unifint(diff_lb, diff_ub, (ONE, x3 - TWO))
        x14 = frozenset(sample(x12, x13))
        x15 = tuple(
            tuple(
                x8 if position == x11 else x9 if position in x14 else x6
                for position in tuple((i, j) for j in range(x2))
            )
            for i in range(x1)
        )
        x16 = tuple(
            tuple(
                x8 if position == x11 or position in x14 else x6
                for position in tuple((i, j) for j in range(x2))
            )
            for i in range(x1)
        )
        x17 = compose_tiles_e734a0e8(x15)
        x18 = compose_tiles_e734a0e8(x16)
        if x17 != x18:
            return {"input": x17, "output": x18}
