from synth_rearc.core import *

from .helpers import (
    adjacent_endpoint_arcs_753ea09b,
    dominant_fill_color_753ea09b,
    enclosed_cells_753ea09b,
    largest_two_eight_components_753ea09b,
)


GRID_SIZE_753EA09B = 30


def _joint_profiles_753ea09b(
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[int, ...], tuple[int, ...]] | None:
    min_gap = unifint(diff_lb, diff_ub, (4, 6))
    max_gap = unifint(diff_lb, diff_ub, (7, 10))
    if max_gap < min_gap:
        max_gap = min_gap
    top_gap = randint(min_gap, max_gap)
    bottom_gap = randint(min_gap, max_gap)
    top_left = randint(ZERO, GRID_SIZE_753EA09B - top_gap - ONE)
    left_lb = max(ZERO, top_left - EIGHT)
    left_ub = min(GRID_SIZE_753EA09B - bottom_gap - ONE, top_left + EIGHT)
    if left_lb > left_ub:
        return None
    bottom_left = randint(left_lb, left_ub)
    lefts = [top_left]
    gaps = [top_gap]
    for row in range(ONE, GRID_SIZE_753EA09B):
        remaining = GRID_SIZE_753EA09B - row - ONE
        opts = []
        for dleft in (-ONE, ZERO, ONE):
            nleft = lefts[-ONE] + dleft
            if not (ZERO <= nleft < GRID_SIZE_753EA09B):
                continue
            if abs(bottom_left - nleft) > remaining:
                continue
            for dgap in (-ONE, ZERO, ONE):
                ngap = gaps[-ONE] + dgap
                if not (min_gap <= ngap <= max_gap):
                    continue
                if abs(bottom_gap - ngap) > remaining:
                    continue
                nright = nleft + ngap
                pright = lefts[-ONE] + gaps[-ONE]
                if nright >= GRID_SIZE_753EA09B:
                    continue
                if abs(nright - pright) > ONE:
                    continue
                if abs((bottom_left + bottom_gap) - nright) > remaining:
                    continue
                score = 12 - abs(bottom_left - nleft) - abs(bottom_gap - ngap)
                weight = max(ONE, score)
                opts.extend(repeat((nleft, ngap), weight))
        if len(opts) == ZERO:
            return None
        nleft, ngap = choice(tuple(opts))
        lefts.append(nleft)
        gaps.append(ngap)
    return tuple(lefts), tuple(left + gap for left, gap in zip(lefts, gaps))


def _profile_path_753ea09b(
    cols: tuple[int, ...],
) -> Indices:
    return frozenset((i, col) for i, col in enumerate(cols))


def _expand8_753ea09b(
    patch: Indices,
    radius: int = ONE,
) -> Indices:
    out = set()
    for i, j in patch:
        for di in range(-radius, radius + ONE):
            for dj in range(-radius, radius + ONE):
                ni, nj = i + di, j + dj
                if ZERO <= ni < GRID_SIZE_753EA09B and ZERO <= nj < GRID_SIZE_753EA09B:
                    out.add((ni, nj))
    return frozenset(out)


def _random_fragment_753ea09b(
    length: int,
) -> Indices:
    while True:
        cells = [(ZERO, ZERO)]
        seen = {(ZERO, ZERO)}
        while len(cells) < length:
            i, j = cells[-ONE]
            opts = [
                (i + di, j + dj)
                for di in (-ONE, ZERO, ONE)
                for dj in (-ONE, ZERO, ONE)
                if not (di == ZERO and dj == ZERO)
                and (i + di, j + dj) not in seen
                and abs(i + di) <= THREE
                and abs(j + dj) <= THREE
            ]
            if len(opts) == ZERO:
                break
            nxt = choice(tuple(opts))
            cells.append(nxt)
            seen.add(nxt)
        if len(seen) == length:
            return normalize(frozenset(seen))


