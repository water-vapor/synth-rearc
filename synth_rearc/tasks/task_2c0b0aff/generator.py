from synth_rearc.core import *

from .verifier import verify_2c0b0aff


GRID_HEIGHT_BOUNDS_2C0B0AFF = (22, 24)
GRID_WIDTH_BOUNDS_2C0B0AFF = (20, 24)
PATCH_COUNT_OPTIONS_2C0B0AFF = (THREE, FOUR)
TARGET_PLUS_OPTIONS_2C0B0AFF = (THREE, THREE, THREE, FOUR, FOUR)
TARGET_NOISE_OPTIONS_2C0B0AFF = (ONE, TWO, TWO, THREE, THREE, FOUR, FOUR, FIVE, SIX)
NON_TARGET_NOISE_OPTIONS_2C0B0AFF = (TWO, THREE, THREE, FOUR, FIVE, FIVE, SIX, SEVEN, EIGHT, NINE, TEN)


def _plus_cells_2c0b0aff(
    loc: IntegerTuple,
) -> Indices:
    i, j = loc
    return frozenset({(i, j), (i - ONE, j), (i + ONE, j), (i, j - ONE), (i, j + ONE)})


def _plus_count_2c0b0aff(
    grid: Grid,
) -> Integer:
    x0 = ofcolor(grid, THREE)
    x1 = sfilter(x0, lambda x2: equality(size(intersection(x0, dneighbors(x2))), FOUR))
    return size(x1)


def _plus_corners_2c0b0aff(
    loc: IntegerTuple,
) -> Indices:
    i, j = loc
    return frozenset({(i - ONE, j - ONE), (i - ONE, j + ONE), (i + ONE, j - ONE), (i + ONE, j + ONE)})


def _inside_2c0b0aff(
    loc: IntegerTuple,
    dims: IntegerTuple,
) -> Boolean:
    return 0 <= loc[ZERO] < dims[ZERO] and 0 <= loc[ONE] < dims[ONE]


def _centers_compatible_2c0b0aff(
    a: IntegerTuple,
    b: IntegerTuple,
) -> Boolean:
    x0 = _plus_cells_2c0b0aff(a)
    x1 = _plus_cells_2c0b0aff(b)
    x2 = _plus_corners_2c0b0aff(a)
    x3 = _plus_corners_2c0b0aff(b)
    return x0.isdisjoint(x1) and x0.isdisjoint(x3) and x1.isdisjoint(x2)


def _sample_centers_2c0b0aff(
    dims: IntegerTuple,
    ncenters: Integer,
) -> tuple[IntegerTuple, ...] | None:
    h, w = dims
    x0 = tuple(product(interval(ONE, decrement(h), ONE), interval(ONE, decrement(w), ONE)))
    x1 = sample(x0, len(x0))
    x2 = []
    for x3 in x1:
        if all(_centers_compatible_2c0b0aff(x3, x4) for x4 in x2):
            x2.append(x3)
            if len(x2) == ncenters:
                return tuple(x2)
    return None


def _noise_component_available_2c0b0aff(
    cells: Indices,
    occupied: Indices,
) -> Boolean:
    return all(x0 not in occupied and all((x1 not in occupied) for x1 in difference(dneighbors(x0), cells)) for x0 in cells)


def _sample_noise_2c0b0aff(
    dims: IntegerTuple,
    centers: tuple[IntegerTuple, ...],
    is_target: Boolean,
) -> Indices:
    h, w = dims
    x0 = set()
    for x1 in centers:
        x2 = _plus_cells_2c0b0aff(x1)
        x0.update(x2)
        for x3 in x2:
            x0.add(x3)
            x0.update(x4 for x4 in dneighbors(x3) if _inside_2c0b0aff(x4, dims))
    x5 = tuple((x6, x7) for x6, x7 in product(interval(ZERO, h, ONE), interval(ZERO, w, ONE)) if (x6, x7) not in x0)
    x6 = tuple(x7 for x7 in x5 if x7[ZERO] in (ZERO, decrement(h)) or x7[ONE] in (ZERO, decrement(w)))
    x7 = []
    x8 = []
    for x9 in range(h):
        for x10 in range(decrement(w)):
            x11 = frozenset({(x9, x10), (x9, x10 + ONE)})
            if all(x12 in x6 for x12 in x11):
                x7.append(x11)
    for x9 in range(decrement(h)):
        for x10 in range(w):
            x11 = frozenset({(x9, x10), (x9 + ONE, x10)})
            if all(x12 in x6 for x12 in x11):
                x8.append(x11)
    x9 = choice(TARGET_NOISE_OPTIONS_2C0B0AFF if is_target else NON_TARGET_NOISE_OPTIONS_2C0B0AFF)
    x10 = set()
    for _ in range(multiply(x9, TWO)):
        if len(x10) == x9:
            break
        x11 = tuple(x12 for x12 in x5 if _noise_component_available_2c0b0aff(frozenset({x12}), frozenset(x10)))
        x12 = tuple(x13 for x13 in x11 if x13 in x6)
        x13 = tuple(x14 for x14 in x7 if _noise_component_available_2c0b0aff(x14, frozenset(x10)))
        x14 = tuple(x15 for x15 in x8 if _noise_component_available_2c0b0aff(x15, frozenset(x10)))
        x15 = subtract(x9, len(x10))
        if x15 > ONE and (x13 or x14) and choice((T, F, F, F, F, F, F, F, F)):
            if x13 and (not x14 or choice((T, T, T, T, T, T, T, T, T, F))):
                x16 = choice(x13)
            else:
                x16 = choice(x14)
            x10.update(x16)
            continue
        if x11:
            if x12 and choice((T, F, F)):
                x10.add(choice(x12))
            else:
                x10.add(choice(x11))
            continue
        if x15 > ONE and (x13 or x14):
            if x13 and (not x14 or choice((T, T, T, T, T, T, T, T, T, F))):
                x16 = choice(x13)
            else:
                x16 = choice(x14)
            x10.update(x16)
            continue
        break
    return frozenset(x10)


