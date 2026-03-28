from synth_rearc.core import *


TURN_RIGHT_PATCH_E6DE6E8F = frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE)})
TURN_LEFT_PATCH_E6DE6E8F = frozenset({(ZERO, ZERO), (ONE, ZERO), (ONE, ONE)})
STRAIGHT_PATCH_E6DE6E8F = frozenset({(ZERO, ZERO), (ONE, ZERO)})

STEP_TO_PATCH_E6DE6E8F = {
    NEG_ONE: TURN_RIGHT_PATCH_E6DE6E8F,
    ZERO: STRAIGHT_PATCH_E6DE6E8F,
    ONE: TURN_LEFT_PATCH_E6DE6E8F,
}

PATCH_TO_STEP_E6DE6E8F = {
    TURN_RIGHT_PATCH_E6DE6E8F: NEG_ONE,
    STRAIGHT_PATCH_E6DE6E8F: ZERO,
    TURN_LEFT_PATCH_E6DE6E8F: ONE,
}


def step_from_symbol_e6de6e8f(obj: Object) -> Integer:
    x0 = normalize(toindices(obj))
    if x0 not in PATCH_TO_STEP_E6DE6E8F:
        raise ValueError(f"unknown e6de6e8f symbol: {x0}")
    x1 = PATCH_TO_STEP_E6DE6E8F[x0]
    return x1


def ordered_symbols_e6de6e8f(I: Grid) -> Tuple:
    x0 = objects(I, T, F, F)
    x1 = colorfilter(x0, TWO)
    x2 = order(x1, leftmost)
    return x2


def walk_columns_e6de6e8f(I: Grid) -> Tuple:
    x0 = ordered_symbols_e6de6e8f(I)
    x1 = tuple(step_from_symbol_e6de6e8f(obj) for obj in x0)
    x2 = [THREE]
    for step in x1:
        x2.append(x2[-ONE] + step)
        if step == ZERO:
            x2.append(x2[-ONE])
    x3 = tuple(x2[:EIGHT])
    return x3


def render_output_e6de6e8f(
    walk: Tuple,
    bg_color: Integer,
    path_color: Integer,
    marker_color: Integer,
) -> Grid:
    x0 = canvas(bg_color, (EIGHT, SEVEN))
    x1 = fill(x0, marker_color, initset((ZERO, THREE)))
    x2 = x1
    for row_index, (start, stop) in enumerate(zip(walk, walk[ONE:]), start=ONE):
        x3 = connect((row_index, start), (row_index, stop))
        x2 = fill(x2, path_color, x3)
    return x2


def solve_e6de6e8f(I: Grid) -> Grid:
    x0 = walk_columns_e6de6e8f(I)
    x1 = render_output_e6de6e8f(x0, ZERO, TWO, THREE)
    return x1


def render_input_e6de6e8f(
    steps: Tuple,
    bg_color: Integer,
    path_color: Integer,
    gaps: Tuple = (ZERO, ONE, ONE, ONE, ONE, ZERO),
) -> Grid:
    x0 = sum(gaps)
    for step in steps:
        x0 = x0 + width(STEP_TO_PATCH_E6DE6E8F[step])
    x1 = canvas(bg_color, (TWO, x0))
    x2 = gaps[ZERO]
    x3 = x1
    for index, step in enumerate(steps):
        x4 = STEP_TO_PATCH_E6DE6E8F[step]
        x5 = shift(x4, (ZERO, x2))
        x6 = recolor(path_color, x5)
        x3 = paint(x3, x6)
        x2 = x2 + width(x4) + gaps[index + ONE]
    return x3
