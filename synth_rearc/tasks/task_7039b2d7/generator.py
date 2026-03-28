from synth_rearc.core import *


def _sample_band_sizes(total: int, nbands: int) -> tuple[int, ...]:
    sizes = [ONE] * nbands
    extra = total - nbands
    for _ in range(extra):
        idx = randint(ZERO, nbands - ONE)
        sizes[idx] += ONE
    shuffle(sizes)
    return tuple(sizes)


def _separator_positions(
    band_sizes: tuple[int, ...],
    start_edge: bool,
    end_edge: bool,
) -> tuple[int, ...]:
    positions = []
    cursor = ONE if start_edge else ZERO
    if start_edge:
        positions.append(ZERO)
    for size in band_sizes[:-1]:
        cursor += size
        positions.append(cursor)
        cursor += ONE
    if end_edge:
        cursor += band_sizes[-1]
        positions.append(cursor)
    return tuple(positions)


def generate_7039b2d7(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        bg_col, sep_col = sample(cols, TWO)
        out_h = unifint(diff_lb, diff_ub, (TWO, FIVE))
        out_w = unifint(diff_lb, diff_ub, (TWO, FIVE))
        left_edge = choice((False, False, False, False, True))
        right_edge = False
        n_h_seps = out_h - ONE
        n_w_seps = out_w - ONE + left_edge + right_edge
        side_lb = max(TEN, out_h + n_h_seps, out_w + n_w_seps)
        while side_lb <= 30:
            sep_cells = side_lb * (n_h_seps + n_w_seps) - (n_h_seps * n_w_seps)
            bg_cells = side_lb * side_lb - sep_cells
            if bg_cells > sep_cells:
                break
            side_lb += ONE
        if side_lb > 30:
            continue
        side = unifint(diff_lb, diff_ub, (side_lb, 30))
        row_sizes = _sample_band_sizes(side - n_h_seps, out_h)
        col_sizes = _sample_band_sizes(side - n_w_seps, out_w)
        if out_h > TWO and len(set(row_sizes)) == ONE:
            continue
        if out_w > TWO and len(set(col_sizes)) == ONE:
            continue
        row_seps = _separator_positions(row_sizes, False, False)
        col_seps = _separator_positions(col_sizes, left_edge, right_edge)
        gi = canvas(bg_col, (side, side))
        for sep_r in row_seps:
            gi = fill(gi, sep_col, hfrontier((sep_r, ZERO)))
        for sep_c in col_seps:
            gi = fill(gi, sep_col, vfrontier((ZERO, sep_c)))
        if mostcolor(gi) != bg_col:
            continue
        go = canvas(bg_col, (out_h, out_w))
        return {"input": gi, "output": go}
