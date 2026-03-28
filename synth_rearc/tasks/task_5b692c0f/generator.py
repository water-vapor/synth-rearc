from synth_rearc.core import *

from .verifier import verify_5b692c0f


MAIN_COLORS_5B692C0F = (ONE, TWO, THREE, FIVE, SIX, SEVEN, EIGHT, NINE)
OBJECT_COUNT_BOUNDS_5B692C0F = (ONE, FOUR)
AXIS_LENGTH_BOUNDS_5B692C0F = (THREE, EIGHT)
SIDE_DEPTH_BOUNDS_5B692C0F = (TWO, FIVE)
NOISE_COUNT_BOUNDS_5B692C0F = (ZERO, ONE)
TEMP_CANVAS_SIDE_5B692C0F = 30


def _connected_indices_5b692c0f(
    patch: Indices,
) -> bool:
    if len(patch) == ZERO:
        return F
    x0 = first(patch)
    x1 = {x0}
    x2 = {x0}
    while len(x1) > ZERO:
        x3 = x1.pop()
        for x4 in dneighbors(x3):
            if x4 in patch and x4 not in x2:
                x2.add(x4)
                x1.add(x4)
    return len(x2) == len(patch)


def _axis_distance_5b692c0f(
    loc: IntegerTuple,
    vertical: bool,
) -> Integer:
    return loc[1] if vertical else loc[0]


def _has_axis_contact_5b692c0f(
    patch: Indices,
    vertical: bool,
) -> bool:
    return any(_axis_distance_5b692c0f(loc, vertical) == ONE for loc in patch)


