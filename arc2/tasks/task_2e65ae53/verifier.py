from arc2.core import *


def _frame_signature_2e65ae53(
    I: Grid,
    obj: Object,
) -> tuple[int, int, int, int, int, int] | None:
    x0 = toindices(obj)
    x1 = uppermost(x0)
    x2 = lowermost(x0)
    x3 = leftmost(x0)
    x4 = rightmost(x0)
    x5 = color(obj)
    x6 = tuple(
        x7 for x7 in range(x1, x2 + ONE)
        if all(index(I, (x7, x8)) == x5 for x8 in range(x3, x4 + ONE))
    )
    x7 = tuple(
        x8 for x8 in range(x3, x4 + ONE)
        if all(index(I, (x9, x8)) == x5 for x9 in range(x1, x2 + ONE))
    )
    if len(x6) != THREE or len(x7) != THREE:
        return None
    if x6[ZERO] != x1 or x6[-ONE] != x2:
        return None
    if x7[ZERO] != x3 or x7[-ONE] != x4:
        return None
    x8 = box(x0)
    x9 = connect((x6[ONE], x3), (x6[ONE], x4))
    x10 = connect((x1, x7[ONE]), (x2, x7[ONE]))
    x11 = combine(combine(x8, x9), x10)
    if x11 != x0:
        return None
    return (x1, x6[ONE], x2, x3, x7[ONE], x4)


def _quadrants_2e65ae53(
    sig: tuple[int, int, int, int, int, int],
) -> tuple[Indices, Indices, Indices, Indices]:
    x0, x1, x2, x3, x4, x5 = sig
    x6 = frozenset((x7, x8) for x7 in range(x0 + ONE, x1) for x8 in range(x3 + ONE, x4))
    x7 = frozenset((x8, x9) for x8 in range(x0 + ONE, x1) for x9 in range(x4 + ONE, x5))
    x8 = frozenset((x9, x10) for x9 in range(x1 + ONE, x2) for x10 in range(x3 + ONE, x4))
    x9 = frozenset((x10, x11) for x10 in range(x1 + ONE, x2) for x11 in range(x4 + ONE, x5))
    return (x6, x7, x8, x9)


def verify_2e65ae53(I: Grid) -> Grid:
    x0 = objects(I, T, F, F)
    x1 = sfilter(x0, compose(flip, matcher(color, ZERO)))
    x2 = []
    for x3 in x1:
        x4 = _frame_signature_2e65ae53(I, x3)
        if x4 is not None:
            x2.append(x4)
    x5 = [None, None, None, None]
    for x6 in x2:
        x7 = _quadrants_2e65ae53(x6)
        for x8, x9 in enumerate(x7):
            x10 = frozenset(index(I, x11) for x11 in x9) - {ZERO}
            if len(x10) == ONE:
                x5[x8] = first(x10)
    x11 = I
    for x12 in x2:
        x13 = _quadrants_2e65ae53(x12)
        for x14, x15 in enumerate(x13):
            x11 = fill(x11, x5[x14], x15)
    return x11
