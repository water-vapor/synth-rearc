from synth_rearc.core import *

from .verifier import verify_4f537728


GRID_SIDE_4F537728 = 20
PHASES_4F537728 = (ZERO, ONE)
SPECIAL_COLORS_4F537728 = interval(TWO, TEN, ONE)


def _foreground_axis_4f537728(
    phase: Integer,
) -> FrozenSet[Integer]:
    return frozenset(
        x0 for x0 in interval(ZERO, GRID_SIDE_4F537728, ONE)
        if (x0 + phase) % THREE != TWO
    )


def _full_band_starts_4f537728(
    phase: Integer,
) -> tuple[Integer, ...]:
    return tuple(
        x0 for x0 in interval(ZERO, decrement(GRID_SIDE_4F537728), ONE)
        if (x0 + phase) % THREE == ZERO
    )


def generate_4f537728(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(PHASES_4F537728)
        x1 = choice(PHASES_4F537728)
        x2 = _foreground_axis_4f537728(x0)
        x3 = _foreground_axis_4f537728(x1)
        x4 = choice(_full_band_starts_4f537728(x0))
        x5 = choice(_full_band_starts_4f537728(x1))
        x6 = choice(SPECIAL_COLORS_4F537728)
        x7 = canvas(ZERO, (GRID_SIDE_4F537728, GRID_SIDE_4F537728))
        x8 = product(x2, x3)
        x9 = fill(x7, ONE, x8)
        x10 = frozenset({x4, increment(x4)})
        x11 = frozenset({x5, increment(x5)})
        x12 = product(x10, x11)
        gi = fill(x9, x6, x12)
        x13 = product(x10, x3)
        x14 = product(x2, x11)
        x15 = combine(x13, x14)
        go = fill(gi, x6, x15)
        if verify_4f537728(gi) != go:
            continue
        return {"input": gi, "output": go}
