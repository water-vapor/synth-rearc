from __future__ import annotations

from synth_rearc.core import *

from .verifier import (
    MARKER_MISSING_BOTTOM_LEFT_604001fa,
    MARKER_MISSING_BOTTOM_RIGHT_604001fa,
    MARKER_MISSING_TOP_LEFT_604001fa,
    verify_604001fa,
)


MARKER_TO_COLOR_604001fa = {
    MARKER_MISSING_TOP_LEFT_604001fa: THREE,
    MARKER_MISSING_BOTTOM_RIGHT_604001fa: SIX,
    MARKER_MISSING_BOTTOM_LEFT_604001fa: FOUR,
    frozenset({(ZERO, ZERO), (ONE, ZERO), (ONE, ONE)}): EIGHT,
}
MARKER_SHAPES_604001fa = tuple(MARKER_TO_COLOR_604001fa)
ROW_LAYOUTS_604001fa = {
    ONE: ((ONE,),),
    TWO: ((TWO,), (ONE, ONE)),
    THREE: ((TWO, ONE), (ONE, TWO)),
    FOUR: ((TWO, TWO),),
}


def _shape_rows_604001fa(shape_patch: frozenset[tuple[int, int]]) -> tuple[int, ...]:
    return tuple(sum(ONE for i, _ in shape_patch if i == row) for row in interval(ZERO, height(shape_patch), ONE))


def _is_single_object_604001fa(shape_patch: frozenset[tuple[int, int]]) -> bool:
    h = height(shape_patch)
    w = width(shape_patch)
    grid = fill(canvas(ZERO, (h, w)), ONE, shape_patch)
    return size(objects(grid, T, T, T)) == ONE


def _candidate_cols_604001fa(prev_cols: tuple[int, ...], box_w: int) -> tuple[int, ...]:
    return tuple(sorted({ncol for col in prev_cols for ncol in (col - ONE, col, col + ONE) if ZERO <= ncol < box_w}))


def _make_shape_604001fa(diff_lb: float, diff_ub: float) -> frozenset[tuple[int, int]]:
    for _ in range(200):
        box_h = unifint(diff_lb, diff_ub, (THREE, FOUR))
        box_w = unifint(diff_lb, diff_ub, (THREE, FOUR))
        top_count = unifint(diff_lb, diff_ub, (TWO, box_w))
        top_cols = tuple(sorted(sample(tuple(range(box_w)), top_count)))
        occupied = {(ZERO, col) for col in top_cols}
        prev_cols = top_cols
        for row in range(ONE, box_h):
            candidates = _candidate_cols_604001fa(prev_cols, box_w)
            remaining_rows = box_h - row - ONE
            min_needed = max(ZERO, SIX - len(occupied) - remaining_rows * box_w)
            row_count = unifint(diff_lb, diff_ub, (ONE, len(candidates)))
            row_count = min(len(candidates), max(row_count, min_needed))
            row_cols = tuple(sorted(sample(candidates, row_count)))
            occupied.update((row, col) for col in row_cols)
            prev_cols = row_cols
        shape_patch = normalize(frozenset(occupied))
        if height(shape_patch) < THREE or width(shape_patch) < THREE:
            continue
        if size(shape_patch) < SIX:
            continue
        if size(shape_patch) == height(shape_patch) * width(shape_patch):
            continue
        if not _is_single_object_604001fa(shape_patch):
            continue
        row_sizes = _shape_rows_604001fa(shape_patch)
        if row_sizes[ZERO] < TWO:
            continue
        if maximum(row_sizes) < TWO:
            continue
        return shape_patch
    raise RuntimeError("failed to generate shape for 604001fa")


def _marker_anchor_604001fa(marker_shape: frozenset[tuple[int, int]], obj_w: int) -> int:
    if marker_shape == MARKER_MISSING_BOTTOM_LEFT_604001fa and choice((True, False, False, False)):
        return ZERO
    return min(ONE, obj_w - TWO)


def _make_pair_604001fa(diff_lb: float, diff_ub: float) -> tuple[Object, Object, IntegerTuple]:
    marker_shape = choice(MARKER_SHAPES_604001fa)
    out_color = MARKER_TO_COLOR_604001fa[marker_shape]
    shape_patch = _make_shape_604001fa(diff_lb, diff_ub)
    obj_h = height(shape_patch)
    obj_w = width(shape_patch)
    anchor = _marker_anchor_604001fa(marker_shape, obj_w)
    marker_patch = shift(marker_shape, (ZERO, anchor))
    input_obj = recolor(ONE, shift(shape_patch, (TWO, ZERO)))
    marker_obj = recolor(SEVEN, marker_patch)
    output_obj = recolor(out_color, shift(shape_patch, (TWO, ZERO)))
    pair_dims = (obj_h + TWO, obj_w)
    return combine(input_obj, marker_obj), output_obj, pair_dims


def _layout_rows_604001fa(npairs: int) -> tuple[int, ...]:
    return choice(ROW_LAYOUTS_604001fa[npairs])


def generate_604001fa(diff_lb: float, diff_ub: float) -> dict:
    while True:
        npairs = unifint(diff_lb, diff_ub, (ONE, FOUR))
        pairs = tuple(_make_pair_604001fa(diff_lb, diff_ub) for _ in range(npairs))
        row_layout = _layout_rows_604001fa(npairs)
        left_margin = unifint(diff_lb, diff_ub, (ZERO, TWO))
        top_margin = unifint(diff_lb, diff_ub, (ZERO, TWO))
        right_margin = unifint(diff_lb, diff_ub, (ZERO, TWO))
        bottom_margin = unifint(diff_lb, diff_ub, (ZERO, TWO))
        placements: list[IntegerTuple] = []
        row_cursor = top_margin
        pair_cursor = ZERO
        max_right = ZERO
        for row_count in row_layout:
            row_pairs = pairs[pair_cursor:pair_cursor + row_count]
            row_height = maximum(tuple(dims[ZERO] for _, _, dims in row_pairs)) + ONE
            col_cursor = left_margin
            for input_obj, _, dims in row_pairs:
                jitter = randint(ZERO, row_height - dims[ZERO])
                placements.append((row_cursor + jitter, col_cursor))
                max_right = max(max_right, col_cursor + dims[ONE])
                col_cursor += dims[ONE] + randint(TWO, FOUR)
            row_cursor += row_height + randint(TWO, FOUR)
            pair_cursor += row_count
        total_height = maximum(tuple(pi + dims[ZERO] for (_, _, dims), (pi, _) in zip(pairs, placements))) + bottom_margin
        total_width = max(max_right, maximum(tuple(pj + dims[ONE] for (_, _, dims), (_, pj) in zip(pairs, placements)))) + right_margin
        total_height = max(total_height, EIGHT)
        total_width = max(total_width, SIX)
        if total_height > 30 or total_width > 30:
            continue
        gi = canvas(ZERO, (total_height, total_width))
        go = canvas(ZERO, (total_height, total_width))
        for (input_obj, output_obj, _), offset in zip(pairs, placements):
            gi = paint(gi, shift(input_obj, offset))
            go = paint(go, shift(output_obj, offset))
        if verify_604001fa(gi) != go:
            continue
        return {"input": gi, "output": go}
