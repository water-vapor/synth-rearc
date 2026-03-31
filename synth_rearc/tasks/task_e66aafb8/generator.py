from synth_rearc.core import *


def _d4_orbit_e66aafb8(
    loc: IntegerTuple,
    n: Integer = 24,
) -> Indices:
    i, j = loc
    x0 = subtract(n, ONE)
    return frozenset(
        {
            (i, j),
            (j, i),
            (j, subtract(x0, i)),
            (i, subtract(x0, j)),
            (subtract(x0, i), j),
            (subtract(x0, j), i),
            (subtract(x0, i), subtract(x0, j)),
            (subtract(x0, j), subtract(x0, i)),
        }
    )


def _rectangle_e66aafb8(
    start: IntegerTuple,
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = start
    x2, x3 = dims
    return frozenset((i, j) for i in range(x0, add(x0, x2)) for j in range(x1, add(x1, x3)))


def _valid_hole_e66aafb8(
    hole: Indices,
    n: Integer = 24,
) -> Boolean:
    for x0 in hole:
        x1 = _d4_orbit_e66aafb8(x0, n)
        if x1 <= hole:
            return False
    return True


def _sample_symmetric_grid_e66aafb8(
    diff_lb: float,
    diff_ub: float,
    n: Integer = 24,
) -> Grid:
    x0 = canvas(ZERO, (n, n))
    x1 = [list(x2) for x2 in x0]
    x2 = set()
    x3 = sample(tuple(interval(ONE, TEN, ONE)), unifint(diff_lb, diff_ub, (5, 9)))
    for x4 in range(n):
        for x5 in range(n):
            x6 = (x4, x5)
            if x6 in x2:
                continue
            x7 = _d4_orbit_e66aafb8(x6, n)
            x8 = choice(x3)
            for x9, x10 in x7:
                x1[x9][x10] = x8
            x2 |= set(x7)
    return tuple(tuple(x4) for x4 in x1)


def generate_e66aafb8(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _sample_symmetric_grid_e66aafb8(diff_lb, diff_ub)
        x1 = unifint(diff_lb, diff_ub, (3, 8))
        x2 = unifint(diff_lb, diff_ub, (3, 8))
        x3 = randint(ZERO, subtract(24, x1))
        x4 = randint(ZERO, subtract(24, x2))
        x5 = _rectangle_e66aafb8((x3, x4), (x1, x2))
        if not _valid_hole_e66aafb8(x5):
            continue
        x6 = crop(x0, (x3, x4), (x1, x2))
        if numcolors(x6) == ONE:
            continue
        x7 = fill(x0, ZERO, x5)
        if numcolors(x7) < FIVE:
            continue
        return {"input": x7, "output": x6}
