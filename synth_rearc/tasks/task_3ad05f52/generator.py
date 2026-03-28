from synth_rearc.core import *

from .verifier import verify_3ad05f52


_FILL_COLORS_3AD05F52 = (TWO, THREE, FOUR, SIX)
_VERTICAL_3AD05F52 = "vertical"
_HORIZONTAL_3AD05F52 = "horizontal"
_TOP_3AD05F52 = "top"
_BOTTOM_3AD05F52 = "bottom"
_LEFT_3AD05F52 = "left"
_RIGHT_3AD05F52 = "right"


def _rect_patch_3ad05f52(
    top: Integer,
    left: Integer,
    height: Integer,
    width: Integer,
) -> frozenset[tuple[Integer, Integer]]:
    return frozenset(
        (i, j)
        for i in range(top, top + height)
        for j in range(left, left + width)
    )


def _cell_origin_3ad05f52(
    row: Integer,
    col: Integer,
    cell_size: Integer,
) -> tuple[Integer, Integer]:
    step = cell_size + ONE
    return row * step, col * step


def _cell_interior_3ad05f52(
    row: Integer,
    col: Integer,
    cell_size: Integer,
    top: Integer = ZERO,
    left: Integer = ZERO,
) -> frozenset[tuple[Integer, Integer]]:
    base_top, base_left = _cell_origin_3ad05f52(row, col, cell_size)
    return _rect_patch_3ad05f52(
        top + base_top + ONE,
        left + base_left + ONE,
        cell_size,
        cell_size,
    )


def _cell_border_3ad05f52(
    row: Integer,
    col: Integer,
    cell_size: Integer,
    top: Integer = ZERO,
    left: Integer = ZERO,
) -> frozenset[tuple[Integer, Integer]]:
    base_top, base_left = _cell_origin_3ad05f52(row, col, cell_size)
    base_top += top
    base_left += left
    bottom = base_top + cell_size + ONE
    right = base_left + cell_size + ONE
    top_edge = connect((base_top, base_left), (base_top, right))
    bottom_edge = connect((bottom, base_left), (bottom, right))
    left_edge = connect((base_top, base_left), (bottom, base_left))
    right_edge = connect((base_top, right), (bottom, right))
    return frozenset(top_edge | bottom_edge | left_edge | right_edge)


def _door_patch_3ad05f52(
    cell_a: tuple[Integer, Integer],
    cell_b: tuple[Integer, Integer],
    cell_size: Integer,
    top: Integer = ZERO,
    left: Integer = ZERO,
) -> frozenset[tuple[Integer, Integer]]:
    r0, c0 = cell_a
    r1, c1 = cell_b
    step = cell_size + ONE
    if r0 == r1:
        row = top + r0 * step + step // TWO
        col = left + min(c0, c1) * step + step
        return frozenset({(row, col)})
    row = top + min(r0, r1) * step + step
    col = left + c0 * step + step // TWO
    return frozenset({(row, col)})


