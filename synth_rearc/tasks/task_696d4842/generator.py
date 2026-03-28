from synth_rearc.core import *


PAIR_COUNT_696D4842 = TWO
GRID_SIDES_696D4842 = (20, 20, 30)
MIN_GAP_696D4842 = THREE
MAX_GAP_696D4842 = SIX


def _trace_segment_696d4842(
    start: IntegerTuple,
    direction: IntegerTuple,
    steps: int,
) -> tuple[IntegerTuple, ...]:
    cells = []
    current = start
    for _ in range(steps):
        current = add(current, direction)
        cells.append(current)
    return tuple(cells)


def _build_relative_path_696d4842(
    directions: tuple[IntegerTuple, ...],
    lengths: tuple[int, ...],
) -> tuple[IntegerTuple, ...]:
    cells = [ORIGIN]
    current = ORIGIN
    for direction, length in zip(directions, lengths):
        segment = _trace_segment_696d4842(current, direction, length)
        cells.extend(segment)
        current = cells[-ONE]
    return tuple(cells)


def _translate_cells_696d4842(
    cells: tuple[IntegerTuple, ...],
    offset: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    return tuple(add(cell, offset) for cell in cells)


def _bounds_696d4842(
    cells: tuple[IntegerTuple, ...],
) -> tuple[int, int, int, int]:
    rows = tuple(cell[ZERO] for cell in cells)
    cols = tuple(cell[ONE] for cell in cells)
    return min(rows), max(rows), min(cols), max(cols)


def _buffer_cells_696d4842(
    cells: frozenset[IntegerTuple],
    side: int,
) -> frozenset[IntegerTuple]:
    out = set()
    for cell in cells:
        area = neighbors(cell) | frozenset({cell})
        for loc in area:
            if ZERO <= loc[ZERO] < side and ZERO <= loc[ONE] < side:
                out.add(loc)
    return frozenset(out)


def _clear_alignment_696d4842(
    endpoint: IntegerTuple,
    dot: IntegerTuple,
    occupied: frozenset[IntegerTuple],
) -> bool:
    aligned = endpoint[ZERO] == dot[ZERO] or endpoint[ONE] == dot[ONE]
    if not aligned:
        return False
    segment = frozenset(connect(endpoint, dot))
    return intersection(segment, occupied) == frozenset({endpoint, dot})


def _pairings_are_unique_696d4842(
    pairs: tuple[dict, ...],
) -> bool:
    occupied = frozenset(
        cell
        for pair in pairs
        for cell in pair["path_cells"] + (pair["dot_cell"],)
    )
    for pair_index, pair in enumerate(pairs):
        dot = pair["dot_cell"]
        matches = [
            (other_index, endpoint_index)
            for other_index, other_pair in enumerate(pairs)
            for endpoint_index, endpoint in enumerate((other_pair["path_cells"][ZERO], other_pair["path_cells"][-ONE]))
            if _clear_alignment_696d4842(endpoint, dot, occupied)
        ]
        if len(matches) != ONE or matches[ZERO][ZERO] != pair_index:
            return False
    return True


def _sample_relative_pair_696d4842(
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[IntegerTuple, ...], tuple[IntegerTuple, ...], IntegerTuple, int]:
    while True:
        horizontal = choice((T, F))
        sign_a = choice((NEG_ONE, ONE))
        sign_b = choice((NEG_ONE, ONE))
        if horizontal:
            dir_a = (ZERO, sign_a)
            dir_b = (sign_b, ZERO)
        else:
            dir_a = (sign_a, ZERO)
            dir_b = (ZERO, sign_b)
        if choice((T, F)):
            directions = (dir_a, dir_b)
            lengths = (
                unifint(diff_lb, diff_ub, (THREE, SIX)),
                unifint(diff_lb, diff_ub, (FOUR, EIGHT)),
            )
        else:
            sign_c = choice((NEG_ONE, ONE))
            if horizontal:
                dir_c = (ZERO, sign_c)
            else:
                dir_c = (sign_c, ZERO)
            directions = (dir_a, dir_b, dir_c)
            lengths = (
                unifint(diff_lb, diff_ub, (TWO, FIVE)),
                unifint(diff_lb, diff_ub, (FOUR, EIGHT)),
                unifint(diff_lb, diff_ub, (ONE, THREE)),
            )
        path_cells = _build_relative_path_696d4842(directions, lengths)
        if len(set(path_cells)) != len(path_cells):
            continue
        if path_cells[ZERO][ZERO] == path_cells[-ONE][ZERO]:
            continue
        if path_cells[ZERO][ONE] == path_cells[-ONE][ONE]:
            continue
        max_gap = min(MAX_GAP_696D4842, len(path_cells) - FOUR)
        if max_gap < MIN_GAP_696D4842:
            continue
        gap = unifint(diff_lb, diff_ub, (MIN_GAP_696D4842, max_gap))
        final_dir = subtract(path_cells[-ONE], path_cells[-TWO])
        end = path_cells[-ONE]
        bridge = tuple(
            add(end, multiply(final_dir, step))
            for step in range(ONE, gap + ONE)
        )
        dot = add(end, multiply(final_dir, gap + ONE))
        return path_cells, bridge, dot, gap


def _place_pair_696d4842(
    side: int,
    top_half: bool,
    reserved: frozenset[IntegerTuple],
    diff_lb: float,
    diff_ub: float,
) -> dict:
    mid = side // TWO
    for _ in range(400):
        path_cells, bridge_cells, dot_cell, gap = _sample_relative_pair_696d4842(diff_lb, diff_ub)
        output_cells = path_cells + bridge_cells + (dot_cell,)
        path_min_i, path_max_i, path_min_j, path_max_j = _bounds_696d4842(path_cells)
        out_min_i, out_max_i, out_min_j, out_max_j = _bounds_696d4842(output_cells)
        row_lb = max(-out_min_i, ONE - path_min_i)
        row_ub = min(side - ONE - out_max_i, side - TWO - path_max_i)
        col_lb = max(-out_min_j, ONE - path_min_j)
        col_ub = min(side - ONE - out_max_j, side - TWO - path_max_j)
        if top_half:
            row_ub = min(row_ub, mid + ONE - out_max_i)
        else:
            row_lb = max(row_lb, mid - ONE - out_min_i)
        if row_lb > row_ub or col_lb > col_ub:
            continue
        for _ in range(80):
            offset = (randint(row_lb, row_ub), randint(col_lb, col_ub))
            path_abs = _translate_cells_696d4842(path_cells, offset)
            bridge_abs = _translate_cells_696d4842(bridge_cells, offset)
            dot_abs = add(dot_cell, offset)
            final_cells = frozenset(path_abs + bridge_abs + (dot_abs,))
            if len(final_cells) != len(path_abs) + len(bridge_abs) + ONE:
                continue
            buffered = _buffer_cells_696d4842(final_cells, side)
            if len(buffered & reserved) > ZERO:
                continue
            return {
                "path_cells": path_abs,
                "bridge_cells": bridge_abs,
                "dot_cell": dot_abs,
                "gap": gap,
                "buffered": buffered,
            }
    raise RuntimeError("failed to place pair for 696d4842")


def generate_696d4842(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        side = choice(GRID_SIDES_696D4842)
        colors = tuple(sample(remove(ZERO, interval(ZERO, TEN, ONE)), FOUR))
        pair_colors = (
            (colors[ZERO], colors[TWO]),
            (colors[ONE], colors[THREE]),
        )
        reserved = frozenset()
        pairs = []
        for pair_index in range(PAIR_COUNT_696D4842):
            pair = _place_pair_696d4842(
                side,
                pair_index == ZERO,
                reserved,
                diff_lb,
                diff_ub,
            )
            reserved = reserved | pair["buffered"]
            pairs.append(pair)
        pairs = tuple(pairs)
        if not _pairings_are_unique_696d4842(pairs):
            continue
        gi = canvas(ZERO, (side, side))
        go = canvas(ZERO, (side, side))
        for pair, colors_for_pair in zip(pairs, pair_colors):
            shape_color, dot_color = colors_for_pair
            path_patch = frozenset(pair["path_cells"])
            bridge_patch = frozenset(pair["bridge_cells"])
            dot_patch = frozenset({pair["dot_cell"]})
            recolor_patch = frozenset(pair["path_cells"][:pair["gap"]])
            gi = fill(gi, shape_color, path_patch)
            gi = fill(gi, dot_color, dot_patch)
            go = fill(go, shape_color, path_patch)
            go = fill(go, shape_color, bridge_patch)
            go = fill(go, dot_color, recolor_patch)
            go = fill(go, dot_color, dot_patch)
        return {"input": gi, "output": go}
