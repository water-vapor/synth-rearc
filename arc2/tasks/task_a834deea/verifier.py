from arc2.core import *


STENCIL_CELLS_A834DEEA = (
    (ONE, UNITY),
    (SEVEN, (ONE, TWO)),
    (SIX, (ONE, THREE)),
    (FOUR, (TWO, ONE)),
    (FIVE, (TWO, THREE)),
    (TWO, (THREE, ONE)),
    (NINE, (THREE, TWO)),
    (THREE, (THREE, THREE)),
)


def verify_a834deea(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = ofcolor(I, ZERO)
    x3 = frozenset()
    x4 = subtract(x0, FOUR)
    x5 = subtract(x1, FOUR)
    for x6 in range(x4):
        for x7 in range(x5):
            x8 = frozenset({(x6, x7), (add(x6, FOUR), add(x7, FOUR))})
            x9 = box(x8)
            x10 = difference(x9, x2)
            if size(x10) == ZERO:
                x3 = insert((x6, x7), x3)
    x11 = frozenset()
    for x12 in x3:
        for x13, x14 in STENCIL_CELLS_A834DEEA:
            x15 = add(x12, x14)
            if contained(x15, x2):
                x11 = insert((x13, x15), x11)
    x16 = paint(I, x11)
    return x16
