from arc2.core import *


COLORS_CA8DE6EA = remove(ZERO, interval(ZERO, TEN, ONE))


def generate_ca8de6ea(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = tuple(sample(COLORS_CA8DE6EA, FIVE))
    x1, x2, x3, x4, x5 = x0
    x6 = canvas(ZERO, (FIVE, FIVE))
    x7 = astuple(FOUR, FOUR)
    x8 = initset(ORIGIN)
    x9 = insert(x7, x8)
    x10 = fill(x6, x1, x9)
    x11 = astuple(ZERO, FOUR)
    x12 = astuple(FOUR, ZERO)
    x13 = initset(x11)
    x14 = insert(x12, x13)
    x15 = fill(x10, x2, x14)
    x16 = astuple(THREE, THREE)
    x17 = initset(UNITY)
    x18 = insert(x16, x17)
    x19 = fill(x15, x3, x18)
    x20 = astuple(ONE, THREE)
    x21 = astuple(THREE, ONE)
    x22 = initset(x20)
    x23 = insert(x21, x22)
    x24 = fill(x19, x4, x23)
    x25 = initset(TWO_BY_TWO)
    x26 = fill(x24, x5, x25)
    x27 = (
        (x1, x3, x2),
        (x4, x5, x4),
        (x2, x3, x1),
    )
    return {"input": x26, "output": x27}
