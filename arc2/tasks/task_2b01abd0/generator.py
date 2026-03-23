from arc2.core import *

from .verifier import verify_2b01abd0


ACCENT_COUNTS_2B01ABD0 = (ONE, ONE, ONE, TWO, TWO, THREE, FOUR)


def _connected_2b01abd0(
    patch: frozenset[IntegerTuple],
    dims: IntegerTuple,
) -> Boolean:
    if len(patch) == ZERO:
        return F
    grid = fill(canvas(ZERO, dims), TWO, patch)
    return equality(size(objects(grid, T, F, T)), ONE)


def _touches_box_2b01abd0(
    patch: frozenset[IntegerTuple],
    h: Integer,
    w: Integer,
) -> Boolean:
    rows = {i for i, _ in patch}
    cols = {j for _, j in patch}
    return (
        ZERO in rows
        and decrement(h) in rows
        and ZERO in cols
        and decrement(w) in cols
    )


def _build_patch_2b01abd0(
    h: Integer,
    w: Integer,
    diff_lb: float,
    diff_ub: float,
) -> frozenset[IntegerTuple] | None:
    area = h * w
    lower = max(SIX, divide(add(area, ONE), TWO))
    universe = frozenset((i, j) for i in range(h) for j in range(w))
    for _ in range(12):
        target = unifint(diff_lb, diff_ub, (lower, area))
        patch = set(universe)
        candidates = list(universe)
        shuffle(candidates)
        for loc in candidates:
            if len(patch) <= target:
                break
            trial = frozenset(patch - {loc})
            if not _touches_box_2b01abd0(trial, h, w):
                continue
            if not _connected_2b01abd0(trial, (h, w)):
                continue
            patch = set(trial)
        patch = frozenset(patch)
        if len(patch) != target:
            continue
        if not _touches_box_2b01abd0(patch, h, w):
            continue
        if not _connected_2b01abd0(patch, (h, w)):
            continue
        return patch
    return None


def _paint_pattern_2b01abd0(
    grid: Grid,
    patch: frozenset[IntegerTuple],
    offset: IntegerTuple,
    major: Integer,
    minor: Integer,
    minor_count: Integer,
) -> Grid:
    shifted = shift(patch, offset)
    cells = tuple(shifted)
    accents = frozenset(sample(cells, minor_count))
    mains = frozenset(loc for loc in shifted if loc not in accents)
    grid = fill(grid, major, mains)
    grid = fill(grid, minor, accents)
    return grid


def generate_2b01abd0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        horizontal = choice((T, F))
        ph = unifint(diff_lb, diff_ub, (THREE, SIX))
        pw = unifint(diff_lb, diff_ub, (THREE, SEVEN))
        patch = _build_patch_2b01abd0(ph, pw, diff_lb, diff_ub)
        if patch is None:
            continue
        colors = sample(tuple(range(TWO, TEN)), 2)
        major, minor = colors
        max_minor = min(FOUR, max(ONE, halve(decrement(len(patch)))))
        minor_count = choice(tuple(v for v in ACCENT_COUNTS_2B01ABD0 if v <= max_minor))
        if horizontal:
            top_margin = randint(ZERO, SIX)
            bottom_margin = randint(ZERO, SIX)
            axis = add(top_margin, increment(ph))
            h = add(add(top_margin, bottom_margin), add(double(ph), THREE))
            left_margin = randint(ZERO, SIX)
            right_margin = randint(ZERO, SIX)
            w = add(add(left_margin, right_margin), pw)
            upper_side = choice((T, F))
            start_i = branch(upper_side, top_margin, add(axis, TWO))
            start_j = left_margin
            gi = canvas(ZERO, (h, w))
            gi = fill(gi, ONE, hfrontier((axis, ZERO)))
        else:
            left_margin = randint(ZERO, SIX)
            right_margin = randint(ZERO, SIX)
            axis = add(left_margin, increment(pw))
            w = add(add(left_margin, right_margin), add(double(pw), THREE))
            top_margin = randint(ZERO, SIX)
            bottom_margin = randint(ZERO, SIX)
            h = add(add(top_margin, bottom_margin), ph)
            left_side = choice((T, F))
            start_i = top_margin
            start_j = branch(left_side, left_margin, add(axis, TWO))
            gi = canvas(ZERO, (h, w))
            gi = fill(gi, ONE, vfrontier((ZERO, axis)))
        gi = _paint_pattern_2b01abd0(gi, patch, (start_i, start_j), major, minor, minor_count)
        go = verify_2b01abd0(gi)
        if go == gi:
            continue
        return {"input": gi, "output": go}
