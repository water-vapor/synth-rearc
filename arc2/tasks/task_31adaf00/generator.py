from arc2.core import *

from .verifier import verify_31adaf00


GRID_SHAPE_31ADAF00 = (TEN, TEN)
SQUARE_COUNT_BOUNDS_31ADAF00 = (THREE, FIVE)
THREE_SQUARE_COUNT_BOUNDS_31ADAF00 = (ZERO, TWO)
FIVE_COUNT_BOUNDS_31ADAF00 = (35, 45)
MIN_FILLED_AREA_31ADAF00 = 20
LAYOUT_ATTEMPTS_31ADAF00 = 256
PLACEMENT_ATTEMPTS_31ADAF00 = 128


def _square_patch_31adaf00(
    top: Integer,
    left: Integer,
    side: Integer,
) -> Indices:
    return product(interval(top, add(top, side), ONE), interval(left, add(left, side), ONE))


def _window_patch_31adaf00(
    top: Integer,
    left: Integer,
) -> Indices:
    return _square_patch_31adaf00(top, left, TWO)


def _forbidden_patch_31adaf00(
    patch: Indices,
) -> Indices:
    x0 = set(toindices(patch))
    x1, x2 = GRID_SHAPE_31ADAF00
    for x3 in patch:
        for x4, x5 in dneighbors(x3):
            if 0 <= x4 < x1 and 0 <= x5 < x2:
                x0.add((x4, x5))
    return frozenset(x0)


def _sample_layout_31adaf00(
    diff_lb: float,
    diff_ub: float,
) -> Tuple | None:
    x0, x1 = GRID_SHAPE_31ADAF00
    for _ in range(LAYOUT_ATTEMPTS_31ADAF00):
        x2 = unifint(diff_lb, diff_ub, SQUARE_COUNT_BOUNDS_31ADAF00)
        x3 = min(unifint(diff_lb, diff_ub, THREE_SQUARE_COUNT_BOUNDS_31ADAF00), subtract(x2, ONE))
        x4 = [THREE] * x3 + [TWO] * subtract(x2, x3)
        if sum(multiply(x5, x5) for x5 in x4) < MIN_FILLED_AREA_31ADAF00:
            continue
        shuffle(x4)
        x5 = []
        x6 = frozenset()
        x7 = frozenset()
        x8 = T
        for x9 in x4:
            x10 = F
            for _ in range(PLACEMENT_ATTEMPTS_31ADAF00):
                x11 = randint(ZERO, subtract(x0, x9))
                x12 = randint(ZERO, subtract(x1, x9))
                x13 = _square_patch_31adaf00(x11, x12, x9)
                if size(intersection(x13, x7)) != ZERO:
                    continue
                x5.append((x11, x12, x9, x13))
                x6 = combine(x6, x13)
                x7 = combine(x7, _forbidden_patch_31adaf00(x13))
                x10 = T
                break
            if x10:
                continue
            x8 = F
            break
        if x8:
            return tuple(x5)
    return None


def _allowed_windows_31adaf00(
    specs: Tuple,
) -> FrozenSet:
    x0 = set()
    for x1, x2, x3, _ in specs:
        x4 = subtract(add(x1, x3), ONE)
        x5 = subtract(add(x2, x3), ONE)
        for x6 in interval(x1, x4, ONE):
            for x7 in interval(x2, x5, ONE):
                x0.add((x6, x7))
    return frozenset(x0)


def _cover_windows_31adaf00(
    protected: Indices,
    allowed_windows: FrozenSet,
) -> Indices | None:
    x0 = {}
    x1 = {}
    for x2 in interval(ZERO, NINE, ONE):
        for x3 in interval(ZERO, NINE, ONE):
            x4 = (x2, x3)
            if contained(x4, allowed_windows):
                continue
            x5 = _window_patch_31adaf00(x2, x3)
            x6 = difference(x5, protected)
            if size(x6) == ZERO:
                return None
            x0[x4] = tuple(x6)
            for x7 in x6:
                if x7 not in x1:
                    x1[x7] = set()
                x1[x7].add(x4)
    x8 = set(x0.keys())
    x9 = set()
    while len(x8) > ZERO:
        x10 = choice(tuple(x8))
        x11 = x0[x10]
        x12 = []
        x13 = ZERO
        for x14 in x11:
            x15 = len(x8 & x1[x14])
            if x15 > x13:
                x12 = [x14]
                x13 = x15
            elif x15 == x13:
                x12.append(x14)
        x16 = choice(tuple(x12))
        x9.add(x16)
        x8 -= x1[x16]
    return frozenset(x9)


def _render_input_31adaf00(
    protected: Indices,
    blockers: Indices,
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    x0 = canvas(ZERO, GRID_SHAPE_31ADAF00)
    x1 = max(size(blockers), unifint(diff_lb, diff_ub, FIVE_COUNT_BOUNDS_31ADAF00))
    x2 = difference(difference(asindices(x0), protected), blockers)
    x3 = min(subtract(x1, size(blockers)), size(x2))
    x4 = frozenset()
    if x3 > ZERO:
        x4 = frozenset(sample(tuple(x2), x3))
    x5 = combine(blockers, x4)
    return fill(x0, FIVE, x5)


def _render_output_31adaf00(
    gi: Grid,
    specs: Tuple,
) -> Grid:
    x0 = tuple(x3 for _, _, _, x3 in specs)
    x1 = merge(x0)
    return fill(gi, ONE, x1)


def generate_31adaf00(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _sample_layout_31adaf00(diff_lb, diff_ub)
        if x0 is None:
            continue
        x1 = merge(tuple(x3 for _, _, _, x3 in x0))
        x2 = _allowed_windows_31adaf00(x0)
        x3 = _cover_windows_31adaf00(x1, x2)
        if x3 is None:
            continue
        x4 = _render_input_31adaf00(x1, x3, diff_lb, diff_ub)
        x5 = _render_output_31adaf00(x4, x0)
        if verify_31adaf00(x4) != x5:
            continue
        return {"input": x4, "output": x5}
