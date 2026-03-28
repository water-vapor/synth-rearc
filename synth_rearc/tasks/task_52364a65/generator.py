from synth_rearc.core import *

from .verifier import verify_52364a65


BG_52364A65 = EIGHT
ACTIVE_COLORS_52364A65 = remove(BG_52364A65, interval(ZERO, TEN, ONE))


def _rows_to_indices_52364a65(
    rows: tuple[tuple[Integer, Integer], ...],
) -> Indices:
    return frozenset(
        (i, j)
        for i, (left0, right0) in enumerate(rows)
        for j in range(left0, right0 + ONE)
    )


def _rectangle_shape_52364a65(
    height0: Integer,
    width0: Integer,
) -> Indices:
    x0 = tuple((ZERO, width0 - ONE) for _ in range(height0))
    return _rows_to_indices_52364a65(x0)


def _bulge_shape_52364a65(
    height0: Integer,
    width0: Integer,
) -> Indices:
    if height0 <= TWO or width0 <= TWO:
        return _rectangle_shape_52364a65(height0, width0)
    x0 = randint(ONE, height0 - TWO)
    x1 = min(height0 - ONE, x0 + choice((ZERO, ONE)))
    x2 = randint(max(ONE, width0 // THREE), width0 - ONE)
    x3 = randint(max(ONE, width0 // THREE), width0 - ONE)
    x4 = randint(ZERO, width0 - x2)
    x5 = randint(ZERO, width0 - x3)
    x6 = []
    for x7 in range(height0):
        if x0 <= x7 <= x1:
            x6.append((ZERO, width0 - ONE))
        elif x7 < x0:
            x6.append((x4, x4 + x2 - ONE))
        else:
            x6.append((x5, x5 + x3 - ONE))
    return _rows_to_indices_52364a65(tuple(x6))


def _tail_shape_52364a65(
    height0: Integer,
    width0: Integer,
) -> Indices:
    if height0 <= TWO or width0 <= TWO:
        return _rectangle_shape_52364a65(height0, width0)
    x0 = randint(ONE, height0 - ONE)
    x1 = randint(max(ONE, width0 // TWO), width0 - ONE)
    x2 = randint(ONE, max(ONE, width0 - TWO))
    x3 = width0 - x2
    x4 = []
    for x5 in range(height0):
        if x5 < x0:
            x4.append((ZERO, x1 - ONE))
        elif x5 == x0:
            x4.append((ZERO, width0 - ONE))
        else:
            x4.append((x3, width0 - ONE))
    return _rows_to_indices_52364a65(tuple(x4))


def _sample_shape_52364a65(
    height0: Integer,
    width0: Integer,
) -> Indices:
    x0 = choice((ZERO, ONE, TWO, THREE, FOUR, FIVE))
    if x0 == ZERO:
        return _rectangle_shape_52364a65(height0, width0)
    if x0 == ONE:
        return _bulge_shape_52364a65(height0, width0)
    x1 = _tail_shape_52364a65(height0, width0)
    if x0 == TWO:
        return x1
    if x0 == THREE:
        return hmirror(x1)
    if x0 == FOUR:
        return vmirror(x1)
    return hmirror(vmirror(x1))


def _split_regions_52364a65(
    side: Integer,
) -> tuple[tuple[Integer, Integer, Integer, Integer], ...]:
    x0 = randint(FOUR, side - FIVE)
    x1 = randint(FOUR, side - FIVE)
    x2 = side - x0 - ONE
    x3 = side - x1 - ONE
    return (
        (ZERO, ZERO, x0, x1),
        (ZERO, x1 + ONE, x0, x3),
        (x0 + ONE, ZERO, x2, x1),
        (x0 + ONE, x1 + ONE, x2, x3),
    )


def _height_pool_52364a65(
    limit: Integer,
) -> tuple[Integer, ...]:
    return tuple(x0 for x0 in (TWO, TWO, THREE, THREE, FOUR, FIVE) if x0 <= limit)


def _width_pool_52364a65(
    limit: Integer,
    kind: Integer,
) -> tuple[Integer, ...]:
    if kind == ZERO:
        x0 = (TWO, THREE)
    elif kind == ONE:
        x0 = (FOUR, FOUR, FIVE, SIX)
    else:
        x0 = (THREE, FOUR, FIVE)
    x1 = tuple(x2 for x2 in x0 if x2 <= limit)
    if len(x1) != ZERO:
        return x1
    return tuple(x3 for x3 in (TWO, THREE, FOUR, FIVE, SIX) if x3 <= limit)


def _trim_object_52364a65(
    patch: Indices,
) -> Indices:
    x0 = minimum(tuple(x1 for _, x1 in patch))
    x2 = x0 + TWO
    return frozenset((x3, x4) for x3, x4 in patch if x4 >= x2)


def generate_52364a65(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (NINE, 13))
        x1 = astuple(x0, x0)
        x2 = _split_regions_52364a65(x0)
        x3 = sample(ACTIVE_COLORS_52364A65, FOUR)
        x4 = canvas(BG_52364A65, x1)
        x5 = canvas(BG_52364A65, x1)
        x6 = randint(ZERO, THREE)
        x7 = sample(remove(x6, interval(ZERO, FOUR, ONE)), TWO)
        x8 = next(x10 for x10 in range(FOUR) if x10 != x6 and x10 not in x7)
        x9 = {}
        x9[x6] = ZERO
        for x10 in x7:
            x9[x10] = ONE
        x9[x8] = TWO
        for x11, (x12, x13, x14, x15) in enumerate(x2):
            x16 = choice(_height_pool_52364a65(x14))
            x17 = choice(_width_pool_52364a65(x15, x9[x11]))
            x18 = _sample_shape_52364a65(x16, x17)
            x19 = randint(ZERO, x14 - x16)
            x20 = randint(ZERO, x15 - x17)
            x21 = shift(x18, (x12 + x19, x13 + x20))
            x22 = _trim_object_52364a65(x21)
            x23 = x3[x11]
            x4 = fill(x4, x23, x21)
            x5 = fill(x5, x23, x22)
        if x4 == x5:
            continue
        if size(objects(x4, T, F, T)) != FOUR:
            continue
        if mostcolor(x4) != BG_52364A65:
            continue
        if verify_52364a65(x4) != x5:
            continue
        return {"input": x4, "output": x5}
