from synth_rearc.core import *


def generate_0a1d4ef5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        h, w = 30, 30
        gi = canvas(ZERO, (h, w))
        noisecols = sample(cols, TWO)
        sigcols = difference(cols, noisecols)
        nrows = unifint(diff_lb, diff_ub, (2, 4))
        top0 = unifint(diff_lb, diff_ub, (1, 3))
        left0 = unifint(diff_lb, diff_ub, (1, 3))
        row_bases = [top0 + 7 * k for k in range(nrows)]
        col_bases = [left0 + 10 * k for k in range(3)]
        out_rows = []
        occ = frozenset()
        for row_base in row_bases:
            out_row = []
            for col_base in col_bases:
                color_value = choice(sigcols)
                rect_h = unifint(diff_lb, diff_ub, (3, 5))
                rect_w = unifint(diff_lb, diff_ub, (3, 6))
                top = row_base + randint(0, 1)
                left = col_base + randint(0, 2)
                ulc = (top, left)
                lrc = (top + rect_h - 1, left + rect_w - 1)
                patch = backdrop(frozenset({ulc, lrc}))
                gi = fill(gi, color_value, patch)
                occ = combine(occ, patch)
                out_row.append(color_value)
            out_rows.append(tuple(out_row))
        rem = difference(asindices(gi), occ)
        nna = unifint(diff_lb, diff_ub, (110, 170))
        nnb = unifint(diff_lb, diff_ub, (110, 170))
        if nna + nnb >= len(rem):
            continue
        noia = frozenset(sample(totuple(rem), nna))
        rem = difference(rem, noia)
        noib = frozenset(sample(totuple(rem), nnb))
        gi = fill(gi, first(noisecols), noia)
        gi = fill(gi, last(noisecols), noib)
        objs = objects(gi, T, F, T)
        x1 = fork(multiply, height, width)
        x2 = fork(equality, size, x1)
        x3 = compose(rbind(greater, TWO), height)
        x4 = compose(rbind(greater, TWO), width)
        x5 = fork(both, x2, x4)
        x6 = fork(both, x5, x3)
        bigobjs = sfilter(objs, x6)
        noiseobjs = difference(objs, bigobjs)
        if size(bigobjs) != nrows * THREE:
            continue
        if not (150 <= size(noiseobjs) <= 220):
            continue
        go = tuple(out_rows)
        return {"input": gi, "output": go}

