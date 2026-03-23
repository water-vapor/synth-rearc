from arc2.core import *


GRID_SHAPE_6DF30AD6 = astuple(TEN, TEN)
GRID_CELLS_6DF30AD6 = asindices(canvas(ZERO, GRID_SHAPE_6DF30AD6))
COLORS_6DF30AD6 = remove(FIVE, remove(ZERO, interval(ZERO, TEN, ONE)))
RECTANGLE_DIMS_6DF30AD6 = (
    astuple(TWO, THREE),
    astuple(THREE, TWO),
    astuple(THREE, THREE),
)


def _diamond_6df30ad6(
    radius: Integer,
) -> Indices:
    x0 = 2 * radius + 1
    return frozenset(
        (i, j)
        for i in range(x0)
        for j in range(x0)
        if abs(i - radius) + abs(j - radius) <= radius
    )


def _base_shape_6df30ad6(
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    x0 = choice(("line", "line", "rectangle", "rectangle", "diamond"))
    if x0 == "line":
        x1 = unifint(diff_lb, diff_ub, (FOUR, SIX))
        x2 = choice((T, F))
        return connect(ORIGIN, branch(x2, astuple(subtract(x1, ONE), ZERO), astuple(ZERO, subtract(x1, ONE))))
    if x0 == "diamond":
        x1 = TWO
        return _diamond_6df30ad6(x1)
    x1 = choice(RECTANGLE_DIMS_6DF30AD6)
    x2 = subtract(x1[0], ONE)
    x3 = subtract(x1[1], ONE)
    return backdrop(frozenset({ORIGIN, astuple(x2, x3)}))


def _place_shape_6df30ad6(
    patch: Indices,
) -> Indices:
    x0 = height(patch)
    x1 = width(patch)
    x2 = randint(ONE, TEN - x0 - ONE)
    x3 = randint(ONE, TEN - x1 - ONE)
    return shift(patch, (x2, x3))


def _distance_to_shape_6df30ad6(
    patch: Indices,
    loc: IntegerTuple,
) -> Integer:
    return manhattan(patch, frozenset({loc}))


def _singleton_ok_6df30ad6(
    loc: IntegerTuple,
    placed: tuple[IntegerTuple, ...],
) -> Boolean:
    return all(loc != other and loc not in dneighbors(other) for other in placed)


def _candidate_cells_6df30ad6(
    patch: Indices,
    placed: tuple[IntegerTuple, ...],
    min_distance: Integer,
    exact_distance: Integer | None = None,
) -> tuple[IntegerTuple, ...]:
    x0 = []
    for x1 in GRID_CELLS_6DF30AD6:
        if x1 in patch:
            continue
        x2 = _distance_to_shape_6df30ad6(patch, x1)
        if x2 < min_distance:
            continue
        if exact_distance is not None and x2 != exact_distance:
            continue
        if not _singleton_ok_6df30ad6(x1, placed):
            continue
        x0.append(x1)
    return tuple(x0)


def _place_singletons_6df30ad6(
    patch: Indices,
    specs: dict[Integer, dict[str, Integer]],
) -> dict[Integer, tuple[IntegerTuple, ...]] | None:
    x0: list[IntegerTuple] = []
    x1: dict[Integer, list[IntegerTuple]] = {x2: [] for x2 in specs}
    x2 = sorted(specs, key=lambda x3: (specs[x3]["anchor_distance"], specs[x3]["count"]), reverse=True)
    for x3 in x2:
        x4 = specs[x3]["anchor_distance"]
        x5 = specs[x3]["min_distance"]
        x6 = _candidate_cells_6df30ad6(patch, tuple(x0), x5, x4)
        if len(x6) == ZERO:
            return None
        x7 = choice(x6)
        x0.append(x7)
        x1[x3].append(x7)
    x8 = sorted(specs, key=lambda x9: (specs[x9]["min_distance"], specs[x9]["count"]), reverse=True)
    for x9 in x8:
        x10 = specs[x9]["count"]
        x11 = specs[x9]["min_distance"]
        while len(x1[x9]) < x10:
            x12 = _candidate_cells_6df30ad6(patch, tuple(x0), x11)
            if len(x12) == ZERO:
                return None
            x13 = choice(x12)
            x0.append(x13)
            x1[x9].append(x13)
    return {x14: tuple(x15) for x14, x15 in x1.items()}


def _winning_color_6df30ad6(
    patch: Indices,
    bycolor: dict[Integer, tuple[IntegerTuple, ...]],
) -> Integer:
    x0 = tuple(bycolor)
    return min(
        x0,
        key=lambda x1: (
            min(_distance_to_shape_6df30ad6(patch, x2) for x2 in bycolor[x1]),
            len(bycolor[x1]),
            x1,
        ),
    )


def generate_6df30ad6(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _base_shape_6df30ad6(diff_lb, diff_ub)
        x1 = _place_shape_6df30ad6(x0)
        x2 = choice((TWO, THREE, THREE, THREE))
        x3 = sample(COLORS_6DF30AD6, x2)
        x4 = choice(x3)
        x5 = choice((TWO, TWO, TWO, THREE))
        x6 = x2 == THREE and choice((F, F, F, T))
        x7 = unifint(diff_lb, diff_ub, (ONE, FIVE if x6 else SIX))
        x8 = tuple(x9 for x9 in x3 if x9 != x4)
        x9 = choice(x8) if x6 else None
        x10 = {
            x4: {
                "count": x7,
                "min_distance": x5,
                "anchor_distance": x5,
            }
        }
        for x11 in x8:
            if x11 == x9:
                x12 = randint(x7 + ONE, SIX)
                x13 = x5
            else:
                x12 = unifint(diff_lb, diff_ub, (ONE, FIVE))
                x13 = x5 + randint(ONE, THREE)
            x10[x11] = {
                "count": x12,
                "min_distance": x13,
                "anchor_distance": x13,
            }
        x14 = _place_singletons_6df30ad6(x1, x10)
        if x14 is None:
            continue
        if _winning_color_6df30ad6(x1, x14) != x4:
            continue
        gi = fill(canvas(ZERO, GRID_SHAPE_6DF30AD6), FIVE, x1)
        for x15, x16 in x14.items():
            gi = fill(gi, x15, frozenset(x16))
        go = fill(canvas(ZERO, GRID_SHAPE_6DF30AD6), x4, x1)
        return {"input": gi, "output": go}
