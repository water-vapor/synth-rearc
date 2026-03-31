from synth_rearc.core import *

from .verifier import verify_fc7cae8d


NONZERO_COLORS_FC7CAE8D = remove(ZERO, interval(ZERO, TEN, ONE))
PORTRAIT_FC7CAE8D = "portrait"
SQUARE_FC7CAE8D = "square"
LANDSCAPE_FC7CAE8D = "landscape"


def _rect_patch_fc7cae8d(
    i0: Integer,
    j0: Integer,
    h: Integer,
    w: Integer,
) -> Indices:
    return frozenset((i, j) for i in range(i0, i0 + h) for j in range(j0, j0 + w))


def _hline_patch_fc7cae8d(
    i: Integer,
    j0: Integer,
    j1: Integer,
) -> Indices:
    return frozenset((i, j) for j in range(j0, j1 + ONE))


def _vline_patch_fc7cae8d(
    i0: Integer,
    i1: Integer,
    j: Integer,
) -> Indices:
    return frozenset((i, j) for i in range(i0, i1 + ONE))


def _fill_rect_fc7cae8d(
    grid: Grid,
    color_value: Integer,
    i0: Integer,
    j0: Integer,
    h: Integer,
    w: Integer,
) -> Grid:
    x0 = _rect_patch_fc7cae8d(i0, j0, h, w)
    x1 = fill(grid, color_value, x0)
    return x1


def _fill_cells_fc7cae8d(
    grid: Grid,
    color_value: Integer,
    cells: Indices,
) -> Grid:
    x0 = fill(grid, color_value, cells)
    return x0


def _sample_kind_and_shape_fc7cae8d(
    diff_lb: float,
    diff_ub: float,
) -> tuple[str, Integer, Integer]:
    while True:
        x0 = choice((PORTRAIT_FC7CAE8D, SQUARE_FC7CAE8D, LANDSCAPE_FC7CAE8D))
        if x0 == PORTRAIT_FC7CAE8D:
            x1 = unifint(diff_lb, diff_ub, (SEVEN, 16))
            x2 = unifint(diff_lb, diff_ub, (FIVE, 11))
            if x1 >= x2 + TWO:
                return x0, x1, x2
            continue
        if x0 == SQUARE_FC7CAE8D:
            x1 = unifint(diff_lb, diff_ub, (FIVE, 12))
            return x0, x1, x1
        x1 = unifint(diff_lb, diff_ub, (SIX, 12))
        x2 = unifint(diff_lb, diff_ub, (12, 20))
        if x2 >= x1 + THREE:
            return x0, x1, x2


def _add_notch_fc7cae8d(
    grid: Grid,
    h: Integer,
    w: Integer,
) -> Grid:
    if not choice((T, T, F)):
        return grid
    x0 = choice(("top", "left", "bottom", "right"))
    if x0 in ("top", "bottom"):
        x1 = choice((ONE, ONE, TWO))
        x2 = randint(ONE, max(ONE, min(FOUR, w - TWO)))
        x3 = randint(ONE, max(ONE, w - x2 - ONE))
        x4 = ZERO if x0 == "top" else h - x1
        x5 = _rect_patch_fc7cae8d(x4, x3, x1, x2)
        x6 = _fill_cells_fc7cae8d(grid, ZERO, x5)
        return x6
    x1 = randint(ONE, max(ONE, min(FOUR, h - TWO)))
    x2 = choice((ONE, ONE, TWO))
    x3 = randint(ONE, max(ONE, h - x1 - ONE))
    x4 = ZERO if x0 == "left" else w - x2
    x5 = _rect_patch_fc7cae8d(x3, x4, x1, x2)
    x6 = _fill_cells_fc7cae8d(grid, ZERO, x5)
    return x6


