from arc2.core import *


COLORS_B7955B3C = tuple(remove(EIGHT, interval(ZERO, TEN, ONE)))
RECTANGLE_MODES_B7955B3C = ("block", "block", "block", "hbar", "vbar")


def _rect_patch_b7955b3c(
    top: Integer,
    left: Integer,
    bottom: Integer,
    right: Integer,
) -> Indices:
    return backdrop(frozenset({(top, left), (bottom, right)}))


def _rect_area_b7955b3c(
    rect: tuple[int, int, int, int],
) -> int:
    top, left, bottom, right = rect
    return (bottom - top + ONE) * (right - left + ONE)


def _rect_overlap_b7955b3c(
    a: tuple[int, int, int, int],
    b: tuple[int, int, int, int],
) -> bool:
    return not (
        a[2] < b[0]
        or b[2] < a[0]
        or a[3] < b[1]
        or b[3] < a[1]
    )


def _sample_rect_b7955b3c(
    height_value: Integer,
    width_value: Integer,
    ref_rect: tuple[int, int, int, int],
    diff_lb: float,
    diff_ub: float,
) -> tuple[int, int, int, int]:
    mode = choice(RECTANGLE_MODES_B7955B3C)
    if mode == "hbar":
        rect_h = unifint(diff_lb, diff_ub, (ONE, max(ONE, height_value // FOUR)))
        rect_w = unifint(diff_lb, diff_ub, (max(THREE, width_value // THREE), max(THREE, width_value - ONE)))
    elif mode == "vbar":
        rect_h = unifint(diff_lb, diff_ub, (max(THREE, height_value // THREE), max(THREE, height_value - ONE)))
        rect_w = unifint(diff_lb, diff_ub, (ONE, max(ONE, width_value // FOUR)))
    else:
        rect_h = unifint(diff_lb, diff_ub, (TWO, max(TWO, height_value - ONE)))
        rect_w = unifint(diff_lb, diff_ub, (TWO, max(TWO, width_value - ONE)))
    rect_h = min(rect_h, height_value - ONE)
    rect_w = min(rect_w, width_value - ONE)
    top_lb = max(ZERO, ref_rect[0] - rect_h + ONE)
    top_ub = min(height_value - rect_h, ref_rect[2])
    left_lb = max(ZERO, ref_rect[1] - rect_w + ONE)
    left_ub = min(width_value - rect_w, ref_rect[3])
    if top_lb > top_ub:
        top_lb = ZERO
        top_ub = height_value - rect_h
    if left_lb > left_ub:
        left_lb = ZERO
        left_ub = width_value - rect_w
    top = unifint(diff_lb, diff_ub, (top_lb, top_ub))
    left = unifint(diff_lb, diff_ub, (left_lb, left_ub))
    bottom = top + rect_h - ONE
    right = left + rect_w - ONE
    return (top, left, bottom, right)


def _paint_rectangles_b7955b3c(
    dimensions: tuple[int, int],
    rects: tuple[tuple[int, tuple[int, int, int, int]], ...],
) -> Grid:
    grid = canvas(rects[0][0], dimensions)
    for color_value, rect in rects[1:]:
        grid = fill(grid, color_value, _rect_patch_b7955b3c(*rect))
    return grid


def _color_data_b7955b3c(
    grid: Grid,
) -> tuple[tuple[int, frozenset[tuple[int, int]], frozenset[tuple[int, int]]], ...]:
    parts = partition(grid)
    return tuple((color(obj), toindices(obj), backdrop(obj)) for obj in parts)


def _precedence_edges_b7955b3c(
    data: tuple[tuple[int, frozenset[tuple[int, int]], frozenset[tuple[int, int]]], ...],
) -> dict[int, set[int]]:
    edges = {color_value: set() for color_value, _, _ in data}
    for color_value, cells, _ in data:
        for lower_color, _, rect_patch in data:
            if color_value != lower_color and size(intersection(cells, rect_patch)) > ZERO:
                edges[lower_color].add(color_value)
    return edges


def _scene_ok_b7955b3c(
    rects: tuple[tuple[int, tuple[int, int, int, int]], ...],
    output: Grid,
) -> bool:
    data = _color_data_b7955b3c(output)
    color_to_patch = {color_value: rect_patch for color_value, _, rect_patch in data}
    if len(color_to_patch) != len(rects):
        return False
    for color_value, rect in rects:
        if color_value not in color_to_patch:
            return False
        if color_to_patch[color_value] != _rect_patch_b7955b3c(*rect):
            return False
    overlap_count = ZERO
    for idx, (_, rect) in enumerate(rects[1:], start=ONE):
        for _, prev_rect in rects[1:idx]:
            if _rect_overlap_b7955b3c(rect, prev_rect):
                overlap_count += ONE
    return overlap_count >= max(ONE, len(rects) - THREE)


def _protected_cells_b7955b3c(
    data: tuple[tuple[int, frozenset[tuple[int, int]], frozenset[tuple[int, int]]], ...],
    edges: dict[int, set[int]],
) -> frozenset[tuple[int, int]]:
    protected = set()
    cells_by_color = {color_value: cells for color_value, cells, _ in data}
    rect_by_color = {color_value: rect_patch for color_value, _, rect_patch in data}
    for _, cells, _ in data:
        top = uppermost(cells)
        bottom = lowermost(cells)
        left = leftmost(cells)
        right = rightmost(cells)
        top_cells = tuple(sorted(cell for cell in cells if cell[0] == top))
        bottom_cells = tuple(sorted(cell for cell in cells if cell[0] == bottom))
        left_cells = tuple(sorted(cell for cell in cells if cell[1] == left))
        right_cells = tuple(sorted(cell for cell in cells if cell[1] == right))
        protected.add(choice(top_cells))
        protected.add(choice(bottom_cells))
        protected.add(choice(left_cells))
        protected.add(choice(right_cells))
    for lower_color, upper_colors in edges.items():
        lower_patch = rect_by_color[lower_color]
        for upper_color in upper_colors:
            witness_cells = tuple(sorted(intersection(cells_by_color[upper_color], lower_patch)))
            protected.add(choice(witness_cells))
    return frozenset(protected)


def _cross_patch_b7955b3c(
    center_cell: tuple[int, int],
) -> frozenset[tuple[int, int]]:
    return insert(center_cell, dneighbors(center_cell))


def _cross_count_bounds_b7955b3c(
    output: Grid,
) -> tuple[int, int]:
    area = len(output) * len(output[0])
    upper_bound = min(SIX, max(ONE, area // 50))
    lower_bound = min(upper_bound, max(ONE, area // 70))
    return lower_bound, upper_bound


def _corrupt_output_b7955b3c(
    output: Grid,
    protected: frozenset[tuple[int, int]],
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    height_value = len(output)
    width_value = len(output[0])
    cross_candidates = []
    for row_idx in range(ONE, height_value - ONE):
        for col_idx in range(ONE, width_value - ONE):
            patch = _cross_patch_b7955b3c((row_idx, col_idx))
            if size(intersection(patch, protected)) == ZERO:
                cross_candidates.append(patch)
    if not cross_candidates:
        return output
    cross_lb, cross_ub = _cross_count_bounds_b7955b3c(output)
    cross_ub = min(cross_ub, len(cross_candidates))
    cross_lb = min(cross_lb, cross_ub)
    cross_target = unifint(diff_lb, diff_ub, (cross_lb, cross_ub))
    chosen_noise = frozenset()
    forbidden_noise = frozenset()
    chosen_crosses = []
    for patch in sample(cross_candidates, len(cross_candidates)):
        if size(intersection(patch, forbidden_noise)) > ZERO:
            continue
        chosen_crosses.append(patch)
        chosen_noise = frozenset(set(chosen_noise) | set(patch))
        forbidden_noise = frozenset(
            set(chosen_noise)
            | {
                neighbor
                for cell in chosen_noise
                for neighbor in dneighbors(cell)
            }
        )
        if len(chosen_crosses) == cross_target:
            break
    if len(chosen_crosses) < cross_lb:
        return output
    return fill(output, EIGHT, chosen_noise)


def generate_b7955b3c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        height_value = unifint(diff_lb, diff_ub, (TEN, 26))
        width_value = unifint(diff_lb, diff_ub, (EIGHT, 24))
        overlay_count = unifint(diff_lb, diff_ub, (TWO, SIX))
        colors = tuple(sample(COLORS_B7955B3C, overlay_count + ONE))
        rects = [(colors[0], (ZERO, ZERO, height_value - ONE, width_value - ONE))]
        attempt_count = ZERO
        while len(rects) < overlay_count + ONE and attempt_count < 240:
            attempt_count += ONE
            if len(rects) > ONE and choice((T, T, F)):
                ref_color, ref_rect = choice(tuple(rects[1:]))
            else:
                ref_color, ref_rect = choice(tuple(rects))
            rect = _sample_rect_b7955b3c(height_value, width_value, ref_rect, diff_lb, diff_ub)
            rect_area = _rect_area_b7955b3c(rect)
            if rect_area < FOUR or rect_area > max(NINE, (height_value * width_value * 3) // 4):
                continue
            if rect in tuple(existing_rect for _, existing_rect in rects):
                continue
            if len(rects) > ONE and choice((T, T, T, F)):
                overlaps = tuple(
                    _rect_overlap_b7955b3c(rect, existing_rect)
                    for _, existing_rect in rects[1:]
                )
                if not any(overlaps):
                    continue
            rects.append((colors[len(rects)], rect))
        if len(rects) < overlay_count + ONE:
            continue
        rects_tuple = tuple(rects)
        go = _paint_rectangles_b7955b3c((height_value, width_value), rects_tuple)
        if not _scene_ok_b7955b3c(rects_tuple, go):
            continue
        output_data = _color_data_b7955b3c(go)
        output_edges = _precedence_edges_b7955b3c(output_data)
        protected = _protected_cells_b7955b3c(output_data, output_edges)
        if len(protected) >= len(go) * len(go[0]):
            continue
        gi = _corrupt_output_b7955b3c(go, protected, diff_lb, diff_ub)
        if gi == go or EIGHT not in palette(gi):
            continue
        input_parts = sfilter(partition(gi), lambda obj: color(obj) != EIGHT)
        input_boxes = {color(obj): backdrop(obj) for obj in input_parts}
        latent_boxes = {color_value: _rect_patch_b7955b3c(*rect) for color_value, rect in rects_tuple}
        if input_boxes != latent_boxes:
            continue
        input_data = _color_data_b7955b3c(gi)
        input_data = tuple(item for item in input_data if item[0] != EIGHT)
        input_edges = _precedence_edges_b7955b3c(input_data)
        if input_edges != output_edges:
            continue
        return {"input": gi, "output": go}
