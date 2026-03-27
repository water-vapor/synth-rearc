from arc2.core import *

from .helpers import (
    border_cells_62ab2642,
    interior_degree_two_cells_62ab2642,
    l_path_62ab2642,
    leaf_count_62ab2642,
    segment_62ab2642,
    valid_tree_62ab2642,
    zero_regions_62ab2642,
)
from .verifier import verify_62ab2642


SHAPE_BUCKETS_62AB2642 = ("box", "box", "tall", "wide")
BRANCH_COUNTS_62AB2642 = (FIVE, FIVE, SIX, SIX, SIX)
FIVE_DENSITY_BOUNDS_62AB2642 = (0.30, 0.48)
FIVE_COUNT_BOUNDS_62AB2642 = (24, 45)


def _sample_dims_62ab2642(
    diff_lb: float,
    diff_ub: float,
) -> IntegerTuple:
    x0 = choice(SHAPE_BUCKETS_62AB2642)
    if x0 == "box":
        return (unifint(diff_lb, diff_ub, (EIGHT, 12)), unifint(diff_lb, diff_ub, (SEVEN, 12)))
    if x0 == "tall":
        return (unifint(diff_lb, diff_ub, (10, 15)), unifint(diff_lb, diff_ub, (FIVE, SEVEN)))
    return (unifint(diff_lb, diff_ub, (FIVE, SEVEN)), unifint(diff_lb, diff_ub, (10, 15)))


def _sample_trunk_62ab2642(
    dims: IntegerTuple,
) -> frozenset[tuple[int, int]]:
    x0, x1 = dims
    x2 = choice(("tb", "lr"))
    if x2 == "tb":
        x3 = choice(tuple(range(ONE, subtract(x1, ONE))))
        x4 = choice(tuple(range(ONE, subtract(x1, ONE))))
        x5 = choice(tuple(range(ONE, subtract(x0, ONE))))
        x6 = (ZERO, x3)
        x7 = (subtract(x0, ONE), x4)
        return segment_62ab2642(x6, (x5, x3)) | segment_62ab2642((x5, x3), (x5, x4)) | segment_62ab2642((x5, x4), x7)
    x3 = choice(tuple(range(ONE, subtract(x0, ONE))))
    x4 = choice(tuple(range(ONE, subtract(x0, ONE))))
    x5 = choice(tuple(range(ONE, subtract(x1, ONE))))
    x6 = (x3, ZERO)
    x7 = (x4, subtract(x1, ONE))
    return segment_62ab2642(x6, (x3, x5)) | segment_62ab2642((x3, x5), (x4, x5)) | segment_62ab2642((x4, x5), x7)


def _grow_tree_62ab2642(
    dims: IntegerTuple,
    target_branches: Integer,
) -> frozenset[tuple[int, int]] | None:
    x0 = _sample_trunk_62ab2642(dims)
    if not valid_tree_62ab2642(x0, dims):
        return None
    x1 = frozenset(border_cells_62ab2642(dims))
    x2 = x0
    for _ in range(target_branches):
        x3 = list(interior_degree_two_cells_62ab2642(x2, dims))
        shuffle(x3)
        x4 = list(x1)
        shuffle(x4)
        x5 = False
        for x6 in x3:
            for x7 in x4:
                if x7 in x2:
                    continue
                x8 = [ZERO, ONE]
                shuffle(x8)
                for x9 in x8:
                    x10 = l_path_62ab2642(x6, x7, x9)
                    if x10 is None or (x10 & x2) != {x6}:
                        continue
                    x11 = x2 | x10
                    if not valid_tree_62ab2642(x11, dims):
                        continue
                    x2 = x11
                    x5 = True
                    break
                if x5:
                    break
            if x5:
                break
        if not x5:
            return None
    return x2


def _render_output_62ab2642(
    gi: Grid,
) -> Grid:
    x0 = zero_regions_62ab2642(gi)
    x1 = x0[ZERO]
    x2 = x0[NEG_ONE]
    x3 = fill(gi, SEVEN, x1)
    x4 = fill(x3, EIGHT, x2)
    return x4


def generate_62ab2642(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _sample_dims_62ab2642(diff_lb, diff_ub)
        x1 = choice(BRANCH_COUNTS_62AB2642)
        x2 = _grow_tree_62ab2642(x0, x1)
        if x2 is None:
            continue
        x3 = len(x2)
        x4 = multiply(x0[ZERO], x0[ONE])
        x5 = x3 / x4
        if x3 < FIVE_COUNT_BOUNDS_62AB2642[ZERO] or x3 > FIVE_COUNT_BOUNDS_62AB2642[ONE]:
            continue
        if x5 < FIVE_DENSITY_BOUNDS_62AB2642[ZERO] or x5 > FIVE_DENSITY_BOUNDS_62AB2642[ONE]:
            continue
        x6 = fill(canvas(ZERO, x0), FIVE, x2)
        x7 = zero_regions_62ab2642(x6)
        x8 = tuple(len(x9) for x9 in x7)
        if len(x7) not in (SEVEN, EIGHT):
            continue
        if leaf_count_62ab2642(x2) != len(x7):
            continue
        if x8[ZERO] > FIVE or x8[NEG_ONE] < 10:
            continue
        if x8[ZERO] == x8[ONE] or x8[NEG_ONE] == x8[NEG_TWO]:
            continue
        x9 = _render_output_62ab2642(x6)
        if verify_62ab2642(x6) != x9:
            continue
        return {"input": x6, "output": x9}
