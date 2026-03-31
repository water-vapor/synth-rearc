from synth_rearc.core import *


GRID_SIZE_903D1B4A = 16
BLOCK_SIZE_903D1B4A = 4
AVAILABLE_COLORS_903D1B4A = (ONE, TWO, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)
UPPER_TRIANGLE_CELLS_903D1B4A = (
    (ZERO, ZERO),
    (ZERO, ONE),
    (ZERO, TWO),
    (ZERO, THREE),
    (ONE, ONE),
    (ONE, TWO),
    (ONE, THREE),
    (TWO, TWO),
    (TWO, THREE),
    (THREE, THREE),
)


def render_output_903d1b4a(
    block_a: Grid,
    block_b: Grid,
    block_d: Grid,
) -> Grid:
    x0 = hconcat(block_a, block_b)
    x1 = hconcat(block_b, block_d)
    x2 = vconcat(x0, x1)
    x3 = hconcat(x2, vmirror(x2))
    x4 = vconcat(x3, hmirror(x3))
    return x4


def rect_patch_903d1b4a(
    top: Integer,
    left: Integer,
    height: Integer,
    width: Integer,
):
    x0 = interval(top, add(top, height), ONE)
    x1 = interval(left, add(left, width), ONE)
    return product(x0, x1)
