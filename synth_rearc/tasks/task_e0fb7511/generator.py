from synth_rearc.core import *


_PATCH_TRANSFORMS_E0FB7511 = (
    identity,
    hmirror,
    vmirror,
    dmirror,
    cmirror,
    compose(hmirror, vmirror),
    compose(hmirror, dmirror),
    compose(vmirror, dmirror),
)

_SMALL_PATTERNS_E0FB7511 = (
    ("xx",),
    ("x.", "xx"),
)

_LARGE_PATTERNS_E0FB7511 = (
    (".x.", "xxx", "..x"),
    ("xxx", "xx.", ".x."),
    (".xx", ".xx", ".x.", "xx.", "x.."),
)


def _sample_int_e0fb7511(
    diff_lb: float,
    diff_ub: float,
    lower: int,
    upper: int,
) -> int:
    if upper <= lower:
        return lower
    return unifint(diff_lb, diff_ub, (lower, upper))


def _pattern_to_patch_e0fb7511(
    pattern: tuple[str, ...],
) -> Indices:
    return frozenset(
        (i, j)
        for i, row in enumerate(pattern)
        for j, value in enumerate(row)
        if value == "x"
    )


_SMALL_PATCHES_E0FB7511 = tuple(
    _pattern_to_patch_e0fb7511(pattern)
    for pattern in _SMALL_PATTERNS_E0FB7511
)

_LARGE_PATCHES_E0FB7511 = tuple(
    _pattern_to_patch_e0fb7511(pattern)
    for pattern in _LARGE_PATTERNS_E0FB7511
)


def _transformed_patch_e0fb7511(
    patch: Patch,
) -> Indices:
    x0 = []
    for transform in _PATCH_TRANSFORMS_E0FB7511:
        x1 = normalize(toindices(transform(toindices(patch))))
        if x1 not in x0:
            x0.append(x1)
    return choice(x0)


def _orth_halo_e0fb7511(
    patch: Patch,
) -> Indices:
    x0 = set(toindices(patch))
    for loc in toindices(patch):
        x0.update(dneighbors(loc))
    return frozenset(x0)


def _origin_candidates_e0fb7511(
    height_: int,
    width_: int,
    patch: Patch,
    force_edge: bool,
) -> tuple[tuple[int, int], ...]:
    ph, pw = shape(patch)
    x0 = [(i, j) for i in range(height_ - ph + ONE) for j in range(width_ - pw + ONE)]
    shuffle(x0)
    if not force_edge:
        return tuple(x0)
    x1 = [loc for loc in x0 if loc[0] == ZERO or loc[1] == ZERO or loc[0] == height_ - ph or loc[1] == width_ - pw]
    x1.extend(loc for loc in x0 if loc not in x1)
    return tuple(x1)


def _place_patch_e0fb7511(
    blocked: set[tuple[int, int]],
    height_: int,
    width_: int,
    patch: Patch,
    force_edge: bool,
) -> Indices | None:
    for origin in _origin_candidates_e0fb7511(height_, width_, patch, force_edge):
        x0 = shift(toindices(patch), origin)
        x1 = toindices(x0)
        if len(set(_orth_halo_e0fb7511(x1)) & blocked) > ZERO:
            continue
        return x1
    return None


def generate_e0fb7511(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        height_, width_ = 13, 13
        background = canvas(ONE, (height_, width_))
        all_indices = asindices(background)
        blocked = set()
        targets = []
        nsmall = _sample_int_e0fb7511(diff_lb, diff_ub, FOUR, SIX)
        nsingletons = _sample_int_e0fb7511(diff_lb, diff_ub, 13, 24)
        large_patch = _transformed_patch_e0fb7511(choice(_LARGE_PATCHES_E0FB7511))
        large_loc = _place_patch_e0fb7511(blocked, height_, width_, large_patch, choice((T, F)))
        if large_loc is None:
            continue
        targets.append(large_loc)
        blocked.update(_orth_halo_e0fb7511(large_loc))
        x0 = T
        for _ in range(nsmall):
            x1 = _transformed_patch_e0fb7511(choice((_SMALL_PATCHES_E0FB7511[ZERO], _SMALL_PATCHES_E0FB7511[ZERO], _SMALL_PATCHES_E0FB7511[ONE])))
            x2 = _place_patch_e0fb7511(blocked, height_, width_, x1, choice((T, F, F)))
            if x2 is None:
                x0 = F
                break
            targets.append(x2)
            blocked.update(_orth_halo_e0fb7511(x2))
        if not x0:
            continue
        singletons = []
        for _ in range(nsingletons):
            x3 = tuple(set(all_indices) - blocked)
            if len(x3) == ZERO:
                x0 = F
                break
            x4 = choice(x3)
            x5 = frozenset({x4})
            singletons.append(x5)
            blocked.update(_orth_halo_e0fb7511(x5))
        if not x0:
            continue
        x6 = tuple(len(patch) for patch in targets)
        if not contained(THREE, x6) and choice((T, F)):
            continue
        x7 = sum(len(patch) for patch in targets) + len(singletons)
        if x7 < 26 or x7 > 46:
            continue
        x8 = background
        for patch in targets:
            x8 = fill(x8, ZERO, patch)
        for patch in singletons:
            x8 = fill(x8, ZERO, patch)
        x9 = frozenset(cell for patch in targets for cell in patch)
        x10 = fill(x8, EIGHT, x9)
        return {"input": x8, "output": x10}
