from synth_rearc.core import *


def generate_6ea4a07e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = (THREE, FIVE, EIGHT)
    x1 = (
        TWO,
        THREE,
        THREE,
        THREE,
        FOUR,
        FOUR,
        FOUR,
        FIVE,
    )
    x2 = interval(ZERO, NINE, ONE)
    x3 = tuple((x4 // THREE, x4 % THREE) for x4 in x2)
    while True:
        x4 = choice(x0)
        x5 = branch(choice((T, F)), choice(x1), unifint(diff_lb, diff_ub, (TWO, FIVE)))
        x6 = frozenset(sample(x3, x5))
        x7 = canvas(ZERO, (THREE, THREE))
        x8 = fill(x7, x4, x6)
        x9 = equality(x4, THREE)
        x10 = branch(x9, ONE, FOUR)
        x11 = equality(x4, EIGHT)
        x12 = branch(x11, TWO, x10)
        x13 = difference(asindices(x8), x6)
        x14 = fill(x7, x12, x13)
        return {"input": x8, "output": x14}
