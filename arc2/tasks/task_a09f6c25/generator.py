from __future__ import annotations

from arc2.core import *


BG_OPTIONS_A09F6C25 = (FOUR, SEVEN, EIGHT)
GRID_H_BOUNDS_A09F6C25 = (17, 19)
GRID_W_BOUNDS_A09F6C25 = (19, 19)


def _reserve_patch_a09f6c25(patch: Indices) -> Indices:
    x0 = outbox(patch)
    x1 = backdrop(x0)
    return x1


def _connected_a09f6c25(patch: Indices) -> bool:
    if len(patch) == ZERO:
        return False
    frontier = [next(iter(patch))]
    seen = {frontier[0]}
    while frontier:
        cell = frontier.pop()
        for neighbor in dneighbors(cell):
            if neighbor in patch and neighbor not in seen:
                seen.add(neighbor)
                frontier.append(neighbor)
    return len(seen) == len(patch)


def _horizontal_symmetry_a09f6c25(patch: Indices) -> bool:
    x0 = normalize(patch)
    x1 = normalize(hmirror(x0))
    return x0 == x1


def _vertical_symmetry_a09f6c25(patch: Indices) -> bool:
    x0 = normalize(patch)
    x1 = normalize(vmirror(x0))
    return x0 == x1


def _shape_kind_a09f6c25(patch: Indices) -> str:
    x0 = _vertical_symmetry_a09f6c25(patch)
    x1 = _horizontal_symmetry_a09f6c25(patch)
    if x0:
        return "vertical"
    if x1:
        return "horizontal"
    return "none"


def _orbit_h_a09f6c25(cell: IntegerTuple, dims: IntegerTuple) -> Indices:
    h, _ = dims
    i, j = cell
    mate = (h - ONE - i, j)
    return frozenset({cell, mate})


def _orbit_attachable_a09f6c25(orbit: Indices, patch: Indices) -> bool:
    joined = combine(patch, orbit)
    for cell in orbit:
        if len(intersection(dneighbors(cell), joined)) == ZERO:
            return False
    return True


def _all_cells_a09f6c25(dims: IntegerTuple) -> tuple[IntegerTuple, ...]:
    h, w = dims
    return tuple(product(interval(ZERO, h, ONE), interval(ZERO, w, ONE)))


def _grow_orbits_a09f6c25(
    dims: IntegerTuple,
    seed: Indices,
    target_size: Integer,
) -> Indices:
    patch = seed
    cells = _all_cells_a09f6c25(dims)
    while len(patch) < target_size:
        candidates = []
        for cell in cells:
            orbit = _orbit_h_a09f6c25(cell, dims)
            if orbit <= patch:
                continue
            if len(combine(patch, orbit)) > target_size:
                continue
            if not _orbit_attachable_a09f6c25(orbit, patch):
                continue
            candidates.append(orbit)
        if len(candidates) == ZERO:
            break
        patch = combine(patch, choice(candidates))
    return normalize(patch)


def _sample_horizontal_patch_a09f6c25() -> Indices:
    for _ in range(300):
        dims = (choice((FIVE, FIVE, SEVEN, SEVEN, NINE)), randint(FIVE, TEN))
        mid = dims[0] // TWO
        span = randint(THREE, dims[1])
        left = randint(ZERO, dims[1] - span)
        patch = frozenset((mid, j) for j in range(left, left + span))
        starter = []
        for cell in _all_cells_a09f6c25((mid, dims[1])):
            orbit = _orbit_h_a09f6c25(cell, dims)
            if orbit <= patch:
                continue
            if len(orbit) == ONE:
                continue
            if _orbit_attachable_a09f6c25(orbit, patch):
                starter.append(orbit)
        if len(starter) == ZERO:
            continue
        patch = combine(patch, choice(starter))
        upper = min(18, dims[0] * dims[1] - ONE)
        lower = max(SIX, len(patch) + ONE)
        if lower > upper:
            continue
        patch = _grow_orbits_a09f6c25(dims, patch, randint(lower, upper))
        hsym = _horizontal_symmetry_a09f6c25(patch)
        vsym = _vertical_symmetry_a09f6c25(patch)
        area = height(patch) * width(patch)
        if not hsym or vsym:
            continue
        if height(patch) < THREE or width(patch) < THREE:
            continue
        if len(patch) * FOUR < area:
            continue
        if len(patch) * FIVE > area * FOUR:
            continue
        if not _connected_a09f6c25(patch):
            continue
        return patch
    return frozenset({
        (ZERO, ONE),
        (ONE, ZERO),
        (ONE, ONE),
        (ONE, TWO),
        (ONE, THREE),
        (TWO, ONE),
    })


def _sample_vertical_patch_a09f6c25() -> Indices:
    x0 = _sample_horizontal_patch_a09f6c25()
    x1 = dmirror(x0)
    x2 = normalize(x1)
    return x2


