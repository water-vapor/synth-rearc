from __future__ import annotations

from collections import Counter

from synth_rearc.core import *


def bbox_a6f40cea(
    cells: tuple[tuple[int, int, int], ...] | list[tuple[int, int, int]],
) -> tuple[int, int, int, int]:
    rows = tuple(i for i, _, _ in cells)
    cols = tuple(j for _, j, _ in cells)
    return (min(rows), min(cols), max(rows), max(cols))


def border_indices_a6f40cea(
    bbox: tuple[int, int, int, int],
) -> frozenset[tuple[int, int]]:
    r0, c0, r1, c1 = bbox
    x0 = {(r0, j) for j in range(c0, c1 + ONE)}
    x1 = {(r1, j) for j in range(c0, c1 + ONE)}
    x2 = {(i, c0) for i in range(r0, r1 + ONE)}
    x3 = {(i, c1) for i in range(r0, r1 + ONE)}
    return frozenset(x0 | x1 | x2 | x3)


def frame_data_a6f40cea(
    grid: Grid,
) -> tuple[int, int, tuple[int, int, int, int]]:
    x0 = mostcolor(grid)
    x1 = objects(grid, T, F, T)
    x2 = tuple(x3 for x3 in x1 if toindices(x3) == box(x3))
    x3 = argmax(x2, size)
    x4 = toindices(x3)
    x5 = ulcorner(x4)
    x6 = lrcorner(x4)
    return x0, color(x3), (x5[ZERO], x5[ONE], x6[ZERO], x6[ONE])


def outside_components_a6f40cea(
    grid: Grid,
    bg: int,
    frame_color: int,
    frame_bbox: tuple[int, int, int, int],
) -> tuple[tuple[tuple[int, int, int], ...], ...]:
    h = len(grid)
    w = len(grid[ZERO])
    fr0, fc0, fr1, fc1 = frame_bbox

    def allowed(
        i: int,
        j: int,
    ) -> bool:
        if grid[i][j] == bg or grid[i][j] == frame_color:
            return False
        if fr0 <= i <= fr1 and fc0 <= j <= fc1:
            return False
        return True

    seen = set()
    comps: list[tuple[tuple[int, int, int], ...]] = []
    for i in range(h):
        for j in range(w):
            if not allowed(i, j) or (i, j) in seen:
                continue
            frontier = [(i, j)]
            seen.add((i, j))
            cells = []
            while frontier:
                ci, cj = frontier.pop()
                cells.append((ci, cj, grid[ci][cj]))
                for ni, nj in ((ci - ONE, cj), (ci + ONE, cj), (ci, cj - ONE), (ci, cj + ONE)):
                    if not (ZERO <= ni < h and ZERO <= nj < w):
                        continue
                    if not allowed(ni, nj) or (ni, nj) in seen:
                        continue
                    seen.add((ni, nj))
                    frontier.append((ni, nj))
            comps.append(tuple(cells))
    return tuple(comps)


def component_sides_a6f40cea(
    cells: tuple[tuple[int, int, int], ...] | list[tuple[int, int, int]],
    frame_bbox: tuple[int, int, int, int],
) -> frozenset[str]:
    fr0, fc0, fr1, fc1 = frame_bbox
    x0 = set()
    if any(i < fr0 and fc0 < j < fc1 for i, j, _ in cells):
        x0.add("above")
    if any(i > fr1 and fc0 < j < fc1 for i, j, _ in cells):
        x0.add("below")
    if any(j < fc0 and fr0 < i < fr1 for i, j, _ in cells):
        x0.add("left")
    if any(j > fc1 and fr0 < i < fr1 for i, j, _ in cells):
        x0.add("right")
    return frozenset(x0)


def component_is_border_subset_a6f40cea(
    cells: tuple[tuple[int, int, int], ...] | list[tuple[int, int, int]],
) -> bool:
    x0 = border_indices_a6f40cea(bbox_a6f40cea(cells))
    return all((i, j) in x0 for i, j, _ in cells)


def component_style_a6f40cea(
    cells: tuple[tuple[int, int, int], ...] | list[tuple[int, int, int]],
) -> tuple[str, object] | None:
    x0 = tuple(sorted({value for _, _, value in cells}))
    if len(x0) == ONE:
        return ("mono", x0[ZERO])
    if len(x0) == TWO:
        return ("alt", x0)
    return None


