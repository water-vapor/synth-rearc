from synth_rearc.core import *


SIDE_BOUNDS_A6953F00 = (THREE, TEN)
COLOR_POOL_A6953F00 = interval(ZERO, TEN, ONE)


def _random_grid_a6953f00(
    side: Integer,
) -> Grid:
    return tuple(tuple(choice(COLOR_POOL_A6953F00) for _ in range(side)) for _ in range(side))


def _sample_output_a6953f00() -> Grid:
    while True:
        x0 = tuple(tuple(choice(COLOR_POOL_A6953F00) for _ in range(TWO)) for _ in range(TWO))
        if numcolors(x0) >= THREE:
            return x0


def generate_a6953f00(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, SIDE_BOUNDS_A6953F00)
        x1 = even(x0)
        x2 = subtract(x0, TWO)
        x3 = branch(x1, x2, ZERO)
        x4 = branch(x1, ZERO, x2)
        x5 = astuple(ZERO, x3)
        x6 = astuple(ZERO, x4)
        x7 = _sample_output_a6953f00()
        x8 = shift(asobject(x7), x5)
        x9 = _random_grid_a6953f00(x0)
        gi = paint(x9, x8)
        if numcolors(gi) < FIVE:
            continue
        if crop(gi, x6, TWO_BY_TWO) == x7:
            continue
        return {"input": gi, "output": x7}
