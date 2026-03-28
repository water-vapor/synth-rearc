from synth_rearc.core import *


def _quadrants_58743b76(side: int) -> tuple[Indices, Indices, Indices, Indices]:
    x0 = side // TWO
    x1 = frozenset((x2, x3) for x2 in range(x0) for x3 in range(x0))
    x2 = frozenset((x3, x4) for x3 in range(x0) for x4 in range(x0, side))
    x3 = frozenset((x4, x5) for x4 in range(x0, side) for x5 in range(x0))
    x4 = frozenset((x5, x6) for x5 in range(x0, side) for x6 in range(x0, side))
    return (x1, x2, x3, x4)


def _sample_markers_58743b76(
    diff_lb: float,
    diff_ub: float,
    side: int,
) -> frozenset[tuple[int, int]]:
    x0 = _quadrants_58743b76(side)
    x1 = max(TWO, side // TWO - ONE)
    x2 = []
    for x3 in x0:
        x4 = unifint(diff_lb, diff_ub, (ONE, min(len(x3), x1)))
        x2.extend(sample(tuple(x3), x4))
    return frozenset(x2)


def generate_58743b76(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = multiply(TWO, unifint(diff_lb, diff_ub, (FOUR, EIGHT)))
    x1 = x0 + TWO
    x2 = tuple(x3 for x3 in interval(ONE, TEN, ONE) if x3 != EIGHT)
    x3 = sample(x2, FOUR)
    x4 = randint(ZERO, THREE)
    x5 = x3[x4]
    x6 = _sample_markers_58743b76(diff_lb, diff_ub, x0)
    x7 = frozenset((x8, x9) for x8 in range(TWO) for x9 in range(x1))
    x8 = frozenset((x9, x10) for x9 in range(x1) for x10 in range(TWO))
    x9 = frozenset(
        {
            (x3[ZERO], (ZERO, ZERO)),
            (x3[ONE], (ZERO, ONE)),
            (x3[TWO], (ONE, ZERO)),
            (x3[THREE], (ONE, ONE)),
        }
    )
    x10 = canvas(ZERO, (x1, x1))
    x11 = fill(x10, EIGHT, combine(x7, x8))
    x12 = paint(x11, x9)
    x13 = fill(x12, x5, shift(x6, TWO_BY_TWO))
    x14 = x12
    for x15, x16 in enumerate(_quadrants_58743b76(x0)):
        x17 = shift(intersection(x6, x16), TWO_BY_TWO)
        x14 = fill(x14, x3[x15], x17)
    x15 = choice((identity, vmirror, hmirror, rot180))
    return {"input": x15(x13), "output": x15(x14)}