def _decorate_l_fc7cae8d(
    grid: Grid,
    h: Integer,
    w: Integer,
    color_a: Integer,
    color_b: Integer,
    color_c: Integer,
) -> Grid:
    x0 = randint(ONE, w - TWO)
    x1 = randint(ONE, max(ONE, h // THREE))
    x2 = randint(max(x1 + TWO, h // TWO), h - TWO)
    x3 = _vline_patch_fc7cae8d(x1, x2, x0)
    x4 = _fill_cells_fc7cae8d(grid, color_a, x3)
    x5 = randint(max(ONE, x1), h - TWO)
    x6 = randint(ONE, x0)
    x7 = randint(x0, w - TWO)
    if x7 - x6 < TWO:
        x6 = max(ONE, x0 - TWO)
        x7 = min(w - TWO, x0 + TWO)
    x8 = _hline_patch_fc7cae8d(x5, x6, x7)
    x9 = _fill_cells_fc7cae8d(x4, color_a, x8)
    x10 = min(choice((ONE, TWO, TWO, THREE)), h - TWO)
    x11 = min(choice((TWO, THREE, THREE)), w - TWO)
    x12 = min(max(ONE, x5 - ONE), h - x10 - ONE)
    x13 = min(max(ONE, x0 - x11 + ONE), w - x11 - ONE)
    x14 = _fill_rect_fc7cae8d(x9, color_b, x12, x13, x10, x11)
    x15 = choice(((ONE, ONE), (ONE, TWO), (TWO, ONE), (ZERO, ONE), (ONE, ZERO)))
    x16 = randint(max(ONE, h // TWO), h - TWO)
    x17 = randint(ONE, max(ONE, w // THREE))
    x18 = frozenset({
        (x16, x17),
        (x16 + x15[0], x17),
        (x16, x17 + x15[1]),
    })
    x19 = frozenset((i, j) for i, j in x18 if ZERO <= i < h and ZERO <= j < w)
    x20 = _fill_cells_fc7cae8d(x14, color_c, x19)
    x21 = _add_notch_fc7cae8d(x20, h, w)
    return x21


def _decorate_mosaic_fc7cae8d(
    grid: Grid,
    h: Integer,
    w: Integer,
    color_a: Integer,
    color_b: Integer,
    color_c: Integer,
) -> Grid:
    x0 = randint(max(TWO, h // THREE), max(TWO, h // TWO))
    x1 = randint(max(THREE, w // THREE), max(THREE, (TWO * w) // THREE))
    x2 = randint(ONE, h - x0 - ONE)
    x3 = randint(ONE, w - x1 - ONE)
    x4 = frozenset(
        (i, j)
        for i in range(x2, x2 + x0)
        for j in range(x3, x3 + x1)
        if even(add(i, j)) or i in (x2, x2 + x0 - ONE) or j == x3 + x1 - ONE
    )
    x5 = _fill_cells_fc7cae8d(grid, color_a, x4)
    x6 = max(ONE, x0 - TWO)
    x7 = max(TWO, x1 - THREE)
    x8 = min(x6, THREE)
    x9 = min(x7, FIVE)
    x10 = min(x2 + ONE, h - x8 - ONE)
    x11 = min(x3 + ONE, w - x9 - ONE)
    x12 = _fill_rect_fc7cae8d(x5, color_b, x10, x11, x8, x9)
    x13 = randint(ONE, max(ONE, h // TWO))
    x14 = randint(max(ONE, w // TWO), w - TWO)
    x15 = choice(((ZERO, ZERO), (ONE, ZERO), (ZERO, ONE)))
    x16 = frozenset({
        (x13, x14),
        (x13 + x15[0], x14 + x15[1]),
    })
    x17 = frozenset((i, j) for i, j in x16 if ZERO <= i < h and ZERO <= j < w)
    x18 = _fill_cells_fc7cae8d(x12, color_c, x17)
    x19 = _add_notch_fc7cae8d(x18, h, w)
    return x19


def _decorate_bands_fc7cae8d(
    grid: Grid,
    h: Integer,
    w: Integer,
    color_a: Integer,
    color_b: Integer,
    color_c: Integer,
) -> Grid:
    x0 = randint(ONE, max(ONE, h // TWO))
    x1 = _hline_patch_fc7cae8d(x0, ONE, w - TWO)
    x2 = _fill_cells_fc7cae8d(grid, color_a, x1)
    if x0 + ONE < h - ONE and choice((T, F)):
        x3 = _hline_patch_fc7cae8d(x0 + ONE, TWO, w - TWO)
        x2 = _fill_cells_fc7cae8d(x2, color_a, x3)
    x4 = max(ONE, h - THREE)
    x5 = frozenset(
        (i, j)
        for i in range(x4, h - ONE)
        for j in range(ONE, w - ONE)
        if even(add(i, j))
    )
    x6 = _fill_cells_fc7cae8d(x2, color_b, x5)
    x7 = frozenset(
        (i, j)
        for i in range(x4, h - ONE)
        for j in range(ONE, w - ONE)
        if not even(add(i, j)) and j % THREE == ONE
    )
    x8 = _fill_cells_fc7cae8d(x6, color_c, x7)
    for _ in range(TWO):
        x9 = randint(ONE, w - TWO)
        x10 = randint(ONE, max(ONE, x0))
        x11 = randint(x10, min(h - TWO, x0 + THREE))
        x12 = _vline_patch_fc7cae8d(x10, x11, x9)
        x8 = _fill_cells_fc7cae8d(x8, color_a, x12)
    x13 = _fill_rect_fc7cae8d(x8, color_b, max(ONE, h - FOUR), ONE, TWO, min(THREE, w - TWO))
    x14 = _add_notch_fc7cae8d(x13, h, w)
    return x14


def _build_target_fc7cae8d(
    diff_lb: float,
    diff_ub: float,
    kind: str,
    h: Integer,
    w: Integer,
    dom: Integer,
    color_a: Integer,
    color_b: Integer,
    color_c: Integer,
) -> Grid:
    x0 = canvas(dom, (h, w))
    if kind == PORTRAIT_FC7CAE8D:
        x1 = _decorate_l_fc7cae8d(x0, h, w, color_a, color_b, color_c)
        return x1
    if kind == SQUARE_FC7CAE8D:
        x1 = choice((_decorate_l_fc7cae8d, _decorate_mosaic_fc7cae8d))
        x2 = x1(x0, h, w, color_a, color_b, color_c)
        return x2
    x1 = choice((_decorate_mosaic_fc7cae8d, _decorate_bands_fc7cae8d))
    x2 = x1(x0, h, w, color_a, color_b, color_c)
    return x2


def _transform_target_fc7cae8d(
    target: Grid,
) -> Grid:
    x0 = square(target)
    x1 = rot270(target)
    x2 = portrait(target)
    x3 = cmirror(target)
    x4 = dmirror(target)
    x5 = branch(x2, x3, x4)
    x6 = branch(x0, x1, x5)
    return x6


def _surround_colors_fc7cae8d(
    kind: str,
    horizontal_color: Integer,
    vertical_color: Integer,
) -> tuple[Integer, Integer, Integer, Integer]:
    if kind == PORTRAIT_FC7CAE8D:
        return ZERO, horizontal_color, ZERO, vertical_color
    if kind == SQUARE_FC7CAE8D and choice((T, F)):
        return vertical_color, ZERO, horizontal_color, ZERO
    return ZERO, horizontal_color, vertical_color, ZERO


def _add_edge_noise_fc7cae8d(
    grid: Grid,
    noise_a: Integer,
    noise_b: Integer,
    noise_c: Integer,
) -> Grid:
    x0 = height(grid)
    x1 = width(grid)
    x2 = _hline_patch_fc7cae8d(ZERO, ZERO, x1 - ONE)
    x3 = _fill_cells_fc7cae8d(grid, noise_a, x2)
    if x0 > ONE:
        x4 = frozenset((ONE, j) for j in range(ZERO, x1, choice((TWO, THREE, FOUR))))
        x3 = _fill_cells_fc7cae8d(x3, noise_a, x4)
    x5 = _vline_patch_fc7cae8d(ZERO, x0 - ONE, ZERO)
    x6 = _fill_cells_fc7cae8d(x3, noise_b, x5)
    if x1 > ONE:
        x7 = frozenset((i, ONE) for i in range(ZERO, x0, choice((TWO, THREE))))
        x6 = _fill_cells_fc7cae8d(x6, noise_b, x7)
    x8 = frozenset((x0 - ONE, j) for j in range(x1) if j % choice((TWO, THREE)) != ONE)
    x9 = _fill_cells_fc7cae8d(x6, noise_c, x8)
    x10 = frozenset((i, x1 - ONE) for i in range(x0) if i % choice((TWO, THREE)) != ZERO)
    x11 = _fill_cells_fc7cae8d(x9, noise_c, x10)
    return x11


def generate_fc7cae8d(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0, x1, x2 = _sample_kind_and_shape_fc7cae8d(diff_lb, diff_ub)
        x3 = sample(tuple(NONZERO_COLORS_FC7CAE8D), NINE)
        x4, x5, x6, x7, x8, x9, x10, x11, x12 = x3
        x13 = _build_target_fc7cae8d(diff_lb, diff_ub, x0, x1, x2, x4, x5, x6, x7)
        x14 = _transform_target_fc7cae8d(x13)
        x15, x16, x17, x18 = _surround_colors_fc7cae8d(x0, x8, x9)
        x19 = randint(ONE, THREE)
        x20 = randint(ONE, THREE)
        x21 = randint(ONE, THREE)
        x22 = randint(ONE, THREE)
        x23 = x19 + ONE + x1 + ONE + x20
        x24 = x21 + ONE + x2 + ONE + x22
        x25 = canvas(ZERO, (x23, x24))
        x26 = x19 + ONE
        x27 = x21 + ONE
        x28 = shift(asobject(x13), (x26, x27))
        x29 = paint(x25, x28)
        x30 = _hline_patch_fc7cae8d(x26 - ONE, x27, x27 + x2 - ONE)
        x31 = _hline_patch_fc7cae8d(x26 + x1, x27, x27 + x2 - ONE)
        x32 = _vline_patch_fc7cae8d(x26, x26 + x1 - ONE, x27 - ONE)
        x33 = _vline_patch_fc7cae8d(x26, x26 + x1 - ONE, x27 + x2)
        x34 = _fill_cells_fc7cae8d(x29, x15, x30)
        x35 = _fill_cells_fc7cae8d(x34, x16, x31)
        x36 = _fill_cells_fc7cae8d(x35, x17, x32)
        x37 = _fill_cells_fc7cae8d(x36, x18, x33)
        x38 = _add_edge_noise_fc7cae8d(x37, x10, x11, x12)
        x39 = verify_fc7cae8d(x38)
        if x39 != x14:
            continue
        return {"input": x38, "output": x14}
