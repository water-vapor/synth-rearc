from synth_rearc.core import *


_SPECIAL_BOTTOM_WEDGE_IN_D753A70B = frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, TWO)})
_SPECIAL_BOTTOM_WEDGE_OUT_D753A70B = frozenset(
    {(ZERO, TWO), (ONE, ONE), (ONE, THREE), (TWO, ZERO), (TWO, FOUR)}
)


def diamond_outline_d753a70b(
    center: IntegerTuple,
    radius: Integer,
    dims: IntegerTuple,
) -> Indices:
    h, w = dims
    ci, cj = center
    cells = set()
    for di in range(-radius, radius + ONE):
        dj = radius - abs(di)
        row = ci + di
        if dj == ZERO:
            col = cj
            if ZERO <= row < h and ZERO <= col < w:
                cells.add((row, col))
            continue
        col_left = cj - dj
        col_right = cj + dj
        if ZERO <= row < h and ZERO <= col_left < w:
            cells.add((row, col_left))
        if ZERO <= row < h and ZERO <= col_right < w:
            cells.add((row, col_right))
    return frozenset(cells)


def diamond_candidates_d753a70b(
    patch: Patch,
    dims: IntegerTuple,
) -> tuple[tuple[Integer, IntegerTuple], ...]:
    cells = tuple(sorted(toindices(patch)))
    if len(cells) == ZERO:
        return tuple()
    rows = tuple(i for i, _ in cells)
    cols = tuple(j for _, j in cells)
    limit = maximum(dims)
    seed = first(cells)
    candidates = []
    for ci in range(minimum(rows) - limit, maximum(rows) + limit + ONE):
        for cj in range(minimum(cols) - limit, maximum(cols) + limit + ONE):
            center = astuple(ci, cj)
            radius = manhattan(initset(seed), initset(center))
            if any(manhattan(initset(cell), initset(center)) != radius for cell in cells):
                continue
            if diamond_outline_d753a70b(center, radius, dims) != frozenset(cells):
                continue
            candidates.append((radius, center))
    candidates.sort(key=lambda item: (item[ZERO], item[ONE][ZERO], item[ONE][ONE]))
    return tuple(candidates)


def special_bottom_wedge_d753a70b(
    patch: Patch,
    dims: IntegerTuple,
) -> Boolean:
    x0 = toindices(patch)
    x1 = normalize(x0)
    x2 = equality(x1, _SPECIAL_BOTTOM_WEDGE_IN_D753A70B)
    x3 = equality(lowermost(x0), subtract(dims[ZERO], ONE))
    return both(x2, x3)


def transformed_component_d753a70b(
    obj: Object,
    dims: IntegerTuple,
) -> Object:
    x0 = color(obj)
    x1 = toindices(obj)
    if equality(x0, FIVE) and special_bottom_wedge_d753a70b(x1, dims):
        x2 = subtract(uppermost(x1), ONE)
        x3 = leftmost(x1)
        x4 = astuple(x2, x3)
        x5 = shift(_SPECIAL_BOTTOM_WEDGE_OUT_D753A70B, x4)
        return recolor(x0, x5)
    if x0 not in (TWO, FIVE):
        return obj
    x6 = diamond_candidates_d753a70b(x1, dims)
    if len(x6) == ZERO:
        return obj
    x7, x8 = first(x6)
    x9 = maximum((ZERO, subtract(x7, ONE))) if equality(x0, TWO) else add(x7, ONE)
    x10 = diamond_outline_d753a70b(x8, x9, dims)
    return recolor(x0, x10)
