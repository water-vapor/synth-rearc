from arc2.core import *


def _rect_0d87d2a6(
    top: Integer,
    left: Integer,
    h: Integer,
    w: Integer,
) -> Indices:
    return frozenset((i, j) for i in range(top, top + h) for j in range(left, left + w))


def _buffer_0d87d2a6(
    patch: Indices,
    h: Integer,
    w: Integer,
) -> Indices:
    out = set(patch)
    for cell in patch:
        for neighbor in dneighbors(cell):
            if 0 <= neighbor[ZERO] < h and 0 <= neighbor[ONE] < w:
                out.add(neighbor)
    return frozenset(out)


def _adjacent_to_line_0d87d2a6(
    patch: Indices,
    line: Indices,
) -> Boolean:
    return any(len(intersection(dneighbors(cell), line)) > ZERO for cell in patch)


def _sample_rect_dims_0d87d2a6(
    diff_lb: float,
    diff_ub: float,
    h: Integer,
    w: Integer,
) -> tuple[Integer, Integer]:
    rh = unifint(diff_lb, diff_ub, (TWO, min(FIVE, h)))
    rw = unifint(diff_lb, diff_ub, (TWO, min(EIGHT, w)))
    return rh, rw


def _can_place_0d87d2a6(
    patch: Indices,
    blocked: Indices,
    buffered: Indices,
) -> Boolean:
    return len(intersection(patch, blocked)) == ZERO and len(intersection(patch, buffered)) == ZERO


def _place_touched_rect_0d87d2a6(
    diff_lb: float,
    diff_ub: float,
    h: Integer,
    w: Integer,
    line_specs: tuple[tuple[str, Integer], ...],
    line: Indices,
    endpoints: Indices,
    blocked: Indices,
    buffered: Indices,
) -> Indices | None:
    for _ in range(200):
        rh, rw = _sample_rect_dims_0d87d2a6(diff_lb, diff_ub, h, w)
        axis, value = choice(line_specs)
        if axis == "v":
            top = randint(ZERO, h - rh)
            left_lb = max(ZERO, value - rw + ONE)
            left_ub = min(value, w - rw)
            if left_lb > left_ub:
                continue
            left = randint(left_lb, left_ub)
        else:
            top_lb = max(ZERO, value - rh + ONE)
            top_ub = min(value, h - rh)
            if top_lb > top_ub:
                continue
            top = randint(top_lb, top_ub)
            left = randint(ZERO, w - rw)
        patch = _rect_0d87d2a6(top, left, rh, rw)
        if not _can_place_0d87d2a6(patch, blocked | endpoints, buffered):
            continue
        if len(intersection(patch, line)) == ZERO:
            continue
        return patch
    return None


def _place_untouched_rect_0d87d2a6(
    diff_lb: float,
    diff_ub: float,
    h: Integer,
    w: Integer,
    line: Indices,
    endpoints: Indices,
    blocked: Indices,
    buffered: Indices,
) -> Indices | None:
    for _ in range(200):
        rh, rw = _sample_rect_dims_0d87d2a6(diff_lb, diff_ub, h, w)
        top = randint(ZERO, h - rh)
        left = randint(ZERO, w - rw)
        patch = _rect_0d87d2a6(top, left, rh, rw)
        if not _can_place_0d87d2a6(patch, blocked | endpoints, buffered):
            continue
        if len(intersection(patch, line)) > ZERO:
            continue
        if _adjacent_to_line_0d87d2a6(patch, line):
            continue
        return patch
    return None


def generate_0d87d2a6(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = unifint(diff_lb, diff_ub, (TEN, 24))
        w = unifint(diff_lb, diff_ub, (14, 28))
        gi = canvas(ZERO, (h, w))
        vcol = randint(TWO, w - THREE)
        nh = choice((ZERO, ONE, ONE, TWO))
        row_pool = interval(TWO, h - TWO, ONE)
        if nh > len(row_pool):
            nh = len(row_pool)
        hrows = tuple(sorted(sample(row_pool, nh)))
        endpoints = frozenset({(ZERO, vcol), (h - ONE, vcol)} | {(i, ZERO) for i in hrows} | {(i, w - ONE) for i in hrows})
        vline = frozenset((i, vcol) for i in range(h))
        hlines = frozenset((i, j) for i in hrows for j in range(w))
        line = vline | hlines
        line_specs = (("v", vcol),) + tuple(("h", i) for i in hrows)
        touched_target = randint(ONE, THREE + nh)
        untouched_target = randint(TWO, FIVE)
        touched = []
        untouched = []
        blocked = frozenset()
        buffered = frozenset()
        failed = F
        for _ in range(touched_target):
            patch = _place_touched_rect_0d87d2a6(
                diff_lb,
                diff_ub,
                h,
                w,
                line_specs,
                line,
                endpoints,
                blocked,
                buffered,
            )
            if patch is None:
                failed = T
                break
            touched.append(patch)
            blocked = combine(blocked, patch)
            buffered = combine(buffered, _buffer_0d87d2a6(patch, h, w))
        if failed:
            continue
        for _ in range(untouched_target):
            patch = _place_untouched_rect_0d87d2a6(
                diff_lb,
                diff_ub,
                h,
                w,
                line,
                endpoints,
                blocked,
                buffered,
            )
            if patch is None:
                failed = T
                break
            untouched.append(patch)
            blocked = combine(blocked, patch)
            buffered = combine(buffered, _buffer_0d87d2a6(patch, h, w))
        if failed:
            continue
        if double(size(blocked)) >= h * w - size(endpoints):
            continue
        for patch in touched + untouched:
            gi = fill(gi, TWO, patch)
        gi = fill(gi, ONE, endpoints)
        go = fill(gi, ONE, line)
        for patch in touched:
            go = fill(go, ONE, patch)
        return {"input": gi, "output": go}
