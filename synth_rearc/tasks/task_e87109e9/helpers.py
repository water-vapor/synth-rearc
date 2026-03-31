from __future__ import annotations

from synth_rearc.core import *


HEADER_HEIGHT_E87109E9 = SIX
LEGEND_BORDER_COLOR_E87109E9 = FIVE
LEGEND_GAP_COLOR_E87109E9 = ZERO
SEED_COLOR_E87109E9 = EIGHT
CHAMBER_WIDTH_E87109E9 = SIX
CHAMBER_COUNT_E87109E9 = FOUR

TURN_CW_E87109E9 = "cw"
TURN_CCW_E87109E9 = "ccw"

DIRECTION_ORDER_E87109E9 = ("up", "right", "down", "left")
DIRECTION_VECTOR_E87109E9 = {
    "up": UP,
    "right": RIGHT,
    "down": DOWN,
    "left": LEFT,
}
CLOCKWISE_E87109E9 = {
    "up": "right",
    "right": "down",
    "down": "left",
    "left": "up",
}
COUNTERCLOCKWISE_E87109E9 = {x1: x0 for x0, x1 in CLOCKWISE_E87109E9.items()}


def rect_patch_e87109e9(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    return frozenset(
        (i, j)
        for i in range(top, top + height_value)
        for j in range(left, left + width_value)
    )


def strip_header_e87109e9(
    grid: Grid,
) -> Grid:
    return tuple(grid[HEADER_HEIGHT_E87109E9:])


def parse_turns_e87109e9(
    grid: Grid,
) -> dict[Integer, str]:
    x0: dict[Integer, str] = {}
    for x1 in range(CHAMBER_COUNT_E87109E9):
        x2 = x1 * CHAMBER_WIDTH_E87109E9
        x3 = tuple(
            (i, j, grid[i][j])
            for i in range(ONE, HEADER_HEIGHT_E87109E9 - ONE)
            for j in range(x2 + ONE, x2 + CHAMBER_WIDTH_E87109E9 - ONE)
            if grid[i][j] not in (LEGEND_BORDER_COLOR_E87109E9, LEGEND_GAP_COLOR_E87109E9)
        )
        x4 = tuple(v for _, _, v in x3)
        x5 = first(dedupe(x4))
        x6 = minimum(tuple(j for _, j, _ in x3)) - x2
        x7 = TURN_CCW_E87109E9 if x6 == ONE else TURN_CW_E87109E9
        x0[x5] = x7
    return x0


def build_header_e87109e9(
    turns_by_color: dict[Integer, str],
) -> Grid:
    x0 = canvas(LEGEND_BORDER_COLOR_E87109E9, (HEADER_HEIGHT_E87109E9, CHAMBER_WIDTH_E87109E9 * CHAMBER_COUNT_E87109E9))
    x1 = tuple(turns_by_color.items())
    for x2, (x3, x4) in enumerate(x1):
        x5 = x2 * CHAMBER_WIDTH_E87109E9
        x6 = x5 + (ONE if x4 == TURN_CCW_E87109E9 else FOUR)
        x7 = rect_patch_e87109e9(ONE, x5 + ONE, FOUR, FOUR)
        x8 = rect_patch_e87109e9(ONE, x6, FOUR, ONE)
        x0 = fill(x0, LEGEND_GAP_COLOR_E87109E9, x7)
        x0 = fill(x0, x3, x8)
    return x0


def extract_seed_object_e87109e9(
    grid: Grid,
) -> Object:
    x0 = objects(grid, T, F, T)
    return extract(x0, matcher(color, SEED_COLOR_E87109E9))


def seed_block_e87109e9(
    grid: Grid,
) -> tuple[Integer, Integer, Integer]:
    x0 = extract_seed_object_e87109e9(grid)
    x1 = uppermost(x0)
    x2 = leftmost(x0)
    x3 = height(x0)
    return x1, x2, x3


def obstacle_map_e87109e9(
    grid: Grid,
) -> tuple[Integer, dict[IntegerTuple, Integer]]:
    x0 = mostcolor(grid)
    x1 = objects(grid, T, F, T)
    x2 = remove(extract(x1, matcher(color, SEED_COLOR_E87109E9)), x1)
    x3 = {
        x5: color(x4)
        for x4 in x2
        for x5 in toindices(x4)
    }
    return x0, x3


def _block_patch_e87109e9(
    top: Integer,
    left: Integer,
    size_value: Integer,
) -> Indices:
    return rect_patch_e87109e9(top, left, size_value, size_value)


def _advance_segment_e87109e9(
    block: IntegerTuple,
    direction_name: str,
    size_value: Integer,
    dims: IntegerTuple,
    occupied: dict[IntegerTuple, Integer],
) -> tuple[Indices, IntegerTuple, frozenset[Integer], str]:
    x0, x1 = block
    x2, x3 = dims
    x4, x5 = DIRECTION_VECTOR_E87109E9[direction_name]
    x6 = frozenset()
    while T:
        x7 = x0 + x4
        x8 = x1 + x5
        x9 = _block_patch_e87109e9(x7, x8, size_value)
        x10 = any(i < ZERO or i >= x2 or j < ZERO or j >= x3 for i, j in x9)
        if x10:
            return x6, (x0, x1), frozenset(), "border"
        x11 = frozenset(occupied[x12] for x12 in x9 if x12 in occupied)
        if len(x11) > ZERO:
            return x6, (x0, x1), x11, "object"
        x6 = combine(x6, x9)
        x0 = x7
        x1 = x8


def trace_metadata_e87109e9(
    grid: Grid,
    turns_by_color: dict[Integer, str],
) -> dict[str, object]:
    x0 = shape(grid)
    x1, x2, x3 = seed_block_e87109e9(grid)
    x4 = obstacle_map_e87109e9(grid)[1]
    x5 = _block_patch_e87109e9(x1, x2, x3)
    x6 = set(x5)
    x7 = set()
    x8 = F
    x9 = ZERO
    for x10 in DIRECTION_ORDER_E87109E9:
        x11 = (x1, x2)
        x12 = x10
        x13 = set()
        while T:
            x14 = (x11, x12)
            if x14 in x13:
                x8 = T
                break
            x13.add(x14)
            x15, x11, x16, x17 = _advance_segment_e87109e9(x11, x12, x3, x0, x4)
            x6 |= set(x15)
            x9 = x9 + (ONE if len(x15) > ZERO else ZERO)
            if x17 != "object" or len(x16) != ONE:
                break
            x18 = first(tuple(x16))
            if x18 not in turns_by_color:
                break
            x7.add(x18)
            x19 = turns_by_color[x18]
            x12 = CLOCKWISE_E87109E9[x12] if x19 == TURN_CW_E87109E9 else COUNTERCLOCKWISE_E87109E9[x12]
    return {
        "path": frozenset(x6),
        "hit_colors": frozenset(x7),
        "cycle": x8,
        "segments": x9,
    }


def render_output_e87109e9(
    grid: Grid,
    turns_by_color: dict[Integer, str],
) -> Grid:
    x0 = trace_metadata_e87109e9(grid, turns_by_color)
    return fill(grid, SEED_COLOR_E87109E9, x0["path"])
