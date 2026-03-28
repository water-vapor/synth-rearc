from synth_rearc.core import *


SAMPLE_COLORS_EF26CBF6 = (TWO, THREE, FIVE, SIX, SEVEN, EIGHT, NINE)
LOCAL_CELLS_EF26CBF6 = tuple((i, j) for i in range(THREE) for j in range(THREE))
ROW_STARTS_EF26CBF6 = (ZERO, FOUR, EIGHT)


def _random_pattern_ef26cbf6(
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    x0 = unifint(diff_lb, diff_ub, (THREE, SIX))
    return frozenset(sample(LOCAL_CELLS_EF26CBF6, x0))


def _render_canonical_ef26cbf6(
    colors: tuple[Integer, Integer, Integer],
    patterns: tuple[Indices, Indices, Indices],
    sample_left: Boolean,
) -> tuple[Grid, Grid]:
    gi = canvas(ZERO, (11, 7))
    for x0 in (THREE, SEVEN):
        gi = fill(gi, FOUR, hfrontier((x0, ZERO)))
    gi = fill(gi, FOUR, vfrontier((ZERO, THREE)))
    go = gi
    x1 = branch(sample_left, ZERO, FOUR)
    x2 = branch(sample_left, FOUR, ZERO)
    x3 = increment(x1)
    for x4, x5, x6 in zip(ROW_STARTS_EF26CBF6, colors, patterns):
        x7 = frozenset({(increment(x4), x3)})
        x8 = shift(x6, (x4, x2))
        gi = fill(gi, x5, x7)
        gi = fill(gi, ONE, x8)
        go = fill(go, x5, x7)
        go = fill(go, x5, x8)
    return gi, go


def generate_ef26cbf6(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = choice(("left", "right", "top", "bottom"))
    x1 = x0 in ("left", "top")
    x2 = tuple(sample(SAMPLE_COLORS_EF26CBF6, THREE))
    x3 = []
    while len(x3) < THREE:
        x4 = _random_pattern_ef26cbf6(diff_lb, diff_ub)
        if x4 not in x3:
            x3.append(x4)
    gi, go = _render_canonical_ef26cbf6(x2, tuple(x3), x1)
    if x0 in ("top", "bottom"):
        gi = rot90(gi)
        go = rot90(go)
    return {"input": gi, "output": go}
