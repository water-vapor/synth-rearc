from arc2.core import *


def generate_9473c6fb(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = (ZERO, ONE, TWO, FOUR, SIX, NINE)
    while True:
        x1 = choice((True, False))
        if x1:
            x2 = unifint(diff_lb, diff_ub, (SIX, TEN))
            x3 = unifint(diff_lb, diff_ub, (EIGHT, 12))
            x4 = max(FIVE, x2 - TWO)
            x5 = x2
        else:
            x2 = unifint(diff_lb, diff_ub, (SIX, TEN))
            x3 = unifint(diff_lb, diff_ub, (NINE, 12))
            x4 = max(SIX, x3 - TWO)
            x5 = x3
        if x4 > x5:
            continue
        x6 = unifint(diff_lb, diff_ub, (x4, x5))
        if x1:
            x7 = tuple(sorted(sample(interval(ZERO, x2, ONE), x6)))
            x8 = tuple(interval(ZERO, x3, ONE))
            x9 = min(x3 - ONE, max(THREE, x6 // TWO + ONE))
            x10 = randint(THREE, x9)
            x11 = tuple(sorted(sample(x8, x10)))
            x12 = tuple(choice(x11) for _ in x7)
            if size(frozenset(x12)) == x6:
                continue
            x13 = frozenset((x14, x15) for x14, x15 in zip(x7, x12))
        else:
            x7 = tuple(sorted(sample(interval(ZERO, x3, ONE), x6)))
            x8 = tuple(interval(ZERO, x2, ONE))
            x9 = min(x2 - ONE, max(THREE, x6 // TWO + ONE))
            x10 = randint(THREE, x9)
            x11 = tuple(sorted(sample(x8, x10)))
            x12 = tuple(choice(x11) for _ in x7)
            if size(frozenset(x12)) == x6:
                continue
            x13 = frozenset((x15, x14) for x14, x15 in zip(x7, x12))
        x14 = choice((THREE, THREE, THREE, FOUR))
        x15 = tuple(sample(x0, x14))
        x16 = canvas(SEVEN, astuple(x2, x3))
        x17 = x16
        for x18 in x13:
            x19 = choice(x15)
            x17 = fill(x17, x19, initset(x18))
        x20 = apply(first, x13)
        x21 = equality(size(x20), size(x13))
        x22 = order(x13, identity)
        x23 = order(x13, last)
        x24 = branch(x21, x22, x23)
        x25 = size(x24)
        x26 = interval(ZERO, x25, THREE)
        x27 = interval(ONE, x25, THREE)
        x28 = interval(TWO, x25, THREE)
        x29 = frozenset(x24[x30] for x30 in x26)
        x31 = frozenset(x24[x32] for x32 in x27)
        x33 = frozenset(x24[x34] for x34 in x28)
        x35 = fill(x17, TWO, x29)
        x36 = fill(x35, EIGHT, x31)
        x37 = fill(x36, FIVE, x33)
        if x17 == x37:
            continue
        if numcolors(x17) != x14 + ONE:
            continue
        return {"input": x17, "output": x37}
