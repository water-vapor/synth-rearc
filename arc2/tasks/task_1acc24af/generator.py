from __future__ import annotations

from arc2.core import *

from .helpers import (
    GRID_SHAPE_1ACC24AF,
    blue_slots_1acc24af,
    normalize_indices_1acc24af,
    piece_matches_slot_1acc24af,
    rotations_1acc24af,
)
from .verifier import verify_1acc24af


SLOT_LIBRARY_1ACC24AF = (
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE), (ONE, TWO)}),
)

SLOT_POOL_1ACC24AF = (
    SLOT_LIBRARY_1ACC24AF[ZERO],
    SLOT_LIBRARY_1ACC24AF[ZERO],
    SLOT_LIBRARY_1ACC24AF[ZERO],
    SLOT_LIBRARY_1ACC24AF[ONE],
    SLOT_LIBRARY_1ACC24AF[TWO],
    SLOT_LIBRARY_1ACC24AF[THREE],
    SLOT_LIBRARY_1ACC24AF[THREE],
    SLOT_LIBRARY_1ACC24AF[FOUR],
    SLOT_LIBRARY_1ACC24AF[FOUR],
)


def _patch_key_1acc24af(
    patch: Patch,
) -> tuple[int, int, int, int, int]:
    return (uppermost(patch), leftmost(patch), height(patch), width(patch), size(patch))


def _sample_slots_1acc24af(
    top_row: Integer,
    slot_count: Integer,
) -> tuple[Indices, ...] | None:
    x0 = []
    for _ in range(200):
        if len(x0) == slot_count:
            break
        x1 = choice(SLOT_POOL_1ACC24AF)
        x2 = choice(rotations_1acc24af(x1))
        x3 = height(x2)
        x4 = width(x2)
        x5 = randint(top_row, top_row + THREE - x3)
        x6 = randint(ONE, 11 - x4)
        x7 = shift(x2, (x5, x6))
        x8 = any(manhattan(x7, x9) <= ONE for x9 in x0)
        if x8:
            continue
        x0.append(x7)
    if len(x0) != slot_count:
        return None
    return tuple(sorted(x0, key=_patch_key_1acc24af))


def _build_blue_1acc24af(
    top_row: Integer,
    slots: tuple[Indices, ...],
) -> Indices | None:
    x0 = tuple(x1[1] for x2 in slots for x1 in x2)
    x3 = min(x0)
    x4 = max(x0)
    x5 = x3 - randint(ONE, min(THREE, x3))
    x6 = x4 + randint(ONE, min(THREE, 11 - x4))
    x7 = set()
    for x8 in range(THREE):
        x9 = top_row + x8
        x10 = ZERO if x8 == TWO else randint(ZERO, TWO)
        x11 = ZERO if x8 == TWO else randint(ZERO, TWO)
        x12 = x5 + x10
        x13 = x6 - x11
        x14 = tuple(x15[1] for x16 in slots for x15 in x16 if x15[0] == x9)
        if len(x14) != ZERO:
            x12 = min(x12, min(x14) - ONE)
            x13 = max(x13, max(x14) + ONE)
        if x13 - x12 < TWO:
            return None
        x17 = frozenset((x9, x18) for x18 in range(x12, x13 + ONE))
        x19 = frozenset(x20 for x21 in slots for x20 in x21 if x20[0] == x9)
        x7 |= x17 - x19
    x22 = fill(canvas(ZERO, GRID_SHAPE_1ACC24AF), ONE, frozenset(x7))
    x23 = colorfilter(objects(x22, T, F, T), ONE)
    if len(x23) != ONE:
        return None
    x24 = frozenset(blue_slots_1acc24af(frozenset(x7)))
    if x24 != frozenset(slots):
        return None
    return frozenset(x7)


def _grow_matching_piece_1acc24af(
    slot_shape: Patch,
    max_height: Integer,
) -> Indices:
    x0 = set(normalize_indices_1acc24af(slot_shape))
    x1 = lowermost(x0)
    x2 = max_height - height(x0)
    x3 = min(FOUR, max(ZERO, x2))
    x4 = randint(ZERO, x3)
    x5 = size(x0) + x4
    while len(x0) < x5:
        x6 = set()
        for x7 in x0:
            for x8 in dneighbors(x7):
                if x8 in x0:
                    continue
                if x8[0] <= x1:
                    continue
                if x8[0] >= max_height:
                    continue
                x6.add(x8)
        if len(x6) == ZERO:
            break
        x0.add(choice(tuple(x6)))
    return normalize_indices_1acc24af(frozenset(x0))


