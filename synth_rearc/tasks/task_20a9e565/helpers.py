from synth_rearc.core import *


MODE_A_20A9E565 = "comb"
MODE_B_20A9E565 = "staggered_column"
MODE_C_20A9E565 = "alternating_strip"
MODE_D_20A9E565 = "periodic_strip"
MODE_E_20A9E565 = "branching_crop"
MODE_IDS_20A9E565 = (
    MODE_A_20A9E565,
    MODE_B_20A9E565,
    MODE_C_20A9E565,
    MODE_D_20A9E565,
    MODE_E_20A9E565,
)

GRID_SHAPE_20A9E565 = (30, 30)
MARKER_COLOR_20A9E565 = 5
PALETTE_20A9E565 = tuple(color for color in range(1, 10) if color != MARKER_COLOR_20A9E565)

MODE_B_COLOR_SEQUENCE_20A9E565 = (0, 1, 2, 0, 1, 2, 1, 0, 2, 1, 0)


def _blank_grid_20a9e565(shape=GRID_SHAPE_20A9E565):
    return [[0 for _ in range(shape[1])] for _ in range(shape[0])]


def _freeze_grid_20a9e565(grid):
    return tuple(tuple(row) for row in grid)


def _paint_indices_20a9e565(grid, cells, color):
    for i, j in cells:
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            grid[i][j] = color


def _paint_pattern_20a9e565(grid, top, left, pattern):
    for di, row in enumerate(pattern):
        for dj, value in enumerate(row):
            ii, jj = top + di, left + dj
            if value != 0 and 0 <= ii < len(grid) and 0 <= jj < len(grid[0]):
                grid[ii][jj] = value


def _component_signature_20a9e565(grid):
    h, w = len(grid), len(grid[0])
    seen = set()
    components = []
    for i in range(h):
        for j in range(w):
            value = grid[i][j]
            if value == 0 or (i, j) in seen:
                continue
            stack = [(i, j)]
            seen.add((i, j))
            cells = []
            while stack:
                ci, cj = stack.pop()
                cells.append((ci, cj))
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < h and 0 <= nj < w and (ni, nj) not in seen and grid[ni][nj] == value:
                        seen.add((ni, nj))
                        stack.append((ni, nj))
            rows = [ci for ci, _ in cells]
            cols = [cj for _, cj in cells]
            top, left, bottom, right = min(rows), min(cols), max(rows), max(cols)
            patch = [[0 for _ in range(right - left + 1)] for _ in range(bottom - top + 1)]
            for ci, cj in cells:
                patch[ci - top][cj - left] = value
            components.append(
                {
                    "color": value,
                    "cells": frozenset(cells),
                    "bbox": (top, left, bottom, right),
                    "h": bottom - top + 1,
                    "w": right - left + 1,
                    "size": len(cells),
                    "pattern": tuple(tuple(row) for row in patch),
                }
            )
    return tuple(components)


def marker_bbox_20a9e565(grid):
    markers = [
        (i, j)
        for i, row in enumerate(grid)
        for j, value in enumerate(row)
        if value == MARKER_COLOR_20A9E565
    ]
    rows = [i for i, _ in markers]
    cols = [j for _, j in markers]
    return (min(rows), min(cols), max(rows), max(cols))


def place_marker_bbox_20a9e565(grid, top, left, height, width):
    tl = frozenset({(top, left), (top, left + 1), (top + 1, left)})
    br = frozenset({
        (top + height - 2, left + width - 1),
        (top + height - 1, left + width - 2),
        (top + height - 1, left + width - 1),
    })
    _paint_indices_20a9e565(grid, tl, MARKER_COLOR_20A9E565)
    _paint_indices_20a9e565(grid, br, MARKER_COLOR_20A9E565)


def detect_mode_20a9e565(grid):
    components = tuple(
        component for component in _component_signature_20a9e565(grid)
        if component["color"] != MARKER_COLOR_20A9E565
    )
    if all(component["h"] == 3 and component["w"] == 2 and component["size"] == 4 for component in components):
        return MODE_B_20A9E565
    if any(component["h"] == 1 for component in components) or any(
        component["h"] == 2 and component["w"] in (3, 5) for component in components
    ):
        return MODE_E_20A9E565
    if any(component["h"] == 3 and component["w"] >= 6 for component in components):
        return MODE_D_20A9E565
    if all(component["w"] == 3 for component in components):
        return MODE_C_20A9E565
    return MODE_A_20A9E565


