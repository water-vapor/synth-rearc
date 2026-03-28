from collections import deque

from arc2.core import *


def _polyline_3bd292e8(
    points,
):
    x0 = frozenset()
    for x1, x2 in zip(points, points[1:]):
        x0 = combine(x0, connect(x1, x2))
    return x0


def _sample_top_right_path_3bd292e8(
    side: Integer,
    short0: Boolean,
):
    x0 = randint(ZERO, side - THREE)
    x1 = randint(TWO if short0 else THREE, side - ONE)
    if short0:
        x2 = ((ZERO, x0), (x1, x0), (x1, side - ONE))
    else:
        x2 = randint(ONE, x1 - TWO)
        x3 = randint(x0 + ONE, side - TWO)
        x2 = ((ZERO, x0), (x2, x0), (x2, x3), (x1, x3), (x1, side - ONE))
    return _polyline_3bd292e8(x2)


def _sample_left_bottom_path_3bd292e8(
    side: Integer,
    short0: Boolean,
):
    x0 = randint(ZERO, side - THREE)
    x1 = randint(TWO if short0 else THREE, side - ONE)
    if short0:
        x2 = ((x0, ZERO), (x0, x1), (side - ONE, x1))
    else:
        x2 = randint(ONE, x1 - TWO)
        x3 = randint(x0 + ONE, side - TWO)
        x2 = ((x0, ZERO), (x0, x2), (x3, x2), (x3, x1), (side - ONE, x1))
    return _polyline_3bd292e8(x2)


def _sample_path_3bd292e8(
    side: Integer,
):
    x0 = choice((T, F, F))
    x1 = choice(("top_right", "left_bottom"))
    if x1 == "top_right":
        return _sample_top_right_path_3bd292e8(side, x0)
    return _sample_left_bottom_path_3bd292e8(side, x0)


def _components_3bd292e8(
    grid: Grid,
    color0: Integer,
):
    x0 = objects(grid, T, F, F)
    x1 = colorfilter(x0, color0)
    return tuple(order(x1, ulcorner))


def _is_simple_path_3bd292e8(
    patch: Patch,
):
    x0 = toindices(patch)
    x1 = tuple(len(intersection(dneighbors(x2), x0)) for x2 in x0)
    return x1.count(ONE) == TWO and minimum(x1) == ONE and maximum(x1) == TWO


def _separate_path_3bd292e8(
    grid: Grid,
    path: Patch,
):
    x0 = toindices(path)
    if (subtract(height(grid), ONE), ZERO) in x0:
        return F
    x1 = ofcolor(grid, TWO)
    if len(intersection(x0, x1)) > ZERO:
        return F
    for x2 in x0:
        for x3 in dneighbors(x2):
            if x3 in x1 and x3 not in x0:
                return F
    return T


def _try_add_path_3bd292e8(
    grid: Grid,
    path: Patch,
):
    if not _separate_path_3bd292e8(grid, path):
        return None
    x0 = _components_3bd292e8(grid, TWO)
    x1 = _components_3bd292e8(grid, SEVEN)
    x2 = fill(grid, TWO, path)
    x3 = _components_3bd292e8(x2, TWO)
    x4 = _components_3bd292e8(x2, SEVEN)
    if len(x3) != len(x0) + ONE:
        return None
    if len(x4) != len(x1) + ONE:
        return None
    if min(len(obj) for obj in x4) < TWO:
        return None
    if not all(_is_simple_path_3bd292e8(obj) for obj in x3):
        return None
    return x2


def _paint_regions_3bd292e8(
    grid: Grid,
):
    x0 = _components_3bd292e8(grid, SEVEN)
    x1 = {cell: idx for idx, obj in enumerate(x0) for cell in toindices(obj)}
    x2 = [set() for _ in x0]
    for x3 in ofcolor(grid, TWO):
        x4 = {x1[x5] for x5 in dneighbors(x3) if x5 in x1}
        for x5 in x4:
            for x6 in x4:
                if x5 != x6:
                    x2[x5].add(x6)
    x3 = x1[(subtract(height(grid), ONE), ZERO)]
    x4 = {x3: ZERO}
    x5 = deque((x3,))
    while len(x5) > ZERO:
        x6 = x5.popleft()
        for x7 in x2[x6]:
            if x7 not in x4:
                x4[x7] = increment(x4[x6])
                x5.append(x7)
    x6 = grid
    for x7, x8 in enumerate(x0):
        x9 = branch(even(x4[x7]), FIVE, THREE)
        x6 = fill(x6, x9, x8)
    return x6


def generate_3bd292e8(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    for _ in range(800):
        x0 = unifint(diff_lb, diff_ub, (SEVEN, NINE))
        if x0 == SEVEN:
            x2 = choice((ONE, TWO, TWO))
        elif x0 == EIGHT:
            x2 = choice((TWO, THREE, THREE))
        else:
            x2 = choice((TWO, THREE, THREE, THREE))
        x3 = canvas(SEVEN, (x0, x0))
        x4 = T
        for _ in range(x2):
            x5 = F
            for _ in range(250):
                x6 = _sample_path_3bd292e8(x0)
                x7 = _try_add_path_3bd292e8(x3, x6)
                if x7 is None:
                    continue
                x3 = x7
                x5 = T
                break
            if not x5:
                x4 = F
                break
        if not x4:
            continue
        x8 = _paint_regions_3bd292e8(x3)
        if x3 == x8:
            continue
        return {"input": x3, "output": x8}
    raise RuntimeError("failed to generate example for 3bd292e8")
