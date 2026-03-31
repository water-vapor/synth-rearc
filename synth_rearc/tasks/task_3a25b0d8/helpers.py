from __future__ import annotations

from collections import Counter

from synth_rearc.core import *


WALL_3A25B0D8 = NEG_ONE
REGION_MATCH_THRESHOLD_3A25B0D8 = 0.01
MAX_OBJECT_HEIGHT_3A25B0D8 = 18
MAX_OBJECT_WIDTH_3A25B0D8 = 13

TEMPLATE_MASKS_3A25B0D8 = (
    (
        "...##...##...",
        "..#..###..#..",
        ".#....#....#.",
        ".#....#....#.",
        ".###..#..###.",
        "..#########..",
        ".#...###...#.",
        ".#...#.#...#.",
        ".####...####.",
        ".#.###.###.#.",
        ".###.###.###.",
        "..#...#...#..",
        "##.........##",
        ".#.........#.",
        ".#....#....#.",
        ".###########.",
        "....#...#....",
        "....#####....",
    ),
    (
        "...#####...",
        "..##...##..",
        ".###...###.",
        "#.#######.#",
        "#..#...#..#",
        "#.#######.#",
        ".##..#..##.",
        "..#######..",
        "...#...#...",
        "...#...#...",
        "...#####...",
    ),
    (
        ".##.##.",
        "#..#..#",
        "#..#..#",
        ".##.##.",
        ".#...#.",
        ".#...#.",
        "#######",
        "..#.#..",
        "..#.#..",
        ".##.##.",
        ".#...#.",
        "##...##",
        "#######",
    ),
    (
        "....###....",
        "...##.##...",
        ".###...###.",
        "#..##.##..#",
        "#..#.#.#..#",
        "####...####",
        ".##.....##.",
        ".#########.",
        ".#...#...#.",
        ".#...#...#.",
        "#.###.###.#",
        "####...####",
        "...##.##...",
        "....###....",
    ),
)


def dominant_fill_color_3a25b0d8(
    grid: Grid,
) -> Integer:
    bg = mostcolor(grid)
    ctr = Counter(value for row in grid for value in row if value != bg)
    return ctr.most_common(ONE)[ZERO][ZERO]


def _component_crop_3a25b0d8(
    grid: Grid,
    cells: set[IntegerTuple],
    bg: Integer,
) -> Grid:
    rows = tuple(loc[ZERO] for loc in cells)
    cols = tuple(loc[ONE] for loc in cells)
    top = min(rows)
    bottom = max(rows)
    left = min(cols)
    right = max(cols)
    out = []
    for i in range(top, bottom + ONE):
        row = []
        for j in range(left, right + ONE):
            row.append(grid[i][j] if (i, j) in cells else bg)
        out.append(tuple(row))
    return tuple(out)


def _non_bg_components_3a25b0d8(
    grid: Grid,
    bg: Integer,
) -> tuple[set[IntegerTuple], ...]:
    h = len(grid)
    w = len(grid[ZERO])
    seen = set()
    comps: list[set[IntegerTuple]] = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == bg or (i, j) in seen:
                continue
            frontier = [(i, j)]
            seen.add((i, j))
            comp = set()
            while frontier:
                ci, cj = frontier.pop()
                comp.add((ci, cj))
                for ni, nj in ((ci - ONE, cj), (ci + ONE, cj), (ci, cj - ONE), (ci, cj + ONE)):
                    if not (ZERO <= ni < h and ZERO <= nj < w):
                        continue
                    if grid[ni][nj] == bg or (ni, nj) in seen:
                        continue
                    seen.add((ni, nj))
                    frontier.append((ni, nj))
            comps.append(comp)
    return tuple(comps)


