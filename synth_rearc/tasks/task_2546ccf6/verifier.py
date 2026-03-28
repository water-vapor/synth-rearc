from synth_rearc.core import *

from .helpers import cell_layout_2546ccf6, crop_cell_2546ccf6, paint_cell_grid_2546ccf6


def _cell_color_2546ccf6(
    cell_grid: Grid,
) -> Integer | None:
    x0 = tuple(value for value in palette(cell_grid) if value != ZERO)
    if len(x0) != ONE:
        return None
    return x0[ZERO]


def verify_2546ccf6(I: Grid) -> Grid:
    x0, x1, _ = cell_layout_2546ccf6(I)
    x2 = (
        (ZERO, ZERO),
        (ZERO, ONE),
        (ONE, ZERO),
        (ONE, ONE),
    )
    x3 = I
    for x4 in range(len(x0) - ONE):
        for x5 in range(len(x1) - ONE):
            x6 = tuple(crop_cell_2546ccf6(I, x0, x1, add(x4, a), add(x5, b)) for a, b in x2)
            x7 = tuple(_cell_color_2546ccf6(cell_grid) for cell_grid in x6)
            x8 = tuple(index_value for index_value, color_value in enumerate(x7) if color_value is not None)
            if len(x8) != THREE:
                continue
            x9 = {x7[index_value] for index_value in x8}
            if len(x9) != ONE:
                continue
            x10 = next(index_value for index_value in range(FOUR) if index_value not in x8)
            x11 = subtract(THREE, x10)
            if x10 in (ZERO, THREE):
                x12, x13 = ONE, TWO
            else:
                x12, x13 = ZERO, THREE
            if rot180(x6[x12]) != x6[x13]:
                continue
            x14 = rot180(x6[x11])
            x15, x16 = x2[x10]
            x3 = paint_cell_grid_2546ccf6(x3, x0, x1, add(x4, x15), add(x5, x16), x14)
    return x3
