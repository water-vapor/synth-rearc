from arc2.core import *

from .helpers import (
    CORNER_NAMES_902510D5,
    corner_cell_902510d5,
    corner_cells_902510d5,
    corner_name_from_cell_902510d5,
    neighborhood_902510d5,
    triangle_patch_902510d5,
)


ALL_COLORS_902510D5 = tuple(remove(ZERO, interval(ZERO, TEN, ONE)))
GRID_HEIGHT_BOUNDS_902510D5 = (8, 15)
GRID_WIDTH_BOUNDS_902510D5 = (8, 15)
TRIANGLE_SIZE_BOUNDS_902510D5 = (2, 6)
MAX_MAIN_ATTEMPTS_902510D5 = 96
MAX_PLACEMENT_ATTEMPTS_902510D5 = 96
# The official fixed object is consistently a sparse hammer-like motif under symmetry.
HAMMER_TEMPLATES_902510D5 = (
    frozenset({(0, 0), (1, 1), (2, 2), (1, 3), (3, 1)}),
    frozenset({(0, 0), (1, 1), (2, 2), (1, 3), (2, 3), (3, 1), (3, 2)}),
    frozenset({(0, 1), (1, 2), (2, 2), (2, 3), (3, 1), (3, 4), (4, 0)}),
    frozenset(
        {
            (0, 3),
            (0, 4),
            (0, 5),
            (1, 2),
            (2, 1),
            (2, 2),
            (3, 0),
            (3, 3),
            (4, 0),
            (4, 4),
            (5, 0),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
        }
    ),
)
HAMMER_TEMPLATE_WEIGHTS_902510D5 = (0, 0, 1, 2, 3)
HAMMER_TEMPLATE_TIPS_902510D5 = (
    (ZERO, ZERO),
    (ZERO, ZERO),
    (FOUR, ZERO),
    (EIGHT, EIGHT),
)


def _sample_dims_902510d5(
    diff_lb: float,
    diff_ub: float,
    side: Integer,
) -> IntegerTuple:
    h = unifint(diff_lb, diff_ub, (max(GRID_HEIGHT_BOUNDS_902510D5[ZERO], side + FOUR), GRID_HEIGHT_BOUNDS_902510D5[ONE]))
    w = unifint(diff_lb, diff_ub, (max(GRID_WIDTH_BOUNDS_902510D5[ZERO], side + FOUR), GRID_WIDTH_BOUNDS_902510D5[ONE]))
    return (h, w)


def _sample_main_patch_902510d5(
    diff_lb: float,
    diff_ub: float,
    target_corner: str,
) -> frozenset[IntegerTuple]:
    del diff_lb, diff_ub
    idx = choice(HAMMER_TEMPLATE_WEIGHTS_902510D5)
    patch = HAMMER_TEMPLATES_902510D5[idx]
    tip = HAMMER_TEMPLATE_TIPS_902510D5[idx]
    return _orient_main_patch_902510d5(patch, tip, target_corner)


def _normalize_with_tip_902510d5(
    patch: frozenset[IntegerTuple],
    tip: IntegerTuple,
) -> tuple[frozenset[IntegerTuple], IntegerTuple]:
    a = min(i for i, _ in patch)
    b = min(j for _, j in patch)
    normalized = frozenset((i - a, j - b) for i, j in patch)
    return normalized, (tip[ZERO] - a, tip[ONE] - b)


def _rot90_with_tip_902510d5(
    patch: frozenset[IntegerTuple],
    tip: IntegerTuple,
) -> tuple[frozenset[IntegerTuple], IntegerTuple]:
    h, _ = shape(patch)
    rotated = frozenset((j, h - ONE - i) for i, j in patch)
    rotated_tip = (tip[ONE], h - ONE - tip[ZERO])
    return _normalize_with_tip_902510d5(rotated, rotated_tip)


def _hmirror_with_tip_902510d5(
    patch: frozenset[IntegerTuple],
    tip: IntegerTuple,
) -> tuple[frozenset[IntegerTuple], IntegerTuple]:
    _, w = shape(patch)
    mirrored = frozenset((i, w - ONE - j) for i, j in patch)
    mirrored_tip = (tip[ZERO], w - ONE - tip[ONE])
    return _normalize_with_tip_902510d5(mirrored, mirrored_tip)


def _orient_main_patch_902510d5(
    patch: frozenset[IntegerTuple],
    tip: IntegerTuple,
    target_corner: str,
) -> frozenset[IntegerTuple]:
    patch, tip = _normalize_with_tip_902510d5(patch, tip)
    variants = []
    seen = set()
    current_patch = patch
    current_tip = tip
    for _ in range(FOUR):
        for variant_patch, variant_tip in (current_patch, current_tip), _hmirror_with_tip_902510d5(current_patch, current_tip):
            key = tuple(sorted(variant_patch))
            if key in seen:
                continue
            seen.add(key)
            if corner_name_from_cell_902510d5(variant_tip, shape(variant_patch)) == target_corner:
                variants.append(variant_patch)
        current_patch, current_tip = _rot90_with_tip_902510d5(current_patch, current_tip)
    return choice(tuple(variants))