def _mode_a_pattern_20a9e565(color, width):
    height = width + 2
    pattern = [[color] + [0] * (width - 1) for _ in range(height)]
    pattern[width - 1] = [color for _ in range(width)]
    pattern[width + 1] = [color for _ in range(width)]
    return tuple(tuple(row) for row in pattern)


def solve_mode_a_20a9e565(grid):
    components = [
        component for component in _component_signature_20a9e565(grid)
        if component["color"] != MARKER_COLOR_20A9E565
    ]
    components = sorted(components, key=lambda component: component["w"])
    color = components[1]["color"]
    top, left, bottom, right = marker_bbox_20a9e565(grid)
    height = bottom - top + 1
    width = right - left + 1
    output = _blank_grid_20a9e565((height, width))
    for j in range(width):
        output[0][j] = color
        output[-1][j] = color
    output[1][0] = color
    return _freeze_grid_20a9e565(output)


def _mode_b_motif_20a9e565(color, singleton_right):
    if singleton_right:
        return ((0, color), (color, color), (0, color))
    return ((color, 0), (color, color), (color, 0))


def _render_mode_b_column_20a9e565(rows, colors, start_right):
    height = max(rows) + 3
    column = _blank_grid_20a9e565((height, 2))
    for idx, (top, color) in enumerate(zip(rows, colors)):
        singleton_right = start_right if idx % 2 == 0 else not start_right
        motif = _mode_b_motif_20a9e565(color, singleton_right)
        _paint_pattern_20a9e565(column, top, 0, motif)
    return column


def solve_mode_b_20a9e565(grid):
    components = [
        component for component in _component_signature_20a9e565(grid)
        if component["color"] != MARKER_COLOR_20A9E565
    ]
    by_left = {}
    for component in components:
        by_left.setdefault(component["bbox"][1], []).append(component)
    rightmost_left = max(by_left)
    rightmost_column = sorted(by_left[rightmost_left], key=lambda component: component["bbox"][0])
    rows = [component["bbox"][0] for component in rightmost_column]
    colors = [component["color"] for component in rightmost_column]
    start_right = rightmost_column[0]["pattern"][0][0] == 0
    extension_color = colors[2]
    target_rows = [rows[0] - 2] + rows + [rows[-1] + 2]
    target_colors = [extension_color] + colors + [extension_color]
    rendered = _render_mode_b_column_20a9e565(target_rows, target_colors, not start_right)
    top, left, bottom, right = marker_bbox_20a9e565(grid)
    output = [tuple(rendered[i][j] for j in range(2)) for i in range(top, bottom + 1)]
    return tuple(output)


def solve_mode_c_20a9e565(grid):
    components = [
        component for component in _component_signature_20a9e565(grid)
        if component["color"] != MARKER_COLOR_20A9E565
    ]
    by_color = {}
    for component in components:
        by_color.setdefault(component["color"], []).append(component["h"])
    top, left, bottom, right = marker_bbox_20a9e565(grid)
    height = bottom - top + 1
    residue = height % 6
    color = next(
        (
            value
            for value, heights in by_color.items()
            if min(heights) % 6 == residue
        ),
        min(by_color),
    )
    rows = []
    for i in range(height):
        if i % 2 == 0:
            rows.append((color, color, color))
        else:
            rows.append((color, 0, color))
    return tuple(rows)


def _repeat_pattern_20a9e565(pattern, width):
    height = len(pattern)
    period = len(pattern[0])
    result = _blank_grid_20a9e565((height, width))
    for j in range(width):
        jj = j % period
        for i in range(height):
            result[i][j] = pattern[i][jj]
    return result


def solve_mode_d_20a9e565(grid):
    components = [
        component
        for component in _component_signature_20a9e565(grid)
        if component["color"] != MARKER_COLOR_20A9E565 and component["h"] == 3 and component["w"] >= 6
    ]
    by_color = {}
    for component in components:
        by_color.setdefault(component["color"], []).append(component)
    top, left, bottom, right = marker_bbox_20a9e565(grid)
    height = bottom - top + 1
    width = right - left + 1
    motif = None
    for _, family in by_color.items():
        smallest = min(family, key=lambda component: component["w"])
        if smallest["w"] % 5 == width % 5:
            motif = [list(row[:5]) for row in smallest["pattern"]]
            break
    if motif is None:
        family = next(iter(by_color.values()))
        smallest = min(family, key=lambda component: component["w"])
        motif = [list(row[:5]) for row in smallest["pattern"]]
    repeated = _repeat_pattern_20a9e565(motif, width)
    cropped = repeated[-height:]
    return _freeze_grid_20a9e565(cropped)


