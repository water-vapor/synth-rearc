from arc2.core import *

from .verifier import verify_b5bb5719


def _toggle_b5bb5719(
    value: Integer,
) -> Integer:
    if equality(value, TWO):
        return FIVE
    if equality(value, FIVE):
        return TWO
    return SEVEN


def generate_b5bb5719(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (FIVE, 14))
        x1 = unifint(diff_lb, diff_ub, (THREE, min(TEN, add(halve(x0), FOUR))))
        x2 = choice(("dense", "dense", "alternating"))
        x3 = x0
        if equality(x2, "alternating"):
            x3 = choice(tuple(x4 for x4 in interval(THREE, increment(x0), ONE) if flip(even(x4))))
        x4 = ZERO
        if both(greater(x0, x3), choice((T, F, F))):
            x4 = unifint(diff_lb, diff_ub, (ZERO, subtract(x0, x3)))
        x5 = subtract(subtract(x0, x4), x3)
        x6 = [SEVEN for _ in range(x0)]
        x7 = choice((TWO, FIVE))
        x8 = choice((TWO, FIVE))
        x6[x4] = x7
        x6[subtract(add(x4, x3), ONE)] = x8
        x9 = interval(ONE, subtract(x3, ONE), ONE)
        for x10 in x9:
            x11 = add(x4, x10)
            if equality(x2, "alternating") and flip(even(x10)):
                continue
            x6[x11] = choice((TWO, FIVE))
        x12 = tuple(x6)
        x13 = canvas(SEVEN, astuple(x1, x0))
        x14 = fill(x13, TWO, ofcolor((x12,), TWO))
        x15 = fill(x14, FIVE, ofcolor((x12,), FIVE))
        x16 = [list(x17) for x17 in x15]
        x17 = list(x12[x4:add(x4, x3)])
        x18 = interval(ONE, x1, ONE)
        for x19 in x18:
            x20 = tuple(_toggle_b5bb5719(x21) for x21 in x17[:-TWO])
            x17 = list(x20)
            if len(x17) == ZERO:
                break
            x22 = add(x4, x19)
            for x23, x24 in enumerate(x17):
                x16[x19][add(x22, x23)] = x24
        x25 = tuple(tuple(x26) for x26 in x16)
        if equality(x15, x25):
            continue
        x26 = maximum(tuple(colorcount(x25, x27) for x27 in (TWO, FIVE)))
        if equality(x26, ZERO):
            continue
        if verify_b5bb5719(x15) != x25:
            continue
        return {"input": x15, "output": x25}
