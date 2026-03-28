from arc2.core import *


SIDE_RANGE_50C07299 = (EIGHT, 30)
DEFAULT_BG_50C07299 = SEVEN
DEFAULT_FG_50C07299 = TWO
PALETTE_50C07299 = interval(ZERO, TEN, ONE)


def _max_input_length_50c07299(side: Integer) -> Integer:
    x0 = ONE
    while (x0 + ONE) * (x0 + TWO) // TWO <= side:
        x0 += ONE
    return x0 - ONE


def _chain_segment_50c07299(
    side: Integer,
    length: Integer,
) -> Indices:
    x0 = divide(multiply(length, increment(length)), TWO)
    x1 = subtract(side, x0)
    x2 = astuple(x1, subtract(decrement(side), x1))
    x3 = multiply(decrement(length), DOWN_LEFT)
    x4 = add(x2, x3)
    x5 = connect(x2, x4)
    return x5


def generate_50c07299(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = 16 if choice((T, T, F)) else unifint(diff_lb, diff_ub, SIDE_RANGE_50C07299)
        x1 = _max_input_length_50c07299(x0)
        x2 = unifint(diff_lb, diff_ub, (ONE, x1))
        if choice((T, T, T, F)):
            x3, x4 = DEFAULT_BG_50C07299, DEFAULT_FG_50C07299
        else:
            x3, x4 = sample(PALETTE_50C07299, TWO)
        x5 = canvas(x3, (x0, x0))
        x6 = _chain_segment_50c07299(x0, x2)
        x7 = _chain_segment_50c07299(x0, increment(x2))
        gi = fill(x5, x4, x6)
        go = fill(canvas(x3, (x0, x0)), x4, x7)
        return {"input": gi, "output": go}
