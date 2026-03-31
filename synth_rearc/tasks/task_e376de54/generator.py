from __future__ import annotations

from synth_rearc.core import *

from .helpers import STEP_BY_ORIENTATION_E376DE54
from .helpers import segment_patch_e376de54


GRID_SIZE_E376DE54 = 16
GRID_SHAPE_E376DE54 = (GRID_SIZE_E376DE54, GRID_SIZE_E376DE54)
FG_COLORS_E376DE54 = (ONE, TWO, THREE, FIVE, SIX, EIGHT, NINE)
ORIENTATION_CHOICES_E376DE54 = (
    "horizontal",
    "vertical",
    "diag_anti",
    "diag_anti",
)


def _spaced_positions_e376de54(
    count_value: Integer,
    low: Integer,
    high: Integer,
) -> tuple[Integer, ...]:
    x0 = [TWO for _ in range(count_value - ONE)]
    x1 = max(ZERO, subtract(subtract(high, low), sum(x0)))
    x2 = min(count_value - ONE, x1)
    x3 = randint(ZERO, x2)
    x4 = tuple(sample(interval(ZERO, count_value - ONE, ONE), x3)) if x3 > ZERO else ()
    for x5 in x4:
        x0[x5] = THREE
    x6 = randint(low, subtract(high, sum(x0)))
    x7 = [x6]
    for x8 in x0:
        x7.append(x7[-ONE] + x8)
    return tuple(x7)


def _color_runs_e376de54(
    count_value: Integer,
) -> tuple[Integer, ...]:
    x0 = min(count_value, choice((ONE, TWO, TWO, THREE)))
    x1 = tuple(sample(FG_COLORS_E376DE54, x0))
    if x0 == ONE:
        return repeat(first(x1), count_value)
    x2 = tuple(sorted(sample(interval(ONE, count_value, ONE), x0 - ONE)))
    x3 = []
    x4 = ZERO
    for x5 in x2:
        x3.append(x5 - x4)
        x4 = x5
    x3.append(count_value - x4)
    x6 = []
    for x7, x8 in pair(x1, tuple(x3)):
        x6.extend(repeat(x7, x8))
    return tuple(x6)


def _max_length_e376de54(
    anchor: IntegerTuple,
    orientation: str,
    anchor_side: str,
) -> Integer:
    x0 = STEP_BY_ORIENTATION_E376DE54[orientation]
    x1 = x0 if anchor_side == "start" else invert(x0)
    x2, x3 = anchor
    x4, x5 = x1
    x6 = ZERO
    while both(
        both(0 <= x2 < GRID_SIZE_E376DE54, 0 <= x3 < GRID_SIZE_E376DE54),
        T,
    ):
        x6 = increment(x6)
        x2 = add(x2, x4)
        x3 = add(x3, x5)
    return x6


def _lengths_e376de54(
    anchors: tuple[IntegerTuple, ...],
    orientation: str,
    anchor_side: str,
    target_length: Integer,
) -> tuple[Integer, ...]:
    x0 = len(anchors)
    x1 = x0 // TWO
    x2 = []
    x3 = F
    for x4, x5 in enumerate(anchors):
        if x4 == x1:
            x2.append(target_length)
            continue
        x6 = _max_length_e376de54(x5, orientation, anchor_side)
        x7 = max(TWO, target_length - THREE)
        x8 = min(x6, target_length + THREE)
        x9 = tuple(x10 for x10 in range(x7, x8 + ONE) if x10 != target_length)
        if len(x9) == ZERO:
            x2.append(target_length)
            continue
        x10 = choice(x9)
        x2.append(x10)
        x3 = T
    if x3:
        return tuple(x2)
    for x4, x5 in enumerate(anchors):
        if x4 == x1:
            continue
        x6 = _max_length_e376de54(x5, orientation, anchor_side)
        x7 = tuple(x8 for x8 in range(TWO, x6 + ONE) if x8 != target_length)
        if len(x7) == ZERO:
            continue
        x2[x4] = choice(x7)
        return tuple(x2)
    return tuple(x2)


def _horizontal_layout_e376de54(
    count_value: Integer,
    target_length: Integer,
    anchor_side: str,
) -> tuple[IntegerTuple, ...]:
    x0 = _spaced_positions_e376de54(count_value, ZERO, GRID_SIZE_E376DE54 - ONE)
    if anchor_side == "start":
        x1 = randint(ZERO, GRID_SIZE_E376DE54 - target_length)
    else:
        x1 = randint(target_length - ONE, GRID_SIZE_E376DE54 - ONE)
    return tuple((x2, x1) for x2 in x0)


def _vertical_layout_e376de54(
    count_value: Integer,
    target_length: Integer,
    anchor_side: str,
) -> tuple[IntegerTuple, ...]:
    x0 = _spaced_positions_e376de54(count_value, ZERO, GRID_SIZE_E376DE54 - ONE)
    if anchor_side == "start":
        x1 = randint(ZERO, GRID_SIZE_E376DE54 - target_length)
    else:
        x1 = randint(target_length - ONE, GRID_SIZE_E376DE54 - ONE)
    return tuple((x1, x2) for x2 in x0)


def _antidiag_layout_e376de54(
    count_value: Integer,
    target_length: Integer,
    anchor_side: str,
) -> tuple[IntegerTuple, ...]:
    x0 = multiply(TWO, count_value - ONE)
    x1 = []
    for x2 in range(-TEN, TEN + ONE):
        if anchor_side == "start":
            x3 = max(ZERO, add(x2, target_length - ONE))
            x4 = min(GRID_SIZE_E376DE54 - target_length, add(GRID_SIZE_E376DE54 - ONE, x2))
        else:
            x3 = max(target_length - ONE, x2)
            x4 = min(GRID_SIZE_E376DE54 - ONE, add(x2, GRID_SIZE_E376DE54 - target_length))
        if subtract(x4, x3) >= x0:
            x1.append((x2, x3, x4))
    x2, x3, x4 = choice(tuple(x1))
    x5 = _spaced_positions_e376de54(count_value, x3, x4)
    return tuple((x6, subtract(x6, x2)) for x6 in x5)


def _anchors_e376de54(
    orientation: str,
    count_value: Integer,
    target_length: Integer,
    anchor_side: str,
) -> tuple[IntegerTuple, ...]:
    if orientation == "horizontal":
        return _horizontal_layout_e376de54(count_value, target_length, anchor_side)
    if orientation == "vertical":
        return _vertical_layout_e376de54(count_value, target_length, anchor_side)
    return _antidiag_layout_e376de54(count_value, target_length, anchor_side)


def generate_e376de54(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(ORIENTATION_CHOICES_E376DE54)
        x1 = choice((THREE, FIVE, FIVE))
        x2 = choice(("start", "end"))
        x3 = unifint(diff_lb, diff_ub, (FOUR, SEVEN))
        if x0 == "diag_anti":
            x3 = min(x3, SIX)
        x4 = _anchors_e376de54(x0, x1, x3, x2)
        x5 = _color_runs_e376de54(x1)
        x6 = _lengths_e376de54(x4, x0, x2, x3)
        x7 = canvas(SEVEN, GRID_SHAPE_E376DE54)
        x8 = x7
        for x9, x10, x11 in zip(x5, x4, x6):
            x12 = segment_patch_e376de54(x10, x0, x3, x2)
            x13 = segment_patch_e376de54(x10, x0, x11, x2)
            x7 = fill(x7, x9, x13)
            x8 = fill(x8, x9, x12)
        if x7 == x8:
            continue
        return {
            "input": x7,
            "output": x8,
        }
