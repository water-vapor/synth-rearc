from synth_rearc.core import *


def generate_9b365c51(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = (ONE, TWO, THREE, FOUR, SIX, SEVEN)
    while True:
        x1 = unifint(diff_lb, diff_ub, (SIX, EIGHT))
        x2 = unifint(diff_lb, diff_ub, (THREE, SIX))
        x3 = tuple(sample(x0, x2))
        x4 = tuple(unifint(diff_lb, diff_ub, (TWO, FOUR)) for _ in range(x2))
        x5 = tuple(choice((ZERO, ZERO, ZERO, ONE)) for _ in range(x2 - ONE))
        if x2 > ONE and all(v == ONE for v in x5):
            x6 = randint(ZERO, x2 - TWO)
            x5 = x5[:x6] + (ZERO,) + x5[x6 + ONE:]
        x7 = choice((ZERO, ZERO, ZERO, ONE))
        x8 = (x2 * TWO) + ONE + x7 + sum(x4) + sum(x5)
        if x8 > 30:
            continue
        x9 = []
        for x10 in range(x2):
            x11 = False
            for _ in range(30):
                x12 = unifint(diff_lb, diff_ub, (TWO, min(FIVE, x1 - ONE)))
                if x10 == ZERO or x5[x10 - ONE] == ONE:
                    x13 = randint(ZERO, x1 - x12)
                else:
                    x14, x15 = x9[-ONE]
                    x16 = max(ZERO, x14 - x12 + ONE)
                    x17 = min(x1 - x12, x15)
                    x13 = randint(x16, x17)
                x18 = x13 + x12 - ONE
                if x10 > ZERO and x5[x10 - ONE] == ZERO and (x13, x18) == x9[-ONE]:
                    continue
                x9.append((x13, x18))
                x11 = True
                break
            if not x11:
                x9 = []
                break
        if len(x9) != x2:
            continue
        x19 = canvas(ZERO, astuple(x1, x8))
        x20 = canvas(ZERO, astuple(x1, x8))
        for x21, x22 in enumerate(x3):
            x23 = (ZERO, (x21 * TWO) + ONE)
            x24 = (x1 - ONE, (x21 * TWO) + ONE)
            x25 = connect(x23, x24)
            x19 = fill(x19, x22, x25)
        x26 = (x2 * TWO) + ONE + x7
        for x27, x28 in enumerate(x3):
            x29, x30 = x9[x27]
            x31 = x4[x27]
            x32 = product(interval(x29, x30 + ONE, ONE), interval(x26, x26 + x31, ONE))
            x19 = fill(x19, EIGHT, x32)
            x20 = fill(x20, x28, x32)
            x26 = x26 + x31
            if x27 < x2 - ONE:
                x26 = x26 + x5[x27]
        return {"input": x19, "output": x20}
