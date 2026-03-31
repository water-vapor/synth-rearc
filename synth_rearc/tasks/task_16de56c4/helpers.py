from __future__ import annotations

from collections import defaultdict, deque

from synth_rearc.core import *


TraceCandidate16de56c4 = tuple[Integer, Integer, tuple[Integer, ...], Integer]


def color_objects_16de56c4(grid: Grid) -> tuple[tuple[Integer, tuple[IntegerTuple, ...]], ...]:
    h = len(grid)
    w = len(grid[0])
    seen = set()
    objs = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == ZERO or (i, j) in seen:
                continue
            color0 = grid[i][j]
            queue = deque([(i, j)])
            seen.add((i, j))
            cells = []
            while queue:
                i0, j0 = queue.popleft()
                cells.append((i0, j0))
                for ni, nj in dneighbors((i0, j0)):
                    if 0 <= ni < h and 0 <= nj < w:
                        if (ni, nj) in seen:
                            continue
                        if grid[ni][nj] != color0:
                            continue
                        seen.add((ni, nj))
                        queue.append((ni, nj))
            objs.append((color0, tuple(sorted(cells))))
    return tuple(objs)


def progression_positions_16de56c4(
    limit: Integer,
    anchor: Integer,
    step: Integer,
) -> tuple[Integer, ...]:
    return tuple(pos for pos in range(limit) if (pos - anchor) % step == ZERO)


def line_patch_16de56c4(
    axis: str,
    line: Integer,
    positions: tuple[Integer, ...],
) -> Indices:
    if axis == "h":
        return frozenset((line, pos) for pos in positions)
    return frozenset((pos, line) for pos in positions)


def paint_progression_16de56c4(
    grid: Grid,
    axis: str,
    line: Integer,
    positions: tuple[Integer, ...],
    color0: Integer,
) -> Grid:
    return fill(grid, color0, line_patch_16de56c4(axis, line, positions))


def _constant_step_16de56c4(
    positions: tuple[Integer, ...],
) -> Integer | None:
    if len(positions) < TWO:
        return None
    diffs = tuple(b - a for a, b in zip(positions, positions[1:]))
    if len(set(diffs)) != ONE:
        return None
    return diffs[ZERO]


def line_trace_candidates_16de56c4(
    grid: Grid,
    axis: str,
) -> tuple[tuple[TraceCandidate16de56c4, ...], tuple[tuple[Integer, IntegerTuple], ...]]:
    objs = color_objects_16de56c4(grid)
    candidates = []
    singletons = []
    for color0, cells in objs:
        if len(cells) == ONE:
            singletons.append((color0, cells[ZERO]))
            continue
        rows = {i for i, _ in cells}
        cols = {j for _, j in cells}
        if axis == "h" and len(rows) == ONE:
            line = next(iter(rows))
            positions = tuple(j for _, j in cells)
            step = _constant_step_16de56c4(positions)
            if step is not None:
                candidates.append((line, color0, positions, step))
        if axis == "v" and len(cols) == ONE:
            line = next(iter(cols))
            positions = tuple(i for i, _ in cells)
            step = _constant_step_16de56c4(positions)
            if step is not None:
                candidates.append((line, color0, positions, step))
    grouped = defaultdict(lambda: defaultdict(list))
    for color0, loc in singletons:
        if axis == "h":
            grouped[loc[0]][color0].append(loc[1])
        else:
            grouped[loc[1]][color0].append(loc[0])
    for line, by_color in grouped.items():
        for color0, positions0 in by_color.items():
            positions = tuple(sorted(positions0))
            step = _constant_step_16de56c4(positions)
            if step is not None:
                candidates.append((line, color0, positions, step))
    return tuple(candidates), tuple(singletons)


def _marker_by_line_16de56c4(
    singletons: tuple[tuple[Integer, IntegerTuple], ...],
    axis: str,
) -> dict[Integer, list[tuple[Integer, Integer]]]:
    by_line: dict[Integer, list[tuple[Integer, Integer]]] = defaultdict(list)
    for color0, loc in singletons:
        if axis == "h":
            by_line[loc[0]].append((loc[1], color0))
        else:
            by_line[loc[1]].append((loc[0], color0))
    return by_line


def render_axis_16de56c4(
    grid: Grid,
    axis: str,
) -> tuple[Grid, Integer, Integer]:
    h = len(grid)
    w = len(grid[0])
    limit = w if axis == "h" else h
    candidates, singletons = line_trace_candidates_16de56c4(grid, axis)
    by_line = _marker_by_line_16de56c4(singletons, axis)
    out = grid
    changed = ZERO
    for line, color0, positions, step in candidates:
        lo = positions[ZERO]
        hi = positions[-ONE]
        markers = []
        for pos, color1 in by_line.get(line, []):
            if color1 == color0:
                continue
            if (pos - lo) % step != ZERO:
                continue
            if lo < pos < hi:
                continue
            markers.append((pos, color1))
        if len(markers) == ZERO:
            fill_color = color0
            fill_positions = progression_positions_16de56c4(limit, lo, step)
        else:
            marker_pos, fill_color = max(
                markers,
                key=lambda item: min(abs(item[0] - lo), abs(item[0] - hi)),
            )
            start = min(lo, marker_pos)
            stop = max(hi, marker_pos)
            fill_positions = tuple(range(start, stop + ONE, step))
        fill_patch = line_patch_16de56c4(axis, line, fill_positions)
        for loc in fill_patch:
            if index(out, loc) != fill_color:
                changed += ONE
        out = fill(out, fill_color, fill_patch)
    return out, len(candidates), changed


def solve_16de56c4(grid: Grid) -> Grid:
    horizontal, horizontal_count, horizontal_changed = render_axis_16de56c4(grid, "h")
    vertical, vertical_count, vertical_changed = render_axis_16de56c4(grid, "v")
    if horizontal_changed > vertical_changed:
        return horizontal
    if vertical_changed > horizontal_changed:
        return vertical
    if horizontal_count >= vertical_count:
        return horizontal
    return vertical