def _place_fragment_753ea09b(
    patch: Indices,
    blocked: Indices,
    allow_border: Boolean,
) -> Indices | None:
    h = height(patch)
    w = width(patch)
    cells = tuple(sorted(patch))
    if allow_border:
        ilb, iub = ZERO, GRID_SIZE_753EA09B - h
        jlb, jub = ZERO, GRID_SIZE_753EA09B - w
    else:
        ilb, iub = ONE, GRID_SIZE_753EA09B - h - ONE
        jlb, jub = ONE, GRID_SIZE_753EA09B - w - ONE
        if ilb > iub or jlb > jub:
            return None
    for _ in range(120):
        loc = (randint(ilb, iub), randint(jlb, jub))
        shifted = frozenset((i + loc[ZERO], j + loc[ONE]) for i, j in cells)
        if len(intersection(shifted, blocked)) == ZERO:
            return shifted
    return None


def _apply_random_transform_753ea09b(
    gi: Grid,
    go: Grid,
) -> tuple[Grid, Grid]:
    turns = randint(ZERO, THREE)
    for _ in range(turns):
        gi = rot90(gi)
        go = rot90(go)
    if choice((T, F)):
        gi = hmirror(gi)
        go = hmirror(go)
    if choice((T, F)):
        gi = vmirror(gi)
        go = vmirror(go)
    return gi, go


def generate_753ea09b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        profiles = _joint_profiles_753ea09b(diff_lb, diff_ub)
        if profiles is None:
            continue
        left_cols, right_cols = profiles
        left_path = _profile_path_753ea09b(left_cols)
        right_path = _profile_path_753ea09b(right_cols)
        paths = (left_path, right_path)
        arcs = adjacent_endpoint_arcs_753ea09b(paths, (GRID_SIZE_753EA09B, GRID_SIZE_753EA09B))
        barrier = merge((left_path, right_path, arcs[ZERO], arcs[ONE]))
        inside = enclosed_cells_753ea09b(barrier, (GRID_SIZE_753EA09B, GRID_SIZE_753EA09B))
        if not (120 <= len(inside) <= 240):
            continue
        bg = choice(tuple(range(TEN)))
        colors = tuple(color for color in range(TEN) if color != bg)
        fill_color = choice(colors)
        rare_color = choice(tuple(color for color in colors if color != fill_color))
        gi = canvas(bg, (GRID_SIZE_753EA09B, GRID_SIZE_753EA09B))
        gi = fill(gi, fill_color, left_path)
        gi = fill(gi, fill_color, right_path)
        reserved_arc = _expand8_753ea09b(combine(arcs[ZERO], arcs[ONE]))
        fill_blocked = _expand8_753ea09b(combine(left_path, right_path))
        nfill = unifint(diff_lb, diff_ub, (2, 5))
        for _ in range(nfill):
            frag = _random_fragment_753ea09b(unifint(diff_lb, diff_ub, (1, 7)))
            placed = _place_fragment_753ea09b(frag, combine(fill_blocked, reserved_arc), F)
            if placed is None:
                continue
            gi = fill(gi, fill_color, placed)
            fill_blocked = combine(fill_blocked, _expand8_753ea09b(placed))
        rare_blocked = combine(ofcolor(gi, fill_color), reserved_arc)
        nrare = unifint(diff_lb, diff_ub, (8, 16))
        for _ in range(nrare):
            frag = _random_fragment_753ea09b(unifint(diff_lb, diff_ub, (1, 6)))
            placed = _place_fragment_753ea09b(frag, rare_blocked, choice((T, F)))
            if placed is None:
                continue
            gi = fill(gi, rare_color, placed)
            rare_blocked = combine(rare_blocked, placed)
        if colorcount(gi, rare_color) >= colorcount(gi, fill_color):
            continue
        fill_patch = intersection(inside, ofcolor(gi, bg))
        if not (110 <= len(fill_patch) <= 230):
            continue
        go = fill(gi, fill_color, fill_patch)
        gi, go = _apply_random_transform_753ea09b(gi, go)
        x0 = dominant_fill_color_753ea09b(gi)
        x1 = largest_two_eight_components_753ea09b(ofcolor(gi, x0))
        if len(x1) < TWO:
            continue
        x2 = adjacent_endpoint_arcs_753ea09b(x1, shape(gi))
        x3 = merge((x1[ZERO], x1[ONE], x2[ZERO], x2[ONE]))
        x4 = enclosed_cells_753ea09b(x3, shape(gi))
        x5 = fill(gi, x0, intersection(x4, ofcolor(gi, mostcolor(gi))))
        if x5 != go:
            continue
        return {"input": gi, "output": go}
