from collections import Counter

from synth_rearc.core import *


def _high_cluster_min_8dab14c2(
    counts: tuple[Integer, ...],
) -> Integer:
    x0 = tuple(sorted({x1 for x1 in counts if x1 > ZERO}))
    if len(x0) == ONE:
        return x0[0]
    x1 = NEG_ONE
    x2 = x0[1]
    for x3, x4 in zip(x0, x0[1:]):
        x5 = subtract(x4, x3)
        if x5 > x1 or both(equality(x5, x1), x4 > x2):
            x1 = x5
            x2 = x4
    return x2


def _mode_8dab14c2(
    values: tuple[Integer, ...],
) -> Integer:
    x0 = Counter(values)
    return max(x0.items(), key=lambda x1: (x1[1], -x1[0]))[0]


def _paint_cell_8dab14c2(
    grid: Grid,
    value: Integer,
    loc: IntegerTuple,
) -> Grid:
    return fill(grid, value, frozenset({loc}))


def verify_8dab14c2(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = other(palette(I), x0)
    x2 = height(I)
    x3 = width(I)
    x4 = tuple(sum(v == x1 for v in row) for row in I)
    x5 = _high_cluster_min_8dab14c2(x4)
    x6 = tuple(i for i, x7 in enumerate(x4) if x7 >= x5)
    x7 = min(x6)
    x8 = max(x6)
    x9 = tuple(sum(I[i][j] == x1 for i in range(x2)) for j in range(x3))
    x10 = _high_cluster_min_8dab14c2(x9)
    x11 = tuple(j for j, x12 in enumerate(x9) if x12 >= x10)
    x12 = min(x11)
    x13 = max(x11)
    x14 = ofcolor(I, x1)
    x15 = min(i for i, _ in x14)
    x16 = max(i for i, _ in x14)
    x17 = min(j for _, j in x14)
    x18 = max(j for _, j in x14)
    x19 = subtract(x7, x15) <= subtract(x16, x8)
    x20 = subtract(x12, x17) <= subtract(x18, x13)
    x21 = tuple(tuple(j for j in range(x3) if I[i][j] == x1) for i in range(x2))
    x22 = tuple(tuple(i for i in range(x2) if I[i][j] == x1) for j in range(x3))
    if x20:
        x23 = x12
        x24 = _mode_8dab14c2(tuple(max(x21[i]) for i in range(x7, add(x8, ONE))))
    else:
        x23 = _mode_8dab14c2(tuple(min(x21[i]) for i in range(x7, add(x8, ONE))))
        x24 = x13
    if x19:
        x25 = x7
        x26 = _mode_8dab14c2(tuple(max(x22[j]) for j in range(x12, add(x13, ONE))))
    else:
        x25 = _mode_8dab14c2(tuple(min(x22[j]) for j in range(x12, add(x13, ONE))))
        x26 = x8
    x27 = tuple(j for j in range(x23, add(x24, ONE)) if not x12 <= j <= x13)
    x28 = tuple(i for i in range(x25, add(x26, ONE)) if not x7 <= i <= x8)
    x29 = I
    for x30 in range(x7, add(x8, ONE)):
        if x23 > ZERO and I[x30][decrement(x23)] == x1:
            x29 = _paint_cell_8dab14c2(x29, x0, (x30, x24))
        if I[x30][x23] == x0:
            x29 = _paint_cell_8dab14c2(x29, x1, (x30, increment(x24)))
        if increment(x24) < x3 and I[x30][increment(x24)] == x1:
            x29 = _paint_cell_8dab14c2(x29, x0, (x30, x23))
        if I[x30][x24] == x0:
            x29 = _paint_cell_8dab14c2(x29, x1, (x30, decrement(x23)))
    for x30 in x27:
        if x7 > ZERO and I[decrement(x7)][x30] == x1:
            x29 = _paint_cell_8dab14c2(x29, x0, (x8, x30))
        if I[x7][x30] == x0:
            x29 = _paint_cell_8dab14c2(x29, x1, (increment(x8), x30))
        if increment(x8) < x2 and I[increment(x8)][x30] == x1:
            x29 = _paint_cell_8dab14c2(x29, x0, (x7, x30))
        if I[x8][x30] == x0:
            x29 = _paint_cell_8dab14c2(x29, x1, (decrement(x7), x30))
    for x30 in range(x12, add(x13, ONE)):
        if x25 > ZERO and I[decrement(x25)][x30] == x1:
            x29 = _paint_cell_8dab14c2(x29, x0, (x26, x30))
        if I[x25][x30] == x0:
            x29 = _paint_cell_8dab14c2(x29, x1, (increment(x26), x30))
        if increment(x26) < x2 and I[increment(x26)][x30] == x1:
            x29 = _paint_cell_8dab14c2(x29, x0, (x25, x30))
        if I[x26][x30] == x0:
            x29 = _paint_cell_8dab14c2(x29, x1, (decrement(x25), x30))
    for x30 in x28:
        if x12 > ZERO and I[x30][decrement(x12)] == x1:
            x29 = _paint_cell_8dab14c2(x29, x0, (x30, x13))
        if I[x30][x12] == x0:
            x29 = _paint_cell_8dab14c2(x29, x1, (x30, increment(x13)))
        if increment(x13) < x3 and I[x30][increment(x13)] == x1:
            x29 = _paint_cell_8dab14c2(x29, x0, (x30, x12))
        if I[x30][x13] == x0:
            x29 = _paint_cell_8dab14c2(x29, x1, (x30, decrement(x12)))
    return x29
