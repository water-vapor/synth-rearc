from arc2.core import *


NONZERO_COLORS_73CCF9C2 = (ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)


def _connected_patch_73ccf9c2(
    patch: frozenset[tuple[int, int]] | set[tuple[int, int]],
) -> bool:
    if len(patch) == ZERO:
        return F
    x0 = next(iter(patch))
    x1 = {x0}
    x2 = [x0]
    while len(x2) > ZERO:
        x3 = x2.pop()
        x4 = {
            x5 for x5 in neighbors(x3)
            if x5 in patch and x5 not in x1
        }
        x1.update(x4)
        x2.extend(x4)
    return len(x1) == len(patch)


def _covers_bbox_73ccf9c2(
    patch: frozenset[tuple[int, int]] | set[tuple[int, int]],
    height_: Integer,
    width_: Integer,
) -> bool:
    x0 = {i for i, _ in patch}
    x1 = {j for _, j in patch}
    return len(x0) == height_ and len(x1) == width_


def _expand_half_row_73ccf9c2(
    row: frozenset[int] | set[int],
    width_: Integer,
) -> frozenset[int]:
    x0 = []
    for j in row:
        x0.append(j)
        x1 = width_ - j - ONE
        if x1 != j:
            x0.append(x1)
    return frozenset(x0)


def _random_half_row_73ccf9c2(
    half_width: Integer,
) -> frozenset[int]:
    while True:
        x0 = {j for j in range(half_width) if choice((T, F))}
        if len(x0) == ZERO:
            x0.add(randint(ZERO, half_width - ONE))
        if len(x0) == half_width and choice((T, F)):
            x0.remove(randint(ZERO, half_width - ONE))
        if len(x0) > ZERO:
            return frozenset(x0)


def _step_half_row_73ccf9c2(
    row: frozenset[int],
    half_width: Integer,
) -> frozenset[int]:
    x0 = set(row)
    for _ in range(randint(ONE, TWO)):
        x1 = randint(ZERO, half_width - ONE)
        if x1 in x0 and len(x0) > ONE and choice((T, F)):
            x0.remove(x1)
        else:
            x0.add(x1)
    if choice((T, F)):
        x2 = randint(ZERO, half_width - ONE)
        x3 = x2 + choice((-ONE, ONE))
        if ZERO <= x3 < half_width:
            if x2 in x0 and len(x0) > ONE:
                x0.remove(x2)
            x0.add(x3)
    if len(x0) == ZERO:
        x0.add(randint(ZERO, half_width - ONE))
    return frozenset(x0)


def _rows_to_patch_73ccf9c2(
    rows: tuple[frozenset[int], ...],
    width_: Integer,
) -> frozenset[tuple[int, int]]:
    x0 = set()
    for i, row in enumerate(rows):
        for j in _expand_half_row_73ccf9c2(row, width_):
            x0.add((i, j))
    return frozenset(x0)


def _symmetric_patch_73ccf9c2(
    diff_lb: float,
    diff_ub: float,
) -> frozenset[tuple[int, int]]:
    while True:
        x0 = unifint(diff_lb, diff_ub, (THREE, SIX))
        x1 = unifint(diff_lb, diff_ub, (FOUR, EIGHT))
        x2 = divide(x1 + ONE, TWO)
        x3 = [_random_half_row_73ccf9c2(x2)]
        for _ in range(x0 - ONE):
            x4 = x3[-ONE]
            if choice((T, T, F)):
                x5 = _step_half_row_73ccf9c2(x4, x2)
            else:
                x5 = _random_half_row_73ccf9c2(x2)
            x3.append(x5)
        x6 = tuple(x3)
        x7 = _rows_to_patch_73ccf9c2(x6, x1)
        if len(set(x6)) == ONE:
            continue
        if len(x7) == x0 * x1:
            continue
        if not _covers_bbox_73ccf9c2(x7, x0, x1):
            continue
        if not _connected_patch_73ccf9c2(x7):
            continue
        return x7


