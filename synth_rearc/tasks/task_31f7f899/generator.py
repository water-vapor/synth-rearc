from synth_rearc.core import *

from .verifier import verify_31f7f899


GRID_HALF_RANGE_31F7F899 = (THREE, TEN)
OBJECT_COUNT_CHOICES_31F7F899 = (FOUR, FOUR, FOUR, FIVE, FIVE)
BAR_WIDTH_CHOICES_31F7F899 = (ONE, ONE, ONE, THREE)
COLOR_POOL_31F7F899 = (ONE, TWO, THREE, FOUR, FIVE, SEVEN, NINE)


def _bar_patch_31f7f899(
    axis: Integer,
    height_value: Integer,
    left: Integer,
    width_value: Integer,
) -> Indices:
    x0 = subtract(axis, divide(height_value, TWO))
    return frozenset((x1, x2) for x1 in range(x0, add(x0, height_value)) for x2 in range(left, add(left, width_value)))


def _render_31f7f899(
    side: Integer,
    axis: Integer,
    specs: tuple[tuple[Integer, Integer, Integer, Integer], ...],
) -> Grid:
    x0 = canvas(EIGHT, astuple(side, side))
    x1 = connect(astuple(axis, ZERO), astuple(axis, decrement(side)))
    x2 = fill(x0, SIX, x1)
    for x3, x4, x5, x6 in specs:
        x7 = _bar_patch_31f7f899(axis, x6, x4, x5)
        x8 = recolor(x3, x7)
        x2 = paint(x2, x8)
    return x2


def _pack_columns_31f7f899(
    side: Integer,
    widths: tuple[Integer, ...],
) -> tuple[Integer, ...] | None:
    x0 = sum(widths)
    x1 = add(x0, subtract(len(widths), ONE))
    if x1 > side:
        return None
    x2 = [ZERO] * increment(len(widths))
    for _ in range(subtract(side, x1)):
        x3 = randint(ZERO, len(widths))
        x2[x3] += ONE
    x4 = x2[ZERO]
    x5 = []
    x6 = []
    for x7, x8 in enumerate(widths):
        x5.append(x4)
        x4 = add(x4, x8)
        if x7 != subtract(len(widths), ONE):
            x4 = add(x4, increment(x2[increment(x7)]))
    return tuple(x5)


def _pick_input_heights_31f7f899(
    output_heights: tuple[Integer, ...],
    widths: tuple[Integer, ...],
) -> tuple[Integer, ...] | None:
    x0 = tuple(reversed(output_heights))
    if both(x0 != output_heights, all(x1 >= x2 for x1, x2 in zip(x0, widths))):
        return x0
    for _ in range(40):
        x1 = tuple(sample(output_heights, len(output_heights)))
        if both(x1 != output_heights, all(x2 >= x3 for x2, x3 in zip(x1, widths))):
            return x1
    return None


def generate_31f7f899(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, GRID_HALF_RANGE_31F7F899)
        x1 = increment(double(x0))
        x2 = x0
        x3 = choice(OBJECT_COUNT_CHOICES_31F7F899)
        x4 = tuple(choice(BAR_WIDTH_CHOICES_31F7F899) for _ in range(x3))
        x5 = _pack_columns_31f7f899(x1, x4)
        if x5 is None:
            continue
        x6 = randint(ONE, max(ONE, subtract(x0, ONE)))
        x7 = subtract(x1, double(x6))
        x8 = tuple(sorted(randint(ONE, x7) for _ in range(x3)))
        if len(set(x8)) == ONE:
            continue
        if any(x9 < x10 for x9, x10 in zip(x8, x4)):
            continue
        x9 = _pick_input_heights_31f7f899(x8, x4)
        if x9 is None:
            continue
        x10 = tuple(choice(COLOR_POOL_31F7F899) for _ in range(x3))
        if len(set(x10)) == ONE:
            continue
        x11 = tuple((x12, x13, x14, x15) for x12, x13, x14, x15 in zip(x10, x5, x4, x9))
        x12 = tuple((x13, x14, x15, x16) for x13, x14, x15, x16 in zip(x10, x5, x4, x8))
        x13 = _render_31f7f899(x1, x2, x11)
        x14 = _render_31f7f899(x1, x2, x12)
        if verify_31f7f899(x13) != x14:
            continue
        return {"input": x13, "output": x14}
