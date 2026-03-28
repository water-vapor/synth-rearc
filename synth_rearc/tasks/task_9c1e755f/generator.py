from synth_rearc.core import *

from .verifier import verify_9c1e755f


GRID_SHAPE_9C1E755F = (TEN, TEN)
NONFIVE_COLORS_9C1E755F = (ONE, TWO, THREE, FOUR, SIX, SEVEN, EIGHT, NINE)


def _paint_row_segment_9c1e755f(
    grid: Grid,
    row: int,
    start: int,
    values: tuple[int, ...],
) -> Grid:
    x0 = grid
    for x1, x2 in enumerate(values):
        x3 = initset((row, start + x1))
        x0 = fill(x0, x2, x3)
    return x0


def _mirror_pair_9c1e755f(
    gi: Grid,
    go: Grid,
) -> tuple[Grid, Grid]:
    x0, x1 = gi, go
    if choice((T, F)):
        x0 = vmirror(x0)
        x1 = vmirror(x1)
    if choice((T, F)):
        x0 = hmirror(x0)
        x1 = hmirror(x1)
    return x0, x1


def _sample_pattern_9c1e755f(
    width: int,
    seen: tuple[tuple[int, ...], ...],
) -> tuple[int, ...]:
    while True:
        x0 = randint(ONE, min(FOUR, len(NONFIVE_COLORS_9C1E755F)))
        x1 = sample(NONFIVE_COLORS_9C1E755F, x0)
        x2 = (FIVE,) + tuple(choice(x1) for _ in range(width - ONE))
        if x2 not in seen:
            return x2


def _generate_horizontal_case_9c1e755f(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Grid, Grid]:
    x0, x1 = GRID_SHAPE_9C1E755F
    x2 = unifint(diff_lb, diff_ub, (FOUR, SEVEN))
    x3 = unifint(diff_lb, diff_ub, (ONE, FIVE))
    x4 = randint(ZERO, x1 - x2)
    x5 = min(x0 - x3 - ONE, unifint(diff_lb, diff_ub, (TWO, SIX)))
    x6 = canvas(ZERO, GRID_SHAPE_9C1E755F)
    x7 = connect((x3, x4), (x3, x4 + x2 - ONE))
    x8 = fill(x6, FIVE, x7)
    x9 = x8
    x10 = randint(ONE, FOUR)
    x11 = sample(NONFIVE_COLORS_9C1E755F, x10)
    for x12 in range(x5):
        x13 = x3 + x12 + ONE
        x14 = choice(x11)
        x15 = initset((x13, x4))
        x16 = connect((x13, x4), (x13, x4 + x2 - ONE))
        x8 = fill(x8, x14, x15)
        x9 = fill(x9, x14, x16)
    return _mirror_pair_9c1e755f(x8, x9)


def _sample_template_count_9c1e755f() -> int:
    return choice((ONE, ONE, TWO))


def _sample_span_length_9c1e755f(
    template_count: int,
    mixed: bool,
) -> int:
    if template_count == TWO:
        return choice((SIX, EIGHT) if mixed else (FOUR, SIX, EIGHT))
    return choice((SIX, SEVEN, EIGHT) if mixed else (FOUR, FIVE, SIX, SEVEN, EIGHT))


def _generate_vertical_template_case_9c1e755f(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Grid, Grid]:
    x0, x1 = GRID_SHAPE_9C1E755F
    x2 = _sample_template_count_9c1e755f()
    x3 = _sample_span_length_9c1e755f(x2, F)
    x4 = randint(ONE, x0 - x3 - ONE)
    x5 = randint(ZERO, SIX)
    x6 = randint(FOUR, x1 - x5)
    x7 = x4 + x3 - ONE
    x8 = tuple(range(x7 - x2 + ONE, x7 + ONE))
    x9 = canvas(ZERO, GRID_SHAPE_9C1E755F)
    x10 = connect((x4, x5), (x7, x5))
    x11 = fill(x9, FIVE, x10)
    x12 = tuple()
    for x13 in range(x2):
        x14 = _sample_pattern_9c1e755f(x6, x12)
        x12 = x12 + (x14,)
        x11 = _paint_row_segment_9c1e755f(x11, x8[x13], x5, x14)
    x15 = x11
    for x16, x17 in enumerate(range(x4, x7 + ONE)):
        x18 = x12[x16 % x2]
        x15 = _paint_row_segment_9c1e755f(x15, x17, x5, x18)
    return _mirror_pair_9c1e755f(x11, x15)


def _generate_vertical_mixed_case_9c1e755f(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Grid, Grid]:
    x0, x1 = GRID_SHAPE_9C1E755F
    x2 = _sample_template_count_9c1e755f()
    x3 = _sample_span_length_9c1e755f(x2, T)
    x4 = randint(ONE, x0 - x3 - ONE)
    x5 = x4 + x3 - ONE
    x6 = randint(THREE, SIX)
    x7 = x6 - ONE
    x8 = x1 - x6
    x9 = tuple(range(x5 - x2 + ONE, x5 + ONE))
    x10 = choice(("inside", "outside"))
    x11 = canvas(ZERO, GRID_SHAPE_9C1E755F)
    x12 = connect((x4, x6), (x5, x6))
    x13 = fill(x11, FIVE, x12)
    x14 = tuple()
    for x15 in range(x2):
        x16 = _sample_pattern_9c1e755f(x8, x14)
        x14 = x14 + (x16,)
        x13 = _paint_row_segment_9c1e755f(x13, x9[x15], x6, x16)
    x17 = connect((x4, ZERO), (x4, x7 - ONE))
    x18 = connect((x4 - ONE, ZERO), (x4 - ONE, x7 - ONE))
    x19 = tuple(range(x4 + ONE, x5 - x2 + ONE)) if x10 == "inside" else tuple(range(x4, x5 - x2 + ONE))
    x20 = x17 if x10 == "inside" else x18
    x13 = fill(x13, FIVE, x20)
    x21 = randint(ONE, FOUR)
    x22 = sample(NONFIVE_COLORS_9C1E755F, x21)
    x23 = x13
    for x24 in x19:
        x25 = choice(x22)
        x26 = initset((x24, ZERO))
        x13 = fill(x13, x25, x26)
        x27 = connect((x24, ZERO), (x24, x7 - ONE))
        x23 = fill(x23, x25, x27)
    for x28, x29 in enumerate(range(x4, x5 + ONE)):
        x30 = x14[x28 % x2]
        x23 = _paint_row_segment_9c1e755f(x23, x29, x6, x30)
    return _mirror_pair_9c1e755f(x13, x23)


def generate_9c1e755f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(("horizontal", "template", "template", "mixed", "mixed"))
        if x0 == "horizontal":
            x1, x2 = _generate_horizontal_case_9c1e755f(diff_lb, diff_ub)
        elif x0 == "template":
            x1, x2 = _generate_vertical_template_case_9c1e755f(diff_lb, diff_ub)
        else:
            x1, x2 = _generate_vertical_mixed_case_9c1e755f(diff_lb, diff_ub)
        if x1 == x2:
            continue
        if verify_9c1e755f(x1) != x2:
            continue
        return {"input": x1, "output": x2}
