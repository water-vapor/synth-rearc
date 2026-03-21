from arc2.core import *

from .verifier import verify_ba9d41b8


ACTIVE_COLORS_BA9D41B8 = interval(ONE, TEN, ONE)
RECT_HEIGHTS_BA9D41B8 = (FIVE, FIVE, SIX, SIX, SEVEN, SEVEN, EIGHT, EIGHT, NINE)
RECT_WIDTHS_BA9D41B8 = (FIVE, SIX, SEVEN, EIGHT, EIGHT, NINE, TEN, TEN, 11, 12)


def _rectangle_patch_ba9d41b8(
    x0: IntegerTuple,
    x1: IntegerTuple,
) -> Indices:
    x2, x3 = x0
    x4, x5 = x1
    x6 = interval(x2, x2 + x4, ONE)
    x7 = interval(x3, x3 + x5, ONE)
    x8 = product(x6, x7)
    return x8


def _rectangle_halo_ba9d41b8(
    x0: IntegerTuple,
    x1: IntegerTuple,
) -> Indices:
    x2, x3 = x0
    x4, x5 = x1
    x6 = interval(x2 - ONE, x2 + x4 + ONE, ONE)
    x7 = interval(x3 - ONE, x3 + x5 + ONE, ONE)
    x8 = product(x6, x7)
    return x8


def _checkerboard_patch_ba9d41b8(
    x0: Indices,
    x1: Integer,
) -> Object:
    x2 = ulcorner(x0)
    x3 = fork(add, first, last)
    x4 = x3(x2)
    x5 = even(x4)
    x6 = box(x0)
    x7 = difference(x0, x6)
    x8 = compose(even, x3)
    x9 = matcher(x8, flip(x5))
    x10 = sfilter(x7, x9)
    x11 = combine(x6, x10)
    x12 = recolor(x1, x11)
    return x12


def _sample_rectangle_ba9d41b8(
    x0: Integer,
    x1: Integer,
    x2: Indices,
) -> tuple[IntegerTuple, IntegerTuple] | None:
    x3 = tuple(x4 for x4 in RECT_HEIGHTS_BA9D41B8 if x4 <= x0)
    x5 = tuple(x6 for x6 in RECT_WIDTHS_BA9D41B8 if x6 <= x1)
    if len(x3) == ZERO or len(x5) == ZERO:
        return None
    for _ in range(200):
        x7 = choice(x3)
        x8 = choice(x5)
        x9 = astuple(x7, x8)
        x10 = tuple(
            (x11, x12)
            for x11 in range(x0 - x7 + ONE)
            for x12 in range(x1 - x8 + ONE)
            if len(intersection(_rectangle_patch_ba9d41b8((x11, x12), x9), x2)) == ZERO
        )
        if len(x10) == ZERO:
            continue
        x13 = tuple(
            x14 for x14 in x10
            if x14[0] == ZERO or x14[1] == ZERO or x14[0] + x7 == x0 or x14[1] + x8 == x1
        )
        x14 = branch(len(x13) > ZERO and choice((T, F)), x13, x10)
        x15 = choice(x14)
        return (x15, x9)
    return None


def generate_ba9d41b8(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (13, 20))
        x1 = unifint(diff_lb, diff_ub, (13, 20))
        x2 = astuple(x0, x1)
        x3 = min(FOUR, max(ONE, (x0 * x1) // 70))
        x4 = unifint(diff_lb, diff_ub, (ONE, x3))
        x5 = sample(ACTIVE_COLORS_BA9D41B8, x4)
        x6 = tuple()
        x7 = frozenset()
        x8 = T
        for x9 in range(x4):
            x10 = _sample_rectangle_ba9d41b8(x0, x1, x7)
            if x10 is None:
                x8 = F
                break
            x11, x12 = x10
            x13 = _rectangle_patch_ba9d41b8(x11, x12)
            x14 = _rectangle_halo_ba9d41b8(x11, x12)
            x15 = x5[x9]
            x6 = x6 + ((x11, x12, x15, x13),)
            x7 = combine(x7, x14)
        if not x8:
            continue
        x16 = canvas(ZERO, x2)
        x17 = canvas(ZERO, x2)
        for x18, x19, x20, x21 in x6:
            x16 = fill(x16, x20, x21)
            x22 = _checkerboard_patch_ba9d41b8(x21, x20)
            x17 = paint(x17, x22)
        if len(objects(x16, T, F, T)) != x4:
            continue
        if x16 == x17:
            continue
        if verify_ba9d41b8(x16) != x17:
            continue
        return {"input": x16, "output": x17}
