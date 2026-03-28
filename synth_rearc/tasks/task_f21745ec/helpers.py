from synth_rearc.core import *


def box_patch_f21745ec(
    loc: IntegerTuple,
    dims: IntegerTuple,
) -> Patch:
    x0 = (loc[0] + dims[0] - ONE, loc[1] + dims[1] - ONE)
    x1 = frozenset({loc, x0})
    x2 = box(x1)
    return x2


def pattern_patch_f21745ec(
    dims: IntegerTuple,
    inner_patch: Patch,
) -> Patch:
    x0 = box_patch_f21745ec((ZERO, ZERO), dims)
    x1 = shift(inner_patch, (ONE, ONE))
    x2 = combine(x0, x1)
    return x2


def _expanded_patch_f21745ec(
    loc: IntegerTuple,
    dims: IntegerTuple,
    side: Integer,
) -> Patch:
    rows = range(max(ZERO, loc[0] - ONE), min(side, loc[0] + dims[0] + ONE))
    cols = range(max(ZERO, loc[1] - ONE), min(side, loc[1] + dims[1] + ONE))
    return frozenset((i, j) for i in rows for j in cols)


def _neighbors_f21745ec(
    loc: IntegerTuple,
    dims: IntegerTuple,
) -> Tuple:
    x0 = []
    for di, dj in (UP, DOWN, LEFT, RIGHT):
        ii = loc[0] + di
        jj = loc[1] + dj
        if 0 <= ii < dims[0] and 0 <= jj < dims[1]:
            x0.append((ii, jj))
    return tuple(x0)


def sample_inner_patch_f21745ec(
    diff_lb: float,
    diff_ub: float,
    dims: IntegerTuple,
) -> Patch:
    area = multiply(dims[0], dims[1])
    lower = max(TWO, area // THREE)
    upper = min(area - ONE, max(lower, (area * THREE) // FIVE))
    boundary = frozenset(
        (i, j)
        for i in range(dims[0])
        for j in range(dims[1])
        if i in (ZERO, dims[0] - ONE) or j in (ZERO, dims[1] - ONE)
    )
    while True:
        target = unifint(diff_lb, diff_ub, (lower, upper))
        patch = frozenset({choice(totuple(boundary))})
        frontier = patch
        steps = ZERO
        while len(patch) < target and steps < area * TEN:
            steps += ONE
            current = choice(totuple(frontier if len(frontier) else patch))
            neighbors = tuple(
                loc
                for loc in _neighbors_f21745ec(current, dims)
                if loc not in patch
            )
            if len(neighbors) == ZERO:
                frontier = sfilter(
                    frontier,
                    lambda loc: any(
                        nbr not in patch
                        for nbr in _neighbors_f21745ec(loc, dims)
                    ),
                )
                continue
            nxt = choice(neighbors)
            patch = insert(nxt, patch)
            frontier = insert(nxt, frontier)
            frontier = sfilter(
                frontier,
                lambda loc: any(
                    nbr not in patch
                    for nbr in _neighbors_f21745ec(loc, dims)
                ),
            )
        if len(patch) != target:
            continue
        if height(patch) == ONE or width(patch) == ONE:
            continue
        return patch


def place_boxes_f21745ec(
    side: Integer,
    dims_seq: Tuple,
) -> Tuple | None:
    order_ids = list(range(len(dims_seq)))
    shuffle(order_ids)
    order_ids.sort(key=lambda idx: dims_seq[idx][0] * dims_seq[idx][1], reverse=True)
    forbidden = frozenset()
    locs = [None] * len(dims_seq)
    for idx in order_ids:
        dims = dims_seq[idx]
        candidates = []
        for i in range(side - dims[0] + ONE):
            for j in range(side - dims[1] + ONE):
                rect = frozenset(
                    (ii, jj)
                    for ii in range(i, i + dims[0])
                    for jj in range(j, j + dims[1])
                )
                if len(intersection(rect, forbidden)) == ZERO:
                    candidates.append((i, j))
        if len(candidates) == ZERO:
            return None
        loc = choice(candidates)
        locs[idx] = loc
        forbidden = combine(forbidden, _expanded_patch_f21745ec(loc, dims, side))
    return tuple(locs)
