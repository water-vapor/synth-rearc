from __future__ import annotations

from collections import deque

from synth_rearc.core import *


def orth_neighbors_477d2879(
    loc: IntegerTuple,
) -> tuple[IntegerTuple, IntegerTuple, IntegerTuple, IntegerTuple]:
    i, j = loc
    return ((i - ONE, j), (i + ONE, j), (i, j - ONE), (i, j + ONE))


def in_bounds_477d2879(
    shape0: IntegerTuple,
    loc: IntegerTuple,
) -> Boolean:
    i, j = loc
    return ZERO <= i < shape0[0] and ZERO <= j < shape0[1]


def white_neighbor_count_477d2879(
    white: Indices,
    loc: IntegerTuple,
) -> Integer:
    return sum(nbr in white for nbr in orth_neighbors_477d2879(loc))


def orth_degree_477d2879(
    indices: Indices,
    loc: IntegerTuple,
) -> Integer:
    return sum(nbr in indices for nbr in orth_neighbors_477d2879(loc))


def connected_components_477d2879(
    indices: Indices,
) -> tuple[Indices, ...]:
    remaining = set(indices)
    parts: list[Indices] = []
    while len(remaining) > ZERO:
        start = remaining.pop()
        part = {start}
        queue = deque((start,))
        while len(queue) > ZERO:
            loc = queue.popleft()
            for nbr in orth_neighbors_477d2879(loc):
                if nbr in remaining:
                    remaining.remove(nbr)
                    part.add(nbr)
                    queue.append(nbr)
        parts.append(frozenset(part))
    return tuple(sorted(parts, key=lambda patch: (uppermost(patch), leftmost(patch), size(patch))))


def turn_count_477d2879(
    indices: Indices,
) -> Integer:
    total = ZERO
    for loc in indices:
        nbrs = tuple(nbr for nbr in orth_neighbors_477d2879(loc) if nbr in indices)
        if len(nbrs) != TWO:
            continue
        a, b = nbrs
        if a[0] != b[0] and a[1] != b[1]:
            total += ONE
    return total


def has_2x2_477d2879(
    indices: Indices,
) -> Boolean:
    if len(indices) == ZERO:
        return F
    top = uppermost(indices)
    left = leftmost(indices)
    bottom = lowermost(indices)
    right = rightmost(indices)
    for i in range(top, bottom):
        for j in range(left, right):
            block = frozenset({(i, j), (i + ONE, j), (i, j + ONE), (i + ONE, j + ONE)})
            if block.issubset(indices):
                return T
    return F


def touches_border_477d2879(
    indices: Indices,
    shape0: IntegerTuple,
) -> Boolean:
    h, w = shape0
    return any(i in (ZERO, h - ONE) or j in (ZERO, w - ONE) for i, j in indices)


def rectangle_perimeter_477d2879(
    top: Integer,
    left: Integer,
    height: Integer,
    width: Integer,
) -> Indices:
    bottom = top + height - ONE
    right = left + width - ONE
    return box(frozenset({(top, left), (bottom, right)}))


def touches_existing_orthogonally_477d2879(
    patch: Indices,
    occupied: Indices,
) -> Boolean:
    return any(nbr in occupied for cell in patch for nbr in orth_neighbors_477d2879(cell))


def zero_regions_477d2879(
    white: Indices,
    shape0: IntegerTuple,
) -> tuple[Indices, ...]:
    h, w = shape0
    zeros = frozenset((i, j) for i in range(h) for j in range(w) if (i, j) not in white)
    return connected_components_477d2879(zeros)


def seedable_object_cells_477d2879(
    obj: Indices,
    white: Indices,
) -> tuple[IntegerTuple, ...]:
    return tuple(sorted(loc for loc in obj if white_neighbor_count_477d2879(white, loc) == TWO))


def seedable_background_cells_477d2879(
    region: Indices,
    white: Indices,
) -> tuple[IntegerTuple, ...]:
    return tuple(sorted(loc for loc in region if white_neighbor_count_477d2879(white, loc) < TWO))
