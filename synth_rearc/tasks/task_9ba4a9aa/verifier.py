from __future__ import annotations

from collections import deque

from synth_rearc.core import *


def _is_checker_9ba4a9aa(
    grid: Grid,
    origin: IntegerTuple,
    bg: Integer,
) -> Boolean:
    x0 = crop(grid, origin, (THREE, THREE))
    x1 = {x2 for x3 in x0 for x2 in x3}
    if bg in x1 or len(x1) != TWO:
        return False
    x2 = x0[0][0]
    x3 = x0[0][1]
    x4 = (
        (x2, x3, x2),
        (x3, x2, x3),
        (x2, x3, x2),
    )
    return x0 == x4


def _is_ring_9ba4a9aa(
    grid: Grid,
    origin: IntegerTuple,
    bg: Integer,
) -> Boolean:
    x0 = crop(grid, origin, (THREE, THREE))
    x1 = {x2 for x3 in x0 for x2 in x3}
    if bg in x1:
        return False
    x2 = tuple(
        x0[x3][x4]
        for x3 in range(THREE)
        for x4 in range(THREE)
        if (x3, x4) != (ONE, ONE)
    )
    return len(set(x2)) == ONE and x0[ONE][ONE] != x2[ZERO]


def _scan_blocks_9ba4a9aa(
    grid: Grid,
    bg: Integer,
) -> tuple[IntegerTuple, tuple[IntegerTuple, ...]]:
    x0 = []
    x1 = None
    for x2 in range(len(grid) - TWO):
        for x3 in range(len(grid[0]) - TWO):
            x4 = (x2, x3)
            if _is_checker_9ba4a9aa(grid, x4, bg):
                x1 = x4
            elif _is_ring_9ba4a9aa(grid, x4, bg):
                x0.append(x4)
    return x1, tuple(x0)


def _checker_seed_9ba4a9aa(
    grid: Grid,
    checker_origin: IntegerTuple,
    bg: Integer,
) -> tuple[Integer, IntegerTuple]:
    x0, x1 = checker_origin
    x2 = {(x0 + x3, x1 + x4) for x3 in range(THREE) for x4 in range(THREE)}
    for x3 in x2:
        for x4 in dneighbors(x3):
            x5 = index(grid, x4)
            if x4 in x2:
                continue
            if x5 is None or x5 == bg:
                continue
            return x5, x4
    raise ValueError("checkerboard marker has no outgoing path")


def _dotted_component_9ba4a9aa(
    grid: Grid,
    color_value: Integer,
    start: IntegerTuple,
) -> frozenset[IntegerTuple]:
    x0 = ofcolor(grid, color_value)
    x1 = deque([start])
    x2 = {start}
    while len(x1) > ZERO:
        x3, x4 = x1.popleft()
        for x5 in ((x3 - TWO, x4), (x3 + TWO, x4), (x3, x4 - TWO), (x3, x4 + TWO)):
            if x5 not in x0 or x5 in x2:
                continue
            x2.add(x5)
            x1.append(x5)
    return frozenset(x2)


def _touches_ring_9ba4a9aa(
    component: frozenset[IntegerTuple],
    ring_origin: IntegerTuple,
) -> Boolean:
    x0, x1 = ring_origin
    x2 = {(x0 + x3, x1 + x4) for x3 in range(THREE) for x4 in range(THREE)}
    for x3 in component:
        if len(intersection(dneighbors(x3), x2)) > ZERO:
            return True
    return False


def verify_9ba4a9aa(
    I: Grid,
) -> Grid:
    x0 = mostcolor(I)
    x1, x2 = _scan_blocks_9ba4a9aa(I, x0)
    x3, x4 = _checker_seed_9ba4a9aa(I, x1, x0)
    x5 = _dotted_component_9ba4a9aa(I, x3, x4)
    x6 = extract(x2, lambda x7: _touches_ring_9ba4a9aa(x5, x7))
    x7 = crop(I, x6, (THREE, THREE))
    return x7
