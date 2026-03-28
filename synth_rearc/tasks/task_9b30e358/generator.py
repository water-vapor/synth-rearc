from synth_rearc.core import *

from .verifier import verify_9b30e358


HEIGHT_9B30E358 = TEN
WIDTHS_9B30E358 = (FIVE, SEVEN)

PATTERNS_9B30E358 = {
    FOUR: (
        (
            (ONE, TWO, ONE),
            (TWO, ONE, TWO),
            (ONE, ONE, ONE),
            (ZERO, ONE, ZERO),
        ),
        (
            (ONE, ONE, ONE),
            (ZERO, ONE, ZERO),
            (ONE, TWO, ONE),
            (TWO, ONE, TWO),
        ),
        (
            (TWO, ZERO, TWO),
            (ONE, TWO, ONE),
            (ZERO, ONE, ZERO),
            (ONE, ONE, ONE),
        ),
        (
            (ZERO, ONE, ZERO, ONE, ZERO),
            (ONE, ZERO, TWO, ZERO, ONE),
            (ZERO, TWO, ONE, TWO, ZERO),
            (ZERO, ONE, ZERO, ONE, ZERO),
        ),
        (
            (ZERO, ONE, ONE, ONE, ZERO),
            (ONE, ZERO, TWO, ZERO, ONE),
            (ZERO, TWO, TWO, TWO, ZERO),
            (ZERO, ONE, ZERO, ONE, ZERO),
        ),
    ),
    FIVE: (
        (
            (ONE, ONE, ONE),
            (ZERO, ONE, ZERO),
            (TWO, TWO, ZERO),
            (ZERO, TWO, TWO),
            (ZERO, TWO, ZERO),
        ),
        (
            (ONE, TWO, ONE),
            (ZERO, ONE, ZERO),
            (TWO, TWO, TWO),
            (ZERO, TWO, ZERO),
            (ZERO, ONE, ZERO),
        ),
        (
            (ONE, ONE, ZERO),
            (ZERO, ONE, ONE),
            (ZERO, TWO, ZERO),
            (TWO, TWO, ZERO),
            (ZERO, TWO, TWO),
        ),
        (
            (ZERO, ONE, ONE, ONE, ZERO),
            (ZERO, ZERO, ONE, ZERO, ZERO),
            (ZERO, TWO, TWO, ZERO, ZERO),
            (ZERO, ZERO, TWO, TWO, ZERO),
            (ZERO, ZERO, TWO, ZERO, ZERO),
        ),
    ),
}


def _pick_9b30e358(
    values: tuple,
    diff_lb: float,
    diff_ub: float,
):
    x0 = unifint(diff_lb, diff_ub, (ZERO, len(values) - ONE))
    return values[x0]


def _materialize_pattern_9b30e358(
    template: Grid,
    bg: int,
    fg1: int,
    fg2: int,
) -> Grid:
    x0 = canvas(bg, shape(template))
    x1 = recolor(fg1, ofcolor(template, ONE))
    x2 = paint(x0, x1)
    x3 = recolor(fg2, ofcolor(template, TWO))
    x4 = paint(x2, x3)
    return x4


def _embed_pattern_9b30e358(
    pattern: Grid,
    width_: int,
    offset: int,
    bg: int,
    fg1: int,
    fg2: int,
) -> Grid:
    x0 = canvas(bg, astuple(height(pattern), width_))
    x1 = shift(recolor(fg1, ofcolor(pattern, fg1)), (ZERO, offset))
    x2 = paint(x0, x1)
    x3 = shift(recolor(fg2, ofcolor(pattern, fg2)), (ZERO, offset))
    x4 = paint(x2, x3)
    return x4


def _reorder_pattern_9b30e358(
    pattern: Grid,
) -> Grid:
    x0 = vconcat(bottomhalf(pattern), tophalf(pattern))
    return branch(even(height(pattern)), x0, pattern)


def _tile_pattern_9b30e358(
    pattern: Grid,
) -> Grid:
    x0 = height(pattern)
    x1 = divide(HEIGHT_9B30E358, x0)
    x2 = merge(repeat(pattern, x1))
    x3 = subtract(HEIGHT_9B30E358, multiply(x1, x0))
    x4 = crop(pattern, ORIGIN, astuple(x3, width(pattern)))
    x5 = vconcat(x2, x4)
    return x5


def generate_9b30e358(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _pick_9b30e358(tuple(PATTERNS_9B30E358.keys()), diff_lb, diff_ub)
        x1 = _pick_9b30e358(PATTERNS_9B30E358[x0], diff_lb, diff_ub)
        x2 = sample(interval(ZERO, TEN, ONE), THREE)
        x3 = x2[ZERO]
        x4 = x2[ONE]
        x5 = x2[TWO]
        x6 = _materialize_pattern_9b30e358(x1, x3, x4, x5)
        x7 = branch(choice((True, False)), vmirror(x6), x6)
        x8 = tuple(w for w in WIDTHS_9B30E358 if w >= width(x7))
        x9 = _pick_9b30e358(x8, diff_lb, diff_ub)
        x10 = subtract(x9, width(x7))
        x11 = unifint(diff_lb, diff_ub, (ZERO, x10))
        x12 = _embed_pattern_9b30e358(x7, x9, x11, x3, x4, x5)
        x13 = canvas(x3, astuple(subtract(HEIGHT_9B30E358, x0), x9))
        x14 = vconcat(x13, x12)
        x15 = _reorder_pattern_9b30e358(x12)
        x16 = _tile_pattern_9b30e358(x15)
        if mostcolor(x14) != x3:
            continue
        if colorcount(x12, x4) < TWO:
            continue
        if colorcount(x12, x5) < TWO:
            continue
        if verify_9b30e358(x14) != x16:
            continue
        return {"input": x14, "output": x16}
