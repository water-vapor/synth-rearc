from arc2.core import *


def _tile2_cf5fd0ad(grid: Grid) -> Grid:
    x0 = hconcat(grid, grid)
    x1 = vconcat(x0, x0)
    return x1


def generate_cf5fd0ad(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = canvas(EIGHT, (THREE, THREE))
    x1 = totuple(asindices(x0))
    x2 = remove(EIGHT, interval(ONE, TEN, ONE))
    while True:
        x3 = unifint(diff_lb, diff_ub, (ONE, FOUR))
        x4 = sample(x1, x3)
        x5 = unifint(diff_lb, diff_ub, (ONE, minimum((THREE, x3))))
        x6 = sample(x2, x5)
        x7 = tuple(choice(x6) for _ in range(x3 - x5))
        x8 = list(x6) + list(x7)
        shuffle(x8)
        gi = x0
        for x9, x10 in zip(x4, x8):
            gi = fill(gi, x10, {x9})
        x11 = rot90(gi)
        x12 = rot180(gi)
        x13 = rot270(gi)
        x14 = frozenset((gi, x11, x12, x13))
        if size(x14) != FOUR:
            continue
        x15 = _tile2_cf5fd0ad(gi)
        x16 = _tile2_cf5fd0ad(x11)
        x17 = _tile2_cf5fd0ad(x12)
        x18 = _tile2_cf5fd0ad(x13)
        x19 = hconcat(x17, x16)
        x20 = hconcat(x18, x15)
        go = vconcat(x19, x20)
        return {"input": gi, "output": go}
