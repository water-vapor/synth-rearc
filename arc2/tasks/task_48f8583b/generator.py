from arc2.core import *


NONZERO_COLORS_48F8583B = interval(ONE, TEN, ONE)
FOUR_COLOR_PATTERNS_48F8583B = (
    (ONE, TWO, TWO, FOUR),
    (ONE, TWO, THREE, THREE),
)
TWO_OR_THREE_COLOR_PATTERNS_48F8583B = (
    (TWO, THREE, FOUR),
    (TWO, SEVEN),
)
TWO_COLOR_PATTERNS_48F8583B = (
    (THREE, SIX),
    (FOUR, FIVE),
)


def _render_output_48f8583b(
    gi: Grid,
    rare_locs: Indices,
) -> Grid:
    x0 = shape(gi)
    x1 = asobject(gi)
    x2 = rbind(multiply, x0)
    x3 = apply(x2, rare_locs)
    x4 = lbind(shift, x1)
    x5 = mapply(x4, x3)
    x6 = canvas(ZERO, multiply(x0, THREE))
    x7 = paint(x6, x5)
    return x7


def _sample_counts_48f8583b(
    diff_lb: float,
    diff_ub: float,
) -> Tuple:
    x0 = unifint(diff_lb, diff_ub, (ONE, FOUR))
    if x0 == ONE:
        return choice(FOUR_COLOR_PATTERNS_48F8583B)
    if x0 == TWO:
        return choice(TWO_OR_THREE_COLOR_PATTERNS_48F8583B)
    return TWO_COLOR_PATTERNS_48F8583B[subtract(x0, THREE)]


def _sample_input_48f8583b(
    counts: Tuple,
) -> Tuple:
    x0 = size(counts)
    x1 = tuple(sample(NONZERO_COLORS_48F8583B, x0))
    x2 = first(x1)
    x3 = first(counts)
    x4 = tuple(product(interval(ZERO, THREE, ONE), interval(ZERO, THREE, ONE)))
    x5 = frozenset(sample(x4, x3))
    x6 = canvas(x2, THREE_BY_THREE)
    x7 = difference(asindices(x6), x5)
    x8 = x6
    for x9, x10 in pair(x1[1:], counts[1:]):
        x11 = frozenset(sample(totuple(x7), x10))
        x8 = fill(x8, x9, x11)
        x7 = difference(x7, x11)
    return x8, x5


def generate_48f8583b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = _sample_counts_48f8583b(diff_lb, diff_ub)
    x1, x2 = _sample_input_48f8583b(x0)
    x3 = _render_output_48f8583b(x1, x2)
    return {
        "input": x1,
        "output": x3,
    }
