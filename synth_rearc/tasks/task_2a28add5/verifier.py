from synth_rearc.core import *


def verify_2a28add5(I: Grid) -> Grid:
    x0 = ofcolor(I, SIX)
    x1 = canvas(SEVEN, shape(I))
    x2 = matcher(identity, SEVEN)
    x3 = compose(flip, x2)

    def x4(x5: IntegerTuple) -> Indices:
        x6 = first(x5)
        x7 = last(x5)
        x8 = I[x6]
        x9 = x8[:x7]
        x10 = x8[add(x7, ONE):]
        x11 = sfilter(x9, x3)
        x12 = sfilter(x10, x3)
        x13 = size(x11)
        x14 = size(x12)
        x15 = subtract(x7, x13)
        x16 = add(x7, x14)
        x17 = astuple(x6, x15)
        x18 = astuple(x6, x16)
        x19 = connect(x17, x18)
        return x19

    x20 = mapply(x4, x0)
    x21 = fill(x1, EIGHT, x20)
    return x21
