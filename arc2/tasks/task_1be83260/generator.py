from arc2.core import *


GRID_BOUNDS = (TWO, THREE)
COLORS = remove(ZERO, interval(ZERO, TEN, ONE))


def _sample_holes(
    nr: int,
    nc: int,
    diff_lb: float,
    diff_ub: float,
) -> frozenset[tuple[int, int]]:
    x0 = tuple((i, j) for i in range(nr) for j in range(nc))
    x1 = max(TWO, max(nr, nc))
    x2 = nr * nc - ONE
    while True:
        x3 = unifint(diff_lb, diff_ub, (x1, x2))
        x4 = frozenset(sample(x0, x3))
        x5 = all(any(i == r for i, _ in x4) for r in range(nr))
        x6 = all(any(j == c for _, j in x4) for c in range(nc))
        if both(x5, x6):
            return x4


def _build_clean_tile(
    nr: int,
    nc: int,
    base: int,
    holes: frozenset[tuple[int, int]],
) -> Grid:
    x0 = canvas(base, (double(nr) + ONE, double(nc) + ONE))
    x1 = frozenset((double(i) + ONE, double(j) + ONE) for i, j in holes)
    x2 = fill(x0, ZERO, x1)
    return x2


def _build_marked_tile(
    clean_tile: Grid,
    markers: dict[tuple[int, int], int],
) -> Grid:
    x0 = clean_tile
    for (i, j), value in markers.items():
        x1 = initset((double(i) + ONE, double(j) + ONE))
        x0 = fill(x0, value, x1)
    return x0


def _paint_nonzero(
    grid: Grid,
    tile: Grid,
    loc: tuple[int, int],
) -> Grid:
    x0 = frozenset(
        (value, add(loc, (i, j)))
        for i, row in enumerate(tile)
        for j, value in enumerate(row)
        if value != ZERO
    )
    x1 = paint(grid, x0)
    return x1


def _render_output(
    nr: int,
    nc: int,
    base: int,
    clean_tile: Grid,
    markers: dict[tuple[int, int], int],
) -> Grid:
    x0 = height(clean_tile)
    x1 = width(clean_tile)
    x2 = nr * x0 + nr - ONE
    x3 = nc * x1 + nc - ONE
    x4 = canvas(base, (x2, x3))
    x5 = ofcolor(clean_tile, base)
    for i in range(nr):
        for j in range(nc):
            x6 = i * (x0 + ONE)
            x7 = j * (x1 + ONE)
            x8 = markers.get((i, j), base)
            x9 = shift(x5, (x6, x7))
            x4 = fill(x4, x8, x9)
    return x4


def generate_1be83260(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, GRID_BOUNDS)
    x1 = unifint(diff_lb, diff_ub, GRID_BOUNDS)
    x2 = choice(COLORS)
    x3 = _sample_holes(x0, x1, diff_lb, diff_ub)
    x4 = remove(x2, COLORS)
    x5 = min(FOUR, len(x4))
    x6 = min(max(TWO, len(x3)), x5)
    x7 = unifint(diff_lb, diff_ub, (TWO, x6))
    x8 = sample(x4, x7)
    while True:
        x9 = {loc: choice(x8) for loc in x3}
        if len(set(x9.values())) >= min(TWO, len(x9)):
            break
    x10 = _build_clean_tile(x0, x1, x2, x3)
    x11 = _build_marked_tile(x10, x9)
    x12 = height(x10)
    x13 = width(x10)
    x14 = x0 * x12 + x0 - ONE
    x15 = x1 * x13 + x1 - ONE
    x16 = 30 - x14
    x17 = 30 - x15
    x18 = randint(ZERO, x16)
    x19 = randint(ZERO, x16 - x18)
    x20 = randint(ZERO, x17)
    x21 = randint(ZERO, x17 - x20)
    x22 = canvas(ZERO, (x14 + x18 + x19, x15 + x20 + x21))
    x23 = tuple(i * (x12 + ONE) for i in range(x0))
    x24 = tuple(j * (x13 + ONE) for j in range(x1))
    x25 = (randint(ZERO, x0 - ONE), randint(ZERO, x1 - ONE))
    for i, a in enumerate(x23):
        for j, b in enumerate(x24):
            x26 = add((a, b), (x18, x20))
            x27 = x11 if (i, j) == x25 else x10
            x22 = _paint_nonzero(x22, x27, x26)
    x28 = _render_output(x0, x1, x2, x10, x9)
    return {"input": x22, "output": x28}
