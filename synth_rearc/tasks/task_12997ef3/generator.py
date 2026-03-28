from synth_rearc.core import *


def _template_indices_12997ef3() -> Indices:
    x0 = totuple(asindices(canvas(ZERO, (THREE, THREE))))
    while True:
        x1 = choice((FOUR, FIVE, FIVE, FIVE))
        x2 = frozenset(sample(x0, x1))
        if height(x2) != THREE:
            continue
        if width(x2) != THREE:
            continue
        return x2


def generate_12997ef3(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = interval(TWO, TEN, ONE)
    x1 = _template_indices_12997ef3()
    x2 = fill(canvas(ZERO, (THREE, THREE)), ONE, x1)
    x3 = unifint(diff_lb, diff_ub, (TWO, FOUR))
    x4 = sample(x0, x3)
    x5 = choice((TWO, TWO, THREE))
    x6 = choice((True, False))
    x7 = False
    if not x6 and x3 == TWO:
        x7 = choice((True, False, False))
    while True:
        if x6:
            x8 = unifint(diff_lb, diff_ub, (NINE, 11))
            x9 = max(NINE, THREE + x5 * (x3 - ONE) + ONE)
            x10 = unifint(diff_lb, diff_ub, (x9, 14))
            x11 = tuple(range(ZERO, min(x8 - FIVE, FOUR) + ONE))
            x12 = tuple(range(ZERO, min(x10 - THREE, FOUR) + ONE))
            x13 = choice(x11)
            x14 = choice(x12)
            x15 = tuple(range(x13 + FOUR, x8))
            x16 = choice(x15)
            x17 = tuple(range(ZERO, x10 - x5 * (x3 - ONE)))
            x18 = choice(x17)
            x19 = tuple((x16, x18 + x5 * k) for k in range(x3))
            x20 = (x8, x10)
        else:
            x8 = max(NINE, ONE + x5 * (x3 - ONE))
            x21 = unifint(diff_lb, diff_ub, (x8, 11))
            x10 = unifint(diff_lb, diff_ub, (NINE, 11))
            x22 = tuple(range(ZERO, min(x21 - THREE, FOUR) + ONE))
            x23 = tuple(range(ONE, min(x10 - THREE, FOUR) + ONE))
            x13 = choice(x22)
            x14 = choice(x23)
            x24 = tuple(range(ZERO, x21 - x5 * (x3 - ONE)))
            x25 = choice(x24)
            x26 = tuple(range(ZERO, x14 - ONE))
            x27 = tuple(range(x14 + FOUR, x10))
            if x7:
                x27 = tuple(range(x14 + FOUR, x10 - x5 * (x3 - ONE)))
            x28 = ()
            if len(x26) > ZERO:
                x28 = x28 + tuple(("left", x29) for x29 in x26)
            if len(x27) > ZERO:
                x28 = x28 + tuple(("right", x29) for x29 in x27)
            if len(x28) == ZERO:
                continue
            x29 = choice(x28)
            x30 = last(x29)
            if x7 and first(x29) == "right":
                x19 = tuple((x25 + x5 * k, x30 + x5 * k) for k in range(x3))
            else:
                x19 = tuple((x25 + x5 * k, x30) for k in range(x3))
            x20 = (x21, x10)
        x31 = shift(x1, (x13, x14))
        if len(intersection(x31, frozenset(x19))) == ZERO:
            break
    x32 = canvas(ZERO, x20)
    x33 = fill(x32, ONE, x31)
    for x34, x35 in zip(x4, x19):
        x33 = fill(x33, x34, initset(x35))
    x36 = tuple(replace(x2, ONE, x37) for x37 in x4)
    x38 = first(x36)
    for x39 in x36[ONE:]:
        x38 = branch(x6, hconcat(x38, x39), vconcat(x38, x39))
    return {"input": x33, "output": x38}
