from synth_rearc.core import *


ACCENT_COLORS_C8B7CC0F = tuple(remove(ONE, remove(ZERO, interval(ZERO, TEN, ONE))))
OUTPUT_PATCHES_C8B7CC0F = tuple(
    frozenset((x0 // THREE, x0 % THREE) for x0 in range(x1))
    for x1 in range(TEN)
)


def _sample_isolated_c8b7cc0f(
    cands: Indices,
    count: Integer,
    blocked: Indices = frozenset({}),
) -> Indices:
    x0 = frozenset(cands)
    for _ in range(200):
        x1 = set(x0)
        for x2 in blocked:
            x1.discard(x2)
            x1.difference_update(dneighbors(x2))
        x3 = []
        while x1 and len(x3) < count:
            x4 = choice(tuple(x1))
            x3.append(x4)
            x1.discard(x4)
            x1.difference_update(dneighbors(x4))
        if len(x3) == count:
            return frozenset(x3)
    return frozenset({})


def generate_c8b7cc0f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (SEVEN, TEN))
        x1 = unifint(diff_lb, diff_ub, (SEVEN, TEN))
        x2 = unifint(diff_lb, diff_ub, (FOUR, x0))
        x3 = unifint(diff_lb, diff_ub, (FOUR, x1))
        x4 = (x2 - TWO) * (x3 - TWO)
        x5 = x0 * x1 - x2 * x3
        if x4 < THREE or x5 < TWO:
            continue
        x6 = randint(ZERO, x0 - x2)
        x7 = randint(ZERO, x1 - x3)
        x8 = frozenset({(x6, x7), (x6 + x2 - ONE, x7 + x3 - ONE)})
        x9 = box(x8)
        x10 = backdrop(x9)
        x11 = difference(x10, x9)
        x12 = unifint(diff_lb, diff_ub, (THREE, min(FIVE, len(x11))))
        x13 = max(TWO, x12 - ONE)
        x14 = min(FIVE, x5, x12 + ONE)
        if x13 > x14:
            continue
        x15 = _sample_isolated_c8b7cc0f(x11, x12)
        if len(x15) != x12:
            continue
        x16 = difference(asindices(canvas(ZERO, (x0, x1))), x10)
        x17 = unifint(diff_lb, diff_ub, (x13, x14))
        x18 = _sample_isolated_c8b7cc0f(x16, x17, x15)
        if len(x18) != x17:
            continue
        x19 = choice(ACCENT_COLORS_C8B7CC0F)
        x20 = canvas(ZERO, (x0, x1))
        x21 = fill(x20, ONE, x9)
        x22 = fill(x21, x19, combine(x15, x18))
        x23 = canvas(ZERO, (THREE, THREE))
        x24 = fill(x23, x19, OUTPUT_PATCHES_C8B7CC0F[x12])
        return {"input": x22, "output": x24}
