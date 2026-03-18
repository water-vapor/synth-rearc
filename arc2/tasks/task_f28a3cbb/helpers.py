from __future__ import annotations

from arc2.core import *


def _step_component_f28a3cbb(
    value: Integer,
    lower: Integer,
    upper: Integer,
) -> Integer:
    if value < lower:
        return ONE
    if value > upper:
        return NEG_ONE
    return ZERO


def landing_cell_f28a3cbb(
    source: IntegerTuple,
    anchor: Patch,
    dims: IntegerTuple | None = None,
) -> IntegerTuple | None:
    anchor_cells = toindices(anchor)
    if source in anchor_cells:
        return None
    step = (
        _step_component_f28a3cbb(source[0], uppermost(anchor_cells), lowermost(anchor_cells)),
        _step_component_f28a3cbb(source[1], leftmost(anchor_cells), rightmost(anchor_cells)),
    )
    if step == ORIGIN:
        return None
    patch = frozenset({source})
    if adjacent(patch, anchor_cells):
        return None
    limit = 30 if dims is None else multiply(maximum(dims), TWO)
    for _ in range(limit):
        patch = shift(patch, step)
        loc = first(patch)
        if dims is not None:
            h, w = dims
            if not (ZERO <= loc[0] < h and ZERO <= loc[1] < w):
                return None
        if len(intersection(patch, anchor_cells)) > ZERO:
            return None
        if adjacent(patch, anchor_cells):
            return loc
    return None


def landing_to_anchor_f28a3cbb(
    source: IntegerTuple,
    anchor: Patch,
) -> IntegerTuple:
    landing = landing_cell_f28a3cbb(source, anchor)
    if landing is None:
        raise ValueError(f"invalid f28a3cbb source: {source}")
    return landing


def is_diagonal_source_f28a3cbb(
    source: IntegerTuple,
    anchor: Patch,
) -> Boolean:
    anchor_cells = toindices(anchor)
    outside_rows = source[0] < uppermost(anchor_cells) or source[0] > lowermost(anchor_cells)
    outside_cols = source[1] < leftmost(anchor_cells) or source[1] > rightmost(anchor_cells)
    return both(outside_rows, outside_cols)


def candidate_sources_by_landing_f28a3cbb(
    anchor: Patch,
    dims: IntegerTuple,
    blocked: Indices = frozenset(),
) -> dict[IntegerTuple, tuple[IntegerTuple, ...]]:
    h, w = dims
    groups: dict[IntegerTuple, list[IntegerTuple]] = {}
    anchor_cells = toindices(anchor)
    for i in range(h):
        for j in range(w):
            cell = (i, j)
            if cell in blocked or cell in anchor_cells:
                continue
            landing = landing_cell_f28a3cbb(cell, anchor, dims)
            if landing is None:
                continue
            groups.setdefault(landing, []).append(cell)
    return {landing: tuple(sorted(cells)) for landing, cells in groups.items()}
