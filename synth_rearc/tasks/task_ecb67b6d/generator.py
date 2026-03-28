from synth_rearc.core import *

from .helpers import halo_ecb67b6d, has_diagonal_run_ecb67b6d


_PATCH_TRANSFORMS_ECB67B6D = (
    identity,
    hmirror,
    vmirror,
    dmirror,
    cmirror,
    compose(hmirror, vmirror),
    compose(hmirror, dmirror),
    compose(vmirror, dmirror),
)

_DISTRACTOR_PATTERNS_ECB67B6D = (
    ("x",),
    ("xx",),
    ("xxx",),
    ("x", "x"),
    ("x", "x", "x"),
    ("xx", "xx"),
    ("xxx", "xxx"),
    ("x.", "xx"),
    (".x", "xx"),
    ("xx", "x."),
    ("xx", ".x"),
    ("x.", "xx", "x."),
    ("xxx", "x.."),
    ("xxx", ".x."),
)


def _sample_int_ecb67b6d(
    diff_lb: float,
    diff_ub: float,
    lower: int,
    upper: int,
) -> int:
    if upper <= lower:
        return lower
    return unifint(diff_lb, diff_ub, (lower, upper))


def _pattern_to_patch_ecb67b6d(
    pattern: tuple[str, ...],
) -> Indices:
    return frozenset(
        (i, j)
        for i, row in enumerate(pattern)
        for j, value in enumerate(row)
        if value == "x"
    )


_DISTRACTOR_PATCHES_ECB67B6D = tuple(
    _pattern_to_patch_ecb67b6d(pattern)
    for pattern in _DISTRACTOR_PATTERNS_ECB67B6D
)

for patch in _DISTRACTOR_PATCHES_ECB67B6D:
    if has_diagonal_run_ecb67b6d(patch):
        raise ValueError("invalid distractor patch for ecb67b6d")


def _transformed_patch_ecb67b6d(
    patch: Patch,
    max_h: int,
    max_w: int,
) -> Indices:
    x0 = []
    for transform in _PATCH_TRANSFORMS_ECB67B6D:
        x1 = normalize(toindices(transform(toindices(patch))))
        if height(x1) <= max_h and width(x1) <= max_w and x1 not in x0:
            x0.append(x1)
    return choice(x0)


def _diagonal_backbone_ecb67b6d(
    length: int,
    falling: bool,
) -> Indices:
    if falling:
        return frozenset((k, k) for k in range(length))
    return frozenset((k, length - ONE - k) for k in range(length))


def _expand_patch_ecb67b6d(
    patch: Patch,
    nsteps: int,
    max_h: int,
    max_w: int,
    avoid_diagonal: bool,
) -> Indices:
    x0 = normalize(toindices(patch))
    for _ in range(nsteps):
        x1 = set()
        for loc in x0:
            x1.update(neighbors(loc))
        x1.difference_update(x0)
        x2 = list(x1)
        shuffle(x2)
        x3 = F
        for loc in x2:
            x4 = normalize(frozenset(set(x0) | {loc}))
            if height(x4) > max_h or width(x4) > max_w:
                continue
            if avoid_diagonal and has_diagonal_run_ecb67b6d(x4):
                continue
            x0 = x4
            x3 = T
            break
        if not x3:
            break
    return x0


def _sample_target_patch_ecb67b6d(
    diff_lb: float,
    diff_ub: float,
    max_h: int,
    max_w: int,
) -> Indices:
    x0 = min(max_h, max_w, 7)
    x1 = _sample_int_ecb67b6d(diff_lb, diff_ub, THREE, x0)
    x2 = _diagonal_backbone_ecb67b6d(x1, choice((T, F)))
    x3 = _sample_int_ecb67b6d(diff_lb, diff_ub, ZERO, x1 + TWO)
    x4 = _expand_patch_ecb67b6d(x2, x3, max_h, max_w, F)
    return _transformed_patch_ecb67b6d(x4, max_h, max_w)


def _sample_strip_distractor_ecb67b6d(
    diff_lb: float,
    diff_ub: float,
    max_h: int,
    max_w: int,
) -> Indices:
    if choice((T, F)):
        x0 = ONE if max_h == ONE else choice((ONE, TWO))
        x1 = _sample_int_ecb67b6d(diff_lb, diff_ub, TWO, min(SIX, max_w))
    else:
        x0 = _sample_int_ecb67b6d(diff_lb, diff_ub, TWO, min(SIX, max_h))
        x1 = ONE if max_w == ONE else choice((ONE, TWO))
    return frozenset((i, j) for i in range(x0) for j in range(x1))


