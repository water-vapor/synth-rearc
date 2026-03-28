from synth_rearc.core import *


REGION_DIRECTIONS_18286EF8 = (
    (-ONE, -ONE),
    (-ONE, ZERO),
    (-ONE, ONE),
    (ZERO, -ONE),
    (ZERO, ONE),
    (ONE, -ONE),
    (ONE, ZERO),
    (ONE, ONE),
)

CENTER_PATCH_18286EF8 = product(interval(ZERO, THREE, ONE), interval(ZERO, THREE, ONE))
NOISE_COLORS_18286EF8 = (ONE, TWO, THREE, FOUR, EIGHT)
NOISE_COUNTS_18286EF8 = (ZERO, ZERO, ONE, ONE, ONE, TWO, TWO, THREE)


def generate_18286ef8(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (ONE, 12))
    x1 = unifint(diff_lb, diff_ub, (ONE, 12))
    x2 = unifint(diff_lb, diff_ub, (ONE, 12))
    x3 = unifint(diff_lb, diff_ub, (ONE, 12))
    x4 = x0 + x2 + FIVE
    x5 = x1 + x3 + FIVE
    x6 = canvas(SEVEN, (x4, x5))
    x7 = connect((x0, ZERO), (x0, decrement(x5)))
    x8 = fill(x6, ZERO, x7)
    x9 = x0 + FOUR
    x10 = connect((x9, ZERO), (x9, decrement(x5)))
    x11 = fill(x8, ZERO, x10)
    x12 = connect((ZERO, x1), (decrement(x4), x1))
    x13 = fill(x11, ZERO, x12)
    x14 = x1 + FOUR
    x15 = connect((ZERO, x14), (decrement(x4), x14))
    x16 = fill(x13, ZERO, x15)
    x17 = astuple(increment(x0), increment(x1))
    x18 = shift(CENTER_PATCH_18286EF8, x17)
    x19 = fill(x16, FIVE, x18)
    x20 = add(x17, (ONE, ONE))
    x21 = fill(x19, NINE, initset(x20))
    x22 = (ZERO, increment(x0), x0 + FIVE)
    x23 = (x0, THREE, x2)
    x24 = (ZERO, increment(x1), x1 + FIVE)
    x25 = (x1, THREE, x3)
    x26 = choice(REGION_DIRECTIONS_18286EF8)
    x27 = x26[ZERO] + ONE
    x28 = x26[ONE] + ONE
    x29 = interval(x22[x27], x22[x27] + x23[x27], ONE)
    x30 = interval(x24[x28], x24[x28] + x25[x28], ONE)
    x31 = totuple(product(x29, x30))
    x32 = choice(x31)
    x21 = fill(x21, SIX, initset(x32))
    for x33 in REGION_DIRECTIONS_18286EF8:
        x34 = x33[ZERO] + ONE
        x35 = x33[ONE] + ONE
        x36 = interval(x22[x34], x22[x34] + x23[x34], ONE)
        x37 = interval(x24[x35], x24[x35] + x25[x35], ONE)
        x38 = totuple(product(x36, x37))
        x39 = tuple(x40 for x40 in x38 if x40 != x32) if x33 == x26 else x38
        x40 = min(choice(NOISE_COUNTS_18286EF8), len(x39))
        for x41 in sample(x39, x40):
            x21 = fill(x21, choice(NOISE_COLORS_18286EF8), initset(x41))
    x42 = fill(x21, FIVE, initset(x20))
    x43 = add(x20, x26)
    x44 = fill(x42, NINE, initset(x43))
    x45 = fill(x44, NINE, initset(x32))
    return {"input": x21, "output": x45}
