from synth_rearc.core import *


def verify_bf45cf4b(
    I: Grid,
) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = compose(flip, matcher(numcolors, ONE))
    x2 = extract(x0, x1)
    x3 = fgpartition(I)
    x4 = backdrop(x2)
    x5 = lambda x6: size(difference(toindices(x6), x4)) > ZERO
    x6 = extract(x3, x5)
    x7 = subgrid(x2, I)
    x8 = subgrid(x6, I)
    x9 = shape(x8)
    x10 = shape(x7)
    x11 = multiply(x9, x10)
    x12 = mostcolor(I)
    x13 = canvas(x12, x11)
    x14 = color(x6)
    x15 = ofcolor(x8, x14)
    x16 = lbind(multiply, x10)
    x17 = apply(x16, x15)
    x18 = asobject(x7)
    x19 = lbind(shift, x18)
    x20 = mapply(x19, x17)
    x21 = paint(x13, x20)
    return x21
