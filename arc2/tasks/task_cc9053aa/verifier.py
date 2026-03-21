from collections import deque

from arc2.core import *


def _safe_cells_and_entries_cc9053aa(
    I: Grid,
):
    x0 = ofcolor(I, EIGHT)
    x1 = ofcolor(I, SEVEN)
    x2 = ofcolor(I, NINE)
    x3 = frozenset(x4 for x4 in x0 if len(dneighbors(x4) & x1) > ZERO)
    x4 = difference(x0, x3)
    x5 = tuple(sorted({x7 for x6 in x2 for x7 in dneighbors(x6) if x7 in x0}))
    return x4, x5


def _path_cc9053aa(
    I: Grid,
):
    x0, x1 = _safe_cells_and_entries_cc9053aa(I)
    x2 = x1[ZERO]
    x3 = x1[ONE]
    x4 = ofcolor(I, SEVEN)

    def x5(start):
        x6 = deque((start,))
        x7 = {start: ZERO}
        while len(x6) > ZERO:
            x8 = x6.popleft()
            for x9 in dneighbors(x8):
                if x9 not in x0 or x9 in x7:
                    continue
                x7[x9] = x7[x8] + ONE
                x6.append(x9)
        return x7

    x6 = x5(x2)
    x7 = x5(x3)
    x8 = x6[x3]
    x9 = {
        x10: min(abs(x10[ZERO] - x11[ZERO]) + abs(x10[ONE] - x11[ONE]) for x11 in x4)
        for x10 in x0
    }
    x10 = {x3: (x9[x3], x9[x3], (x3,))}
    for x11 in range(x8 - ONE, -ONE, -ONE):
        x12 = [
            x13 for x13 in x0
            if x6.get(x13) == x11 and x6.get(x13, 999) + x7.get(x13, 999) == x8
        ]
        for x13 in sorted(x12, reverse=True):
            x14 = []
            for x15 in dneighbors(x13):
                if x6.get(x15) != x11 + ONE or x6.get(x15, 999) + x7.get(x15, 999) != x8:
                    continue
                if x15 not in x10:
                    continue
                x16 = x10[x15]
                x17 = (
                    min(x9[x13], x16[ZERO]),
                    x9[x13] + x16[ONE],
                    (x13,) + x16[TWO],
                )
                x14.append(x17)
            x10[x13] = max(x14)
    return frozenset(x10[x2][TWO])


def verify_cc9053aa(
    I: Grid,
) -> Grid:
    x0 = _path_cc9053aa(I)
    x1 = fill(I, NINE, x0)
    return x1