def _outer_opening_3ad05f52(
    cell: tuple[Integer, Integer],
    side: str,
    cell_size: Integer,
    top: Integer = ZERO,
    left: Integer = ZERO,
) -> frozenset[tuple[Integer, Integer]]:
    row, col = cell
    step = cell_size + ONE
    base_top, base_left = _cell_origin_3ad05f52(row, col, cell_size)
    base_top += top
    base_left += left
    if side == _LEFT_3AD05F52:
        return frozenset({(base_top + step // TWO, base_left)})
    if side == _RIGHT_3AD05F52:
        return frozenset({(base_top + step // TWO, base_left + step)})
    if side == _TOP_3AD05F52:
        return frozenset({(base_top, base_left + step // TWO)})
    return frozenset({(base_top + step, base_left + step // TWO)})


def _neighbors_3ad05f52(
    cell: tuple[Integer, Integer],
    nrows: Integer,
    ncols: Integer,
) -> tuple[tuple[Integer, Integer], ...]:
    row, col = cell
    out = []
    for dr, dc in ((-ONE, ZERO), (ONE, ZERO), (ZERO, -ONE), (ZERO, ONE)):
        nr, nc = row + dr, col + dc
        if ZERO <= nr < nrows and ZERO <= nc < ncols:
            out.append((nr, nc))
    return tuple(out)


def _all_cells_3ad05f52(
    nrows: Integer,
    ncols: Integer,
) -> tuple[tuple[Integer, Integer], ...]:
    return tuple((row, col) for row in range(nrows) for col in range(ncols))


def _all_edges_3ad05f52(
    nrows: Integer,
    ncols: Integer,
) -> tuple[frozenset[tuple[Integer, Integer]], ...]:
    seen = set()
    out = []
    for cell in _all_cells_3ad05f52(nrows, ncols):
        for nei in _neighbors_3ad05f52(cell, nrows, ncols):
            edge = frozenset((cell, nei))
            if edge in seen:
                continue
            seen.add(edge)
            out.append(edge)
    return tuple(out)


def _reachable_cells_3ad05f52(
    cells: tuple[tuple[Integer, Integer], ...],
    edges: frozenset[frozenset[tuple[Integer, Integer]]],
    starts: tuple[tuple[Integer, Integer], ...],
) -> frozenset[tuple[Integer, Integer]]:
    edge_map: dict[tuple[Integer, Integer], set[tuple[Integer, Integer]]] = {
        cell: set() for cell in cells
    }
    for edge in edges:
        a, b = tuple(edge)
        edge_map[a].add(b)
        edge_map[b].add(a)
    seen = set(starts)
    queue = list(starts)
    while queue:
        cell = queue.pop()
        for nei in edge_map[cell]:
            if nei not in seen:
                seen.add(nei)
                queue.append(nei)
    return frozenset(seen)


def _side_cells_3ad05f52(
    nrows: Integer,
    ncols: Integer,
    side: str,
) -> tuple[tuple[Integer, Integer], ...]:
    if side == _LEFT_3AD05F52:
        return tuple((row, ZERO) for row in range(nrows))
    if side == _RIGHT_3AD05F52:
        return tuple((row, ncols - ONE) for row in range(nrows))
    if side == _TOP_3AD05F52:
        return tuple((ZERO, col) for col in range(ncols))
    return tuple((nrows - ONE, col) for col in range(ncols))


def _sample_component_3ad05f52(
    nrows: Integer,
    ncols: Integer,
    diff_lb: float,
    diff_ub: float,
    side: str | None,
) -> dict:
    cells = _all_cells_3ad05f52(nrows, ncols)
    edges = _all_edges_3ad05f52(nrows, ncols)
    side_cells = _side_cells_3ad05f52(nrows, ncols, side) if side is not None else cells
    door_lb = max(ONE, len(edges) // FOUR)
    door_ub = max(door_lb, len(edges) // TWO)
    while True:
        open_edges = frozenset(
            sample(edges, unifint(diff_lb, diff_ub, (door_lb, door_ub)))
        )
        anchor = choice(side_cells)
        reachable = _reachable_cells_3ad05f52(cells, open_edges, (anchor,))
        if len(reachable) < TWO:
            continue
        seed_pool = tuple(cell for cell in reachable if cell != anchor)
        if not seed_pool:
            continue
        return {
            "nrows": nrows,
            "ncols": ncols,
            "cells": cells,
            "open_edges": open_edges,
            "anchor": anchor,
            "seed": choice(seed_pool),
            "side": side,
        }


def _paint_component_3ad05f52(
    grid: Grid,
    component: dict,
    top: Integer,
    left: Integer,
    cell_size: Integer,
    color: Integer,
    include_opening: Boolean,
) -> Grid:
    out = grid
    for cell in component["cells"]:
        out = fill(out, EIGHT, _cell_border_3ad05f52(*cell, cell_size, top, left))
    for edge in component["open_edges"]:
        a, b = tuple(edge)
        out = fill(out, ZERO, _door_patch_3ad05f52(a, b, cell_size, top, left))
    if include_opening and component["side"] is not None:
        out = fill(
            out,
            ZERO,
            _outer_opening_3ad05f52(
                component["anchor"],
                component["side"],
                cell_size,
                top,
                left,
            ),
        )
    return fill(
        out,
        color,
        _cell_interior_3ad05f52(*component["seed"], cell_size, top, left),
    )


def _component_count_3ad05f52(
    grid: Grid,
    target: Integer,
) -> Integer:
    cells = {
        (i, j)
        for i, row in enumerate(grid)
        for j, value in enumerate(row)
        if value == target
    }
    count = ZERO
    while cells:
        root = next(iter(cells))
        seen = {root}
        queue = [root]
        while queue:
            cell = queue.pop()
            for nei in _neighbors_3ad05f52(cell, len(grid), len(grid[ZERO])):
                if nei in cells and nei not in seen:
                    seen.add(nei)
                    queue.append(nei)
        cells.difference_update(seen)
        count += ONE
    return count


def _color_of_3ad05f52(grid: Grid) -> Integer:
    return next(
        value
        for row in grid
        for value in row
        if value not in (ZERO, EIGHT)
    )


def _gap_strip_3ad05f52(
    dims: tuple[Integer, Integer],
    orientation: str,
    top_a: Integer,
    left_a: Integer,
    nrows_a: Integer,
    ncols_a: Integer,
    top_b: Integer,
    left_b: Integer,
    nrows_b: Integer,
    ncols_b: Integer,
    cell_size: Integer,
) -> frozenset[tuple[Integer, Integer]]:
    step = cell_size + ONE
    if orientation == _HORIZONTAL_3AD05F52:
        start = left_a + ncols_a * step + ONE
        stop = left_b
        if start >= stop:
            return frozenset()
        return frozenset(
            (row, col)
            for row in range(dims[ZERO])
            for col in range(start, stop)
        )
    start = top_a + nrows_a * step + ONE
    stop = top_b
    if start >= stop:
        return frozenset()
    return frozenset(
        (row, col)
        for row in range(start, stop)
        for col in range(dims[ONE])
    )


def _gap_stats_3ad05f52(
    gi: Grid,
    go: Grid,
    gap: frozenset[tuple[Integer, Integer]],
    color: Integer,
) -> tuple[Integer, Integer, Integer]:
    added = {
        cell
        for cell in gap
        if gi[cell[ZERO]][cell[ONE]] == ZERO and go[cell[ZERO]][cell[ONE]] == color
    }
    if not added:
        return ZERO, ZERO, ZERO
    rowmax = max(
        sum(ONE for cell in added if cell[ZERO] == row)
        for row in range(len(gi))
    )
    colmax = max(
        sum(ONE for cell in added if cell[ONE] == col)
        for col in range(len(gi[ZERO]))
    )
    return len(added), rowmax, colmax


def _render_candidate_3ad05f52(
    diff_lb: float,
    diff_ub: float,
    linked: Boolean,
) -> dict | None:
    cell_size = choice((THREE, THREE, FOUR)) if linked else choice((THREE, THREE, FOUR, FIVE))
    orientation = choice((_HORIZONTAL_3AD05F52, _VERTICAL_3AD05F52))
    color = choice(_FILL_COLORS_3AD05F52)
    step = cell_size + ONE

    if orientation == _HORIZONTAL_3AD05F52:
        left_rows = unifint(diff_lb, diff_ub, (THREE, FIVE if cell_size == THREE else FOUR))
        left_cols = unifint(diff_lb, diff_ub, (TWO, FOUR if cell_size == THREE else THREE))
        right_rows = unifint(diff_lb, diff_ub, (TWO, FOUR))
        right_cols = unifint(diff_lb, diff_ub, (ONE, THREE if cell_size == THREE else TWO))
        component_a = _sample_component_3ad05f52(
            left_rows,
            left_cols,
            diff_lb,
            diff_ub,
            _RIGHT_3AD05F52 if linked else None,
        )
        component_b = _sample_component_3ad05f52(
            right_rows,
            right_cols,
            diff_lb,
            diff_ub,
            _LEFT_3AD05F52 if linked else None,
        )
        top_a = unifint(diff_lb, diff_ub, (ZERO, THREE))
        shift_choices = (-THREE, -TWO, -ONE, ONE, TWO, THREE) if linked else (-ONE, ZERO, ONE)
        top_b = max(
            ZERO,
            top_a
            + (component_a["anchor"][ZERO] - component_b["anchor"][ZERO]) * step
            + choice(shift_choices),
        )
        left_a = unifint(diff_lb, diff_ub, (ZERO, TWO))
        gap = unifint(diff_lb, diff_ub, (FOUR, EIGHT))
        left_b = left_a + left_cols * step + gap
        dims = (
            max(
                top_a + left_rows * step + ONE,
                top_b + right_rows * step + ONE,
            ) + unifint(diff_lb, diff_ub, (ZERO, TWO)),
            left_b + right_cols * step + ONE + unifint(diff_lb, diff_ub, (ZERO, TWO)),
        )
        gap_strip = _gap_strip_3ad05f52(
            dims,
            orientation,
            top_a,
            left_a,
            left_rows,
            left_cols,
            top_b,
            left_b,
            right_rows,
            right_cols,
            cell_size,
        )
    else:
        top_rows = unifint(diff_lb, diff_ub, (TWO, FOUR))
        top_cols = unifint(diff_lb, diff_ub, (THREE, FIVE if cell_size == THREE else FOUR))
        bottom_rows = unifint(diff_lb, diff_ub, (TWO, THREE))
        bottom_cols = unifint(diff_lb, diff_ub, (TWO, FOUR))
        component_a = _sample_component_3ad05f52(
            top_rows,
            top_cols,
            diff_lb,
            diff_ub,
            _BOTTOM_3AD05F52 if linked else None,
        )
        component_b = _sample_component_3ad05f52(
            bottom_rows,
            bottom_cols,
            diff_lb,
            diff_ub,
            _TOP_3AD05F52 if linked else None,
        )
        left_a = unifint(diff_lb, diff_ub, (ZERO, THREE))
        shift_choices = (-THREE, -TWO, -ONE, ONE, TWO, THREE) if linked else (-ONE, ZERO, ONE)
        left_b = max(
            ZERO,
            left_a
            + (component_a["anchor"][ONE] - component_b["anchor"][ONE]) * step
            + choice(shift_choices),
        )
        top_a = unifint(diff_lb, diff_ub, (ZERO, TWO))
        gap = unifint(diff_lb, diff_ub, (FOUR, EIGHT))
        top_b = top_a + top_rows * step + gap
        dims = (
            top_b + bottom_rows * step + ONE + unifint(diff_lb, diff_ub, (ZERO, TWO)),
            max(
                left_a + top_cols * step + ONE,
                left_b + bottom_cols * step + ONE,
            ) + unifint(diff_lb, diff_ub, (ZERO, TWO)),
        )
        gap_strip = _gap_strip_3ad05f52(
            dims,
            orientation,
            top_a,
            left_a,
            top_rows,
            top_cols,
            top_b,
            left_b,
            bottom_rows,
            bottom_cols,
            cell_size,
        )

    if dims[ZERO] > 30 or dims[ONE] > 30 or not gap_strip:
        return None

    gi = canvas(ZERO, dims)
    gi = _paint_component_3ad05f52(
        gi,
        component_a,
        top_a,
        left_a,
        cell_size,
        color,
        linked,
    )
    if orientation == _HORIZONTAL_3AD05F52:
        gi = _paint_component_3ad05f52(
            gi,
            component_b,
            top_b,
            left_b,
            cell_size,
            color,
            linked,
        )
    else:
        gi = _paint_component_3ad05f52(
            gi,
            component_b,
            top_b,
            left_b,
            cell_size,
            color,
            linked,
        )
    go = verify_3ad05f52(gi)

    if gi == go or _component_count_3ad05f52(gi, color) != TWO:
        return None

    gap_count, rowmax, colmax = _gap_stats_3ad05f52(gi, go, gap_strip, color)
    output_components = _component_count_3ad05f52(go, color)
    if linked:
        if output_components != ONE:
            return None
        if gap_count < max(EIGHT, cell_size * THREE):
            return None
        if max(rowmax, colmax) < cell_size:
            return None
    else:
        if gap_count != ZERO:
            return None
        if output_components < TWO:
            return None

    return {"input": gi, "output": go}


def generate_3ad05f52(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        linked = choice(
            (True, True, True, True, False)
        )
        example = _render_candidate_3ad05f52(diff_lb, diff_ub, linked)
        if example is not None:
            return example
