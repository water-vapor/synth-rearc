from synth_rearc.core import *


def _is_key_58743b76(grid: Grid) -> bool:
    x0 = palette(grid)
    return len(x0) == FOUR and ZERO not in x0 and EIGHT not in x0


def _normalize_58743b76(
    grid: Grid,
) -> tuple[Grid, callable]:
    x0 = height(grid)
    x1 = width(grid)
    x2 = crop(grid, (ZERO, ZERO), TWO_BY_TWO)
    x3 = crop(grid, (ZERO, x1 - TWO), TWO_BY_TWO)
    x4 = crop(grid, (x0 - TWO, ZERO), TWO_BY_TWO)
    x5 = crop(grid, (x0 - TWO, x1 - TWO), TWO_BY_TWO)
    if _is_key_58743b76(x2):
        return grid, identity
    if _is_key_58743b76(x3):
        return vmirror(grid), vmirror
    if _is_key_58743b76(x4):
        return hmirror(grid), hmirror
    if _is_key_58743b76(x5):
        return rot180(grid), rot180
    return grid, identity


def verify_58743b76(I: Grid) -> Grid:
    x0, x1 = _normalize_58743b76(I)
    x2 = height(x0)
    x3 = width(x0)
    x4 = crop(x0, (ZERO, ZERO), TWO_BY_TWO)
    x5 = crop(x0, TWO_BY_TWO, (x2 - TWO, x3 - TWO))
    x6 = tuple(x7 for x7 in palette(x5) if x7 != ZERO)
    if len(x6) == ZERO:
        return I
    x7 = first(x6)
    x8 = ofcolor(x5, x7)
    x9 = (x2 - TWO) // TWO
    x10 = (x3 - TWO) // TWO
    x11 = frozenset((x12, x13) for x12, x13 in x8 if x12 < x9 and x13 < x10)
    x12 = frozenset((x13, x14) for x13, x14 in x8 if x13 < x9 and x14 >= x10)
    x13 = frozenset((x14, x15) for x14, x15 in x8 if x14 >= x9 and x15 < x10)
    x14 = frozenset((x15, x16) for x15, x16 in x8 if x15 >= x9 and x16 >= x10)
    x15 = fill(x0, x4[ZERO][ZERO], shift(x11, TWO_BY_TWO))
    x16 = fill(x15, x4[ZERO][ONE], shift(x12, TWO_BY_TWO))
    x17 = fill(x16, x4[ONE][ZERO], shift(x13, TWO_BY_TWO))
    x18 = fill(x17, x4[ONE][ONE], shift(x14, TWO_BY_TWO))
    return x1(x18)
