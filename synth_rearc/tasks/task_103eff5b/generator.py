from synth_rearc.core import *


ROTATIONS_103EFF5B = (identity, rot90, rot180, rot270)
PALETTE_103EFF5B = (ONE, TWO, THREE, FOUR)


def _nonzero_object_103eff5b(grid: Grid) -> Object:
    x0 = asobject(grid)
    x1 = sfilter(x0, lambda x: x[0] != ZERO)
    return x1


def _build_motif_103eff5b(
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    while True:
        side = choice((THREE, THREE, FOUR))
        ncols = choice((THREE, FOUR, FOUR))
        cols = sample(PALETTE_103EFF5B, ncols)
        occ_lb = FIVE if side == THREE else SEVEN
        occ_ub = SIX if side == THREE else TEN
        nocc = unifint(diff_lb, diff_ub, (occ_lb, occ_ub))
        cells = tuple(product(interval(ZERO, side, ONE), interval(ZERO, side, ONE)))
        picks = sample(cells, nocc)
        if not any(i == ZERO for i, _ in picks):
            continue
        if not any(i == side - ONE for i, _ in picks):
            continue
        if not any(j == ZERO for _, j in picks):
            continue
        if not any(j == side - ONE for _, j in picks):
            continue
        vals = tuple(choice(cols) for _ in range(nocc))
        if len(set(vals)) != ncols:
            continue
        rows = [[ZERO for _ in range(side)] for _ in range(side)]
        for (i, j), value in zip(picks, vals):
            rows[i][j] = value
        gi = tuple(tuple(row) for row in rows)
        x0 = objects(gi, F, T, T)
        if size(x0) != ONE:
            continue
        if colorcount(gi, ZERO) < ONE:
            continue
        return gi


def _template_pair_103eff5b(
    motif: Grid,
    factor: Integer,
) -> tuple[Grid, Grid]:
    x0 = rot90(motif)
    x1 = upscale(x0, factor)
    x2 = _nonzero_object_103eff5b(x1)
    x3 = recolor(EIGHT, x2)
    x4 = canvas(ZERO, shape(x1))
    x5 = paint(x4, x3)
    return x5, x1


def generate_103eff5b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        motif = _build_motif_103eff5b(diff_lb, diff_ub)
        factor = unifint(diff_lb, diff_ub, (TWO, FOUR))
        template_in, template_out = _template_pair_103eff5b(motif, factor)
        mh, mw = shape(motif)
        th, tw = shape(template_in)
        gap = unifint(diff_lb, diff_ub, (TWO, SIX))
        width = max(mw, tw) + unifint(diff_lb, diff_ub, (THREE, EIGHT))
        height0 = mh + gap + th + randint(TWO, FIVE)
        if height0 > 30 or width > 30:
            continue
        motif_j = randint(ZERO, width - mw)
        template_j = randint(ZERO, width - tw)
        motif_i = randint(ZERO, height0 - (mh + gap + th))
        template_i = motif_i + mh + gap
        gi = canvas(ZERO, (height0, width))
        go = canvas(ZERO, (height0, width))
        x0 = shift(_nonzero_object_103eff5b(motif), (motif_i, motif_j))
        x1 = shift(_nonzero_object_103eff5b(template_in), (template_i, template_j))
        x2 = shift(_nonzero_object_103eff5b(template_out), (template_i, template_j))
        gi = paint(paint(gi, x0), x1)
        go = paint(paint(go, x0), x2)
        x3 = choice(ROTATIONS_103EFF5B)
        x4 = x3(gi)
        x5 = x3(go)
        x6 = objects(x4, F, T, T)
        if size(x6) != TWO:
            continue
        if colorcount(x4, EIGHT) != size(_nonzero_object_103eff5b(template_in)):
            continue
        return {"input": x4, "output": x5}
