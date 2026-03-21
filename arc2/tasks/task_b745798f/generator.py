from arc2.core import *


TL_MARKER_B745798F = frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO)})
TR_MARKER_B745798F = frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ONE)})
BL_MARKER_B745798F = frozenset({(ZERO, ZERO), (ONE, ZERO), (ONE, ONE)})
BR_MARKER_B745798F = frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE)})

MARKERS_B745798F = (
    TL_MARKER_B745798F,
    TR_MARKER_B745798F,
    BL_MARKER_B745798F,
    BR_MARKER_B745798F,
)

SIDE_PAIRS_B745798F = (
    (ZERO, ONE),
    (TWO, THREE),
    (ZERO, TWO),
    (ONE, THREE),
)


def _corner_patches_b745798f(
    side: Integer,
) -> Tuple:
    x0 = decrement(side)
    x1 = decrement(halve(side))
    x2 = increment(halve(side))
    x3 = combine(connect((ZERO, ZERO), (ZERO, x1)), connect((ZERO, ZERO), (x1, ZERO)))
    x4 = combine(connect((ZERO, x2), (ZERO, x0)), connect((ZERO, x0), (x1, x0)))
    x5 = combine(connect((x2, ZERO), (x0, ZERO)), connect((x0, ZERO), (x0, x1)))
    x6 = combine(connect((x2, x0), (x0, x0)), connect((x0, x2), (x0, x0)))
    return (x3, x4, x5, x6)


def _corner_colors_b745798f() -> Tuple:
    x0 = remove(EIGHT, interval(ZERO, TEN, ONE))
    x1 = choice((THREE, FOUR, FOUR))
    if x1 == FOUR:
        return tuple(sample(x0, FOUR))
    x2 = tuple(sample(x0, THREE))
    x3 = list(x2)
    x4 = choice(SIDE_PAIRS_B745798F)
    x5 = [None] * FOUR
    x5[x4[0]] = x3[ZERO]
    x5[x4[1]] = x3[ZERO]
    x6 = tuple(idx for idx in range(FOUR) if idx not in x4)
    x5[x6[0]] = x3[ONE]
    x5[x6[1]] = x3[TWO]
    return tuple(x5)


def generate_b745798f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (TWO, 14))
        x1 = increment(double(x0))
        x2 = canvas(EIGHT, (x1, x1))
        x3 = canvas(EIGHT, (x1, x1))
        x4 = _corner_patches_b745798f(x1)
        x5 = _corner_colors_b745798f()
        x6 = frozenset()
        x7 = []
        x8 = ZERO
        while x8 < FOUR:
            x9 = (randint(ZERO, x1 - TWO), randint(ZERO, x1 - TWO))
            x10 = shift(MARKERS_B745798F[x8], x9)
            x11 = intersection(x6, x10)
            if len(x11) != ZERO:
                continue
            x7.append(x10)
            x6 = combine(x6, x10)
            x8 = increment(x8)
        x12 = ZERO
        while x12 < FOUR:
            x13 = fill(x2, x5[x12], x7[x12])
            x14 = fill(x3, x5[x12], x4[x12])
            x2 = x13
            x3 = x14
            x12 = increment(x12)
        x15 = objects(x2, T, F, T)
        if len(x15) != FOUR:
            continue
        return {"input": x2, "output": x3}
