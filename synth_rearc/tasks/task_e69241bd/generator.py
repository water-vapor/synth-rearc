from synth_rearc.core import *


COLOR_POOL_E69241BD = remove(FIVE, remove(ZERO, interval(ZERO, TEN, ONE)))
GRID_SIZES_E69241BD = (SEVEN, NINE, NINE)


def _zero_components_e69241bd(grid: Grid) -> tuple[frozenset[tuple[int, int]], ...]:
    x0 = ofcolor(grid, ZERO)
    x1 = fill(canvas(FIVE, shape(grid)), ONE, x0)
    x2 = colorfilter(objects(x1, T, F, F), ONE)
    return tuple(toindices(x3) for x3 in x2)


def _base_grid_e69241bd(
    size: int,
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    x0 = canvas(ZERO, (size, size))
    x1 = tuple(asindices(x0))
    x2 = size * size
    x3 = unifint(diff_lb, diff_ub, ((x2 * THREE) // EIGHT, (x2 * NINE) // 20))
    x4 = frozenset(sample(x1, x3))
    return fill(x0, FIVE, x4)


def generate_e69241bd(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(GRID_SIZES_E69241BD)
        x1 = _base_grid_e69241bd(x0, diff_lb, diff_ub)
        x2 = _zero_components_e69241bd(x1)
        x3 = tuple(len(x4) for x4 in x2)
        x4 = 7 if x0 == NINE else 5
        x5 = 15 if x0 == NINE else 10
        x6 = 13 if x0 == NINE else 10
        x7 = 3 if x0 == NINE else 2
        if len(x2) < x4 or maximum(x3) > x5:
            continue
        x8 = tuple(x9 for x9 in x2 if THREE <= len(x9) <= x6)
        if len(x8) < TWO:
            continue
        x9 = choice((T, T, F)) if x0 == NINE else choice((T, F, F))
        x10 = THREE if len(x8) >= THREE and x9 else TWO
        if len(x2) - x10 < x7:
            continue
        x11 = tuple(sample(x8, x10))
        x12 = sum(len(x13) for x13 in x11)
        x13 = 15 if x10 == THREE else 12
        x14 = 28 if x0 == NINE else 20
        if x12 < x13 or x12 > x14:
            continue
        x15 = tuple(sample(COLOR_POOL_E69241BD, x10))
        x16 = x1
        x17 = x1
        for x18, x19 in zip(x11, x15):
            x20 = initset(choice(tuple(x18)))
            x16 = fill(x16, x19, x20)
            x17 = fill(x17, x19, x18)
        return {"input": x16, "output": x17}
