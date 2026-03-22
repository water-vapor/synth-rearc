from arc2.core import *


TOP_COLORS_7E4D4F7C = remove(SIX, interval(ZERO, TEN, ONE))
ALL_COLORS_7E4D4F7C = interval(ZERO, TEN, ONE)


def generate_7e4d4f7c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (THREE, 12))
    x1 = unifint(diff_lb, diff_ub, (FIVE, 13))
    x2, x3 = sample(TOP_COLORS_7E4D4F7C, TWO)
    x4 = choice(remove(x2, remove(x3, ALL_COLORS_7E4D4F7C)))
    x5 = max(TWO, x1 // THREE)
    x6 = min(subtract(x1, TWO), x1 - x5)
    x7 = unifint(diff_lb, diff_ub, (x5, x6))
    x8 = frozenset(sample(tuple(range(x1)), x7))
    x9 = frozenset((ZERO, x10) for x10 in x8)
    x11 = canvas(x2, (ONE, x1))
    x12 = fill(x11, x3, x9)
    x13 = canvas(x2, (ONE, x1))
    x14 = fill(x13, x4, frozenset({ORIGIN}))
    x15 = frozenset((x16, ZERO) for x16 in range(ONE, x0, TWO))
    gi = canvas(x2, (x0, x1))
    gi = fill(gi, x4, x15)
    gi = fill(gi, x3, x9)
    x17 = replace(x12, x3, SIX)
    go = vconcat(x12, x14)
    go = vconcat(go, x17)
    return {"input": gi, "output": go}
