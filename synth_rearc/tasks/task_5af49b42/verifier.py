from synth_rearc.core import *


def verify_5af49b42(I: Grid) -> Grid:
    x0 = decrement(height(I))
    x1 = objects(I, F, F, T)
    x2 = lambda x: both(
        greater(size(x), ONE),
        both(hline(x), either(equality(uppermost(x), ZERO), equality(lowermost(x), x0))),
    )
    x3 = sfilter(x1, x2)
    x4 = difference(x1, x3)
    x5 = I
    for x6 in x4:
        x7 = color(x6)
        x8 = extract(x3, compose(lbind(contained, x7), palette))
        x9 = extract(x8, matcher(first, x7))
        x10 = subtract(ulcorner(x6), x9[1])
        x11 = shift(x8, x10)
        x5 = paint(x5, x11)
    return x5
