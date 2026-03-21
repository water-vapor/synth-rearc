from arc2.core import *


CENTER_DIMS_99306F82 = (
    (TWO, TWO),
    (TWO, THREE),
    (THREE, TWO),
    (THREE, THREE),
    (THREE, FOUR),
    (FOUR, THREE),
)
FILL_COLORS_99306F82 = interval(TWO, TEN, ONE)


def generate_99306f82(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (TWO, SEVEN))
    x1 = choice(CENTER_DIMS_99306F82)
    x2 = add(multiply(subtract(x0, ONE), TWO), x1[ZERO])
    x3 = add(multiply(subtract(x0, ONE), TWO), x1[ONE])
    x4 = add(x2, TWO)
    x5 = add(x3, TWO)
    x6 = unifint(diff_lb, diff_ub, (ONE, FOUR))
    x7 = unifint(diff_lb, diff_ub, (ONE, FOUR))
    x8 = add(add(x0, x4), x6)
    x9 = add(add(x0, x5), x7)
    x10 = canvas(ZERO, (x8, x9))
    x11 = box(frozenset({(x0, x0), (subtract(add(x0, x4), ONE), subtract(add(x0, x5), ONE))}))
    x12 = fill(x10, ONE, x11)
    x13 = tuple(sample(FILL_COLORS_99306F82, x0))
    x14 = x12
    for x15, x16 in enumerate(x13):
        x17 = fill(x14, x16, initset((x15, x15)))
        x14 = x17
    x18 = x14
    x19 = backdrop(inbox(x11))
    for x20 in x13[:-ONE]:
        x21 = box(x19)
        x18 = fill(x18, x20, x21)
        x19 = backdrop(inbox(x19))
    x22 = fill(x18, last(x13), x19)
    return {"input": x14, "output": x22}
