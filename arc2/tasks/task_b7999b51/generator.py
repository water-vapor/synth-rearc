from arc2.core import *


NONZERO_COLORS_B7999B51 = interval(ONE, TEN, ONE)
WIDTH_BOUNDS_B7999B51 = (15, 24)
TOP_MARGIN_BOUNDS_B7999B51 = (ONE, THREE)
BOTTOM_MARGIN_BOUNDS_B7999B51 = (ONE, THREE)
GAP_BOUNDS_B7999B51 = (ONE, FOUR)


def _rect_b7999b51(
    top: Integer,
    left: Integer,
    h: Integer,
    w: Integer,
) -> Indices:
    bottom = top + h - ONE
    right = left + w - ONE
    return backdrop(frozenset({(top, left), (bottom, right)}))


def _paint_rect_b7999b51(
    grid: Grid,
    value: Integer,
    top: Integer,
    left: Integer,
    h: Integer,
    w: Integer,
) -> Grid:
    x0 = _rect_b7999b51(top, left, h, w)
    x1 = recolor(value, x0)
    return paint(grid, x1)


def _build_output_b7999b51(
    profile: Tuple[Tuple[Integer, Integer], ...],
) -> Grid:
    x0 = maximum(tuple(span for _, span in profile))
    x1 = len(profile)
    x2 = canvas(ZERO, (x0, x1))
    x3 = x2
    for x4, (x5, x6) in enumerate(profile):
        x7 = connect((ZERO, x4), (x6 - ONE, x4))
        x8 = recolor(x5, x7)
        x3 = paint(x3, x8)
    return x3


def _profile_from_grid_b7999b51(
    grid: Grid,
) -> Tuple[Tuple[Integer, Integer], ...]:
    x0 = order(fgpartition(grid), lambda x: (-height(x), leftmost(x), uppermost(x), color(x)))
    return tuple((color(x1), height(x1)) for x1 in x0)


def _band_rectangles_b7999b51(
    entries: Tuple[Tuple[Integer, Integer], ...],
    band_top: Integer,
    grid_width: Integer,
) -> Tuple[Tuple[Integer, Integer, Integer, Integer, Integer], ...]:
    x0 = tuple(sorted(entries, key=lambda x: (-x[1], x[0])))
    x1 = []
    x2 = x0[0][1]
    x3 = randint(ONE, max(ONE, grid_width // FOUR))
    x4 = min(12, grid_width - x3 - ONE)
    x5 = max(SIX, grid_width // THREE)
    x5 = min(x4, x5)
    x6 = randint(x5, x4)
    x7 = (x0[0][0], band_top, x3, x0[0][1], x6)
    x1.append(x7)
    x8 = x7
    for x9, x10 in x0[1:]:
        x11 = band_top + randint(ZERO, x2 - x10)
        x12 = min(12, grid_width - TWO, x8[4] + FOUR)
        x13 = max(FOUR, x8[4] - THREE)
        x13 = min(x12, x13)
        x14 = randint(x13, x12)
        x15 = grid_width - x14 - ONE
        x16 = max(ONE, x8[2] - TWO)
        x17 = min(x15, x8[2] + max(ONE, x8[4] - TWO))
        if x17 < x16:
            x16 = x15
            x17 = x15
        x18 = randint(x16, x17)
        if x18 == x8[2] and x14 == x8[4]:
            if x17 > x16:
                x18 = x16 if x18 != x16 else x17
            elif x14 > FOUR:
                x14 = x14 - ONE
                x15 = grid_width - x14 - ONE
                x18 = min(x18, x15)
        x19 = (x9, x11, x18, x10, x14)
        x1.append(x19)
        x8 = x19
    return tuple(x1)


def generate_b7999b51(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (THREE, FIVE))
        x1 = unifint(diff_lb, diff_ub, (max(THREE, x0), min(7, x0 + TWO)))
        x2 = tuple(range(ONE, x1 + ONE))
        x3 = tuple(sorted(sample(x2, x0), reverse=True))
        x4 = tuple(sample(NONZERO_COLORS_B7999B51, x0))
        x5 = tuple(zip(x4, x3))
        x6 = tuple(v for v in range(ONE, x0) if max(v, x0 - v) <= THREE)
        x7 = choice(x6)
        x8 = list(x5)
        shuffle(x8)
        x9 = tuple(x8[:x7])
        x10 = tuple(x8[x7:])
        x11 = maximum(tuple(span for _, span in x9))
        x12 = maximum(tuple(span for _, span in x10))
        x13 = unifint(diff_lb, diff_ub, TOP_MARGIN_BOUNDS_B7999B51)
        x14 = unifint(diff_lb, diff_ub, GAP_BOUNDS_B7999B51)
        x15 = unifint(diff_lb, diff_ub, BOTTOM_MARGIN_BOUNDS_B7999B51)
        x16 = x13 + x11 + x14 + x12 + x15
        if x16 > 30:
            continue
        x17 = unifint(diff_lb, diff_ub, WIDTH_BOUNDS_B7999B51)
        x18 = canvas(ZERO, (x16, x17))
        x19 = _band_rectangles_b7999b51(x9, x13, x17)
        x20 = _band_rectangles_b7999b51(x10, x13 + x11 + x14, x17)
        x21 = x18
        for x22, x23, x24, x25, x26 in x19 + x20:
            x21 = _paint_rect_b7999b51(x21, x22, x23, x24, x25, x26)
        if _profile_from_grid_b7999b51(x21) != x5:
            continue
        x27 = _build_output_b7999b51(x5)
        return {"input": x21, "output": x27}
