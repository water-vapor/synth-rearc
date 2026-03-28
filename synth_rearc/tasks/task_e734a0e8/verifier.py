from synth_rearc.core import *

from .helpers import (
    compose_tiles_e734a0e8,
    motif_center_e734a0e8,
    split_tiles_e734a0e8,
    tile_is_motif_e734a0e8,
    tile_is_target_e734a0e8,
)


def verify_e734a0e8(I: Grid) -> Grid:
    x0 = split_tiles_e734a0e8(I)
    x1 = tuple(tile for row in x0 for tile in row)
    x2 = next(tile for tile in x1 if tile_is_motif_e734a0e8(tile))
    x3 = motif_center_e734a0e8(x2)
    x4 = tuple(
        tuple(x2 if tile_is_target_e734a0e8(tile, x3) else tile for tile in row)
        for row in x0
    )
    x5 = compose_tiles_e734a0e8(x4)
    return x5
