from synth_rearc.core import *

from .helpers import MOTIF_BANK_8BA14F53


COUNT_BAG_8BA14F53 = (
    ONE,
    ONE,
    TWO,
    TWO,
    THREE,
    THREE,
    THREE,
    FOUR,
    SIX,
)


def _render_output_8ba14f53(
    specs: tuple[tuple[Integer, Integer], ...],
) -> Grid:
    x0 = canvas(ZERO, (THREE, THREE))
    x1 = ZERO
    for x2, x3 in specs:
        x4 = x3
        while x4 > ZERO:
            x5 = min(THREE, x4)
            x6 = frozenset((x1, x7) for x7 in range(x5))
            x0 = fill(x0, x2, x6)
            x4 = subtract(x4, x5)
            x1 = increment(x1)
    return x0


def _row_cost_8ba14f53(
    count: Integer,
) -> Integer:
    return divide(add(count, TWO), THREE)


def generate_8ba14f53(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(COUNT_BAG_8BA14F53)
        x1 = choice(COUNT_BAG_8BA14F53)
        if greater(add(_row_cost_8ba14f53(x0), _row_cost_8ba14f53(x1)), THREE):
            continue
        x2 = choice(MOTIF_BANK_8BA14F53[x0])
        x3 = choice(MOTIF_BANK_8BA14F53[x1])
        x4 = width(x2)
        x5 = width(x3)
        x6 = subtract(NINE, add(x4, x5))
        if x6 < ZERO:
            continue
        x7 = tuple(x8 for x8 in (ZERO, ONE) if x8 <= x6)
        x8 = choice(x7)
        x9 = subtract(x6, x8)
        x10 = randint(ZERO, x9)
        x11 = subtract(x9, x10)
        x12 = branch(equality(height(x2), FOUR), ZERO, choice((ZERO, ONE)))
        x13 = branch(equality(height(x3), FOUR), ZERO, choice((ZERO, ONE)))
        x14 = tuple(remove(ZERO, interval(ZERO, TEN, ONE)))
        x15 = choice(x14)
        x16 = choice(remove(x15, x14))
        x17 = shift(x2, (x12, x10))
        x18 = shift(x3, (x13, add(add(x10, x4), x8)))
        x19 = canvas(ZERO, (FOUR, NINE))
        x20 = fill(x19, x15, x17)
        x21 = fill(x20, x16, x18)
        x22 = _render_output_8ba14f53(((x15, x0), (x16, x1)))
        x23 = objects(x21, T, F, F)
        x24 = sfilter(x23, lambda x25: color(x25) != ZERO)
        if size(x24) != TWO:
            continue
        if x22 == x21:
            continue
        return {"input": x21, "output": x22}
