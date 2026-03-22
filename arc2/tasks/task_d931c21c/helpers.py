from collections import deque

from arc2.core import *


def _as_local_patch_d931c21c(
    patch: Patch,
) -> Indices:
    return toindices(normalize(patch))


def _degree_histogram_d931c21c(
    patch: Patch,
) -> Tuple:
    x0 = toindices(patch)
    return tuple(sum(x1 in x0 for x1 in dneighbors(x2)) for x2 in x0)


def _is_single_component_d931c21c(
    patch: Patch,
) -> Boolean:
    if len(patch) == ZERO:
        return F
    x0 = _as_local_patch_d931c21c(patch)
    x1 = fill(canvas(ZERO, shape(x0)), ONE, x0)
    x2 = objects(x1, T, F, F)
    x3 = colorfilter(x2, ONE)
    return len(x3) == ONE


def is_cycle_d931c21c(
    patch: Patch,
) -> Boolean:
    x0 = _degree_histogram_d931c21c(patch)
    return len(x0) >= FOUR and _is_single_component_d931c21c(patch) and all(x1 == TWO for x1 in x0)


def is_open_path_d931c21c(
    patch: Patch,
) -> Boolean:
    x0 = _degree_histogram_d931c21c(patch)
    if len(x0) < TWO or not _is_single_component_d931c21c(patch):
        return F
    return x0.count(ONE) == TWO and all(x1 in (ONE, TWO) for x1 in x0)


def ring_patch_d931c21c(
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    x0 = interval(ZERO, height_value, ONE)
    x1 = interval(ZERO, width_value, ONE)
    x2 = product(x0, x1)
    return box(x2)


def slide_patch_d931c21c(
    patch: Patch,
    top: Integer,
    left: Integer,
) -> Indices:
    x0 = toindices(patch)
    x1 = frozenset(
        {
            (top, left),
            (top, increment(left)),
            (increment(top), left),
            (increment(top), increment(left)),
        }
    )
    x2 = intersection(x0, x1)
    if len(x2) != THREE:
        return x0
    x3 = first(difference(x1, x2))
    x4 = subtract(x3, (top, left))
    x5 = subtract((ONE, ONE), x4)
    x6 = add((top, left), x5)
    x7 = difference(x0, x2)
    x8 = difference(x1, initset(x6))
    return frozenset(combine(x7, x8))


def slide_candidates_d931c21c(
    patch: Patch,
    validator,
) -> Tuple:
    x0 = _as_local_patch_d931c21c(patch)
    x1, x2 = shape(x0)
    x3 = []
    x4 = set()
    for x5 in interval(ZERO, decrement(x1), ONE):
        for x6 in interval(ZERO, decrement(x2), ONE):
            x7 = slide_patch_d931c21c(x0, x5, x6)
            x8 = normalize(x7)
            if x8 == x0 or not validator(x8) or x8 in x4:
                continue
            x4.add(x8)
            x3.append(x8)
    return tuple(x3)


def mutate_shape_d931c21c(
    patch: Patch,
    validator,
    steps: Integer,
) -> Indices:
    x0 = _as_local_patch_d931c21c(patch)
    for _ in range(steps):
        x1 = slide_candidates_d931c21c(x0, validator)
        if len(x1) == ZERO:
            break
        x0 = choice(x1)
    return normalize(x0)


def make_cycle_patch_d931c21c(
    height_value: Integer,
    width_value: Integer,
    steps: Integer,
) -> Indices:
    x0 = ring_patch_d931c21c(height_value, width_value)
    return mutate_shape_d931c21c(x0, is_cycle_d931c21c, steps)


def make_open_patch_d931c21c(
    height_value: Integer,
    width_value: Integer,
    steps: Integer,
) -> Indices:
    x0 = make_cycle_patch_d931c21c(height_value, width_value, steps)
    x1 = []
    for x2 in x0:
        x3 = difference(x0, initset(x2))
        if is_open_path_d931c21c(x3):
            x1.append(normalize(x3))
    if len(x1) == ZERO:
        x4 = remove(last(totuple(x0)), x0)
        x0 = normalize(x4)
    else:
        x0 = choice(tuple(x1))
    x5 = randint(ZERO, increment(steps))
    return mutate_shape_d931c21c(x0, is_open_path_d931c21c, x5)


def _interior_cells_d931c21c(
    patch: Patch,
) -> Indices:
    x0 = _as_local_patch_d931c21c(patch)
    x1, x2 = shape(x0)
    x3 = add(double(x1), ONE)
    x4 = add(double(x2), ONE)
    x5 = set()
    for x6, x7 in x0:
        x8 = increment(double(x6))
        x9 = increment(double(x7))
        x5.add((x8, x9))
        for x10, x11 in dneighbors((x6, x7)):
            if (x10, x11) in x0:
                x5.add((add(x8, subtract(x10, x6)), add(x9, subtract(x11, x7))))
    x12 = deque()
    x13 = set()
    for x14 in range(x3):
        for x15 in (ZERO, decrement(x4)):
            if (x14, x15) in x5 or (x14, x15) in x13:
                continue
            x13.add((x14, x15))
            x12.append((x14, x15))
    for x16 in range(x4):
        for x17 in (ZERO, decrement(x3)):
            if (x17, x16) in x5 or (x17, x16) in x13:
                continue
            x13.add((x17, x16))
            x12.append((x17, x16))
    while len(x12) > ZERO:
        x18, x19 = x12.popleft()
        for x20, x21 in dneighbors((x18, x19)):
            if not (ZERO <= x20 < x3 and ZERO <= x21 < x4):
                continue
            if (x20, x21) in x5 or (x20, x21) in x13:
                continue
            x13.add((x20, x21))
            x12.append((x20, x21))
    x22 = set()
    for x23 in range(x1):
        for x24 in range(x2):
            if (x23, x24) in x0:
                continue
            x25 = (increment(double(x23)), increment(double(x24)))
            if x25 not in x13:
                x22.add((x23, x24))
    return frozenset(x22)


def cycle_bands_d931c21c(
    patch: Patch,
) -> Tuple:
    x0 = _as_local_patch_d931c21c(patch)
    x1 = _interior_cells_d931c21c(x0)
    x2 = mapply(neighbors, x0)
    x3 = intersection(x1, x2)
    x4 = difference(x2, x3)
    return x3, x4
