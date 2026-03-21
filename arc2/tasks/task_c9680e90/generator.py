from arc2.core import *

from .verifier import verify_c9680e90


GRID_SIZES_C9680E90 = (SEVEN, NINE, NINE, 11, 11)
RAY_LENGTH_POOL_C9680E90 = (ONE, ONE, ONE, TWO, TWO, THREE, FOUR)
DIRECTION_ORDER_C9680E90 = (UP, DOWN, LEFT, RIGHT)


def _direct_halo_c9680e90(
    patch: Indices,
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = dims
    x2 = set(patch)
    for x3 in patch:
        for x4 in dneighbors(x3):
            x5, x6 = x4
            if 0 <= x5 < x0 and 0 <= x6 < x1:
                x2.add(x4)
    return frozenset(x2)


def _ray_cells_c9680e90(
    anchor: IntegerTuple,
    direction: IntegerTuple,
    length: Integer,
) -> Indices:
    x0 = add(anchor, direction)
    x1 = add(anchor, multiply(direction, length))
    return connect(x0, x1)


def _max_length_c9680e90(
    anchor: IntegerTuple,
    direction: IntegerTuple,
    side: Integer,
    axis: Integer,
) -> Integer:
    x0, x1 = anchor
    if equality(direction, UP):
        return subtract(subtract(x0, axis), ONE)
    if equality(direction, DOWN):
        return subtract(subtract(side, ONE), x0)
    if equality(direction, LEFT):
        return x1
    return subtract(subtract(side, ONE), x1)


def _candidate_lengths_c9680e90(
    max_length: Integer,
) -> Tuple:
    x0 = [x1 for x1 in RAY_LENGTH_POOL_C9680E90 if x1 <= max_length]
    if len(x0) == ZERO:
        return tuple()
    shuffle(x0)
    x2 = list(range(ONE, max_length + ONE))
    shuffle(x2)
    return tuple(x0 + x2)


def _sample_ray_c9680e90(
    side: Integer,
    axis: Integer,
    anchors: Indices,
    rays: Indices,
    ray_halo: Indices,
    anchor_halo: Indices,
) -> tuple[IntegerTuple, IntegerTuple, Integer] | None:
    x0 = [(i, j) for i in range(axis + ONE, side) for j in range(side)]
    shuffle(x0)
    for x1 in x0:
        if x1 in anchors or x1 in rays:
            continue
        if len(intersection(dneighbors(x1), rays)) > ZERO:
            continue
        x2 = list(DIRECTION_ORDER_C9680E90)
        shuffle(x2)
        for x3 in x2:
            x4 = _max_length_c9680e90(x1, x3, side, axis)
            if x4 < ONE:
                continue
            for x5 in _candidate_lengths_c9680e90(x4):
                x6 = _ray_cells_c9680e90(x1, x3, x5)
                if len(intersection(x6, anchors)) > ZERO:
                    continue
                if len(intersection(x6, rays)) > ZERO:
                    continue
                if len(intersection(x6, ray_halo)) > ZERO:
                    continue
                if len(intersection(x6, anchor_halo)) > ZERO:
                    continue
                return (x1, x3, x5)
    return None


def _count_choices_c9680e90(
    side: Integer,
) -> Tuple:
    if equality(side, SEVEN):
        return (TWO, TWO, THREE)
    if equality(side, NINE):
        return (THREE, THREE, FOUR)
    return (FOUR, FOUR, FIVE)


def _distractors_c9680e90(
    side: Integer,
    axis: Integer,
    count: Integer,
    blocked: Indices,
) -> tuple[IntegerTuple, ...] | None:
    x0 = [(i, j) for i in range(axis) for j in range(side)]
    shuffle(x0)
    x1 = []
    for x2 in x0:
        if x2 in blocked:
            continue
        x1.append(x2)
        if len(x1) == count:
            return tuple(x1)
    return None


def generate_c9680e90(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(GRID_SIZES_C9680E90)
        x1 = astuple(x0, x0)
        x2 = halve(x0)
        x3 = choice(_count_choices_c9680e90(x0))
        x4 = frozenset()
        x5 = frozenset()
        x6 = frozenset()
        x7 = frozenset()
        x8 = []
        x9 = T
        for _ in range(x3):
            x10 = _sample_ray_c9680e90(x0, x2, x4, x5, x6, x7)
            if x10 is None:
                x9 = F
                break
            x11, x12, x13 = x10
            x14 = _ray_cells_c9680e90(x11, x12, x13)
            x8.append(x10)
            x4 = combine(x4, initset(x11))
            x5 = combine(x5, x14)
            x6 = combine(x6, _direct_halo_c9680e90(x14, x1))
            x7 = combine(x7, dneighbors(x11))
        if flip(x9):
            continue
        x15 = frozenset()
        for x17, x18, x19 in x8:
            x20 = add(x17, multiply(x18, x19))
            x21 = astuple(subtract(double(x2), x20[0]), x20[1])
            x15 = combine(x15, initset(x21))
        x22 = _distractors_c9680e90(x0, x2, x3, x15)
        if x22 is None:
            continue
        gi = canvas(SEVEN, x1)
        go = canvas(SEVEN, x1)
        x23 = hfrontier((x2, ZERO))
        gi = fill(gi, NINE, x23)
        go = fill(go, NINE, x23)
        for x24 in x22:
            gi = fill(gi, FIVE, initset(x24))
        for x25, x26, x27 in x8:
            x28 = _ray_cells_c9680e90(x25, x26, x27)
            x29 = add(x25, multiply(x26, x27))
            x30 = astuple(subtract(double(x2), x29[0]), x29[1])
            gi = fill(gi, TWO, initset(x25))
            gi = fill(gi, SIX, x28)
            go = fill(go, TWO, initset(x29))
            go = fill(go, FIVE, initset(x30))
        if equality(gi, go):
            continue
        if colorcount(gi, FIVE) != x3:
            continue
        if colorcount(gi, TWO) != x3:
            continue
        if verify_c9680e90(gi) != go:
            continue
        return {"input": gi, "output": go}
