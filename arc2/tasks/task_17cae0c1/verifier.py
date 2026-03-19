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

TOP_BAR_CELLS_17CAE0C1 = ofcolor(TOP_BAR_17CAE0C1, FIVE)
BOTTOM_BAR_CELLS_17CAE0C1 = ofcolor(BOTTOM_BAR_17CAE0C1, FIVE)
CENTER_DOT_CELLS_17CAE0C1 = ofcolor(CENTER_DOT_17CAE0C1, FIVE)
RING_CELLS_17CAE0C1 = ofcolor(RING_17CAE0C1, FIVE)
ANTI_DIAGONAL_CELLS_17CAE0C1 = ofcolor(ANTI_DIAGONAL_17CAE0C1, FIVE)


def verify_17cae0c1(I: Grid) -> Grid:
    x0 = width(I)
    x1 = divide(x0, THREE)
    x2 = hsplit(I, x1)
    x3 = []
    for x4 in x2:
        x5 = ofcolor(x4, FIVE)
        x6 = equality(x5, TOP_BAR_CELLS_17CAE0C1)
        x7 = branch(x6, SIX, ZERO)
        x8 = equality(x5, BOTTOM_BAR_CELLS_17CAE0C1)
        x9 = branch(x8, ONE, x7)
        x10 = equality(x5, ANTI_DIAGONAL_CELLS_17CAE0C1)
        x11 = branch(x10, NINE, x9)
        x12 = equality(x5, CENTER_DOT_CELLS_17CAE0C1)
        x13 = branch(x12, FOUR, x11)
        x14 = equality(x5, RING_CELLS_17CAE0C1)
        x15 = branch(x14, THREE, x13)
        x16 = canvas(x15, (THREE, THREE))
        x3.append(x16)
    x17 = x3[ZERO]
    for x18 in x3[ONE:]:
        x17 = hconcat(x17, x18)
    return x17