def interior_bbox_a6f40cea(
    frame_bbox: tuple[int, int, int, int],
) -> tuple[int, int, int, int]:
    fr0, fc0, fr1, fc1 = frame_bbox
    return (fr0 + ONE, fc0 + ONE, fr1 - ONE, fc1 - ONE)


def hidden_patch_a6f40cea(
    bbox: tuple[int, int, int, int],
    frame_bbox: tuple[int, int, int, int],
) -> frozenset[tuple[int, int]]:
    r0, c0, r1, c1 = bbox
    ir0, ic0, ir1, ic1 = interior_bbox_a6f40cea(frame_bbox)
    x0 = set()
    if ir0 <= r0 <= ir1:
        x0.update((r0, j) for j in range(max(ic0, c0), min(ic1, c1) + ONE))
    if ir0 <= r1 <= ir1:
        x0.update((r1, j) for j in range(max(ic0, c0), min(ic1, c1) + ONE))
    if ic0 <= c0 <= ic1:
        x0.update((i, c0) for i in range(max(ir0, r0), min(ir1, r1) + ONE))
    if ic0 <= c1 <= ic1:
        x0.update((i, c1) for i in range(max(ir0, r0), min(ir1, r1) + ONE))
    return frozenset(x0)


def crop_interior_a6f40cea(
    grid: Grid,
    frame_bbox: tuple[int, int, int, int],
) -> list[list[int]]:
    ir0, ic0, ir1, ic1 = interior_bbox_a6f40cea(frame_bbox)
    return [list(row[ic0:ic1 + ONE]) for row in grid[ir0:ir1 + ONE]]


def freeze_rows_a6f40cea(
    rows: list[list[int]],
) -> Grid:
    return tuple(tuple(row) for row in rows)


def paint_hidden_mono_a6f40cea(
    rows: list[list[int]],
    bbox: tuple[int, int, int, int],
    color_value: int,
    frame_bbox: tuple[int, int, int, int],
) -> bool:
    ir0, ic0, _, _ = interior_bbox_a6f40cea(frame_bbox)
    x0 = hidden_patch_a6f40cea(bbox, frame_bbox)
    if len(x0) == ZERO:
        return False
    for i, j in x0:
        rows[i - ir0][j - ic0] = color_value
    return True


def _filtered_left_rows_bottomright_a6f40cea(
    bbox: tuple[int, int, int, int],
    frame_bbox: tuple[int, int, int, int],
) -> tuple[int, ...]:
    r0, c0, r1, _ = bbox
    fr0, fc0, fr1, fc1 = frame_bbox
    x0 = []
    for i in range(r0, r1 + ONE):
        x1 = fr0 <= i <= fr1 and fc0 <= c0 <= fc1 and (i in (fr0, fr1) or c0 in (fc0, fc1))
        if not x1:
            x0.append(i)
    return tuple(x0)


def paint_hidden_alt_topleft_a6f40cea(
    rows: list[list[int]],
    bbox: tuple[int, int, int, int],
    cells: tuple[tuple[int, int, int], ...] | list[tuple[int, int, int]],
    colors: tuple[int, int],
    frame_bbox: tuple[int, int, int, int],
) -> bool:
    ir0, ic0, ir1, ic1 = interior_bbox_a6f40cea(frame_bbox)
    r0, c0, r1, c1 = bbox
    x0 = {i: value for i, j, value in cells if j == c0}
    x1 = range(max(ir0, r0), min(ir1, r1) + ONE)
    for i in x1:
        rows[i - ir0][c1 - ic0] = x0[i]
    x2 = rows[r1 - ir0][c1 - ic0]
    x3 = colors[ZERO] if x2 == colors[ONE] else colors[ONE]
    for j in range(c1, max(ic0, c0) - ONE, NEG_ONE):
        rows[r1 - ir0][j - ic0] = x2
        x2, x3 = x3, x2
    return True


