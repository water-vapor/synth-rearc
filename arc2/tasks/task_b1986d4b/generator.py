from arc2.core import *


GRID_HEIGHT_BOUNDS_B1986D4B = (26, 28)
GRID_WIDTH_BOUNDS_B1986D4B = (25, 28)
SMALL_COUNT_BOUNDS_B1986D4B = (THREE, FIVE)
MEDIUM_COUNT_BOUNDS_B1986D4B = (TWO, SIX)
LARGE_COUNT_BOUNDS_B1986D4B = (TWO, SIX)
NOISE_FRAGMENT_COUNT_B1986D4B = (24, 56)
MAX_PLACEMENT_ATTEMPTS_B1986D4B = 512


def _square_patch_b1986d4b(
    top: Integer,
    left: Integer,
    side: Integer,
) -> Indices:
    return product(interval(top, top + side, ONE), interval(left, left + side, ONE))


def _moat_patch_b1986d4b(
    top: Integer,
    left: Integer,
    side: Integer,
) -> Indices:
    return product(
        interval(top - ONE, top + side + ONE, ONE),
        interval(left - ONE, left + side + ONE, ONE),
    )


def _paint_square_b1986d4b(
    grid: Grid,
    top: Integer,
    left: Integer,
    side: Integer,
    value: Integer,
) -> Grid:
    return fill(grid, value, _square_patch_b1986d4b(top, left, side))


def _render_output_b1986d4b(
    bg: Integer,
    small_color: Integer,
    small_count: Integer,
    medium_color: Integer,
    medium_count: Integer,
    large_color: Integer,
    large_count: Integer,
) -> Grid:
    x0 = maximum((small_count, medium_count, large_count))
    x1 = canvas(bg, (FIVE, ONE))
    x2 = []
    x3 = interval(ZERO, TWO, ONE)
    x4 = interval(ZERO, THREE, ONE)
    x5 = interval(ZERO, FOUR, ONE)
    for x6 in interval(ZERO, x0, ONE):
        x7 = ZERO
        if small_count > x6:
            x7 = TWO
        if medium_count > x6:
            x7 = THREE
        if large_count > x6:
            x7 = FOUR
        x8 = canvas(bg, (FIVE, x7))
        if large_count > x6:
            x8 = fill(x8, large_color, product(x5, x5))
        if medium_count > x6:
            x8 = fill(x8, medium_color, product(x4, x4))
        if small_count > x6:
            x8 = fill(x8, small_color, product(x3, x3))
        x2.append(hconcat(x8, x1))
    x9 = x2[ZERO]
    for x10 in x2[ONE:]:
        x9 = hconcat(x9, x10)
    return x9


def _sample_colors_b1986d4b(
    bg: Integer,
) -> Tuple:
    x0 = remove(bg, interval(ONE, TEN, ONE))
    if bg == ONE:
        x1 = choice((TWO, THREE, SIX, SEVEN))
        x2 = remove(EIGHT, remove(x1, x0))
        x3 = choice(x2)
        x4 = choice(remove(x3, x2))
        return (x1, x3, x4, (EIGHT,))
    x1 = EIGHT
    x2 = remove(ONE, remove(x1, x0))
    x3 = choice(x2)
    x4 = choice(remove(x3, x2))
    return (x1, x3, x4, (ONE,))


def _sample_counts_b1986d4b(
    diff_lb: float,
    diff_ub: float,
    bg: Integer,
) -> Tuple:
    while True:
        x0 = unifint(diff_lb, diff_ub, SMALL_COUNT_BOUNDS_B1986D4B)
        x1 = unifint(diff_lb, diff_ub, MEDIUM_COUNT_BOUNDS_B1986D4B)
        x2 = unifint(diff_lb, diff_ub, LARGE_COUNT_BOUNDS_B1986D4B)
        x3 = ZERO
        if bg == ONE and x0 >= x1 and choice((F, T)):
            x3 = ONE
        x4 = _render_output_b1986d4b(ONE, TWO, x0, THREE, x1, FOUR, x2)
        x5 = width(x4)
        if 14 <= x5 <= 30:
            return (x0, x1, x2, x3)


def _place_object_b1986d4b(
    forbidden: Indices,
    grid_shape: Tuple,
    side: Integer,
    row_bounds: Tuple,
) -> Tuple:
    x0, x1 = grid_shape
    x2, x3 = row_bounds
    x4 = max(ZERO, x2)
    x5 = min(x0 - side, x3)
    if x4 > x5:
        return None
    for _ in range(MAX_PLACEMENT_ATTEMPTS_B1986D4B):
        x6 = randint(x4, x5)
        x7 = randint(ZERO, x1 - side)
        x8 = _moat_patch_b1986d4b(x6, x7, side)
        x9 = frozenset((i, j) for i, j in x8 if 0 <= i < x0 and 0 <= j < x1)
        if len(intersection(forbidden, x9)) != ZERO:
            continue
        return (x6, x7, _square_patch_b1986d4b(x6, x7, side), x9)
    return None


