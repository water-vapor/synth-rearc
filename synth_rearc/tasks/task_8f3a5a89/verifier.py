from synth_rearc.core import *


def verify_8f3a5a89(I: Grid) -> Grid:
    x0 = ofcolor(I, SIX)
    x1 = first(x0)
    x2 = fill(I, EIGHT, x0)
    x3 = objects(x2, T, F, F)
    x4 = extract(x3, lambda x: both(equality(color(x), EIGHT), contained(x1, toindices(x))))
    x5 = objects(I, T, F, F)
    x6 = sfilter(x5, lambda x: both(equality(color(x), ONE), adjacent(x, x4)))
    x7 = mapply(toindices, x6)
    x8 = canvas(ZERO, shape(I))
    x9 = fill(x8, TWO, x4)
    x10 = objects(x9, T, F, F)
    x11 = sfilter(x10, lambda x: both(equality(color(x), ZERO), flip(bordering(x, x9))))
    x12 = mapply(toindices, x11)
    x13 = combine(toindices(x4), x12)
    x14 = sfilter(x13, lambda x: positive(size(difference(neighbors(x), x13))))
    x15 = difference(x14, x0)
    x16 = canvas(EIGHT, shape(I))
    x17 = fill(x16, ONE, x7)
    x18 = fill(x17, SEVEN, x15)
    x19 = fill(x18, SIX, x0)
    return x19
