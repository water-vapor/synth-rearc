from synth_rearc.core import *


OUTPUT_COLORS_c803e39c = (THREE, FOUR, SIX, SEVEN, EIGHT, NINE)
SHAPE_TRANSFORMS_c803e39c = (identity, hmirror, vmirror, dmirror, cmirror)


def _segment_c803e39c(
    horizontal: Boolean,
    anchor: Integer,
    start: Integer,
    stop: Integer,
) -> Indices:
    if horizontal:
        return frozenset((anchor, j) for j in range(start, stop + ONE))
    return frozenset((i, anchor) for i in range(start, stop + ONE))


def _edge_interval_c803e39c(k: Integer) -> tuple[Integer, Integer]:
    start = randint(ZERO, k - TWO)
    stop = randint(start + ONE, k - ONE)
    return start, stop


def _shape_bounds_c803e39c(k: Integer) -> tuple[Integer, Integer]:
    if k == THREE:
        return FIVE, SEVEN
    if k == FOUR:
        return SEVEN, 11
    return 10, 18


def _motif_c803e39c(
    k: Integer,
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    min_cells, max_cells = _shape_bounds_c803e39c(k)
    while True:
        topa, topb = _edge_interval_c803e39c(k)
        bota, botb = _edge_interval_c803e39c(k)
        lefta, leftb = _edge_interval_c803e39c(k)
        righta, rightb = _edge_interval_c803e39c(k)
        x0 = _segment_c803e39c(T, ZERO, topa, topb)
        x1 = _segment_c803e39c(T, k - ONE, bota, botb)
        x2 = _segment_c803e39c(F, ZERO, lefta, leftb)
        x3 = _segment_c803e39c(F, k - ONE, righta, rightb)
        cells = combine(combine(x0, x1), combine(x2, x3))
        nextra = unifint(diff_lb, diff_ub, (ZERO, TWO))
        for _ in range(nextra):
            horizontal = choice((T, F))
            anchor = randint(ZERO, k - ONE)
            start, stop = _edge_interval_c803e39c(k)
            cells = combine(cells, _segment_c803e39c(horizontal, anchor, start, stop))
        cells = choice(SHAPE_TRANSFORMS_c803e39c)(cells)
        ncells = size(cells)
        if ncells < min_cells or ncells > max_cells:
            continue
        if ncells == k * k:
            continue
        return cells


def _panel_c803e39c(
    patch: Indices,
    color: Integer,
    k: Integer,
    *,
    trim_right: Boolean = F,
) -> Grid:
    width_ = k + ONE if trim_right else k + TWO
    x0 = canvas(ZERO, (k + TWO, width_))
    x1 = shift(patch, (ONE, ONE))
    x2 = fill(x0, color, x1)
    return x2


def _render_output_c803e39c(
    stamp: Indices,
    mask: Indices,
    k: Integer,
    fg: Integer,
    bg: Integer,
) -> Grid:
    x0 = canvas(bg, (k * k, k * k))
    x1 = lbind(shift, stamp)
    x2 = rbind(multiply, (k, k))
    x3 = apply(x2, mask)
    x4 = mapply(x1, x3)
    x5 = fill(x0, fg, x4)
    return x5


def generate_c803e39c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        k = unifint(diff_lb, diff_ub, (THREE, FIVE))
        stamp = _motif_c803e39c(k, diff_lb, diff_ub)
        mask = _motif_c803e39c(k, diff_lb, diff_ub)
        fg, bg = sample(OUTPUT_COLORS_c803e39c, TWO)
        block = asindices(canvas(ZERO, (k, k)))
        x0 = _panel_c803e39c(stamp, ONE, k)
        x1 = _panel_c803e39c(mask, TWO, k)
        x2 = _panel_c803e39c(block, fg, k)
        x3 = _panel_c803e39c(block, bg, k, trim_right=(k == FIVE))
        x4 = canvas(FIVE, (k + TWO, ONE))
        x5 = hconcat(x0, x4)
        x6 = hconcat(x5, x1)
        x7 = hconcat(x6, x4)
        x8 = hconcat(x7, x2)
        x9 = hconcat(x8, x4)
        gi = hconcat(x9, x3)
        go = _render_output_c803e39c(stamp, mask, k, fg, bg)
        if gi == go:
            continue
        return {"input": gi, "output": go}
