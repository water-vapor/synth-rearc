from arc2.core import *


CYCLE_AAEF0977 = (THREE, FOUR, ZERO, FIVE, TWO, EIGHT, NINE, SIX, ONE)


def _render_aaef0977(
    size_: Integer,
    seed_loc: IntegerTuple,
    seed_color: Integer,
) -> Grid:
    x0 = canvas(ZERO, (size_, size_))
    x1 = CYCLE_AAEF0977.index(seed_color)
    x2 = frozenset(
        (CYCLE_AAEF0977[(x1 + manhattan(initset(seed_loc), initset(x3))) % len(CYCLE_AAEF0977)], x3)
        for x3 in asindices(x0)
    )
    x3 = paint(x0, x2)
    return x3


def generate_aaef0977(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (EIGHT, 12))
    x1 = canvas(SEVEN, (x0, x0))
    x2 = astuple(randint(ZERO, decrement(x0)), randint(ZERO, decrement(x0)))
    x3 = choice(CYCLE_AAEF0977)
    x4 = fill(x1, x3, initset(x2))
    x5 = _render_aaef0977(x0, x2, x3)
    return {"input": x4, "output": x5}
