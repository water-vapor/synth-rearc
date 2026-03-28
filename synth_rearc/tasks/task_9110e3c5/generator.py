from synth_rearc.core import *


GRID_SHAPE_9110E3C5 = (SEVEN, SEVEN)
ALL_NONZERO_COLORS_9110E3C5 = interval(ONE, TEN, ONE)
DOMINANT_COLORS_9110E3C5 = (ONE, TWO, THREE)
GLYPH_ONE_9110E3C5 = frozenset({(ZERO, TWO), (ONE, ZERO), (ONE, ONE), (TWO, ONE)})
GLYPH_TWO_9110E3C5 = frozenset({(ONE, ZERO), (ONE, ONE), (ONE, TWO)})
GLYPH_THREE_9110E3C5 = frozenset({(ZERO, ONE), (ZERO, TWO), (ONE, ONE), (TWO, ONE)})


def _render_output(dominant: int) -> Grid:
    x0 = canvas(ZERO, (THREE, THREE))
    x1 = GLYPH_TWO_9110E3C5
    if dominant == ONE:
        x1 = GLYPH_ONE_9110E3C5
    elif dominant == THREE:
        x1 = GLYPH_THREE_9110E3C5
    return fill(x0, EIGHT, x1)


def _sample_counts(total: int, ncolors: int, cap: int) -> tuple[int, ...]:
    x0 = [ONE] * ncolors
    x1 = total - ncolors
    while x1 > ZERO:
        x2 = randint(ZERO, ncolors - ONE)
        if x0[x2] == cap:
            continue
        x0[x2] += ONE
        x1 -= ONE
    return tuple(x0)


def generate_9110e3c5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = canvas(ZERO, GRID_SHAPE_9110E3C5)
    x1 = totuple(asindices(x0))
    while True:
        x2 = choice(DOMINANT_COLORS_9110E3C5)
        x3 = unifint(diff_lb, diff_ub, (12, 21))
        x4 = unifint(diff_lb, diff_ub, (4, 7))
        x5 = max(x4, 6)
        x6 = min(13, 29 - x3)
        if x5 > x6:
            continue
        x7 = unifint(diff_lb, diff_ub, (x5, x6))
        x8 = _sample_counts(x7, x4, 4)
        x9 = 49 - x3 - x7
        x10 = tuple(sample(remove(x2, ALL_NONZERO_COLORS_9110E3C5), x4))
        x11 = sample(x1, x3 + x7)
        x12 = frozenset(x11[:x3])
        x13 = fill(x0, x2, x12)
        x14 = x3
        for x15, x16 in zip(x10, x8):
            x17 = frozenset(x11[x14:x14 + x16])
            x14 += x16
            x13 = fill(x13, x15, x17)
        if colorcount(x13, x2) != x3:
            continue
        if maximum(x8) >= x3:
            continue
        if numcolors(x13) != x4 + 2:
            continue
        if x9 < 20:
            continue
        x18 = _render_output(x2)
        return {"input": x13, "output": x18}
