from __future__ import annotations

from collections import Counter

from synth_rearc.core import *

from .helpers import (
    DIRECTIONS_409aa875,
    INPUT_COLORS_409aa875,
    make_arrow_object_409aa875,
    ordered_objects_409aa875,
    projection_target_409aa875,
    reservation_patch_409aa875,
    valid_joint_409aa875,
)


GRID_DIMS = (16, 16)

_MAIN_DIRECTION_BAG = (
    UP,
    UP,
    LEFT,
    RIGHT,
    DOWN,
    NEG_UNITY,
    NEG_UNITY,
    UP_RIGHT,
    DOWN_LEFT,
    UNITY,
)


def _candidate_joints_409aa875(direction: IntegerTuple) -> tuple[IntegerTuple, ...]:
    h, w = GRID_DIMS
    x0 = []
    for i in range(h):
        for j in range(w):
            x1 = (i, j)
            if valid_joint_409aa875(x1, direction, GRID_DIMS):
                x0.append(x1)
    x2 = tuple(x0)
    return x2


def _line_axis_409aa875(direction: IntegerTuple) -> Integer:
    x0 = branch(contained(direction, (LEFT, RIGHT)), ONE, ZERO)
    return x0


def _place_main_objects_409aa875(
    color: Integer,
    direction: IntegerTuple,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Object, ...] | None:
    x0 = _candidate_joints_409aa875(direction)
    x1 = _line_axis_409aa875(direction)
    x2 = sorted({loc[x1] for loc in x0})
    if len(x2) == ZERO:
        return None
    x3 = branch(greater(len(x2), ONE), unifint(diff_lb, diff_ub, (ONE, TWO)), ONE)
    x4 = sample(x2, x3)
    x5 = [loc for loc in x0 if loc[x1] in x4]
    shuffle(x5)
    x6 = unifint(diff_lb, diff_ub, (THREE, SEVEN))
    x7 = frozenset({})
    x8: list[Object] = []
    for x9 in x5:
        x10 = make_arrow_object_409aa875(color, x9, direction)
        x11 = reservation_patch_409aa875(x10)
        if len(intersection(x11, x7)) != ZERO:
            continue
        x8.append(x10)
        x7 = combine(x7, x11)
        if len(x8) == x6:
            break
    if len(x8) < THREE:
        return None
    x12 = tuple(x8)
    return x12


def _try_add_projection_object_409aa875(
    reserved: Indices,
    color: Integer,
    target: IntegerTuple,
) -> tuple[Object | None, Indices]:
    x0 = list(DIRECTIONS_409aa875)
    shuffle(x0)
    for x1 in x0:
        x2 = subtract(target, multiply(FIVE, x1))
        if not valid_joint_409aa875(x2, x1, GRID_DIMS):
            continue
        x3 = make_arrow_object_409aa875(color, x2, x1)
        x4 = reservation_patch_409aa875(x3)
        if len(intersection(x4, reserved)) != ZERO:
            continue
        x5 = combine(reserved, x4)
        return x3, x5
    return None, reserved


def _paint_scene_409aa875(objs: tuple[Object, ...]) -> tuple[Grid, Grid]:
    x0 = canvas(SEVEN, GRID_DIMS)
    for x1 in objs:
        x0 = paint(x0, x1)
    x2 = ordered_objects_409aa875(objects(x0, T, T, T))
    x3 = Counter()
    x4 = Counter()
    for x5 in x2:
        x6 = projection_target_409aa875(x5)
        x7 = None
        for x8, x9 in enumerate(x2):
            if x6 in toindices(x9):
                x7 = x8
                break
        if x7 is None:
            if index(x0, x6) is not None:
                x3[x6] += ONE
        else:
            x4[x7] += ONE
    x10 = x0
    for x11, x12 in sorted(x3.items()):
        x13 = branch(greater(x12, ONE), ONE, NINE)
        x10 = fill(x10, x13, frozenset({x11}))
    for x14, x15 in sorted(x4.items()):
        x16 = branch(greater(x15, ONE), ONE, NINE)
        x10 = fill(x10, x16, x2[x14])
    return x0, x10


def generate_409aa875(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(INPUT_COLORS_409aa875)
        x1 = choice(_MAIN_DIRECTION_BAG)
        x2 = _place_main_objects_409aa875(x0, x1, diff_lb, diff_ub)
        if x2 is None:
            continue
        x3 = list(x2)
        x4 = frozenset({})
        for x5 in x3:
            x4 = combine(x4, reservation_patch_409aa875(x5))
        x6 = choice((T, F))
        if x6:
            x7 = [projection_target_409aa875(obj) for obj in x3]
            shuffle(x7)
            for x8 in x7:
                x9, x4 = _try_add_projection_object_409aa875(x4, x0, x8)
                if x9 is not None:
                    x3.append(x9)
                    break
        x10 = choice((T, F))
        if x10:
            x11 = [ij for obj in x3 for ij in toindices(obj)]
            shuffle(x11)
            for x12 in x11:
                x13, x4 = _try_add_projection_object_409aa875(x4, x0, x12)
                if x13 is not None:
                    x3.append(x13)
                    break
        x14 = tuple(x3)
        x15 = _paint_scene_409aa875(x14)
        x16, x17 = x15
        x18 = colorcount(x17, ONE)
        x19 = sum(x16[i][j] != x17[i][j] for i in range(GRID_DIMS[0]) for j in range(GRID_DIMS[1]))
        x20 = len(objects(x16, T, T, T))
        x21 = equality(x20, len(x14))
        x22 = greater(x19, TWO)
        x23 = greater(13, x19)
        x24 = x18 <= TWO
        x25 = both(x21, x22)
        x26 = both(x23, x24)
        x27 = both(x25, x26)
        if not x27:
            continue
        return {"input": x16, "output": x17}
