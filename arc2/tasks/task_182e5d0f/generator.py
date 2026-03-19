from arc2.core import *


def _transform_point_182e5d0f(
    loc: IntegerTuple,
    dims: IntegerTuple,
    variant: int,
) -> tuple[IntegerTuple, IntegerTuple]:
    h, w = dims
    i, j = loc
    if variant == ZERO:
        return (i, j), (h, w)
    if variant == ONE:
        return (j, subtract(h, ONE) - i), (w, h)
    if variant == TWO:
        return (subtract(h, ONE) - i, subtract(w, ONE) - j), (h, w)
    if variant == THREE:
        return (subtract(w, ONE) - j, i), (w, h)
    if variant == FOUR:
        return (subtract(h, ONE) - i, j), (h, w)
    if variant == FIVE:
        return (i, subtract(w, ONE) - j), (h, w)
    if variant == SIX:
        return (j, i), (w, h)
    return (subtract(w, ONE) - j, subtract(h, ONE) - i), (w, h)


def _transform_patch_182e5d0f(
    patch: Indices,
    dims: IntegerTuple,
    variant: int,
) -> tuple[Indices, IntegerTuple]:
    out = set()
    new_dims = dims
    for loc in patch:
        new_loc, new_dims = _transform_point_182e5d0f(loc, dims, variant)
        out.add(new_loc)
    return frozenset(out), new_dims


def _translate_point_182e5d0f(
    loc: IntegerTuple,
    offset: IntegerTuple,
) -> IntegerTuple:
    return add(loc, offset)


def _direct_halo_182e5d0f(
    patch: Indices,
    dims: IntegerTuple,
) -> Indices:
    h, w = dims
    out = set(patch)
    for loc in patch:
        for nloc in dneighbors(loc):
            ni, nj = nloc
            if 0 <= ni < h and 0 <= nj < w:
                out.add(nloc)
    return frozenset(out)


def _make_pattern_182e5d0f(
    arm_a: int,
    arm_b: int,
    marked: bool,
    variant: int,
) -> dict:
    dims = (arm_b + THREE, arm_a + TWO)
    special = (ONE, ZERO)
    bend = (ONE, arm_a)
    far = (arm_b + ONE, arm_a)
    inward = (ONE, ONE)
    zeros = frozenset({ORIGIN, (TWO, ZERO)})
    path = connect(special, bend) | connect(bend, far)
    attached = initset((arm_b + ONE, arm_a + ONE)) if marked else frozenset()
    full = combine(path, combine(zeros, attached))
    path, new_dims = _transform_patch_182e5d0f(path, dims, variant)
    zeros, _ = _transform_patch_182e5d0f(zeros, dims, variant)
    attached, _ = _transform_patch_182e5d0f(attached, dims, variant)
    full, _ = _transform_patch_182e5d0f(full, dims, variant)
    special, _ = _transform_point_182e5d0f(special, dims, variant)
    inward, _ = _transform_point_182e5d0f(inward, dims, variant)
    return {
        "dims": new_dims,
        "full": full,
        "path": path,
        "zeros": zeros,
        "attached": attached,
        "special": special,
        "inward": inward,
        "marked": marked,
    }


def _place_pattern_182e5d0f(
    pattern: dict,
    dims: IntegerTuple,
    blocked: Indices,
) -> dict | None:
    h, w = dims
    ph, pw = pattern["dims"]
    if ph > h or pw > w:
        return None
    offsets = [(i, j) for i in range(h - ph + ONE) for j in range(w - pw + ONE)]
    shuffle(offsets)
    for offset in offsets:
        full = shift(pattern["full"], offset)
        halo = _direct_halo_182e5d0f(full, dims)
        if len(intersection(halo, blocked)) > ZERO:
            continue
        placed = {}
        for key, value in pattern.items():
            if key in {"dims", "marked"}:
                placed[key] = value
            elif isinstance(value, frozenset):
                placed[key] = shift(value, offset)
            else:
                placed[key] = _translate_point_182e5d0f(value, offset)
        placed["halo"] = halo
        return placed
    return None


def _place_isolated_fives_182e5d0f(
    count: int,
    dims: IntegerTuple,
    blocked: Indices,
) -> tuple[tuple[IntegerTuple, ...], Indices] | None:
    h, w = dims
    cells = [(i, j) for i in range(h) for j in range(w)]
    shuffle(cells)
    out = []
    for loc in cells:
        halo = _direct_halo_182e5d0f(initset(loc), dims)
        if len(intersection(halo, blocked)) > ZERO:
            continue
        out.append(loc)
        blocked = combine(blocked, halo)
        if len(out) == count:
            return tuple(out), blocked
    return None


def generate_182e5d0f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    variants = tuple(range(EIGHT))
    arm_a_choices = (ONE, ONE, ONE, TWO, TWO, THREE)
    while True:
        side = unifint(diff_lb, diff_ub, (NINE, 15))
        dims = (side, side)
        obj_max = THREE if side < 11 else FOUR
        obj_count = unifint(diff_lb, diff_ub, (ONE, obj_max))
        marked_count = unifint(diff_lb, diff_ub, (ONE, obj_count))
        marked_flags = [T] * marked_count + [F] * (obj_count - marked_count)
        shuffle(marked_flags)
        blocked = frozenset()
        placed = []
        success = T
        for marked in marked_flags:
            arm_a = choice(arm_a_choices)
            max_arm_b = min(EIGHT, subtract(side, FIVE))
            arm_b = unifint(diff_lb, diff_ub, (ONE, max_arm_b))
            pattern = _make_pattern_182e5d0f(arm_a, arm_b, marked, choice(variants))
            candidate = _place_pattern_182e5d0f(pattern, dims, blocked)
            if candidate is None:
                success = F
                break
            placed.append(candidate)
            blocked = combine(blocked, candidate["halo"])
        if flip(success):
            continue
        isolated_count = obj_count - marked_count
        isolated = tuple()
        if positive(isolated_count):
            isolated_data = _place_isolated_fives_182e5d0f(isolated_count, dims, blocked)
            if isolated_data is None:
                continue
            isolated, blocked = isolated_data
        gi = canvas(SEVEN, dims)
        go = canvas(SEVEN, dims)
        for item in placed:
            gi = fill(gi, ZERO, item["zeros"])
            go = fill(go, ZERO, item["zeros"])
            gi = fill(gi, THREE, item["path"])
            if item["marked"]:
                gi = fill(gi, FIVE, item["attached"])
                go = fill(go, THREE, initset(item["special"]))
                go = fill(go, FIVE, initset(item["inward"]))
            else:
                go = fill(go, THREE, item["path"])
        for loc in isolated:
            gi = fill(gi, FIVE, initset(loc))
            go = fill(go, FIVE, initset(loc))
        if equality(gi, go):
            continue
        return {"input": gi, "output": go}
