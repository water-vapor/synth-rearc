from __future__ import annotations

from itertools import combinations

from synth_rearc.core import *


HEIGHT_BOUNDS_358BA94E = (14, 19)
WIDTH_BOUNDS_358BA94E = (18, 19)
OBJECT_COUNT_OPTIONS_358BA94E = (FOUR, FIVE, FIVE)
COMMON_HOLE_COUNT_OPTIONS_358BA94E = (ONE, TWO, TWO, THREE)

FULL_BLOCK_358BA94E = asindices(canvas(ZERO, (FIVE, FIVE)))
INTERIOR_CELLS_358BA94E = product(interval(ONE, FOUR, ONE), interval(ONE, FOUR, ONE))
INNER_RING_CELLS_358BA94E = difference(INTERIOR_CELLS_358BA94E, frozenset({(TWO, TWO)}))


def _well_spaced_holes_358ba94e(
    holes: tuple[IntegerTuple, ...],
) -> Boolean:
    for x0, x1 in combinations(holes, TWO):
        if abs(x0[ZERO] - x1[ZERO]) + abs(x0[ONE] - x1[ONE]) == ONE:
            return F
    x2 = fill(canvas(ONE, (FIVE, FIVE)), ZERO, frozenset(holes))
    x3 = colorfilter(objects(x2, T, F, F), ONE)
    return size(x3) == ONE


HOLE_PATTERNS_358BA94E = {
    x0: tuple(
        frozenset(x1)
        for x1 in combinations(tuple(INNER_RING_CELLS_358BA94E), x0)
        if _well_spaced_holes_358ba94e(x1)
    )
    for x0 in range(1, 5)
}


def _start_options_358ba94e(
    limit: Integer,
    count: Integer,
) -> tuple[tuple[Integer, ...], ...]:
    x0 = []
    for x1 in combinations(interval(ZERO, limit - FOUR, ONE), count):
        if all(x3 - x2 >= SIX for x2, x3 in zip(x1, x1[ONE:])):
            x0.append(x1)
    return tuple(x0)


def _render_pattern_358ba94e(
    color_value: Integer,
    holes: Indices,
) -> Grid:
    return fill(canvas(color_value, (FIVE, FIVE)), ZERO, holes)


def _paint_block_358ba94e(
    grid: Grid,
    color_value: Integer,
    top: Integer,
    left: Integer,
    holes: Indices,
) -> Grid:
    x0 = difference(FULL_BLOCK_358BA94E, holes)
    x1 = shift(x0, (top, left))
    return fill(grid, color_value, x1)


def generate_358ba94e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(interval(ONE, 10, ONE))
        x1 = unifint(diff_lb, diff_ub, HEIGHT_BOUNDS_358BA94E)
        x2 = unifint(diff_lb, diff_ub, WIDTH_BOUNDS_358BA94E)
        x3 = choice(OBJECT_COUNT_OPTIONS_358BA94E)

        x4 = _start_options_358ba94e(x1, TWO)
        x5 = _start_options_358ba94e(x1, THREE)
        x6 = _start_options_358ba94e(x2, TWO)
        x7 = _start_options_358ba94e(x2, THREE)

        x8 = []
        for x9 in (x4, x5):
            if len(x9) == ZERO:
                continue
            for x10 in (x6, x7):
                if len(x10) == ZERO:
                    continue
                if len(first(x9)) * len(first(x10)) >= x3:
                    x8.append((x9, x10))
        if len(x8) == ZERO:
            continue

        x11 = choice(COMMON_HOLE_COUNT_OPTIONS_358BA94E)
        x12 = tuple(x13 for x13 in (x11 - ONE, x11 + ONE) if ONE <= x13 <= FOUR)
        x13 = choice(x12)
        x14 = HOLE_PATTERNS_358BA94E[x11]
        x15 = HOLE_PATTERNS_358BA94E[x13]

        x16, x17 = choice(x8)
        x18 = choice(x16)
        x19 = choice(x17)
        x20 = sample(tuple(product(x18, x19)), x3)
        x21 = randint(ZERO, x3 - ONE)
        x22 = choice(x15)
        if choice((T, F)):
            x23 = list(sample(x14, x3 - ONE))
        else:
            x23 = [choice(x14) for _ in range(x3 - ONE)]

        x24 = canvas(ZERO, (x1, x2))
        for x25, x26 in enumerate(x20):
            x27 = x22 if x25 == x21 else x23.pop()
            x24 = _paint_block_358ba94e(x24, x0, x26[ZERO], x26[ONE], x27)
        x28 = _render_pattern_358ba94e(x0, x22)
        return {"input": x24, "output": x28}