def _asymmetrize_patch_73ccf9c2(
    patch: frozenset[tuple[int, int]],
) -> frozenset[tuple[int, int]] | None:
    x0 = height(patch)
    x1 = width(patch)
    x2 = set(patch)
    x3 = (
        interval(ZERO, divide(x1, TWO), ONE),
        interval(divide(x1 + ONE, TWO), x1, ONE),
    )
    x4 = list(x3)
    shuffle(x4)
    for x5 in x4:
        x6 = set(x2)
        x7 = ZERO
        x8 = randint(ONE, THREE)
        for _ in range(x8):
            x9 = []
            for i in range(x0):
                for j in x5:
                    x9.append(("add", (i, j)))
                    if (i, j) in x6:
                        x9.append(("remove", (i, j)))
            shuffle(x9)
            x10 = F
            for x11, x12 in x9:
                x13 = set(x6)
                if x11 == "add":
                    x13.add(x12)
                else:
                    x13.remove(x12)
                if not _covers_bbox_73ccf9c2(x13, x0, x1):
                    continue
                if not _connected_patch_73ccf9c2(x13):
                    continue
                x14 = frozenset(x13)
                if x14 == vmirror(x14):
                    continue
                x6 = x13
                x7 += ONE
                x10 = T
                break
            if not x10:
                break
        x15 = frozenset(x6)
        if x7 > ZERO and x15 != vmirror(x15):
            return x15
    return None


def _asymmetric_patch_73ccf9c2(
    diff_lb: float,
    diff_ub: float,
) -> frozenset[tuple[int, int]]:
    while True:
        x0 = _symmetric_patch_73ccf9c2(diff_lb, diff_ub)
        if not FOUR <= height(x0) <= SEVEN:
            continue
        if not FOUR <= width(x0) <= SEVEN:
            continue
        x1 = _asymmetrize_patch_73ccf9c2(x0)
        if x1 is not None:
            return x1


def _halo_73ccf9c2(
    patch: Patch,
) -> Indices:
    x0 = uppermost(patch)
    x1 = leftmost(patch)
    x2 = lowermost(patch)
    x3 = rightmost(patch)
    x4 = interval(x0 - ONE, x2 + TWO, ONE)
    x5 = interval(x1 - ONE, x3 + TWO, ONE)
    return product(x4, x5)


def generate_73ccf9c2(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (20, 23))
        x1 = choice(NONZERO_COLORS_73CCF9C2)
        x2 = tuple(_symmetric_patch_73ccf9c2(diff_lb, diff_ub) for _ in range(THREE))
        x3 = _asymmetric_patch_73ccf9c2(diff_lb, diff_ub)
        x4 = list(combine(x2, (x3,)))
        shuffle(x4)
        x5 = canvas(ZERO, (x0, x0))
        x6 = frozenset()
        x7 = None
        x8 = True
        for x9 in x4:
            x10 = height(x9)
            x11 = width(x9)
            if x10 + TWO >= x0 or x11 + TWO >= x0:
                x8 = F
                break
            x12 = False
            for _ in range(200):
                x13 = randint(ONE, x0 - x10 - ONE)
                x14 = randint(ONE, x0 - x11 - ONE)
                x15 = shift(x9, (x13, x14))
                x16 = _halo_73ccf9c2(x15)
                if len(intersection(x16, x6)) != ZERO:
                    continue
                x5 = fill(x5, x1, x15)
                x6 = combine(x6, x16)
                if x9 == x3:
                    x7 = x15
                x12 = T
                break
            if not x12:
                x8 = F
                break
        if not x8 or x7 is None:
            continue
        x17 = subgrid(toobject(x7, x5), x5)
        x18 = choice((identity, hmirror, vmirror, rot180))
        x19 = x18(x5)
        x20 = x18(x17)
        if x19 == x20:
            continue
        return {"input": x19, "output": x20}
