from synth_rearc.core import *


def _endpoint_c9680e90(
    I: Grid,
    x0: IntegerTuple,
) -> IntegerTuple:
    x1 = ofcolor(I, SIX)
    x2 = intersection(dneighbors(x0), x1)
    x3 = first(totuple(x2))
    x4 = subtract(x3, x0)
    x5 = x3
    x6 = add(x5, x4)
    while equality(index(I, x6), SIX):
        x5 = x6
        x6 = add(x6, x4)
    return x5


def verify_c9680e90(I: Grid) -> Grid:
    x0 = extract(frontiers(I), matcher(color, NINE))
    x1 = uppermost(x0)
    x2 = ofcolor(I, TWO)
    x3 = canvas(SEVEN, shape(I))
    x4 = fill(x3, NINE, x0)
    for x5 in x2:
        if x5[0] > x1:
            x6 = _endpoint_c9680e90(I, x5)
            x7 = astuple(subtract(double(x1), x6[0]), x6[1])
            x4 = fill(x4, TWO, initset(x6))
            x4 = fill(x4, FIVE, initset(x7))
    return x4
