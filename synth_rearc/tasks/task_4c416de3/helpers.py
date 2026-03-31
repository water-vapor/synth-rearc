from synth_rearc.core import *


FAMILY_LIBRARY_4C416DE3 = (
    {
        "offsets": frozenset({(0, 0), (1, 1), (2, 2), (2, 3), (3, 2), (3, 3)}),
        "corner_offset": (2, 2),
        "rect_h_bounds": (7, 9),
        "rect_w_bounds": (7, 9),
        "arm_h_bounds": (4, 7),
        "arm_w_bounds": (4, 8),
    },
    {
        "offsets": frozenset({(0, 0), (0, 1), (1, 0), (1, 2), (2, 1), (2, 2)}),
        "corner_offset": (1, 1),
        "rect_h_bounds": (6, 8),
        "rect_w_bounds": (6, 8),
        "arm_h_bounds": (4, 7),
        "arm_w_bounds": (4, 8),
    },
    {
        "offsets": frozenset({(0, 0), (1, 1), (1, 2), (2, 1)}),
        "corner_offset": (1, 1),
        "rect_h_bounds": (5, 7),
        "rect_w_bounds": (5, 7),
        "arm_h_bounds": (4, 7),
        "arm_w_bounds": (4, 8),
    },
    {
        "offsets": frozenset({(-1, 0), (0, -1), (0, 0), (1, 1), (1, 2), (2, 1)}),
        "corner_offset": (1, 1),
        "rect_h_bounds": (6, 8),
        "rect_w_bounds": (6, 8),
        "arm_h_bounds": (4, 7),
        "arm_w_bounds": (4, 8),
    },
)

CORNER_SIGNS_4C416DE3 = {
    "tl": (1, 1),
    "tr": (1, -1),
    "bl": (-1, 1),
    "br": (-1, -1),
}

L_EDGES_4C416DE3 = {
    "tl": ("top", "left"),
    "tr": ("top", "right"),
    "bl": ("bottom", "left"),
    "br": ("bottom", "right"),
}


def corner_anchor_4c416de3(
    corner: tuple[int, int],
    corner_name: str,
    family: dict,
) -> tuple[int, int]:
    sr, sc = CORNER_SIGNS_4C416DE3[corner_name]
    di, dj = family["corner_offset"]
    return (corner[0] + sr * di, corner[1] + sc * dj)


def motif_cells_4c416de3(
    anchor: tuple[int, int],
    corner_name: str,
    family: dict,
) -> frozenset[tuple[int, int]]:
    sr, sc = CORNER_SIGNS_4C416DE3[corner_name]
    ai, aj = anchor
    return frozenset((ai - sr * di, aj - sc * dj) for di, dj in family["offsets"])


def rectangle_zero_frame_4c416de3(
    height_value: int,
    width_value: int,
) -> frozenset[tuple[int, int]]:
    top = frozenset((ZERO, j) for j in range(width_value))
    bottom = frozenset((height_value - ONE, j) for j in range(width_value))
    left = frozenset((i, ZERO) for i in range(height_value))
    right = frozenset((i, width_value - ONE) for i in range(height_value))
    return top | bottom | left | right


def elbow_zero_frame_4c416de3(
    height_value: int,
    width_value: int,
    corner_name: str,
) -> tuple[frozenset[tuple[int, int]], tuple[int, int]]:
    if corner_name == "tl":
        row_idx, col_idx = ZERO, ZERO
    elif corner_name == "tr":
        row_idx, col_idx = ZERO, width_value - ONE
    elif corner_name == "bl":
        row_idx, col_idx = height_value - ONE, ZERO
    else:
        row_idx, col_idx = height_value - ONE, width_value - ONE
    horiz = frozenset((row_idx, j) for j in range(width_value))
    vert = frozenset((i, col_idx) for i in range(height_value))
    return horiz | vert, (row_idx, col_idx)


