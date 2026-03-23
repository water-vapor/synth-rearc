from arc2.core import *


Square22806E14 = tuple[Integer, Integer, Integer]

GRID_DIMS_22806E14 = (16, 16)
BACKGROUND_22806E14 = SEVEN
ACTIVE_COLORS_22806E14 = (ONE, TWO, THREE, FOUR, FIVE, SIX, EIGHT, NINE)
ODD_COUNT_BAG_22806E14 = (TWO, THREE, THREE, FOUR, FOUR, FIVE, FIVE, SIX, SEVEN, EIGHT)
EVEN_COUNT_BAG_22806E14 = (ZERO, ONE, ONE, TWO, TWO, THREE, FOUR)
ODD_SIDE_BAG_22806E14 = (ONE, ONE, ONE, THREE, THREE, THREE, FIVE, FIVE, SEVEN)
EVEN_SIDE_BAG_22806E14 = (TWO, TWO, TWO, FOUR, FOUR, SIX)
MAX_SQUARE_AREA_22806E14 = 125


def _square_patch_22806e14(
    top: Integer,
    left: Integer,
    side: Integer,
) -> Indices:
    return frozenset(
        (i, j)
        for i in range(top, top + side)
        for j in range(left, left + side)
    )


def _reserve_patch_22806e14(
    dims: IntegerTuple,
    top: Integer,
    left: Integer,
    side: Integer,
) -> Indices:
    x0, x1 = dims
    return frozenset(
        (i, j)
        for i in range(max(ZERO, top - ONE), min(x0 - ONE, top + side) + ONE)
        for j in range(max(ZERO, left - ONE), min(x1 - ONE, left + side) + ONE)
    )


def _plus_patch_22806e14(
    top: Integer,
    left: Integer,
) -> Indices:
    return frozenset(
        {
            (top, left + ONE),
            (top + ONE, left),
            (top + ONE, left + ONE),
            (top + ONE, left + TWO),
            (top + TWO, left + ONE),
        }
    )


def _sample_sides_22806e14(
    odd_count: Integer,
    even_count: Integer,
) -> tuple[Integer, ...]:
    x0 = [choice(ODD_SIDE_BAG_22806E14) for _ in range(odd_count)]
    x1 = [choice(EVEN_SIDE_BAG_22806E14) for _ in range(even_count)]
    if odd_count > ZERO and max(x0) == ONE:
        x0[randint(ZERO, odd_count - ONE)] = choice((THREE, FIVE, SEVEN))
    if even_count > ONE and max(x1) == TWO:
        x1[randint(ZERO, even_count - ONE)] = choice((FOUR, SIX))
    x2 = tuple(sorted(x0 + x1, reverse=T))
    return x2


def _sample_squares_22806e14(
    dims: IntegerTuple,
    sides: tuple[Integer, ...],
) -> tuple[tuple[Square22806E14, ...], Indices] | None:
    x0, x1 = dims
    x2 = set()
    x3 = []
    for x4 in sides:
        x5 = F
        for _ in range(400):
            x6 = randint(ZERO, x0 - x4)
            x7 = randint(ZERO, x1 - x4)
            x8 = _square_patch_22806e14(x6, x7, x4)
            if len(intersection(x8, x2)) > ZERO:
                continue
            x9 = _reserve_patch_22806e14(dims, x6, x7, x4)
            x3.append((x6, x7, x4))
            x2 |= x9
            x5 = T
            break
        if not x5:
            return None
    return tuple(x3), frozenset(x2)


def _sample_plus_loc_22806e14(
    dims: IntegerTuple,
    blocked: Indices,
) -> tuple[Integer, Integer] | None:
    x0, x1 = dims
    for _ in range(400):
        x2 = randint(ZERO, x0 - THREE)
        x3 = randint(ZERO, x1 - THREE)
        x4 = _plus_patch_22806e14(x2, x3)
        if len(intersection(x4, blocked)) > ZERO:
            continue
        return (x2, x3)
    return None


def _paint_input_22806e14(
    dims: IntegerTuple,
    square_color: Integer,
    template_color: Integer,
    squares: tuple[Square22806E14, ...],
    plus_loc: tuple[Integer, Integer],
) -> Grid:
    x0 = canvas(BACKGROUND_22806E14, dims)
    for x1, x2, x3 in squares:
        x4 = _square_patch_22806e14(x1, x2, x3)
        x0 = fill(x0, square_color, x4)
    x5, x6 = plus_loc
    x7 = _plus_patch_22806e14(x5, x6)
    x8 = fill(x0, template_color, x7)
    return x8


def _paint_output_22806e14(
    input_grid: Grid,
    template_color: Integer,
    squares: tuple[Square22806E14, ...],
    plus_loc: tuple[Integer, Integer],
) -> Grid:
    x0 = tuple((x1 + x3 // TWO, x2 + x3 // TWO) for x1, x2, x3 in squares if not even(x3))
    x1, x2 = plus_loc
    x3 = _plus_patch_22806e14(x1, x2)
    x4 = input_grid if len(x0) >= FIVE else fill(input_grid, BACKGROUND_22806E14, x3)
    x5 = fill(x4, template_color, frozenset(x0))
    return x5


def generate_22806e14(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(ACTIVE_COLORS_22806E14)
        x1 = choice(tuple(x2 for x2 in ACTIVE_COLORS_22806E14 if x2 != x0))
        x2 = choice(ODD_COUNT_BAG_22806E14)
        x3 = choice(EVEN_COUNT_BAG_22806E14)
        if x2 + x3 < FIVE:
            continue
        x4 = _sample_sides_22806e14(x2, x3)
        if sum(x5 * x5 for x5 in x4) > MAX_SQUARE_AREA_22806E14:
            continue
        x5 = _sample_squares_22806e14(GRID_DIMS_22806E14, x4)
        if x5 is None:
            continue
        x6, x7 = x5
        x8 = _sample_plus_loc_22806e14(GRID_DIMS_22806E14, x7)
        if x8 is None:
            continue
        x9 = _paint_input_22806e14(GRID_DIMS_22806E14, x0, x1, x6, x8)
        x10 = _paint_output_22806e14(x9, x1, x6, x8)
        if x9 == x10:
            continue
        return {"input": x9, "output": x10}
