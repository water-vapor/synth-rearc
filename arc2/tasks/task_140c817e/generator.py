from arc2.core import *


BACKGROUND_COLORS_140C817E = (SEVEN, EIGHT, NINE)


def _sample_axis_140c817e(
    side: int,
    ncenters: int,
) -> tuple[int, ...]:
    for _ in range(200):
        available = list(range(side))
        picked = []
        while len(picked) < ncenters and len(available) > ZERO:
            value = choice(tuple(available))
            picked.append(value)
            available = [other for other in available if abs(other - value) > ONE]
        if len(picked) == ncenters:
            return tuple(sorted(picked))
    raise RuntimeError("failed to sample spaced axis positions")


def _center_count_140c817e(
    side: int,
) -> int:
    if side <= TEN:
        return TWO
    if side <= 12:
        return THREE
    return FOUR


def _paint_output_140c817e(
    grid: Grid,
    centers: Indices,
) -> Grid:
    x0 = fork(combine, hfrontier, vfrontier)
    x1 = mapply(x0, centers)
    x2 = fill(grid, ONE, x1)
    x3 = mapply(ineighbors, centers)
    x4 = fill(x2, THREE, x3)
    x5 = fill(x4, TWO, centers)
    return x5


def generate_140c817e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while T:
        side = unifint(diff_lb, diff_ub, (NINE, 14))
        bg = choice(BACKGROUND_COLORS_140C817E)
        ncenters = _center_count_140c817e(side)
        rows = _sample_axis_140c817e(side, ncenters)
        cols = list(_sample_axis_140c817e(side, ncenters))
        shuffle(cols)
        centers = frozenset((i, j) for i, j in zip(rows, cols))
        gi = fill(canvas(bg, (side, side)), ONE, centers)
        go = _paint_output_140c817e(gi, centers)
        return {"input": gi, "output": go}
