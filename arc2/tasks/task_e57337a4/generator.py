from arc2.core import *


BACKGROUND_COLORS_E57337A4 = (SIX, SEVEN, EIGHT, NINE)
INPUT_SHAPE_E57337A4 = (15, 15)
OUTPUT_CELLS_E57337A4 = tuple(asindices(canvas(ZERO, THREE_BY_THREE)))
LOCAL_CELLS_E57337A4 = tuple(asindices(canvas(ZERO, (FIVE, FIVE))))


def generate_e57337a4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = choice(BACKGROUND_COLORS_E57337A4)
    x1 = unifint(diff_lb, diff_ub, (ONE, THREE))
    x2 = frozenset(sample(OUTPUT_CELLS_E57337A4, x1))
    x3 = fill(canvas(x0, THREE_BY_THREE), ZERO, x2)
    x4 = canvas(x0, INPUT_SHAPE_E57337A4)
    for x5 in x2:
        x6 = choice(LOCAL_CELLS_E57337A4)
        x7 = shift(initset(x6), multiply(x5, FIVE))
        x4 = fill(x4, ZERO, x7)
    return {"input": x4, "output": x3}
