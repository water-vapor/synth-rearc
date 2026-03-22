from __future__ import annotations

from collections import Counter, defaultdict

from arc2.core import *


def _period_score_6cbe9eb8(
    I: Grid,
    axis: Integer,
    step: Integer,
) -> float:
    x0 = height(I)
    x1 = width(I)
    x2 = x0 if axis == ZERO else x1
    x3 = ZERO
    x4 = ZERO
    if axis == ZERO:
        for x5 in range(x0 - step):
            for x6 in range(x1):
                x3 += ONE
                if I[x5][x6] != I[x5 + step][x6]:
                    x4 += ONE
    else:
        for x5 in range(x0):
            for x6 in range(x1 - step):
                x3 += ONE
                if I[x5][x6] != I[x5][x6 + step]:
                    x4 += ONE
    return (x4 / x3) + (step / x2)


def _infer_period_6cbe9eb8(
    I: Grid,
    axis: Integer,
) -> Integer:
    x0 = height(I)
    x1 = width(I)
    x2 = x0 if axis == ZERO else x1
    x3 = None
    x4 = ONE
    for x5 in range(ONE, x2):
        x6 = _period_score_6cbe9eb8(I, axis, x5)
        if x3 is None or x6 < x3:
            x3 = x6
            x4 = x5
    return x4


def _largest_components_by_color_6cbe9eb8(
    I: Grid,
    colors: frozenset[Integer],
) -> dict[Integer, tuple[IntegerTuple, ...]]:
    x0 = height(I)
    x1 = width(I)
    x2 = set()
    x3 = defaultdict(list)
    for x4 in range(x0):
        for x5 in range(x1):
            x6 = I[x4][x5]
            x7 = astuple(x4, x5)
            if x6 not in colors or x7 in x2:
                continue
            x8 = [x7]
            x2.add(x7)
            x9 = []
            while len(x8) > ZERO:
                x10 = x8.pop()
                x9.append(x10)
                x11, x12 = x10
                for x13, x14 in ((x11 - ONE, x12), (x11 + ONE, x12), (x11, x12 - ONE), (x11, x12 + ONE)):
                    x15 = astuple(x13, x14)
                    if x13 < ZERO or x13 >= x0 or x14 < ZERO or x14 >= x1:
                        continue
                    if x15 in x2 or I[x13][x14] != x6:
                        continue
                    x2.add(x15)
                    x8.append(x15)
            x3[x6].append(tuple(x9))
    return {x16: max(x17, key=len) for x16, x17 in x3.items()}


def verify_6cbe9eb8(
    I: Grid,
) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = _infer_period_6cbe9eb8(I, ZERO)
    x3 = _infer_period_6cbe9eb8(I, ONE)
    x4 = {}
    for x5 in range(x2):
        for x6 in range(x3):
            x7 = [I[x8][x9] for x8 in range(x5, x0, x2) for x9 in range(x6, x1, x3)]
            x4[(x5, x6)] = Counter(x7).most_common(ONE)[ZERO][ZERO]
    x8 = frozenset(x4.values())
    x9 = frozenset({x10 for x11 in I for x10 in x11 if x10 not in x8})
    x10 = _largest_components_by_color_6cbe9eb8(I, x9)
    x11 = []
    for x12, x13 in x10.items():
        x14 = tuple(x15[ZERO] for x15 in x13)
        x16 = tuple(x17[ONE] for x17 in x13)
        x18 = min(x14)
        x19 = max(x14)
        x20 = min(x16)
        x21 = max(x16)
        x22 = x19 - x18 + ONE
        x23 = x21 - x20 + ONE
        x24 = x22 * x23
        x25 = x24 if x22 == ONE or x23 == ONE else (TWO * (x22 + x23)) - FOUR
        x26 = abs(len(x13) - x25) <= abs(x24 - len(x13))
        x11.append((x24, x22, x23, x12, x26))
    x27 = tuple(sorted(x11, reverse=T))
    x28 = canvas(ZERO, astuple(x27[ZERO][ONE], x27[ZERO][TWO]))
    x29 = None
    for _, x30, x31, x32, x33 in x27:
        if x29 is None:
            x34 = ZERO
            x35 = ZERO
        else:
            x36, x37, x38, x39, x40 = x29
            if x40:
                x41 = x36 + ONE
                x42 = x37 + ONE
                x43 = x38 - TWO
                x44 = x39 - TWO
            else:
                x41 = x36
                x42 = x37
                x43 = x38
                x44 = x39
            x34 = x41 + x43 - x30
            x35 = x42
        x45 = astuple(x34, x35)
        x46 = astuple(x34 + x30 - ONE, x35 + x31 - ONE)
        x47 = frozenset({x45, x46})
        x48 = box(x47) if both(x33, greater(x30, ONE)) and both(x33, greater(x31, ONE)) else backdrop(x47)
        x28 = fill(x28, x32, x48)
        x29 = (x34, x35, x30, x31, x33)
    return x28
