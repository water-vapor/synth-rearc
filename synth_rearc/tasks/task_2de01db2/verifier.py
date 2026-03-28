from synth_rearc.core import *


FG_COLORS_2DE01DB2 = frozenset((FOUR, SIX, EIGHT))


def _invert_row_2de01db2(
    row: Grid,
) -> Grid:
    x0 = intersection(palette(row), FG_COLORS_2DE01DB2)
    x1 = first(x0)
    x2 = canvas(x1, shape(row))
    x3 = ofcolor(row, x1)
    x4 = fill(x2, ZERO, x3)
    return x4


def verify_2de01db2(I: Grid) -> Grid:
    x0 = height(I)
    x1 = vsplit(I, x0)
    x2 = apply(_invert_row_2de01db2, x1)
    x3 = merge(x2)
    return x3
