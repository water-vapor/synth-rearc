from synth_rearc.core import *


CORNER_COLORS_85fa5666 = (THREE, SIX, SEVEN, EIGHT)


def rotated_corner_specs_from_colors_85fa5666(
    anchor: IntegerTuple,
    colors: tuple[int, int, int, int],
) -> tuple[tuple[IntegerTuple, int, IntegerTuple], ...]:
    x0, x1 = anchor
    x2 = astuple(decrement(x0), decrement(x1))
    x3 = astuple(decrement(x0), add(x1, TWO))
    x4 = astuple(add(x0, TWO), decrement(x1))
    x5 = astuple(add(x0, TWO), add(x1, TWO))
    x6, x7, x8, x9 = colors
    return (
        (x2, x8, (-ONE, -ONE)),
        (x3, x6, (-ONE, ONE)),
        (x4, x9, (ONE, -ONE)),
        (x5, x7, (ONE, ONE)),
    )


def corner_specs_85fa5666(
    grid: Grid,
    anchor: IntegerTuple,
) -> tuple[tuple[IntegerTuple, int, IntegerTuple], ...]:
    x0, x1 = anchor
    x2 = astuple(decrement(x0), decrement(x1))
    x3 = astuple(decrement(x0), add(x1, TWO))
    x4 = astuple(add(x0, TWO), decrement(x1))
    x5 = astuple(add(x0, TWO), add(x1, TWO))
    x6 = (
        index(grid, x2),
        index(grid, x3),
        index(grid, x4),
        index(grid, x5),
    )
    return rotated_corner_specs_from_colors_85fa5666(anchor, x6)


def paint_diagonal_ray_85fa5666(
    grid: Grid,
    start: IntegerTuple,
    step: IntegerTuple,
    color: int,
) -> Grid:
    if color in (None, ZERO):
        return grid
    x0 = len(grid)
    x1 = len(grid[ZERO])
    x2 = list(list(row) for row in grid)
    x3, x4 = start
    x5, x6 = step
    while 0 <= x3 < x0 and 0 <= x4 < x1 and x2[x3][x4] == ZERO:
        x2[x3][x4] = color
        x7 = add(x3, x5)
        x8 = add(x4, x6)
        if not (0 <= x7 < x0 and 0 <= x8 < x1):
            break
        if x2[x7][x8] != ZERO:
            break
        x3, x4 = x7, x8
    return tuple(tuple(row) for row in x2)


def paint_input_block_85fa5666(
    grid: Grid,
    anchor: IntegerTuple,
    colors: tuple[int, int, int, int],
) -> Grid:
    x0, x1 = anchor
    x2 = fill(
        grid,
        TWO,
        product(
            interval(x0, add(x0, TWO), ONE),
            interval(x1, add(x1, TWO), ONE),
        ),
    )
    x3 = (
        (astuple(decrement(x0), decrement(x1)), colors[ZERO]),
        (astuple(decrement(x0), add(x1, TWO)), colors[ONE]),
        (astuple(add(x0, TWO), decrement(x1)), colors[TWO]),
        (astuple(add(x0, TWO), add(x1, TWO)), colors[THREE]),
    )
    x4 = x2
    for x5, x6 in x3:
        x4 = fill(x4, x6, initset(x5))
    return x4
