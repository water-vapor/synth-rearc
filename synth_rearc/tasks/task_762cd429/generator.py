from synth_rearc.core import *

from .verifier import verify_762cd429


NONZERO_COLORS_762CD429 = (ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)


def generate_762cd429(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((FOUR, EIGHT))
        x1 = branch(equality(x0, FOUR), TEN, 16)
        x2 = branch(equality(x0, FOUR), 14, 30)
        x3 = branch(equality(x0, FOUR), FOUR, SEVEN)
        x4 = choice(NONZERO_COLORS_762CD429)
        x5 = choice(NONZERO_COLORS_762CD429)
        x6 = choice(NONZERO_COLORS_762CD429)
        x7 = choice(NONZERO_COLORS_762CD429)
        x8 = frozenset({
            (x4, (x3, ZERO)),
            (x5, (x3, ONE)),
            (x6, (increment(x3), ZERO)),
            (x7, (increment(x3), ONE)),
        })
        if numcolors(x8) == ONE:
            continue
        x9 = canvas(ZERO, (x1, x2))
        x10 = paint(x9, x8)
        x11 = x9
        x12 = ZERO
        x13 = ONE
        while x12 < x2:
            x14 = upscale(x8, x13)
            x15 = astuple(subtract(ONE, x13), x12)
            x16 = shift(x14, x15)
            x11 = paint(x11, x16)
            x12 = add(x12, width(x14))
            x13 = double(x13)
        if verify_762cd429(x10) != x11:
            continue
        return {"input": x10, "output": x11}
