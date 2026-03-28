from arc2.core import *

from .verifier import verify_3d31c5b3


LAYER_SHAPE_3D31C5B3 = (THREE, SIX)
ALL_CELLS_3D31C5B3 = tuple((i, j) for i in range(THREE) for j in range(SIX))
OUTPUT_ZERO_POOL_3D31C5B3 = (ZERO, ZERO, ZERO, ONE, ONE, TWO, THREE)


def _layer_grid_3d31c5b3(
    cells: Indices,
    value: Integer,
) -> Grid:
    x0 = canvas(ZERO, LAYER_SHAPE_3D31C5B3)
    return fill(x0, value, cells)


def generate_3d31c5b3(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (SIX, 13))
        x1 = frozenset(sample(ALL_CELLS_3D31C5B3, x0))
        x2 = tuple(x3 for x3 in ALL_CELLS_3D31C5B3 if x3 not in x1)
        x3 = min(choice(OUTPUT_ZERO_POOL_3D31C5B3), len(x2) - ONE)
        x4 = len(x2) - x3
        x5 = max(ONE, x4 - NINE)
        x6 = min(SEVEN, x4)
        x7 = randint(x5, x6)
        x8 = x4 - x7
        x9 = max(ZERO, x8 - THREE)
        x10 = min(SIX, x8)
        x11 = randint(x9, x10)
        x12 = x8 - x11
        x13 = frozenset(sample(x2, x7))
        x14 = tuple(x15 for x15 in x2 if x15 not in x13)
        x16 = frozenset(sample(x14, x11))
        x17 = tuple(x18 for x18 in x14 if x18 not in x16)
        x19 = frozenset(sample(x17, x12))
        x20 = unifint(diff_lb, diff_ub, (max(SIX, x7), min(11, x0 + x7)))
        x21 = frozenset(sample(tuple(x1), x20 - x7))
        x22 = x13 | x21
        x23 = tuple(x24 for x24 in ALL_CELLS_3D31C5B3 if x24 in x1 or x24 in x13)
        x24 = unifint(diff_lb, diff_ub, (max(FIVE, x11), min(12, x0 + x7 + x11)))
        x25 = frozenset(sample(x23, x24 - x11))
        x26 = x16 | x25
        x27 = tuple(
            x28 for x28 in ALL_CELLS_3D31C5B3 if x28 in x1 or x28 in x13 or x28 in x16
        )
        x28 = unifint(diff_lb, diff_ub, (max(SEVEN, x12), min(TEN, x0 + x7 + x11 + x12)))
        x29 = frozenset(sample(x27, x28 - x12))
        x30 = x19 | x29
        x31 = _layer_grid_3d31c5b3(x1, FIVE)
        x32 = _layer_grid_3d31c5b3(x22, FOUR)
        x33 = _layer_grid_3d31c5b3(x30, TWO)
        x34 = _layer_grid_3d31c5b3(x26, EIGHT)
        x35 = fill(x31, FOUR, x13)
        x36 = fill(x35, EIGHT, x16)
        x37 = fill(x36, TWO, x19)
        x38 = vconcat(x31, x32)
        x39 = vconcat(x33, x34)
        x40 = vconcat(x38, x39)
        if verify_3d31c5b3(x40) != x37:
            continue
        return {"input": x40, "output": x37}
