from arc2.core import *


FOREGROUND_COLORS_32E9702F = (ONE, TWO, THREE, FOUR, SIX, SEVEN, EIGHT, NINE)
MAX_BARS_32E9702F = FOUR


def _segment_32e9702f(
    row: Integer,
    left: Integer,
    length: Integer,
) -> Indices:
    return frozenset((row, j) for j in range(left, add(left, length)))


def _spaced_rows_32e9702f(
    height: Integer,
    count: Integer,
) -> Tuple:
    x0 = subtract(add(height, ONE), count)
    x1 = sample(range(x0), count)
    x2 = tuple(sorted(x1))
    return tuple(add(x3, x4) for x3, x4 in enumerate(x2))


def generate_32e9702f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (THREE, 12))
    x1 = unifint(diff_lb, diff_ub, (THREE, 12))
    x2 = choice(FOREGROUND_COLORS_32E9702F)
    x3 = minimum((MAX_BARS_32E9702F, halve(add(x0, ONE))))
    x4 = unifint(diff_lb, diff_ub, (ONE, x3))
    x5 = _spaced_rows_32e9702f(x0, x4)
    x6 = canvas(ZERO, astuple(x0, x1))
    x7 = canvas(FIVE, astuple(x0, x1))
    for x8 in x5:
        x9 = unifint(diff_lb, diff_ub, (TWO, x1))
        x10 = randint(ZERO, subtract(x1, x9))
        x11 = _segment_32e9702f(x8, x10, x9)
        x6 = fill(x6, x2, x11)
        x12 = shift(x11, LEFT)
        x7 = fill(x7, x2, x12)
    return {"input": x6, "output": x7}
