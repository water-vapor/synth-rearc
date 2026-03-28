from synth_rearc.core import *


GRID_SHAPE_7E2BAD24 = (16, 16)


def barrier_orientations_7e2bad24(
    grid: Grid,
    value: Integer,
) -> dict[tuple[int, int], str]:
    x0 = objects(grid, T, F, T)
    x1 = colorfilter(x0, value)
    x2 = {}
    for x3 in x1:
        x4 = "v" if vline(x3) else "h"
        for x5 in toindices(x3):
            x2[x5] = x4
    return x2


def trace_extension_7e2bad24(
    grid: Grid,
    start: tuple[int, int],
    direction: tuple[int, int],
    reflectors: dict[tuple[int, int], str],
) -> tuple[tuple[tuple[int, int], ...], int, bool]:
    x0 = height(grid) * width(grid) * 8
    x1 = []
    x2 = start
    x3 = direction
    x4 = {(x2, x3)}
    x5 = ZERO
    for _ in range(x0):
        x6 = add(x2, x3)
        x7 = index(grid, x6)
        if x7 is None:
            break
        if x7 == TWO:
            x5 = increment(x5)
            x8 = reflectors.get(x6)
            if x8 == "v":
                x3 = astuple(x3[0], invert(x3[1]))
            else:
                x3 = astuple(invert(x3[0]), x3[1])
            x6 = add(x2, x3)
            x7 = index(grid, x6)
            if x7 is None:
                break
            if x7 == TWO:
                return tuple(), x5, F
        elif x7 == THREE:
            x5 = increment(x5)
        x2 = x6
        x9 = (x2, x3)
        if contained(x9, x4):
            return tuple(), x5, F
        x4.add(x9)
        if contained(x2, x1):
            return tuple(), x5, F
        x1.append(x2)
    return tuple(x1), x5, T
