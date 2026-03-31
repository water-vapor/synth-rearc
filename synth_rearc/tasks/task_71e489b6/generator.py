from synth_rearc.core import *

from .helpers import MAX_DIM_71E489B6
from .helpers import MIN_DIM_71E489B6
from .helpers import ZERO_INTERIOR_SHAPES_71E489B6
from .helpers import blank_grid_71e489b6
from .helpers import freeze_grid_71e489b6
from .helpers import halo_cells_71e489b6
from .helpers import orth_neighbors_71e489b6
from .helpers import paint_cells_71e489b6
from .helpers import paint_rect_71e489b6
from .helpers import random_partition_71e489b6
from .helpers import selected_one_cells_71e489b6
from .helpers import selected_zero_cells_71e489b6
from .helpers import shape_variants_71e489b6
from .verifier import verify_71e489b6


MODE_RECT_ZERO_71E489B6 = "rect_zero"
MODE_RECT_ONE_71E489B6 = "rect_one"
MODE_BANDS_71E489B6 = "bands"
MODE_IDS_71E489B6 = (
    MODE_RECT_ZERO_71E489B6,
    MODE_RECT_ONE_71E489B6,
    MODE_BANDS_71E489B6,
)


def _in_bounds_71e489b6(
    cell,
    dims,
):
    return 0 <= cell[0] < dims[0] and 0 <= cell[1] < dims[1]


def _touches_border_71e489b6(
    cells,
    dims,
):
    h, w = dims
    return any(i in {0, h - 1} or j in {0, w - 1} for i, j in cells)


def _offset_shape_71e489b6(
    shape,
    offset,
):
    return frozenset((i + offset[0], j + offset[1]) for i, j in shape)


def _can_place_isolated_component_71e489b6(
    grid,
    cells,
    host_color,
):
    h = len(grid)
    w = len(grid[0])
    if size(cells) > ONE and _touches_border_71e489b6(cells, (h, w)):
        return False
    for cell in cells:
        if not _in_bounds_71e489b6(cell, (h, w)):
            return False
        i, j = cell
        if grid[i][j] != host_color:
            return False
        for neighbor in orth_neighbors_71e489b6(cell):
            ni, nj = neighbor
            if 0 <= ni < h and 0 <= nj < w and neighbor not in cells and grid[ni][nj] != host_color:
                return False
    return True


def _can_place_attached_single_71e489b6(
    grid,
    cell,
    value,
):
    h = len(grid)
    w = len(grid[0])
    i, j = cell
    if not (0 <= i < h and 0 <= j < w):
        return False
    if grid[i][j] == value:
        return False
    attachments = []
    for neighbor in orth_neighbors_71e489b6(cell):
        ni, nj = neighbor
        if 0 <= ni < h and 0 <= nj < w:
            if grid[ni][nj] == value:
                attachments.append(neighbor)
            elif grid[ni][nj] != 1 - value:
                return False
    return size(attachments) == ONE


def _shape_candidates_71e489b6(
    grid,
    host_color,
    shape,
):
    h = len(grid)
    w = len(grid[0])
    max_i = max(i for i, _ in shape)
    max_j = max(j for _, j in shape)
    candidates = []
    for top in range(h - max_i):
        for left in range(w - max_j):
            cells = _offset_shape_71e489b6(shape, (top, left))
            if _can_place_isolated_component_71e489b6(grid, cells, host_color):
                candidates.append(cells)
    return tuple(candidates)


def _attached_single_candidates_71e489b6(
    grid,
    value,
):
    h = len(grid)
    w = len(grid[0])
    candidates = []
    for i in range(h):
        for j in range(w):
            cell = (i, j)
            if _can_place_attached_single_71e489b6(grid, cell, value):
                candidates.append(frozenset({cell}))
    return tuple(candidates)


