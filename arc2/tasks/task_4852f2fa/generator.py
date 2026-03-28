from arc2.core import *


TILES_4852F2FA = (
    frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE), (TWO, ONE), (TWO, TWO)}),
    frozenset({(ZERO, TWO), (ONE, ZERO), (ONE, ONE), (TWO, ZERO), (TWO, ONE)}),
    frozenset({(ZERO, ONE), (ZERO, TWO), (ONE, ZERO), (ONE, ONE), (TWO, ONE)}),
    frozenset({(ONE, ZERO), (ONE, ONE), (ONE, TWO), (TWO, ONE)}),
    frozenset({(ZERO, ONE), (ZERO, TWO), (ONE, ZERO), (ONE, ONE), (ONE, TWO), (TWO, ONE)}),
    frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE), (ONE, TWO), (TWO, ONE)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, TWO), (TWO, ZERO), (TWO, ONE)}),
)


def generate_4852f2fa(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    tile = choice(TILES_4852F2FA)
    motif = normalize(tile)
    mh = height(motif)
    mw = width(motif)
    loci = randint(ZERO, subtract(NINE, mh))
    locj = randint(ZERO, subtract(NINE, mw))
    offset = astuple(loci, locj)
    obj = shift(motif, offset)
    num = unifint(diff_lb, diff_ub, (ONE, FOUR))
    gi = fill(canvas(ZERO, (NINE, NINE)), EIGHT, obj)
    cands = totuple(difference(asindices(gi), obj))
    marks = sample(cands, num)
    gi = fill(gi, FOUR, marks)
    ow = multiply(THREE, num)
    go = canvas(ZERO, (THREE, ow))
    offsets = apply(tojvec, interval(ZERO, ow, THREE))
    painter = lbind(shift, tile)
    motifcells = mapply(painter, offsets)
    go = fill(go, EIGHT, motifcells)
    return {"input": gi, "output": go}
