from arc2.core import *


TL2_da6e95e5 = frozenset({ORIGIN, RIGHT, DOWN})
TR2_da6e95e5 = frozenset({ORIGIN, RIGHT, UNITY})
BL2_da6e95e5 = frozenset({ORIGIN, DOWN, UNITY})
BR2_da6e95e5 = frozenset({RIGHT, DOWN, UNITY})

TL3_da6e95e5 = frozenset({ORIGIN, RIGHT, (0, 2), DOWN, (2, 0)})
TR3_da6e95e5 = frozenset({ORIGIN, RIGHT, (0, 2), (1, 2), (2, 2)})
BL3_da6e95e5 = frozenset({ORIGIN, DOWN, (2, 0), (2, 1), (2, 2)})
BR3_da6e95e5 = frozenset({(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)})


def verify_da6e95e5(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = frozenset(
        obj for obj in x0
        if normalize(toindices(obj)) in (TL2_da6e95e5, TL3_da6e95e5)
    )
    x2 = frozenset(
        obj for obj in x0
        if normalize(toindices(obj)) in (TR2_da6e95e5, TR3_da6e95e5)
    )
    x3 = frozenset(
        obj for obj in x0
        if normalize(toindices(obj)) in (BL2_da6e95e5, BL3_da6e95e5)
    )
    x4 = frozenset(
        obj for obj in x0
        if normalize(toindices(obj)) in (BR2_da6e95e5, BR3_da6e95e5)
    )
    x5 = []
    for x6 in x1:
        x7 = color(x6)
        x8 = normalize(toindices(x6))
        x9 = branch(x8 == TL2_da6e95e5, TR2_da6e95e5, TR3_da6e95e5)
        x10 = branch(x8 == TL2_da6e95e5, BL2_da6e95e5, BL3_da6e95e5)
        x11 = branch(x8 == TL2_da6e95e5, BR2_da6e95e5, BR3_da6e95e5)
        x12 = frozenset(
            obj for obj in x2
            if color(obj) == x7
            and normalize(toindices(obj)) == x9
            and uppermost(obj) == uppermost(x6)
            and leftmost(obj) > leftmost(x6)
        )
        x13 = frozenset(
            obj for obj in x3
            if color(obj) == x7
            and normalize(toindices(obj)) == x10
            and leftmost(obj) == leftmost(x6)
            and uppermost(obj) > uppermost(x6)
        )
        if len(x12) == ZERO or len(x13) == ZERO:
            continue
        x14 = argmin(x12, leftmost)
        x15 = argmin(x13, uppermost)
        x16 = frozenset(
            obj for obj in x4
            if color(obj) == x7
            and normalize(toindices(obj)) == x11
            and uppermost(obj) == uppermost(x15)
            and leftmost(obj) == leftmost(x14)
        )
        if len(x16) == ZERO:
            continue
        x17 = lowermost(x6)
        x18 = rightmost(x6)
        x19 = uppermost(x15)
        x20 = leftmost(x14)
        x21 = frozenset(
            (i, j)
            for i in range(x17, x19 + ONE)
            for j in range(x18, x20 + ONE)
            if I[i][j] == x7
        )
        if len(x21) == ZERO:
            continue
        x5.append(x21)
    x22 = argmin(tuple(x5), lambda patch: height(patch) * width(patch))
    x23 = subgrid(x22, I)
    return x23