def _place_main_patch_902510d5(
    dims: IntegerTuple,
    forbidden: frozenset[IntegerTuple],
    diff_lb: float,
    diff_ub: float,
    target_corner: str,
) -> frozenset[IntegerTuple]:
    h, w = dims
    for _ in range(MAX_MAIN_ATTEMPTS_902510D5):
        patch = _sample_main_patch_902510d5(diff_lb, diff_ub, target_corner)
        ph, pw = shape(patch)
        if ph > h or pw > w:
            continue
        for _ in range(MAX_PLACEMENT_ATTEMPTS_902510D5):
            top = randint(ZERO, h - ph)
            left = randint(ZERO, w - pw)
            placed = shift(patch, (top, left))
            if len(toindices(placed) & forbidden) != ZERO:
                continue
            return toindices(placed)
    return frozenset()


def _place_singletons_902510d5(
    dims: IntegerTuple,
    blocked: frozenset[IntegerTuple],
    count: Integer,
) -> tuple[IntegerTuple, ...]:
    h, w = dims
    taken = set(blocked)
    cells = []
    for _ in range(count):
        options = [
            (i, j)
            for i in range(h)
            for j in range(w)
            if (i, j) not in taken
        ]
        if len(options) == ZERO:
            return tuple()
        cell = choice(options)
        cells.append(cell)
        taken |= neighborhood_902510d5({cell})
    return tuple(cells)


def _sample_marker_colors_902510d5(
    side: Integer,
    main_color: Integer,
) -> tuple[Integer, Integer, tuple[Integer, ...]]:
    fill_color = choice(tuple(color for color in ALL_COLORS_902510D5 if color != main_color))
    if randint(ZERO, THREE) == ZERO:
        corner_color = fill_color
    else:
        corner_pool = tuple(color for color in ALL_COLORS_902510D5 if color not in (main_color, fill_color))
        corner_color = choice(corner_pool)
    if side == TWO:
        fill_count = TWO
    else:
        fill_count = randint(TWO, min(side, FOUR))
    fill_count = min(fill_count, side)
    distractor_pool = tuple(color for color in ALL_COLORS_902510D5 if color != fill_color)
    distractors = tuple(sample(distractor_pool, side - fill_count))
    colors = (fill_color,) * fill_count + distractors
    colors = tuple(colors[idx] for idx in sample(range(len(colors)), len(colors)))
    return corner_color, fill_color, colors


def _render_input_902510d5(
    dims: IntegerTuple,
    main_patch: frozenset[IntegerTuple],
    main_color: Integer,
    corner: str,
    corner_color: Integer,
    singletons: tuple[tuple[Integer, IntegerTuple], ...],
) -> Grid:
    grid = canvas(ZERO, dims)
    grid = paint(grid, recolor(main_color, main_patch))
    grid = fill(grid, corner_color, {corner_cell_902510d5(corner, dims)})
    for value, cell in singletons:
        grid = fill(grid, value, {cell})
    return grid


def _render_output_902510d5(
    dims: IntegerTuple,
    main_patch: frozenset[IntegerTuple],
    main_color: Integer,
    corner: str,
    fill_color: Integer,
    side: Integer,
) -> Grid:
    grid = canvas(ZERO, dims)
    grid = paint(grid, recolor(main_color, main_patch))
    return fill(grid, fill_color, triangle_patch_902510d5(corner, side, dims))


def generate_902510d5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        side = unifint(diff_lb, diff_ub, TRIANGLE_SIZE_BOUNDS_902510D5)
        dims = _sample_dims_902510d5(diff_lb, diff_ub, side)
        corner = choice(CORNER_NAMES_902510D5)
        output_triangle = triangle_patch_902510d5(corner, side, dims)
        main_color = choice(ALL_COLORS_902510D5)
        forbidden = neighborhood_902510d5(output_triangle)
        main_patch = _place_main_patch_902510d5(dims, forbidden, diff_lb, diff_ub, corner)
        if len(main_patch) < FIVE:
            continue
        blocked = neighborhood_902510d5(main_patch) | output_triangle
        blocked |= neighborhood_902510d5({corner_cell_902510d5(corner, dims)})
        blocked |= corner_cells_902510d5(dims)
        singleton_cells = _place_singletons_902510d5(dims, blocked, side)
        if len(singleton_cells) != side:
            continue
        corner_color, fill_color, singleton_colors = _sample_marker_colors_902510d5(side, main_color)
        singletons = tuple(pair for pair in zip(singleton_colors, singleton_cells))
        gi = _render_input_902510d5(dims, main_patch, main_color, corner, corner_color, singletons)
        go = _render_output_902510d5(dims, main_patch, main_color, corner, fill_color, side)
        if gi == go:
            continue
        return {"input": gi, "output": go}
