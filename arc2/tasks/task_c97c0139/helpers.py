from arc2.core import *


def blue_patch_c97c0139(
    line: Patch,
) -> Indices:
    x0 = toindices(line)
    if len(x0) == ZERO:
        return frozenset()
    x1 = uppermost(x0)
    x2 = lowermost(x0)
    x3 = leftmost(x0)
    x4 = rightmost(x0)
    x5 = branch(hline(x0), subtract(x4, x3), subtract(x2, x1))
    x6 = divide(x5, TWO)
    x7 = frozenset()
    if hline(x0):
        for x8 in interval(ONE, add(x6, ONE), ONE):
            x9 = astuple(subtract(x1, x8), add(x3, x8))
            x10 = astuple(subtract(x1, x8), subtract(x4, x8))
            x11 = astuple(add(x1, x8), add(x3, x8))
            x12 = astuple(add(x1, x8), subtract(x4, x8))
            x13 = connect(x9, x10)
            x14 = connect(x11, x12)
            x7 = combine(x7, combine(x13, x14))
        return x7
    if vline(x0):
        for x8 in interval(ONE, add(x6, ONE), ONE):
            x9 = astuple(add(x1, x8), subtract(x3, x8))
            x10 = astuple(subtract(x2, x8), subtract(x4, x8))
            x11 = astuple(add(x1, x8), add(x3, x8))
            x12 = astuple(subtract(x2, x8), add(x4, x8))
            x13 = connect(x9, x10)
            x14 = connect(x11, x12)
            x7 = combine(x7, combine(x13, x14))
        return x7
    raise ValueError("c97c0139 expects straight red line objects")
