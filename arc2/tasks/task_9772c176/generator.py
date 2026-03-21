from arc2.core import *


GRID_BOUNDS_9772C176 = (20, 29)


def _yellow_patch_9772c176(
    patch: Indices,
    dims: IntegerTuple,
) -> Indices:
    h, w = dims
    rows = {}
    cols = {}
    for i, j in patch:
        rows.setdefault(i, []).append(j)
        cols.setdefault(j, []).append(i)
    out = set()
    top = min(rows)
    bottom = max(rows)
    left = min(cols)
    right = max(cols)
    lft = min(rows[top])
    rgt = max(rows[top])
    step = ONE
    while top - step >= ZERO and lft + step <= rgt - step:
        ii = top - step
        for jj in range(lft + step, rgt - step + ONE):
            out.add((ii, jj))
        step += ONE
    lft = min(rows[bottom])
    rgt = max(rows[bottom])
    step = ONE
    while bottom + step < h and lft + step <= rgt - step:
        ii = bottom + step
        for jj in range(lft + step, rgt - step + ONE):
            out.add((ii, jj))
        step += ONE
    topc = min(cols[left])
    botc = max(cols[left])
    step = ONE
    while left - step >= ZERO and topc + step <= botc - step:
        jj = left - step
        for ii in range(topc + step, botc - step + ONE):
            out.add((ii, jj))
        step += ONE
    topc = min(cols[right])
    botc = max(cols[right])
    step = ONE
    while right + step < w and topc + step <= botc - step:
        jj = right + step
        for ii in range(topc + step, botc - step + ONE):
            out.add((ii, jj))
        step += ONE
    return frozenset(out)


def _reserve_patch_9772c176(
    patch: Indices,
    dims: IntegerTuple,
) -> Indices:
    if len(patch) == ZERO:
        return frozenset()
    h, w = dims
    top = max(ZERO, decrement(uppermost(patch)))
    bottom = min(decrement(h), increment(lowermost(patch)))
    left = max(ZERO, decrement(leftmost(patch)))
    right = min(decrement(w), increment(rightmost(patch)))
    return frozenset(
        (i, j)
        for i in range(top, bottom + ONE)
        for j in range(left, right + ONE)
    )


def _profile_patch_9772c176(
    width_box: Integer,
    top_ramp: Integer,
    plateau: Integer,
    bottom_ramp: Integer,
) -> Indices:
    widths = tuple()
    for k in range(top_ramp):
        widths = widths + (subtract(width_box, double(subtract(top_ramp, k))),)
    widths = widths + repeat(width_box, plateau)
    for k in range(bottom_ramp):
        widths = widths + (subtract(width_box, double(increment(k))),)
    patch = set()
    for i, width_value in enumerate(widths):
        left = divide(subtract(width_box, width_value), TWO)
        right = add(left, subtract(width_value, ONE))
        for j in range(left, right + ONE):
            patch.add((i, j))
    return frozenset(patch)


def _sample_profile_9772c176(
    large: Boolean,
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    while True:
        if large:
            half_w = unifint(diff_lb, diff_ub, (FIVE, EIGHT))
            top_ramp = unifint(diff_lb, diff_ub, (ONE, FIVE))
            bottom_ramp = unifint(diff_lb, diff_ub, (ONE, FIVE))
            plateau = unifint(diff_lb, diff_ub, (THREE, EIGHT))
        else:
            half_w = unifint(diff_lb, diff_ub, (THREE, SIX))
            top_ramp = unifint(diff_lb, diff_ub, (ONE, FOUR))
            bottom_ramp = unifint(diff_lb, diff_ub, (ONE, FOUR))
            plateau = unifint(diff_lb, diff_ub, (TWO, FIVE))
        width_box = add(double(half_w), ONE)
        if subtract(width_box, double(top_ramp)) < THREE:
            continue
        if subtract(width_box, double(bottom_ramp)) < THREE:
            continue
        patch = _profile_patch_9772c176(width_box, top_ramp, plateau, bottom_ramp)
        if height(patch) < FIVE or width(patch) < FIVE:
            continue
        return patch


def _sample_offset_9772c176(
    patch: Indices,
    dims: IntegerTuple,
    region: str,
) -> IntegerTuple | None:
    h, w = dims
    hp = height(patch)
    wp = width(patch)
    if hp >= h or wp >= w:
        return None
    max_top = subtract(h, hp)
    max_left = subtract(w, wp)
    if region == "ul":
        top_hi = min(max_top, divide(h, THREE))
        left_hi = min(max_left, divide(w, THREE))
        top = choice((ZERO, randint(ZERO, top_hi)))
        left = choice((ZERO, randint(ZERO, left_hi)))
        return astuple(top, left)
    top_lo = max(ZERO, subtract(max_top, divide(h, THREE)))
    left_lo = max(ZERO, subtract(max_left, divide(w, THREE)))
    top = choice((max_top, randint(top_lo, max_top)))
    left = choice((max_left, randint(left_lo, max_left)))
    return astuple(top, left)


def _place_component_9772c176(
    gi: Grid,
    go: Grid,
    patch: Indices,
    dims: IntegerTuple,
    region: str,
    occupied: Indices,
) -> tuple[Grid, Grid, Indices] | None:
    for _ in range(300):
        offset = _sample_offset_9772c176(patch, dims, region)
        if offset is None:
            return None
        input_patch = shift(patch, offset)
        yellow_patch = _yellow_patch_9772c176(input_patch, dims)
        full_patch = combine(input_patch, yellow_patch)
        reserve = _reserve_patch_9772c176(full_patch, dims)
        if len(intersection(reserve, occupied)) > ZERO:
            continue
        gi = fill(gi, EIGHT, input_patch)
        go = fill(go, EIGHT, input_patch)
        go = fill(go, FOUR, yellow_patch)
        occupied = combine(occupied, reserve)
        return gi, go, occupied
    return None


def generate_9772c176(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = unifint(diff_lb, diff_ub, GRID_BOUNDS_9772C176)
        w = unifint(diff_lb, diff_ub, GRID_BOUNDS_9772C176)
        dims = astuple(h, w)
        gi = canvas(ZERO, dims)
        go = canvas(ZERO, dims)
        occupied = frozenset()
        x0 = _sample_profile_9772c176(T, diff_lb, diff_ub)
        x1 = _sample_profile_9772c176(F, diff_lb, diff_ub)
        x2 = _place_component_9772c176(gi, go, x0, dims, "ul", occupied)
        if x2 is None:
            continue
        gi, go, occupied = x2
        x3 = _place_component_9772c176(gi, go, x1, dims, "lr", occupied)
        if x3 is None:
            continue
        gi, go, occupied = x3
        if gi == go:
            continue
        return {"input": gi, "output": go}
