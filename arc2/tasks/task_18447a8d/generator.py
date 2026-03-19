from arc2.core import *


PANEL_HEIGHT_18447A8D = THREE
LEFT_WIDTH_18447A8D = FIVE
RIGHT_START_18447A8D = SEVEN
RIGHT_WIDTH_18447A8D = FOUR
GRID_WIDTH_18447A8D = 11
PANEL_COLORS_18447A8D = (ONE, TWO, THREE, FOUR, FIVE, SIX, NINE)
PROFILES_18447A8D = tuple(
    (a, b, c)
    for a in range(ONE, FIVE)
    for b in range(ONE, FIVE)
    for c in range(ONE, FIVE)
)


def _complement_profile_18447a8d(profile: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(FIVE - v for v in profile)


def _paint_input_panel_18447a8d(
    grid: Grid,
    top: int,
    left_profile: tuple[int, int, int],
    right_profile: tuple[int, int, int],
    color: int,
) -> Grid:
    x0 = grid
    for x1, x2 in enumerate(left_profile):
        x3 = frozenset((top + x1, j) for j in range(x2))
        x4 = add(RIGHT_START_18447A8D, subtract(RIGHT_WIDTH_18447A8D, right_profile[x1]))
        x5 = frozenset((top + x1, j) for j in range(x4, GRID_WIDTH_18447A8D))
        x0 = fill(x0, EIGHT, x3)
        x0 = fill(x0, color, x5)
    return x0


def _paint_output_panel_18447a8d(
    grid: Grid,
    top: int,
    left_profile: tuple[int, int, int],
    color: int,
) -> Grid:
    x0 = grid
    for x1, x2 in enumerate(left_profile):
        x3 = frozenset((top + x1, j) for j in range(x2))
        x4 = frozenset((top + x1, j) for j in range(x2, LEFT_WIDTH_18447A8D))
        x0 = fill(x0, EIGHT, x3)
        x0 = fill(x0, color, x4)
    return x0


def generate_18447a8d(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (TWO, FOUR))
    x1 = list(sample(PROFILES_18447A8D, x0))
    x2 = sample(PANEL_COLORS_18447A8D, x0)
    x3 = list(range(x0))
    shuffle(x3)
    x4 = {x5: x2[x6] for x6, x5 in enumerate(x3)}
    x5 = add(multiply(increment(PANEL_HEIGHT_18447A8D), x0), ONE)
    x6 = canvas(SEVEN, (x5, GRID_WIDTH_18447A8D))
    x7 = canvas(SEVEN, (x5, GRID_WIDTH_18447A8D))
    for x8, x9 in enumerate(x1):
        x10 = add(ONE, multiply(FOUR, x8))
        x11 = _complement_profile_18447a8d(x1[x3[x8]])
        x12 = x2[x8]
        x13 = x4[x8]
        x6 = _paint_input_panel_18447a8d(x6, x10, x9, x11, x12)
        x7 = _paint_output_panel_18447a8d(x7, x10, x9, x13)
    return {"input": x6, "output": x7}
