from synth_rearc.core import *


GRID_SHAPE_54DB823B = (15, 15)
RECT_DIMS_54DB823B = (
    (TWO, THREE),
    (TWO, THREE),
    (THREE, FIVE),
    (THREE, FIVE),
    (THREE, FIVE),
    (FOUR, FOUR),
    (FOUR, FOUR),
    (FOUR, FIVE),
    (FOUR, FIVE),
    (FIVE, TWO),
    (FIVE, THREE),
    (FIVE, THREE),
    (FIVE, FOUR),
    (FIVE, FOUR),
    (FIVE, FIVE),
    (FIVE, FIVE),
    (FIVE, SEVEN),
    (FIVE, SEVEN),
    (SIX, THREE),
    (SIX, SEVEN),
    (SEVEN, FOUR),
)


def _rectangle_patch_54db823b(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    x0 = interval(top, top + height_value, ONE)
    x1 = interval(left, left + width_value, ONE)
    return product(x0, x1)


def _blocked_patch_54db823b(
    patch: Indices,
) -> Indices:
    x0 = combine(patch, shift(patch, (-ONE, ZERO)))
    x1 = combine(x0, shift(patch, (ONE, ZERO)))
    x2 = combine(x1, shift(patch, (ZERO, -ONE)))
    x3 = combine(x2, shift(patch, (ZERO, ONE)))
    return x3


def _sample_dimensions_54db823b(
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[Integer, Integer], ...]:
    x0 = unifint(diff_lb, diff_ub, (FOUR, SIX))
    return tuple(choice(RECT_DIMS_54DB823B) for _ in range(x0))


def _max_nines_54db823b(
    dims: tuple[Integer, Integer],
) -> Integer:
    x0 = dims[ZERO] * dims[ONE]
    x1 = max(TWO, increment(x0 // FIVE))
    return min(SEVEN, x1)


def _choose_nine_counts_54db823b(
    dims: tuple[tuple[Integer, Integer], ...],
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, tuple[Integer, ...]] | None:
    x0 = tuple(_max_nines_54db823b(x1) for x1 in dims)
    x1 = []
    for x2, x3 in enumerate(x0):
        x4 = tuple(x5 for x6, x5 in enumerate(x0) if x6 != x2)
        x5 = min(x3, THREE, decrement(min(x4)))
        if x5 >= ONE:
            x1.append((x2, x5))
    if len(x1) == ZERO:
        return None
    x2, x3 = choice(x1)
    x4 = unifint(diff_lb, diff_ub, (ONE, x3))
    x5 = []
    for x6, x7 in enumerate(x0):
        if x6 == x2:
            x5.append(x4)
            continue
        x8 = increment(x4)
        x9 = unifint(diff_lb, diff_ub, (x8, x7))
        x5.append(x9)
    return x2, tuple(x5)


def _place_rectangles_54db823b(
    dims: tuple[tuple[Integer, Integer], ...],
) -> tuple[tuple[Integer, Integer, Integer, Integer, Indices], ...] | None:
    x0 = tuple(sorted(enumerate(dims), key=lambda x1: x1[1][ZERO] * x1[1][ONE], reverse=True))
    x1 = [None] * len(dims)
    x2 = frozenset()
    x3, x4 = GRID_SHAPE_54DB823B
    for x5, (x6, x7) in x0:
        x8 = F
        for _ in range(400):
            x9 = randint(ZERO, x3 - x6)
            x10 = randint(ZERO, x4 - x7)
            x11 = _rectangle_patch_54db823b(x9, x10, x6, x7)
            if len(intersection(x11, x2)) > ZERO:
                continue
            x1[x5] = (x9, x10, x6, x7, x11)
            x2 = combine(x2, _blocked_patch_54db823b(x11))
            x8 = T
            break
        if not x8:
            return None
    return tuple(x1)


def _paint_rectangle_54db823b(
    grid: Grid,
    patch: Indices,
    nine_count: Integer,
) -> Grid:
    x0 = fill(grid, THREE, patch)
    x1 = sample(totuple(patch), nine_count)
    x2 = fill(x0, NINE, x1)
    return x2


def _nonzero_objects_54db823b(
    grid: Grid,
) -> Objects:
    x0 = asindices(grid)
    x1 = ofcolor(grid, ZERO)
    x2 = difference(x0, x1)
    x3 = canvas(ZERO, shape(grid))
    x4 = fill(x3, ONE, x2)
    x5 = objects(x4, T, F, F)
    x6 = colorfilter(x5, ONE)
    return x6


def generate_54db823b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    for _ in range(400):
        x0 = _sample_dimensions_54db823b(diff_lb, diff_ub)
        x1 = tuple(x2 * x3 for x2, x3 in x0)
        x2 = sum(x1)
        if x2 < 75 or x2 > 130:
            continue
        if len(set(x0)) == ONE and choice((T, T, F)):
            continue
        x3 = _choose_nine_counts_54db823b(x0, diff_lb, diff_ub)
        if x3 is None:
            continue
        x4, x5 = x3
        x6 = _place_rectangles_54db823b(x0)
        if x6 is None:
            continue
        x7 = canvas(ZERO, GRID_SHAPE_54DB823B)
        for x8, x9 in zip(x6, x5):
            x7 = _paint_rectangle_54db823b(x7, x8[-ONE], x9)
        x10 = _nonzero_objects_54db823b(x7)
        if size(x10) != len(x0):
            continue
        x11 = tuple(colorcount(toobject(x12, x7), NINE) for x12 in x10)
        x12 = min(x5)
        if x11.count(x12) != ONE:
            continue
        x13 = toobject(x6[x4][-ONE], x7)
        x14 = argmin(x10, compose(rbind(colorcount, NINE), rbind(toobject, x7)))
        x15 = toobject(x14, x7)
        if x13 != x15:
            continue
        x16 = fill(x7, ZERO, x6[x4][-ONE])
        return {"input": x7, "output": x16}
    raise RuntimeError("failed to generate 54db823b example")
