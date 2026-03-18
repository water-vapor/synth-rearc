from arc2.core import *


def _side_13f06aa5(
    obj: Object,
    tip: Object,
) -> str:
    if uppermost(tip) == uppermost(obj):
        return "top"
    if lowermost(tip) == lowermost(obj):
        return "bottom"
    if leftmost(tip) == leftmost(obj):
        return "left"
    return "right"


def _trace_13f06aa5(
    loc: IntegerTuple,
    side: str,
    dims: IntegerTuple,
) -> Indices:
    h, w = dims
    i, j = loc
    if side == "top":
        return frozenset((k, j) for k in range(i - TWO, ZERO, -TWO))
    if side == "bottom":
        return frozenset((k, j) for k in range(i + TWO, h - ONE, TWO))
    if side == "left":
        return frozenset((i, k) for k in range(j - TWO, ZERO, -TWO))
    return frozenset((i, k) for k in range(j + TWO, w - ONE, TWO))


def _border_13f06aa5(
    side: str,
    dims: IntegerTuple,
) -> Indices:
    h, w = dims
    if side == "top":
        return frozenset((ZERO, j) for j in range(w))
    if side == "bottom":
        return frozenset((h - ONE, j) for j in range(w))
    if side == "left":
        return frozenset((i, ZERO) for i in range(h))
    return frozenset((i, w - ONE) for i in range(h))


def _corners_13f06aa5(
    sides: set[str],
    dims: IntegerTuple,
) -> Indices:
    h, w = dims
    out = set()
    if "top" in sides and "left" in sides:
        out.add((ZERO, ZERO))
    if "top" in sides and "right" in sides:
        out.add((ZERO, w - ONE))
    if "bottom" in sides and "left" in sides:
        out.add((h - ONE, ZERO))
    if "bottom" in sides and "right" in sides:
        out.add((h - ONE, w - ONE))
    return frozenset(out)


def verify_13f06aa5(I: Grid) -> Grid:
    x0 = shape(I)
    x1 = objects(I, F, F, T)
    x2 = I
    x3 = set()
    for x4 in x1:
        x5 = leastcolor(x4)
        x6 = sfilter(x4, matcher(first, x5))
        x7 = ulcorner(x6)
        x8 = _side_13f06aa5(x4, x6)
        x9 = _trace_13f06aa5(x7, x8, x0)
        x10 = _border_13f06aa5(x8, x0)
        x2 = fill(x2, x5, x9)
        x2 = fill(x2, x5, x10)
        x3.add(x8)
    x11 = _corners_13f06aa5(x3, x0)
    x12 = fill(x2, ZERO, x11)
    return x12
