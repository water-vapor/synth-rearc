from synth_rearc.core import *


def _center_patch_9f5f939b(
    center: IntegerTuple,
) -> Indices:
    i, j = center
    return frozenset(
        {
            (i - THREE, j),
            (i - TWO, j),
            (i, j - THREE),
            (i, j - TWO),
            (i, j + TWO),
            (i, j + THREE),
            (i + TWO, j),
            (i + THREE, j),
        }
    )


def _center_reserve_9f5f939b(
    center: IntegerTuple,
    dims: IntegerTuple,
) -> Indices:
    h, w = dims
    i, j = center
    out = set()
    for ni in range(max(ZERO, i - FOUR), min(h, i + FIVE)):
        for nj in range(max(ZERO, j - FOUR), min(w, j + FIVE)):
            out.add((ni, nj))
    return frozenset(out)


def _domino_patch_9f5f939b(
    loc: IntegerTuple,
    horizontal: Boolean,
) -> Indices:
    i, j = loc
    if horizontal:
        return frozenset({(i, j), (i, j + ONE)})
    return frozenset({(i, j), (i + ONE, j)})


def _domino_reserve_9f5f939b(
    patch: Indices,
    dims: IntegerTuple,
) -> Indices:
    h, w = dims
    out = set()
    for i, j in patch:
        for di in (-ONE, ZERO, ONE):
            for dj in (-ONE, ZERO, ONE):
                ni, nj = i + di, j + dj
                if ZERO <= ni < h and ZERO <= nj < w:
                    out.add((ni, nj))
    return frozenset(out)


def _find_centers_9f5f939b(
    grid: Grid,
) -> Indices:
    x0 = objects(grid, T, F, T)
    x1 = colorfilter(x0, ONE)
    x2 = sizefilter(x1, TWO)
    x3 = sfilter(x2, hline)
    x4 = sfilter(x2, vline)
    x5 = apply(lrcorner, x3)
    x6 = apply(rbind(add, (ZERO, TWO)), x5)
    x7 = apply(ulcorner, x3)
    x8 = apply(rbind(add, (ZERO, -TWO)), x7)
    x9 = intersection(x6, x8)
    x10 = apply(llcorner, x4)
    x11 = apply(rbind(add, (TWO, ZERO)), x10)
    x12 = apply(ulcorner, x4)
    x13 = apply(rbind(add, (-TWO, ZERO)), x12)
    x14 = intersection(x11, x13)
    x15 = intersection(x9, x14)
    return intersection(x15, ofcolor(grid, EIGHT))


def _noise_candidates_9f5f939b(
    dims: IntegerTuple,
    reserved: Indices,
) -> tuple[tuple[Indices, Indices], ...]:
    h, w = dims
    out = []
    for i in range(h):
        for j in range(w - ONE):
            patch = _domino_patch_9f5f939b((i, j), T)
            if len(intersection(patch, reserved)) > ZERO:
                continue
            out.append((patch, _domino_reserve_9f5f939b(patch, dims)))
    for i in range(h - ONE):
        for j in range(w):
            patch = _domino_patch_9f5f939b((i, j), F)
            if len(intersection(patch, reserved)) > ZERO:
                continue
            out.append((patch, _domino_reserve_9f5f939b(patch, dims)))
    return tuple(out)


def generate_9f5f939b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        n = choice((EIGHT, double(EIGHT), double(EIGHT), double(EIGHT), double(TEN)))
        dims = (n, n)
        gi = canvas(EIGHT, dims)
        reserved = frozenset()
        centers = []
        ncenters = ONE
        if both(greater(n, double(SIX)), choice((T, F))):
            ncenters = increment(ncenters)
        if both(greater(n, double(EIGHT)), choice((T, F, F))):
            ncenters = increment(ncenters)

        candidates = [(i, j) for i in range(THREE, n - THREE) for j in range(THREE, n - THREE)]
        shuffle(candidates)
        for center in candidates:
            patch = _center_patch_9f5f939b(center)
            reserve = _center_reserve_9f5f939b(center, dims)
            if len(intersection(reserve, reserved)) > ZERO:
                continue
            gi = fill(gi, ONE, patch)
            reserved = combine(reserved, reserve)
            centers.append(center)
            if len(centers) == ncenters:
                break
        if len(centers) != ncenters:
            continue

        nnoise = unifint(diff_lb, diff_ub, (ZERO, max(TWO, halve(n))))
        for _ in range(nnoise):
            candidates = _noise_candidates_9f5f939b(dims, reserved)
            if len(candidates) == ZERO:
                break
            patch, reserve = choice(candidates)
            gi = fill(gi, ONE, patch)
            reserved = combine(reserved, reserve)

        intended = frozenset(centers)
        detected = _find_centers_9f5f939b(gi)
        if detected != intended:
            continue

        go = fill(gi, FOUR, intended)
        if choice((T, F)):
            gi = hmirror(gi)
            go = hmirror(go)
        if choice((T, F)):
            gi = vmirror(gi)
            go = vmirror(go)
        if _find_centers_9f5f939b(gi) != ofcolor(go, FOUR):
            continue
        return {"input": gi, "output": go}