def _random_piece_1acc24af(
    max_height: Integer,
) -> Indices:
    x0 = choice((THREE, FOUR, FOUR, FIVE, FIVE, SIX))
    x1 = {(ZERO, ZERO)}
    while len(x1) < x0:
        x2 = set()
        for x3 in x1:
            for x4 in dneighbors(x3):
                if x4 in x1:
                    continue
                if x4[0] < ZERO or x4[0] >= max_height:
                    continue
                if x4[1] < NEG_TWO or x4[1] > FOUR:
                    continue
                x2.add(x4)
        if len(x2) == ZERO:
            break
        x1.add(choice(tuple(x2)))
        x1 = set(normalize_indices_1acc24af(frozenset(x1)))
    return normalize_indices_1acc24af(frozenset(x1))


def _place_pieces_1acc24af(
    pieces: tuple[Indices, ...],
    bottom_top: Integer,
) -> tuple[Indices, ...] | None:
    x0 = []
    x1 = set()
    x2 = sorted(pieces, key=lambda x3: (-size(x3), -height(x3), -width(x3)))
    for x3 in x2:
        x4 = F
        for _ in range(200):
            x5 = choice(rotations_1acc24af(x3))
            x6 = height(x5)
            x7 = width(x5)
            if x6 > TEN - bottom_top + ONE:
                continue
            x8 = randint(bottom_top, TEN - x6 + ONE)
            x9 = randint(ZERO, 12 - x7)
            x10 = shift(x5, (x8, x9))
            x11 = set(x10)
            x12 = set(x11)
            for x13 in tuple(x11):
                x12 |= dneighbors(x13)
            if len(intersection(frozenset(x12), frozenset(x1))) != ZERO:
                continue
            x0.append(x10)
            x1 |= x11
            x4 = T
            break
        if not x4:
            return None
    return tuple(sorted(x0, key=_patch_key_1acc24af))


def generate_1acc24af(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (ONE, THREE))
        x1 = randint(ONE, FOUR)
        x2 = _sample_slots_1acc24af(x1, x0)
        if x2 is None:
            continue
        x3 = _build_blue_1acc24af(x1, x2)
        if x3 is None:
            continue
        x4 = blue_slots_1acc24af(x3)
        x5 = max(SEVEN, min(EIGHT, x1 + randint(FOUR, FIVE)))
        x6 = TEN - x5 + ONE
        x7 = max(x0, unifint(diff_lb, diff_ub, (ONE, THREE)))
        x8 = choice((ONE, ONE, TWO))
        x9 = []
        for _ in range(x7):
            x10 = normalize_indices_1acc24af(choice(x4))
            for _ in range(100):
                x11 = _grow_matching_piece_1acc24af(x10, x6)
                if piece_matches_slot_1acc24af(x3, x4, x11):
                    x9.append(x11)
                    break
            else:
                break
        if len(x9) != x7:
            continue
        x12 = []
        for _ in range(x8):
            for _ in range(200):
                x13 = _random_piece_1acc24af(x6)
                if height(x13) > x6 or width(x13) > FIVE:
                    continue
                if piece_matches_slot_1acc24af(x3, x4, x13):
                    continue
                x12.append(x13)
                break
            else:
                break
        if len(x12) != x8:
            continue
        x13 = tuple(x9 + x12)
        x14 = _place_pieces_1acc24af(x13, x5)
        if x14 is None:
            continue
        x15 = canvas(ZERO, GRID_SHAPE_1ACC24AF)
        x16 = fill(x15, ONE, x3)
        for x17 in x14:
            x16 = fill(x16, FIVE, x17)
        x18 = verify_1acc24af(x16)
        if equality(x16, x18):
            continue
        if colorcount(x18, FIVE) == ZERO:
            continue
        if colorcount(x18, TWO) == ZERO:
            continue
        return {"input": x16, "output": x18}