def _build_rect_base_71e489b6(
    background,
):
    h = randint(MIN_DIM_71E489B6, MAX_DIM_71E489B6)
    w = randint(MIN_DIM_71E489B6, MAX_DIM_71E489B6)
    grid = blank_grid_71e489b6((h, w), background)
    foreground = ONE - background
    rect_count = choice((ONE, ONE, TWO))
    painted = 0
    attempts = 0
    while painted < rect_count and attempts < 60:
        attempts += 1
        rh = randint(max(5, h // 3), max(6, h - 4))
        rw = randint(max(5, w // 3), max(6, w - 4))
        if h - rh - 4 < 0 or w - rw - 4 < 0:
            continue
        top = randint(2, h - rh - 2)
        left = randint(2, w - rw - 2)
        paint_rect_71e489b6(grid, top, left, rh, rw, foreground)
        painted += 1
    return grid


def _build_band_base_71e489b6():
    h = randint(MIN_DIM_71E489B6, MAX_DIM_71E489B6)
    w = randint(MIN_DIM_71E489B6, MAX_DIM_71E489B6)
    grid = blank_grid_71e489b6((h, w), ZERO)
    orientation = choice(("h", "v"))
    if orientation == "h":
        band_count = randint(3, min(5, h // 3))
        sizes = random_partition_71e489b6(h, band_count, 3)
        cursor = 0
        start_color = choice((ZERO, ONE))
        for idx, band_height in enumerate(sizes):
            color = (start_color + idx) % 2
            paint_rect_71e489b6(grid, cursor, 0, band_height, w, color)
            cursor += band_height
    else:
        band_count = randint(3, min(5, w // 3))
        sizes = random_partition_71e489b6(w, band_count, 3)
        cursor = 0
        start_color = choice((ZERO, ONE))
        for idx, band_width in enumerate(sizes):
            color = (start_color + idx) % 2
            paint_rect_71e489b6(grid, 0, cursor, h, band_width, color)
            cursor += band_width
    return grid


def _build_base_grid_71e489b6(
    mode,
):
    if mode == MODE_RECT_ZERO_71E489B6:
        return _build_rect_base_71e489b6(ZERO)
    if mode == MODE_RECT_ONE_71E489B6:
        return _build_rect_base_71e489b6(ONE)
    return _build_band_base_71e489b6()


def _place_zero_components_71e489b6(
    grid,
    target_count,
):
    placed = []
    variants = tuple(
        candidate
        for shape in ZERO_INTERIOR_SHAPES_71E489B6
        for candidate in shape_variants_71e489b6(shape)
    )
    attempts = 0
    while len(placed) < target_count and attempts < target_count * 60:
        attempts += 1
        mode = choice(("isolated", "isolated", "isolated", "attached"))
        if mode == "attached":
            candidates = _attached_single_candidates_71e489b6(grid, ZERO)
        else:
            x0 = choice(variants)
            candidates = _shape_candidates_71e489b6(grid, ONE, x0)
        if not candidates:
            continue
        x1 = choice(candidates)
        paint_cells_71e489b6(grid, x1, ZERO)
        placed.append(x1)
    return placed


def _place_one_components_71e489b6(
    grid,
    halo,
    target_count,
):
    placed = []
    h = len(grid)
    w = len(grid[0])
    attempts = 0
    while len(placed) < target_count and attempts < target_count * 80:
        attempts += 1
        mode = choice(("isolated", "isolated", "attached"))
        candidates = []
        for i in range(h):
            for j in range(w):
                cell = (i, j)
                if cell in halo or grid[i][j] != ZERO:
                    continue
                if mode == "attached":
                    if _can_place_attached_single_71e489b6(grid, cell, ONE):
                        candidates.append(cell)
                    continue
                if all(
                    not _in_bounds_71e489b6(neighbor, (h, w)) or grid[neighbor[0]][neighbor[1]] == ZERO
                    for neighbor in orth_neighbors_71e489b6(cell)
                ):
                    candidates.append(cell)
        if not candidates:
            continue
        x0 = choice(candidates)
        grid[x0[0]][x0[1]] = ONE
        placed.append(frozenset({x0}))
    return placed


def _count_targets_71e489b6(
    diff_lb,
    diff_ub,
):
    diff = (diff_lb + diff_ub) / 2.0
    zero_count = randint(2, 3 + int(3 * diff))
    one_count = randint(1, 2 + int(2 * diff))
    return zero_count, one_count


def _render_output_71e489b6(
    gi,
    zero_cells,
    one_cells,
):
    x0 = halo_cells_71e489b6(zero_cells, shape(gi))
    x1 = fill(gi, ZERO, one_cells)
    x2 = fill(x1, SEVEN, x0)
    x3 = fill(x2, ZERO, zero_cells)
    return x3


def generate_71e489b6(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(MODE_IDS_71E489B6)
        x1 = _build_base_grid_71e489b6(x0)
        x2, x3 = _count_targets_71e489b6(diff_lb, diff_ub)
        x4 = _place_zero_components_71e489b6(x1, x2)
        if len(x4) < x2:
            continue
        x5 = frozenset(cell for component in x4 for cell in component)
        x6 = halo_cells_71e489b6(x5, (len(x1), len(x1[0])))
        x7 = _place_one_components_71e489b6(x1, x6, x3)
        if len(x7) < x3:
            continue
        x8 = frozenset(cell for component in x7 for cell in component)
        x9 = freeze_grid_71e489b6(x1)
        x10 = selected_zero_cells_71e489b6(x9)
        x11 = halo_cells_71e489b6(x10, shape(x9))
        x12 = selected_one_cells_71e489b6(x9, x11)
        if x10 != x5 or x12 != x8:
            continue
        x13 = _render_output_71e489b6(x9, x10, x12)
        if verify_71e489b6(x9) != x13:
            continue
        if x9 == x13:
            continue
        return {"input": x9, "output": x13}
