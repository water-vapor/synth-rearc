from arc2.core import *


GRID_SHAPE = (10, 10)
FGC_OPTIONS = (SIX, EIGHT)
TARGET_SIZE_OPTIONS = (TWO, TWO, THREE, THREE, THREE, FOUR, FOUR, FIVE, SIX, SEVEN, EIGHT)
NOISE_KIND_OPTIONS = ("single", "single", "hbar", "vbar", "rect")


def _square_patch(size: int, loc: tuple[int, int], filled: bool) -> Indices:
    x0 = canvas(ZERO, (size, size))
    x1 = asindices(x0)
    x2 = branch(both(flip(filled), greater(size, TWO)), box(x1), x1)
    x3 = shift(x2, loc)
    return x3


def _mark_patch(patch: Indices) -> Indices:
    x0 = corners(patch)
    x1 = mapply(dneighbors, x0)
    x2 = outbox(patch)
    x3 = intersection(x1, x2)
    return x3


def _reserve_patch(patch: Indices) -> Indices:
    x0 = outbox(patch)
    x1 = backdrop(x0)
    return x1


def _can_place(patch: Indices, reserved: Indices) -> bool:
    x0 = intersection(patch, reserved)
    x1 = equality(x0, frozenset({}))
    return x1


def _target_candidates(reserved: Indices) -> list[Indices]:
    candidates = []
    for size in TARGET_SIZE_OPTIONS:
        fills = (T,) if size == TWO else (F,)
        for filled in fills:
            for i in range(ONE, GRID_SHAPE[0] - size):
                for j in range(ONE, GRID_SHAPE[1] - size):
                    patch = _square_patch(size, (i, j), filled)
                    reserve = _reserve_patch(patch)
                    if _can_place(reserve, reserved):
                        candidates.append(patch)
    return candidates


def _noise_candidates(kind: str, reserved: Indices) -> list[Indices]:
    candidates = []
    if kind == "single":
        for i in range(GRID_SHAPE[0]):
            for j in range(GRID_SHAPE[1]):
                patch = frozenset({(i, j)})
                reserve = _reserve_patch(patch)
                if _can_place(reserve, reserved):
                    candidates.append(patch)
    elif kind == "hbar":
        for width_ in range(TWO, GRID_SHAPE[1] - ONE):
            for i in range(GRID_SHAPE[0]):
                for j in range(GRID_SHAPE[1] - width_ + ONE):
                    patch = shift(asindices(canvas(ZERO, (ONE, width_))), (i, j))
                    reserve = _reserve_patch(patch)
                    if _can_place(reserve, reserved):
                        candidates.append(patch)
    elif kind == "vbar":
        for height_ in range(TWO, GRID_SHAPE[0] - ONE):
            for i in range(GRID_SHAPE[0] - height_ + ONE):
                for j in range(GRID_SHAPE[1]):
                    patch = shift(asindices(canvas(ZERO, (height_, ONE))), (i, j))
                    reserve = _reserve_patch(patch)
                    if _can_place(reserve, reserved):
                        candidates.append(patch)
    else:
        for shape_ in ((TWO, THREE), (THREE, TWO), (TWO, FOUR), (FOUR, TWO)):
            height_, width_ = shape_
            for i in range(GRID_SHAPE[0] - height_ + ONE):
                for j in range(GRID_SHAPE[1] - width_ + ONE):
                    patch = shift(asindices(canvas(ZERO, shape_)), (i, j))
                    reserve = _reserve_patch(patch)
                    if _can_place(reserve, reserved):
                        candidates.append(patch)
    return candidates


def _nested_cluster() -> tuple[list[Indices], Indices]:
    size = choice((SIX, SEVEN, EIGHT))
    locs = [(i, j) for i in range(ONE, GRID_SHAPE[0] - size) for j in range(ONE, GRID_SHAPE[1] - size)]
    if len(locs) == ZERO:
        return [], frozenset({})
    loc = choice(locs)
    outer = _square_patch(size, loc, F)
    inner_sizes = [candidate for candidate in (TWO, THREE, FOUR) if candidate <= size - FOUR]
    if len(inner_sizes) == ZERO:
        return [], frozenset({})
    inner_size = choice(inner_sizes)
    inner_candidates = []
    for i in range(loc[0] + TWO, loc[0] + size - inner_size - ONE):
        for j in range(loc[1] + TWO, loc[1] + size - inner_size - ONE):
            filled = equality(inner_size, TWO)
            inner = _square_patch(inner_size, (i, j), filled)
            if _can_place(inner, outer):
                inner_candidates.append(inner)
    if len(inner_candidates) == ZERO:
        return [], frozenset({})
    inner = choice(inner_candidates)
    reserve = _reserve_patch(outer)
    return [outer, inner], reserve


def generate_14b8e18c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        gi = canvas(SEVEN, GRID_SHAPE)
        go = canvas(SEVEN, GRID_SHAPE)
        fgc = choice(FGC_OPTIONS)
        reserved = frozenset({})
        target_patches = []

        ntargets = unifint(diff_lb, diff_ub, (ONE, FOUR))
        if both(greater(ntargets, ONE), choice((T, F, F))):
            nested, nest_reserved = _nested_cluster()
            if len(nested) > ZERO:
                target_patches.extend(nested)
                reserved = combine(reserved, nest_reserved)

        remaining = max(ONE, ntargets - len(target_patches))
        failed = F
        for _ in range(remaining):
            candidates = _target_candidates(reserved)
            if len(candidates) == ZERO:
                failed = T
                break
            patch = choice(candidates)
            target_patches.append(patch)
            reserved = combine(reserved, _reserve_patch(patch))
        if failed:
            continue

        for patch in target_patches:
            gi = fill(gi, fgc, patch)
            go = fill(go, fgc, patch)
            go = underfill(go, TWO, _mark_patch(patch))

        nnoise_ub = max(ZERO, FIVE - len(target_patches))
        nnoise = unifint(diff_lb, diff_ub, (ZERO, nnoise_ub))
        for _ in range(nnoise):
            kinds = list(NOISE_KIND_OPTIONS)
            shuffle(kinds)
            placed = F
            for kind in kinds:
                candidates = _noise_candidates(kind, reserved)
                if len(candidates) == ZERO:
                    continue
                patch = choice(candidates)
                gi = fill(gi, fgc, patch)
                go = fill(go, fgc, patch)
                reserved = combine(reserved, _reserve_patch(patch))
                placed = T
                break
            if flip(placed):
                break

        if choice((T, F)):
            gi = hmirror(gi)
            go = hmirror(go)
        if choice((T, F)):
            gi = vmirror(gi)
            go = vmirror(go)
        if gi == go:
            continue
        if mostcolor(gi) != SEVEN:
            continue
        return {"input": gi, "output": go}
