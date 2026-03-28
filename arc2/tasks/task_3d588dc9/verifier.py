from arc2.core import *


WEDGE_PATTERNS_3D588DC9 = (
    (FOUR, SIX, FOUR),
    (ONE, ONE, THREE, THREE, THREE, THREE),
    (THREE, THREE, THREE, THREE, ONE, ONE),
)


def _is_wedge_3d588dc9(x0: Object) -> Boolean:
    y0 = toindices(normalize(x0))
    y1 = tuple(sum(1 for i, _ in y0 if i == k) for k in range(height(y0)))
    y2 = tuple(sum(1 for _, j in y0 if j == k) for k in range(width(y0)))
    return both(size(y0) == 14, both(contained(y1, WEDGE_PATTERNS_3D588DC9), contained(y2, WEDGE_PATTERNS_3D588DC9)))


def _row_overlap_3d588dc9(x0: Patch, x1: Patch) -> Integer:
    y0 = {i for i, _ in toindices(x0)}
    y1 = {i for i, _ in toindices(x1)}
    return len(y0 & y1)


def _horizontal_gap_3d588dc9(x0: Patch, x1: Patch) -> Integer:
    y0 = rightmost(x0)
    y1 = leftmost(x0)
    y2 = rightmost(x1)
    y3 = leftmost(x1)
    if y0 < y3:
        return y3 - y0 - ONE
    if y2 < y1:
        return y1 - y2 - ONE
    return ZERO


def _contact_and_tail_3d588dc9(
    x0: Object,
    x1: Boolean,
) -> tuple[Indices, Indices]:
    y0 = toindices(normalize(x0))
    y1 = tuple(sum(1 for i, _ in y0 if i == k) for k in range(height(y0)))
    y2 = tuple(sum(1 for _, j in y0 if j == k) for k in range(width(y0)))
    y3 = ulcorner(x0)
    if height(y0) == THREE:
        y4 = tuple(k for k, v in enumerate(y2) if v == THREE)
        y5 = tuple(k for k, v in enumerate(y2) if v == ONE)
        y6 = min(y4) if x1 else max(y4)
        y7 = frozenset((i, j) for i, j in y0 if j == y6)
        y8 = frozenset((i, j) for i, j in y0 if j in y5)
        return shift(y7, y3), shift(y8, y3)
    y4 = tuple(k for k, v in enumerate(y1) if v == THREE)
    y5 = tuple(k for k, v in enumerate(y1) if v == ONE)
    y6 = min(j for i, j in y0 if i in y4) if x1 else max(j for i, j in y0 if i in y4)
    y7 = frozenset((i, j) for i, j in y0 if both(contained(i, y4), j == y6))
    y8 = frozenset((i, j) for i, j in y0 if contained(i, y5))
    return shift(y7, y3), shift(y8, y3)


def verify_3d588dc9(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = argmax(colorfilter(x0, FIVE), size)
    x2 = colorfilter(x0, ZERO)
    x3 = sfilter(x2, _is_wedge_3d588dc9)
    x4 = argmax(
        x3,
        lambda x: (
            _row_overlap_3d588dc9(x, x1),
            -_horizontal_gap_3d588dc9(x, x1),
            -size(x),
            -manhattan(x, x1),
        ),
    )
    x5 = greater(leftmost(x4), rightmost(x1))
    x6, x7 = _contact_and_tail_3d588dc9(x4, x5)
    x8 = fill(I, mostcolor(I), x7)
    x9 = fill(x8, SIX, x6)
    return x9
