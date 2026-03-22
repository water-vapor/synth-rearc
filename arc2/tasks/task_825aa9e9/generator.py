from arc2.core import *


def _support_from_profile_825aa9e9(
    dims: IntegerTuple,
    heights: tuple[int, ...],
) -> Indices:
    h, _ = dims
    out = set()
    for j, height0 in enumerate(heights):
        for i in range(subtract(h, height0), h):
            out.add((i, j))
    return frozenset(out)


def _profile_segments_825aa9e9(
    width0: int,
    count: int,
) -> tuple[int, ...]:
    if count == ONE:
        return (width0,)
    cuts = sorted(sample(range(ONE, width0), count - ONE))
    points = (ZERO,) + tuple(cuts) + (width0,)
    return tuple(b - a for a, b in zip(points, points[ONE:]))


def _posts_profile_825aa9e9(
    dims: IntegerTuple,
) -> tuple[int, ...]:
    h, w = dims
    base = choice((ZERO, ZERO, ONE, ONE))
    out = [base] * w
    count = randint(TWO, max(TWO, min(w, add(w // THREE, ONE))))
    for j in sample(range(w), count):
        out[j] = choice((ONE, ONE, TWO, THREE, h))
    if maximum(out) == ZERO:
        out[randint(ZERO, subtract(w, ONE))] = ONE
    if base == ONE and w > FOUR and flip(choice((T, F))):
        out[choice((ZERO, subtract(w, ONE)))] = h
    return tuple(min(h, value) for value in out)


def _step_profile_825aa9e9(
    dims: IntegerTuple,
) -> tuple[int, ...]:
    h, w = dims
    count = randint(TWO, min(FIVE, w))
    widths = _profile_segments_825aa9e9(w, count)
    cur = choice((ZERO, ZERO, ONE, ONE, TWO))
    vals = []
    for _ in widths:
        cur = min(h, add(cur, choice((ZERO, ZERO, ONE, ONE, TWO))))
        vals.append(cur)
    if maximum(vals) == ZERO:
        vals[-ONE] = ONE
    if flip(choice((T, F))):
        vals[-ONE] = h
    if flip(choice((T, F))):
        vals = vals[::-1]
    out = []
    for width0, value in zip(widths, vals):
        out.extend([value] * width0)
    return tuple(out)


def _basin_profile_825aa9e9(
    dims: IntegerTuple,
) -> tuple[int, ...]:
    h, w = dims
    left_w = randint(ONE, max(ONE, w // THREE))
    right_w = randint(ONE, max(ONE, w // THREE))
    mid_w = subtract(w, add(left_w, right_w))
    if mid_w <= ZERO:
        return _step_profile_825aa9e9(dims)
    high_a = randint(max(TWO, h // TWO), h)
    high_b = randint(max(TWO, h // TWO), h)
    low = randint(ZERO, min(subtract(high_a, ONE), subtract(high_b, ONE)))
    out = [high_a] * left_w + [low] * mid_w + [high_b] * right_w
    if flip(choice((T, F))):
        out = out[::-1]
    return tuple(out)


def _make_profile_825aa9e9(
    dims: IntegerTuple,
) -> tuple[int, ...]:
    style = choice(
        (
            "posts",
            "posts",
            "posts",
            "step",
            "step",
            "step",
            "basin",
            "basin",
        )
    )
    if style == "posts":
        return _posts_profile_825aa9e9(dims)
    if style == "basin":
        return _basin_profile_825aa9e9(dims)
    return _step_profile_825aa9e9(dims)


def _frame_825aa9e9(
    h: int,
    w: int,
) -> Indices:
    if h < THREE or w < THREE:
        return frozenset((i, j) for i in range(h) for j in range(w))
    return box(frozenset((i, j) for i in range(h) for j in range(w)))


def _el_825aa9e9(
    h: int,
    w: int,
) -> Indices:
    return connect((ZERO, ZERO), (subtract(h, ONE), ZERO)) | connect(
        (subtract(h, ONE), ZERO), (subtract(h, ONE), subtract(w, ONE))
    )


def _tee_825aa9e9(
    w: int,
    stem: int,
) -> Indices:
    mid = w // TWO
    return connect((ZERO, ZERO), (ZERO, subtract(w, ONE))) | connect(
        (ZERO, mid), (subtract(stem, ONE), mid)
    )


def _frame_tail_825aa9e9(
    tail: int,
) -> Indices:
    return combine(_frame_825aa9e9(THREE, THREE), connect((TWO, ZERO), (add(TWO, tail), ZERO)))


def _block_tail_825aa9e9(
    w: int,
    stem: int,
) -> Indices:
    top = frozenset((i, j) for i in range(TWO) for j in range(w))
    mid = w // TWO
    tail = connect((ONE, mid), (add(stem, ONE), mid))
    return combine(top, tail)


def _shape_transforms_825aa9e9() -> tuple:
    return (
        identity,
        hmirror,
        vmirror,
        compose(hmirror, vmirror),
        dmirror,
        cmirror,
    )


def _make_shape_825aa9e9(
    dims: IntegerTuple,
) -> Indices:
    h, w = dims
    limit_h = max(ONE, min(subtract(h, ONE), SEVEN))
    limit_w = max(ONE, min(subtract(w, ONE), SEVEN))
    kinds = (
        "single",
        "single",
        "line",
        "line",
        "el",
        "el",
        "tee",
        "rect",
        "frame",
        "frame_tail",
        "block_tail",
    )
    transforms = _shape_transforms_825aa9e9()
    while True:
        kind = choice(kinds)
        if kind == "single":
            shape0 = frozenset({ORIGIN})
        elif kind == "line":
            if flip(choice((T, F))):
                length = randint(TWO, limit_h)
                shape0 = frozenset((i, ZERO) for i in range(length))
            else:
                length = randint(TWO, limit_w)
                shape0 = frozenset((ZERO, j) for j in range(length))
        elif kind == "el":
            shape0 = _el_825aa9e9(randint(TWO, limit_h), randint(TWO, limit_w))
        elif kind == "tee":
            if limit_w < THREE:
                continue
            shape0 = _tee_825aa9e9(randint(THREE, limit_w), randint(TWO, limit_h))
        elif kind == "rect":
            shape0 = frozenset(
                (i, j)
                for i in range(randint(TWO, min(limit_h, FOUR)))
                for j in range(randint(TWO, min(limit_w, FOUR)))
            )
        elif kind == "frame":
            if limit_h < THREE or limit_w < THREE:
                continue
            shape0 = _frame_825aa9e9(
                randint(THREE, min(limit_h, FOUR)),
                randint(THREE, min(limit_w, FOUR)),
            )
        elif kind == "frame_tail":
            if limit_h < FOUR or limit_w < THREE:
                continue
            shape0 = _frame_tail_825aa9e9(randint(ONE, subtract(limit_h, THREE)))
        else:
            if limit_h < FOUR or limit_w < THREE:
                continue
            shape0 = _block_tail_825aa9e9(
                randint(THREE, min(limit_w, FIVE)),
                randint(TWO, subtract(limit_h, ONE)),
            )
        shape0 = normalize(choice(transforms)(shape0))
        if height(shape0) <= subtract(h, ONE) and width(shape0) <= w:
            return shape0


def _effective_blocked_825aa9e9(
    dims: IntegerTuple,
    support: Indices,
) -> Indices:
    h, w = dims
    bottom = frozenset((subtract(h, ONE), j) for j in range(w))
    return combine(support, combine(shift(support, UP), bottom))


def _drop_patch_825aa9e9(
    patch: Indices,
    blocked: Indices,
) -> Indices:
    out = patch
    while True:
        nxt = shift(out, DOWN)
        if positive(size(intersection(nxt, blocked))):
            return out
        out = nxt


def _touching_825aa9e9(
    patch: Indices,
    occupied: Indices,
) -> bool:
    if len(occupied) == ZERO:
        return F
    return positive(size(intersection(mapply(dneighbors, patch), occupied)))


def _settle_objects_825aa9e9(
    dims: IntegerTuple,
    support: Indices,
    objects0: tuple[Indices, ...],
) -> tuple[Indices, ...]:
    blocked = _effective_blocked_825aa9e9(dims, support)
    out = []
    for patch in sorted(objects0, key=lowermost, reverse=True):
        dropped = _drop_patch_825aa9e9(patch, blocked)
        out.append(dropped)
        blocked = combine(blocked, dropped)
    return tuple(out)


def _render_825aa9e9(
    dims: IntegerTuple,
    bg: Integer,
    support_color: Integer,
    support: Indices,
    moving_color: Integer,
    objects0: tuple[Indices, ...],
) -> Grid:
    out = canvas(bg, dims)
    out = paint(out, recolor(support_color, support))
    for patch in objects0:
        out = paint(out, recolor(moving_color, patch))
    return out


def generate_825aa9e9(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    colors = tuple(c for c in interval(ONE, TEN, ONE) if c != SEVEN)
    while True:
        h = unifint(diff_lb, diff_ub, (FOUR, TEN))
        w = unifint(diff_lb, diff_ub, (SEVEN, 20))
        dims = (h, w)
        support_color = choice(colors)
        moving_color = choice(tuple(c for c in colors if c != support_color))
        profile = _make_profile_825aa9e9(dims)
        support = _support_from_profile_825aa9e9(dims, profile)
        support_size = size(support)
        if support_size < TWO or greater(support_size, multiply(h, w) * 2 // 3):
            continue
        obj_cap = FOUR if w > TEN else THREE
        obj_count = unifint(diff_lb, diff_ub, (ONE, obj_cap))
        blocked = _effective_blocked_825aa9e9(dims, support)
        settled = []
        success = T
        for _ in range(obj_count):
            placed = None
            for _ in range(200):
                shape0 = _make_shape_825aa9e9(dims)
                sw = width(shape0)
                cols = list(range(add(subtract(w, sw), ONE)))
                shuffle(cols)
                for left in cols:
                    base = shift(shape0, (ZERO, left))
                    if positive(size(intersection(base, support))):
                        continue
                    dropped = _drop_patch_825aa9e9(base, blocked)
                    if positive(size(intersection(dropped, blocked))):
                        continue
                    placed = dropped
                    break
                if placed is not None:
                    break
            if placed is None:
                success = F
                break
            settled.append(placed)
            blocked = combine(blocked, placed)
        if flip(success):
            continue
        settled = tuple(sorted(settled, key=uppermost))
        occupied = set(support)
        moving_occupied = frozenset()
        lifted = [None] * len(settled)
        moved = F
        lift_success = T
        for idx, patch in enumerate(settled):
            lifts = []
            for amount in range(add(uppermost(patch), ONE)):
                candidate = shift(patch, invert(toivec(amount)))
                clear = len(intersection(candidate, occupied)) == ZERO
                separate = flip(_touching_825aa9e9(candidate, moving_occupied))
                if clear and separate:
                    lifts.append(amount)
            if len(lifts) == ZERO:
                lift_success = F
                break
            positive_lifts = [amount for amount in lifts if positive(amount)]
            if positive_lifts and (flip(moved) or flip(choice((T, F, F)))):
                amount = choice(positive_lifts)
                moved = T
            else:
                amount = choice(lifts)
                if positive(amount):
                    moved = T
            candidate = shift(patch, invert(toivec(amount)))
            lifted[idx] = candidate
            occupied |= candidate
            moving_occupied = combine(moving_occupied, candidate)
        if flip(lift_success):
            continue
        lifted = tuple(lifted)
        if flip(moved):
            continue
        gi = _render_825aa9e9(dims, SEVEN, support_color, support, moving_color, lifted)
        go = _render_825aa9e9(dims, SEVEN, support_color, support, moving_color, settled)
        if equality(gi, go):
            continue
        if _settle_objects_825aa9e9(dims, support, lifted) != settled:
            continue
        return {"input": gi, "output": go}
