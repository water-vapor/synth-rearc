from synth_rearc.core import *


QUAD_SHAPE = (FIVE, FOUR)
FULL_SHAPE = (11, 9)
QUAD_CELLS = tuple(sorted(product(interval(ZERO, FIVE, ONE), interval(ZERO, FOUR, ONE))))


def _sample_mask(
    diff_lb: float,
    diff_ub: float,
    bounds: tuple[int, int],
) -> frozenset[tuple[int, int]]:
    ncells = unifint(diff_lb, diff_ub, bounds)
    return frozenset(sample(QUAD_CELLS, ncells))


def generate_e99362f0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        mask7 = _sample_mask(diff_lb, diff_ub, (7, 15))
        mask9 = _sample_mask(diff_lb, diff_ub, (7, 13))
        mask2 = _sample_mask(diff_lb, diff_ub, (7, 14))
        mask8 = _sample_mask(diff_lb, diff_ub, (6, 13))

        go = canvas(ZERO, QUAD_SHAPE)
        go = paint(go, recolor(TWO, mask2))
        go = paint(go, recolor(NINE, mask9))
        go = paint(go, recolor(SEVEN, mask7))
        go = paint(go, recolor(EIGHT, mask8))

        if colorcount(go, EIGHT) < 6:
            continue
        if colorcount(go, SEVEN) < 2:
            continue
        if colorcount(go, NINE) < 1:
            continue
        if colorcount(go, TWO) < 1:
            continue
        if size(difference(asindices(go), ofcolor(go, ZERO))) < 15:
            continue

        gi = canvas(ZERO, FULL_SHAPE)
        gi = fill(gi, FOUR, hfrontier((FIVE, ZERO)))
        gi = fill(gi, FOUR, vfrontier((ZERO, FOUR)))
        gi = paint(gi, recolor(SEVEN, mask7))
        gi = paint(gi, shift(recolor(NINE, mask9), (ZERO, FIVE)))
        gi = paint(gi, shift(recolor(TWO, mask2), (SIX, ZERO)))
        gi = paint(gi, shift(recolor(EIGHT, mask8), (SIX, FIVE)))

        if mostcolor(gi) != ZERO:
            continue
        return {"input": gi, "output": go}
