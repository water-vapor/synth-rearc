from synth_rearc.core import *


def _dense_grid_319f2597(
    n: Integer,
) -> Grid:
    return tuple(tuple(randint(ONE, NINE) for _ in range(n)) for _ in range(n))


def generate_319f2597(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    n = 20
    x0 = interval(ZERO, n, ONE)
    x1 = interval(TWO, n - THREE, ONE)
    while True:
        x2 = _dense_grid_319f2597(n)
        x3 = choice(x1)
        x4 = choice(x1)
        x5 = product((x3, x3 + ONE), (x4, x4 + ONE))
        gi = fill(x2, ZERO, x5)
        x6 = product(x0, (x4, x4 + ONE))
        x7 = product((x3, x3 + ONE), x0)
        x8 = combine(x6, x7)
        x9 = ofcolor(gi, TWO)
        x10 = intersection(x8, x9)
        if size(x10) < FIVE:
            continue
        x11 = fill(gi, ZERO, x8)
        go = fill(x11, TWO, x10)
        return {"input": gi, "output": go}
