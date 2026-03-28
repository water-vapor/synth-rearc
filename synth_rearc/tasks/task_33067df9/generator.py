from synth_rearc.core import *


OUTPUT_SIDE = 26
BORDER = TWO
GAP = TWO
COLORS = remove(ZERO, interval(ZERO, TEN, ONE))
SIZE_OPTIONS = (ONE, TWO, TWO, THREE, THREE, FOUR, FOUR, FOUR)
PALETTE_SIZE_OPTIONS = (TWO, TWO, THREE, THREE, FOUR, FOUR, FIVE)


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


def _sample_row(ncols, palette, previous):
    x0 = _row_runs(previous) if previous is not None else ()
    while True:
        x1 = choice(x0) if x0 and choice((True, False)) else None
        row = []
        for x2 in range(ncols):
            if x1 is not None and x1[ONE] <= x2 < x1[ONE] + x1[TWO]:
                row.append(x1[ZERO])
                continue
            x3 = row[-ONE] if row else None
            x4 = previous[x2] if previous is not None else ZERO
            if x3 not in (None, ZERO) and choice((True, False, False)):
                x5 = x3
            elif x4 != ZERO and choice((True, False, False)):
                x5 = x4
            elif choice((True, False, False, False)):
                x5 = ZERO
            else:
                x6 = tuple(value for value in palette if value != x3) if x3 not in (None, ZERO) else palette
                x5 = choice(x6)
            row.append(x5)
        x7 = tuple(row)
        if all(value == ZERO for value in x7):
            continue
        if x7.count(ZERO) > max(ONE, ncols // TWO):
            continue
        if x1 is not None:
            x8 = x1[ONE]
            x9 = x8 + x1[TWO]
            if x8 > ZERO and x7[x8 - ONE] == x1[ZERO]:
                continue
            if x9 < ncols and x7[x9] == x1[ZERO]:
                continue
        return x7


def _sampled_grid(nrows, ncols, palette):
    while True:
        rows = []
        for _ in range(nrows):
            x0 = rows[-ONE] if rows else None
            x1 = _sample_row(ncols, palette, x0)
            rows.append(x1)
        x2 = tuple(rows)
        x3 = tuple(value for row in x2 for value in row if value != ZERO)
        if len(x3) < max(TWO, nrows):
            continue
        if len(set(x3)) < TWO:
            continue
        if nrows > ONE and all(row == x2[ZERO] for row in x2[ONE:]):
            continue
        return x2


def generate_33067df9(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(SIZE_OPTIONS)
        x1 = choice(SIZE_OPTIONS)
        if x0 == ONE and x1 == ONE:
            continue
        x2 = min(choice(PALETTE_SIZE_OPTIONS), len(COLORS), x0 * x1)
        if x2 < TWO:
            continue
        x3 = tuple(sample(COLORS, x2))
        x4 = _sampled_grid(x0, x1, x3)
        x5 = 2 * x0 + ONE
        x6 = 2 * x1 + ONE
        x7 = frozenset(
            (value, (2 * i + ONE, 2 * j + ONE))
            for i, row in enumerate(x4)
            for j, value in enumerate(row)
            if value != ZERO
        )
        gi = paint(canvas(ZERO, (x5, x6)), x7)
        go = _render_sampled(x4)
        return {"input": gi, "output": go}