def _place_fragments_b1986d4b(
    grid: Grid,
    forbidden: Indices,
    noise_colors: Tuple,
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    x0 = height(grid)
    x1 = width(grid)
    x2 = unifint(diff_lb, diff_ub, NOISE_FRAGMENT_COUNT_B1986D4B)
    x3 = grid
    x4 = forbidden
    x5 = ZERO
    x6 = ZERO
    while x5 < x2 and x6 < x2 * TEN:
        x6 += ONE
        x7 = choice((ONE, ONE, ONE, TWO))
        x8 = choice((RIGHT, DOWN))
        x9 = randint(ZERO, x0 - ONE)
        x10 = randint(ZERO, x1 - ONE)
        x11 = connect((x9, x10), add((x9, x10), multiply(x8, decrement(x7))))
        if len(x11) != x7:
            continue
        x12 = _moat_patch_b1986d4b(uppermost(x11), leftmost(x11), max(height(x11), width(x11)))
        x13 = frozenset((i, j) for i, j in x12 if 0 <= i < x0 and 0 <= j < x1)
        if len(intersection(x4, x13)) != ZERO:
            continue
        x14 = choice(noise_colors)
        x3 = fill(x3, x14, x11)
        x4 = combine(x4, x13)
        x5 += ONE
    return x3


def generate_b1986d4b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((ONE, ONE, FOUR))
        x1 = _sample_colors_b1986d4b(x0)
        x2, x3, x4, x5 = _sample_counts_b1986d4b(diff_lb, diff_ub, x0)
        x6 = unifint(diff_lb, diff_ub, GRID_HEIGHT_BOUNDS_B1986D4B)
        x7 = unifint(diff_lb, diff_ub, GRID_WIDTH_BOUNDS_B1986D4B)
        x8 = canvas(x0, (x6, x7))
        x9 = frozenset()
        x10 = randint(EIGHT, x6 - FOUR - x5)
        x11 = _place_object_b1986d4b(x9, (x6, x7), THREE, (x10, x10))
        if x11 is None:
            continue
        x12, x13, _, x14 = x11
        x8 = _paint_square_b1986d4b(x8, x12, x13, THREE, x1[ONE])
        x9 = combine(x9, x14)
        x15 = ONE
        while x15 < x3:
            x16 = _place_object_b1986d4b(x9, (x6, x7), THREE, (ZERO, x10))
            if x16 is None:
                break
            x17, x18, _, x19 = x16
            x8 = _paint_square_b1986d4b(x8, x17, x18, THREE, x1[ONE])
            x9 = combine(x9, x19)
            x15 += ONE
        if x15 != x3:
            continue
        x20 = ZERO
        while x20 < x4:
            x21 = _place_object_b1986d4b(x9, (x6, x7), FOUR, (ZERO, x6 - FOUR))
            if x21 is None:
                break
            x22, x23, _, x24 = x21
            x8 = _paint_square_b1986d4b(x8, x22, x23, FOUR, x1[TWO])
            x9 = combine(x9, x24)
            x20 += ONE
        if x20 != x4:
            continue
        x25 = ZERO
        while x25 < x2:
            x26 = _place_object_b1986d4b(x9, (x6, x7), TWO, (ZERO, x10))
            if x26 is None:
                break
            x27, x28, _, x29 = x26
            x8 = _paint_square_b1986d4b(x8, x27, x28, TWO, x1[ZERO])
            x9 = combine(x9, x29)
            x25 += ONE
        if x25 != x2:
            continue
        x30 = ZERO
        while x30 < x5:
            x31 = _place_object_b1986d4b(x9, (x6, x7), TWO, (x10 + ONE, x6 - TWO))
            if x31 is None:
                break
            x32, x33, _, x34 = x31
            x8 = _paint_square_b1986d4b(x8, x32, x33, TWO, x1[ZERO])
            x9 = combine(x9, x34)
            x30 += ONE
        if x30 != x5:
            continue
        x35 = _place_fragments_b1986d4b(x8, x9, x1[THREE], diff_lb, diff_ub)
        x36 = _render_output_b1986d4b(x0, x1[ZERO], x2, x1[ONE], x3, x1[TWO], x4)
        if x35 == x36:
            continue
        return {"input": x35, "output": x36}
