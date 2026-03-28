from synth_rearc.core import *


def generate_8e2edd66(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(ZERO, interval(ZERO, TEN, ONE))
    loci = asindices(canvas(ZERO, (THREE, THREE)))
    fgc = choice(cols)
    nzero = unifint(diff_lb, diff_ub, (THREE, FIVE))
    zeros = frozenset(sample(totuple(loci), nzero))
    fg = difference(loci, zeros)
    gi = fill(canvas(ZERO, (THREE, THREE)), fgc, fg)
    offsets = apply(rbind(multiply, shape(gi)), zeros)
    place = mapply(lbind(shift, zeros), offsets)
    go = fill(canvas(ZERO, multiply(shape(gi), shape(gi))), fgc, place)
    return {"input": gi, "output": go}
