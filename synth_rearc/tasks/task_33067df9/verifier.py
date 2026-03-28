from synth_rearc.core import *


OUTPUT_SIDE = 26
BORDER = TWO
GAP = TWO


def _row_runs(row):
    runs = []
    j = ZERO
    while j < len(row):
        value = row[j]
        if value == ZERO:
            j += ONE
            continue
        k = j + ONE
        while k < len(row) and row[k] == value:
            k += ONE
        runs.append((value, j, k - j))
        j = k
    return tuple(runs)


def _render_sampled(sampled):
    x0 = len(sampled)
    x1 = len(sampled[ZERO])
    x2 = (OUTPUT_SIDE - 2 * BORDER - GAP * (x0 - ONE)) // x0
    x3 = (OUTPUT_SIDE - 2 * BORDER - GAP * (x1 - ONE)) // x1
    x4 = canvas(ZERO, (OUTPUT_SIDE, OUTPUT_SIDE))
    x5 = tuple(_row_runs(row) for row in sampled)
    x6 = set()
    for x7, x8 in enumerate(x5):
        for x9 in x8:
            if (x7, x9) in x6:
                continue
            x6.add((x7, x9))
            x10 = x7
            while x10 + ONE < x0 and x9 in x5[x10 + ONE]:
                x10 += ONE
                x6.add((x10, x9))
            x11, x12, x13 = x9
            x14 = BORDER + x7 * (x2 + GAP)
            x15 = BORDER + x10 * (x2 + GAP) + x2 - ONE
            x16 = BORDER + x12 * (x3 + GAP)
            x17 = BORDER + (x12 + x13 - ONE) * (x3 + GAP) + x3 - ONE
            x18 = frozenset((i, j) for i in range(x14, x15 + ONE) for j in range(x16, x17 + ONE))
            x4 = fill(x4, x11, x18)
    return x4


def verify_33067df9(I: Grid) -> Grid:
    x0 = interval(ONE, height(I), TWO)
    x1 = interval(ONE, width(I), TWO)
    x2 = tuple(tuple(I[i][j] for j in x1) for i in x0)
    x3 = _render_sampled(x2)
    return x3
