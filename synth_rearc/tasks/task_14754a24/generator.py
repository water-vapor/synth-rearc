from synth_rearc.core import *

from .helpers import plus_connected_subsets_14754a24, plus_patch_14754a24, valid_plus_center_14754a24


def _expand_14754a24(
    patch: Indices,
    dims: IntegerTuple,
    radius: Integer = ONE,
) -> Indices:
    h, w = dims
    out = set()
    for i, j in patch:
        for di in range(-radius, radius + ONE):
            for dj in range(-radius, radius + ONE):
                ni, nj = i + di, j + dj
                if ZERO <= ni < h and ZERO <= nj < w:
                    out.add((ni, nj))
    return frozenset(out)


def _detect_centers_14754a24(
    grid: Grid,
) -> tuple[IntegerTuple, ...]:
    h = height(grid)
    w = width(grid)
    centers = []
    for i in range(h):
        for j in range(w):
            if valid_plus_center_14754a24(grid, (i, j)) is not None:
                centers.append((i, j))
    return tuple(centers)


def _weighted_subset_14754a24(
    patch: Indices,
) -> Indices:
    subsets = plus_connected_subsets_14754a24(patch)
    pool = []
    for subset in subsets:
        n = len(subset)
        if n == TWO:
            weight = FOUR
        elif n == THREE:
            weight = THREE
        else:
            weight = TWO
        pool.extend(repeat(subset, weight))
    return choice(tuple(pool))


def _random_noise_14754a24(
    dims: IntegerTuple,
    blocked: Indices,
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    h, w = dims
    cells = tuple(sorted(difference(asindices(canvas(ZERO, dims)), blocked)))
    area = h * w
    target = unifint(diff_lb, diff_ub, (area * 7 // 20, area * 9 // 20))
    target = min(target, len(cells))
    return frozenset(sample(cells, target))


def generate_14754a24(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = unifint(diff_lb, diff_ub, (14, 19))
        w = unifint(diff_lb, diff_ub, (15, 20))
        dims = (h, w)
        motif_target = unifint(diff_lb, diff_ub, (FOUR, SIX))
        centers = []
        blocked = frozenset()
        motifs = []
        candidates = [
            (i, j)
            for i in range(h)
            for j in range(w)
            if len(plus_patch_14754a24((i, j), dims)) >= FOUR
        ]
        shuffle(candidates)
        for center in candidates:
            patch = plus_patch_14754a24(center, dims)
            if len(intersection(patch, blocked)) > ZERO:
                continue
            subset = _weighted_subset_14754a24(patch)
            motifs.append((center, patch, subset))
            centers.append(center)
            blocked = combine(blocked, _expand_14754a24(patch, dims))
            if len(motifs) == motif_target:
                break
        if len(motifs) < FOUR:
            continue
        gi = canvas(ZERO, dims)
        motif_cells = merge(tuple(patch for _, patch, _ in motifs))
        noise = _random_noise_14754a24(dims, motif_cells, diff_lb, diff_ub)
        gi = fill(gi, FIVE, noise)
        for _, patch, subset in motifs:
            gi = fill(gi, FIVE, patch)
            gi = fill(gi, FOUR, subset)
        detected = _detect_centers_14754a24(gi)
        intended = tuple(sorted(centers))
        if tuple(sorted(detected)) != intended:
            continue
        go = gi
        for center, _, _ in motifs:
            fill_patch = valid_plus_center_14754a24(gi, center)
            if fill_patch is None:
                break
            go = fill(go, TWO, fill_patch)
        else:
            return {"input": gi, "output": go}
