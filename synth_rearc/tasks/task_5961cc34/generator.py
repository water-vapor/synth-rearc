from synth_rearc.core import *

from .helpers import (
    OPPOSITE_SIDE_5961CC34,
    SHAPE_LIBRARY_5961CC34,
    SIDE_TO_VECTOR_5961CC34,
    VECTOR_TO_SIDE_5961CC34,
    expand4_5961cc34,
    in_bounds_5961cc34,
    marker_patch_5961cc34,
    orient_patch_5961cc34,
    paired_segment_5961cc34,
    place_shape_on_ray_5961cc34,
    ray_to_border_5961cc34,
    side_patch_5961cc34,
    subset_options_5961cc34,
)
from .verifier import verify_5961cc34


BG_COLOR_5961CC34 = EIGHT
OBJ_COLOR_5961CC34 = ONE
PATH_COLOR_5961CC34 = TWO
MARKER_COLOR_5961CC34 = THREE
HEAD_COLOR_5961CC34 = FOUR

HEIGHT_RANGE_5961CC34 = (13, 28)
WIDTH_RANGE_5961CC34 = (15, 29)
SEED_LENGTH_RANGE_5961CC34 = (TWO, THREE)
PATH_OBJECT_RANGE_5961CC34 = (ZERO, THREE)
DISTRACTOR_RANGE_5961CC34 = (ZERO, THREE)
DISTANCE_RANGE_5961CC34 = (TWO, EIGHT)


def _entry_side_5961cc34(
    direction: tuple[int, int],
) -> str:
    x0 = VECTOR_TO_SIDE_5961CC34[direction]
    return OPPOSITE_SIDE_5961CC34[x0]


def _shape_variants_5961cc34(
    direction: tuple[int, int],
    width0: Integer,
) -> tuple[Indices, ...]:
    x0 = _entry_side_5961cc34(direction)
    x1 = []
    for base in SHAPE_LIBRARY_5961CC34:
        for turns in range(FOUR):
            x2 = orient_patch_5961cc34(base, turns)
            if size(side_patch_5961cc34(x2, x0)) >= width0:
                x1.append(x2)
    return tuple(x1)


def _candidate_exit_sides_5961cc34(
    direction: tuple[int, int],
) -> tuple[str, ...]:
    x0 = _entry_side_5961cc34(direction)
    return tuple(side for side in ("u", "d", "l", "r") if side != x0)


def _reserve_pair_5961cc34(
    obj: Patch,
    marker: Patch,
) -> Indices:
    return expand4_5961cc34(toindices(obj) | toindices(marker))


def _try_place_path_object_5961cc34(
    current_patch: Patch,
    direction: tuple[int, int],
    dims: tuple[int, int],
    occupied: Patch,
    pair_reserved: Patch,
) -> tuple[Indices, Indices, Indices, tuple[int, int]] | None:
    x0 = size(current_patch)
    x1 = _entry_side_5961cc34(direction)
    x2 = _shape_variants_5961cc34(direction, x0)
    for _ in range(120):
        x3 = choice(x2)
        x4 = side_patch_5961cc34(x3, x1)
        x5 = subset_options_5961cc34(x4, x0, direction)
        if len(x5) == ZERO:
            continue
        x6 = choice(x5)
        x7 = unifint(0.0, 1.0, DISTANCE_RANGE_5961CC34)
        x8, x9 = place_shape_on_ray_5961cc34(current_patch, direction, x3, x1, x6, x7)
        if not in_bounds_5961cc34(x8, dims):
            continue
        x10 = _candidate_exit_sides_5961cc34(direction)
        x11 = choice(x10)
        x12 = marker_patch_5961cc34(x8, x11)
        if not in_bounds_5961cc34(x12, dims):
            continue
        x13 = paired_segment_5961cc34(current_patch, x9, direction)
        x14 = (toindices(x13) | toindices(x8) | toindices(x12)) - toindices(current_patch)
        if len(x14 & toindices(occupied)) != ZERO:
            continue
        x15 = _reserve_pair_5961cc34(x8, x12)
        if len(x15 & toindices(pair_reserved)) != ZERO:
            continue
        return x8, x13, x12, SIDE_TO_VECTOR_5961CC34[x11]
    return None