def decompose_input_3a25b0d8(
    grid: Grid,
) -> tuple[Integer, Integer, Grid, Grid]:
    bg = mostcolor(grid)
    fg = dominant_fill_color_3a25b0d8(grid)
    comps = _non_bg_components_3a25b0d8(grid, bg)
    source_cells = max(
        comps,
        key=lambda comp: (
            len({grid[i][j] for i, j in comp}),
            len(comp),
        ),
    )
    source = _component_crop_3a25b0d8(grid, source_cells, bg)
    scaffold_cells = {
        (i, j)
        for i, row in enumerate(grid)
        for j, value in enumerate(row)
        if value == fg and (i, j) not in source_cells
    }
    scaffold = _component_crop_3a25b0d8(
        tuple(
            tuple(fg if (i, j) in scaffold_cells else bg for j in range(len(grid[ZERO])))
            for i in range(len(grid))
        ),
        scaffold_cells,
        bg,
    )
    return bg, fg, source, scaffold


def open_regions_3a25b0d8(
    grid: Grid,
    wall: Integer,
) -> tuple[dict[str, object], ...]:
    h = len(grid)
    w = len(grid[ZERO])
    seen = set()
    regions: list[dict[str, object]] = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == wall or (i, j) in seen:
                continue
            frontier = [(i, j)]
            seen.add((i, j))
            cells = []
            values = []
            while frontier:
                ci, cj = frontier.pop()
                cells.append((ci, cj))
                values.append(grid[ci][cj])
                for ni, nj in ((ci - ONE, cj), (ci + ONE, cj), (ci, cj - ONE), (ci, cj + ONE)):
                    if not (ZERO <= ni < h and ZERO <= nj < w):
                        continue
                    if grid[ni][nj] == wall or (ni, nj) in seen:
                        continue
                    seen.add((ni, nj))
                    frontier.append((ni, nj))
            rows = tuple(loc[ZERO] for loc in cells)
            cols = tuple(loc[ONE] for loc in cells)
            regions.append(
                {
                    "cells": tuple(cells),
                    "color": Counter(values).most_common(ONE)[ZERO][ZERO],
                    "center": (
                        (sum(rows) / len(rows)) / max(ONE, h - ONE),
                        (sum(cols) / len(cols)) / max(ONE, w - ONE),
                    ),
                    "touches_border": (
                        min(rows) == ZERO
                        or max(rows) == h - ONE
                        or min(cols) == ZERO
                        or max(cols) == w - ONE
                    ),
                }
            )
    return tuple(regions)


def recolor_scaffold_regions_3a25b0d8(
    source: Grid,
    scaffold: Grid,
    bg: Integer,
    fg: Integer,
) -> Grid:
    source_regions = open_regions_3a25b0d8(source, fg)
    scaffold_regions = open_regions_3a25b0d8(scaffold, fg)
    sh = len(source)
    sw = len(source[ZERO])
    out = [list(row) for row in scaffold]
    for region in scaffold_regions:
        ci, cj = region["center"]
        si = round(ci * max(ZERO, sh - ONE))
        sj = round(cj * max(ZERO, sw - ONE))
        value = source[si][sj]
        if value == fg:
            nearest = min(
                source_regions,
                key=lambda other: (
                    (other["center"][ZERO] - ci) ** TWO + (other["center"][ONE] - cj) ** TWO
                ),
            )
            distance = (
                (nearest["center"][ZERO] - ci) ** TWO + (nearest["center"][ONE] - cj) ** TWO
            )
            value = nearest["color"] if distance < REGION_MATCH_THRESHOLD_3A25B0D8 else bg
        for i, j in region["cells"]:
            out[i][j] = value
    return tuple(tuple(row) for row in out)


def _label_grid_from_mask_3a25b0d8(
    mask: tuple[str, ...],
) -> tuple[tuple[Integer, ...], ...]:
    h = len(mask)
    w = len(mask[ZERO])
    labels = [[WALL_3A25B0D8 if cell == "#" else NEG_TWO for cell in row] for row in mask]
    next_region = ZERO
    for i in range(h):
        for j in range(w):
            if labels[i][j] != NEG_TWO:
                continue
            frontier = [(i, j)]
            labels[i][j] = next_region
            while frontier:
                ci, cj = frontier.pop()
                for ni, nj in ((ci - ONE, cj), (ci + ONE, cj), (ci, cj - ONE), (ci, cj + ONE)):
                    if not (ZERO <= ni < h and ZERO <= nj < w):
                        continue
                    if labels[ni][nj] != NEG_TWO:
                        continue
                    labels[ni][nj] = next_region
                    frontier.append((ni, nj))
            next_region += ONE
    return tuple(tuple(row) for row in labels)


