from synth_rearc.core import *


def generate_7e0986d6(diff_lb: float, diff_ub: float) -> dict:
    cols = remove(ZERO, interval(ZERO, TEN, ONE))
    h = unifint(diff_lb, diff_ub, (TEN, 30))
    w = unifint(diff_lb, diff_ub, (TEN, 30))
    bgc = ZERO
    sqc, noisec = sample(cols, TWO)
    numsq = unifint(diff_lb, diff_ub, (ONE, max(ONE, (h * w) // 45)))
    succ = ZERO
    tr = ZERO
    maxtr = TEN * numsq
    go = canvas(bgc, (h, w))
    inds = asindices(go)
    while tr < maxtr and succ < numsq:
        tr += ONE
        oh = randint(2, 7)
        ow = randint(2, 7)
        cands = sfilter(inds, lambda ij: ij[0] <= h - oh and ij[1] <= w - ow)
        if len(cands) == ZERO:
            continue
        loc = choice(totuple(cands))
        loci, locj = loc
        sq = backdrop(frozenset({(loci, locj), (loci + oh - ONE, locj + ow - ONE)}))
        if sq.issubset(inds):
            succ += ONE
            inds = (inds - sq) - outbox(sq)
            go = fill(go, sqc, sq)
    gi = tuple(e for e in go)
    sqinds = ofcolor(go, sqc)
    bginds = ofcolor(go, bgc)
    inner_cands = set(sqinds)
    outer_cands = set(bginds)
    nin = unifint(diff_lb, diff_ub, (ONE, max(ONE, len(sqinds) // 6)))
    nout = unifint(diff_lb, diff_ub, (ONE, max(ONE, len(sqinds) // 10)))
    for k in range(nin):
        if len(inner_cands) == ZERO:
            break
        loc = choice(totuple(inner_cands))
        torem = neighbors(loc) & ofcolor(go, sqc)
        inner_cands = inner_cands - torem
        gi = fill(gi, noisec, {loc})
    for k in range(nout):
        if len(outer_cands) == ZERO:
            break
        loc = choice(totuple(outer_cands))
        torem = neighbors(loc) & ofcolor(go, bgc)
        outer_cands = outer_cands - torem
        gi = fill(gi, noisec, {loc})
    if gi == go:
        loc = choice(totuple(sqinds))
        gi = fill(gi, noisec, {loc})
    return {"input": gi, "output": go}