def _sample_none_patch_a09f6c25() -> Indices:
    for _ in range(300):
        dims = (randint(FOUR, SIX), randint(FOUR, SIX))
        start = frozenset({
            (ZERO, max(ZERO, dims[1] - TWO)),
            (ONE, max(ZERO, dims[1] - TWO)),
            (ONE, dims[1] - ONE),
        })
        patch = start
        target_size = randint(SEVEN, min(13, dims[0] * dims[1] - ONE))
        cells = _all_cells_a09f6c25(dims)
        while len(patch) < target_size:
            frontier = [cell for cell in cells if cell not in patch and len(intersection(dneighbors(cell), patch)) > ZERO]
            if len(frontier) == ZERO:
                break
            frontier.sort(key=lambda cell: (cell[0] + (dims[1] - ONE - cell[1]), -abs(cell[0] - cell[1])))
            patch = combine(patch, frozenset({choice(frontier[max(ZERO, len(frontier) // TWO - ONE):])}))
        patch = normalize(patch)
        if height(patch) < FOUR or width(patch) < FOUR:
            continue
        if _horizontal_symmetry_a09f6c25(patch):
            continue
        if _vertical_symmetry_a09f6c25(patch):
            continue
        if not _connected_a09f6c25(patch):
            continue
        return patch
    return frozenset({
        (ZERO, THREE),
        (ONE, TWO),
        (ONE, THREE),
        (TWO, ONE),
        (TWO, TWO),
        (THREE, ZERO),
        (THREE, ONE),
    })


def _sample_patch_a09f6c25(kind: str) -> Indices:
    if kind == "horizontal":
        return _sample_horizontal_patch_a09f6c25()
    if kind == "vertical":
        return _sample_vertical_patch_a09f6c25()
    return _sample_none_patch_a09f6c25()


def _placement_candidates_a09f6c25(
    patch: Indices,
    dims: IntegerTuple,
    reserved: Indices,
) -> list[tuple[Indices, Indices]]:
    ph, pw = shape(patch)
    h, w = dims
    candidates = []
    for i in range(h - ph + ONE):
        for j in range(w - pw + ONE):
            placed = shift(patch, (i, j))
            reserve = _reserve_patch_a09f6c25(placed)
            if len(intersection(reserve, reserved)) > ZERO:
                continue
            candidates.append((placed, reserve))
    return candidates


def _target_kinds_a09f6c25(diff_lb: float, diff_ub: float) -> list[str]:
    horizontal = unifint(diff_lb, diff_ub, (ONE, TWO))
    vertical = unifint(diff_lb, diff_ub, (ONE, TWO))
    nonsymmetric = choice((ZERO, ZERO, ZERO, ONE))
    kinds = ["horizontal"] * horizontal + ["vertical"] * vertical + ["none"] * nonsymmetric
    while len(kinds) < THREE:
        kinds.append(choice(("horizontal", "vertical")))
    while len(kinds) > FIVE:
        kinds.pop()
    shuffle(kinds)
    return kinds


def _output_color_a09f6c25(kind: str) -> Integer:
    if kind == "horizontal":
        return ONE
    if kind == "vertical":
        return THREE
    return SIX


def generate_a09f6c25(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        dims = (
            unifint(diff_lb, diff_ub, GRID_H_BOUNDS_A09F6C25),
            unifint(diff_lb, diff_ub, GRID_W_BOUNDS_A09F6C25),
        )
        bgc = choice(BG_OPTIONS_A09F6C25)
        gi = canvas(bgc, dims)
        go = canvas(bgc, dims)
        reserved = frozenset({})
        targets = []
        failed = False

        for kind in _target_kinds_a09f6c25(diff_lb, diff_ub):
            placed = None
            for _ in range(120):
                patch = _sample_patch_a09f6c25(kind)
                candidates = _placement_candidates_a09f6c25(patch, dims, reserved)
                if len(candidates) == ZERO:
                    continue
                placed = choice(candidates)
                break
            if placed is None:
                failed = True
                break
            patch, reserve = placed
            reserved = combine(reserved, reserve)
            targets.append((kind, patch))
        if failed:
            continue

        singletons = []
        nsingles = unifint(diff_lb, diff_ub, (TWO, FIVE))
        singleton_patch = frozenset({(ZERO, ZERO)})
        for _ in range(nsingles):
            candidates = _placement_candidates_a09f6c25(singleton_patch, dims, reserved)
            if len(candidates) == ZERO:
                break
            patch, reserve = choice(candidates)
            reserved = combine(reserved, reserve)
            singletons.append(patch)
        if len(singletons) < TWO:
            continue

        for kind, patch in targets:
            gi = fill(gi, TWO, patch)
            go = fill(go, _output_color_a09f6c25(_shape_kind_a09f6c25(patch)), patch)
        for patch in singletons:
            gi = fill(gi, TWO, patch)

        if choice((T, F)):
            gi = hmirror(gi)
            go = hmirror(go)
        if choice((T, F)):
            gi = vmirror(gi)
            go = vmirror(go)
        if gi == go:
            continue
        return {"input": gi, "output": go}
