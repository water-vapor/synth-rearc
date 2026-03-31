from __future__ import annotations

from synth_rearc.core import *


def horizontal_run_7b80bb43(
    row: Integer,
    col_start: Integer,
    length: Integer,
) -> Indices:
    return frozenset((row, j) for j in range(col_start, col_start + length))


def vertical_run_7b80bb43(
    row_start: Integer,
    col: Integer,
    length: Integer,
) -> Indices:
    return frozenset((i, col) for i in range(row_start, row_start + length))


def staircase_row_7b80bb43(
    row: Integer,
    left_end: Integer,
    right_start: Integer,
    kind: str,
) -> Indices:
    x0 = right_start - left_end - ONE
    if x0 <= ONE:
        return frozenset({})
    if kind == "right":
        return frozenset((row + ONE + k, right_start - ONE - k) for k in range(x0 - ONE))
    return frozenset((row + ONE + k, left_end + ONE + k) for k in range(x0 - ONE))


def staircase_col_7b80bb43(
    top_end: Integer,
    bottom_start: Integer,
    col: Integer,
    side: str,
    anchor: str,
) -> Indices:
    x0 = bottom_start - top_end - ONE
    if x0 <= ONE:
        return frozenset({})
    if anchor == "top":
        if side == "left":
            return frozenset((top_end + ONE + k, col - ONE - k) for k in range(x0 - ONE))
        return frozenset((top_end + ONE + k, col + ONE + k) for k in range(x0 - ONE))
    if side == "left":
        return frozenset((bottom_start - ONE - k, col - ONE - k) for k in range(x0 - ONE))
    return frozenset((bottom_start - ONE - k, col + ONE + k) for k in range(x0 - ONE))


def diagonal_staircase_7b80bb43(
    patch: Indices,
) -> bool:
    x0 = len(patch)
    if x0 < TWO:
        return False
    x1 = sorted(patch)
    x2 = tuple(i for i, _ in x1)
    x3 = tuple(j for _, j in x1)
    if len(set(x2)) != x0 or len(set(x3)) != x0:
        return False
    if max(x2) - min(x2) != x0 - ONE:
        return False
    if max(x3) - min(x3) != x0 - ONE:
        return False
    x4 = tuple(x3[k + ONE] - x3[k] for k in range(x0 - ONE))
    return x4 == repeat(ONE, x0 - ONE) or x4 == repeat(NEG_ONE, x0 - ONE)


def stair_cells_7b80bb43(
    grid: Grid,
) -> tuple[Integer, Integer, frozenset[IntegerTuple]]:
    x0 = mostcolor(grid)
    x1 = other(palette(grid), x0)
    x2 = ofcolor(grid, x1)
    x3 = frozenset(
        x4
        for x4 in x2
        if len(intersection(dneighbors(x4), x2)) <= ONE
    )
    return x0, x1, x3


def diagonal_components_7b80bb43(
    patch: Indices,
) -> frozenset[Indices]:
    x0 = set()
    x1 = set(patch)
    for x2 in x1:
        for x3 in (ONE, NEG_ONE):
            x4 = (x2[ZERO] - ONE, x2[ONE] - x3)
            if x4 in x1:
                continue
            x5 = []
            x6 = x2
            while x6 in x1:
                x5.append(x6)
                x6 = (x6[ZERO] + ONE, x6[ONE] + x3)
            x7 = frozenset(x5)
            if diagonal_staircase_7b80bb43(x7):
                x0.add(x7)
    return frozenset(x0)


def reserve_with_margin_7b80bb43(
    patch: Indices,
    margin: Integer = ONE,
) -> Indices:
    if len(patch) == ZERO:
        return frozenset({})
    x0 = uppermost(patch) - margin
    x1 = lowermost(patch) + margin
    x2 = leftmost(patch) - margin
    x3 = rightmost(patch) + margin
    return frozenset(
        (i, j)
        for i in range(x0, x1 + ONE)
        for j in range(x2, x3 + ONE)
    )


def patch_in_bounds_7b80bb43(
    patch: Indices,
    dims: IntegerTuple,
) -> bool:
    x0, x1 = dims
    return all(ZERO <= i < x0 and ZERO <= j < x1 for i, j in patch)
