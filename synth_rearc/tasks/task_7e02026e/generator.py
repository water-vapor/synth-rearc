from synth_rearc.core import *


GRID_SHAPE = (12, 12)
CENTER_COUNT_OPTIONS = (TWO, TWO, THREE, THREE, FOUR, FOUR, FIVE)
ZERO_COUNT_BOUNDS = (56, 76)
ALL_LOCS = tuple((i, j) for i in range(GRID_SHAPE[0]) for j in range(GRID_SHAPE[1]))
INTERIOR_LOCS = tuple(
    (i, j)
    for i in range(ONE, GRID_SHAPE[0] - ONE)
    for j in range(ONE, GRID_SHAPE[1] - ONE)
)
CENTER_STEP_OPTIONS = tuple(
    (di, dj)
    for di in (-ONE, ZERO, ONE)
    for dj in (-ONE, ZERO, ONE)
    if (di, dj) != ORIGIN
)


def _plus_centers(grid: Grid) -> frozenset[tuple[int, int]]:
    x0 = set()
    for i, j in INTERIOR_LOCS:
        if grid[i][j] != ZERO:
            continue
        x1 = dneighbors((i, j)) | frozenset({(i, j)})
        if colorcount(toobject(x1, grid), ZERO) == FIVE:
            x0.add((i, j))
    return frozenset(x0)


def _plus_cover(centers: frozenset[tuple[int, int]]) -> frozenset[tuple[int, int]]:
    x0 = set()
    for x1 in centers:
        x0 |= {x1}
        x0 |= set(dneighbors(x1))
    return frozenset(x0)


def _neighbor_centers(loc: tuple[int, int]) -> tuple[tuple[int, int], ...]:
    x0 = []
    for di, dj in CENTER_STEP_OPTIONS:
        x1 = loc[0] + di
        x2 = loc[1] + dj
        if 1 <= x1 < GRID_SHAPE[0] - 1 and 1 <= x2 < GRID_SHAPE[1] - 1:
            x0.append((x1, x2))
    return tuple(x0)


def _sample_centers() -> frozenset[tuple[int, int]]:
    x0 = choice(CENTER_COUNT_OPTIONS)
    x1 = []
    while len(x1) < x0:
        if len(x1) == ZERO or choice((T, F, F)):
            x2 = [x3 for x3 in INTERIOR_LOCS if x3 not in x1]
        else:
            x2 = []
            x3 = x1[:]
            shuffle(x3)
            for x4 in x3:
                x5 = list(_neighbor_centers(x4))
                shuffle(x5)
                for x6 in x5:
                    if x6 not in x1 and x6 not in x2:
                        x2.append(x6)
            if len(x2) == ZERO:
                x2 = [x3 for x3 in INTERIOR_LOCS if x3 not in x1]
        x1.append(choice(x2))
    return frozenset(x1)


def _densify_grid(
    grid: Grid,
    centers: frozenset[tuple[int, int]],
    target_zeros: int,
) -> Grid:
    x0 = [x1 for x1 in ALL_LOCS if index(grid, x1) != ZERO]
    shuffle(x0)
    x1 = grid
    for x2 in x0:
        if colorcount(x1, ZERO) >= target_zeros:
            break
        x3 = fill(x1, ZERO, frozenset({x2}))
        if _plus_centers(x3) == centers:
            x1 = x3
    return x1


def generate_7e02026e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _sample_centers()
        x1 = _plus_cover(x0)
        x2 = max(ZERO_COUNT_BOUNDS[0], len(x1))
        x3 = unifint(diff_lb, diff_ub, (x2, ZERO_COUNT_BOUNDS[1]))
        x4 = canvas(EIGHT, GRID_SHAPE)
        x5 = fill(x4, ZERO, x1)
        x6 = _densify_grid(x5, x0, x3)
        x7 = _plus_centers(x6)
        x8 = colorcount(x6, ZERO)
        if x7 != x0:
            continue
        if x8 < ZERO_COUNT_BOUNDS[0]:
            continue
        x9 = fill(x6, THREE, _plus_cover(x7))
        return {"input": x6, "output": x9}
