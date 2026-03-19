from arc2.core import *


def split_tiles_dc2aa30b(grid: Grid) -> tuple[Grid, ...]:
    x0 = compress(grid)
    x1 = vsplit(x0, THREE)
    x2 = rbind(hsplit, THREE)
    x3 = apply(x2, x1)
    return merge(x3)


def assemble_tiles_dc2aa30b(tiles: tuple[Grid, ...]) -> Grid:
    x0 = canvas(ZERO, (THREE, ONE))
    x1 = hconcat(tiles[ZERO], x0)
    x2 = hconcat(x1, tiles[ONE])
    x3 = hconcat(x2, x0)
    x4 = hconcat(x3, tiles[TWO])
    x5 = hconcat(tiles[THREE], x0)
    x6 = hconcat(x5, tiles[FOUR])
    x7 = hconcat(x6, x0)
    x8 = hconcat(x7, tiles[FIVE])
    x9 = hconcat(tiles[SIX], x0)
    x10 = hconcat(x9, tiles[SEVEN])
    x11 = hconcat(x10, x0)
    x12 = hconcat(x11, tiles[EIGHT])
    x13 = canvas(ZERO, (ONE, width(x4)))
    x14 = vconcat(x4, x13)
    x15 = vconcat(x14, x8)
    x16 = vconcat(x15, x13)
    x17 = vconcat(x16, x12)
    return x17
