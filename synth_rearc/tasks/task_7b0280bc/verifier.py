from __future__ import annotations

from collections import Counter, deque

from synth_rearc.core import *


def _is_two_by_two_7b0280bc(
    obj: Object,
) -> Boolean:
    return square(obj) and size(obj) > ONE


def _touches_8_7b0280bc(
    a: Patch,
    b: Patch,
) -> Boolean:
    x0 = toindices(b)
    for x1 in toindices(a):
        if positive(size(intersection(neighbors(x1), x0))):
            return True
    return False


def verify_7b0280bc(
    I: Grid,
) -> Grid:
    x0 = tuple(sorted(objects(I, T, F, T), key=lambda x1: (ulcorner(x1), size(x1), color(x1))))
    x1 = tuple(x2 for x2 in x0 if _is_two_by_two_7b0280bc(x2))
    x2 = mostcommon(tuple(size(x3) for x3 in x1))
    x3 = tuple(x4 for x4 in x1 if equality(size(x4), x2))
    x4 = Counter(color(x5) for x5 in x3)
    x5 = tuple(sorted(x4))
    x6 = argmin(x5, lambda x7: x4[x7])
    x7 = other(x5, x6)
    x8 = tuple(x9 for x9 in x3 if equality(color(x9), x6))
    x9 = first(tuple(sorted(difference(palette(I), frozenset({mostcolor(I), x6, x7})))))
    x10 = {x11: x12 for x11, x12 in enumerate(x0)}
    x11 = {
        x12: tuple(
            x13
            for x13 in x10
            if x13 != x12 and _touches_8_7b0280bc(x10[x12], x10[x13])
        )
        for x12 in x10
    }
    x12 = {x13: x14 for x14, x13 in x10.items()}
    x13 = x12[x8[ZERO]]
    x14 = x12[x8[ONE]]
    x15 = deque((x13,))
    x16 = {x13: None}
    while len(x15) > ZERO:
        x17 = x15.popleft()
        if equality(x17, x14):
            break
        for x18 in x11[x17]:
            if x18 in x16:
                continue
            x16[x18] = x17
            x15.append(x18)
    x19 = []
    x20 = x14
    while x20 is not None:
        x19.append(x20)
        x20 = x16[x20]
    x21 = tuple(reversed(x19))
    x22 = I
    for x23 in x21[ONE:-ONE]:
        x24 = x10[x23]
        x25 = color(x24)
        if equality(x25, x7):
            x22 = paint(x22, recolor(THREE, x24))
        elif equality(x25, x9):
            x22 = paint(x22, recolor(FIVE, x24))
    return x22
