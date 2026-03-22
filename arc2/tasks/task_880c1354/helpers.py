from arc2.core import *


# Ordered from simpler two-region layouts to denser four-region layouts.
SCAFFOLD_SPECS_880C1354 = (
    ((3, 2, 1, 2, 3, 4, 5, 6), (5, 5, 5, 5, 5, 5, 5, 5), ZERO, FIVE, False, True),
    ((3, 2, 1, 2, 3, 4, 5, 6), (6, 6, 6, 6, 6, 6, 6, 6), ZERO, FIVE, False, True),
    ((NEG_ONE, NEG_ONE, ZERO, ZERO, ZERO, ZERO, ZERO, ZERO), (EIGHT, EIGHT, EIGHT, SEVEN, FIVE, TWO, ONE, ZERO), THREE, FIVE, True, True),
    ((NEG_ONE, NEG_ONE, ZERO, ZERO, ZERO, ZERO, ZERO, ZERO), (EIGHT, EIGHT, EIGHT, SEVEN, SIX, THREE, TWO, ONE), THREE, FIVE, True, True),
    ((TWO, ONE, ZERO, ONE, TWO, THREE, FOUR, FIVE), (FIVE, FIVE, FIVE, FIVE, FIVE, FIVE, FIVE, FIVE), ZERO, FIVE, False, True),
    ((TWO, ONE, ZERO, ONE, TWO, THREE, FOUR, FIVE), (SIX, SIX, SIX, SIX, SIX, SIX, SIX, SIX), ZERO, FIVE, False, True),
    ((TWO, TWO, ONE, ZERO, NEG_ONE, THREE, FOUR, FOUR), (EIGHT, FIVE, FIVE, FIVE, FIVE, FIVE, EIGHT, EIGHT), ONE, FIVE, True, True),
    ((THREE, THREE, TWO, ONE, NEG_ONE, THREE, FOUR, FOUR), (EIGHT, FIVE, FIVE, FIVE, FIVE, FIVE, EIGHT, EIGHT), ONE, FIVE, True, True),
    ((TWO, ONE, ZERO, NEG_ONE, ZERO, ONE, TWO, THREE), (FIVE, SIX, SEVEN, SEVEN, FOUR, FOUR, FOUR, FOUR), ZERO, SIX, False, True),
    ((TWO, ONE, ZERO, NEG_ONE, ZERO, ONE, TWO, THREE), (FIVE, SIX, SEVEN, SEVEN, THREE, THREE, THREE, THREE), ZERO, SIX, False, True),
    ((THREE, TWO, ONE, ZERO, ONE, TWO, THREE, FOUR), (FIVE, SIX, SEVEN, SEVEN, FOUR, FOUR, FOUR, FOUR), ZERO, SIX, False, True),
)


def row_interval_880c1354(
    row: Integer,
    left: Integer,
    right: Integer,
) -> Indices:
    x0 = max(ZERO, left)
    x1 = min(SEVEN, right)
    if x0 > x1:
        return frozenset()
    return frozenset((row, x2) for x2 in range(x0, x1 + ONE))


def transition_strip_880c1354(
    previous: Integer,
    current: Integer,
    row: Integer,
    is_left: Boolean,
) -> Indices:
    if current < ZERO or current > SEVEN:
        return frozenset()
    if row == ZERO:
        return frozenset({(row, current)})
    if is_left and previous < ZERO:
        return row_interval_880c1354(row, ZERO, current)
    if previous > SEVEN:
        return frozenset({(row, current)})
    if previous < ZERO:
        return frozenset({(row, current)})
    if current > previous:
        return row_interval_880c1354(row, previous + ONE, current)
    if current < previous:
        return row_interval_880c1354(row, current, previous - ONE)
    return frozenset({(row, current)})


def build_scaffold_880c1354(
    spec: tuple[tuple[Integer, ...], tuple[Integer, ...], Integer, Integer, Boolean, Boolean],
) -> Grid:
    x0, x1, x2, x3, x4, x5 = spec
    x6 = canvas(ZERO, (EIGHT, EIGHT))
    for x7 in range(x2, x3 + ONE):
        x8 = row_interval_880c1354(x7, x0[x7] + ONE, x1[x7] - ONE)
        x6 = fill(x6, FOUR, x8)
    for x7 in range(EIGHT):
        x8 = branch(x7 == ZERO, NEG_ONE, x0[x7 - ONE])
        x9 = branch(x7 == ZERO, EIGHT, x1[x7 - ONE])
        x10 = transition_strip_880c1354(x8, x0[x7], x7, True)
        x11 = transition_strip_880c1354(x9, x1[x7], x7, False)
        x6 = fill(x6, SEVEN, combine(x10, x11))
    if x4 and x2 > ZERO:
        x12 = row_interval_880c1354(x2 - ONE, x0[x2] + ONE, x1[x2] - ONE)
        x6 = fill(x6, SEVEN, x12)
    if x5 and x3 < SEVEN:
        x13 = row_interval_880c1354(x3 + ONE, x0[x3] + ONE, x1[x3] - ONE)
        x6 = fill(x6, SEVEN, x13)
    return x6


def clockwise_border_880c1354(
    dims: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    x0, x1 = dims
    x2 = tuple((ZERO, x3) for x3 in range(x1))
    x3 = tuple((x4, x1 - ONE) for x4 in range(ONE, x0))
    x4 = tuple((x0 - ONE, x5) for x5 in range(x1 - TWO, NEG_ONE, NEG_ONE))
    x5 = tuple((x6, ZERO) for x6 in range(x0 - TWO, ZERO, NEG_ONE))
    return x2 + x3 + x4 + x5


def border_rank_880c1354(
    patch: Patch,
    dims: IntegerTuple = (EIGHT, EIGHT),
) -> Integer:
    x0 = {
        x1: x2
        for x2, x1 in enumerate(clockwise_border_880c1354(dims))
    }
    return min(x0[x3] for x3 in toindices(patch) if x3 in x0)


def ordered_outer_objects_880c1354(
    grid: Grid,
) -> tuple[Object, ...]:
    x0 = objects(grid, T, F, F)
    x1 = frozenset(
        x2
        for x2 in x0
        if color(x2) not in (FOUR, SEVEN)
    )
    return order(x1, lambda x3: border_rank_880c1354(x3, shape(grid)))


def paint_regions_880c1354(
    grid: Grid,
    regions: tuple[Object, ...],
    colors: tuple[Integer, ...],
) -> Grid:
    x0 = grid
    for x1, x2 in zip(colors, regions):
        x0 = paint(x0, recolor(x1, x2))
    return x0
