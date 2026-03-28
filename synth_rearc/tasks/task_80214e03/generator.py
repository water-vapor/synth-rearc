from __future__ import annotations

from synth_rearc.core import *


PALETTE_80214E03 = (ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)
MERGE_COUNTS_80214E03 = (ZERO, ZERO, ONE, ONE, TWO, TWO, THREE)
HOLE_COUNTS_80214E03 = (ZERO, ONE, ONE, TWO, TWO, THREE, THREE, FOUR, FOUR, FIVE)


def _sample_spans(
    count: Integer,
    diff_lb: float,
    diff_ub: float,
    bounds: tuple[Integer, Integer],
    totals: tuple[Integer, Integer],
) -> tuple[Integer, ...]:
    lower, upper = totals
    while True:
        spans = tuple(unifint(diff_lb, diff_ub, bounds) for _ in range(count))
        total = sum(spans)
        if lower <= total <= upper:
            return spans


def _region_boxes(layout: tuple[tuple[Integer, ...], ...]) -> dict[Integer, tuple[Integer, Integer, Integer, Integer]]:
    boxes: dict[Integer, list[Integer]] = {}
    for i, row in enumerate(layout):
        for j, region_id in enumerate(row):
            if region_id not in boxes:
                boxes[region_id] = [i, i, j, j]
                continue
            boxes[region_id][0] = min(boxes[region_id][0], i)
            boxes[region_id][1] = max(boxes[region_id][1], i)
            boxes[region_id][2] = min(boxes[region_id][2], j)
            boxes[region_id][3] = max(boxes[region_id][3], j)
    return {region_id: tuple(bounds) for region_id, bounds in boxes.items()}


def _supports_boundaries(layout: tuple[tuple[Integer, ...], ...]) -> bool:
    h = len(layout)
    w = len(layout[0])
    for j in range(w - ONE):
        if all(layout[i][j] == layout[i][j + ONE] for i in range(h)):
            return False
    for i in range(h - ONE):
        if all(layout[i][j] == layout[i + ONE][j] for j in range(w)):
            return False
    return True


def _merge_options(layout: tuple[tuple[Integer, ...], ...]) -> tuple[tuple[Integer, Integer], ...]:
    h = len(layout)
    w = len(layout[0])
    boxes = _region_boxes(layout)
    options = set()
    for i in range(h):
        for j in range(w - ONE):
            left = layout[i][j]
            right = layout[i][j + ONE]
            if left == right:
                continue
            a = boxes[left]
            b = boxes[right]
            if a[0] == a[1] == b[0] == b[1] and a[0] == b[0]:
                options.add((min(left, right), max(left, right)))
    for i in range(h - ONE):
        for j in range(w):
            top = layout[i][j]
            bottom = layout[i + ONE][j]
            if top == bottom:
                continue
            a = boxes[top]
            b = boxes[bottom]
            if a[2] == a[3] == b[2] == b[3] and a[2] == b[2]:
                options.add((min(top, bottom), max(top, bottom)))
    return tuple(sorted(options))


def _apply_merge(
    layout: tuple[tuple[Integer, ...], ...],
    first: Integer,
    second: Integer,
) -> tuple[tuple[Integer, ...], ...]:
    rows = []
    for row in layout:
        rows.append(tuple(first if value == second else value for value in row))
    return tuple(rows)


def _sample_layout(
    rows: Integer,
    cols: Integer,
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[Integer, ...], ...]:
    layout = tuple(tuple(i * cols + j for j in range(cols)) for i in range(rows))
    target_merges = min(choice(MERGE_COUNTS_80214E03), rows * cols - ONE)
    for _ in range(target_merges):
        options = []
        for first, second in _merge_options(layout):
            trial = _apply_merge(layout, first, second)
            if _supports_boundaries(trial):
                options.append(trial)
        if len(options) == ZERO:
            break
        layout = choice(options)
    if _supports_boundaries(layout):
        return layout
    return tuple(tuple(i * cols + j for j in range(cols)) for i in range(rows))


def _adjacency(layout: tuple[tuple[Integer, ...], ...]) -> dict[Integer, set[Integer]]:
    h = len(layout)
    w = len(layout[0])
    result = {value: set() for row in layout for value in row}
    for i in range(h):
        for j in range(w - ONE):
            left = layout[i][j]
            right = layout[i][j + ONE]
            if left == right:
                continue
            result[left].add(right)
            result[right].add(left)
    for i in range(h - ONE):
        for j in range(w):
            top = layout[i][j]
            bottom = layout[i + ONE][j]
            if top == bottom:
                continue
            result[top].add(bottom)
            result[bottom].add(top)
    return result


