from synth_rearc.core import *


TARGET_MOTIFS_58490D8A = (
    frozenset({(0, 0), (0, 1), (1, 0), (1, 1)}),
    frozenset({(0, 1), (1, 0), (1, 1), (1, 2)}),
    frozenset({(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)}),
    frozenset({(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)}),
    frozenset({(0, 0), (0, 1), (1, 0), (1, 2), (2, 1)}),
    frozenset({(0, 1), (1, 0), (1, 1), (1, 2), (2, 0), (2, 2)}),
    frozenset({(0, 0), (0, 1), (0, 2), (1, 0), (1, 2)}),
    frozenset({(0, 0), (0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (2, 2)}),
    frozenset({(0, 1), (1, 0), (1, 2), (2, 1)}),
)
DISTRACTOR_MOTIFS_58490D8A = TARGET_MOTIFS_58490D8A + (
    frozenset({(0, 0), (1, 0), (1, 1), (2, 0)}),
    frozenset({(0, 1), (1, 1), (2, 0), (2, 1)}),
)
PATCH_TRANSFORMS_58490D8A = (
    identity,
    hmirror,
    vmirror,
    dmirror,
    cmirror,
    compose(hmirror, dmirror),
    compose(vmirror, dmirror),
    compose(hmirror, vmirror),
)
NONZERO_COLORS_58490D8A = interval(ONE, TEN, ONE)


def _halo_58490d8a(patch: Patch, dims: tuple[int, int]) -> set[tuple[int, int]]:
    h, w = dims
    res = set()
    for loc in toindices(patch):
        res.add(loc)
        for ij in neighbors(loc):
            if 0 <= ij[0] < h and 0 <= ij[1] < w:
                res.add(ij)
    return res


def _place_patch_58490d8a(
    blocked: set[tuple[int, int]],
    patch: Patch,
    dims: tuple[int, int],
) -> tuple[set[tuple[int, int]], Patch]:
    h, w = dims
    ph, pw = shape(patch)
    candidates = []
    for i in range(h - ph + 1):
        for j in range(w - pw + 1):
            placed = shift(patch, (i, j))
            if toindices(placed).isdisjoint(blocked):
                candidates.append((i, j))
    if len(candidates) == 0:
        raise RuntimeError("no placement available")
    anchor = choice(candidates)
    placed = shift(patch, anchor)
    blocked |= _halo_58490d8a(placed, dims)
    return blocked, placed


def _corner_anchor_58490d8a(
    grid_shape: tuple[int, int],
    canvas_shape: tuple[int, int],
) -> tuple[int, int]:
    gh, gw = grid_shape
    ch, cw = canvas_shape
    max_i = gh - ch
    max_j = gw - cw
    band_i = min(FOUR, max_i)
    band_j = min(FOUR, max_j)
    top = randint(ZERO, band_i) if choice((T, F)) else randint(max_i - band_i, max_i)
    left = randint(ZERO, band_j) if choice((T, F)) else randint(max_j - band_j, max_j)
    return (top, left)


def _variant_58490d8a(motif: Indices) -> Indices:
    return normalize(choice(PATCH_TRANSFORMS_58490D8A)(motif))


def generate_58490d8a(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    _ = (diff_lb, diff_ub)
    for _attempt in range(200):
        ntargets = randint(TWO, FOUR)
        maxcount = randint(TWO, FIVE)
        counts = [randint(ONE, maxcount) for _ in range(ntargets)]
        counts[randint(ZERO, ntargets - 1)] = maxcount

        canvas_h = add(double(ntargets), ONE)
        canvas_w = add(add(double(maxcount), ONE), randint(ZERO, TWO))
        grid_h = randint(max(18, add(canvas_h, SIX)), 28)
        grid_w = randint(max(20, add(canvas_w, SIX)), 30)

        bgc = choice(NONZERO_COLORS_58490D8A)
        remcols = remove(bgc, NONZERO_COLORS_58490D8A)
        target_colors = sample(remcols, ntargets)
        remcols = difference(remcols, target_colors)

        ndistractors = ONE if choice((T, T, T, F)) else ZERO
        distractor_colors = sample(remcols, ndistractors)
        target_motifs = [_variant_58490d8a(motif) for motif in sample(TARGET_MOTIFS_58490D8A, ntargets)]
        distractor_motifs = [
            _variant_58490d8a(motif) for motif in sample(DISTRACTOR_MOTIFS_58490D8A, ndistractors)
        ]

        gi = canvas(bgc, (grid_h, grid_w))
        go = canvas(ZERO, (canvas_h, canvas_w))
        canvas_patch = shift(asindices(go), _corner_anchor_58490d8a((grid_h, grid_w), (canvas_h, canvas_w)))
        gi = fill(gi, ZERO, canvas_patch)

        blocked = _halo_58490d8a(canvas_patch, (grid_h, grid_w))
        ci, cj = ulcorner(canvas_patch)
        for idx, col in enumerate(target_colors):
            marker = frozenset({(col, (ci + 1 + 2 * idx, cj + 1))})
            gi = paint(gi, marker)
            row = 1 + 2 * idx
            cols = interval(ONE, add(ONE, double(counts[idx])), TWO)
            go = fill(go, col, product(initset(row), cols))

        pieces = []
        for col, motif, count in zip(target_colors, target_motifs, counts):
            for _ in range(count):
                pieces.append((col, motif))
        for col, motif in zip(distractor_colors, distractor_motifs):
            pieces.append((col, motif))

        shuffle(pieces)
        pieces.sort(key=lambda item: (0 - height(item[1]), 0 - width(item[1]), 0 - len(item[1])))
        try:
            for col, motif in pieces:
                blocked, placed = _place_patch_58490d8a(blocked, motif, (grid_h, grid_w))
                gi = paint(gi, recolor(col, placed))
        except RuntimeError:
            continue
        return {"input": gi, "output": go}
    raise RuntimeError("failed to generate 58490d8a example")
