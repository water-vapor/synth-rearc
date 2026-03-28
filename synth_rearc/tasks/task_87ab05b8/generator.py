from synth_rearc.core import *


def _quadrant_patch_87ab05b8(
    row_block: Integer,
    col_block: Integer,
) -> Indices:
    x0 = interval(multiply(row_block, TWO), multiply(row_block, TWO) + TWO, ONE)
    x1 = interval(multiply(col_block, TWO), multiply(col_block, TWO) + TWO, ONE)
    x2 = product(x0, x1)
    return x2


def generate_87ab05b8(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = canvas(SIX, astuple(FOUR, FOUR))
    x1 = (astuple(ZERO, ZERO), astuple(ZERO, ONE), astuple(ONE, ZERO), astuple(ONE, ONE))
    x2 = choice(x1)
    x3 = _quadrant_patch_87ab05b8(x2[ZERO], x2[ONE])
    x4 = choice(tuple(x3))
    x5 = fill(x0, TWO, initset(x4))
    x6 = []
    for x7 in x1:
        x8 = tuple(x9 for x9 in _quadrant_patch_87ab05b8(x7[ZERO], x7[ONE]) if x9 != x4)
        x9 = branch(equality(x7, x2), randint(ZERO, ONE), randint(ONE, TWO))
        if x9 > ZERO:
            x6.extend(sample(x8, x9))
    x10 = (ZERO, ONE, FOUR, FIVE, EIGHT, NINE)
    x11 = randint(THREE, min(FIVE, len(x6)))
    x12 = list(sample(x10, x11))
    x13 = list(x6)
    shuffle(x13)
    x14 = x12 + [choice(x12) for _ in range(len(x13) - x11)]
    shuffle(x14)
    gi = x5
    for x15, x16 in zip(x13, x14):
        gi = fill(gi, x16, initset(x15))
    go = fill(x0, TWO, x3)
    return {"input": gi, "output": go}
