from arc2.core import *


HEIGHT_E45EF808 = 12
WIDTH_E45EF808 = 12


def _row_patch_e45ef808(
    row: Integer,
    left: Integer,
    right: Integer,
) -> Indices:
    x0 = max(ZERO, left)
    x1 = min(WIDTH_E45EF808 - ONE, right)
    if x0 > x1:
        return frozenset()
    return frozenset((row, x2) for x2 in range(x0, x1 + ONE))


def _monotone_sequence_e45ef808(
    start: Integer,
    end: Integer,
    length: Integer,
    diff_lb: float,
    diff_ub: float,
) -> Tuple:
    if length <= ONE:
        return (end,)
    if start == end:
        return (start,) * length
    x0 = abs(end - start)
    x1 = sign(end - start)
    x2 = [ZERO] * (length - ONE)
    for _ in range(x0):
        x3 = unifint(diff_lb, diff_ub, (ZERO, length - TWO))
        x2[x3] += ONE
    x4 = [start]
    x5 = start
    for x6 in x2:
        x5 += x1 * x6
        x4.append(x5)
    return tuple(x4)


def _paint_columns_e45ef808(gi: Grid) -> Grid:
    x0 = ofcolor(gi, SIX)
    x1 = ofcolor(gi, ONE)
    x2 = uppermost(x0)
    x3 = lowermost(x1)
    x4 = sfilter(x0, matcher(first, x2))
    x5 = sfilter(x1, matcher(first, x3))
    x6 = rightmost(x4)
    x7 = rightmost(x5)
    x8 = sfilter(x1, matcher(last, x6))
    x9 = sfilter(x1, matcher(last, x7))
    x10 = fill(gi, FOUR, x8)
    x11 = fill(x10, NINE, x9)
    return x11


def _base_grid_e45ef808(
    bottom_one_row: Integer,
) -> Grid:
    x0 = canvas(ONE, (HEIGHT_E45EF808, WIDTH_E45EF808))
    x1 = fill(x0, ZERO, _row_patch_e45ef808(ZERO, ZERO, WIDTH_E45EF808 - ONE))
    for x2 in range(bottom_one_row + ONE, HEIGHT_E45EF808):
        x1 = fill(x1, SIX, _row_patch_e45ef808(x2, ZERO, WIDTH_E45EF808 - ONE))
    return x1


def _prefix_suffix_input_e45ef808(
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    x0 = unifint(diff_lb, diff_ub, (FIVE, SEVEN))
    x1 = choice((FOUR, FIVE))
    x1 = min(x1, HEIGHT_E45EF808 - x0 - ONE)
    x2 = x0 + x1 - ONE
    x3 = unifint(diff_lb, diff_ub, (TWO, FIVE))
    x4 = unifint(diff_lb, diff_ub, (x3 + THREE, TEN))
    x5 = choice((ONE, ONE, TWO))
    x6 = max(ZERO, x4 - x5 + ONE)
    x7 = _monotone_sequence_e45ef808(x6, x3 + ONE, x1, diff_lb, diff_ub)
    x8 = _monotone_sequence_e45ef808(x4, WIDTH_E45EF808 - ONE, x1, diff_lb, diff_ub)
    x9 = unifint(diff_lb, diff_ub, (ONE, x1 - TWO))
    x10 = choice((ZERO, ZERO, ONE))
    x11 = min(x3 - ONE, x10 + choice((ZERO, ONE)))
    x12 = _monotone_sequence_e45ef808(x10, ZERO, x1 - x9, diff_lb, diff_ub)
    x13 = _monotone_sequence_e45ef808(x11, x3 - ONE, x1 - x9, diff_lb, diff_ub)
    gi = _base_grid_e45ef808(x2)
    for x14, x15 in enumerate(range(x0, x2 + ONE)):
        gi = fill(gi, SIX, _row_patch_e45ef808(x15, x7[x14], x8[x14]))
        if x14 >= x9:
            x16 = x14 - x9
            gi = fill(gi, SIX, _row_patch_e45ef808(x15, x12[x16], x13[x16]))
    return gi


def _edge_gap_input_e45ef808(
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    x0 = unifint(diff_lb, diff_ub, (FIVE, SEVEN))
    x1 = choice((FOUR, FIVE))
    x1 = min(x1, HEIGHT_E45EF808 - x0 - ONE)
    x2 = x0 + x1 - ONE
    x3 = unifint(diff_lb, diff_ub, (ZERO, TWO))
    x4 = max(x3 + SIX, EIGHT)
    x5 = unifint(diff_lb, diff_ub, (x4, WIDTH_E45EF808 - ONE))
    x6 = choice((ONE, ONE, TWO))
    x7 = max(x3 + ONE, x5 - x6 + ONE)
    x8 = _monotone_sequence_e45ef808(x7, x3 + ONE, x1, diff_lb, diff_ub)
    x9 = _monotone_sequence_e45ef808(x5, WIDTH_E45EF808 - ONE, x1, diff_lb, diff_ub)
    x10 = choice((T, T, F))
    gi = _base_grid_e45ef808(x2)
    x11 = ()
    x12 = ()
    x13 = ZERO
    if x10:
        x13 = unifint(diff_lb, diff_ub, (ZERO, x1 - TWO))
        x14 = max(x3 + FOUR, x7 + ONE)
        x15 = max(x14, x5 - TWO)
        x16 = unifint(diff_lb, diff_ub, (x14, x15))
        x17 = choice((ONE, ONE, TWO))
        x18 = max(x3 + ONE, x16 - x17 + ONE)
        x19 = min(x5 - TWO, x18 + x17 - ONE)
        x20 = unifint(diff_lb, diff_ub, (x3 + ONE, min(x3 + THREE, WIDTH_E45EF808 - TWO)))
        x21 = min(WIDTH_E45EF808 - TWO, x20 + choice((ZERO, ONE)))
        x11 = _monotone_sequence_e45ef808(x18, x20, x1 - x13, diff_lb, diff_ub)
        x12 = _monotone_sequence_e45ef808(x19, x21, x1 - x13, diff_lb, diff_ub)
    for x22, x23 in enumerate(range(x0, x2 + ONE)):
        gi = fill(gi, SIX, _row_patch_e45ef808(x23, x8[x22], x9[x22]))
        if x10 and x22 >= x13:
            x24 = x22 - x13
            gi = fill(gi, SIX, _row_patch_e45ef808(x23, x11[x24], x12[x24]))
    return gi


def generate_e45ef808(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        gi = branch(
            choice((T, F)),
            _prefix_suffix_input_e45ef808(diff_lb, diff_ub),
            _edge_gap_input_e45ef808(diff_lb, diff_ub),
        )
        if choice((T, F)):
            gi = vmirror(gi)
        go = _paint_columns_e45ef808(gi)
        if gi == go:
            continue
        return {"input": gi, "output": go}
