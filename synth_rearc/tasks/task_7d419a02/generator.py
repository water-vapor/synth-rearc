from synth_rearc.core import *

from .verifier import verify_7d419a02


def _apply_tall_rule_7d419a02(
    gi: Grid,
    body_top: Integer,
    body_left: Integer,
) -> Grid:
    x0 = body_top + ONE
    x1 = body_left + ONE
    x2 = ofcolor(gi, EIGHT)
    x3 = frozenset(
        (x4, x5)
        for x4, x5 in x2
        if (
            ((body_top - x4 + TWO) // THREE if x4 < body_top else (x4 - x0 + TWO) // THREE if x4 > x0 else ZERO)
            <= ((body_left - x5 + ONE) // TWO if x5 < body_left else (x5 - x1 + ONE) // TWO if x5 > x1 else ZERO)
            and positive((body_top - x4 + TWO) // THREE if x4 < body_top else (x4 - x0 + TWO) // THREE if x4 > x0 else ZERO)
        )
    )
    x6 = fill(gi, FOUR, x3)
    return x6


def _row_holes_7d419a02(
    width: Integer,
    forbidden: frozenset[int],
    diff_lb: float,
    diff_ub: float,
) -> frozenset[int]:
    x0 = tuple(x1 for x1 in range(ONE, width - ONE) if x1 not in forbidden)
    x1 = max(ONE, min(THREE, (width - FOUR) // FOUR))
    x2 = min(len(x0), unifint(diff_lb, diff_ub, (ZERO, x1)))
    if x2 == ZERO:
        return frozenset({})
    x3 = randint(ZERO, x2)
    if x3 == ZERO:
        return frozenset({})
    x4 = sample(x0, x3)
    return frozenset(x4)


def _orient_pair_7d419a02(
    gi: Grid,
    go: Grid,
) -> tuple[Grid, Grid]:
    x0 = choice((identity, rot90, rot270))
    x1 = x0(gi)
    x2 = x0(go)
    if choice((T, F)):
        x1 = vmirror(x1)
        x2 = vmirror(x2)
    if choice((T, F)):
        x1 = hmirror(x1)
        x2 = hmirror(x2)
    return x1, x2


def generate_7d419a02(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (FOUR, SEVEN))
        x1 = multiply(THREE, x0) + ONE
        x2 = unifint(diff_lb, diff_ub, (TEN, min(20, x1 - ONE)))
        x3 = randint(ONE, x0 - TWO)
        x4 = randint(TWO, x2 - FOUR)
        x5 = multiply(THREE, x3) + ONE
        x6 = canvas(ZERO, (x1, x2))
        for x7 in range(x0):
            x8 = multiply(THREE, x7) + ONE
            x9 = connect((x8, ONE), (x8, x2 - TWO))
            x10 = connect((x8 + ONE, ONE), (x8 + ONE, x2 - TWO))
            x6 = fill(x6, EIGHT, x9)
            x6 = fill(x6, EIGHT, x10)
        for x11 in range(x0):
            x12 = multiply(THREE, x11) + ONE
            for x13 in (x12, x12 + ONE):
                x14 = frozenset({x4, x4 + ONE}) if x11 == x3 else frozenset({})
                x15 = _row_holes_7d419a02(x2, x14, diff_lb, diff_ub)
                if len(x15) == ZERO:
                    continue
                x16 = frozenset((x13, x17) for x17 in x15)
                x6 = fill(x6, ZERO, x16)
        x17 = frozenset((x18, x19) for x18 in (x5, x5 + ONE) for x19 in (x4, x4 + ONE))
        x18 = fill(x6, SIX, x17)
        x19 = _apply_tall_rule_7d419a02(x18, x5, x4)
        x20, x21 = _orient_pair_7d419a02(x18, x19)
        if x20 == x21:
            continue
        if verify_7d419a02(x20) != x21:
            continue
        return {"input": x20, "output": x21}
