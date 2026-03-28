from synth_rearc.core import *


GRID_SHAPE_D304284E = (23, 28)
LEFT_RANGE_D304284E = (0, 6)
TOP_RANGE_D304284E = (0, 8)
HEIGHTS_D304284E = (THREE, FIVE, SEVEN)
FULL_ROW_D304284E = frozenset({ZERO, ONE, TWO})
SIDE_ROW_D304284E = frozenset({ZERO, TWO})
CENTER_ROW_D304284E = frozenset({ONE})
ROW_PROFILES_D304284E = (
    (FULL_ROW_D304284E, SIDE_ROW_D304284E),
    (SIDE_ROW_D304284E, FULL_ROW_D304284E),
    (CENTER_ROW_D304284E, SIDE_ROW_D304284E),
    (CENTER_ROW_D304284E, FULL_ROW_D304284E),
    (SIDE_ROW_D304284E, CENTER_ROW_D304284E),
    (FULL_ROW_D304284E, CENTER_ROW_D304284E),
)


def _make_motif_d304284e(
    outer_profile,
    middle_profile,
    motif_h: Integer,
) -> Indices:
    x0 = divide(motif_h, TWO)
    x1 = set()
    for x2 in interval(ZERO, motif_h, ONE):
        x3 = middle_profile if x2 == x0 else outer_profile
        for x4 in x3:
            x1.add((x2, x4))
    return frozenset(x1)


def _paint_output_d304284e(
    patch: Patch,
) -> Grid:
    x0 = canvas(ZERO, GRID_SHAPE_D304284E)
    x1 = increment(width(patch))
    x2 = increment(height(patch))
    x3 = interval(ZERO, increment(width(x0)), ONE)
    x4 = interval(ONE, increment(height(x0)), ONE)
    x5 = x0
    for x6 in x3:
        x7 = multiply(tojvec(x1), x6)
        x8 = branch(equality(x6 % THREE, TWO), SIX, SEVEN)
        x9 = shift(recolor(x8, patch), x7)
        x5 = paint(x5, x9)
        if x8 == SIX:
            for x10 in x4:
                x11 = multiply(toivec(x2), x10)
                x12 = shift(x9, x11)
                x5 = paint(x5, x12)
    return x5


def generate_d304284e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = choice(ROW_PROFILES_D304284E)
    x1 = choice(HEIGHTS_D304284E)
    x2 = _make_motif_d304284e(x0[ZERO], x0[ONE], x1)
    x3 = randint(TOP_RANGE_D304284E[0], TOP_RANGE_D304284E[1])
    x4 = randint(LEFT_RANGE_D304284E[0], LEFT_RANGE_D304284E[1])
    x5 = shift(x2, (x3, x4))
    x6 = fill(canvas(ZERO, GRID_SHAPE_D304284E), SEVEN, x5)
    x7 = _paint_output_d304284e(x5)
    return {"input": x6, "output": x7}
