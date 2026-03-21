from arc2.core import *


_PATCH_TRANSFORMS_AA62E3F4 = (
    identity,
    hmirror,
    vmirror,
    dmirror,
    cmirror,
    compose(hmirror, vmirror),
    compose(hmirror, dmirror),
    compose(vmirror, dmirror),
)


def _sample_int_aa62e3f4(
    diff_lb: float,
    diff_ub: float,
    lower: int,
    upper: int,
) -> int:
    if upper <= lower:
        return lower
    return unifint(diff_lb, diff_ub, (lower, upper))


def _build_patch_aa62e3f4(
    target_h: int,
    target_w: int,
) -> Indices:
    for _ in range(200):
        x0 = randint(ZERO, target_w - ONE)
        x1 = randint(x0, min(target_w - ONE, x0 + randint(ZERO, min(TWO, target_w - x0 - ONE))))
        x2 = [(x0, x1)]
        x3 = T
        for _ in range(1, target_h):
            x4 = []
            for x5 in (-ONE, ZERO, ONE):
                for x6 in (-ONE, ZERO, ONE):
                    x7 = max(ZERO, min(target_w - ONE, x0 + x5))
                    x8 = max(x7, min(target_w - ONE, x1 + x6))
                    if max(x7, x0) <= min(x8, x1):
                        x4.append((x7, x8))
            if len(x4) == ZERO:
                x3 = F
                break
            x0, x1 = choice(x4)
            x2.append((x0, x1))
        if not x3:
            continue
        x9 = frozenset((i, j) for i, (left, right) in enumerate(x2) for j in range(left, right + ONE))
        x10 = tuple(right - left + ONE for left, right in x2)
        if maximum(x10) == ONE:
            continue
        if len(set(x2)) == ONE:
            continue
        if size(x9) < target_h + TWO:
            continue
        return x9
    raise RuntimeError("failed to build aa62e3f4 patch")


def _transformed_patch_aa62e3f4(
    patch: Patch,
) -> Indices:
    x0 = []
    for transform in _PATCH_TRANSFORMS_AA62E3F4:
        x1 = normalize(toindices(transform(toindices(patch))))
        if x1 not in x0:
            x0.append(x1)
    return choice(x0)


def _boundary_cells_aa62e3f4(
    patch: Patch,
) -> Indices:
    x0 = frozenset(toindices(patch))
    return frozenset(x1 for x1 in x0 if len(dneighbors(x1) & x0) < FOUR)


def _outer_border_aa62e3f4(
    patch: Patch,
) -> Indices:
    x0 = frozenset(toindices(patch))
    x1 = set()
    for x2 in x0:
        for x3 in dneighbors(x2):
            if x3 not in x0:
                x1.add(x3)
    return frozenset(x1)


def _origin_candidates_aa62e3f4(
    grid_h: int,
    grid_w: int,
    patch: Patch,
    force_edge: bool,
) -> tuple[tuple[int, int], ...]:
    ph, pw = shape(patch)
    x0 = [(i, j) for i in range(grid_h - ph + ONE) for j in range(grid_w - pw + ONE)]
    shuffle(x0)
    if not force_edge:
        return tuple(x0)
    x1 = [
        loc
        for loc in x0
        if loc[ZERO] == ZERO
        or loc[ONE] == ZERO
        or loc[ZERO] == grid_h - ph
        or loc[ONE] == grid_w - pw
    ]
    x1.extend(loc for loc in x0 if loc not in x1)
    return tuple(x1)


def generate_aa62e3f4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = tuple(x1 for x1 in range(TEN) if x1 != EIGHT)
    while T:
        x1 = _sample_int_aa62e3f4(diff_lb, diff_ub, FIVE, 18)
        x2 = _sample_int_aa62e3f4(diff_lb, diff_ub, FIVE, 18)
        if choice((T, F)):
            x2 = x1
        x3 = _sample_int_aa62e3f4(diff_lb, diff_ub, THREE, min(EIGHT, x1 - ONE))
        x4 = _sample_int_aa62e3f4(diff_lb, diff_ub, THREE, min(EIGHT, x2 - ONE))
        x5 = _transformed_patch_aa62e3f4(_build_patch_aa62e3f4(x3, x4))
        x6 = _origin_candidates_aa62e3f4(x1, x2, x5, choice((T, T, F)))
        if len(x6) == ZERO:
            continue
        x7 = shift(x5, choice(x6))
        x8 = toindices(x7)
        if 2 * size(x8) >= x1 * x2:
            continue
        x9 = _boundary_cells_aa62e3f4(x8)
        x10 = frozenset(x11 for x11 in x8 if x11 not in x9)
        if len(x10) == ZERO and size(x8) < FIVE:
            continue
        x11 = choice(x0)
        x12 = tuple(x13 for x13 in x0 if x13 != x11)
        x13 = choice(x12)
        x14 = tuple(x15 for x15 in x12 if x15 != x13)
        x15 = choice(x14)
        x16 = x10 if len(x10) > ZERO else x8
        x17 = min(THREE, len(x16), max(ONE, size(x8) // SIX + ONE))
        x18 = randint(ONE, x17)
        x19 = len(x10) >= 2 * x18 + ONE and choice((T, F, F))
        gi = canvas(EIGHT, (x1, x2))
        gi = fill(gi, x13, x8)
        if x19:
            gi = fill(gi, x15, x10)
        x20 = frozenset(sample(totuple(x16), x18))
        gi = fill(gi, x11, x20)
        if mostcolor(gi) != EIGHT:
            continue
        if leastcolor(gi) != x11:
            continue
        x21 = _outer_border_aa62e3f4(x8)
        go = canvas(EIGHT, (x1, x2))
        go = fill(go, x11, x21)
        x22 = colorcount(gi, x11)
        x23 = colorcount(gi, x13)
        if x22 >= x23:
            continue
        if x19 and colorcount(gi, x15) <= x22:
            continue
        if colorcount(go, x11) < FOUR:
            continue
        return {"input": gi, "output": go}
