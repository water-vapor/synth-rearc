from arc2.core import *

from .verifier import verify_e2092e0c


def generate_e2092e0c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    dims = (15, 15)
    base = canvas(ZERO, dims)
    fullinds = asindices(base)
    tplinds = totuple(asindices(canvas(ZERO, THREE_BY_THREE)))
    tplcols = remove(FIVE, interval(ONE, 10, ONE))
    noisecols = interval(ONE, 10, ONE)
    while True:
        ntpl = unifint(diff_lb, diff_ub, (FOUR, SIX))
        tplcells = sample(tplinds, ntpl)
        ncols = unifint(diff_lb, diff_ub, (THREE, min(FOUR, ntpl)))
        cols = list(sample(tplcols, ncols))
        cols.extend(choice(cols) for _ in range(ntpl - ncols))
        shuffle(cols)
        tplobj = frozenset((c, ij) for c, ij in zip(cols, tplcells))
        tpl = paint(canvas(ZERO, THREE_BY_THREE), tplobj)
        refobj = asobject(tpl)
        loci = randint(5, 10)
        locj = randint(5, 10)
        loc = (loci, locj)
        refpatch = toindices(refobj)
        cornerbox = intersection(fullinds, outbox(refobj))
        copyobj = shift(refobj, loc)
        copypatch = shift(refpatch, loc)
        copybox = shift(outbox(refobj), loc)
        special = insert((3, 4), initset((4, 3)))
        noisefree = merge((cornerbox, refpatch, copypatch, copybox, special))
        noisecands = totuple(difference(fullinds, noisefree))
        bordercands = totuple(copybox | special)
        ngi = unifint(diff_lb, diff_ub, (58, 74))
        ngi = min(ngi, len(noisecands))
        ngi = max(ngi, 1)
        giobj = frozenset((choice(noisecols), ij) for ij in sample(noisecands, ngi))
        nbo = unifint(diff_lb, diff_ub, (TWO, SIX))
        nbo = min(nbo, len(bordercands))
        boobj = frozenset((choice(tplcols), ij) for ij in sample(bordercands, nbo))
        gi = paint(base, giobj)
        gi = paint(gi, boobj)
        gi = fill(gi, FIVE, cornerbox)
        gi = paint(gi, refobj)
        gi = paint(gi, copyobj)
        x0 = occurrences(gi, refobj)
        if x0 != frozenset({ORIGIN, loc}):
            continue
        go = fill(gi, FIVE, copybox)
        if go == gi:
            continue
        if verify_e2092e0c(gi) != go:
            continue
        return {"input": gi, "output": go}
