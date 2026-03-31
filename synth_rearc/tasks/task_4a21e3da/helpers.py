from __future__ import annotations

from collections import deque

from synth_rearc.core import *


BG_COLOR_4A21E3DA = ONE
SEED_COLOR_4A21E3DA = TWO
SHAPE_COLOR_4A21E3DA = SEVEN


def _rotate_grid_4a21e3da(
    grid: Grid,
    turns: Integer,
) -> Grid:
    x0 = grid
    for _ in range(turns % FOUR):
        x0 = rot90(x0)
    return x0


def _nearest_cell_4a21e3da(
    target: IntegerTuple,
    cells: frozenset[IntegerTuple],
) -> IntegerTuple:
    return min(cells, key=lambda cell: abs(cell[0] - target[0]) + abs(cell[1] - target[1]))


def _neighbors_in_allowed_4a21e3da(
    cell: IntegerTuple,
    allowed: frozenset[IntegerTuple],
) -> tuple[IntegerTuple, ...]:
    x0 = [x1 for x1 in dneighbors(cell) if x1 in allowed]
    shuffle(x0)
    return tuple(x0)


def _path_between_4a21e3da(
    start: IntegerTuple,
    goal: IntegerTuple,
    allowed: frozenset[IntegerTuple],
) -> frozenset[IntegerTuple]:
    if start == goal:
        return frozenset({start})
    x0 = deque([start])
    x1 = {start: None}
    while len(x0) > ZERO:
        x2 = x0.popleft()
        if x2 == goal:
            break
        for x3 in _neighbors_in_allowed_4a21e3da(x2, allowed):
            if x3 in x1:
                continue
            x1[x3] = x2
            x0.append(x3)
    if goal not in x1:
        return frozenset({start, goal})
    x4 = {goal}
    x5 = goal
    while x1[x5] is not None:
        x5 = x1[x5]
        x4.add(x5)
    return frozenset(x4)


def _grow_connected_object_4a21e3da(
    anchors: frozenset[IntegerTuple],
    allowed: frozenset[IntegerTuple],
    target_size: Integer,
) -> frozenset[IntegerTuple]:
    x0 = tuple(anchors)
    x1 = set()
    x1.add(choice(x0))
    x2 = [x3 for x3 in x0 if x3 not in x1]
    shuffle(x2)
    for x3 in x2:
        x4 = _nearest_cell_4a21e3da(x3, frozenset(x1))
        x5 = _path_between_4a21e3da(x4, x3, allowed)
        x1 |= set(x5)
    x6 = ZERO
    while len(x1) < target_size and x6 < 800:
        x6 = x6 + ONE
        x7 = {x8 for x9 in x1 for x8 in dneighbors(x9) if x8 in allowed and x8 not in x1}
        if len(x7) == ZERO:
            break
        x10 = choice(tuple(x7))
        x1.add(x10)
        if randint(ZERO, FOUR) == ZERO:
            x11 = tuple(x12 for x12 in dneighbors(x10) if x12 in allowed and x12 not in x1)
            if len(x11) > ZERO:
                x1.add(choice(x11))
    return frozenset(x1)


def generate_input_4a21e3da(
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    while True:
        x0 = unifint(diff_lb, diff_ub, (18, 24))
        x1 = unifint(diff_lb, diff_ub, (18, 24))
        x2 = randint(4, max(4, x0 // TWO - TWO))
        if max(x2 + FIVE, x0 // TWO) > x0 - SIX:
            continue
        x3 = randint(max(x2 + FIVE, x0 // TWO), x0 - SIX)
        x4 = randint(4, max(4, x1 // FOUR))
        if max(x4 + SIX, x1 // TWO) > x1 - FIVE:
            continue
        x5 = randint(max(x4 + SIX, x1 // TWO), x1 - FIVE)
        if x3 - x2 < FIVE or x5 - x4 < SIX:
            continue
        x6 = randint(x4 + TWO, x5 - TWO)
        x7 = choice((False, False, True))
        x8 = None
        x9 = set()
        x10 = set()
        if x7:
            x8 = randint(x2 + TWO, x3 - TWO)
            x11 = tuple(range(x2, x8))
            x12 = tuple(range(x8 + ONE, x3 + ONE))
            if len(x11) < TWO or len(x12) < TWO:
                continue
            x13 = sample(x11, randint(ONE, min(THREE, len(x11))))
            x9 |= {(x14, x6) for x14 in x13}
            x9.add((choice(x11), randint(x4, x6 - ONE)))
            x9.add((choice(x11), randint(x6 + ONE, x5)))
            x9.add((choice(x12), randint(x6 + ONE, x5)))
            if choice((False, True, True)):
                x9.add((choice(x12), randint(x4, x6 - ONE)))
            x15 = {randint(x4, x6 - ONE), randint(x6 + ONE, x5)}
            x16 = [j for j in range(x4, x5 + ONE) if j not in x15]
            shuffle(x16)
            for x17 in x16[: randint(ZERO, min(TWO, len(x16)))]:
                x15.add(x17)
            x9 |= {(x8, x17) for x17 in x15}
            x10 = {(i, x6) for i in range(x8 + ONE, x3 + ONE)}
        else:
            x18 = sample(tuple(range(x2, x3 + ONE)), randint(ONE, min(FOUR, x3 - x2 + ONE)))
            x9 |= {(x19, x6) for x19 in x18}
            x9.add((randint(x2, x3), randint(x4, x6 - ONE)))
            x9.add((randint(x2, x3), randint(x6 + ONE, x5)))
            for _ in range(randint(ONE, THREE)):
                x20 = choice(("left", "right", "column"))
                if x20 == "left":
                    x9.add((randint(x2, x3), randint(x4, x6 - ONE)))
                elif x20 == "right":
                    x9.add((randint(x2, x3), randint(x6 + ONE, x5)))
                else:
                    x9.add((randint(x2, x3), x6))
        x21 = frozenset(
            (i, j)
            for i in range(x2, x3 + ONE)
            for j in range(x4, x5 + ONE)
            if (i, j) not in x10
        )
        x22 = max(len(x9) + SIX, 18)
        x23 = min(len(x21), 38 if not x7 else 34)
        if x22 > x23:
            continue
        x24 = unifint(diff_lb, diff_ub, (x22, x23))
        x25 = _grow_connected_object_4a21e3da(frozenset(x9), x21, x24)
        if len(frozenset((i, j) for i, j in x25 if j < x6)) == ZERO:
            continue
        if len(frozenset((i, j) for i, j in x25 if j > x6)) == ZERO:
            continue
        if len(frozenset((i, j) for i, j in x25 if j == x6)) == ZERO:
            continue
        if x7 and len(frozenset((i, j) for i, j in x25 if i == x8)) == ZERO:
            continue
        if x7 and not any(i < x8 and j > x6 for i, j in x25):
            continue
        if x7 and not any(i > x8 and j > x6 for i, j in x25):
            continue
        x26 = canvas(BG_COLOR_4A21E3DA, (x0, x1))
        x26 = fill(x26, SHAPE_COLOR_4A21E3DA, x25)
        x27 = frozenset({(ZERO, x6)})
        if x7:
            x27 = combine(x27, frozenset({(x8, x1 - ONE)}))
        x26 = fill(x26, SEED_COLOR_4A21E3DA, x27)
        x28 = randint(ZERO, THREE)
        return _rotate_grid_4a21e3da(x26, x28)