def _assign_colors(layout: tuple[tuple[Integer, ...], ...]) -> dict[Integer, Integer] | None:
    neighbors = _adjacency(layout)
    region_ids = tuple(sorted(neighbors))
    max_palette = min(SEVEN, len(PALETTE_80214E03), len(region_ids))
    min_palette = min(FOUR, max_palette)
    palette_size = randint(min_palette, max_palette)
    ordering = tuple(sorted(region_ids, key=lambda value: (-len(neighbors[value]), value)))
    for _ in range(80):
        colors = {}
        palette_values = sample(PALETTE_80214E03, palette_size)
        for region_id in ordering:
            blocked = {colors[other] for other in neighbors[region_id] if other in colors}
            candidates = tuple(value for value in palette_values if value not in blocked)
            if len(candidates) == ZERO:
                break
            colors[region_id] = choice(candidates)
        if len(colors) != len(region_ids):
            continue
        if len(set(colors.values())) < min_palette:
            continue
        return colors
    return None


def _sparse_points(candidates: tuple[IntegerTuple, ...], target: Integer) -> Indices:
    if target <= ZERO or len(candidates) == ZERO:
        return frozenset()
    pool = list(candidates)
    shuffle(pool)
    chosen = []
    blocked = set()
    for cell in pool:
        if cell in blocked:
            continue
        chosen.append(cell)
        blocked.add(cell)
        blocked |= neighbors(cell)
        if len(chosen) == target:
            return frozenset(chosen)
    for cell in pool:
        if cell in chosen:
            continue
        chosen.append(cell)
        if len(chosen) == target:
            break
    return frozenset(chosen)


def generate_80214e03(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        num_rows = unifint(diff_lb, diff_ub, (TWO, FOUR))
        num_cols = unifint(diff_lb, diff_ub, (TWO, THREE))
        top_margin = unifint(diff_lb, diff_ub, (ONE, TWO))
        bottom_margin = unifint(diff_lb, diff_ub, (TWO, FIVE))
        left_margin = unifint(diff_lb, diff_ub, (ONE, TWO))
        right_margin = unifint(diff_lb, diff_ub, (ONE, FOUR))
        min_active_h = max(THREE * num_rows, 18 - top_margin - bottom_margin)
        max_active_h = 22 - top_margin - bottom_margin
        min_active_w = max(THREE * num_cols, 11 - left_margin - right_margin)
        max_active_w = 19 - left_margin - right_margin
        if min_active_h > max_active_h or min_active_w > max_active_w:
            continue
        row_heights = _sample_spans(num_rows, diff_lb, diff_ub, (THREE, EIGHT), (min_active_h, max_active_h))
        col_widths = _sample_spans(num_cols, diff_lb, diff_ub, (THREE, SIX), (min_active_w, max_active_w))
        layout = _sample_layout(num_rows, num_cols, diff_lb, diff_ub)
        colors = _assign_colors(layout)
        if colors is None:
            continue
        grid_h = top_margin + sum(row_heights) + bottom_margin
        grid_w = left_margin + sum(col_widths) + right_margin
        row_starts = []
        col_starts = []
        cursor = top_margin
        for height_value in row_heights:
            row_starts.append(cursor)
            cursor += height_value
        cursor = left_margin
        for width_value in col_widths:
            col_starts.append(cursor)
            cursor += width_value
        gi = canvas(ZERO, (grid_h, grid_w))
        boxes = _region_boxes(layout)
        total_holes = ZERO
        for region_id, (r0, r1, c0, c1) in boxes.items():
            top = row_starts[r0]
            bottom = row_starts[r1] + row_heights[r1] - ONE
            left = col_starts[c0]
            right = col_starts[c1] + col_widths[c1] - ONE
            patch = frozenset((i, j) for i in range(top, bottom + ONE) for j in range(left, right + ONE))
            gi = fill(gi, colors[region_id], patch)
            candidates = tuple(
                (i, j)
                for i in range(top, bottom + ONE)
                for j in range(left, right + ONE)
            )
            max_holes = min(len(candidates) // FOUR, max(ONE, len(patch) // FIVE))
            if max_holes <= ZERO:
                continue
            target_holes = min(choice(HOLE_COUNTS_80214E03), max_holes)
            holes = _sparse_points(candidates, target_holes)
            if len(holes) == ZERO:
                continue
            gi = fill(gi, ZERO, holes)
            total_holes += len(holes)
        if total_holes < max(TWO, num_rows):
            continue
        if mostcolor(gi) != ZERO:
            continue
        go = tuple(
            tuple(colors[layout[i][j]] for j in range(num_cols - ONE, -ONE, -ONE))
            for i in range(num_rows)
        )
        return {"input": gi, "output": go}
