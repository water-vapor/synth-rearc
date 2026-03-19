from arc2.core import *


def _basin_patch_db7260a4(
    I: Grid,
    marker_col: Integer,
) -> Indices:
    h = height(I)
    w = width(I)
    cands = []
    for top in range(h - ONE):
        for bottom in range(top + ONE, h):
            for left in range(w - TWO):
                for right in range(left + ONE, w):
                    if not (left < marker_col <= right):
                        continue
                    if right - left < TWO:
                        continue
                    if any(index(I, (i, left)) != TWO for i in range(top, bottom + ONE)):
                        continue
                    if any(index(I, (i, right)) != TWO for i in range(top, bottom + ONE)):
                        continue
                    if any(index(I, (bottom, j)) != TWO for j in range(left, right + ONE)):
                        continue
                    if top > ZERO and index(I, (top - ONE, left)) == TWO and index(I, (top - ONE, right)) == TWO:
                        continue
                    if bottom < h - ONE and index(I, (bottom + ONE, left)) == TWO and index(I, (bottom + ONE, right)) == TWO:
                        continue
                    if any(index(I, (i, j)) != ZERO for i in range(top, bottom) for j in range(left + ONE, right)):
                        continue
                    cands.append((top, bottom, left, right))
    if len(cands) == ZERO:
        return frozenset()
    top, bottom, left, right = min(cands)
    rows = interval(top, bottom, ONE)
    cols = interval(left + ONE, right, ONE)
    return product(rows, cols)


def verify_db7260a4(I: Grid) -> Grid:
    x0 = ofcolor(I, ONE)
    x1 = first(x0)
    x2 = last(x1)
    x3 = fill(I, ZERO, x0)
    x4 = _basin_patch_db7260a4(x3, x2)
    x5 = size(x4)
    x6 = equality(x5, ZERO)
    x7 = height(I)
    x8 = width(I)
    x9 = decrement(x7)
    x10 = decrement(x8)
    x11 = connect((x9, ZERO), (x9, x10))
    x12 = branch(x6, x11, x4)
    x13 = fill(x3, ONE, x12)
    return x13
