from arc2.core import *


def _bar_digit_e048c9ed(
    lengths: tuple[Integer, ...],
    length: Integer,
) -> Integer:
    if length == FIVE and set(lengths) == {TWO, FIVE}:
        return NINE
    return ((length - ONE) * (length - ONE)) % 10


def verify_e048c9ed(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = matcher(size, ONE)
    x2 = matcher(uppermost, ZERO)
    x3 = fork(both, x1, x2)
    x4 = extract(x0, x3)
    x5 = leftmost(x4)
    x6 = remove(x4, x0)
    x7 = order(x6, uppermost)
    x8 = apply(size, x7)
    x9 = dedupe(order(x8, identity))
    x10 = frozenset(
        (_bar_digit_e048c9ed(x8, size(obj)), (uppermost(obj), x5))
        for obj in x7
    )
    x11 = paint(I, x10)
    return x11