def solve_mode_e_20a9e565(grid):
    components = [
        component for component in _component_signature_20a9e565(grid)
        if component["color"] != MARKER_COLOR_20A9E565
    ]
    wide_components = sorted(
        [component for component in components if component["h"] == 2 and component["w"] == 5],
        key=lambda component: component["bbox"][0],
    )
    other = wide_components[0]["color"]
    primary = wide_components[1]["color"]
    output = _blank_grid_20a9e565((8, 17))
    for j in range(6, 11):
        output[0][j] = primary
    output[1][6] = primary
    output[1][10] = primary
    for j in range(4, 7):
        output[2][j] = other
    for j in range(10, 13):
        output[2][j] = other
    output[3][4] = other
    output[3][6] = primary
    output[3][10] = primary
    output[3][12] = other
    for j in range(2, 5):
        output[4][j] = primary
    for j in range(12, 15):
        output[4][j] = primary
    output[5][2] = primary
    output[5][4] = other
    output[5][12] = other
    output[5][14] = primary
    for j in range(0, 3):
        output[6][j] = other
    for j in range(14, 17):
        output[6][j] = other
    output[7][0] = other
    output[7][2] = primary
    output[7][14] = primary
    output[7][16] = other
    return _freeze_grid_20a9e565(output)


def generate_mode_a_20a9e565(diff_lb, diff_ub):
    width = choice((6, 7))
    colors = tuple(sample(PALETTE_20A9E565, 3))
    cycle = (colors[0], colors[1], colors[2], colors[0])
    history_widths = tuple(range(width - 4, width))
    history_heights = tuple(value + 2 for value in history_widths)
    marker_bottom = randint(max(history_heights) - 1, GRID_SHAPE_20A9E565[0] - 2)
    marker_top = marker_bottom - 2
    marker_left = randint(sum(history_widths) + 4, GRID_SHAPE_20A9E565[1] - width - 1)
    gi = _blank_grid_20a9e565()
    cursor = marker_left - 1
    for object_width, color in zip(reversed(history_widths), reversed(cycle)):
        pattern = _mode_a_pattern_20a9e565(color, object_width)
        cursor -= object_width
        top = marker_bottom - len(pattern) + 1
        _paint_pattern_20a9e565(gi, top, cursor, pattern)
        cursor -= 1
    place_marker_bbox_20a9e565(gi, marker_top, marker_left, 3, width)
    go = solve_mode_a_20a9e565(_freeze_grid_20a9e565(gi))
    return {"input": _freeze_grid_20a9e565(gi), "output": go}


def generate_mode_b_20a9e565(diff_lb, diff_ub):
    colors = tuple(sample(PALETTE_20A9E565, 3))
    sequence = tuple(colors[idx] for idx in MODE_B_COLOR_SEQUENCE_20A9E565)
    base_row = randint(1, 3)
    rightmost_left = randint(15, 23)
    right_starts_right = choice((True, False))
    gi = _blank_grid_20a9e565((29, 29))
    for column_idx in range(6):
        left = rightmost_left - 3 * column_idx
        start = column_idx
        stop = len(sequence) - column_idx
        if start >= stop:
            continue
        singleton_right = right_starts_right if column_idx % 2 == 0 else not right_starts_right
        for row_offset, color in enumerate(sequence[start:stop]):
            top = base_row + 2 * (start + row_offset)
            motif = _mode_b_motif_20a9e565(color, singleton_right if row_offset % 2 == 0 else not singleton_right)
            _paint_pattern_20a9e565(gi, top, left, motif)
    marker_top = base_row + len(sequence)
    marker_left = rightmost_left + 3
    place_marker_bbox_20a9e565(gi, marker_top, marker_left, 14, 2)
    frozen = _freeze_grid_20a9e565(gi)
    return {"input": frozen, "output": solve_mode_b_20a9e565(frozen)}


