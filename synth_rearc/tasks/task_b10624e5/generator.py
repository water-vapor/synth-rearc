from synth_rearc.core import *

from .helpers import (
    ANCHOR_10624E5,
    BACKGROUND_10624E5,
    CROSS_INDEX_10624E5,
    DIVIDER_10624E5,
    GRID_SIZE_10624E5,
    MOTIF_COLORS_10624E5,
    MOTIF_TEMPLATES_10624E5,
    foreground_objects_10624e5,
    rectangle_object_10624e5,
    render_output_10624e5,
)


MOTIF_FAMILIES_10624E5 = (
    ("up_full", "right_full"),
    ("up_full", "right_full", "down_full"),
    ("up_half_right", "diag_up_left_half", "left_half", "right_full"),
    ("up_half_right", "diag_up_left_half", "left_half", "down_full"),
    ("up_full", "diag_up_left_full", "left_double", "down_full"),
    ("diag_up_left_full", "left_double", "up_full"),
    ("left_half", "right_full", "down_full"),
    ("diag_up_left_full", "up_full", "right_full"),
)
TARGET_SIZE_POOLS_10624E5 = {
    "tr": (TWO, TWO, THREE, THREE, FOUR),
    "bl": (ONE, ONE, TWO, FOUR, FOUR),
    "br": (TWO, THREE, THREE, FOUR, FOUR),
}


def _cross_indices_10624e5() -> Indices:
    x0 = connect((CROSS_INDEX_10624E5, ZERO), (CROSS_INDEX_10624E5, decrement(GRID_SIZE_10624E5)))
    x1 = connect((ZERO, CROSS_INDEX_10624E5), (decrement(GRID_SIZE_10624E5), CROSS_INDEX_10624E5))
    return combine(x0, x1)


def _target_anchor_ul_10624e5(
    quadrant: str,
    size_: Integer,
) -> IntegerTuple:
    if quadrant == "tr":
        return randint(2, 6), randint(18, subtract(23, size_))
    if quadrant == "bl":
        return randint(18, subtract(23, size_)), randint(2, 5)
    return randint(18, subtract(23, size_)), randint(18, subtract(23, size_))


def _source_piece_10624e5(
    anchor_ul: IntegerTuple,
    name: str,
    value: Integer,
) -> Object:
    x0 = MOTIF_TEMPLATES_10624E5[name]
    x1 = add(anchor_ul, x0["offset"])
    return rectangle_object_10624e5(value, x1, x0["dims"])


def _motif_input_grid_10624e5(
    anchor_ul: IntegerTuple,
    family: tuple[str, ...],
    colors: tuple[Integer, ...],
) -> Grid:
    x0 = canvas(BACKGROUND_10624E5, (CROSS_INDEX_10624E5, CROSS_INDEX_10624E5))
    x1 = rectangle_object_10624e5(ANCHOR_10624E5, anchor_ul, (TWO, TWO))
    x2 = paint(x0, x1)
    for x3, x4 in zip(family, colors):
        x5 = _source_piece_10624e5(anchor_ul, x3, x4)
        x2 = paint(x2, x5)
    return x2


def _source_motif_ok_10624e5(
    grid: Grid,
) -> Boolean:
    x0 = objects(grid, F, F, T)
    x1 = equality(size(x0), ONE)
    x2 = contained(ANCHOR_10624E5, palette(grid))
    return both(x1, x2)


def _build_input_10624e5(
    source_anchor_ul: IntegerTuple,
    family: tuple[str, ...],
    colors: tuple[Integer, ...],
    target_specs: tuple[tuple[str, Integer, IntegerTuple], ...],
) -> Grid:
    x0 = canvas(BACKGROUND_10624E5, (GRID_SIZE_10624E5, GRID_SIZE_10624E5))
    x1 = fill(x0, DIVIDER_10624E5, _cross_indices_10624e5())
    x2 = _motif_input_grid_10624e5(source_anchor_ul, family, colors)
    x3 = paint(x1, merge(foreground_objects_10624e5(x2, BACKGROUND_10624E5)))
    for _, x4, x5 in target_specs:
        x6 = rectangle_object_10624e5(ANCHOR_10624E5, x5, (x4, x4))
        x3 = paint(x3, x6)
    return x3


def _divider_preserved_10624e5(
    grid: Grid,
) -> Boolean:
    x0 = _cross_indices_10624e5()
    return all(index(grid, x1) == DIVIDER_10624E5 for x1 in x0)


def _quadrant_changed_10624e5(
    input_grid: Grid,
    output_grid: Grid,
    start: IntegerTuple,
    dims: IntegerTuple,
) -> Boolean:
    x0 = crop(input_grid, start, dims)
    x1 = crop(output_grid, start, dims)
    return x0 != x1


def generate_b10624e5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(MOTIF_FAMILIES_10624E5)
        x1 = list(MOTIF_COLORS_10624E5)
        shuffle(x1)
        x2 = tuple(x1[: len(x0)])
        x3 = (randint(5, 7), randint(5, 7))
        x4 = _motif_input_grid_10624e5(x3, x0, x2)
        if not _source_motif_ok_10624e5(x4):
            continue
        x5 = (
            ("tr", choice(TARGET_SIZE_POOLS_10624E5["tr"])),
            ("bl", choice(TARGET_SIZE_POOLS_10624E5["bl"])),
            ("br", choice(TARGET_SIZE_POOLS_10624E5["br"])),
        )
        x6 = tuple((x7, x8, _target_anchor_ul_10624e5(x7, x8)) for x7, x8 in x5)
        x7 = _build_input_10624e5(x3, x0, x2, x6)
        x8 = render_output_10624e5(x7)
        if not _divider_preserved_10624e5(x8):
            continue
        x9 = (
            ((ZERO, increment(CROSS_INDEX_10624E5)), (CROSS_INDEX_10624E5, CROSS_INDEX_10624E5)),
            ((increment(CROSS_INDEX_10624E5), ZERO), (CROSS_INDEX_10624E5, CROSS_INDEX_10624E5)),
            ((increment(CROSS_INDEX_10624E5), increment(CROSS_INDEX_10624E5)), (CROSS_INDEX_10624E5, CROSS_INDEX_10624E5)),
        )
        if not all(_quadrant_changed_10624e5(x7, x8, x10, x11) for x10, x11 in x9):
            continue
        if x7 == x8:
            continue
        return {"input": x7, "output": x8}
