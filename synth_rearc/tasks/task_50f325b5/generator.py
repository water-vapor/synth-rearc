from synth_rearc.core import *


NOISE_BAG_50f325b5 = (
    ZERO,
    ZERO,
    ZERO,
    TWO,
    TWO,
    TWO,
    FOUR,
    FOUR,
    SEVEN,
    SEVEN,
)

TEMPLATE_BANK_50f325b5 = (
    frozenset({(0, 1), (1, 0), (1, 1), (1, 2)}),
    frozenset({(0, 0), (0, 2), (1, 1), (1, 2)}),
    frozenset({(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)}),
    frozenset({(0, 0), (0, 1), (0, 2), (1, 1), (2, 1)}),
)


def _variants_50f325b5(patch: Patch) -> tuple[Patch, ...]:
    out = []
    x0 = normalize(patch)
    x1 = normalize(dmirror(vmirror(x0)))
    x2 = normalize(dmirror(vmirror(x1)))
    x3 = normalize(dmirror(vmirror(x2)))
    x4 = normalize(hmirror(x0))
    x5 = normalize(vmirror(x0))
    x6 = normalize(dmirror(x0))
    x7 = normalize(cmirror(x0))
    for candidate in (x0, x1, x2, x3, x4, x5, x6, x7):
        if candidate not in out:
            out.append(candidate)
    return tuple(out)


def _occurrence_patches_50f325b5(
    grid: Grid,
    variants: tuple[Patch, ...],
) -> tuple[Patch, ...]:
    found = []
    for patch in variants:
        probe = recolor(THREE, patch)
        for loc in occurrences(grid, probe):
            shifted = shift(patch, loc)
            if shifted not in found:
                found.append(shifted)
    found = sorted(
        found,
        key=lambda patch: (
            uppermost(patch),
            leftmost(patch),
            lowermost(patch),
            rightmost(patch),
            tuple(sorted(patch)),
        ),
    )
    out = []
    occupied = frozenset()
    for patch in found:
        if size(intersection(occupied, patch)) > ZERO:
            continue
        out.append(patch)
        occupied = combine(occupied, patch)
    return tuple(out)


def _random_grid_50f325b5(
    h: Integer,
    w: Integer,
) -> Grid:
    rows = []
    for _ in range(h):
        rows.append(tuple(choice(NOISE_BAG_50f325b5) for _ in range(w)))
    return tuple(rows)


def _placement_pool_50f325b5(
    variants: tuple[Patch, ...],
    dims: tuple[Integer, Integer],
) -> list[Patch]:
    h, w = dims
    out = []
    for patch in variants:
        ph, pw = shape(patch)
        for i in range(h - ph + ONE):
            for j in range(w - pw + ONE):
                out.append(shift(patch, (i, j)))
    shuffle(out)
    return out


def _in_bounds_50f325b5(
    loc: IntegerTuple,
    dims: tuple[Integer, Integer],
) -> Boolean:
    return both(
        both(loc[0] >= ZERO, loc[1] >= ZERO),
        both(loc[0] < dims[0], loc[1] < dims[1]),
    )


def _can_place_50f325b5(
    patch: Patch,
    placed: tuple[Patch, ...],
) -> Boolean:
    for other in placed:
        if size(intersection(patch, other)) > ZERO:
            return F
        if manhattan(patch, other) <= TWO:
            return F
    return T


def _decorate_candidates_50f325b5(
    patch: Patch,
    dims: tuple[Integer, Integer],
) -> tuple[IntegerTuple, ...]:
    cells = toindices(patch)
    out = []
    extras = delta(patch)
    for cell in extras:
        if _in_bounds_50f325b5(cell, dims):
            out.append(cell)
    shell = set()
    for cell in cells:
        for nbr in neighbors(cell):
            if nbr in cells:
                continue
            if _in_bounds_50f325b5(nbr, dims):
                shell.add(nbr)
    shell = tuple(shell)
    shuffle(out)
    shell = list(shell)
    shuffle(shell)
    out.extend(shell)
    return tuple(dedupe(tuple(out)))


def _try_add_three_50f325b5(
    grid: Grid,
    loc: IntegerTuple,
    variants: tuple[Patch, ...],
    targets: frozenset[Patch],
    reserved: frozenset[IntegerTuple],
) -> tuple[Grid, Boolean]:
    if contained(loc, reserved):
        return grid, F
    if index(grid, loc) == THREE:
        return grid, F
    candidate = fill(grid, THREE, frozenset({loc}))
    hits = frozenset(_occurrence_patches_50f325b5(candidate, variants))
    if hits <= targets:
        return candidate, T
    return grid, F


def generate_50f325b5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = unifint(diff_lb, diff_ub, (11, 18))
        w = choice((17, 17, 18, 18))
        shape0 = choice(TEMPLATE_BANK_50f325b5)
        variants = _variants_50f325b5(shape0)
        pool = _placement_pool_50f325b5(variants, (h, w))
        if len(pool) == ZERO:
            continue

        source = first(pool)
        placed = [source]
        ntargets = choice((ONE, TWO, TWO, THREE))
        shuffle(pool)
        for candidate in pool:
            if len(placed) == ntargets + ONE:
                break
            if not _can_place_50f325b5(candidate, tuple(placed)):
                continue
            placed.append(candidate)
        if len(placed) != ntargets + ONE:
            continue

        targets = tuple(placed[ONE:])
        target_set = frozenset(targets)
        reserved = frozenset(set(source) | set().union(*(set(p) for p in targets)))

        gi = _random_grid_50f325b5(h, w)
        gi = fill(gi, EIGHT, source)
        for target in targets:
            gi = fill(gi, THREE, target)

        hits = frozenset(_occurrence_patches_50f325b5(gi, variants))
        if hits != target_set:
            continue

        local_candidates = []
        for target in targets:
            local_candidates.extend(_decorate_candidates_50f325b5(target, (h, w)))
        local_candidates = list(dedupe(tuple(local_candidates)))
        shuffle(local_candidates)

        global_candidates = [
            cell for cell in asindices(gi)
            if cell not in reserved and cell not in local_candidates
        ]
        shuffle(global_candidates)

        local_budget = min(
            len(local_candidates),
            choice((ONE, TWO, TWO, THREE, FOUR, FOUR, FIVE, SIX)),
            max(ONE, 2 * ntargets + TWO),
        )
        global_budget = min(
            len(global_candidates),
            unifint(diff_lb, diff_ub, (max(6, (h * w) // 28), max(12, (h * w) // 11))),
        )

        for loc in local_candidates:
            if local_budget == ZERO:
                break
            if choice((T, T, F)):
                gi, added = _try_add_three_50f325b5(gi, loc, variants, target_set, reserved)
                if added:
                    local_budget -= ONE

        for loc in global_candidates:
            if global_budget == ZERO:
                break
            if choice((T, F, F)):
                gi, added = _try_add_three_50f325b5(gi, loc, variants, target_set, reserved)
                if added:
                    global_budget -= ONE

        hits = frozenset(_occurrence_patches_50f325b5(gi, variants))
        if hits != target_set:
            continue

        go = gi
        for target in targets:
            go = fill(go, EIGHT, target)
        return {"input": gi, "output": go}
