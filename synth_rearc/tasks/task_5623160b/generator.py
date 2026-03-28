from synth_rearc.core import *

from .verifier import verify_5623160b


BG_5623160B = SEVEN
HUB_5623160B = NINE
DIM_BOUNDS_5623160B = (9, 16)
OBJECT_COUNT_BOUNDS_5623160B = (3, 7)
MAX_HUB_SIZE_5623160B = EIGHT
MAX_REACH_5623160B = FOUR
DIRS_5623160B = (UP, DOWN, LEFT, RIGHT)
OBJECT_COLORS_5623160B = tuple(
    x0 for x0 in interval(ZERO, TEN, ONE) if x0 not in (BG_5623160B, HUB_5623160B)
)


def _shift_index_5623160b(
    loc: IntegerTuple,
    direction: IntegerTuple,
) -> IntegerTuple:
    return add(loc, direction)


def _exposed_sides_5623160b(
    hub: Indices,
    dim: int,
) -> tuple[tuple[IntegerTuple, IntegerTuple, IntegerTuple], ...]:
    x0 = []
    for x1 in hub:
        for x2 in DIRS_5623160B:
            x3 = _shift_index_5623160b(x1, x2)
            if 0 <= x3[ZERO] < dim and 0 <= x3[ONE] < dim and x3 not in hub:
                x0.append((x1, x2, x3))
    return tuple(x0)


def _grow_hub_5623160b(
    diff_lb: float,
    diff_ub: float,
    dim: int,
) -> Indices:
    x0 = min(MAX_HUB_SIZE_5623160B, max(ONE, dim - THREE))
    for _ in range(200):
        x1 = unifint(diff_lb, diff_ub, (ONE, x0))
        x2 = (randint(TWO, dim - THREE), randint(TWO, dim - THREE))
        x3 = {x2}
        while len(x3) < x1:
            x4 = []
            for x5 in tuple(x3):
                for x6 in dneighbors(x5):
                    if not (TWO <= x6[ZERO] <= dim - THREE and TWO <= x6[ONE] <= dim - THREE):
                        continue
                    if x6 in x3:
                        continue
                    x7 = sum(x8 in x3 for x8 in dneighbors(x6))
                    if x7 > TWO:
                        continue
                    x4.append(x6)
            if len(x4) == ZERO:
                break
            x3.add(choice(tuple(x4)))
        if len(x3) != x1:
            continue
        x9 = _exposed_sides_5623160b(frozenset(x3), dim)
        x10 = {x11 for _, x11, _ in x9}
        if len(x10) < THREE:
            continue
        return frozenset(x3)
    raise ValueError("unable to sample a 9-framework for 5623160b")


def _relative_area_5623160b(
    direction: IntegerTuple,
    anchor: IntegerTuple,
    dim: int,
) -> set[IntegerTuple]:
    x0, x1 = anchor
    if direction == UP:
        x2 = randint(ZERO, min(MAX_REACH_5623160B, x0))
        x3 = randint(ZERO, min(MAX_REACH_5623160B, x1))
        x4 = randint(ZERO, min(MAX_REACH_5623160B, dim - ONE - x1))
        return {(x5, x6) for x5 in range(-x2, ONE) for x6 in range(-x3, x4 + ONE)}
    if direction == DOWN:
        x2 = randint(ZERO, min(MAX_REACH_5623160B, dim - ONE - x0))
        x3 = randint(ZERO, min(MAX_REACH_5623160B, x1))
        x4 = randint(ZERO, min(MAX_REACH_5623160B, dim - ONE - x1))
        return {(x5, x6) for x5 in range(ZERO, x2 + ONE) for x6 in range(-x3, x4 + ONE)}
    if direction == LEFT:
        x2 = randint(ZERO, min(MAX_REACH_5623160B, x1))
        x3 = randint(ZERO, min(MAX_REACH_5623160B, x0))
        x4 = randint(ZERO, min(MAX_REACH_5623160B, dim - ONE - x0))
        return {(x5, x6) for x5 in range(-x3, x4 + ONE) for x6 in range(-x2, ONE)}
    x2 = randint(ZERO, min(MAX_REACH_5623160B, dim - ONE - x1))
    x3 = randint(ZERO, min(MAX_REACH_5623160B, x0))
    x4 = randint(ZERO, min(MAX_REACH_5623160B, dim - ONE - x0))
    return {(x5, x6) for x5 in range(-x3, x4 + ONE) for x6 in range(ZERO, x2 + ONE)}


