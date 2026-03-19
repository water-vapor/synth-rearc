from arc2.core import *

from .helpers import assemble_tiles_dc2aa30b


TILE_SHAPE_DC2AA30B = (THREE, THREE)
TILE_CELLS_DC2AA30B = tuple(sorted(asindices(canvas(ZERO, TILE_SHAPE_DC2AA30B))))


def _make_tile_dc2aa30b(n_twos: Integer) -> Grid:
    x0 = frozenset(sample(TILE_CELLS_DC2AA30B, n_twos))
    x1 = canvas(ONE, TILE_SHAPE_DC2AA30B)
    x2 = fill(x1, TWO, x0)
    return x2


def _target_order_dc2aa30b(tiles: tuple[Grid, ...]) -> tuple[Grid, ...]:
    x0 = order(tiles, rbind(colorcount, TWO))
    return (
        x0[TWO],
        x0[ONE],
        x0[ZERO],
        x0[FIVE],
        x0[FOUR],
        x0[THREE],
        x0[EIGHT],
        x0[SEVEN],
        x0[SIX],
    )


def generate_dc2aa30b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (ZERO, NINE))
        x1 = tuple(x2 for x2 in interval(ZERO, TEN, ONE) if x2 != x0)
        x2 = tuple(_make_tile_dc2aa30b(x3) for x3 in x1)
        x3 = _target_order_dc2aa30b(x2)
        x4 = tuple(sample(x2, len(x2)))
        if x4 == x3:
            continue
        x5 = assemble_tiles_dc2aa30b(x4)
        x6 = assemble_tiles_dc2aa30b(x3)
        return {"input": x5, "output": x6}