def _sample_patch_2c0b0aff(
    diff_lb: float,
    diff_ub: float,
    npluses: Integer,
    is_target: Boolean,
) -> Grid:
    while True:
        if is_target:
            x0 = unifint(diff_lb, diff_ub, (SEVEN, EIGHT))
            x1 = unifint(diff_lb, diff_ub, (EIGHT, 11))
        else:
            x0 = min(TEN, add(npluses, FOUR))
            x1 = max(FIVE, subtract(x0, choice((ZERO, ONE, TWO))))
            x2 = min(11, add(npluses, FIVE))
            x3 = max(SEVEN, subtract(x2, choice((ZERO, ONE, TWO))))
            x0 = unifint(diff_lb, diff_ub, (x1, x0))
            x1 = unifint(diff_lb, diff_ub, (x3, x2))
        x6 = _sample_centers_2c0b0aff((x0, x1), npluses)
        if x6 is None:
            continue
        x7 = set()
        for x8 in x6:
            x7.update(_plus_cells_2c0b0aff(x8))
        x9 = _sample_noise_2c0b0aff((x0, x1), x6, is_target)
        x7.update(x9)
        x10 = fill(canvas(EIGHT, (x0, x1)), THREE, frozenset(x7))
        x11 = _plus_count_2c0b0aff(x10)
        if x11 != npluses:
            continue
        x12 = subtract(colorcount(x10, THREE), multiply(FIVE, npluses))
        if is_target:
            if x12 < ONE or x12 > SIX:
                continue
        elif x12 < TWO or x12 > TEN:
            continue
        x13 = ofcolor(x10, THREE)
        if any(not _plus_corners_2c0b0aff(x14).isdisjoint(x13) for x14 in x6):
            continue
        if numcolors(x10) != TWO:
            continue
        return x10


def _boxes_separate_2c0b0aff(
    a: tuple[Integer, Integer, Integer, Integer],
    b: tuple[Integer, Integer, Integer, Integer],
) -> Boolean:
    return (
        a[2] + ONE < b[0]
        or b[2] + ONE < a[0]
        or a[3] + ONE < b[1]
        or b[3] + ONE < a[1]
    )


def _place_patches_2c0b0aff(
    dims: IntegerTuple,
    patches: tuple[Grid, ...],
) -> tuple[tuple[Integer, Integer], ...] | None:
    h, w = dims
    order_ids = tuple(sorted(range(len(patches)), key=lambda x0: multiply(height(patches[x0]), width(patches[x0])), reverse=True))
    boxes = [None] * len(patches)
    for x0 in order_ids:
        x1 = patches[x0]
        x2 = height(x1)
        x3 = width(x1)
        if x2 >= h or x3 >= w:
            return None
        x4 = tuple(product(interval(ZERO, add(subtract(h, x2), ONE), ONE), interval(ZERO, add(subtract(w, x3), ONE), ONE)))
        x5 = sample(x4, len(x4))
        x6 = None
        for x7 in x5:
            x8 = (x7[ZERO], x7[ONE], add(x7[ZERO], subtract(x2, ONE)), add(x7[ONE], subtract(x3, ONE)))
            if all(_boxes_separate_2c0b0aff(x8, x9) for x9 in boxes if x9 is not None):
                x6 = x7
                boxes[x0] = x8
                break
        if x6 is None:
            return None
    return tuple((x0[ZERO], x0[ONE]) for x0 in boxes)


def generate_2c0b0aff(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(PATCH_COUNT_OPTIONS_2C0B0AFF)
        x1 = choice(TARGET_PLUS_OPTIONS_2C0B0AFF)
        x2 = randint(ZERO, subtract(x0, ONE))
        x3 = []
        for x4 in range(x0):
            if x4 == x2:
                x3.append(x1)
            else:
                x3.append(randint(ONE, subtract(x1, ONE)))
        x4 = tuple(_sample_patch_2c0b0aff(diff_lb, diff_ub, x5, equality(x6, x2)) for x6, x5 in enumerate(x3))
        x5 = unifint(diff_lb, diff_ub, GRID_HEIGHT_BOUNDS_2C0B0AFF)
        x6 = unifint(diff_lb, diff_ub, GRID_WIDTH_BOUNDS_2C0B0AFF)
        x7 = _place_patches_2c0b0aff((x5, x6), x4)
        if x7 is None:
            continue
        x8 = canvas(ZERO, (x5, x6))
        for x9, x10 in zip(x4, x7):
            x8 = paint(x8, shift(asobject(x9), x10))
        x11 = x4[x2]
        if verify_2c0b0aff(x8) != x11:
            continue
        return {"input": x8, "output": x11}