def paint_hidden_alt_bottomright_a6f40cea(
    rows: list[list[int]],
    bbox: tuple[int, int, int, int],
    cells: tuple[tuple[int, int, int], ...] | list[tuple[int, int, int]],
    colors: tuple[int, int],
    frame_bbox: tuple[int, int, int, int],
) -> bool:
    ir0, ic0, ir1, ic1 = interior_bbox_a6f40cea(frame_bbox)
    r0, c0, r1, _ = bbox
    fr0, _, fr1, _ = frame_bbox
    x0 = {i: value for i, j, value in cells if j == c0}
    x1 = min(x0)
    x2 = x0[x1]
    x3 = colors[ZERO] if x2 == colors[ONE] else colors[ONE]
    x4 = (fr1 - r0) % TWO == ONE
    if x4:
        for i in range(max(ir0, r0), min(ir1, r1) + ONE):
            x5 = x1 - i
            rows[i - ir0][c0 - ic0] = x2 if x5 % TWO == ZERO else x3
    else:
        x5 = _filtered_left_rows_bottomright_a6f40cea(bbox, frame_bbox)
        x6 = {row: idx for idx, row in enumerate(x5)}
        x7 = x6[x1]
        for i in range(max(ir0, r0), min(ir1, r1) + ONE):
            x8 = x7 - x6[i]
            rows[i - ir0][c0 - ic0] = x2 if x8 % TWO == ZERO else x3
    x9 = rows[r0 - ir0][c0 - ic0]
    x10 = colors[ZERO] if x9 == colors[ONE] else colors[ONE]
    for j in range(max(ic0, c0), min(ic1, bbox[THREE]) + ONE):
        rows[r0 - ir0][j - ic0] = x9
        x9, x10 = x10, x9
    return True


def solve_hidden_rectangles_a6f40cea(
    grid: Grid,
) -> Grid:
    bg, frame_color, frame_bbox = frame_data_a6f40cea(grid)
    rows = crop_interior_a6f40cea(grid, frame_bbox)
    comps = outside_components_a6f40cea(grid, bg, frame_color, frame_bbox)
    used = set()
    above = {}
    below = {}
    left = {}
    right = {}
    for idx, cells in enumerate(comps):
        bbox = bbox_a6f40cea(cells)
        if not component_is_border_subset_a6f40cea(cells):
            continue
        style = component_style_a6f40cea(cells)
        if style is None:
            continue
        sides = component_sides_a6f40cea(cells, frame_bbox)
        if style[ZERO] == "mono":
            if paint_hidden_mono_a6f40cea(rows, bbox, style[ONE], frame_bbox):
                used.add(idx)
            if sides == frozenset({"above"}):
                above[(bbox[ONE], bbox[THREE], style[ONE])] = cells
            elif sides == frozenset({"below"}):
                below[(bbox[ONE], bbox[THREE], style[ONE])] = cells
            elif sides == frozenset({"left"}):
                left[(bbox[ZERO], bbox[TWO], style[ONE])] = cells
            elif sides == frozenset({"right"}):
                right[(bbox[ZERO], bbox[TWO], style[ONE])] = cells
            continue
        if sides == frozenset({"above", "left"}):
            paint_hidden_alt_topleft_a6f40cea(rows, bbox, cells, style[ONE], frame_bbox)
            used.add(idx)
        elif sides == frozenset({"below", "right"}):
            paint_hidden_alt_bottomright_a6f40cea(rows, bbox, cells, style[ONE], frame_bbox)
            used.add(idx)
    for key in set(above) & set(below):
        x0 = above[key] + below[key]
        paint_hidden_mono_a6f40cea(rows, bbox_a6f40cea(x0), key[TWO], frame_bbox)
    for key in set(left) & set(right):
        x0 = left[key] + right[key]
        paint_hidden_mono_a6f40cea(rows, bbox_a6f40cea(x0), key[TWO], frame_bbox)
    return freeze_rows_a6f40cea(rows)


def paint_cells_a6f40cea(
    grid: Grid,
    colored_cells: dict[tuple[int, int], int],
) -> Grid:
    x0 = frozenset((value, index) for index, value in colored_cells.items())
    return paint(grid, x0)


def visible_cells_a6f40cea(
    colored_cells: dict[tuple[int, int], int],
    frame_bbox: tuple[int, int, int, int],
) -> dict[tuple[int, int], int]:
    fr0, fc0, fr1, fc1 = frame_bbox
    return {
        index: value
        for index, value in colored_cells.items()
        if not (fr0 <= index[ZERO] <= fr1 and fc0 <= index[ONE] <= fc1)
    }


