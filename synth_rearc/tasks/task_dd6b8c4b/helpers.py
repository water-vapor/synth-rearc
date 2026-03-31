from __future__ import annotations

from collections import deque

from synth_rearc.core import *


BG_DD6B8C4B = SEVEN
WALL_DD6B8C4B = SIX
FRAME_DD6B8C4B = THREE
CENTER_DD6B8C4B = TWO
MARK_DD6B8C4B = NINE


def _motif_cells_dd6b8c4b(
    top_left: IntegerTuple,
) -> frozenset[IntegerTuple]:
    return frozenset((top_left[ZERO] + i, top_left[ONE] + j) for i in range(THREE) for j in range(THREE))


def _ring_cells_dd6b8c4b(
    top_left: IntegerTuple,
) -> frozenset[IntegerTuple]:
    x0, x1 = top_left
    return frozenset(
        (i, j)
        for i in range(x0 - ONE, x0 + FOUR)
        for j in range(x1 - ONE, x1 + FOUR)
        if not (x0 <= i < x0 + THREE and x1 <= j < x1 + THREE)
    )


def _row_major_fill_cells_dd6b8c4b(
    top_left: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    return tuple((top_left[ZERO] + i, top_left[ONE] + j) for i in range(THREE) for j in range(THREE))


def _find_motif_dd6b8c4b(
    grid: Grid,
) -> IntegerTuple:
    h, w = shape(grid)
    for i in range(h - TWO):
        for j in range(w - TWO):
            patch = crop(grid, (i, j), (THREE, THREE))
            if patch[ONE][ONE] != CENTER_DD6B8C4B:
                continue
            if all(patch[a][b] == FRAME_DD6B8C4B for a in range(THREE) for b in range(THREE) if (a, b) != (ONE, ONE)):
                return (i, j)
    raise ValueError("dd6b8c4b motif not found")


def _allowed_from_open_dd6b8c4b(
    loc: IntegerTuple,
    opener: IntegerTuple,
    top_left: IntegerTuple,
) -> Boolean:
    i, j = loc
    x0, x1 = top_left
    north = opener[ZERO] == x0 - ONE
    south = opener[ZERO] == x0 + THREE
    west = opener[ONE] == x1 - ONE
    east = opener[ONE] == x1 + THREE
    if north and i > x0 + THREE:
        return False
    if south and i < x0 - ONE:
        return False
    if west and j > x1 + THREE:
        return False
    if east and j < x1 - ONE:
        return False
    return True


def _base_seen_dd6b8c4b(
    grid: Grid,
    top_left: IntegerTuple,
) -> frozenset[IntegerTuple]:
    h, w = shape(grid)
    motif_cells = _motif_cells_dd6b8c4b(top_left)
    ring_cells = _ring_cells_dd6b8c4b(top_left)
    seen: set[IntegerTuple] = set()
    for opener in ring_cells:
        oi, oj = opener
        if grid[oi][oj] == WALL_DD6B8C4B:
            continue
        frontier = deque((opener,))
        local_seen = {opener}
        while frontier:
            loc = frontier.popleft()
            seen.add(loc)
            for nxt in dneighbors(loc):
                ni, nj = nxt
                if not (ZERO <= ni < h and ZERO <= nj < w):
                    continue
                if nxt in local_seen or nxt in motif_cells:
                    continue
                if grid[ni][nj] == WALL_DD6B8C4B:
                    continue
                if not _allowed_from_open_dd6b8c4b(nxt, opener, top_left):
                    continue
                local_seen.add(nxt)
                frontier.append(nxt)
    return frozenset(seen)


def _nearest_extra_dd6b8c4b(
    grid: Grid,
    base_seen: frozenset[IntegerTuple],
    top_left: IntegerTuple,
) -> IntegerTuple | None:
    h, w = shape(grid)
    motif_cells = _motif_cells_dd6b8c4b(top_left)
    remaining = {
        (i, j)
        for i, row in enumerate(grid)
        for j, value in enumerate(row)
        if value == MARK_DD6B8C4B and (i, j) not in base_seen
    }
    if len(remaining) == ZERO:
        return None
    dists = {loc: 10 ** 6 for loc in remaining}
    frontier = deque((loc, ZERO) for loc in base_seen)
    seen = set(base_seen)
    while frontier:
        loc, dist = frontier.popleft()
        for nxt in dneighbors(loc):
            ni, nj = nxt
            if not (ZERO <= ni < h and ZERO <= nj < w):
                continue
            if nxt in seen or nxt in motif_cells:
                continue
            if grid[ni][nj] == WALL_DD6B8C4B:
                continue
            if grid[ni][nj] == MARK_DD6B8C4B:
                if nxt in dists and dist + ONE < dists[nxt]:
                    dists[nxt] = dist + ONE
                continue
            seen.add(nxt)
            frontier.append((nxt, dist + ONE))
    finite = tuple((dist, loc) for loc, dist in dists.items() if dist < 10 ** 6)
    if len(finite) == ZERO:
        return None
    return min(finite)[ONE]


def selected_cells_dd6b8c4b(
    grid: Grid,
) -> frozenset[IntegerTuple]:
    top_left = _find_motif_dd6b8c4b(grid)
    base_seen = _base_seen_dd6b8c4b(grid, top_left)
    selected = {loc for loc in base_seen if grid[loc[ZERO]][loc[ONE]] == MARK_DD6B8C4B}
    extra = _nearest_extra_dd6b8c4b(grid, base_seen, top_left)
    if extra is not None:
        selected.add(extra)
    return frozenset(selected)


def analyze_structure_dd6b8c4b(
    grid: Grid,
) -> dict[str, object]:
    top_left = _find_motif_dd6b8c4b(grid)
    base_seen = _base_seen_dd6b8c4b(grid, top_left)
    motif_cells = _motif_cells_dd6b8c4b(top_left)
    ring_cells = _ring_cells_dd6b8c4b(top_left)
    frontier = deque(base_seen)
    visible = set(base_seen)
    h, w = shape(grid)
    while frontier:
        loc = frontier.popleft()
        for nxt in dneighbors(loc):
            ni, nj = nxt
            if not (ZERO <= ni < h and ZERO <= nj < w):
                continue
            if nxt in visible or nxt in motif_cells:
                continue
            if grid[ni][nj] != BG_DD6B8C4B:
                continue
            visible.add(nxt)
            frontier.append(nxt)
    safe_noise = frozenset(
        (i, j)
        for i, row in enumerate(grid)
        for j, value in enumerate(row)
        if value == BG_DD6B8C4B and (i, j) not in visible and (i, j) not in motif_cells
    )
    return {
        "motif_top_left": top_left,
        "ring_cells": ring_cells,
        "base_seen": base_seen,
        "safe_noise": safe_noise,
    }


def transform_grid_dd6b8c4b(
    grid: Grid,
) -> Grid:
    top_left = _find_motif_dd6b8c4b(grid)
    selected = selected_cells_dd6b8c4b(grid)
    out = [list(row) for row in grid]
    for i, j in selected:
        out[i][j] = BG_DD6B8C4B
    fill_cells = _row_major_fill_cells_dd6b8c4b(top_left)
    for i, j in fill_cells[: len(selected)]:
        out[i][j] = MARK_DD6B8C4B
    return tuple(tuple(row) for row in out)
