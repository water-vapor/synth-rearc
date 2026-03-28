from arc2.core import *


def _tile2_48131b3c(grid: Grid) -> Grid:
    x0 = hconcat(grid, grid)
    x1 = vconcat(x0, x0)
    return x1


def generate_48131b3c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = interval(ONE, TEN, ONE)
    while True:
        x1 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x2 = canvas(ZERO, (x1, x1))
        x3 = totuple(asindices(x2))
        x4 = choice(x0)
        x5 = multiply(x1, x1)
        x6 = unifint(diff_lb, diff_ub, (x1, subtract(x5, x1)))
        x7 = sample(x3, x6)
        gi = fill(x2, x4, x7)
        x8 = switch(gi, ZERO, x4)
        go = _tile2_48131b3c(x8)
        return {"input": gi, "output": go}
