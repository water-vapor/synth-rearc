from arc2.core import *

from .verifier import verify_7c9b52a0


GRID_SHAPE_7C9B52A0 = (16, 16)
WINDOW_HEIGHT_BOUNDS_7C9B52A0 = (3, 5)
WINDOW_WIDTH_BOUNDS_7C9B52A0 = (3, 5)
WINDOW_COUNT_BOUNDS_7C9B52A0 = (2, 4)
BACKGROUND_COLORS_7C9B52A0 = (ONE, EIGHT, NINE)
ACTIVE_COLORS_7C9B52A0 = (ONE, TWO, THREE, FOUR, SIX)


def _rect_patch_7c9b52a0(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    x0 = interval(top, add(top, height_value), ONE)
    x1 = interval(left, add(left, width_value), ONE)
    return product(x0, x1)


def _grow_patch_7c9b52a0(
    shape_value: IntegerTuple,
    occupied: Indices,
    target_size: Integer,
) -> Indices:
    x0, x1 = shape_value
    x2 = tuple(product(interval(ZERO, x0, ONE), interval(ZERO, x1, ONE)))
    x3 = tuple(loc for loc in x2 if loc not in occupied)
    if len(x3) < target_size:
        return frozenset()
    x4 = {choice(x3)}
    while len(x4) < target_size:
        x5 = set()
        for x6 in x4:
            for x7 in dneighbors(x6):
                if ZERO <= x7[0] < x0 and ZERO <= x7[1] < x1 and x7 not in occupied and x7 not in x4:
                    x5.add(x7)
        if len(x5) == ZERO:
            return frozenset()
        x4.add(choice(tuple(x5)))
    return frozenset(x4)


def _sample_layers_7c9b52a0(
    diff_lb: float,
    diff_ub: float,
    shape_value: IntegerTuple,
    colors: tuple[Integer, ...],
) -> tuple[tuple[Integer, Indices], ...] | None:
    x0 = shape_value[0] * shape_value[1]
    x1 = frozenset()
    x2 = tuple()
    for x3, x4 in enumerate(colors):
        x5 = len(colors) - x3 - ONE
        x6 = min(FIVE, x0 - len(x1) - TWO * x5 - ONE)
        if x6 < TWO:
            return None
        x7 = unifint(diff_lb, diff_ub, (TWO, x6))
        x8 = frozenset()
        for _ in range(40):
            x8 = _grow_patch_7c9b52a0(shape_value, x1, x7)
            if len(x8) == x7:
                break
        if len(x8) != x7:
            return None
        x1 = combine(x1, x8)
        x2 = x2 + ((x4, x8),)
    return x2


def _sample_positions_7c9b52a0(
    window_shape: IntegerTuple,
    total: Integer,
) -> tuple[IntegerTuple, ...] | None:
    x0, x1 = GRID_SHAPE_7C9B52A0
    x2, x3 = window_shape
    x4 = tuple()
    x5 = frozenset()
    for _ in range(total):
        x6 = None
        for _ in range(200):
            x7 = randint(ONE, x0 - x2 - ONE)
            x8 = randint(ONE, x1 - x3 - ONE)
            x9 = _rect_patch_7c9b52a0(x7 - ONE, x8 - ONE, x2 + TWO, x3 + TWO)
            if len(intersection(x5, x9)) > ZERO:
                continue
            x6 = astuple(x7, x8)
            x4 = x4 + (x6,)
            x5 = combine(x5, x9)
            break
        if x6 is None:
            return None
    return x4


def _build_input_7c9b52a0(
    background: Integer,
    window_shape: IntegerTuple,
    layers: tuple[tuple[Integer, Indices], ...],
    positions: tuple[IntegerTuple, ...],
) -> Grid:
    x0 = canvas(background, GRID_SHAPE_7C9B52A0)
    x1, x2 = window_shape
    for (x3, x4), (x5, x6) in zip(layers, positions):
        x7 = _rect_patch_7c9b52a0(x5, x6, x1, x2)
        x8 = shift(x4, astuple(x5, x6))
        x0 = fill(x0, ZERO, x7)
        x0 = fill(x0, x3, x8)
    return x0


def _build_output_7c9b52a0(
    window_shape: IntegerTuple,
    layers: tuple[tuple[Integer, Indices], ...],
) -> Grid:
    x0 = canvas(ZERO, window_shape)
    for x1, x2 in layers:
        x0 = fill(x0, x1, x2)
    return x0


def generate_7c9b52a0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, WINDOW_HEIGHT_BOUNDS_7C9B52A0)
        x1 = unifint(diff_lb, diff_ub, WINDOW_WIDTH_BOUNDS_7C9B52A0)
        if x0 * x1 < 12 or x0 * x1 > 20:
            continue
        x2 = astuple(x0, x1)
        x3 = unifint(diff_lb, diff_ub, WINDOW_COUNT_BOUNDS_7C9B52A0)
        x4 = choice(BACKGROUND_COLORS_7C9B52A0)
        x5 = tuple(color for color in ACTIVE_COLORS_7C9B52A0 if color != x4)
        x6 = tuple(sample(x5, x3))
        x7 = _sample_layers_7c9b52a0(diff_lb, diff_ub, x2, x6)
        if x7 is None:
            continue
        x8 = _sample_positions_7c9b52a0(x2, x3)
        if x8 is None:
            continue
        x9 = _build_input_7c9b52a0(x4, x2, x7, x8)
        x10 = _build_output_7c9b52a0(x2, x7)
        if verify_7c9b52a0(x9) != x10:
            continue
        return {"input": x9, "output": x10}