LABEL_GRIDS_3A25B0D8 = tuple(
    _label_grid_from_mask_3a25b0d8(tuple(mask))
    for mask in TEMPLATE_MASKS_3A25B0D8
)


def region_infos_from_labels_3a25b0d8(
    label_grid: tuple[tuple[Integer, ...], ...],
) -> dict[Integer, dict[str, object]]:
    h = len(label_grid)
    w = len(label_grid[ZERO])
    by_region: dict[Integer, list[IntegerTuple]] = {}
    for i, row in enumerate(label_grid):
        for j, value in enumerate(row):
            if value == WALL_3A25B0D8:
                continue
            by_region.setdefault(value, []).append((i, j))
    out = {}
    for region_id, cells in by_region.items():
        rows = tuple(loc[ZERO] for loc in cells)
        cols = tuple(loc[ONE] for loc in cells)
        out[region_id] = {
            "cells": tuple(cells),
            "center": (
                (sum(rows) / len(rows)) / max(ONE, h - ONE),
                (sum(cols) / len(cols)) / max(ONE, w - ONE),
            ),
            "touches_border": (
                min(rows) == ZERO
                or max(rows) == h - ONE
                or min(cols) == ZERO
                or max(cols) == w - ONE
            ),
        }
    return out


def mirror_groups_3a25b0d8(
    region_infos: dict[Integer, dict[str, object]],
) -> tuple[tuple[Integer, ...], ...]:
    pending = [
        region_id
        for region_id, info in region_infos.items()
        if not info["touches_border"]
    ]
    pending.sort(
        key=lambda region_id: (
            region_infos[region_id]["center"][ZERO],
            region_infos[region_id]["center"][ONE],
        )
    )
    groups: list[tuple[Integer, ...]] = []
    while pending:
        region_id = pending.pop(ZERO)
        ci, cj = region_infos[region_id]["center"]
        if abs(cj - 0.5) < 0.08:
            groups.append((region_id,))
            continue
        best_idx = None
        best_score = None
        for idx, other_id in enumerate(pending):
            oi, oj = region_infos[other_id]["center"]
            score = abs(ci - oi) + abs((cj + oj) - ONE)
            if best_score is None or score < best_score:
                best_score = score
                best_idx = idx
        if best_idx is not None and best_score is not None and best_score < 0.2:
            other_id = pending.pop(best_idx)
            groups.append(tuple(sorted((region_id, other_id))))
        else:
            groups.append((region_id,))
    groups.sort(
        key=lambda group: (
            min(region_infos[region_id]["center"][ZERO] for region_id in group),
            min(region_infos[region_id]["center"][ONE] for region_id in group),
        )
    )
    return tuple(groups)


def choose_region_colors_3a25b0d8(
    label_grid: tuple[tuple[Integer, ...], ...],
    bg: Integer,
    fg: Integer,
) -> dict[Integer, Integer]:
    infos = region_infos_from_labels_3a25b0d8(label_grid)
    groups = mirror_groups_3a25b0d8(infos)
    pool = [color for color in range(TEN) if color not in (bg, fg)]
    shuffle(pool)
    region_colors = {region_id: bg for region_id in infos}
    for idx, group in enumerate(groups):
        color = pool[idx % len(pool)]
        for region_id in group:
            region_colors[region_id] = color
    return region_colors


def _scale_vector_3a25b0d8(
    length: Integer,
    max_length: Integer,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, ...]:
    extras_cap = max(ZERO, min(FOUR, max_length - length))
    extras = unifint(diff_lb, diff_ub, (ZERO, extras_cap))
    scales = [ONE for _ in range(length)]
    if extras > ZERO:
        picks = sample(tuple(range(length)), extras)
        for idx in picks:
            scales[idx] = TWO
    return tuple(scales)