def _sample_distractor_patch_ecb67b6d(
    diff_lb: float,
    diff_ub: float,
    max_h: int,
    max_w: int,
) -> Indices:
    x0 = choice(("strip", "strip", "motif", "blob"))
    if x0 == "strip":
        x1 = _sample_strip_distractor_ecb67b6d(diff_lb, diff_ub, max_h, max_w)
    else:
        x2 = [
            patch
            for patch in _DISTRACTOR_PATCHES_ECB67B6D
            if height(patch) <= max_h and width(patch) <= max_w
        ]
        x1 = choice(x2)
        if x0 == "blob":
            x3 = _sample_int_ecb67b6d(diff_lb, diff_ub, ZERO, FOUR)
            x1 = _expand_patch_ecb67b6d(x1, x3, max_h, max_w, T)
    return _transformed_patch_ecb67b6d(x1, max_h, max_w)


def _origin_candidates_ecb67b6d(
    h: int,
    w: int,
    patch: Patch,
    force_edge: bool,
) -> tuple[tuple[int, int], ...]:
    ph, pw = shape(patch)
    if force_edge:
        x0 = choice(("top", "bottom", "free"))
        x1 = choice(("left", "right", "free"))
        if x0 == "free" and x1 == "free":
            x0 = choice(("top", "bottom"))
    else:
        x0 = choice(("free", "free", "top", "bottom"))
        x1 = choice(("free", "free", "left", "right"))
    rows = [ZERO] if x0 == "top" else [h - ph] if x0 == "bottom" else list(range(h - ph + ONE))
    cols = [ZERO] if x1 == "left" else [w - pw] if x1 == "right" else list(range(w - pw + ONE))
    x2 = [(i, j) for i in rows for j in cols]
    shuffle(x2)
    x3 = [(i, j) for i in range(h - ph + ONE) for j in range(w - pw + ONE)]
    shuffle(x3)
    x2.extend(loc for loc in x3 if loc not in x2)
    return tuple(x2)


def _place_patch_ecb67b6d(
    blocked: set[tuple[int, int]],
    h: int,
    w: int,
    patch: Patch,
    force_edge: bool,
) -> Indices | None:
    for origin in _origin_candidates_ecb67b6d(h, w, patch, force_edge):
        x0 = toindices(shift(toindices(patch), origin))
        if len(set(halo_ecb67b6d(x0)) & blocked) > ZERO:
            continue
        return x0
    return None


def generate_ecb67b6d(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _sample_int_ecb67b6d(diff_lb, diff_ub, FOUR, 18)
        x1 = _sample_int_ecb67b6d(diff_lb, diff_ub, FIVE, 22)
        x2 = x0 * x1
        x3 = max(TWO, x2 // 24 + ONE)
        x4 = _sample_int_ecb67b6d(diff_lb, diff_ub, ONE, min(FOUR, x3))
        x5 = _sample_int_ecb67b6d(diff_lb, diff_ub, ONE, min(12, x3 + TWO))
        blocked = set()
        targets = []
        distractors = []
        x6 = T
        for _ in range(x4):
            placed = None
            for _ in range(48):
                x7 = _sample_target_patch_ecb67b6d(diff_lb, diff_ub, min(x0, 8), min(x1, 8))
                placed = _place_patch_ecb67b6d(blocked, x0, x1, x7, T)
                if placed is not None:
                    targets.append(placed)
                    blocked.update(halo_ecb67b6d(placed))
                    break
            if placed is None:
                x6 = F
                break
        if not x6:
            continue
        for _ in range(x5):
            placed = None
            for _ in range(48):
                x8 = _sample_distractor_patch_ecb67b6d(diff_lb, diff_ub, min(x0, 6), min(x1, 6))
                placed = _place_patch_ecb67b6d(blocked, x0, x1, x8, F)
                if placed is not None:
                    distractors.append(placed)
                    blocked.update(halo_ecb67b6d(placed))
                    break
            if placed is None:
                break
        x9 = targets + distractors
        if len(distractors) == ZERO or len(x9) < TWO:
            continue
        x10 = sum(len(patch) for patch in x9)
        if x10 * TWO >= x2:
            continue
        if x10 < max(FOUR, x2 // 8):
            continue
        if x10 > (9 * x2) // 20:
            continue
        x11 = lambda patch: uppermost(patch) == ZERO or leftmost(patch) == ZERO or lowermost(patch) == x0 - ONE or rightmost(patch) == x1 - ONE
        if not any(x11(patch) for patch in x9):
            continue
        gi = canvas(SEVEN, (x0, x1))
        for patch in x9:
            gi = fill(gi, FIVE, patch)
        go = gi
        for patch in targets:
            go = fill(go, EIGHT, patch)
        x12 = colorfilter(objects(gi, T, T, F), FIVE)
        if size(x12) != len(x9):
            continue
        x13 = sfilter(x12, has_diagonal_run_ecb67b6d)
        if size(x13) != len(targets):
            continue
        if colorcount(gi, SEVEN) <= colorcount(gi, FIVE):
            continue
        return {"input": gi, "output": go}
