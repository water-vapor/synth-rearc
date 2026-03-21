from arc2.core import *


DIRECTIONS_C074846D = (UP, RIGHT, DOWN, LEFT)


def _clockwise_direction_c074846d(
    direction: IntegerTuple,
) -> IntegerTuple:
    x0 = last(direction)
    x1 = first(direction)
    x2 = invert(x1)
    return astuple(x0, x2)


def _margin_c074846d(
    side: IntegerTuple,
    direction: IntegerTuple,
    rotated_direction: IntegerTuple,
    arm_length: Integer,
    diff_lb: float,
    diff_ub: float,
) -> Integer:
    x0 = unifint(diff_lb, diff_ub, (ZERO, THREE))
    if side == direction or side == rotated_direction:
        return add(x0, arm_length)
    return x0


def _arm_patch_c074846d(
    pivot: IntegerTuple,
    direction: IntegerTuple,
    arm_length: Integer,
) -> Indices:
    x0 = add(pivot, direction)
    x1 = multiply(direction, arm_length)
    x2 = add(pivot, x1)
    return connect(x0, x2)


def generate_c074846d(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (ONE, FOUR))
        x1 = choice(DIRECTIONS_C074846D)
        x2 = _clockwise_direction_c074846d(x1)
        x3 = _margin_c074846d(UP, x1, x2, x0, diff_lb, diff_ub)
        x4 = _margin_c074846d(DOWN, x1, x2, x0, diff_lb, diff_ub)
        x5 = _margin_c074846d(LEFT, x1, x2, x0, diff_lb, diff_ub)
        x6 = _margin_c074846d(RIGHT, x1, x2, x0, diff_lb, diff_ub)
        x7 = add(add(x3, x4), ONE)
        x8 = add(add(x5, x6), ONE)
        if x7 < THREE or x8 < THREE:
            continue
        x9 = astuple(x3, x5)
        x10 = _arm_patch_c074846d(x9, x1, x0)
        x11 = _arm_patch_c074846d(x9, x2, x0)
        gi = canvas(ZERO, (x7, x8))
        gi = fill(gi, FIVE, frozenset({x9}))
        gi = fill(gi, TWO, x10)
        go = canvas(ZERO, (x7, x8))
        go = fill(go, FIVE, frozenset({x9}))
        go = fill(go, THREE, x10)
        go = fill(go, TWO, x11)
        return {"input": gi, "output": go}
