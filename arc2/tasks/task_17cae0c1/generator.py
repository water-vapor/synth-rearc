from arc2.core import *


TOP_BAR_17CAE0C1 = (
    (FIVE, FIVE, FIVE),
    (ZERO, ZERO, ZERO),
    (ZERO, ZERO, ZERO),
)

BOTTOM_BAR_17CAE0C1 = (
    (ZERO, ZERO, ZERO),
    (ZERO, ZERO, ZERO),
    (FIVE, FIVE, FIVE),
)

CENTER_DOT_17CAE0C1 = (
    (ZERO, ZERO, ZERO),
    (ZERO, FIVE, ZERO),
    (ZERO, ZERO, ZERO),
)

RING_17CAE0C1 = (
    (FIVE, FIVE, FIVE),
    (FIVE, ZERO, FIVE),
    (FIVE, FIVE, FIVE),
)

ANTI_DIAGONAL_17CAE0C1 = (
    (ZERO, ZERO, FIVE),
    (ZERO, FIVE, ZERO),
    (FIVE, ZERO, ZERO),
)

GLYPHS_17CAE0C1 = (
    (TOP_BAR_17CAE0C1, SIX),
    (BOTTOM_BAR_17CAE0C1, ONE),
    (ANTI_DIAGONAL_17CAE0C1, NINE),
    (CENTER_DOT_17CAE0C1, FOUR),
    (RING_17CAE0C1, THREE),
)


def generate_17cae0c1(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = choice((THREE, THREE, FOUR, FOUR, FIVE))
    x1 = tuple(choice(GLYPHS_17CAE0C1) for _ in range(x0))
    x2, x3 = x1[ZERO]
    x4 = x2
    x5 = canvas(x3, (THREE, THREE))
    for x6, x7 in x1[ONE:]:
        x4 = hconcat(x4, x6)
        x8 = canvas(x7, (THREE, THREE))
        x5 = hconcat(x5, x8)
    return {"input": x4, "output": x5}
