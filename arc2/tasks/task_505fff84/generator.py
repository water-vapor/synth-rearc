from arc2.core import *

from .verifier import verify_505fff84


OUTPUT_HEIGHT_RANGE_505FFF84 = (ONE, FIVE)
OUTPUT_WIDTH_RANGE_505FFF84 = (THREE, SEVEN)
INPUT_HEIGHT_MAX_505FFF84 = 14
INPUT_WIDTH_MIN_505FFF84 = TEN
INPUT_WIDTH_MAX_505FFF84 = 14
TWO_DENSITIES_505FFF84 = (0.30, 0.40, 0.45, 0.50, 0.55, 0.60)


def _random_binary_row_505fff84(
    width: Integer,
    density: float,
) -> tuple[Integer, ...]:
    return tuple(TWO if uniform(0.0, 1.0) < density else ZERO for _ in interval(ZERO, width, ONE))


def generate_505fff84(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, OUTPUT_HEIGHT_RANGE_505FFF84)
        x1 = unifint(diff_lb, diff_ub, OUTPUT_WIDTH_RANGE_505FFF84)
        x2 = maximum((FOUR, add(x0, THREE)))
        x3 = maximum((INPUT_WIDTH_MIN_505FFF84, add(x1, FOUR)))
        x4 = unifint(diff_lb, diff_ub, (x2, INPUT_HEIGHT_MAX_505FFF84))
        x5 = unifint(diff_lb, diff_ub, (x3, INPUT_WIDTH_MAX_505FFF84))
        x6 = tuple(sorted(sample(interval(ZERO, x4, ONE), x0)))
        x7 = choice(TWO_DENSITIES_505FFF84)
        go = tuple(_random_binary_row_505fff84(x1, x7) for _ in interval(ZERO, x0, ONE))
        x8 = [_random_binary_row_505fff84(x5, x7) for _ in interval(ZERO, x4, ONE)]
        x9 = subtract(subtract(x5, x1), TWO)
        for x10, x11 in enumerate(x6):
            x12 = go[x10]
            x13 = randint(ZERO, x9)
            x14 = _random_binary_row_505fff84(x13, x7)
            x15 = subtract(subtract(subtract(x5, x13), x1), TWO)
            x16 = _random_binary_row_505fff84(x15, x7)
            x17 = x14 + (ONE,) + x12 + (EIGHT,) + x16
            x8[x11] = x17
        gi = tuple(x8)
        if verify_505fff84(gi) != go:
            continue
        return {"input": gi, "output": go}
