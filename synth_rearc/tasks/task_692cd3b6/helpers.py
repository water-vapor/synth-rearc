from __future__ import annotations

from collections import deque

from synth_rearc.core import *


FrameRecord692cd3b6 = tuple[IntegerTuple, IntegerTuple, IntegerTuple]
DIHEDRAL_TRANSFORMS_692cd3b6 = (
    identity,
    rot90,
    rot180,
    rot270,
    hmirror,
    vmirror,
    dmirror,
    cmirror,
)
ORTHOGONAL_DIRECTIONS_692cd3b6 = (
    (-ONE, ZERO),
    (ONE, ZERO),
    (ZERO, -ONE),
    (ZERO, ONE),
)


def sign_692cd3b6(n: Integer) -> Integer:
    return (n > ZERO) - (n < ZERO)


def frame_cells_692cd3b6(
    center: IntegerTuple,
    direction: IntegerTuple,
) -> Object:
    ci, cj = center
    di, dj = direction
    x0 = frozenset(
        (TWO, (ci + oi, cj + oj))
        for oi in (-ONE, ZERO, ONE)
        for oj in (-ONE, ZERO, ONE)
        if (oi, oj) != ORIGIN and (oi, oj) != (di, dj)
    )
    return x0 | frozenset({(FIVE, center)})


def frame_records_692cd3b6(
    I: Grid,
) -> tuple[FrameRecord692cd3b6, FrameRecord692cd3b6]:
    x0 = tuple(sorted(ofcolor(I, FIVE)))
    x1 = []
    for x2 in x0:
        for x3 in ORTHOGONAL_DIRECTIONS_692cd3b6:
            x4 = add(x2, x3)
            if index(I, x4) != ZERO:
                continue
            x5 = add(x4, x3)
            x1.append((x2, x4, x5))
            break
    return tuple(sorted(x1, key=lambda x6: (x6[2][0], x6[2][1], x6[0][0], x6[0][1])))


def monotone_reach_692cd3b6(
    I: Grid,
    seeds: tuple[IntegerTuple, ...] | frozenset[IntegerTuple],
    directions: tuple[IntegerTuple, ...],
) -> Indices:
    h, w = shape(I)
    x0 = tuple(x1 for x1 in directions if x1 != ORIGIN)
    x2 = deque()
    x3 = set()
    for x4 in seeds:
        i, j = x4
        if not (ZERO <= i < h and ZERO <= j < w):
            continue
        if index(I, x4) != ZERO:
            continue
        if x4 in x3:
            continue
        x3.add(x4)
        x2.append(x4)
    while len(x2) > ZERO:
        x5 = x2.popleft()
        for x6 in x0:
            x7 = add(x5, x6)
            i, j = x7
            if not (ZERO <= i < h and ZERO <= j < w):
                continue
            if x7 in x3:
                continue
            if index(I, x7) != ZERO:
                continue
            x3.add(x7)
            x2.append(x7)
    return frozenset(x3)


def connector_directions_692cd3b6(
    record: FrameRecord692cd3b6,
    other_external: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    _, opening, external = record
    x0 = subtract(external, opening)
    x1 = subtract(other_external, opening)
    if x0[0] != ZERO:
        x2 = (ZERO, sign_692cd3b6(x1[1]))
    else:
        x2 = (sign_692cd3b6(x1[0]), ZERO)
    return tuple(x3 for x3 in (x0, x2) if x3 != ORIGIN)
