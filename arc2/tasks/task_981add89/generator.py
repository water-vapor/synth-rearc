from arc2.core import *


ALL_COLORS_981ADD89 = interval(ZERO, TEN, ONE)


def _rect_patch_981add89(
    top: Integer,
    left: Integer,
    height_: Integer,
    width_: Integer,
) -> Indices:
    x0 = interval(top, add(top, height_), ONE)
    x1 = interval(left, add(left, width_), ONE)
    return product(x0, x1)


def _anchored_start_981add89(
    limit: Integer,
    span: Integer,
    floor: Integer,
) -> Integer:
    x0 = subtract(limit, span)
    if x0 <= floor:
        return floor
    x1 = randint(floor, x0)
    return choice((floor, x1, x0))


def _marker_columns_981add89(
    width_: Integer,
    count_: Integer,
) -> tuple[int, ...]:
    x0 = interval(ZERO, width_, ONE)
    while True:
        x1 = tuple(sorted(sample(x0, count_)))
        if all(b - a > ONE for a, b in zip(x1, x1[1:])):
            return x1


def _apply_markers_981add89(
    grid: Grid,
) -> Grid:
    x0 = width(grid)
    x1 = astuple(ONE, x0)
    x2 = crop(grid, ORIGIN, x1)
    x3 = decrement(height(grid))
    x4 = astuple(x3, x0)
    x5 = crop(grid, DOWN, x4)
    x6 = mostcolor(grid)
    x7 = difference(asindices(x2), ofcolor(x2, x6))
    x8 = x5
    for x9 in x7:
        x10 = index(x2, x9)
        x11 = product(interval(ZERO, x3, ONE), initset(last(x9)))
        x12 = intersection(x11, ofcolor(x8, x10))
        x13 = fill(x8, x10, x11)
        x8 = fill(x13, x6, x12)
    return vconcat(x2, x8)


def generate_981add89(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((T, F, F))
        x1 = (18, 24) if x0 else (24, 30)
        x2 = unifint(diff_lb, diff_ub, x1)
        x3 = choice(ALL_COLORS_981ADD89)
        x4 = tuple(remove(x3, ALL_COLORS_981ADD89))
        x5 = unifint(diff_lb, diff_ub, (ONE, TWO)) if x0 else unifint(diff_lb, diff_ub, (FOUR, SIX))
        x6 = ONE if x5 == ONE else randint(TWO, min(FIVE, x5)) if x0 else randint(THREE, min(FIVE, x5))
        x7 = list(sample(x4, x6))
        while len(x7) < x5:
            x7.append(choice(x7))
        shuffle(x7)
        x8 = canvas(x3, (x2, x2))
        x9 = max(FOUR, x2 // SIX) if x0 else max(FIVE, x2 // FIVE)
        x10 = max(x9, min(x2 - ONE, (double(x2) // THREE) + (x2 // THREE) + ONE))
        for x11 in x7:
            x12 = unifint(diff_lb, diff_ub, (x9, x10))
            x13 = unifint(diff_lb, diff_ub, (x9, x10))
            x14 = _anchored_start_981add89(x2, x12, ONE)
            x15 = _anchored_start_981add89(x2, x13, ZERO)
            x16 = _rect_patch_981add89(x14, x15, x12, x13)
            x8 = fill(x8, x11, x16)
        x17 = crop(x8, DOWN, astuple(decrement(x2), x2))
        x18 = tuple(sorted(remove(x3, palette(x17))))
        if len(x18) == ZERO:
            continue
        if not x0 and len(x18) < THREE:
            continue
        x19 = (x2 - ONE) * x2
        x20 = x19 - colorcount(x17, x3)
        x21 = x19 // SIX if x0 else x19 // FIVE
        x22 = x19 // TWO if x0 else (x19 * 2) // 3
        if x20 < x21:
            continue
        if x20 > x22:
            continue
        x23 = randint(TWO, THREE) if x0 else randint(FOUR, min(SIX, len(x18) + TWO))
        x24 = [choice(x18) for _ in range(x23)]
        x25 = tuple(c for c in x4 if c not in x18)
        x26 = choice((T, F)) if x0 else choice((T, F, F))
        if len(x25) > ZERO and x26:
            x24[randint(ZERO, x23 - ONE)] = choice(x25)
        x27 = _marker_columns_981add89(x2, x23)
        for x28, x29 in zip(x27, x24):
            x30 = frozenset({(ZERO, x28)})
            x8 = fill(x8, x29, x30)
        if mostcolor(x8) != x3:
            continue
        x31 = _apply_markers_981add89(x8)
        if mostcolor(x31) != x3:
            continue
        return {"input": x8, "output": x31}
