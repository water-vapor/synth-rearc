from synth_rearc.core import *


PALETTE_1B8318E3 = remove(FIVE, remove(ZERO, interval(ZERO, TEN, ONE)))


def _block_1b8318e3(anchor: IntegerTuple) -> Indices:
    ai, aj = anchor
    return frozenset((ai + di, aj + dj) for di in range(TWO) for dj in range(TWO))


def _halo_1b8318e3(
    anchor: IntegerTuple,
    dims: IntegerTuple,
) -> Indices:
    h, w = dims
    return frozenset(
        (i, j)
        for i, j in outbox(_block_1b8318e3(anchor))
        if ZERO <= i < h and ZERO <= j < w
    )


def _anchor_distance_1b8318e3(
    loc: IntegerTuple,
    anchor: IntegerTuple,
) -> Integer:
    patch = _block_1b8318e3(anchor)
    return manhattan(initset(loc), patch)


def _nearest_anchor_1b8318e3(
    loc: IntegerTuple,
    anchors: tuple[IntegerTuple, ...],
) -> IntegerTuple:
    return min(
        anchors,
        key=lambda x1: (
            _anchor_distance_1b8318e3(loc, x1),
            x1[0],
            x1[1],
        ),
    )


def _assigned_target_1b8318e3(
    loc: IntegerTuple,
    anchor: IntegerTuple,
    occupied: set[IntegerTuple],
) -> IntegerTuple:
    i, j = loc
    x0, x2 = anchor
    x1, x3 = x0 + ONE, x2 + ONE
    x4 = x0 - i if i < x0 else i - x1 if i > x1 else ZERO
    x5 = x2 - j if j < x2 else j - x3 if j > x3 else ZERO
    if x4 > ZERO and x5 > ZERO and x4 == x5:
        x6 = x0 - ONE if i < x0 else x1 + ONE
        x7 = x2 - ONE if j < x2 else x3 + ONE
        return (x6, x7)
    if x4 >= x5:
        x6 = x0 - ONE if i < x0 else x1 + ONE
        x7 = min(max(j, x2 - ONE), x3 + ONE)
    else:
        x6 = min(max(i, x0 - ONE), x1 + ONE)
        x7 = x2 - ONE if j < x2 else x3 + ONE
    x8 = x6 in (x0 - ONE, x1 + ONE)
    x9 = x7 in (x2 - ONE, x3 + ONE)
    if x4 > x5 and j < x2 and x8 and x9:
        x10 = any((x11, x2 - ONE) in occupied for x11 in range(x0 - ONE, x1 + TWO))
        if x10:
            x7 += ONE
    return (x6, x7)


def _solve_layout_1b8318e3(
    dims: IntegerTuple,
    anchors: tuple[IntegerTuple, ...],
    sources: tuple[tuple[IntegerTuple, Integer], ...],
) -> tuple[Grid, tuple[tuple[IntegerTuple, Integer, IntegerTuple, IntegerTuple], ...], dict[IntegerTuple, Integer]]:
    occupied = set()
    go = canvas(ZERO, dims)
    for anchor in anchors:
        patch = _block_1b8318e3(anchor)
        occupied |= patch
        go = fill(go, FIVE, patch)
    placed = []
    counts = {anchor: ZERO for anchor in anchors}
    x0 = tuple(sorted(sources, key=lambda x1: (x1[0][0], x1[0][1], x1[1])))
    for loc, color_value in x0:
        x1 = tuple(sorted(anchors, key=lambda x2: (_anchor_distance_1b8318e3(loc, x2), x2[0], x2[1])))
        for anchor in x1:
            target = _assigned_target_1b8318e3(loc, anchor, occupied)
            if target in occupied:
                continue
            occupied.add(target)
            counts[anchor] += ONE
            go = fill(go, color_value, initset(target))
            placed.append((loc, color_value, anchor, target))
            break
    return go, tuple(placed), counts


def _source_candidates_1b8318e3(
    dims: IntegerTuple,
    anchors: tuple[IntegerTuple, ...],
    anchor: IntegerTuple,
    target: IntegerTuple,
    blocked: set[IntegerTuple],
) -> tuple[IntegerTuple, ...]:
    h, w = dims
    anchor_cells = set()
    for anchor0 in anchors:
        anchor_cells |= _block_1b8318e3(anchor0)
    cands = []
    for i in range(h):
        for j in range(w):
            loc = (i, j)
            if loc in blocked or loc in anchor_cells:
                continue
            if _nearest_anchor_1b8318e3(loc, anchors) != anchor:
                continue
            if _assigned_target_1b8318e3(loc, anchor, anchor_cells) != target:
                continue
            cands.append(loc)
    return tuple(cands)


