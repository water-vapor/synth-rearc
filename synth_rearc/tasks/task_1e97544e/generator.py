from __future__ import annotations

from synth_rearc.core import *

from .helpers import GRID_SHAPE_1E97544E, build_output_1e97544e, rect_indices_1e97544e
from .verifier import verify_1e97544e


def _sample_cluster_1e97544e(
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = dims
    x2 = choice((TWO, THREE, THREE, FOUR, FOUR, FIVE))
    x3 = choice((TWO, THREE, THREE, FOUR, FOUR, FIVE))
    x4 = randint(ZERO, x0 - x2)
    x5 = randint(ZERO, x1 - x3)
    x6 = rect_indices_1e97544e((x4, x5), (x2, x3))
    x7 = choice((ZERO, ONE, ONE))
    for _ in range(x7):
        for _ in range(50):
            x8 = choice((TWO, THREE, THREE, FOUR, FOUR, FIVE))
            x9 = choice((TWO, THREE, THREE, FOUR, FOUR, FIVE))
            x10 = min(max(x4 + randint(-TWO, TWO), ZERO), x0 - x8)
            x11 = min(max(x5 + randint(-TWO, TWO), ZERO), x1 - x9)
            x12 = rect_indices_1e97544e((x10, x11), (x8, x9))
            if manhattan(x6, x12) > ONE and len(intersection(x6, x12)) == ZERO:
                continue
            x6 = combine(x6, x12)
            break
    return x6


def _zero_components_1e97544e(
    mask: Indices,
    dims: IntegerTuple,
) -> Objects:
    x0 = fill(canvas(ONE, dims), ZERO, mask)
    x1 = objects(x0, T, F, T)
    x2 = colorfilter(x1, ZERO)
    return x2


def generate_1e97544e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = GRID_SHAPE_1E97544E
    x1 = x0[0]
    while True:
        x2 = choice((SIX, SEVEN, EIGHT, NINE))
        x3 = randint(ONE, x2)
        x4 = build_output_1e97544e(x3, x2, x0)
        x5 = []
        x6 = unifint(diff_lb, diff_ub, (THREE, FIVE))
        for _ in range(x6):
            for _ in range(100):
                x7 = _sample_cluster_1e97544e(x0)
                if any(manhattan(x7, x8) <= ONE for x8 in x5):
                    continue
                x5.append(x7)
                break
            else:
                x5 = []
                break
        if len(x5) != x6:
            continue
        x7 = frozenset(merge(tuple(x5)))
        x8 = size(x7)
        if x8 < 35 or x8 > 85:
            continue
        x9 = fill(x4, ZERO, x7)
        if index(x9, ORIGIN) == ZERO:
            continue
        x10 = _zero_components_1e97544e(x7, x0)
        x11 = size(x10)
        if x11 != x6:
            continue
        x12 = frozenset(interval(ONE, x2 + ONE, ONE))
        x13 = remove(ZERO, palette(x9))
        if x13 != x12:
            continue
        if colorcount(x9, ZERO) <= x1:
            continue
        if verify_1e97544e(x9) != x4:
            continue
        return {"input": x9, "output": x4}
