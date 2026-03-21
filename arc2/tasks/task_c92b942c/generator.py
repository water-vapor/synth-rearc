from arc2.core import *

from .verifier import verify_c92b942c


FG_COLORS_C92B942C = (TWO, FOUR, FIVE, SIX)


def _cyclic_distance_c92b942c(
    a: Integer,
    b: Integer,
    modulus: Integer,
) -> Integer:
    x0 = abs(a - b)
    return min(x0, modulus - x0)


def _sample_spread_values_c92b942c(
    modulus: Integer,
    count: Integer,
) -> tuple[Integer, ...]:
    x0 = list(range(modulus))
    shuffle(x0)
    x1 = []
    for x2 in x0:
        x3 = T
        for x4 in x1:
            if _cyclic_distance_c92b942c(x2, x4, modulus) < TWO:
                x3 = F
                break
        if x3:
            x1.append(x2)
        if len(x1) == count:
            return tuple(sorted(x1))
    return tuple()


def generate_c92b942c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (TWO, FIVE))
        x1 = unifint(diff_lb, diff_ub, (THREE, SIX))
        x2 = choice(FG_COLORS_C92B942C)
        x3 = max(ONE, min(TWO, x0 // TWO))
        x4 = max(ONE, min(TWO, x1 // TWO))
        x5 = choice((ONE, ONE, ONE, x3))
        x6 = _sample_spread_values_c92b942c(x0, x5)
        if len(x6) != x5:
            continue
        x7 = []
        for x8 in x6:
            x9 = choice((ONE, ONE, x4))
            x10 = _sample_spread_values_c92b942c(x1, x9)
            if len(x10) != x9:
                x7 = []
                break
            for x11 in x10:
                x7.append((x8, x11))
        if len(x7) == ZERO:
            continue
        x12 = frozenset(x7)
        if len(x12) > THREE:
            continue
        x13 = canvas(ZERO, (x0, x1))
        x14 = fill(x13, x2, x12)
        x15 = hconcat(x14, x14)
        x16 = hconcat(x15, x14)
        x17 = vconcat(x16, x16)
        x18 = vconcat(x17, x16)
        x19 = ofcolor(x18, x2)
        x20 = mapply(hfrontier, x19)
        x21 = underfill(x18, ONE, x20)
        x22 = combine(shift(x19, NEG_UNITY), shift(x19, UNITY))
        x23 = fill(
            x21,
            THREE,
            difference(x22, x19),
        )
        if verify_c92b942c(x14) != x23:
            continue
        return {"input": x14, "output": x23}
