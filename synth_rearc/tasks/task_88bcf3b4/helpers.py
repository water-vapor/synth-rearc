from __future__ import annotations

import math
from synth_rearc.core import *


DIRS8_88BCF3B4 = (
    (-ONE, -ONE),
    (-ONE, ZERO),
    (-ONE, ONE),
    (ZERO, -ONE),
    (ZERO, ONE),
    (ONE, -ONE),
    (ONE, ZERO),
    (ONE, ONE),
)

DIRS4_88BCF3B4 = (
    (-ONE, ZERO),
    (ONE, ZERO),
    (ZERO, -ONE),
    (ZERO, ONE),
)


def sign_88bcf3b4(
    value: float,
) -> Integer:
    if value > ZERO:
        return ONE
    if value < ZERO:
        return -ONE
    return ZERO


def cross_88bcf3b4(
    a: IntegerTuple,
    b: tuple[float, float] | IntegerTuple,
) -> float:
    return a[0] * b[1] - a[1] * b[0]


def neighbors8_88bcf3b4(
    cell: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    x0, x1 = cell
    return tuple((x0 + x2, x1 + x3) for x2, x3 in DIRS8_88BCF3B4)


def neighbors4_88bcf3b4(
    cell: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    x0, x1 = cell
    return tuple((x0 + x2, x1 + x3) for x2, x3 in DIRS4_88BCF3B4)


def shift_patch_88bcf3b4(
    patch: frozenset[IntegerTuple],
    offset: IntegerTuple,
) -> frozenset[IntegerTuple]:
    return frozenset((i + offset[0], j + offset[1]) for i, j in patch)


def chebyshev_distance_88bcf3b4(
    cell: IntegerTuple,
    patch: frozenset[IntegerTuple],
) -> Integer:
    x0, x1 = cell
    return min(max(abs(x0 - x2), abs(x1 - x3)) for x2, x3 in patch)


def center_88bcf3b4(
    patch: frozenset[IntegerTuple],
) -> tuple[float, float]:
    x0 = tuple(i for i, _ in patch)
    x1 = tuple(j for _, j in patch)
    return (sum(x0) / len(x0), sum(x1) / len(x1))


def line_like_88bcf3b4(
    patch: frozenset[IntegerTuple],
) -> Boolean:
    if len(patch) < TWO:
        return False
    x0 = {i for i, _ in patch}
    x1 = {j for _, j in patch}
    return len(x0) == ONE or len(x1) == ONE


def component_inventory_88bcf3b4(
    grid: Grid,
) -> tuple[tuple[Integer, Integer, frozenset[IntegerTuple]], ...]:
    x0 = mostcolor(grid)
    x1, x2 = shape(grid)
    x3 = set()
    x4 = []
    for x5 in range(x1):
        for x6 in range(x2):
            if (x5, x6) in x3 or grid[x5][x6] == x0:
                continue
            x7 = grid[x5][x6]
            x8 = {(x5, x6)}
            x9 = [(x5, x6)]
            x3.add((x5, x6))
            while len(x9) > ZERO:
                x10 = x9.pop()
                for x11 in neighbors8_88bcf3b4(x10):
                    x12, x13 = x11
                    if x12 < ZERO or x13 < ZERO or x12 >= x1 or x13 >= x2:
                        continue
                    if x11 in x3 or grid[x12][x13] != x7:
                        continue
                    x3.add(x11)
                    x8.add(x11)
                    x9.append(x11)
            x4.append((x7, frozenset(x8)))
    x4.sort(key=lambda item: (uppermost(item[1]), leftmost(item[1]), item[0], len(item[1])))
    return tuple((x14, x15, x16) for x14, (x15, x16) in enumerate(x4))


def rerouted_path_88bcf3b4(
    anchor_cell: IntegerTuple,
    target_patch: frozenset[IntegerTuple],
    path_len: Integer,
    anchor_vec: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    x0 = center_88bcf3b4(target_patch)
    x1 = (x0[0] - anchor_cell[0], x0[1] - anchor_cell[1])
    x2 = -sign_88bcf3b4(cross_88bcf3b4(anchor_vec, x1))
    if x2 == ZERO:
        x2 = -ONE
    x3 = set()
    x4 = min(i for i, _ in target_patch) - path_len - THREE
    x5 = max(i for i, _ in target_patch) + path_len + THREE
    x6 = min(j for _, j in target_patch) - path_len - THREE
    x7 = max(j for _, j in target_patch) + path_len + THREE
    for x8 in range(x4, x5 + ONE):
        for x9 in range(x6, x7 + ONE):
            if (x8, x9) in target_patch:
                continue
            if chebyshev_distance_88bcf3b4((x8, x9), target_patch) == ONE:
                x3.add((x8, x9))
    x10 = [anchor_cell]
    x11 = anchor_cell
    x12 = None
    for _ in range(path_len * THREE):
        if x11 in x3:
            break
        x13 = chebyshev_distance_88bcf3b4(x11, target_patch)
        x14 = (x0[0] - x11[0], x0[1] - x11[1])
        x15 = []
        for x16 in neighbors8_88bcf3b4(x11):
            if x16 in x10 or x16 in target_patch:
                continue
            x17 = chebyshev_distance_88bcf3b4(x16, target_patch)
            if x17 >= x13:
                continue
            x18 = (x16[0] - x11[0], x16[1] - x11[1])
            x19 = sign_88bcf3b4(cross_88bcf3b4(x18, x14))
            x20 = ZERO if x19 in (x2, ZERO) else ONE
            x21 = ZERO if x12 is None else -(x12[0] * x18[0] + x12[1] * x18[1])
            x22 = x18[0] * x14[0] + x18[1] * x14[1]
            x15.append((x17, x20, x21, -x22, x16, x18))
        x15.sort(key=lambda item: (item[0], item[1], item[2], item[3], item[4]))
        if len(x15) == ZERO:
            break
        _, _, _, _, x23, x24 = x15[0]
        x10.append(x23)
        x12 = x24
        x11 = x23
    while len(x10) < path_len:
        if x11 in x3:
            x25 = (x0[0] - x11[0], x0[1] - x11[1])
            x26 = []
            for x27 in neighbors8_88bcf3b4(x11):
                if x27 in x10 or x27 not in x3:
                    continue
                x28 = max(abs(x27[0] - anchor_cell[0]), abs(x27[1] - anchor_cell[1]))
                x29 = max(abs(x11[0] - anchor_cell[0]), abs(x11[1] - anchor_cell[1]))
                if x28 <= x29:
                    continue
                x30 = (x27[0] - x11[0], x27[1] - x11[1])
                x31 = sign_88bcf3b4(cross_88bcf3b4(x30, x25))
                x32 = ZERO if x31 in (x2, ZERO) else ONE
                x33 = ZERO if x12 is None else -(x12[0] * x30[0] + x12[1] * x30[1])
                x26.append((x32, math.dist(x27, x0), x33, x27, x30))
            x26.sort(key=lambda item: (item[0], item[1], item[2], item[3]))
            if len(x26) > ZERO:
                _, _, _, x34, x35 = x26[0]
                x10.append(x34)
                x12 = x35
                x11 = x34
                continue
        if x12 is None:
            break
        x36 = (x11[0] + x12[0], x11[1] + x12[1])
        x10.append(x36)
        x11 = x36
    return tuple(x10)


def _grow_connected_patch_88bcf3b4(
    seed: IntegerTuple,
    allowed: frozenset[IntegerTuple],
    target_size: Integer,
) -> frozenset[IntegerTuple]:
    x0 = {seed}
    while len(x0) < target_size:
        x1 = {
            x2
            for x3 in x0
            for x2 in neighbors8_88bcf3b4(x3)
            if x2 in allowed and x2 not in x0
        }
        if len(x1) == ZERO:
            break
        x4 = []
        for x5 in x1:
            x6 = sum(x7 in x0 for x7 in neighbors8_88bcf3b4(x5))
            x4.extend((x5,) * max(ONE, x6))
        x0.add(choice(tuple(x4)))
    return frozenset(x0)


def _random_path_in_allowed_88bcf3b4(
    start: IntegerTuple,
    path_len: Integer,
    allowed: frozenset[IntegerTuple],
) -> frozenset[IntegerTuple] | None:
    for _ in range(40):
        x0 = [start]
        x1 = None
        while len(x0) < path_len:
            x2 = []
            for x3 in neighbors8_88bcf3b4(x0[-ONE]):
                if x3 not in allowed or x3 in x0:
                    continue
                x4 = (x3[0] - x0[-ONE][0], x3[1] - x0[-ONE][1])
                x5 = ZERO if x1 is None else -(x1[0] * x4[0] + x1[1] * x4[1])
                x2.append((x5, randint(ZERO, 1000), x3, x4))
            x2.sort(key=lambda item: (item[0], item[1], item[2]))
            if len(x2) == ZERO:
                break
            _, _, x6, x7 = choice(x2[: min(len(x2), FOUR)])
            x0.append(x6)
            x1 = x7
        if len(x0) == path_len:
            return frozenset(x0)
    return None


def sample_target_patch_88bcf3b4(
    diff_lb: float,
    diff_ub: float,
    box: frozenset[IntegerTuple],
    anchor_patch: frozenset[IntegerTuple],
    anchor_cell: IntegerTuple,
    anchor_vec: IntegerTuple,
) -> frozenset[IntegerTuple] | None:
    x0 = box - anchor_patch - frozenset({anchor_cell})
    x1 = frozenset({x2 for x3 in anchor_patch for x2 in neighbors4_88bcf3b4(x3)})
    x2 = tuple(
        x3 for x3 in x0
        if x3 not in x1 and x3 not in neighbors4_88bcf3b4(anchor_cell)
    )
    if len(x2) == ZERO:
        return None
    for _ in range(160):
        x3 = choice(x2)
        x4 = choice(("singleton", "line"))
        x5 = frozenset()
        if x4 == "singleton":
            x5 = frozenset({x3})
        else:
            x6 = choice(("v", "h"))
            x7 = unifint(diff_lb, diff_ub, (TWO, SIX))
            if x6 == "v":
                x8 = randint(max(ZERO, x3[0] - x7 + ONE), min(x3[0], max(i for i, _ in box) - x7 + ONE))
                x5 = frozenset((x8 + x9, x3[1]) for x9 in range(x7))
            else:
                x8 = randint(max(ZERO, x3[1] - x7 + ONE), min(x3[1], max(j for _, j in box) - x7 + ONE))
                x5 = frozenset((x3[0], x8 + x9) for x9 in range(x7))
            if not x5 <= box:
                continue
        if len(x5) == ZERO:
            continue
        if not x5 <= box:
            continue
        if len(anchor_patch & x5) > ZERO:
            continue
        if any(x6 in x5 for x6 in neighbors4_88bcf3b4(anchor_cell)):
            continue
        x12 = (center_88bcf3b4(x5)[0] - anchor_cell[0], center_88bcf3b4(x5)[1] - anchor_cell[1])
        if sign_88bcf3b4(cross_88bcf3b4(anchor_vec, x12)) == ZERO:
            continue
        return x5
    return None


def _candidate_steps_88bcf3b4(
    cell: IntegerTuple,
    target_center: tuple[float, float],
    anchor_vec: IntegerTuple,
    prev_step: IntegerTuple | None,
    path: tuple[IntegerTuple, ...],
    allowed: frozenset[IntegerTuple],
) -> tuple[IntegerTuple, ...]:
    x0 = (cell[0] - target_center[0], cell[1] - target_center[1])
    x1 = []
    for x2 in neighbors8_88bcf3b4(cell):
        if x2 not in allowed or x2 in path:
            continue
        x3 = (x2[0] - cell[0], x2[1] - cell[1])
        x4 = x3[0] * x0[0] + x3[1] * x0[1]
        x5 = -(x3[0] * anchor_vec[0] + x3[1] * anchor_vec[1])
        x6 = ZERO if prev_step is None else prev_step[0] * x3[0] + prev_step[1] * x3[1]
        x1.append((-x4, -x5, -x6, randint(ZERO, 1000), x2))
    x1.sort()
    return tuple(x7 for _, _, _, _, x7 in x1)


def sample_input_path_88bcf3b4(
    start: IntegerTuple,
    path_len: Integer,
    allowed: frozenset[IntegerTuple],
    target_patch: frozenset[IntegerTuple],
    anchor_vec: IntegerTuple,
) -> frozenset[IntegerTuple] | None:
    x0 = center_88bcf3b4(target_patch)
    for _ in range(40):
        x1 = [start]
        x2 = None
        x3 = False
        while len(x1) < path_len:
            x4 = _candidate_steps_88bcf3b4(x1[-ONE], x0, anchor_vec, x2, tuple(x1), allowed)
            if len(x4) == ZERO:
                break
            x5 = choice(x4[: min(len(x4), FOUR)])
            x2 = (x5[0] - x1[-ONE][0], x5[1] - x1[-ONE][1])
            x1.append(x5)
        if len(x1) == path_len:
            x3 = True
        if x3:
            return frozenset(x1)
    return None


def sample_local_motif_88bcf3b4(
    diff_lb: float,
    diff_ub: float,
) -> dict | None:
    for _ in range(240):
        x0 = unifint(diff_lb, diff_ub, (EIGHT, 13))
        x1 = unifint(diff_lb, diff_ub, (EIGHT, 13))
        x2 = frozenset((i, j) for i in range(x0) for j in range(x1))
        x3 = choice(("v", "h"))
        if x3 == "v":
            x4 = unifint(diff_lb, diff_ub, (TWO, max(TWO, x0 - THREE)))
            x5 = randint(ONE, x0 - x4 - ONE)
            x6 = randint(ONE, x1 - TWO)
            x7 = frozenset((x5 + x8, x6) for x8 in range(x4))
            x8 = randint(x5, x5 + x4 - ONE)
            if choice((False, True)):
                x9 = (x8, x6 - ONE)
                x10 = (ZERO, ONE)
            else:
                x9 = (x8, x6 + ONE)
                x10 = (ZERO, -ONE)
        else:
            x4 = unifint(diff_lb, diff_ub, (TWO, max(TWO, x1 - THREE)))
            x5 = randint(ONE, x0 - TWO)
            x6 = randint(ONE, x1 - x4 - ONE)
            x7 = frozenset((x5, x6 + x8) for x8 in range(x4))
            x8 = randint(x6, x6 + x4 - ONE)
            if choice((False, True)):
                x9 = (x5 - ONE, x8)
                x10 = (ONE, ZERO)
            else:
                x9 = (x5 + ONE, x8)
                x10 = (-ONE, ZERO)
        if x9 not in x2:
            continue
        x11 = sample_target_patch_88bcf3b4(diff_lb, diff_ub, x2, x7, x9, x10)
        if x11 is None:
            continue
        x12 = unifint(diff_lb, diff_ub, (FOUR, TEN))
        x13 = tuple(rerouted_path_88bcf3b4(x9, x11, x12, x10))
        if not all(x14 in x2 for x14 in x13):
            continue
        x14 = frozenset(x13)
        if len(x7 & x14) > ZERO or len(x11 & x14) > ZERO:
            continue
        x15 = frozenset({x16 for x17 in x7 for x16 in neighbors4_88bcf3b4(x17)}) - frozenset({x9})
        x16 = frozenset({x17 for x18 in x11 for x17 in neighbors4_88bcf3b4(x18)})
        x17 = x2 - x7 - x11 - x15 - x16
        if x9 not in x17:
            x17 = x17 | frozenset({x9})
        x18 = sample_input_path_88bcf3b4(x9, x12, x17, x11, x10)
        if x18 is None:
            continue
        if x18 == x14:
            continue
        return {
            "dims": (x0, x1),
            "anchor": x7,
            "target": x11,
            "input_path": x18,
            "output_path": x14,
        }
    return None
