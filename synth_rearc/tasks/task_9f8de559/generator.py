from synth_rearc.core import *


GRID_SIZE_9F8DE559 = 14
ARROW_LENGTH_9F8DE559 = FOUR
FRAME_COLORS_9F8DE559 = (FIVE, EIGHT, NINE)
DIRECTIONS_9F8DE559 = (UP, DOWN, LEFT, RIGHT, NEG_UNITY, UP_RIGHT, DOWN_LEFT, UNITY)
VERTICAL_MARGINS_9F8DE559 = ((ONE, ONE), (ONE, TWO), (TWO, ONE), (TWO, TWO))
HORIZONTAL_MARGINS_9F8DE559 = ((ONE, THREE), (TWO, TWO), (TWO, THREE), (THREE, TWO))


def _rect_patch_9f8de559(top: int, left: int, height: int, width: int) -> Indices:
    return frozenset((i, j) for i in range(top, top + height) for j in range(left, left + width))


def _in_rect_9f8de559(loc: tuple[int, int], top: int, left: int, bottom: int, right: int) -> bool:
    return top <= loc[0] < bottom and left <= loc[1] < right


def _candidate_tips_9f8de559(
    top: int,
    left: int,
    bottom: int,
    right: int,
    direction: tuple[int, int],
) -> tuple[tuple[int, int], ...]:
    di, dj = direction
    x0 = []
    for x1 in range(top, bottom):
        for x2 in range(left, right):
            x3 = all(
                _in_rect_9f8de559((x1 + k * di, x2 + k * dj), top, left, bottom, right)
                for k in range(-ARROW_LENGTH_9F8DE559, TWO)
            )
            if x3:
                x0.append((x1, x2))
    return tuple(x0)


def _target_loc_9f8de559(
    tip: tuple[int, int],
    direction: tuple[int, int],
    top: int,
    left: int,
    bottom: int,
    right: int,
) -> tuple[int, int]:
    di, dj = direction
    x0 = ONE
    x1 = (tip[0] + di, tip[1] + dj)
    while _in_rect_9f8de559(x1, top, left, bottom, right):
        x0 += ONE
        x1 = (tip[0] + x0 * di, tip[1] + x0 * dj)
    return x1


def _paint_frame_9f8de559(
    diff_lb: float,
    diff_ub: float,
    top: int,
    left: int,
    bottom: int,
    right: int,
) -> Grid:
    x0 = [choice(FRAME_COLORS_9F8DE559) for _ in range(FOUR)]
    if len(set(x0)) == ONE:
        x0[ONE] = choice(remove(x0[0], FRAME_COLORS_9F8DE559))
    x1 = canvas(x0[0], (GRID_SIZE_9F8DE559, GRID_SIZE_9F8DE559))
    x1 = fill(x1, x0[0], _rect_patch_9f8de559(ZERO, ZERO, top, GRID_SIZE_9F8DE559))
    x1 = fill(
        x1,
        x0[1],
        _rect_patch_9f8de559(bottom, ZERO, GRID_SIZE_9F8DE559 - bottom, GRID_SIZE_9F8DE559),
    )
    x1 = fill(x1, x0[2], _rect_patch_9f8de559(top, ZERO, bottom - top, left))
    x1 = fill(
        x1,
        x0[3],
        _rect_patch_9f8de559(top, right, bottom - top, GRID_SIZE_9F8DE559 - right),
    )
    x2 = (
        ("top", top, GRID_SIZE_9F8DE559),
        ("bottom", GRID_SIZE_9F8DE559 - bottom, GRID_SIZE_9F8DE559),
        ("left", bottom - top, left),
        ("right", bottom - top, GRID_SIZE_9F8DE559 - right),
    )
    x3 = tuple(x4 for x4 in x2 if x4[1] > ZERO and x4[2] > ZERO)
    x4 = unifint(diff_lb, diff_ub, (ONE, THREE))
    for _ in range(x4):
        x5, x6, x7 = choice(x3)
        x8 = unifint(diff_lb, diff_ub, (ONE, x6))
        x9 = unifint(diff_lb, diff_ub, (ONE, x7))
        if x5 == "top":
            x10 = ZERO
            x11 = unifint(diff_lb, diff_ub, (ZERO, GRID_SIZE_9F8DE559 - x9))
        elif x5 == "bottom":
            x10 = GRID_SIZE_9F8DE559 - x8
            x11 = unifint(diff_lb, diff_ub, (ZERO, GRID_SIZE_9F8DE559 - x9))
        elif x5 == "left":
            x10 = unifint(diff_lb, diff_ub, (top, bottom - x8))
            x11 = ZERO
        else:
            x10 = unifint(diff_lb, diff_ub, (top, bottom - x8))
            x11 = GRID_SIZE_9F8DE559 - x9
        x12 = choice(remove(x1[x10][x11], FRAME_COLORS_9F8DE559))
        x13 = _rect_patch_9f8de559(x10, x11, x8, x9)
        x1 = fill(x1, x12, x13)
    return x1


def generate_9f8de559(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0, x1 = choice(VERTICAL_MARGINS_9F8DE559)
    x2, x3 = choice(HORIZONTAL_MARGINS_9F8DE559)
    x4 = x0
    x5 = x2
    x6 = GRID_SIZE_9F8DE559 - x1
    x7 = GRID_SIZE_9F8DE559 - x3
    x8 = _paint_frame_9f8de559(diff_lb, diff_ub, x4, x5, x6, x7)
    x9 = _rect_patch_9f8de559(x4, x5, x6 - x4, x7 - x5)
    x10 = fill(x8, SEVEN, x9)
    x11 = {x12: _candidate_tips_9f8de559(x4, x5, x6, x7, x12) for x12 in DIRECTIONS_9F8DE559}
    x12 = tuple(x13 for x13, x14 in x11.items() if len(x14) > ZERO)
    x13 = choice(x12)
    x14 = choice(x11[x13])
    x15 = frozenset(
        (x14[0] - k * x13[0], x14[1] - k * x13[1]) for k in range(ONE, ARROW_LENGTH_9F8DE559 + ONE)
    )
    x16 = _target_loc_9f8de559(x14, x13, x4, x5, x6, x7)
    x17 = fill(x10, SIX, x15)
    x18 = fill(x17, TWO, initset(x14))
    x19 = fill(x18, SEVEN, initset(x16))
    return {"input": x18, "output": x19}
