from arc2.core import *


def verify_ad38a9d0(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ONE)})
    x2 = frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ONE), (ONE, TWO)})
    x3 = frozenset(
        {
            (ZERO, ONE),
            (ONE, ZERO),
            (ONE, ONE),
            (ONE, TWO),
            (TWO, ONE),
        }
    )
    x4 = frozenset({(ZERO, ZERO), (ONE, ZERO), (TWO, ZERO)})
    x5 = frozenset({(ZERO, ZERO), (ONE, ZERO)})
    x6 = frozenset(
        {
            (ZERO, ZERO),
            (ZERO, ONE),
            (ZERO, TWO),
            (ONE, ZERO),
            (ONE, ONE),
            (ONE, TWO),
        }
    )
    x7 = compose(normalize, toindices)
    x8 = matcher(x7, x1)
    x9 = sfilter(x0, x8)
    x10 = mapply(lbind(recolor, FOUR), x9)
    x11 = matcher(x7, x2)
    x12 = sfilter(x0, x11)
    x13 = mapply(lbind(recolor, EIGHT), x12)
    x14 = matcher(x7, x3)
    x15 = sfilter(x0, x14)
    x16 = mapply(lbind(recolor, THREE), x15)
    x17 = matcher(x7, x4)
    x18 = sfilter(x0, x17)
    x19 = mapply(lbind(recolor, TWO), x18)
    x20 = matcher(x7, x5)
    x21 = sfilter(x0, x20)
    x22 = mapply(lbind(recolor, NINE), x21)
    x23 = matcher(x7, x6)
    x24 = sfilter(x0, x23)
    x25 = mapply(lbind(recolor, FIVE), x24)
    x26 = canvas(SEVEN, shape(I))
    x27 = paint(x26, x10)
    x28 = paint(x27, x13)
    x29 = paint(x28, x16)
    x30 = paint(x29, x19)
    x31 = paint(x30, x22)
    x32 = paint(x31, x25)
    return x32
