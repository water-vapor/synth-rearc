from synth_rearc.core import *


def verify_320afe60(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, F, T)
    x2 = width(I)
    x3 = canvas(x0, shape(I))
    x4 = tuple(delta(x) for x in x1)
    x5 = tuple(
        (
            connect(ulcorner(x), urcorner(x)),
            connect(llcorner(x), lrcorner(x)),
            connect(ulcorner(x), llcorner(x)),
            connect(urcorner(x), lrcorner(x)),
        )
        for x in x1
    )
    x6 = tuple(sum(ONE for y in z if size(intersection(w, y)) > ZERO) for w, z in zip(x4, x5))
    x7 = tuple(
        shift(x, (ZERO, subtract(decrement(x2), rightmost(x)))) if equality(y, ONE)
        else shift(x, (ZERO, invert(leftmost(x))))
        for x, y in zip(x1, x6)
    )
    x8 = tuple(recolor(THREE, x) if equality(y, ONE) else recolor(TWO, x) for x, y in zip(x7, x6))
    x9 = paint(x3, merge(x8))
    return x9
