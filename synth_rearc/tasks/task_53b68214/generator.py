from synth_rearc.core import *

from .verifier import verify_53b68214


def _sample_patch_53b68214(
    diff_lb: float,
    diff_ub: float,
    oh: int,
    ow: int,
) -> Indices:
    x0 = asindices(canvas(NEG_ONE, (oh, ow)))
    x1 = {choice(totuple(x0))}
    x2 = unifint(diff_lb, diff_ub, (ONE, oh * ow))
    while len(x1) < x2:
        x3 = (mapply(neighbors, x1) & x0) - x1
        if len(x3) == ZERO:
            break
        x1.add(choice(totuple(x3)))
    x4 = frozenset(x1)
    if choice((T, F, F)):
        x5 = uppermost(x4)
        x6 = frozenset((x5, j) for j in range(leftmost(x4), rightmost(x4) + ONE))
        x4 = combine(x4, x6)
    if choice((T, F, F)):
        x7 = leftmost(x4)
        x8 = frozenset((i, x7) for i in range(uppermost(x4), lowermost(x4) + ONE))
        x4 = combine(x4, x8)
    return normalize(x4)


def generate_53b68214(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = interval(ZERO, TEN, ONE)
    while True:
        h = unifint(diff_lb, diff_ub, (FIVE, EIGHT))
        w = TEN
        bgc = ZERO
        remcols = remove(bgc, cols)
        fgc = choice(remcols)
        oh = unifint(diff_lb, diff_ub, (ONE, h // TWO))
        ow = unifint(diff_lb, diff_ub, (ONE, w // TWO - ONE))
        obj = _sample_patch_53b68214(diff_lb, diff_ub, oh, ow)
        obj = recolor(fgc, obj)
        oh, ow = shape(obj)
        locj = randint(ZERO, w // TWO)
        plcd = shift(obj, (ZERO, locj))
        go = canvas(bgc, (TEN, w))
        hoffs = randint(ZERO, ow // TWO + ONE)
        for k in range(TEN // oh + ONE):
            go = paint(go, shift(plcd, (k * oh, k * hoffs)))
        if len(palette(go[h:])) == ONE:
            continue
        gi = go[:h]
        if (
            shape(gi) != (h, TEN)
            or shape(go) != (TEN, TEN)
            or palette(gi) != frozenset((ZERO, fgc))
            or palette(go) != frozenset((ZERO, fgc))
        ):
            continue
        if verify_53b68214(gi) != go:
            continue
        return {"input": gi, "output": go}