def choose_scales_3a25b0d8(
    label_grid: tuple[tuple[Integer, ...], ...],
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[Integer, ...], tuple[Integer, ...]]:
    h = len(label_grid)
    w = len(label_grid[ZERO])
    row_scales = _scale_vector_3a25b0d8(h, MAX_OBJECT_HEIGHT_3A25B0D8, diff_lb, diff_ub)
    col_scales = _scale_vector_3a25b0d8(w, MAX_OBJECT_WIDTH_3A25B0D8, diff_lb, diff_ub)
    return row_scales, col_scales


def expand_label_grid_3a25b0d8(
    label_grid: tuple[tuple[Integer, ...], ...],
    row_scales: tuple[Integer, ...],
    col_scales: tuple[Integer, ...],
) -> tuple[tuple[Integer, ...], ...]:
    rows = []
    for i, row in enumerate(label_grid):
        expanded_row = []
        for j, value in enumerate(row):
            expanded_row.extend(repeat(value, col_scales[j]))
        rows.extend(repeat(tuple(expanded_row), row_scales[i]))
    return tuple(rows)


def render_label_grid_3a25b0d8(
    label_grid: tuple[tuple[Integer, ...], ...],
    bg: Integer,
    fg: Integer,
    region_colors: dict[Integer, Integer],
) -> Grid:
    out = []
    for row in label_grid:
        out.append(
            tuple(
                fg if value == WALL_3A25B0D8 else region_colors[value]
                for value in row
            )
        )
    return tuple(out)


def render_scaffold_3a25b0d8(
    label_grid: tuple[tuple[Integer, ...], ...],
    bg: Integer,
    fg: Integer,
) -> Grid:
    return render_label_grid_3a25b0d8(
        label_grid,
        bg,
        fg,
        {value: bg for row in label_grid for value in row if value != WALL_3A25B0D8},
    )


def _paint_full_grid_3a25b0d8(
    grid: list[list[Integer]],
    patch: Grid,
    offset: IntegerTuple,
) -> None:
    oi, oj = offset
    for i, row in enumerate(patch):
        for j, value in enumerate(row):
            grid[oi + i][oj + j] = value


def compose_input_grid_3a25b0d8(
    source: Grid,
    scaffold: Grid,
    bg: Integer,
) -> Grid:
    sh = len(source)
    sw = len(source[ZERO])
    bh = len(scaffold)
    bw = len(scaffold[ZERO])
    gap = randint(ONE, THREE)
    extra_h = randint(ONE, THREE)
    extra_w = randint(ZERO, ONE)
    horizontal_dims = (
        max(sh, bh) + extra_h,
        sw + bw + gap + extra_w,
    )
    vertical_dims = (
        sh + bh + gap + extra_h,
        max(sw, bw) + extra_w,
    )
    use_horizontal = horizontal_dims[ZERO] <= 30 and horizontal_dims[ONE] <= 30
    if vertical_dims[ZERO] <= 30 and vertical_dims[ONE] <= 30:
        use_horizontal = use_horizontal and choice((T, F, T))
    elif not use_horizontal:
        use_horizontal = F
    if use_horizontal:
        h, w = horizontal_dims
        source_offset = (
            randint(ZERO, max(ZERO, h - sh)),
            randint(ZERO, max(ZERO, w - sw - bw - gap)),
        )
        scaffold_offset = (
            randint(ZERO, max(ZERO, h - bh)),
            randint(add(source_offset[ONE], sw + gap), max(add(source_offset[ONE], sw + gap), w - bw)),
        )
    else:
        h, w = vertical_dims
        source_offset = (
            randint(ZERO, max(ZERO, h - sh - bh - gap)),
            randint(ZERO, max(ZERO, w - sw)),
        )
        scaffold_offset = (
            randint(add(source_offset[ZERO], sh + gap), max(add(source_offset[ZERO], sh + gap), h - bh)),
            randint(ZERO, max(ZERO, w - bw)),
        )
    out = [[bg for _ in range(w)] for _ in range(h)]
    _paint_full_grid_3a25b0d8(out, source, source_offset)
    _paint_full_grid_3a25b0d8(out, scaffold, scaffold_offset)
    return tuple(tuple(row) for row in out)
