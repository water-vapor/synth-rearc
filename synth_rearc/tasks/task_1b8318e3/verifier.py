from synth_rearc.core import *


def _block_distance_1b8318e3(
    loc: IntegerTuple,
    anchor: Patch,
) -> Integer:
    return manhattan(initset(loc), anchor)


def _preferred_target_1b8318e3(
    loc: IntegerTuple,
    anchor: Patch,
    occupied: set[IntegerTuple],
) -> IntegerTuple:
    i, j = loc
    x0 = uppermost(anchor)
    x1 = lowermost(anchor)
    x2 = leftmost(anchor)
    x3 = rightmost(anchor)
    x4 = x0 - i if i < x0 else i - x1 if i > x1 else ZERO
    x5 = x2 - j if j < x2 else j - x3 if j > x3 else ZERO
    if both(positive(x4), positive(x5)) and equality(x4, x5):
        x6 = decrement(x0) if i < x0 else increment(x1)
        x7 = decrement(x2) if j < x2 else increment(x3)
        return (x6, x7)
    if greater(x4, x5) or equality(x4, x5):
        x6 = decrement(x0) if i < x0 else increment(x1)
        x7 = max(decrement(x2), min(j, increment(x3)))
    else:
        x6 = max(decrement(x0), min(i, increment(x1)))
        x7 = decrement(x2) if j < x2 else increment(x3)
    x8 = x6 in (decrement(x0), increment(x1))
    x9 = x7 in (decrement(x2), increment(x3))
    if both(greater(x4, x5), j < x2) and both(x8, x9):
        x10 = any((x11, decrement(x2)) in occupied for x11 in range(decrement(x0), increment(x1) + ONE))
        if x10:
            x7 = increment(x7)
    return (x6, x7)


def verify_1b8318e3(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, FIVE)
    x2 = sfilter(x1, lambda x3: both(equality(size(x3), FOUR), square(x3)))
    x3 = tuple(sorted(x2, key=lambda x4: (uppermost(x4), leftmost(x4))))
    x4 = mostcolor(I)
    x5 = canvas(x4, shape(I))
    x6 = paint(x5, merge(x3))
    x7 = set(toindices(merge(x3)))
    x8 = tuple(
        sorted(
            (x9 for x9 in asobject(I) if x9[0] != x4 and x9[0] != FIVE),
            key=lambda x10: (x10[1][0], x10[1][1], x10[0]),
        )
    )
    for x9, x10 in x8:
        x11 = tuple(sorted(x3, key=lambda x12: (_block_distance_1b8318e3(x10, x12), uppermost(x12), leftmost(x12))))
        for x12 in x11:
            x13 = _preferred_target_1b8318e3(x10, x12, x7)
            if x13 in x7:
                continue
            x7.add(x13)
            x6 = fill(x6, x9, initset(x13))
            break
    return x6
