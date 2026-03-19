from arc2.core import *


def generate_e9ac8c9e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(FIVE, remove(ZERO, interval(ZERO, TEN, ONE)))
    while True:
        nrects = unifint(diff_lb, diff_ub, (ONE, THREE))
        d = 15 if nrects == THREE else multiply(FIVE, unifint(diff_lb, diff_ub, (TWO, THREE)))
        gi = canvas(ZERO, (d, d))
        go = canvas(ZERO, (d, d))
        occ = frozenset()
        placed_all = T
        for k in range(nrects):
            placed = F
            for _ in range(200):
                side = choice((TWO, FOUR, SIX))
                if side > d - TWO:
                    continue
                top = randint(ONE, d - side - ONE)
                left = randint(ONE, d - side - ONE)
                ulc = (top, left)
                lrc = (top + side - ONE, left + side - ONE)
                halo = backdrop(frozenset({(top - ONE, left - ONE), (top + side, left + side)}))
                if size(intersection(halo, occ)) != ZERO:
                    continue
                rect = backdrop(frozenset({ulc, lrc}))
                markers = (
                    (top - ONE, left - ONE),
                    (top - ONE, left + side),
                    (top + side, left - ONE),
                    (top + side, left + side),
                )
                vals = sample(cols, FOUR)
                gi = fill(gi, FIVE, rect)
                for loc, val in zip(markers, vals):
                    gi = fill(gi, val, initset(loc))
                half = halve(side)
                tl = backdrop(frozenset({ulc, (top + half - ONE, left + half - ONE)}))
                tr = shift(tl, tojvec(half))
                bl = shift(tl, toivec(half))
                br = shift(tl, (half, half))
                go = fill(go, vals[0], tl)
                go = fill(go, vals[1], tr)
                go = fill(go, vals[2], bl)
                go = fill(go, vals[3], br)
                occ = combine(occ, halo)
                placed = T
                break
            if not placed:
                placed_all = F
                break
        if not placed_all:
            continue
        x0 = objects(gi, T, F, T)
        x1 = colorfilter(x0, FIVE)
        if size(x1) != nrects:
            continue
        if size(x0) != multiply(nrects, FIVE):
            continue
        return {"input": gi, "output": go}