def hidden_cells_a6f40cea(
    colored_cells: dict[tuple[int, int], int],
    frame_bbox: tuple[int, int, int, int],
) -> dict[tuple[int, int], int]:
    ir0, ic0, ir1, ic1 = interior_bbox_a6f40cea(frame_bbox)
    return {
        index: value
        for index, value in colored_cells.items()
        if ir0 <= index[ZERO] <= ir1 and ic0 <= index[ONE] <= ic1
    }


def mono_border_a6f40cea(
    bbox: tuple[int, int, int, int],
    color_value: int,
) -> dict[tuple[int, int], int]:
    return {index: color_value for index in border_indices_a6f40cea(bbox)}


def _alternate_sequence_a6f40cea(
    start_value: int,
    other_value: int,
    n: int,
) -> tuple[int, ...]:
    out = []
    cur = start_value
    nxt = other_value
    for _ in range(n):
        out.append(cur)
        cur, nxt = nxt, cur
    return tuple(out)


def alt_topleft_border_a6f40cea(
    bbox: tuple[int, int, int, int],
    colors: tuple[int, int],
) -> dict[tuple[int, int], int]:
    r0, c0, r1, c1 = bbox
    start_value = choice(colors)
    other_value = colors[ZERO] if start_value == colors[ONE] else colors[ONE]
    width = c1 - c0 + ONE
    height = r1 - r0 + ONE
    x0 = {}
    x1 = _alternate_sequence_a6f40cea(start_value, other_value, height)
    x2 = _alternate_sequence_a6f40cea(start_value, other_value, width)
    for di, value in enumerate(x1):
        x0[(r0 + di, c0)] = value
        x0[(r0 + di, c1)] = value
    for dj, value in enumerate(x2):
        x0[(r0, c0 + dj)] = value
    x3 = x1[-ONE]
    x4 = colors[ZERO] if x3 == colors[ONE] else colors[ONE]
    x5 = _alternate_sequence_a6f40cea(x3, x4, width)
    for dj, value in enumerate(reversed(x5)):
        x0[(r1, c0 + dj)] = value
    return x0


def alt_bottomright_border_a6f40cea(
    bbox: tuple[int, int, int, int],
    colors: tuple[int, int],
    frame_bbox: tuple[int, int, int, int],
) -> dict[tuple[int, int], int]:
    r0, c0, r1, c1 = bbox
    _, _, fr1, fc1 = frame_bbox
    start_value = choice(colors)
    other_value = colors[ZERO] if start_value == colors[ONE] else colors[ONE]
    width = c1 - c0 + ONE
    height = r1 - r0 + ONE
    x0 = {}
    x1 = (fr1 - r0) % TWO == ONE
    if x1:
        x2 = _alternate_sequence_a6f40cea(start_value, other_value, height)
        for di, value in enumerate(x2):
            x0[(r0 + di, c0)] = value
    else:
        x2 = _filtered_left_rows_bottomright_a6f40cea(bbox, frame_bbox)
        x3 = _alternate_sequence_a6f40cea(start_value, other_value, len(x2))
        for row, value in zip(x2, x3):
            x0[(row, c0)] = value
    x4 = (fr1 - r0) % TWO == ONE
    if x4:
        x5 = _alternate_sequence_a6f40cea(start_value, other_value, width)
        for dj, value in enumerate(x5):
            x0[(r0, c0 + dj)] = value
    else:
        x5 = tuple(j for j in range(c0, c1 + ONE) if j != fc1)
        x6 = _alternate_sequence_a6f40cea(start_value, other_value, len(x5))
        for col, value in zip(x5, x6):
            x0[(r0, col)] = value
        x0[(r0, fc1)] = other_value
    x7 = x0[(r0, c1)] if (r0, c1) in x0 else choice(colors)
    x8 = colors[ZERO] if x7 == colors[ONE] else colors[ONE]
    x9 = _alternate_sequence_a6f40cea(x7, x8, height)
    for di, value in enumerate(x9):
        x0[(r0 + di, c1)] = value
    x10 = x0[(r1, c0)] if (r1, c0) in x0 else choice(colors)
    x11 = colors[ZERO] if x10 == colors[ONE] else colors[ONE]
    x12 = _alternate_sequence_a6f40cea(x10, x11, width)
    for dj, value in enumerate(x12):
        x0[(r1, c0 + dj)] = value
    return x0
