from arc2.core import *


def _yellow_patch_9772c176(
    obj: Object,
    dims: IntegerTuple,
) -> Indices:
    h, w = dims
    rows = {}
    cols = {}
    for _, (i, j) in obj:
        rows.setdefault(i, []).append(j)
        cols.setdefault(j, []).append(i)
    patch = set()
    top = min(rows)
    bottom = max(rows)
    left = min(cols)
    right = max(cols)
    lft = min(rows[top])
    rgt = max(rows[top])
    step = ONE
    while top - step >= ZERO and lft + step <= rgt - step:
        ii = top - step
        for jj in range(lft + step, rgt - step + ONE):
            patch.add((ii, jj))
        step += ONE
    lft = min(rows[bottom])
    rgt = max(rows[bottom])
    step = ONE
    while bottom + step < h and lft + step <= rgt - step:
        ii = bottom + step
        for jj in range(lft + step, rgt - step + ONE):
            patch.add((ii, jj))
        step += ONE
    topc = min(cols[left])
    botc = max(cols[left])
    step = ONE
    while left - step >= ZERO and topc + step <= botc - step:
        jj = left - step
        for ii in range(topc + step, botc - step + ONE):
            patch.add((ii, jj))
        step += ONE
    topc = min(cols[right])
    botc = max(cols[right])
    step = ONE
    while right + step < w and topc + step <= botc - step:
        jj = right + step
        for ii in range(topc + step, botc - step + ONE):
            patch.add((ii, jj))
        step += ONE
    return frozenset(patch)


def verify_9772c176(I: Grid) -> Grid:
    x0 = shape(I)
    x1 = objects(I, T, F, T)
    x2 = colorfilter(x1, EIGHT)
    x3 = I
    for x4 in x2:
        x5 = _yellow_patch_9772c176(x4, x0)
        x3 = fill(x3, FOUR, x5)
    return x3
