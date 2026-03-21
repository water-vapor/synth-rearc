from arc2.core import *


def _canonical_rows_97c75046(
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[int, int], ...]:
    x0 = unifint(diff_lb, diff_ub, (THREE, EIGHT))
    x1 = unifint(diff_lb, diff_ub, (TWO, SIX))
    x2 = add(x1, ONE)
    x3 = add(x2, decrement(x0))
    x5 = x3
    x6 = []
    x7 = []
    x8 = ONE if equality(x0, THREE) else unifint(diff_lb, diff_ub, (ONE, decrement(x0)))
    for x9 in range(x0):
        x10 = subtract(x3, x9)
        if x9 < x8:
            x11 = choice((ZERO, ZERO, ONE))
        else:
            x11 = choice((NEG_ONE, ZERO, ZERO, ONE))
        x12 = add(x5, x11)
        x12 = max(x12, x10)
        x13 = subtract(add(x10, x12), ONE)
        x6.append(x10)
        x7.append(x13)
        x5 = x12
    x14 = tuple(pair(tuple(x6), tuple(x7)))
    x15 = tuple(x18 - x17 for x17, x18 in x14)
    x16 = minimum(x15)
    x17 = maximum(x15)
    if both(equality(x16, ZERO), equality(x17, ZERO)):
        x18 = x14[-ONE]
        x19 = add(x18[1], ONE)
        x14 = x14[:-ONE] + ((x18[0], x19),)
    return x14


def _canonical_example_97c75046(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _canonical_rows_97c75046(diff_lb, diff_ub)
        x1 = size(x0)
        x2 = decrement(x1)
        x3 = x0[ZERO][ZERO]
        x4 = maximum(apply(last, x0))
        x5 = unifint(diff_lb, diff_ub, (ONE, FOUR))
        x6 = unifint(diff_lb, diff_ub, (ZERO, FOUR))
        x7 = unifint(diff_lb, diff_ub, (ZERO, FOUR))
        x8 = unifint(diff_lb, diff_ub, (ZERO, FOUR))
        x9 = unifint(diff_lb, diff_ub, (ONE, FOUR))
        x10 = add(add(x4, x7), ONE)
        x11 = add(add(x1, x5), x6)
        x12 = add(add(x10, x8), x9)
        if greater(x11, 30) or greater(x12, 30):
            continue
        x13 = canvas(SEVEN, (x11, x12))
        x14 = add(x5, x2)
        x15 = x6
        x16 = fill(x13, FIVE, initset((x14, x15)))
        for x17, x18 in x0:
            x19 = add(x5, subtract(x3, x17))
            x20 = add(x6, x17)
            x21 = add(x6, x18)
            x22 = connect((x19, x20), (x19, x21))
            x16 = fill(x16, ZERO, x22)
        x23 = fill(x16, SEVEN, initset((x14, x15)))
        x24 = fill(x23, FIVE, initset((subtract(x5, ONE), add(x6, x3))))
        x25 = choice(
            (
                identity,
                rot90,
                rot180,
                rot270,
                hmirror,
                vmirror,
                lambda g: rot90(hmirror(g)),
                lambda g: rot90(vmirror(g)),
            )
        )
        x26 = x25(x16)
        x27 = x25(x24)
        if equality(x26, x27):
            continue
        from .verifier import verify_97c75046

        if verify_97c75046(x26) != x27:
            continue
        return {"input": x26, "output": x27}


def generate_97c75046(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    return _canonical_example_97c75046(diff_lb, diff_ub)
