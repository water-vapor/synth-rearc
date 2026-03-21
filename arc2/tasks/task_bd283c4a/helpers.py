from arc2.core import *


def pack_histogram_bottom_up(
    shp: tuple[int, int],
    colors: tuple[int, ...],
    counts: tuple[int, ...],
) -> Grid:
    h, _ = shp
    x0 = canvas(ZERO, shp)
    x1 = ZERO
    x2 = x0
    for color0, count0 in zip(colors, counts):
        x3 = frozenset((h - ONE - (k % h), k // h) for k in range(x1, x1 + count0))
        x2 = fill(x2, color0, x3)
        x1 += count0
    return x2
