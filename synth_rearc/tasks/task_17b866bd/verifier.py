from synth_rearc.core import *


def verify_17b866bd(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = interval(ZERO, x0, FIVE)
    x3 = interval(ZERO, x1, FIVE)
    x4 = product(x2, x3)
    x5 = lbind(index, I)
    x6 = matcher(x5, ZERO)
    x7 = compose(flip, x6)
    x8 = sfilter(x4, x7)
    x9 = order(x8, identity)
    x10 = connect((ONE, TWO), (ONE, THREE))
    x11 = connect((TWO, ONE), (TWO, FOUR))
    x12 = connect((THREE, ONE), (THREE, FOUR))
    x13 = connect((FOUR, TWO), (FOUR, THREE))
    x14 = combine(x10, x11)
    x15 = combine(x12, x13)
    x16 = combine(x14, x15)
    x17 = lbind(shift, x16)
    x18 = apply(x17, x9)
    x19 = apply(x5, x9)
    x20 = mpapply(recolor, x19, x18)
    x21 = fill(I, ZERO, x8)
    x22 = paint(x21, x20)
    return x22
