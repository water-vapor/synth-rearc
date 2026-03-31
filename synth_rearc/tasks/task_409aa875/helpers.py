from __future__ import annotations

from synth_rearc.core import *


DIRECTIONS_409aa875 = (
    UP,
    DOWN,
    LEFT,
    RIGHT,
    NEG_UNITY,
    UP_RIGHT,
    DOWN_LEFT,
    UNITY,
)

INPUT_COLORS_409aa875 = tuple(c for c in range(TEN) if c not in (ONE, SEVEN))

_LEAF_OFFSETS_409aa875 = {
    UP: ((1, -1), (1, 1)),
    DOWN: ((-1, -1), (-1, 1)),
    LEFT: ((-1, 1), (1, 1)),
    RIGHT: ((-1, -1), (1, -1)),
    NEG_UNITY: ((0, 1), (1, 0)),
    UP_RIGHT: ((0, -1), (1, 0)),
    DOWN_LEFT: ((-1, 0), (0, 1)),
    UNITY: ((-1, 0), (0, -1)),
}


def make_arrow_object_409aa875(
    value: Integer,
    joint: IntegerTuple,
    direction: IntegerTuple,
) -> Object:
    x0 = _LEAF_OFFSETS_409aa875[direction]
    x1 = {joint, add(joint, x0[0]), add(joint, x0[1])}
    x2 = recolor(value, frozenset(x1))
    return x2


def ordered_objects_409aa875(objs: Objects) -> tuple[Object, ...]:
    x0 = tuple(sorted(objs, key=lambda obj: (ulcorner(obj), lowermost(obj), rightmost(obj))))
    return x0


def reservation_patch_409aa875(obj: Object) -> Indices:
    x0 = toindices(obj)
    x1 = set(x0)
    for ij in x0:
        x1.update(neighbors(ij))
    x2 = frozenset(x1)
    return x2


def joint_cell_409aa875(obj: Object) -> IntegerTuple:
    x0 = toindices(obj)
    for x1 in (dneighbors, ineighbors):
        for x2 in x0:
            x3 = intersection(x1(x2), x0)
            if size(x3) == TWO:
                return x2
    raise ValueError(f"could not locate joint cell for {obj}")


def pointing_direction_409aa875(obj: Object) -> IntegerTuple:
    x0 = joint_cell_409aa875(obj)
    x1 = list(remove(x0, toindices(obj)))
    x2 = add(x1[0], x1[1])
    x3 = subtract(multiply(x0, TWO), x2)
    x4 = sign(x3)
    return x4


def projection_target_409aa875(obj: Object) -> IntegerTuple:
    x0 = joint_cell_409aa875(obj)
    x1 = pointing_direction_409aa875(obj)
    x2 = multiply(FIVE, x1)
    x3 = add(x0, x2)
    return x3


def valid_joint_409aa875(
    joint: IntegerTuple,
    direction: IntegerTuple,
    dims: IntegerTuple,
) -> Boolean:
    x0 = make_arrow_object_409aa875(TWO, joint, direction)
    x1 = toindices(x0)
    x2 = projection_target_409aa875(x0)
    h, w = dims
    x3 = all(0 <= i < h and 0 <= j < w for i, j in x1)
    x4 = 0 <= x2[0] < h and 0 <= x2[1] < w
    x5 = both(x3, x4)
    return x5
