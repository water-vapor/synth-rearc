from synth_rearc.core import *


def _split_sections_b0039139(
    grid: Grid,
) -> tuple[tuple[Grid, ...], Boolean]:
    x0 = height(grid)
    x1 = width(grid)
    x2 = tuple(
        x3 for x3 in range(x1) if all(index(grid, (x4, x3)) == ONE for x4 in range(x0))
    )
    if len(x2) > ZERO:
        x3 = []
        x4 = ZERO
        for x5 in x2:
            if x5 > x4:
                x3.append(crop(grid, (ZERO, x4), (x0, subtract(x5, x4))))
            x4 = increment(x5)
        if x4 < x1:
            x3.append(crop(grid, (ZERO, x4), (x0, subtract(x1, x4))))
        return tuple(x3), F
    x3 = tuple(
        x4 for x4 in range(x0) if all(index(grid, (x4, x5)) == ONE for x5 in range(x1))
    )
    x4 = []
    x5 = ZERO
    for x6 in x3:
        if x6 > x5:
            x4.append(crop(grid, (x5, ZERO), (subtract(x6, x5), x1)))
        x5 = increment(x6)
    if x5 < x0:
        x4.append(crop(grid, (x5, ZERO), (subtract(x0, x5), x1)))
    return tuple(x4), T


def verify_b0039139(
    I: Grid,
) -> Grid:
    x0, x1 = _split_sections_b0039139(I)
    x2, x3, x4, x5 = x0
    x6 = extract(objects(x2, T, F, T), matcher(color, FOUR))
    x7 = subgrid(x6, x2)
    x8 = mostcolor(x4)
    x9 = mostcolor(x5)
    x10 = canvas(x9, shape(x7))
    x11 = fill(x10, x8, ofcolor(x7, FOUR))
    x12 = size(objects(x3, T, F, T))
    if x1:
        x13 = canvas(x9, (ONE, width(x11)))
        x14 = x11
        for _ in range(decrement(x12)):
            x14 = vconcat(x14, x13)
            x14 = vconcat(x14, x11)
        return x14
    x13 = canvas(x9, (height(x11), ONE))
    x14 = x11
    for _ in range(decrement(x12)):
        x14 = hconcat(x14, x13)
        x14 = hconcat(x14, x11)
    return x14
