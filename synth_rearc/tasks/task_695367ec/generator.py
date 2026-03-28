from synth_rearc.core import *


OUTPUT_SHAPE_695367EC = (15, 15)
OUTPUT_SIZE_695367EC = 15
INPUT_COLORS_695367EC = remove(ZERO, interval(ZERO, TEN, ONE))
INPUT_SHAPES_695367EC = tuple(
    (x0, x1)
    for x0 in range(TWO, OUTPUT_SIZE_695367EC)
    for x1 in range(max(TWO, x0 - SIX), min(OUTPUT_SIZE_695367EC - ONE, x0 + SIX) + ONE)
)


def generate_695367ec(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0, x1 = choice(INPUT_SHAPES_695367EC)
    x2 = choice(INPUT_COLORS_695367EC)
    x3 = canvas(x2, (x0, x1))
    x4 = canvas(ZERO, OUTPUT_SHAPE_695367EC)
    x5 = increment(x0)
    x6 = increment(x1)
    x7 = interval(x0, OUTPUT_SIZE_695367EC, x5)
    x8 = interval(x1, OUTPUT_SIZE_695367EC, x6)
    x9 = interval(ZERO, OUTPUT_SIZE_695367EC, ONE)
    x10 = product(x7, x9)
    x11 = product(x9, x8)
    x12 = combine(x10, x11)
    x13 = fill(x4, x2, x12)
    return {"input": x3, "output": x13}
