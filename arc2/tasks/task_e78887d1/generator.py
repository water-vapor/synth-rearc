from arc2.core import *


MOTIFS_E78887D1 = (
    frozenset({(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)}),
    frozenset({(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)}),
    frozenset({(0, 0), (1, 1), (1, 2), (2, 0)}),
    frozenset({(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2)}),
    frozenset({(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)}),
    frozenset({(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)}),
    frozenset({(0, 0), (0, 1), (0, 2), (1, 1), (2, 1)}),
    frozenset({(0, 0), (0, 2), (1, 0), (1, 1), (1, 2), (2, 1)}),
    frozenset({(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)}),
    frozenset({(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)}),
    frozenset({(0, 0), (0, 1), (0, 2), (2, 0), (2, 1), (2, 2)}),
)


def _render_slot_e78887d1(
    color_value: Integer,
    motif: Indices,
) -> Grid:
    x0 = canvas(ZERO, (THREE, THREE))
    x1 = fill(x0, color_value, motif)
    return x1


def _render_band_e78887d1(
    colors: Tuple,
    motifs: Tuple,
) -> Grid:
    x0 = size(colors)
    x1 = subtract(multiply(FOUR, x0), ONE)
    x2 = canvas(ZERO, (THREE, x1))
    x3 = interval(ZERO, x0, ONE)
    x4 = apply(lbind(multiply, FOUR), x3)
    x5 = apply(tojvec, x4)
    x6 = papply(_render_slot_e78887d1, colors, motifs)
    x7 = apply(asobject, x6)
    x8 = mpapply(shift, x7, x5)
    x9 = paint(x2, x8)
    return x9


def generate_e78887d1(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = remove(ZERO, interval(ZERO, TEN, ONE))
    x1 = choice((THREE, FOUR))
    x2 = unifint(diff_lb, diff_ub, (ONE, THREE))
    x3 = sample(x0, x1)
    x4 = sample(MOTIFS_E78887D1, x1)
    x5 = randint(ZERO, decrement(x1))
    x6 = x4[x5:] + x4[:x5]
    x7 = add(multiply(FOUR, x2), ONE)
    x8 = subtract(multiply(FOUR, x1), ONE)
    gi = canvas(ZERO, (x7, x8))
    for x9 in range(x2):
        x10 = _render_band_e78887d1(x3, x6)
        x11 = shift(asobject(x10), toivec(add(multiply(FOUR, x9), ONE)))
        gi = paint(gi, x11)
        x6 = x6[ONE:] + x6[:ONE]
    go = _render_band_e78887d1(x3, x6)
    return {"input": gi, "output": go}
