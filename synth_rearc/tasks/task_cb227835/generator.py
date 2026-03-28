from synth_rearc.core import *


def _render_cb227835(
    top: IntegerTuple,
    bottom: IntegerTuple,
    dims: IntegerTuple,
) -> dict:
    x0 = canvas(ZERO, dims)
    x1 = fill(x0, EIGHT, initset(top))
    x2 = fill(x1, EIGHT, initset(bottom))
    x3 = subtract(bottom, top)
    x4 = first(x3)
    x5 = last(x3)
    x6 = sign(x5)
    x7 = multiply(x5, x6)
    x8 = greater(x7, x4)
    x9 = branch(x8, subtract(x7, x4), subtract(x4, x7))
    x10 = branch(x8, astuple(ZERO, multiply(x6, x9)), astuple(x9, ZERO))
    x11 = add(top, x10)
    x12 = subtract(bottom, x10)
    x13 = connect(x11, bottom)
    x14 = connect(top, x12)
    x15 = connect(top, x11)
    x16 = connect(x12, bottom)
    x17 = combine(x13, x14)
    x18 = combine(x15, x16)
    x19 = combine(x17, x18)
    x20 = difference(x19, combine(initset(top), initset(bottom)))
    x21 = fill(x2, THREE, x20)
    return {"input": x2, "output": x21}


def _biased_major_cb227835(limit: Integer) -> Integer:
    x0 = randint(FIVE, limit)
    x1 = randint(FIVE, limit)
    return max(x0, x1)


def _sample_endpoint_cb227835(
    low: Integer,
    high: Integer,
    prefer_high: Boolean,
) -> Integer:
    if low == high:
        return low
    x0 = randint(low, high)
    x1 = randint(low, high)
    x2 = branch(prefer_high, high, low)
    return choice((x0, x1, x2))


def generate_cb227835(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (11, 14))
        x1 = unifint(diff_lb, diff_ub, (11, 15))
        x2 = choice((T, T, F))
        x3 = choice((NEG_ONE, ONE))
        x4 = branch(x2, x1 - ONE, x0 - ONE)
        x5 = branch(x2, x0 - ONE, x1 - ONE)
        if x4 < FIVE or x5 < TWO:
            continue
        x6 = _biased_major_cb227835(x4)
        x7 = min(x6 - ONE, x5)
        if x7 < TWO:
            continue
        x8 = randint(TWO, x7)
        if x2:
            x9 = x8
            x10 = x6
        else:
            x9 = x6
            x10 = x8
        x11 = x0 - x9 - ONE
        if x3 == ONE:
            x12 = x1 - x10 - ONE
            x13 = _sample_endpoint_cb227835(ZERO, x12, F)
        else:
            x12 = x1 - ONE
            x13 = _sample_endpoint_cb227835(x10, x12, T)
        x14 = _sample_endpoint_cb227835(ZERO, x11, F)
        x15 = astuple(x14, x13)
        x16 = astuple(x14 + x9, x13 + x3 * x10)
        x17 = _render_cb227835(x15, x16, astuple(x0, x1))
        return x17
