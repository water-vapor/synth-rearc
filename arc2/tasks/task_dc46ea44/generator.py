from arc2.core import *


SIX_PATCH = frozenset({
    (ZERO, TWO),
    (ONE, TWO),
    (TWO, ZERO),
    (TWO, TWO),
    (THREE, ONE),
})

DIVIDER = connect((FIVE, ZERO), (FIVE, TEN))
OTHER_COLORS = (ONE, TWO, THREE, FIVE, EIGHT, NINE)

SHORT_PATTERNS = (
    frozenset({(ZERO, ZERO), (ONE, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO)}),
    frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ONE)}),
    frozenset({(ZERO, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ONE), (ONE, ZERO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE)}),
)

TALL_PATTERNS = (
    frozenset({(ZERO, ONE), (ONE, ZERO), (TWO, ONE)}),
    frozenset({(ZERO, ZERO), (ONE, ONE), (TWO, ZERO)}),
)


def _place_patch(patch: Indices, anchor: tuple[int, int]) -> Indices:
    return shift(patch, subtract(anchor, lrcorner(patch)))


def generate_dc46ea44(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    del diff_lb, diff_ub
    while True:
        six_left = choice((THREE, FOUR, FIVE, SIX, SEVEN, EIGHT))
        other_color = choice(OTHER_COLORS)
        tall = choice((T, F, F, F))
        pattern = choice(TALL_PATTERNS if tall else SHORT_PATTERNS)
        other_lri = NINE if tall else choice((SEVEN, NINE))
        left_opts = tuple(c for c in (six_left - THREE, six_left - FOUR) if c >= ONE)
        right_opts = tuple(c for c in (six_left + SIX, six_left + SEVEN) if c <= TEN)
        lr_opts = left_opts + right_opts
        if len(lr_opts) == ZERO:
            continue
        other_lrj = choice(lr_opts)
        six_input = shift(SIX_PATCH, (SIX, six_left))
        other_input = _place_patch(pattern, (other_lri, other_lrj))
        six_shift = astuple(invert(SIX), ZERO)
        six_output = shift(six_input, six_shift)
        anchor = (TWO, six_left)
        other_output = _place_patch(other_input, anchor)
        gi = canvas(SEVEN, (11, 11))
        gi = fill(gi, FOUR, DIVIDER)
        gi = fill(gi, SIX, six_input)
        gi = fill(gi, other_color, other_input)
        go = canvas(SEVEN, (11, 11))
        go = fill(go, FOUR, DIVIDER)
        go = fill(go, SIX, six_output)
        go = fill(go, other_color, other_output)
        return {"input": gi, "output": go}
