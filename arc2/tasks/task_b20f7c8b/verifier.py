from arc2.core import *

from .helpers import (
    BLOCK_SHAPE_B20F7C8B,
    block_indices_b20f7c8b,
    normalize_indices_b20f7c8b,
    paint_pattern_at_b20f7c8b,
    paint_solid_at_b20f7c8b,
    shape_key_b20f7c8b,
)


def _is_block_start_b20f7c8b(
    grid: Grid,
    start: tuple[int, int],
) -> bool:
    x0 = crop(grid, start, BLOCK_SHAPE_B20F7C8B)
    x1 = palette(x0)
    x2 = both(ONE in x1, TWO in x1)
    x3 = both(x1 <= {ONE, TWO}, x2)
    x4 = both(size(x1) == ONE, first(x1) not in {ZERO, EIGHT})
    if not either(x3, x4):
        return F
    x5 = block_indices_b20f7c8b(start)
    x6 = frozenset(
        x7 for x7 in outbox(x5)
        if 0 <= x7[0] < height(grid) and 0 <= x7[1] < width(grid)
    )
    x7 = frozenset(index(grid, x8) for x8 in x6)
    return both(size(x6) == 24, both(size(x7) == ONE, first(x7) in {ZERO, EIGHT}))


def verify_b20f7c8b(
    I: Grid,
) -> Grid:
    x0 = shape(I)
    x1 = interval(ZERO, x0[0] - FOUR, ONE)
    x2 = interval(ZERO, x0[1] - FOUR, ONE)
    x3 = product(x1, x2)
    x4 = tuple(sorted(x5 for x5 in x3 if _is_block_start_b20f7c8b(I, x5)))
    x5 = merge(tuple(block_indices_b20f7c8b(x6) for x6 in x4))
    x6 = fill(I, ZERO, x5)
    x7 = tuple(sorted((x8 for x8 in partition(x6) if color(x8) not in {ZERO, EIGHT}), key=color))
    x8 = {color(x9): normalize_indices_b20f7c8b(x9) for x9 in x7}
    x9 = {shape_key_b20f7c8b(x10): x11 for x11, x10 in x8.items()}
    x10 = I
    for x11 in x4:
        x12 = crop(I, x11, BLOCK_SHAPE_B20F7C8B)
        x13 = palette(x12)
        if both(ONE in x13, TWO in x13):
            x14 = ofcolor(x12, ONE)
            x15 = x9[shape_key_b20f7c8b(x14)]
            x10 = paint_solid_at_b20f7c8b(x10, x11, x15)
        else:
            x14 = first(x13)
            x15 = x8[x14]
            x10 = paint_pattern_at_b20f7c8b(x10, x11, x15)
    return x10