def _try_place_distractor_5961cc34(
    dims: tuple[int, int],
    occupied: Patch,
    pair_reserved: Patch,
) -> tuple[Indices, Indices] | None:
    h, w = dims
    for _ in range(120):
        x0 = choice(SHAPE_LIBRARY_5961CC34)
        x1 = orient_patch_5961cc34(x0, randint(ZERO, THREE))
        x2 = h - height(x1)
        x3 = w - width(x1)
        if x2 < ZERO or x3 < ZERO:
            continue
        x4 = shift(x1, (randint(ZERO, x2), randint(ZERO, x3)))
        x5 = choice(("u", "d", "l", "r"))
        x6 = marker_patch_5961cc34(x4, x5)
        if not in_bounds_5961cc34(x6, dims):
            continue
        x7 = toindices(x4) | toindices(x6)
        if len(x7 & toindices(occupied)) != ZERO:
            continue
        x8 = _reserve_pair_5961cc34(x4, x6)
        if len(x8 & toindices(pair_reserved)) != ZERO:
            continue
        return x4, x6
    return None


def generate_5961cc34(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = unifint(diff_lb, diff_ub, HEIGHT_RANGE_5961CC34)
        w = unifint(diff_lb, diff_ub, WIDTH_RANGE_5961CC34)
        seed_len = unifint(diff_lb, diff_ub, SEED_LENGTH_RANGE_5961CC34)
        anchor_col = randint(TWO, w - THREE)
        blue_patch = frozenset((h - seed_len + k, anchor_col) for k in range(seed_len))
        gray_patch = initset((h - seed_len - ONE, anchor_col))
        occupied = toindices(blue_patch) | toindices(gray_patch)
        pair_reserved = frozenset()
        path_cells = toindices(blue_patch)
        path_shapes = []
        path_markers = []
        current_patch = gray_patch
        current_direction = (-1, 0)
        pair_count = unifint(diff_lb, diff_ub, PATH_OBJECT_RANGE_5961CC34)
        ok = True
        for _ in range(pair_count):
            placed = _try_place_path_object_5961cc34(
                current_patch,
                current_direction,
                (h, w),
                occupied,
                pair_reserved,
            )
            if placed is None:
                ok = False
                break
            obj_patch, connector_patch, marker_patch, next_direction = placed
            path_shapes.append(obj_patch)
            path_markers.append(marker_patch)
            path_cells = path_cells | toindices(connector_patch) | toindices(obj_patch)
            occupied = toindices(occupied) | toindices(connector_patch) | toindices(obj_patch) | toindices(marker_patch)
            pair_reserved = toindices(pair_reserved) | _reserve_pair_5961cc34(obj_patch, marker_patch)
            current_patch = marker_patch
            current_direction = next_direction
        if not ok:
            continue
        final_segment = ray_to_border_5961cc34(current_patch, current_direction, (h, w))
        if len((toindices(final_segment) - toindices(current_patch)) & toindices(occupied)) != ZERO:
            continue
        path_cells = path_cells | toindices(final_segment)
        occupied = toindices(occupied) | toindices(final_segment)
        distractors = []
        distractor_count = unifint(diff_lb, diff_ub, DISTRACTOR_RANGE_5961CC34)
        for _ in range(distractor_count):
            placed = _try_place_distractor_5961cc34((h, w), occupied, pair_reserved)
            if placed is None:
                continue
            obj_patch, marker_patch = placed
            distractors.append(placed)
            occupied = toindices(occupied) | toindices(obj_patch) | toindices(marker_patch)
            pair_reserved = toindices(pair_reserved) | _reserve_pair_5961cc34(obj_patch, marker_patch)
        gi = canvas(BG_COLOR_5961CC34, (h, w))
        go = canvas(BG_COLOR_5961CC34, (h, w))
        gi = fill(gi, PATH_COLOR_5961CC34, blue_patch)
        gi = fill(gi, HEAD_COLOR_5961CC34, gray_patch)
        for obj_patch, marker_patch in zip(path_shapes, path_markers):
            gi = fill(gi, OBJ_COLOR_5961CC34, obj_patch)
            gi = fill(gi, MARKER_COLOR_5961CC34, marker_patch)
        for obj_patch, marker_patch in distractors:
            gi = fill(gi, OBJ_COLOR_5961CC34, obj_patch)
            gi = fill(gi, MARKER_COLOR_5961CC34, marker_patch)
        go = fill(go, PATH_COLOR_5961CC34, path_cells)
        if verify_5961cc34(gi) != go:
            continue
        return {"input": gi, "output": go}