def _random_patch_5623160b(
    diff_lb: float,
    diff_ub: float,
    direction: IntegerTuple,
    anchor: IntegerTuple,
    dim: int,
) -> Indices | None:
    for _ in range(80):
        x0 = _relative_area_5623160b(direction, anchor, dim)
        if len(x0) == ZERO:
            continue
        x1 = 20 if dim >= 14 else 14
        x2 = min(len(x0), x1)
        x3 = unifint(diff_lb, diff_ub, (ONE, x2))
        x4 = {(ZERO, ZERO)}
        while len(x4) < x3:
            x5 = [
                x6
                for x6 in x0
                if x6 not in x4 and any(add(x6, x7) in x4 for x7 in DIRS_5623160B)
            ]
            if len(x5) == ZERO:
                break
            x4.add(choice(tuple(x5)))
        if len(x4) != x3:
            continue
        x8 = max(x9[ZERO] for x9 in x4) - min(x9[ZERO] for x9 in x4) + ONE
        x10 = max(x11[ONE] for x11 in x4) - min(x11[ONE] for x11 in x4) + ONE
        if x8 * x10 > len(x4) * FOUR and len(x4) > THREE:
            continue
        return frozenset(shift(x4, anchor))
    return None


def _border_offset_5623160b(
    patch: Indices,
    direction: IntegerTuple,
    dim: int,
) -> IntegerTuple:
    if direction == UP:
        return toivec(invert(uppermost(patch)))
    if direction == DOWN:
        return toivec(subtract(dim - ONE, lowermost(patch)))
    if direction == LEFT:
        return tojvec(invert(leftmost(patch)))
    return tojvec(subtract(dim - ONE, rightmost(patch)))


def _input_object_ok_5623160b(
    patch: Indices,
    hub: Indices,
    others: set[IntegerTuple],
) -> bool:
    if len(intersection(patch, others)) > ZERO:
        return False
    x0 = ZERO
    for x1 in patch:
        for x2 in dneighbors(x1):
            if x2 in hub:
                x0 += ONE
            elif x2 in others:
                return False
    return x0 == ONE


def _output_object_ok_5623160b(
    patch: Indices,
    others: set[IntegerTuple],
) -> bool:
    if len(intersection(patch, others)) > ZERO:
        return False
    for x0 in patch:
        for x1 in dneighbors(x0):
            if x1 in others:
                return False
    return True


def generate_5623160b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, DIM_BOUNDS_5623160B)
        x1 = _grow_hub_5623160b(diff_lb, diff_ub, x0)
        x2 = _exposed_sides_5623160b(x1, x0)
        x3 = tuple({x4 for _, x4, _ in x2})
        x4 = min(OBJECT_COUNT_BOUNDS_5623160B[ONE], len(OBJECT_COLORS_5623160B), len(x2))
        if x4 < OBJECT_COUNT_BOUNDS_5623160B[ZERO]:
            continue
        x5 = unifint(diff_lb, diff_ub, (OBJECT_COUNT_BOUNDS_5623160B[ZERO], x4))
        x6 = list(sample(x3, min(THREE, len(x3))))
        shuffle(x6)
        x7 = sample(OBJECT_COLORS_5623160B, x5)
        x8 = []
        x9 = set()
        x10 = set()
        x11 = set()
        failed = False
        for x12 in range(x5):
            x13 = x6[x12] if x12 < len(x6) else None
            placed = False
            for _ in range(300):
                x14 = [
                    x15
                    for x15 in _exposed_sides_5623160b(x1, x0)
                    if x15[TWO] not in x1 and x15[TWO] not in x9 and x15[TWO] not in x11
                ]
                if x13 is not None:
                    x14 = [x15 for x15 in x14 if x15[ONE] == x13]
                if len(x14) == ZERO:
                    break
                _, x16, x17 = choice(tuple(x14))
                x18 = _random_patch_5623160b(diff_lb, diff_ub, x16, x17, x0)
                if x18 is None:
                    continue
                if not _input_object_ok_5623160b(x18, x1, x9):
                    continue
                x19 = shift(x18, _border_offset_5623160b(x18, x16, x0))
                if not _output_object_ok_5623160b(x19, x10):
                    continue
                x8.append((x7[x12], x16, x18, x19))
                x9 |= set(x18)
                x10 |= set(x19)
                x11.add(x17)
                placed = True
                break
            if not placed:
                failed = True
                break
        if failed:
            continue
        if len({x20 for _, x20, _, _ in x8}) < THREE:
            continue
        x21 = fill(canvas(BG_5623160B, (x0, x0)), HUB_5623160B, x1)
        x22 = fill(canvas(BG_5623160B, (x0, x0)), HUB_5623160B, x1)
        for x23, _, x24, x25 in x8:
            x21 = fill(x21, x23, x24)
            x22 = fill(x22, x23, x25)
        if equality(x21, x22):
            continue
        if verify_5623160b(x21) != x22:
            continue
        return {"input": x21, "output": x22}
