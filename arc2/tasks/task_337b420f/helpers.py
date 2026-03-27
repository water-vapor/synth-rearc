from arc2.core import *


OUTPUT_DIMS_337B420F = (FIVE, FIVE)
OUTPUT_CELLS_337B420F = tuple(asindices(canvas(ZERO, OUTPUT_DIMS_337B420F)))
PANEL_SEPARATOR_337B420F = canvas(ZERO, (FIVE, ONE))
NONZERO_NONBACKGROUND_COLORS_337B420F = remove(EIGHT, interval(ONE, TEN, ONE))


def _sample_connected_patch_337b420f(
    allowed: Indices,
    target_size: int,
) -> Indices | None:
    x0 = tuple(allowed)
    if len(x0) < target_size:
        return None
    for _ in range(48):
        x1 = {choice(x0)}
        while len(x1) < target_size:
            x2 = set()
            for x3 in x1:
                for x4 in dneighbors(x3):
                    if x4 in allowed and x4 not in x1:
                        x2.add(x4)
            if len(x2) == ZERO:
                break
            x1.add(choice(tuple(x2)))
        if len(x1) == target_size:
            return frozenset(x1)
    return None


def _sample_major_sizes_337b420f(
    diff_lb: float,
    diff_ub: float,
) -> tuple[int, int, int]:
    while True:
        x0 = unifint(diff_lb, diff_ub, (NINE, 16))
        x1 = []
        x2 = x0
        x3 = T
        for x4 in (TWO, ONE):
            x5 = min(NINE, x2 - TWO * x4)
            if x5 < TWO:
                x3 = F
                break
            x6 = unifint(diff_lb, diff_ub, (TWO, x5))
            x1.append(x6)
            x2 -= x6
        if not x3:
            continue
        if not TWO <= x2 <= NINE:
            continue
        x1.append(x2)
        shuffle(x1)
        return tuple(x1)


def sample_major_patches_337b420f(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Indices, Indices, Indices] | None:
    x0 = _sample_major_sizes_337b420f(diff_lb, diff_ub)
    x1 = sorted(x0, reverse=T)
    x2 = set(OUTPUT_CELLS_337B420F)
    x3 = []
    for x4 in x1:
        x5 = _sample_connected_patch_337b420f(frozenset(x2), x4)
        if x5 is None:
            return None
        x3.append(x5)
        x2 -= set(x5)
    shuffle(x3)
    return tuple(x3)


def sample_distractor_337b420f(
    major_patch: Indices,
    diff_lb: float,
    diff_ub: float,
) -> Indices | None:
    x0 = min(FOUR, len(major_patch) - ONE, 12 - len(major_patch))
    if x0 < ONE:
        return None
    x1 = set(OUTPUT_CELLS_337B420F) - set(major_patch)
    for x2 in major_patch:
        x1 -= set(dneighbors(x2))
    if len(x1) == ZERO:
        return None
    x3 = min(x0, len(x1))
    x4 = unifint(diff_lb, diff_ub, (ONE, x3))
    x5 = tuple(range(x4, ZERO, NEG_ONE))
    for x6 in x5:
        x7 = _sample_connected_patch_337b420f(frozenset(x1), x6)
        if x7 is not None:
            return x7
    return None


def _inside_output_337b420f(
    patch: Patch,
) -> bool:
    x0 = uppermost(patch) >= ZERO
    x1 = leftmost(patch) >= ZERO
    x2 = lowermost(patch) < OUTPUT_DIMS_337B420F[0]
    x3 = rightmost(patch) < OUTPUT_DIMS_337B420F[1]
    return x0 and x1 and x2 and x3


def _shift_candidates_337b420f(
    patch: Patch,
) -> tuple[IntegerTuple, ...]:
    x0 = []
    if rightmost(patch) == OUTPUT_DIMS_337B420F[1] - ONE:
        x0.append(LEFT)
    if leftmost(patch) == ZERO:
        x0.append(RIGHT)
    if lowermost(patch) == OUTPUT_DIMS_337B420F[0] - ONE:
        x0.append(UP)
    if uppermost(patch) == ZERO:
        x0.append(DOWN)
    for x1 in (LEFT, RIGHT, UP, DOWN):
        if x1 not in x0:
            x0.append(x1)
    return tuple(x0)


def resolve_major_patch_337b420f(
    major_patch: Indices,
    occupied: Indices,
) -> Indices:
    x0 = len(intersection(major_patch, occupied)) == ZERO
    if x0:
        return major_patch
    x1 = _shift_candidates_337b420f(major_patch)
    for x2 in x1:
        x3 = shift(major_patch, x2)
        x4 = len(intersection(x3, occupied)) == ZERO
        x5 = _inside_output_337b420f(x3)
        if x4 and x5:
            return x3
    return major_patch


def maybe_shift_input_major_337b420f(
    major_patch: Indices,
    occupied: Indices,
) -> Indices:
    x0 = []
    for x1 in (LEFT, RIGHT, UP, DOWN):
        x2 = shift(major_patch, invert(x1))
        x3 = len(intersection(x2, occupied)) > ZERO
        x4 = _inside_output_337b420f(x2)
        if not x3 or not x4:
            continue
        x5 = resolve_major_patch_337b420f(x2, occupied)
        if x5 == major_patch:
            x0.append(x2)
    if len(x0) == ZERO:
        return major_patch
    if choice((T, F, F)):
        return choice(tuple(x0))
    return major_patch


def input_components_separate_337b420f(
    major_patch: Indices,
    distractor_patch: Indices,
) -> bool:
    x0 = len(intersection(major_patch, distractor_patch)) == ZERO
    if not x0:
        return F
    x1 = frozenset()
    for x2 in major_patch:
        x1 = combine(x1, dneighbors(x2))
    x3 = len(intersection(x1, distractor_patch)) == ZERO
    return x3


def make_panel_337b420f(
    color_value: int,
    major_patch: Indices,
    distractor_patch: Indices,
) -> Grid:
    x0 = canvas(EIGHT, OUTPUT_DIMS_337B420F)
    x1 = combine(major_patch, distractor_patch)
    x2 = fill(x0, color_value, x1)
    return x2


def stitch_panels_337b420f(
    panels: tuple[Grid, Grid, Grid],
) -> Grid:
    x0 = hconcat(panels[0], PANEL_SEPARATOR_337B420F)
    x1 = hconcat(x0, panels[1])
    x2 = hconcat(x1, PANEL_SEPARATOR_337B420F)
    x3 = hconcat(x2, panels[2])
    return x3
