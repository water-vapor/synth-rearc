from arc2.core import *


PALETTE_CCD554AC = remove(ZERO, interval(ZERO, TEN, ONE))


def _tile_ccd554ac(grid: Grid) -> Grid:
    factor = height(grid)
    expand_row = compose(merge, rbind(repeat, factor))
    tiled_rows = apply(expand_row, grid)
    return merge(repeat(tiled_rows, factor))


def generate_ccd554ac(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    side = unifint(diff_lb, diff_ub, (TWO, FIVE))
    area = side * side
    lower = (area + ONE) // TWO
    upper = min(area - ONE, area - max(ONE, area // THREE))
    nfg = unifint(diff_lb, diff_ub, (lower, upper))
    cells = product(interval(ZERO, side, ONE), interval(ZERO, side, ONE))
    fg = frozenset(sample(tuple(cells), nfg))
    color_ = choice(PALETTE_CCD554AC)
    gi = fill(canvas(ZERO, (side, side)), color_, fg)
    go = _tile_ccd554ac(gi)
    return {"input": gi, "output": go}
