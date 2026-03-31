from synth_rearc.core import *

from .helpers import FAMILY_LIBRARY_4C416DE3
from .helpers import build_elbow_structure_4c416de3
from .helpers import build_rectangle_structure_4c416de3
from .helpers import place_patch_4c416de3
from .helpers import render_grid_4c416de3
from .verifier import verify_4c416de3


GRID_BOUNDS_4C416DE3 = (18, 28)
RECT_CORNER_NAMES_4C416DE3 = ("tl", "tr", "bl", "br")


def _choose_structure_colors_4c416de3(
    slots: int,
    background: int,
    used_colors: list[int],
) -> list[int]:
    palette_values = [value for value in range(1, 10) if value != background]
    available = [value for value in palette_values if value not in used_colors]
    if len(available) < slots:
        available = palette_values
    chosen = []
    for _ in range(slots):
        if used_colors and uniform(0.0, 1.0) < 0.2:
            chosen.append(choice(used_colors))
            continue
        fresh = [value for value in available if value not in chosen]
        if not fresh:
            fresh = [value for value in palette_values if value not in chosen] or palette_values
        picked = choice(fresh)
        chosen.append(picked)
    return chosen


def _build_structure_specs_4c416de3(
    family: dict,
    background: int,
    diff_lb: float,
    diff_ub: float,
) -> list[dict]:
    structure_count = unifint(diff_lb, diff_ub, (2, 3))
    rectangle_count = max(ONE, structure_count - (ONE if uniform(0.0, 1.0) < 0.45 else ZERO))
    used_colors: list[int] = []
    specs = []
    need_full = True
    need_seed = True
    for idx in range(structure_count):
        make_rectangle = idx < rectangle_count
        if make_rectangle:
            active_count = randint(2, 4)
            active_corners = tuple(sample(RECT_CORNER_NAMES_4C416DE3, active_count))
            if need_full:
                full_count_lb = ONE
            else:
                full_count_lb = ZERO
            if need_seed:
                full_count_ub = active_count - ONE
            else:
                full_count_ub = active_count
            full_count = randint(full_count_lb, max(full_count_lb, full_count_ub))
            full_corners = tuple(sample(active_corners, full_count))
            colors = _choose_structure_colors_4c416de3(active_count, background, used_colors)
            color_map = {corner_name: color_value for corner_name, color_value in zip(active_corners, colors)}
            specs.append(
                build_rectangle_structure_4c416de3(
                    family,
                    active_corners,
                    full_corners,
                    color_map,
                    diff_lb,
                    diff_ub,
                )
            )
            used_colors.extend(colors)
            need_full = need_full and full_count == ZERO
            need_seed = need_seed and full_count == active_count
        else:
            elbow_name = choice(RECT_CORNER_NAMES_4C416DE3)
            full_input = not need_seed if need_full else uniform(0.0, 1.0) < 0.4
            color_value = _choose_structure_colors_4c416de3(ONE, background, used_colors)[ZERO]
            specs.append(
                build_elbow_structure_4c416de3(
                    family,
                    elbow_name,
                    full_input,
                    color_value,
                    diff_lb,
                    diff_ub,
                )
            )
            used_colors.append(color_value)
            need_full = need_full and not full_input
            need_seed = need_seed and full_input
    if need_full:
        return _build_structure_specs_4c416de3(family, background, diff_lb, diff_ub)
    if need_seed:
        return _build_structure_specs_4c416de3(family, background, diff_lb, diff_ub)
    return specs


def _try_layout_4c416de3(
    specs: list[dict],
    height_value: int,
    width_value: int,
) -> tuple[dict[tuple[int, int], int], dict[tuple[int, int], int]] | None:
    order = list(range(len(specs)))
    shuffle(order)
    occupied = set()
    input_cells: dict[tuple[int, int], int] = {}
    output_cells: dict[tuple[int, int], int] = {}
    for idx in order:
        spec = specs[idx]
        patch_h, patch_w = spec["dims"]
        placed = False
        for _ in range(80):
            oi = randint(ZERO, height_value - patch_h)
            oj = randint(ZERO, width_value - patch_w)
            footprint = frozenset((i + oi, j + oj) for i in range(patch_h) for j in range(patch_w))
            expanded = footprint | mapply(neighbors, footprint)
            if occupied & expanded:
                continue
            place_patch_4c416de3(input_cells, spec["input_cells"], (oi, oj))
            place_patch_4c416de3(output_cells, spec["output_cells"], (oi, oj))
            occupied |= footprint
            placed = True
            break
        if not placed:
            return None
    return input_cells, output_cells


def generate_4c416de3(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        family = choice(FAMILY_LIBRARY_4C416DE3)
        background = choice(interval(ONE, TEN, ONE))
        specs = _build_structure_specs_4c416de3(family, background, diff_lb, diff_ub)
        max_h = maximum(tuple(spec["dims"][ZERO] for spec in specs))
        max_w = maximum(tuple(spec["dims"][ONE] for spec in specs))
        lower_h = max(max_h + TWO, GRID_BOUNDS_4C416DE3[ZERO])
        lower_w = max(max_w + TWO, GRID_BOUNDS_4C416DE3[ZERO])
        grid_h = unifint(diff_lb, diff_ub, (lower_h, GRID_BOUNDS_4C416DE3[ONE]))
        grid_w = unifint(diff_lb, diff_ub, (lower_w, GRID_BOUNDS_4C416DE3[ONE]))
        layout = _try_layout_4c416de3(specs, grid_h, grid_w)
        if layout is None:
            continue
        input_cells, output_cells = layout
        gi = render_grid_4c416de3(background, (grid_h, grid_w), input_cells)
        go = render_grid_4c416de3(background, (grid_h, grid_w), output_cells)
        if gi == go:
            continue
        if verify_4c416de3(gi) != go:
            continue
        return {"input": gi, "output": go}
