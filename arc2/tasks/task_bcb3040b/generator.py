from arc2.core import *


def _segment_bcb3040b(
    d: Integer,
) -> tuple[Indices, Indices]:
    x0 = choice(("h", "v", "d", "a"))
    x1 = decrement(d)
    if x0 == "h":
        x2 = randint(ONE, d - TWO)
        x3 = astuple(x2, ZERO)
        x4 = astuple(x2, x1)
    elif x0 == "v":
        x2 = randint(ONE, d - TWO)
        x3 = astuple(ZERO, x2)
        x4 = astuple(x1, x2)
    elif x0 == "d":
        x3 = ORIGIN
        x4 = astuple(x1, x1)
    else:
        x3 = astuple(ZERO, x1)
        x4 = astuple(x1, ZERO)
    x5 = connect(x3, x4)
    x6 = frozenset((x3, x4))
    return x6, x5


def _binary_noise_bcb3040b(
    d: Integer,
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    x0 = canvas(ZERO, (d, d))
    x1 = totuple(asindices(x0))
    x2 = d * d
    x3 = x2 // 3
    x4 = (x2 * 3) // 5
    x5 = unifint(diff_lb, diff_ub, (x3, x4))
    x6 = sample(x1, x5)
    x7 = fill(x0, ONE, x6)
    return x7


def generate_bcb3040b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (10, 18))
        x1 = _binary_noise_bcb3040b(x0, diff_lb, diff_ub)
        x2, x3 = _segment_bcb3040b(x0)
        x4 = difference(x3, x2)
        x5 = intersection(x4, ofcolor(x1, ZERO))
        x6 = intersection(x4, ofcolor(x1, ONE))
        if size(x5) == ZERO or size(x6) == ZERO:
            continue
        gi = fill(x1, TWO, x2)
        go = fill(gi, TWO, x5)
        go = fill(go, THREE, x6)
        return {"input": gi, "output": go}
