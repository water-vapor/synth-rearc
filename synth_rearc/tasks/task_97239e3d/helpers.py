from synth_rearc.core import *


MARKER_COLORS_97239E3D = (ONE, TWO, THREE, FOUR, SIX, SEVEN)
LATTICE_SIZE_97239E3D = 17
BLOCK_SPAN_97239E3D = FOUR
BLOCK_COUNT_97239E3D = FOUR


def base_grid_97239e3d() -> Grid:
    x0 = canvas(ZERO, (LATTICE_SIZE_97239E3D, LATTICE_SIZE_97239E3D))
    for x1 in range(BLOCK_COUNT_97239E3D):
        for x2 in range(BLOCK_COUNT_97239E3D):
            x3 = add(multiply(x1, BLOCK_SPAN_97239E3D), ONE)
            x4 = add(multiply(x2, BLOCK_SPAN_97239E3D), ONE)
            x5 = frozenset({(x3, x4), (add(x3, TWO), add(x4, TWO))})
            x6 = box(x5)
            x0 = fill(x0, EIGHT, x6)
    return x0


def region_patch_97239e3d(
    top_block: int,
    bottom_block: int,
    left_block: int,
    right_block: int,
) -> Indices:
    x0 = multiply(top_block, BLOCK_SPAN_97239E3D)
    x1 = multiply(left_block, BLOCK_SPAN_97239E3D)
    x2 = multiply(increment(bottom_block), BLOCK_SPAN_97239E3D)
    x3 = multiply(increment(right_block), BLOCK_SPAN_97239E3D)
    x4 = box(frozenset({(x0, x1), (x2, x3)}))
    x5 = interval(add(x0, TWO), x2, BLOCK_SPAN_97239E3D)
    x6 = interval(add(x1, TWO), x3, BLOCK_SPAN_97239E3D)
    x7 = product(x5, x6)
    return x4 | x7
