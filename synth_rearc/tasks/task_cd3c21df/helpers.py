from synth_rearc.core import *


FG_COLORS_CD3C21DF = tuple(remove(ZERO, interval(ZERO, TEN, ONE)))


def sample_int_cd3c21df(
    diff_lb: float,
    diff_ub: float,
    lower: int,
    upper: int,
) -> int:
    if upper <= lower:
        return lower
    return unifint(diff_lb, diff_ub, (lower, upper))


def rectangle_patch_cd3c21df(
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    x0 = interval(ZERO, height_value, ONE)
    x1 = interval(ZERO, width_value, ONE)
    return frozenset(product(x0, x1))


def sample_connected_patch_cd3c21df(
    diff_lb: float,
    diff_ub: float,
    height_bounds: tuple[int, int],
    width_bounds: tuple[int, int],
    cell_bounds: tuple[int, int],
    *,
    require_irregular: bool = False,
) -> Indices:
    for _ in range(400):
        x0 = sample_int_cd3c21df(diff_lb, diff_ub, height_bounds[ZERO], height_bounds[ONE])
        x1 = sample_int_cd3c21df(diff_lb, diff_ub, width_bounds[ZERO], width_bounds[ONE])
        x2 = min(cell_bounds[ONE], x0 * x1)
        if x2 <= ZERO:
            continue
        x3 = min(cell_bounds[ZERO], x2)
        x4 = sample_int_cd3c21df(diff_lb, diff_ub, x3, x2)
        x5 = {astuple(randint(ZERO, x0 - ONE), randint(ZERO, x1 - ONE))}
        while len(x5) < x4:
            x6 = set()
            for x7 in tuple(x5):
                for x8 in dneighbors(x7):
                    if not (ZERO <= x8[ZERO] < x0 and ZERO <= x8[ONE] < x1):
                        continue
                    if x8 in x5:
                        continue
                    x6.add(x8)
            if len(x6) == ZERO:
                break
            x5.add(choice(tuple(x6)))
        if len(x5) != x4:
            continue
        x9 = frozenset(normalize(frozenset(x5)))
        if height(x9) < height_bounds[ZERO] or width(x9) < width_bounds[ZERO]:
            continue
        if require_irregular and size(x9) == height(x9) * width(x9):
            continue
        return x9
    raise RuntimeError("failed to sample connected patch for cd3c21df")


def _connected_subset_cd3c21df(
    diff_lb: float,
    diff_ub: float,
    cells: Indices,
    lower: int,
    upper: int,
) -> Indices:
    x0 = tuple(cells)
    x1 = min(upper, len(x0))
    if x1 <= ZERO:
        return frozenset()
    x2 = min(lower, x1)
    for _ in range(200):
        x3 = sample_int_cd3c21df(diff_lb, diff_ub, x2, x1)
        x4 = {choice(x0)}
        while len(x4) < x3:
            x5 = set()
            for x6 in tuple(x4):
                x5 |= set(dneighbors(x6)) & set(cells)
            x5 -= x4
            if len(x5) == ZERO:
                break
            x4.add(choice(tuple(x5)))
        if len(x4) == x3:
            return frozenset(x4)
    return frozenset({choice(x0)})


def colored_object_cd3c21df(
    diff_lb: float,
    diff_ub: float,
    patch: Indices,
    min_colors: int,
    max_colors: int,
) -> Object:
    x0 = tuple(patch)
    x1 = min(max_colors, len(x0))
    x2 = min(min_colors, x1)
    x3 = sample_int_cd3c21df(diff_lb, diff_ub, x2, x1)
    x4 = sample(FG_COLORS_CD3C21DF, x3)
    x5 = {x6: x4[ZERO] for x6 in x0}
    x6 = set(x0)
    for x7 in range(ONE, x3):
        x8 = x3 - x7 - ONE
        x9 = len(x6) - x8 - ONE
        if x9 < ONE:
            break
        x10 = max(ONE, min(x9, len(x0) // TWO))
        x11 = _connected_subset_cd3c21df(diff_lb, diff_ub, frozenset(x6), ONE, x10)
        for x12 in x11:
            x5[x12] = x4[x7]
        x6 -= set(x11)
    return frozenset((x5[x13], x13) for x13 in x0)


def spacing_indices_cd3c21df(
    patch: Patch,
) -> Indices:
    x0 = set()
    for x1 in toindices(patch):
        x0.add(x1)
        x0 |= set(neighbors(x1))
    return frozenset(x0)


def place_objects_cd3c21df(
    objects_to_place: tuple[Object, ...],
    grid_shape: tuple[int, int],
) -> tuple[Object, ...] | None:
    x0 = list(range(len(objects_to_place)))
    x0.sort(key=lambda x1: (-height(objects_to_place[x1]) * width(objects_to_place[x1]), -size(objects_to_place[x1])))
    x1 = [None] * len(objects_to_place)
    x2 = frozenset()
    x3, x4 = grid_shape
    for x5 in x0:
        x6 = objects_to_place[x5]
        x7, x8 = shape(x6)
        x9 = x3 - x7
        x10 = x4 - x8
        if x9 < ZERO or x10 < ZERO:
            return None
        x11 = ONE if x9 > TWO else ZERO
        x12 = x9 - ONE if x9 > TWO else x9
        x13 = ONE if x10 > TWO else ZERO
        x14 = x10 - ONE if x10 > TWO else x10
        x15 = None
        for _ in range(600):
            x16 = randint(x11, x12)
            x17 = randint(x13, x14)
            x18 = shift(x6, (x16, x17))
            if len(toindices(x18) & x2) > ZERO:
                continue
            x15 = x18
            break
        if x15 is None:
            return None
        x1[x5] = x15
        x2 = frozenset(set(x2) | set(spacing_indices_cd3c21df(x15)))
    return tuple(x1)