def _place_anchors_1b8318e3(
    dims: IntegerTuple,
    nanchors: Integer,
) -> tuple[IntegerTuple, ...] | None:
    h, w = dims
    cands = [(i, j) for i in range(h - ONE) for j in range(w - ONE)]
    shuffle(cands)
    anchors = []
    for cand in cands:
        if all(abs(cand[0] - other[0]) > THREE or abs(cand[1] - other[1]) > THREE for other in anchors):
            anchors.append(cand)
            if len(anchors) == nanchors:
                return tuple(sorted(anchors))
    return None


def generate_1b8318e3(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        side = unifint(diff_lb, diff_ub, (TEN, 15))
        dims = (side, side)
        if side <= 11:
            nanchors = THREE
        elif side <= 13:
            nanchors = unifint(diff_lb, diff_ub, (THREE, FOUR))
        else:
            nanchors = unifint(diff_lb, diff_ub, (FOUR, SIX))
        anchors = _place_anchors_1b8318e3(dims, nanchors)
        if anchors is None:
            continue
        x0 = max(FIVE, nanchors)
        x1 = min(12, multiply(nanchors, FOUR))
        if x1 < x0:
            continue
        nsources = unifint(diff_lb, diff_ub, (x0, x1))
        counts = {anchor: ONE for anchor in anchors}
        x2 = subtract(nsources, nanchors)
        x3 = list(anchors)
        shuffle(x3)
        for anchor in x3:
            if x2 == ZERO:
                break
            x4 = min(x2, subtract(FOUR, counts[anchor]))
            if x4 == ZERO:
                continue
            x5 = choice(interval(ONE, increment(x4), ONE))
            counts[anchor] = add(counts[anchor], x5)
            x2 = subtract(x2, x5)
        if x2 != ZERO:
            continue
        ncolors = min(nsources, unifint(diff_lb, diff_ub, (THREE, EIGHT)))
        palette0 = sample(PALETTE_1B8318E3, ncolors)
        anchor_cells = set()
        for anchor in anchors:
            anchor_cells |= _block_1b8318e3(anchor)
        chosen_targets = []
        for anchor in anchors:
            x4 = tuple(
                sorted(
                    {
                        _assigned_target_1b8318e3(loc, anchor, anchor_cells)
                        for loc in (
                            (i, j)
                            for i in range(dims[ZERO])
                            for j in range(dims[ONE])
                            if (i, j) not in anchor_cells and _nearest_anchor_1b8318e3((i, j), anchors) == anchor
                        )
                    }
                )
            )
            if len(x4) < counts[anchor]:
                chosen_targets = []
                break
            x5 = list(x4)
            shuffle(x5)
            x6 = tuple(x5[:counts[anchor]])
            for target in x6:
                chosen_targets.append((anchor, target))
        if len(chosen_targets) != nsources:
            continue
        target_set = {target for _, target in chosen_targets}
        blocked = set(anchor_cells) | target_set
        sources = {}
        x4 = list(chosen_targets)
        shuffle(x4)
        x4.sort(key=lambda x5: len(_source_candidates_1b8318e3(dims, anchors, x5[ZERO], x5[ONE], blocked - {x5[ONE]})))
        failed = False
        for anchor, target in x4:
            x5 = (blocked | set(sources.values())) - {target}
            cands = _source_candidates_1b8318e3(dims, anchors, anchor, target, x5)
            if len(cands) == ZERO:
                failed = True
                break
            sources[(anchor, target)] = choice(cands)
        if failed:
            continue
        gi = canvas(ZERO, dims)
        go = canvas(ZERO, dims)
        for anchor in anchors:
            patch = _block_1b8318e3(anchor)
            gi = fill(gi, FIVE, patch)
            go = fill(go, FIVE, patch)
        shuffle(chosen_targets)
        for anchor, target in chosen_targets:
            color_value = choice(palette0)
            loc = sources[(anchor, target)]
            gi = fill(gi, color_value, initset(loc))
            go = fill(go, color_value, initset(target))
        x4, _, _ = _solve_layout_1b8318e3(
            dims,
            anchors,
            tuple((sources[(anchor, target)], index(go, target)) for anchor, target in chosen_targets),
        )
        if x4 != go:
            continue
        if gi == go:
            continue
        return {"input": gi, "output": go}
