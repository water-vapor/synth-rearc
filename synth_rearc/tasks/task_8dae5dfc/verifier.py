from synth_rearc.core import *


def _layer_profile_8dae5dfc(grid: Grid) -> tuple[tuple[int, ...], tuple[int, ...]]:
    x0 = (min(len(grid), len(grid[0])) + ONE) // TWO
    x1 = tuple(grid[x2][x2] for x2 in range(x0))
    x3 = []
    x4 = []
    for x5 in x1:
        if not x3 or x5 != x3[-1]:
            x3.append(x5)
            x4.append(ONE)
        else:
            x4[-1] += ONE
    return tuple(x3), tuple(x4)


def _render_layers_8dae5dfc(
    dims: tuple[int, int],
    colors: tuple[int, ...],
    thicknesses: tuple[int, ...],
) -> Grid:
    x0 = canvas(ZERO, dims)
    x1 = ZERO
    for x2, x3 in zip(colors, thicknesses):
        for x4 in range(x1, x1 + x3):
            x5 = frozenset(
                (i, j)
                for i in range(x4, dims[0] - x4)
                for j in range(x4, dims[1] - x4)
                if i in (x4, dims[0] - x4 - ONE) or j in (x4, dims[1] - x4 - ONE)
            )
            x0 = fill(x0, x2, x5)
        x1 += x3
    return x0


def verify_8dae5dfc(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = I
    for x2 in x0:
        x3 = ulcorner(x2)
        x4 = subgrid(x2, I)
        x5, x6 = _layer_profile_8dae5dfc(x4)
        x7 = tuple(reversed(x5))
        x8 = _render_layers_8dae5dfc(shape(x4), x7, x6)
        x9 = shift(asobject(x8), x3)
        x1 = paint(x1, x9)
    return x1
