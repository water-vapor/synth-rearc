from arc2.core import *


def _collapse_runs_ce8d95cc(
    grid: Grid,
) -> Grid:
    x0 = [grid[ZERO]]
    for x1 in grid[ONE:]:
        if x1 != x0[NEG_ONE]:
            x0.append(x1)
    return tuple(x0)


def verify_ce8d95cc(I: Grid) -> Grid:
    x0 = _collapse_runs_ce8d95cc(I)
    x1 = dmirror(x0)
    x2 = _collapse_runs_ce8d95cc(x1)
    x3 = dmirror(x2)
    return x3
