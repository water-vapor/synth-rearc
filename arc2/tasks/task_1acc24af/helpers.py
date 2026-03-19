from __future__ import annotations

from arc2.core import *


GRID_SHAPE_1ACC24AF = (12, 12)


def _connected_indices_1acc24af(
    patch: Patch,
) -> tuple[Indices, ...]:
    x0 = set(toindices(patch))
    x1 = []
    while x0:
        x2 = x0.pop()
        x3 = {x2}
        x4 = [x2]
        while x4:
            x5 = x4.pop()
            for x6 in dneighbors(x5):
                if x6 in x0:
                    x0.remove(x6)
                    x3.add(x6)
                    x4.append(x6)
        x1.append(frozenset(x3))
    x7 = lambda x8: (uppermost(x8), leftmost(x8), height(x8), width(x8), size(x8))
    return tuple(sorted(x1, key=x7))


def normalize_indices_1acc24af(
    patch: Patch,
) -> Indices:
    x0 = frozenset(toindices(patch))
    if len(x0) == ZERO:
        return x0
    return frozenset(normalize(x0))


def rotations_1acc24af(
    patch: Patch,
) -> tuple[Indices, ...]:
    x0 = normalize_indices_1acc24af(patch)
    if len(x0) == ZERO:
        return (x0,)
    x1 = []
    x2 = x0
    for _ in range(FOUR):
        x2 = normalize_indices_1acc24af(x2)
        if x2 not in x1:
            x1.append(x2)
        x3 = height(x2)
        x2 = frozenset((x4[1], x3 - ONE - x4[0]) for x4 in x2)
    return tuple(x1)


def blue_slots_1acc24af(
    blue: Patch,
) -> tuple[Indices, ...]:
    x0 = toindices(blue)
    if len(x0) == ZERO:
        return ()
    x1 = tuple(sorted({x2[0] for x2 in x0}))
    x2 = set()
    for x3 in x1:
        x4 = sorted(x5[1] for x5 in x0 if x5[0] == x3)
        if len(x4) < TWO:
            continue
        for x5 in range(x4[0], x4[-1] + ONE):
            x6 = (x3, x5)
            if x6 not in x0:
                x2.add(x6)
    return _connected_indices_1acc24af(frozenset(x2))


def piece_matches_slot_1acc24af(
    blue: Patch,
    slots: tuple[Indices, ...],
    piece: Patch,
) -> Boolean:
    x0 = toindices(blue)
    if len(x0) == ZERO or len(slots) == ZERO:
        return F
    x1 = lowermost(x0)
    x2 = rotations_1acc24af(piece)
    for x3 in slots:
        x4 = tuple(x3)
        for x5 in x2:
            x6 = tuple(x5)
            for x7 in x4:
                for x8 in x6:
                    x9 = subtract(x7, x8)
                    x10 = shift(x5, x9)
                    if not x3.issubset(x10):
                        continue
                    if len(intersection(x10, x0)) != ZERO:
                        continue
                    x11 = difference(x10, x3)
                    if all(x12[0] > x1 for x12 in x11):
                        return T
    return F
