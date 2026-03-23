from arc2.core import *


def _grow_shape_2072aba6(
    x0: Integer,
    x1: Integer,
) -> Indices:
    x2 = frozenset((i, j) for i in range(x0) for j in range(x0))
    x3 = {choice(tuple(x2))}
    while len(x3) < x1:
        x4 = set()
        for x5 in x3:
            x6 = intersection(neighbors(x5), x2)
            x7 = difference(x6, x3)
            x4 |= x7
        x8 = choice(tuple(x4))
        x3.add(x8)
    return frozenset(x3)


def generate_2072aba6(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (THREE, TEN))
        x1 = min(subtract(multiply(x0, x0), ONE), add(x0, TWO))
        x2 = unifint(diff_lb, diff_ub, (THREE, x1))
        x3 = _grow_shape_2072aba6(x0, x2)
        if not greater(height(x3), ONE):
            continue
        if not greater(width(x3), ONE):
            continue
        x4 = canvas(ZERO, (x0, x0))
        x5 = fill(x4, FIVE, x3)
        x6 = upscale(x5, TWO)
        x7 = replace(x6, FIVE, ONE)
        x8 = ofcolor(x6, FIVE)
        x9 = fork(add, first, last)
        x10 = compose(flip, even)
        x11 = compose(x10, x9)
        x12 = sfilter(x8, x11)
        x13 = fill(x7, TWO, x12)
        return {"input": x5, "output": x13}