def _carve_side_patch_5b692c0f(
    patch: Indices,
    vertical: bool,
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    x0 = set(patch)
    if len(x0) <= THREE:
        return frozenset(x0)
    x1 = min(THREE, len(x0) - TWO)
    x2 = unifint(diff_lb, diff_ub, (ZERO, x1))
    x3 = ZERO
    while x3 < x2:
        x4 = [loc for loc in x0 if _axis_distance_5b692c0f(loc, vertical) > ONE]
        if len(x4) == ZERO:
            break
        x5 = [loc for loc in x4 for _ in range(_axis_distance_5b692c0f(loc, vertical))]
        x6 = choice(x5)
        x7 = frozenset(loc for loc in x0 if loc != x6)
        if flip(_has_axis_contact_5b692c0f(x7, vertical)):
            continue
        if flip(_connected_indices_5b692c0f(x7)):
            continue
        x0 = set(x7)
        x3 = increment(x3)
    return frozenset(x0)


def _build_side_patch_5b692c0f(
    axis_len: Integer,
    depth: Integer,
    vertical: bool,
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    while True:
        x0 = [unifint(diff_lb, diff_ub, (ONE, depth))]
        for _ in range(axis_len - ONE):
            x1 = x0[-ONE]
            x2 = max(ONE, x1 - ONE)
            x3 = min(depth, x1 + ONE)
            x0.append(unifint(diff_lb, diff_ub, (x2, x3)))
        if max(x0) == ONE and depth > ONE:
            x0[randint(ZERO, axis_len - ONE)] = TWO
        x4 = set()
        for x5, x6 in enumerate(x0):
            for x7 in range(ONE, x6 + ONE):
                x8 = (x5, x7) if vertical else (x7, x5)
                x4.add(x8)
        x9 = _carve_side_patch_5b692c0f(frozenset(x4), vertical, diff_lb, diff_ub)
        if len(x9) <= axis_len:
            continue
        if flip(_connected_indices_5b692c0f(x9)):
            continue
        if flip(_has_axis_contact_5b692c0f(x9, vertical)):
            continue
        return x9


def _thin_side_patch_5b692c0f(
    patch: Indices,
    vertical: bool,
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    x0 = set(patch)
    if len(x0) <= ONE:
        return frozenset(x0)
    x1 = max(ONE, len(x0) // THREE)
    x2 = min(len(x0) - ONE, max(TWO, (len(x0) * THREE) // FOUR))
    if x1 > x2:
        x1 = ONE
        x2 = len(x0) - ONE
    x3 = unifint(diff_lb, diff_ub, (x1, x2))
    x4 = ZERO
    while len(x0) > x3 and x4 < 200:
        x4 = increment(x4)
        x5 = [loc for loc in x0 for _ in range(max(ONE, _axis_distance_5b692c0f(loc, vertical)))]
        x6 = choice(x5)
        x7 = frozenset(loc for loc in x0 if loc != x6)
        if flip(_has_axis_contact_5b692c0f(x7, vertical)):
            continue
        if flip(_connected_indices_5b692c0f(x7)):
            continue
        x0 = set(x7)
    if len(x0) == len(patch):
        x8 = tuple(sorted(patch, key=lambda loc: (_axis_distance_5b692c0f(loc, vertical), loc), reverse=T))
        for x9 in x8:
            x10 = frozenset(loc for loc in x0 if loc != x9)
            if flip(_has_axis_contact_5b692c0f(x10, vertical)):
                continue
            if flip(_connected_indices_5b692c0f(x10)):
                continue
            x0 = set(x10)
            break
    return frozenset(x0)


def _accent_indices_5b692c0f(
    patch: Indices,
    vertical: bool,
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    x0 = tuple(loc for loc in patch if _axis_distance_5b692c0f(loc, vertical) > ONE)
    if len(x0) == ZERO or choice((T, F, F)) == F:
        return frozenset()
    x1 = min(TWO, len(x0))
    x2 = unifint(diff_lb, diff_ub, (ONE, x1))
    return frozenset(sample(x0, x2))


def _color_side_5b692c0f(
    patch: Indices,
    color_value: Integer,
    accents: Indices,
) -> Object:
    return frozenset((FOUR if loc in accents else color_value, loc) for loc in patch)


def _mirror_vertical_object_5b692c0f(
    obj: Object,
) -> Object:
    return frozenset((value, (i, -j)) for value, (i, j) in obj)


def _mirror_horizontal_object_5b692c0f(
    obj: Object,
) -> Object:
    return frozenset((value, (-i, j)) for value, (i, j) in obj)


def _build_pair_5b692c0f(
    color_value: Integer,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Object, Object]:
    while True:
        x0 = choice((T, F))
        x1 = unifint(diff_lb, diff_ub, AXIS_LENGTH_BOUNDS_5B692C0F)
        x2 = unifint(diff_lb, diff_ub, SIDE_DEPTH_BOUNDS_5B692C0F)
        x3 = _build_side_patch_5b692c0f(x1, x2, x0, diff_lb, diff_ub)
        x4 = _thin_side_patch_5b692c0f(x3, x0, diff_lb, diff_ub)
        if len(x4) == len(x3):
            continue
        x5 = _accent_indices_5b692c0f(x3, x0, diff_lb, diff_ub)
        x6 = frozenset((k, ZERO) for k in range(x1)) if x0 else frozenset((ZERO, k) for k in range(x1))
        x7 = recolor(FOUR, x6)
        x8 = _color_side_5b692c0f(x3, color_value, x5)
        x9 = frozenset((value, loc) for value, loc in x8 if loc in x4)
        if x0:
            x10 = _mirror_vertical_object_5b692c0f(x8)
            x11 = _mirror_vertical_object_5b692c0f(x9)
        else:
            x10 = _mirror_horizontal_object_5b692c0f(x8)
            x11 = _mirror_horizontal_object_5b692c0f(x9)
        if choice((T, F)):
            x12 = combine(x7, combine(x8, x11))
            x13 = combine(x7, combine(x8, x10))
        else:
            x12 = combine(x7, combine(x10, x9))
            x13 = combine(x7, combine(x10, x8))
        x14 = normalize(x12)
        x15 = normalize(x13)
        if x14 == x15:
            continue
        return x14, x15


def _scatter_pairs_5b692c0f(
    pairs: tuple[tuple[Object, Object], ...],
) -> tuple[Grid, Grid] | None:
    x0 = canvas(ZERO, (TEMP_CANVAS_SIDE_5B692C0F, TEMP_CANVAS_SIDE_5B692C0F))
    x1 = x0
    x2 = frozenset()
    x3 = tuple(sorted(pairs, key=lambda pair: (-len(pair[1]), -height(pair[1]), -width(pair[1]))))
    for x4, x5 in x3:
        x6 = height(x5)
        x7 = width(x5)
        x8 = []
        for i in range(ONE, TEMP_CANVAS_SIDE_5B692C0F - x6):
            for j in range(ONE, TEMP_CANVAS_SIDE_5B692C0F - x7):
                x9 = shift(x5, (i, j))
                x10 = backdrop(outbox(x9))
                if size(intersection(x2, x10)) != ZERO:
                    continue
                x11 = shift(x4, (i, j))
                x8.append((x11, x9, x10))
        if len(x8) == ZERO:
            return None
        x12, x13, x14 = choice(x8)
        x0 = paint(x0, x12)
        x1 = paint(x1, x13)
        x2 = combine(x2, x14)
    return x0, x1


def _trim_canvas_5b692c0f(
    gi: Grid,
    go: Grid,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Grid, Grid]:
    x0 = [(i, j) for i, row in enumerate(go) for j, value in enumerate(row) if value != ZERO]
    x1 = tuple(i for i, _ in x0)
    x2 = tuple(j for _, j in x0)
    x3 = min(x1)
    x4 = max(x1)
    x5 = min(x2)
    x6 = max(x2)
    x7 = unifint(diff_lb, diff_ub, (ONE, min(FOUR, x3)))
    x8 = unifint(diff_lb, diff_ub, (ONE, min(FOUR, TEMP_CANVAS_SIDE_5B692C0F - ONE - x4)))
    x9 = unifint(diff_lb, diff_ub, (ONE, min(FOUR, x5)))
    x10 = unifint(diff_lb, diff_ub, (ONE, min(FOUR, TEMP_CANVAS_SIDE_5B692C0F - ONE - x6)))
    x11 = subtract(x3, x7)
    x12 = subtract(x5, x9)
    x13 = add(add(subtract(x4, x3), ONE), add(x7, x8))
    x14 = add(add(subtract(x6, x5), ONE), add(x9, x10))
    x15 = crop(gi, (x11, x12), (x13, x14))
    x16 = crop(go, (x11, x12), (x13, x14))
    return x15, x16


def generate_5b692c0f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, OBJECT_COUNT_BOUNDS_5B692C0F)
        x1 = tuple(sample(MAIN_COLORS_5B692C0F, x0))
        x2 = tuple(_build_pair_5b692c0f(color_value, diff_lb, diff_ub) for color_value in x1)
        x3 = unifint(diff_lb, diff_ub, NOISE_COUNT_BOUNDS_5B692C0F)
        x4 = []
        for _ in range(x3):
            x5 = choice(x1)
            x6 = recolor(x5, initset((ZERO, ZERO)))
            x4.append((x6, x6))
        x7 = _scatter_pairs_5b692c0f(x2 + tuple(x4))
        if x7 is None:
            continue
        x8, x9 = x7
        gi, go = _trim_canvas_5b692c0f(x8, x9, diff_lb, diff_ub)
        if gi == go:
            continue
        if verify_5b692c0f(gi) != go:
            continue
        return {"input": gi, "output": go}
