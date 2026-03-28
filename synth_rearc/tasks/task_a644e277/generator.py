from synth_rearc.core import *


def _separator_positions(cell_span: int, nfrontiers: int) -> tuple[int, ...]:
    step = cell_span + ONE
    return tuple(step * k - ONE for k in range(ONE, nfrontiers + ONE))


def generate_a644e277(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    colors = interval(ONE, TEN, ONE)
    while True:
        sep = choice((ONE, TWO))
        bg, dot = sample(remove(sep, colors), TWO)
        cell_h = choice((THREE, FOUR, FOUR))
        cell_w = choice((THREE, FOUR, FOUR))
        span_h = TWO if cell_h == THREE else choice((ONE, TWO))
        span_w = TWO if cell_w == THREE else choice((ONE, TWO))
        n_sep_rows = unifint(diff_lb, diff_ub, (span_h + ONE, FIVE))
        n_sep_cols = unifint(diff_lb, diff_ub, (span_w + ONE, FIVE))
        tail_h = unifint(diff_lb, diff_ub, (ONE, cell_h))
        tail_w = unifint(diff_lb, diff_ub, (ONE, cell_w))
        h = n_sep_rows * (cell_h + ONE) + tail_h
        w = n_sep_cols * (cell_w + ONE) + tail_w
        sep_rows = _separator_positions(cell_h, n_sep_rows)
        sep_cols = _separator_positions(cell_w, n_sep_cols)
        marked_rows = (first(sep_rows), sep_rows[span_h])
        marked_cols = (first(sep_cols), sep_cols[span_w])
        gi = canvas(bg, (h, w))
        for i in sep_rows:
            gi = fill(gi, sep, connect((i, ZERO), (i, w - ONE)))
        for j in sep_cols:
            gi = fill(gi, sep, connect((ZERO, j), (h - ONE, j)))
        gaps = frozenset((i, j) for i in marked_rows for j in marked_cols)
        gi = fill(gi, bg, gaps)
        open_cells = difference(ofcolor(gi, bg), gaps)
        top = first(marked_rows)
        left = first(marked_cols)
        bottom = last(marked_rows)
        right = last(marked_cols)
        crop_patch = frozenset(
            (i, j)
            for i in range(top, bottom + ONE)
            for j in range(left, right + ONE)
        )
        inside = intersection(open_cells, crop_patch)
        outside = difference(open_cells, crop_patch)
        if len(inside) == ZERO:
            continue
        if len(outside) == ZERO:
            continue
        cells = totuple(open_cells)
        nnoise_lb = max(ONE, len(cells) // 12)
        nnoise_ub = min(len(cells), max(nnoise_lb + ONE, len(cells) // 7))
        nnoise = unifint(diff_lb, diff_ub, (nnoise_lb, nnoise_ub))
        noise = frozenset(sample(cells, nnoise))
        if len(intersection(noise, inside)) == ZERO:
            continue
        if len(intersection(noise, outside)) == ZERO:
            continue
        gi = fill(gi, dot, noise)
        dims = (bottom - top + ONE, right - left + ONE)
        go = crop(gi, (top, left), dims)
        return {"input": gi, "output": go}