def _normalize_maps_4c416de3(
    input_cells: dict[tuple[int, int], int],
    output_cells: dict[tuple[int, int], int],
) -> tuple[dict[tuple[int, int], int], dict[tuple[int, int], int], tuple[int, int]]:
    all_cells = tuple(input_cells.keys()) + tuple(output_cells.keys())
    min_i = min(i for i, _ in all_cells)
    min_j = min(j for _, j in all_cells)
    shift_vec = (-min_i, -min_j)
    normalized_input = {(i + shift_vec[0], j + shift_vec[1]): v for (i, j), v in input_cells.items()}
    normalized_output = {(i + shift_vec[0], j + shift_vec[1]): v for (i, j), v in output_cells.items()}
    max_i = max(i for i, _ in normalized_output.keys() | normalized_input.keys()) + ONE
    max_j = max(j for _, j in normalized_output.keys() | normalized_input.keys()) + ONE
    return normalized_input, normalized_output, (max_i, max_j)


def build_rectangle_structure_4c416de3(
    family: dict,
    active_corners: tuple[str, ...],
    full_corners: tuple[str, ...],
    color_map: dict[str, int],
    diff_lb: float,
    diff_ub: float,
) -> dict:
    height_value = unifint(diff_lb, diff_ub, family["rect_h_bounds"])
    width_value = unifint(diff_lb, diff_ub, family["rect_w_bounds"])
    zero_cells = rectangle_zero_frame_4c416de3(height_value, width_value)
    output_cells = {loc: ZERO for loc in zero_cells}
    input_cells = dict(output_cells)
    corners = {
        "tl": (ZERO, ZERO),
        "tr": (ZERO, width_value - ONE),
        "bl": (height_value - ONE, ZERO),
        "br": (height_value - ONE, width_value - ONE),
    }
    for corner_name in active_corners:
        anchor = corner_anchor_4c416de3(corners[corner_name], corner_name, family)
        motif = motif_cells_4c416de3(anchor, corner_name, family)
        color_value = color_map[corner_name]
        for cell in motif:
            output_cells[cell] = color_value
        if corner_name in full_corners:
            for cell in motif:
                input_cells[cell] = color_value
        else:
            input_cells[anchor] = color_value
    normalized_input, normalized_output, dims = _normalize_maps_4c416de3(input_cells, output_cells)
    return {
        "input_cells": normalized_input,
        "output_cells": normalized_output,
        "dims": dims,
    }


def build_elbow_structure_4c416de3(
    family: dict,
    corner_name: str,
    full_input: bool,
    color_value: int,
    diff_lb: float,
    diff_ub: float,
) -> dict:
    height_value = unifint(diff_lb, diff_ub, family["arm_h_bounds"])
    width_value = unifint(diff_lb, diff_ub, family["arm_w_bounds"])
    zero_cells, corner = elbow_zero_frame_4c416de3(height_value, width_value, corner_name)
    output_cells = {loc: ZERO for loc in zero_cells}
    input_cells = dict(output_cells)
    anchor = corner_anchor_4c416de3(corner, corner_name, family)
    motif = motif_cells_4c416de3(anchor, corner_name, family)
    for cell in motif:
        output_cells[cell] = color_value
    if full_input:
        for cell in motif:
            input_cells[cell] = color_value
    else:
        input_cells[anchor] = color_value
    normalized_input, normalized_output, dims = _normalize_maps_4c416de3(input_cells, output_cells)
    return {
        "input_cells": normalized_input,
        "output_cells": normalized_output,
        "dims": dims,
    }


def place_patch_4c416de3(
    grid_map: dict[tuple[int, int], int],
    patch: dict[tuple[int, int], int],
    offset: tuple[int, int],
) -> None:
    oi, oj = offset
    for (i, j), value in patch.items():
        grid_map[(i + oi, j + oj)] = value


def render_grid_4c416de3(
    background: int,
    dims: tuple[int, int],
    cells: dict[tuple[int, int], int],
) -> Grid:
    grid = [list(row) for row in canvas(background, dims)]
    for (i, j), value in cells.items():
        grid[i][j] = value
    return tuple(tuple(row) for row in grid)
