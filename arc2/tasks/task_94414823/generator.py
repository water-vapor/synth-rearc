from arc2.core import *


MARKER_COLORS_94414823 = remove(FIVE, interval(ONE, TEN, ONE))


def generate_94414823(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = canvas(ZERO, (TEN, TEN))
    x1 = unifint(diff_lb, diff_ub, (ONE, THREE))
    x2 = unifint(diff_lb, diff_ub, (ONE, THREE))
    x3 = box(shift(asindices(canvas(ZERO, (SIX, SIX))), (x1, x2)))
    x4 = decrement(x1)
    x5 = decrement(x2)
    x6 = add(x1, SIX)
    x7 = add(x2, SIX)
    x8 = (x4, x5)
    x9 = (x4, x7)
    x10 = (x6, x7)
    x11 = (x6, x5)
    x12 = (
        (x8, x9),
        (x9, x10),
        (x11, x10),
        (x8, x11),
    )
    x13 = choice(x12)
    x14, x15 = sample(MARKER_COLORS_94414823, TWO)
    x16 = first(x13)
    x17 = last(x13)
    x18 = contained(x16, frozenset({x8, x10}))
    x19 = branch(x18, x16, x17)
    x20 = branch(x18, x17, x16)
    x21 = fill(x0, FIVE, x3)
    x22 = fill(x21, x14, initset(x19))
    x23 = fill(x22, x15, initset(x20))
    x24 = add((x1, x2), (ONE, ONE))
    x25 = shift(asindices(canvas(ZERO, TWO_BY_TWO)), x24)
    x26 = shift(x25, ZERO_BY_TWO)
    x27 = shift(x25, TWO_BY_ZERO)
    x28 = shift(x26, TWO_BY_ZERO)
    x29 = fill(x23, x14, x25)
    x30 = fill(x29, x15, x26)
    x31 = fill(x30, x15, x27)
    x32 = fill(x31, x14, x28)
    return {"input": x23, "output": x32}
