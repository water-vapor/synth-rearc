from synth_rearc.core import *

from .helpers import resize_object_465b7d93


GRID_SHAPE_465B7D93 = (TEN, TEN)
SEED_COLORS_465B7D93 = (ONE, TWO, THREE, FOUR, FIVE, EIGHT, NINE)
SEED_SHAPES_465B7D93 = (
    frozenset({(ZERO, ZERO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ONE)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE)}),
)


def _frame_patch_465b7d93(
    top: int,
    left: int,
    side: int,
) -> frozenset[tuple[int, int]]:
    x0 = top + side - ONE
    x1 = left + side - ONE
    x2 = frozenset({(top, left), (x0, x1)})
    return box(x2)


def _seed_positions_465b7d93(
    frame: Patch,
    shape: Patch,
) -> tuple[tuple[int, int], ...]:
    x0 = height(shape)
    x1 = width(shape)
    x2 = backdrop(frame)
    x3 = []
    for x4 in range(TEN - x0 + ONE):
        for x5 in range(TEN - x1 + ONE):
            x6 = shift(backdrop(shape), (x4, x5))
            if len(intersection(x6, x2)) == ZERO:
                x3.append((x4, x5))
    return tuple(x3)


def generate_465b7d93(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (THREE, EIGHT))
        x1 = randint(ZERO, TEN - x0)
        x2 = randint(ZERO, TEN - x0)
        x3 = _frame_patch_465b7d93(x1, x2, x0)
        x4 = x0 - TWO
        if x4 == ONE:
            x5 = SEED_SHAPES_465B7D93[ZERO]
        else:
            x5 = choice(SEED_SHAPES_465B7D93)
        x6 = _seed_positions_465b7d93(x3, x5)
        if len(x6) == ZERO:
            continue
        x7 = choice(SEED_COLORS_465B7D93)
        x8 = choice(x6)
        x9 = recolor(x7, shift(x5, x8))
        x10 = canvas(SEVEN, GRID_SHAPE_465B7D93)
        x11 = fill(x10, SIX, x3)
        x12 = paint(x11, x9)
        x13 = astuple(x4, x4)
        x14 = resize_object_465b7d93(x9, x13)
        x15 = astuple(x1 + ONE, x2 + ONE)
        x16 = shift(x14, x15)
        x17 = cover(x12, x9)
        x18 = paint(x17, x16)
        return {"input": x12, "output": x18}
