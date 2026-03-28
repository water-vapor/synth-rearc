from synth_rearc.core import *


def generate_195ba7dc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = tuple(product(interval(ZERO, FIVE, ONE), interval(ZERO, SIX, ONE)))
    x1 = canvas(ZERO, (FIVE, SIX))
    x2 = canvas(TWO, (FIVE, ONE))
    x3 = ((SEVEN, ZERO), (ZERO, SEVEN), (SEVEN, SEVEN))
    while True:
        x4 = unifint(diff_lb, diff_ub, (18, 24))
        x5 = frozenset(sample(x0, x4))
        x6 = set()
        x7 = set()
        x8 = ZERO
        x9 = ZERO
        x10 = ZERO
        for x11 in x5:
            x12 = choice(x3)
            if x12[ZERO] == SEVEN:
                x6.add(x11)
            if x12[ONE] == SEVEN:
                x7.add(x11)
            if x12 == (SEVEN, ZERO):
                x8 = increment(x8)
            elif x12 == (ZERO, SEVEN):
                x9 = increment(x9)
            else:
                x10 = increment(x10)
        if ZERO in (x8, x9, x10):
            continue
        x13 = fill(x1, SEVEN, x6)
        x14 = fill(x1, SEVEN, x7)
        x15 = hconcat(hconcat(x13, x2), x14)
        x16 = fill(x1, ONE, x5)
        return {"input": x15, "output": x16}
