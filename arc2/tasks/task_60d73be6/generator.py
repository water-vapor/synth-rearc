from arc2.core import *


PATTERN_COLORS_60D73BE6 = tuple(x0 for x0 in interval(ZERO, TEN, ONE) if x0 != SEVEN)


def _reflect_vertical_60d73be6(
    obj: Object,
    axis_col: Integer,
) -> Object:
    x0 = add(leftmost(obj), rightmost(obj))
    x1 = subtract(double(axis_col), x0)
    x2 = vmirror(obj)
    x3 = shift(x2, tojvec(x1))
    return x3


def _reflect_horizontal_60d73be6(
    obj: Object,
    axis_row: Integer,
) -> Object:
    x0 = add(uppermost(obj), lowermost(obj))
    x1 = subtract(double(axis_row), x0)
    x2 = hmirror(obj)
    x3 = shift(x2, toivec(x1))
    return x3


def _cross_grid_60d73be6(
    dims: IntegerTuple,
    axis_color: Integer,
    axis_row: Integer,
    axis_col: Integer,
) -> Grid:
    x0 = canvas(SEVEN, dims)
    x1 = fill(x0, axis_color, hfrontier((axis_row, axis_col)))
    x2 = fill(x1, axis_color, vfrontier((axis_row, axis_col)))
    return x2


def _source_region_60d73be6(
    top: Integer,
    left: Integer,
    right: Integer,
    source_on_left: Boolean,
) -> frozenset[IntegerTuple]:
    x0 = interval(ZERO, top, ONE)
    if source_on_left:
        x1 = interval(ZERO, left, ONE)
    else:
        x1 = interval(increment(left), add(left, increment(right)), ONE)
    return product(x0, x1)


def _seed_cells_60d73be6(
    top: Integer,
    left: Integer,
    right: Integer,
    source_on_left: Boolean,
) -> frozenset[IntegerTuple]:
    if source_on_left:
        x0 = interval(ZERO, left, ONE)
        x1 = ZERO
        x2 = decrement(left)
    else:
        x0 = interval(increment(left), add(left, increment(right)), ONE)
        x1 = add(left, right)
        x2 = increment(left)
    x3 = {
        (ZERO, choice(x0)),
        (randint(ZERO, decrement(top)), x1),
        (randint(ZERO, decrement(top)), x2),
    }
    if choice((T, F)):
        x3.add((decrement(top), choice(x0)))
    return frozenset(x3)


def _grow_source_cells_60d73be6(
    region: frozenset[IntegerTuple],
    seeds: frozenset[IntegerTuple],
    target: Integer,
) -> frozenset[IntegerTuple]:
    x0 = set(seeds)
    x1 = set(region)
    x2 = ZERO
    while len(x0) < target and x2 < 800:
        x2 += ONE
        x3 = {
            x4
            for x5 in x0
            for x4 in dneighbors(x5)
            if x4 in x1 and x4 not in x0
        }
        if len(x3) > ZERO and choice((T, T, F)):
            x6 = choice(tuple(x3))
        else:
            x7 = tuple(x1 - x0)
            if len(x7) == ZERO:
                break
            x6 = choice(x7)
        x0.add(x6)
    return frozenset(x0)


def _well_spread_60d73be6(
    cells: frozenset[IntegerTuple],
    top: Integer,
    left: Integer,
    right: Integer,
    source_on_left: Boolean,
) -> Boolean:
    x0 = frozenset(x1 for x1, _ in cells)
    x2 = frozenset(x3 for _, x3 in cells)
    x4 = left if source_on_left else right
    x5 = ZERO if source_on_left else add(left, right)
    x6 = decrement(left) if source_on_left else increment(left)
    x7 = len(x0) >= min(THREE, top)
    x8 = len(x2) >= min(THREE, x4)
    x9 = any(x10 == ZERO for x10, _ in cells)
    x11 = any(x12 == x5 for _, x12 in cells)
    x13 = any(x14 == x6 for _, x14 in cells)
    return x7 and x8 and x9 and x11 and x13


def _color_source_60d73be6(
    cells: frozenset[IntegerTuple],
    axis_color: Integer,
) -> Object:
    x0 = tuple(x1 for x1 in PATTERN_COLORS_60D73BE6 if x1 != axis_color)
    x2 = len(cells)
    x3 = min(x2, choice((FOUR, FIVE, FIVE, SIX, SIX, SEVEN)))
    x4 = list(sample(x0, x3))
    while len(x4) < x2:
        x4.append(choice(x4))
    shuffle(x4)
    x5 = tuple(sorted(cells))
    return frozenset((x6, x7) for x6, x7 in zip(x4, x5))


def generate_60d73be6(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (FOUR, SIX))
        x1 = unifint(diff_lb, diff_ub, (THREE, SIX))
        x2 = choice((T, F))
        if x2:
            x3 = unifint(diff_lb, diff_ub, (FOUR, EIGHT))
            x4 = unifint(diff_lb, diff_ub, (THREE, TEN))
        else:
            x3 = unifint(diff_lb, diff_ub, (THREE, TEN))
            x4 = unifint(diff_lb, diff_ub, (FOUR, EIGHT))
        x5 = add(add(x0, x1), ONE)
        x6 = add(add(x3, x4), ONE)
        x7 = x0
        x8 = x3
        x9 = choice(tuple(x10 for x10 in PATTERN_COLORS_60D73BE6 if x10 != ZERO))
        x11 = _source_region_60d73be6(x0, x3, x4, x2)
        x12 = len(x11)
        x13 = max(SIX, divide(x12, FIVE))
        x14 = min(12, max(add(x13, ONE), divide(add(x12, ONE), THREE)))
        x15 = unifint(diff_lb, diff_ub, (x13, x14))
        x16 = _seed_cells_60d73be6(x0, x3, x4, x2)
        x17 = _grow_source_cells_60d73be6(x11, x16, x15)
        if len(x17) != x15:
            continue
        if not _well_spread_60d73be6(x17, x0, x3, x4, x2):
            continue
        x18 = _color_source_60d73be6(x17, x9)
        x19 = _cross_grid_60d73be6((x5, x6), x9, x7, x8)
        x20 = paint(x19, x18)
        x21 = _reflect_vertical_60d73be6(x18, x8)
        x22 = _reflect_horizontal_60d73be6(x18, x7)
        x23 = _reflect_horizontal_60d73be6(x21, x7)
        x24 = combine(x18, x21)
        x25 = combine(x22, x23)
        x26 = combine(x24, x25)
        x27 = paint(x19, x26)
        if x20 == x27:
            continue
        return {
            "input": x20,
            "output": x27,
        }
