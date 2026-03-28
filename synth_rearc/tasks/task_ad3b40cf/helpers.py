from __future__ import annotations

from synth_rearc.core import *


AXIS_KINDS_ad3b40cf = ("vertical", "horizontal", "diagonal", "counterdiagonal")
COLOR_POOL_ad3b40cf = (TWO, THREE, FOUR, FIVE, SIX, SEVEN, NINE)


def axis_patch_ad3b40cf(
    size_value: Integer,
    axis_kind: str,
) -> Indices:
    x0 = size_value - ONE
    x1 = size_value // TWO
    if axis_kind == "vertical":
        return connect((ZERO, x1), (x0, x1))
    if axis_kind == "horizontal":
        return connect((x1, ZERO), (x1, x0))
    if axis_kind == "diagonal":
        return connect((ZERO, ZERO), (x0, x0))
    return connect((ZERO, x0), (x0, ZERO))


def axis_metric_ad3b40cf(
    cell: IntegerTuple,
    size_value: Integer,
    axis_kind: str,
) -> Integer:
    i, j = cell
    x0 = size_value // TWO
    if axis_kind == "vertical":
        return j - x0
    if axis_kind == "horizontal":
        return i - x0
    if axis_kind == "diagonal":
        return i - j
    return i + j - (size_value - ONE)


def cell_on_source_side_ad3b40cf(
    cell: IntegerTuple,
    size_value: Integer,
    axis_kind: str,
    source_side: Integer,
) -> Boolean:
    return axis_metric_ad3b40cf(cell, size_value, axis_kind) * source_side > ONE


def mirror_patch_ad3b40cf(
    patch: Patch,
    size_value: Integer,
    axis_kind: str,
) -> Indices:
    x0 = size_value - ONE
    if axis_kind == "vertical":
        return frozenset((i, x0 - j) for i, j in toindices(patch))
    if axis_kind == "horizontal":
        return frozenset((x0 - i, j) for i, j in toindices(patch))
    if axis_kind == "diagonal":
        return frozenset((j, i) for i, j in toindices(patch))
    return frozenset((x0 - j, x0 - i) for i, j in toindices(patch))


def padded_backdrop_ad3b40cf(
    patch: Patch,
    size_value: Integer,
) -> Indices:
    if len(patch) == ZERO:
        return frozenset({})
    x0 = max(ZERO, uppermost(patch) - ONE)
    x1 = min(size_value - ONE, lowermost(patch) + ONE)
    x2 = max(ZERO, leftmost(patch) - ONE)
    x3 = min(size_value - ONE, rightmost(patch) + ONE)
    return frozenset((i, j) for i in range(x0, x1 + ONE) for j in range(x2, x3 + ONE))


def _candidate_boxes_ad3b40cf(
    size_value: Integer,
    axis_kind: str,
    source_side: Integer,
    blocked: Patch,
    dims: IntegerTuple,
) -> tuple[Indices, ...]:
    h, w = dims
    boxes = []
    rows = range(size_value - h + ONE)
    cols = range(size_value - w + ONE)
    for i in rows:
        for j in cols:
            x0 = frozenset((a, b) for a in range(i, i + h) for b in range(j, j + w))
            if len(intersection(x0, blocked)) > ZERO:
                continue
            if not all(cell_on_source_side_ad3b40cf(cell, size_value, axis_kind, source_side) for cell in x0):
                continue
            boxes.append(x0)
    return tuple(boxes)


def _sample_connected_subset_ad3b40cf(
    box: Indices,
    cell_count: Integer,
) -> Indices | None:
    x0 = tuple(sorted(box))
    for _ in range(120):
        x1 = {choice(x0)}
        while len(x1) < cell_count:
            x2 = sorted(
                {
                    nbr
                    for cell in x1
                    for nbr in dneighbors(cell)
                    if nbr in box and nbr not in x1
                }
            )
            if len(x2) == ZERO:
                break
            x1.add(choice(x2))
        if len(x1) != cell_count:
            continue
        x3 = frozenset(x1)
        if cell_count > THREE and (height(x3) == ONE or width(x3) == ONE):
            continue
        return x3
    return None


def sample_compact_patch_ad3b40cf(
    size_value: Integer,
    axis_kind: str,
    source_side: Integer,
    blocked: Patch,
    diff_lb: float,
    diff_ub: float,
    cell_bounds: tuple[Integer, Integer],
) -> Indices | None:
    x0 = unifint(diff_lb, diff_ub, cell_bounds)
    x1 = [
        (h, w)
        for h in range(ONE, FIVE)
        for w in range(ONE, FIVE)
        if x0 <= h * w and not (h == ONE and w == ONE and x0 > ONE)
    ]
    shuffle(x1)
    for dims in x1:
        x2 = _candidate_boxes_ad3b40cf(size_value, axis_kind, source_side, blocked, dims)
        if len(x2) == ZERO:
            continue
        for _ in range(40):
            x3 = choice(x2)
            x4 = _sample_connected_subset_ad3b40cf(x3, x0)
            if x4 is None:
                continue
            return x4
    return None
