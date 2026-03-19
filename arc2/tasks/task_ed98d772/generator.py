from arc2.core import *


def generate_ed98d772(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = canvas(ZERO, (THREE, THREE))
    x1 = totuple(asindices(x0))
    x2 = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        x3 = choice(x2)
        x4 = unifint(diff_lb, diff_ub, (FOUR, SEVEN))
        x5 = sample(x1, x4)
        x6 = fill(x0, x3, x5)
        x7 = rot90(x6)
        x8 = rot180(x6)
        x9 = rot270(x6)
        x10 = frozenset((x6, x7, x8, x9))
        if size(x10) == ONE:
            continue
        x11 = hconcat(x6, x9)
        x12 = hconcat(x8, x7)
        x13 = vconcat(x11, x12)
        return {"input": x6, "output": x13}
