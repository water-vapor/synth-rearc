from arc2.core import *


def generate_fd02da9e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = remove(SEVEN, interval(ZERO, TEN, ONE))
    x1 = interval(ZERO, FOUR, ONE)
    x2 = (
        ORIGIN,
        astuple(ZERO, SEVEN),
        astuple(SEVEN, ZERO),
        astuple(SEVEN, SEVEN),
    )
    x3 = interval(ONE, THREE, ONE)
    x4 = interval(FIVE, SEVEN, ONE)
    x5 = product(x3, x3)
    x6 = product(x3, x4)
    x7 = connect(astuple(FOUR, TWO), astuple(FIVE, TWO))
    x8 = insert(astuple(SIX, THREE), x7)
    x9 = connect(astuple(FOUR, FIVE), astuple(FIVE, FIVE))
    x10 = insert(astuple(SIX, FOUR), x9)
    x11 = (x5, x6, x8, x10)
    x12 = unifint(diff_lb, diff_ub, (ONE, FOUR))
    x13 = sample(x1, x12)
    x14 = sample(x0, x12)
    x15 = canvas(SEVEN, (EIGHT, EIGHT))
    x16 = canvas(SEVEN, (EIGHT, EIGHT))
    for x17, x18 in zip(x13, x14):
        x19 = x2[x17]
        x20 = x11[x17]
        x15 = fill(x15, x18, initset(x19))
        x16 = fill(x16, x18, x20)
    return {"input": x15, "output": x16}
