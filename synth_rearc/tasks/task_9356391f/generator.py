from synth_rearc.core import *


COLORS_9356391F = (ONE, TWO, THREE, FOUR, SIX, SEVEN, EIGHT, NINE)


def _key_9356391f(
    diff_lb: float,
    diff_ub: float,
) -> tuple[int, ...]:
    while True:
        x0 = unifint(diff_lb, diff_ub, (FOUR, SIX))
        x1 = [choice(COLORS_9356391F)]
        for _ in range(x0 - TWO):
            x1.append(choice(COLORS_9356391F))
        x1.append(choice(COLORS_9356391F))
        if choice((T, T, F)):
            x2 = randint(ONE, x0 - TWO)
            x1[x2] = ZERO
        x3 = tuple(x1)
        x4 = tuple(x5 for x5 in x3 if x5 != ZERO)
        if len(set(x4)) < TWO:
            continue
        return x3


def _paint_key_row_9356391f(
    grid: Grid,
    key: tuple[int, ...],
) -> Grid:
    x0 = grid
    for x1, x2 in enumerate(key):
        if x2 == ZERO:
            continue
        x3 = frozenset(((ZERO, x1),))
        x0 = fill(x0, x2, x3)
    return x0


def _paint_output_9356391f(
    grid: Grid,
    key: tuple[int, ...],
    seed: tuple[int, int],
) -> Grid:
    x0 = seed[ONE]
    x1 = index(grid, (ZERO, x0))
    x2 = frozenset(((ZERO, x0),))
    x3 = branch(equality(x1, ZERO), grid, fill(grid, FIVE, x2))
    x4 = x3
    for x5, x6 in enumerate(key):
        if x6 == ZERO:
            continue
        x7 = interval(subtract(seed[ZERO], x5), increment(add(seed[ZERO], x5)), ONE)
        x8 = interval(subtract(seed[ONE], x5), increment(add(seed[ONE], x5)), ONE)
        x9 = product(x7, x8)
        x10 = box(x9)
        x4 = fill(x4, x6, x10)
    return x4


def generate_9356391f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _key_9356391f(diff_lb, diff_ub)
        x1 = len(x0) - ONE
        x2 = add(SIX, x1)
        x3 = unifint(diff_lb, diff_ub, (ZERO, subtract(15, double(x1))))
        x4 = add(x3, x1)
        x5 = canvas(ZERO, (16, 16))
        x6 = product((ONE,), interval(ZERO, 16, ONE))
        x7 = fill(x5, FIVE, x6)
        x8 = _paint_key_row_9356391f(x7, x0)
        x9 = frozenset(((x2, x4),))
        x10 = fill(x8, x0[ZERO], x9)
        x11 = _paint_output_9356391f(x10, x0, (x2, x4))
        if colorcount(x11, ZERO) < 120:
            continue
        return {"input": x10, "output": x11}
