from synth_rearc.core import *

from .helpers import (
    colored_object_cd3c21df,
    place_objects_cd3c21df,
    rectangle_patch_cd3c21df,
    sample_connected_patch_cd3c21df,
)
from .verifier import verify_cd3c21df


UNIQUE_DIMS_CD3C21DF = (
    (ONE, THREE),
    (ONE, FOUR),
    (FOUR, ONE),
    (TWO, TWO),
    (TWO, THREE),
    (THREE, TWO),
)
PAIR_DIMS_CD3C21DF = (
    (ONE, THREE),
    (ONE, FOUR),
    (THREE, ONE),
    (FOUR, ONE),
    (TWO, TWO),
    (TWO, THREE),
)


def _sample_unique_object_cd3c21df(
    diff_lb: float,
    diff_ub: float,
) -> Object:
    x0 = choice(UNIQUE_DIMS_CD3C21DF)
    x1 = rectangle_patch_cd3c21df(x0[ZERO], x0[ONE])
    x2 = size(x1) > ONE and randint(ZERO, 99) < 45
    x3 = TWO if x2 else ONE
    return colored_object_cd3c21df(diff_lb, diff_ub, x1, x3, x3)


def _sample_rect_pair_object_cd3c21df(
    diff_lb: float,
    diff_ub: float,
) -> Object:
    x0 = choice(PAIR_DIMS_CD3C21DF)
    x1 = rectangle_patch_cd3c21df(x0[ZERO], x0[ONE])
    x2 = size(x1) > THREE and randint(ZERO, 99) < 20
    x3 = TWO if x2 else ONE
    return colored_object_cd3c21df(diff_lb, diff_ub, x1, x3, x3)


def _sample_irregular_pair_object_cd3c21df(
    diff_lb: float,
    diff_ub: float,
) -> Object:
    x0 = sample_connected_patch_cd3c21df(
        diff_lb,
        diff_ub,
        (TWO, THREE),
        (TWO, FOUR),
        (THREE, SIX),
        require_irregular=T,
    )
    x1 = size(x0) > THREE and randint(ZERO, 99) < 70
    x2 = TWO if x1 else ONE
    return colored_object_cd3c21df(diff_lb, diff_ub, x0, x2, x2)


def generate_cd3c21df(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _sample_unique_object_cd3c21df(diff_lb, diff_ub)
        x1 = _sample_rect_pair_object_cd3c21df(diff_lb, diff_ub)
        if x1 == x0:
            continue
        x2 = _sample_irregular_pair_object_cd3c21df(diff_lb, diff_ub)
        if x2 in (x0, x1):
            continue
        x3 = unifint(diff_lb, diff_ub, (11, 15))
        x4 = unifint(diff_lb, diff_ub, (11, 15))
        x5 = (x0, x1, x1, x2, x2)
        x6 = place_objects_cd3c21df(x5, (x3, x4))
        if x6 is None:
            continue
        x7 = canvas(ZERO, (x3, x4))
        for x8 in x6:
            x7 = paint(x7, x8)
        x9 = paint(canvas(ZERO, shape(x0)), x0)
        x10 = objects(x7, F, F, T)
        if size(x10) != FIVE:
            continue
        x11 = apply(normalize, totuple(x10))
        if leastcommon(x11) != x0:
            continue
        if verify_cd3c21df(x7) != x9:
            continue
        return {"input": x7, "output": x9}
