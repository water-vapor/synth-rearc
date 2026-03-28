from synth_rearc.core import *

from .helpers import pack_histogram_bottom_up


def _sample_counts(
    diff_lb: float,
    diff_ub: float,
) -> tuple[int, int, int, int]:
    while True:
        x0 = unifint(diff_lb, diff_ub, (44, 54))
        x1 = max(26, 74 - x0)
        x2 = min(32, 82 - x0, x0 - ONE)
        if x1 > x2:
            continue
        x3 = randint(x1, x2)
        x4 = 100 - x0 - x3
        x5 = max(10, x4 - EIGHT, x4 // TWO + ONE)
        x6 = min(20, x3 - ONE, x4 - ONE)
        if x5 > x6:
            continue
        x7 = randint(x5, x6)
        x8 = x4 - x7
        if x0 <= x3 or x3 <= x7 or x7 <= x8 or x8 <= ZERO:
            continue
        return (x0, x3, x7, x8)


def generate_bd283c4a(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = interval(TWO, TEN, ONE)
    while True:
        x1 = sample(x0, FOUR)
        x2 = _sample_counts(diff_lb, diff_ub)
        x3 = [color0 for color0, count0 in zip(x1, x2) for _ in range(count0)]
        shuffle(x3)
        x4 = tuple(tuple(x3[i:i + TEN]) for i in range(ZERO, 100, TEN))
        x5 = pack_histogram_bottom_up((TEN, TEN), x1, x2)
        x6 = frontiers(x4)
        if x4 == x5:
            continue
        if numcolors(x4) != FOUR:
            continue
        if size(x6) != ZERO:
            continue
        return {"input": x4, "output": x5}