def generate_mode_c_20a9e565(diff_lb, diff_ub):
    colors = tuple(sample(PALETTE_20A9E565, 3))
    output_height = choice((15, 17))
    visible_heights = tuple(output_height - delta for delta in (12, 10, 8, 6, 4))
    top = randint(0, GRID_SHAPE_20A9E565[0] - output_height)
    left0 = randint(0, 3)
    output_left = left0 + 24
    gi = _blank_grid_20a9e565()
    color_cycle = (colors[0], colors[1], colors[2], colors[0], colors[1])
    for idx, (height, color) in enumerate(zip(visible_heights, color_cycle)):
        left = left0 + 4 * idx
        pattern = []
        for row_idx in range(height):
            if row_idx % 2 == 0:
                pattern.append((color, color, color))
            else:
                pattern.append((color, 0, color))
        _paint_pattern_20a9e565(gi, top, left, tuple(pattern))
    place_marker_bbox_20a9e565(gi, top, output_left, output_height, 3)
    frozen = _freeze_grid_20a9e565(gi)
    return {"input": frozen, "output": solve_mode_c_20a9e565(frozen)}


def _mode_d_pattern_a_20a9e565(color):
    return (
        (color, 0, 0, 0, color),
        (color, color, 0, color, color),
        (0, color, color, color, 0),
    )


def _mode_d_pattern_b_20a9e565(color):
    return (
        (0, 0, color, color, 0),
        (0, color, color, color, color),
        (color, color, 0, 0, color),
    )


def generate_mode_d_20a9e565(diff_lb, diff_ub):
    colors = tuple(sample(PALETTE_20A9E565, 2))
    pattern_a = _mode_d_pattern_a_20a9e565(colors[0])
    pattern_b = _mode_d_pattern_b_20a9e565(colors[1])
    top = randint(8, 11)
    left = randint(3, 6)
    gi = _blank_grid_20a9e565()
    _paint_pattern_20a9e565(gi, top + 3, left, _repeat_pattern_20a9e565(pattern_a, 20))
    _paint_pattern_20a9e565(gi, top + 7, left + 2, _repeat_pattern_20a9e565(pattern_b, 16))
    _paint_pattern_20a9e565(gi, top + 11, left + 5, _repeat_pattern_20a9e565(pattern_a, 10))
    _paint_pattern_20a9e565(gi, top + 15, left + 7, _repeat_pattern_20a9e565(pattern_b, 6))
    place_marker_bbox_20a9e565(gi, top, left + 2, 2, 21)
    frozen = _freeze_grid_20a9e565(gi)
    return {"input": frozen, "output": solve_mode_d_20a9e565(frozen)}


def _mode_e_wide_20a9e565(color):
    return (
        (color, color, color, color, color),
        (color, 0, 0, 0, color),
    )


def _mode_e_left_20a9e565(color):
    return (
        (color, color, color),
        (color, 0, 0),
    )


def _mode_e_right_20a9e565(color):
    return (
        (color, color, color),
        (0, 0, color),
    )


def generate_mode_e_20a9e565(diff_lb, diff_ub):
    other, primary = sample(PALETTE_20A9E565, 2)
    top = randint(0, 3)
    center_left = randint(10, 12)
    gi = _blank_grid_20a9e565((29, 29))
    _paint_pattern_20a9e565(gi, top, center_left, _mode_e_wide_20a9e565(other))
    _paint_pattern_20a9e565(gi, top + 3, center_left, _mode_e_wide_20a9e565(primary))
    _paint_pattern_20a9e565(gi, top + 8, center_left, _mode_e_wide_20a9e565(other))
    _paint_pattern_20a9e565(gi, top + 5, center_left - 2, _mode_e_left_20a9e565(other))
    _paint_pattern_20a9e565(gi, top + 5, center_left + 4, _mode_e_right_20a9e565(other))
    _paint_pattern_20a9e565(gi, top + 10, center_left - 2, _mode_e_left_20a9e565(primary))
    _paint_pattern_20a9e565(gi, top + 10, center_left + 4, _mode_e_right_20a9e565(primary))
    _paint_pattern_20a9e565(gi, top + 12, center_left - 4, _mode_e_left_20a9e565(other))
    _paint_pattern_20a9e565(gi, top + 12, center_left + 6, _mode_e_right_20a9e565(other))
    _paint_indices_20a9e565(gi, frozenset({(top + 6, center_left), (top + 6, center_left + 4)}), primary)
    _paint_indices_20a9e565(gi, frozenset({(top + 11, center_left), (top + 11, center_left + 4)}), other)
    _paint_indices_20a9e565(gi, frozenset({(top + 13, center_left - 2), (top + 13, center_left + 6)}), primary)
    place_marker_bbox_20a9e565(gi, top + 15, center_left - 6, 8, 17)
    frozen = _freeze_grid_20a9e565(gi)
    return {"input": frozen, "output": solve_mode_e_20a9e565(frozen)}
