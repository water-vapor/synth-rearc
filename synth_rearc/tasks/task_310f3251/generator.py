from synth_rearc.core import *


FG_COLORS_310F3251 = remove(TWO, interval(ONE, TEN, ONE))
GRID_SIZES_310F3251 = (TWO, THREE, FOUR, FOUR, FIVE)
POINT_COUNTS_310F3251 = (ONE, TWO, TWO)


def _marker_indices_310f3251(
    inds: Indices,
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = dims
    return frozenset((((x2 - ONE) % x0), ((x3 - ONE) % x1)) for x2, x3 in inds)


def _tile_three_310f3251(
    G: Grid,
) -> Grid:
    x0 = hconcat(hconcat(G, G), G)
    x1 = vconcat(vconcat(x0, x0), x0)
    return x1


def generate_310f3251(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    _ = diff_lb, diff_ub
    while True:
        x0 = choice(GRID_SIZES_310F3251)
        x1 = choice(POINT_COUNTS_310F3251)
        x2 = tuple(product(interval(ZERO, x0, ONE), interval(ZERO, x0, ONE)))
        x3 = frozenset(sample(x2, x1))
        x4 = choice(FG_COLORS_310F3251)
        x5 = canvas(ZERO, (x0, x0))
        x6 = fill(x5, x4, x3)
        x7 = _marker_indices_310f3251(x3, (x0, x0))
        x8 = underpaint(x6, recolor(TWO, x7))
        if colorcount(x8, TWO) == ZERO:
            continue
        x9 = _tile_three_310f3251(x8)
        return {
            "input": x6,
            "output": x9,
        }
