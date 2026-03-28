from collections import Counter

from synth_rearc.core import *


ROW_LAYOUTS_7C8AF763 = (
    (FOUR, THREE),
    (THREE, FOUR),
    (TWO, TWO, TWO),
)

COL_LAYOUTS_7C8AF763 = (
    (TWO, TWO, FOUR),
    (TWO, THREE, THREE),
    (TWO, FOUR, TWO),
    (THREE, TWO, THREE),
    (THREE, THREE, TWO),
    (FOUR, TWO, TWO),
)


def _row_bands_7c8af763(heights):
    x0 = []
    x1 = [ZERO]
    x2 = ONE
    x3 = len(heights)
    for x4, x5 in enumerate(heights):
        x0.append(tuple(range(x2, x2 + x5)))
        x2 += x5
        if x4 != x3 - ONE:
            x1.append(x2)
            x2 += ONE
    x1.append(decrement(TEN))
    return tuple(x0), tuple(x1)


def _col_bands_7c8af763(widths):
    x0 = []
    x1 = []
    x2 = ZERO
    x3 = len(widths)
    for x4, x5 in enumerate(widths):
        x0.append(tuple(range(x2, x2 + x5)))
        x2 += x5
        if x4 != x3 - ONE:
            x1.append(x2)
            x2 += ONE
    return tuple(x0), tuple(x1)


def _region_vote_counts_7c8af763(
    markers,
    row_bands,
    col_bands,
    wall_rows,
    wall_cols,
):
    x0 = {}
    x1 = len(col_bands)
    for x2, x3 in enumerate(row_bands):
        for x4, x5 in enumerate(col_bands):
            x6 = Counter()
            for x7 in x5:
                for x8 in (wall_rows[x2], wall_rows[x2 + ONE]):
                    x9 = markers.get((x8, x7), FIVE)
                    if x9 in (ONE, TWO):
                        x6[x9] += ONE
            if positive(x4):
                x10 = wall_cols[x4 - ONE]
                for x11 in x3:
                    x12 = markers.get((x11, x10), FIVE)
                    if x12 in (ONE, TWO):
                        x6[x12] += ONE
            if x4 != x1 - ONE:
                x13 = wall_cols[x4]
                for x14 in x3:
                    x15 = markers.get((x14, x13), FIVE)
                    if x15 in (ONE, TWO):
                        x6[x15] += ONE
            x0[(x2, x4)] = x6
    return x0


def _region_fill_colors_7c8af763(counts):
    x0 = {}
    for x1, x2 in counts.items():
        x3 = x2[ONE]
        x4 = x2[TWO]
        x5 = x3 + x4
        if x5 < TWO or x5 > FOUR or x3 == x4:
            return None
        x0[x1] = branch(greater(x3, x4), ONE, TWO)
    return x0


def _build_grid_7c8af763(markers, wall_rows, wall_cols):
    x0 = canvas(ZERO, astuple(TEN, TEN))
    for x1 in wall_rows:
        x2 = connect((x1, ZERO), (x1, decrement(TEN)))
        x0 = fill(x0, FIVE, x2)
    for x3 in wall_cols:
        x4 = connect((ZERO, x3), (decrement(TEN), x3))
        x0 = fill(x0, FIVE, x4)
    for x5, x6 in markers.items():
        x0 = fill(x0, x6, initset(x5))
    return x0


def generate_7c8af763(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(ROW_LAYOUTS_7C8AF763)
        x1 = choice(COL_LAYOUTS_7C8AF763)
        x2, x3 = _row_bands_7c8af763(x0)
        x4, x5 = _col_bands_7c8af763(x1)
        x6 = len(x2)
        x7 = len(x4)
        x8 = {
            (x9, x10): choice((ONE, TWO))
            for x9 in range(x6)
            for x10 in range(x7)
        }
        if len(set(x8.values())) == ONE:
            continue
        x11 = {
            (x12, x13): tuple((x3[x12], x14) for x14 in x4[x13])
            for x12 in range(len(x3))
            for x13 in range(x7)
        }
        x15 = {
            (x16, x17): tuple((x18, x5[x17]) for x18 in x2[x16])
            for x16 in range(x6)
            for x17 in range(len(x5))
        }
        x19 = {}
        for x20 in range(x7):
            x21 = choice(x11[(ZERO, x20)])
            x19[x21] = x8[(ZERO, x20)]
            x22 = choice(x11[(len(x3) - ONE, x20)])
            x19[x22] = x8[(x6 - ONE, x20)]
        for x23 in range(x6 - ONE):
            for x24 in range(x7):
                x25 = x8[(x23, x24)]
                x26 = x8[(x23 + ONE, x24)]
                if x25 == x26:
                    x27 = x25
                elif x6 == THREE:
                    x27 = x8[(ONE, x24)]
                else:
                    x27 = choice((x25, x26))
                x28 = choice(x11[(x23 + ONE, x24)])
                x19[x28] = x27
        x29 = _region_vote_counts_7c8af763(x19, x2, x4, x3, x5)
        for x30 in range(x6):
            for x31 in range(len(x5)):
                x32 = (x30, x31)
                x33 = (x30, x31 + ONE)
                x34 = x8[x32]
                x35 = x8[x33]
                x36 = x29[x32][x34] - x29[x32][other((ONE, TWO), x34)]
                x37 = x29[x33][x35] - x29[x33][other((ONE, TWO), x35)]
                x38 = either(x36 < ONE, x37 < ONE)
                x39 = uniform(ZERO, ONE) < 0.5
                if not either(x38, x39):
                    continue
                x40 = branch(equality(x34, x35), x34, branch(x36 < x37, x34, x35))
                x41 = choice(x15[(x30, x31)])
                x19[x41] = x40
                x29 = _region_vote_counts_7c8af763(x19, x2, x4, x3, x5)
        for x42, x43 in x11.items():
            if uniform(ZERO, ONE) >= 0.35:
                continue
            x44 = tuple(x45 for x45 in x43 if x45 not in x19)
            if len(x44) == ZERO:
                continue
            x46 = x42[ZERO]
            x47 = x42[ONE]
            if x46 == ZERO:
                x48 = (x8[(ZERO, x47)],)
            elif x46 == len(x3) - ONE:
                x48 = (x8[(x6 - ONE, x47)],)
            else:
                x48 = (x8[(x46 - ONE, x47)], x8[(x46, x47)])
            x49 = choice(x44)
            x50 = choice(x48 if uniform(ZERO, ONE) < 0.8 else (ONE, TWO))
            x51 = dict(x19)
            x51[x49] = x50
            x52 = _region_vote_counts_7c8af763(x51, x2, x4, x3, x5)
            x53 = _region_fill_colors_7c8af763(x52)
            if x53 is None:
                continue
            x19 = x51
            x29 = x52
        x54 = _region_fill_colors_7c8af763(x29)
        if x54 is None:
            continue
        if len(set(x54.values())) == ONE:
            continue
        if not (TEN <= len(x19) <= 18):
            continue
        x55 = _build_grid_7c8af763(x19, x3, x5)
        x56 = x55
        for x57, x58 in x54.items():
            x59 = x2[x57[ZERO]]
            x60 = x4[x57[ONE]]
            x61 = frozenset(product(x59, x60))
            x56 = fill(x56, x58, x61)
        return {"input": x55, "output": x56}
