from arc2.core import *


def generate_2a28add5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = canvas(SEVEN, (TEN, TEN))
    x1 = canvas(SEVEN, (TEN, TEN))
    x2 = interval(ZERO, TEN, ONE)
    x3 = remove(SEVEN, x2)
    x4 = remove(SIX, x3)
    x5 = unifint(diff_lb, diff_ub, (THREE, FIVE))
    x6 = sample(x2, x5)
    x7 = difference(x2, x6)
    gi = x0
    go = x1

    for x8 in x6:
        x9 = randint(ZERO, NINE)
        x10 = min(SEVEN, increment(add(x9, subtract(NINE, x9))))
        x11 = unifint(diff_lb, diff_ub, (THREE, x10))
        x12 = subtract(x11, ONE)
        x13 = max(ZERO, subtract(x12, subtract(NINE, x9)))
        x14 = min(x9, x12)
        x15 = randint(x13, x14)
        x16 = subtract(x12, x15)
        x17 = sample(interval(ZERO, x9, ONE), x15)
        x18 = sample(interval(increment(x9), TEN, ONE), x16)
        gi = fill(gi, SIX, frozenset({astuple(x8, x9)}))
        for x19 in x17:
            x20 = choice(x4)
            gi = fill(gi, x20, frozenset({astuple(x8, x19)}))
        for x21 in x18:
            x22 = choice(x4)
            gi = fill(gi, x22, frozenset({astuple(x8, x21)}))
        x23 = astuple(x8, subtract(x9, x15))
        x24 = astuple(x8, add(x9, x16))
        x25 = connect(x23, x24)
        go = fill(go, EIGHT, x25)

    for x26 in x7:
        x27 = unifint(diff_lb, diff_ub, (ZERO, FIVE))
        if x27 == ZERO:
            continue
        x28 = sample(x2, x27)
        for x29 in x28:
            x30 = choice(x4)
            gi = fill(gi, x30, frozenset({astuple(x26, x29)}))

    return {"input": gi, "output": go}
