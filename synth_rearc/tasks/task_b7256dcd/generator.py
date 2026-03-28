from synth_rearc.core import *

from .verifier import verify_b7256dcd


SEED_COLORS_B7256DCD = (ZERO, ONE, TWO, THREE, FOUR, FIVE, EIGHT, NINE)
ORTHOGONAL_STEPS_B7256DCD = (
    UP,
    DOWN,
    LEFT,
    RIGHT,
)


def _normalize_patch_b7256dcd(
    patch: Indices,
) -> Indices:
    return normalize(frozenset(patch))


def _halo_b7256dcd(
    patch: Patch,
) -> Indices:
    x0 = toindices(patch)
    x1 = set(x0)
    for cell in x0:
        x1.update(dneighbors(cell))
    return frozenset(x1)


def _adjacent_background_cells_b7256dcd(
    patch: Patch,
    dims: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    h, w = dims
    x0 = []
    x1 = toindices(patch)
    for cell in x1:
        for step in ORTHOGONAL_STEPS_B7256DCD:
            x2 = add(cell, step)
            if not (ZERO <= x2[0] < h and ZERO <= x2[1] < w):
                continue
            if x2 in x1:
                continue
            x0.append(x2)
    return dedupe(tuple(x0))


def _sample_shape_b7256dcd(
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    while True:
        ncells = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x0 = {ORIGIN}
        while len(x0) < ncells:
            x1 = choice(totuple(frozenset(x0)))
            x2 = choice(ORTHOGONAL_STEPS_B7256DCD)
            x3 = add(x1, x2)
            x0.add(x3)
        x4 = _normalize_patch_b7256dcd(frozenset(x0))
        if height(x4) <= FOUR and width(x4) <= FOUR:
            return x4


def _place_patch_b7256dcd(
    dims: IntegerTuple,
    patch: Indices,
    blocked: Indices,
) -> Indices | None:
    h, w = dims
    ph, pw = shape(patch)
    anchors = [(i, j) for i in range(h - ph + ONE) for j in range(w - pw + ONE)]
    shuffle(anchors)
    for anchor in anchors:
        x0 = shift(patch, anchor)
        if toindices(x0) & blocked:
            continue
        return x0
    return None


def _render_input_b7256dcd(
    dims: IntegerTuple,
    six_patches: tuple[Indices, ...],
    active_seeds: tuple[tuple[Integer, IntegerTuple], ...],
    orphan_seeds: tuple[tuple[Integer, IntegerTuple], ...],
) -> Grid:
    gi = canvas(SEVEN, dims)
    for patch in six_patches:
        gi = paint(gi, recolor(SIX, patch))
    for color_, cell in active_seeds + orphan_seeds:
        gi = fill(gi, color_, frozenset({cell}))
    return gi


def _render_output_b7256dcd(
    dims: IntegerTuple,
    six_patches: tuple[Indices, ...],
    recolors: tuple[Integer, ...],
) -> Grid:
    go = canvas(SEVEN, dims)
    for patch, color_ in zip(six_patches, recolors):
        go = paint(go, recolor(color_, patch))
    return go


def generate_b7256dcd(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = unifint(diff_lb, diff_ub, (FIVE, NINE))
        w = unifint(diff_lb, diff_ub, (FOUR, NINE))
        dims = astuple(h, w)
        nactive = randint(ONE, min(THREE, len(SEED_COLORS_B7256DCD)))
        ninactive = randint(ZERO, ONE)
        norphans = randint(ZERO, min(ONE, len(SEED_COLORS_B7256DCD) - nactive))
        npatches = nactive + ninactive
        palette_ = sample(SEED_COLORS_B7256DCD, nactive + norphans)

        six_patches = []
        blocked = frozenset()
        ok = True
        for _ in range(npatches):
            patch = _sample_shape_b7256dcd(diff_lb, diff_ub)
            placed = _place_patch_b7256dcd(dims, patch, blocked)
            if placed is None:
                ok = False
                break
            six_patches.append(placed)
            blocked = blocked | _halo_b7256dcd(placed)
        if not ok:
            continue

        occupied = frozenset(cell for patch in six_patches for cell in toindices(patch))
        active_seeds = []
        for idx in range(nactive):
            patch = six_patches[idx]
            x0 = []
            for cell in _adjacent_background_cells_b7256dcd(patch, dims):
                if cell in occupied:
                    continue
                if any(cell in toindices(seed) or cell in _halo_b7256dcd(seed) for _, seed in active_seeds):
                    continue
                x1 = frozenset({cell})
                x2 = all(not adjacent(other, x1) for j, other in enumerate(six_patches) if j != idx)
                if x2:
                    x0.append(cell)
            if len(x0) == ZERO:
                ok = False
                break
            cell = choice(x0)
            active_seeds.append((palette_[idx], frozenset({cell})))
            occupied = occupied | frozenset({cell})
        if not ok:
            continue

        orphan_seeds = []
        candidates = [
            (i, j)
            for i in range(h)
            for j in range(w)
            if (i, j) not in occupied
        ]
        shuffle(candidates)
        for cell in candidates:
            if len(orphan_seeds) == norphans:
                break
            x0 = frozenset({cell})
            if any(adjacent(patch, x0) for patch in six_patches):
                continue
            if any(adjacent(seed, x0) or cell in toindices(seed) for _, seed in active_seeds + orphan_seeds):
                continue
            orphan_seeds.append((palette_[nactive + len(orphan_seeds)], frozenset({cell})))
            occupied = occupied | frozenset({cell})
        if len(orphan_seeds) != norphans:
            continue

        x0 = tuple(six_patches)
        x1 = tuple((color_, first(seed)) for color_, seed in active_seeds)
        x2 = tuple((color_, first(seed)) for color_, seed in orphan_seeds)
        x3 = tuple(palette_[idx] if idx < nactive else SIX for idx in range(npatches))
        gi = _render_input_b7256dcd(dims, x0, x1, x2)
        go = _render_output_b7256dcd(dims, x0, x3)
        if verify_b7256dcd(gi) != go:
            continue
        return {"input": gi, "output": go}
