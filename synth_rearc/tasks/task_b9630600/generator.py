from synth_rearc.core import *

from .helpers import (
    GRID_SHAPE_B9630600,
    HORIZONTAL_B9630600,
    VERTICAL_B9630600,
    build_candidate_edges_b9630600,
    kruskal_edges_b9630600,
    render_input_b9630600,
    render_output_b9630600,
    rooms_touch_b9630600,
    shift_room_b9630600,
)


ROOM_COUNT_BOUNDS_B9630600 = (SIX, SEVEN)
ROOM_HEIGHT_BOUNDS_B9630600 = (THREE, 11)
ROOM_WIDTH_BOUNDS_B9630600 = (THREE, 12)
GAP_BOUNDS_B9630600 = (ONE, SIX)
MAX_ROOM_ATTEMPTS_B9630600 = 96


def _sample_room_shape_b9630600(
    diff_lb: float,
    diff_ub: float,
) -> Tuple:
    x0 = unifint(diff_lb, diff_ub, ROOM_HEIGHT_BOUNDS_B9630600)
    x1 = unifint(diff_lb, diff_ub, ROOM_WIDTH_BOUNDS_B9630600)
    return (x0, x1)


def _place_room_b9630600(
    anchor: Tuple,
    shape: Tuple,
    axis: Integer,
    direction: Integer,
    diff_lb: float,
    diff_ub: float,
) -> Tuple:
    x0, x1 = shape
    x2 = unifint(diff_lb, diff_ub, GAP_BOUNDS_B9630600)
    ar0, ac0, ar1, ac1 = anchor
    if axis == HORIZONTAL_B9630600:
        top = randint(ar0 - x0 + TWO, ar1 - TWO)
        left = ac1 + x2 + ONE if direction == ONE else ac0 - x2 - x1
        return (top, left, top + x0 - ONE, left + x1 - ONE)
    left = randint(ac0 - x1 + TWO, ac1 - TWO)
    top = ar1 + x2 + ONE if direction == ONE else ar0 - x2 - x0
    return (top, left, top + x0 - ONE, left + x1 - ONE)


def _normalize_rooms_b9630600(
    rooms: Tuple,
) -> Tuple:
    x0 = min(room[ZERO] for room in rooms)
    x1 = min(room[ONE] for room in rooms)
    x2 = tuple(shift_room_b9630600(room, (-x0, -x1)) for room in rooms)
    x3 = max(room[TWO] for room in x2)
    x4 = max(room[THREE] for room in x2)
    if x3 >= GRID_SHAPE_B9630600[ZERO] or x4 >= GRID_SHAPE_B9630600[ONE]:
        return tuple()
    x5 = randint(ZERO, GRID_SHAPE_B9630600[ZERO] - x3 - ONE)
    x6 = randint(ZERO, GRID_SHAPE_B9630600[ONE] - x4 - ONE)
    return tuple(shift_room_b9630600(room, (x5, x6)) for room in x2)


def _build_rooms_b9630600(
    diff_lb: float,
    diff_ub: float,
) -> Tuple:
    x0 = unifint(diff_lb, diff_ub, ROOM_COUNT_BOUNDS_B9630600)
    x1, x2 = _sample_room_shape_b9630600(diff_lb, diff_ub)
    x3 = ((ZERO, ZERO, x1 - ONE, x2 - ONE),)
    x4 = ZERO
    while len(x3) < x0 and x4 < MAX_ROOM_ATTEMPTS_B9630600:
        x4 += ONE
        x5 = choice(x3)
        x6 = _sample_room_shape_b9630600(diff_lb, diff_ub)
        x7 = choice((HORIZONTAL_B9630600, VERTICAL_B9630600))
        x8 = choice((NEG_ONE, ONE))
        x9 = _place_room_b9630600(x5, x6, x7, x8, diff_lb, diff_ub)
        if any(rooms_touch_b9630600(x9, room) for room in x3):
            continue
        x3 = x3 + (x9,)
    if len(x3) != x0:
        return tuple()
    x10 = _normalize_rooms_b9630600(x3)
    if len(x10) == ZERO:
        return tuple()
    x11 = build_candidate_edges_b9630600(x10)
    x12 = kruskal_edges_b9630600(x11, len(x10))
    if len(x12) != len(x10) - ONE:
        return tuple()
    x13 = frozenset(edge[ONE] for edge in x12)
    if len(x13) != TWO:
        return tuple()
    return tuple(sorted(x10))


def generate_b9630600(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _build_rooms_b9630600(diff_lb, diff_ub)
        if len(x0) == ZERO:
            continue
        x1 = render_input_b9630600(x0)
        x2 = render_output_b9630600(x0)
        if x1 == x2:
            continue
        return {"input": x1, "output": x2}
