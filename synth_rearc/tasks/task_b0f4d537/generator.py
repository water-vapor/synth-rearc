from synth_rearc.core import *

from .verifier import verify_b0f4d537


OUTPUT_WIDTH_B0F4D537 = SEVEN
TEMPLATE_COLORS_B0F4D537 = (ONE, TWO, THREE)
BASE_COLUMN_PATTERNS_B0F4D537 = {
    ONE: ((ONE,), (TWO,), (THREE,), (FOUR,), (FIVE,)),
    TWO: ((ONE, THREE), (ONE, FOUR), (ONE, FIVE), (TWO, FOUR), (TWO, FIVE), (THREE, FIVE)),
    THREE: ((ONE, THREE, FIVE),),
}


def _expand_row_b0f4d537(
    x0: tuple[Integer, ...],
    x1: tuple[Integer, ...],
    x2: Integer,
) -> tuple[Integer, ...]:
    x3 = (NEG_ONE,) + x1 + (x2,)
    x4 = tuple(subtract(subtract(x3[x5 + ONE], x3[x5]), ONE) for x5 in range(len(x3) - ONE))
    x5 = tuple()
    for x6, x7 in enumerate(x0):
        if even(x6):
            x5 = x5 + repeat(x7, x4[x6 // TWO])
        else:
            x5 = x5 + (x7,)
    return x5


def _base_row_b0f4d537(
    x0: tuple[Integer, ...],
) -> tuple[Integer, ...]:
    x1 = tuple()
    for x2 in x0:
        x1 = x1 + (ZERO, x2)
    return x1 + (ZERO,)


def _special_row_b0f4d537(
    x0: tuple[Integer, ...],
) -> tuple[Integer, ...]:
    x1 = len(x0)
    while True:
        x2 = choice(TEMPLATE_COLORS_B0F4D537)
        x3 = choice((ZERO, ONE, TWO))
        if x3 == ZERO:
            x4 = tuple(x2 if even(x5) else x0[x5] for x5 in range(x1))
        elif x3 == ONE:
            x4 = repeat(x2, x1)
        else:
            x4 = tuple(
                x2 if even(x5) else choice((x0[x5], x2, choice(TEMPLATE_COLORS_B0F4D537)))
                for x5 in range(x1)
            )
        if x4 != x0:
            return x4


def _marker_row_b0f4d537(
    x0: tuple[Integer, ...],
    x1: Boolean,
) -> tuple[Integer, ...]:
    x2 = set(x0)
    if x1:
        x2.update({ZERO, SIX})
    return tuple(FOUR if x3 in x2 else ZERO for x3 in range(OUTPUT_WIDTH_B0F4D537))


def generate_b0f4d537(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (ONE, THREE))
        x1 = choice(BASE_COLUMN_PATTERNS_B0F4D537[x0])
        x2 = tuple(choice(TEMPLATE_COLORS_B0F4D537) for _ in range(x0))
        x3 = _base_row_b0f4d537(x2)
        x4 = unifint(diff_lb, diff_ub, (ONE, TWO))
        x5 = tuple(_special_row_b0f4d537(x3) for _ in range(x4))
        x6 = unifint(diff_lb, diff_ub, (max(SEVEN, add(multiply(TWO, x4), FIVE)), 12))
        x7 = tuple(sorted(sample(interval(ONE, decrement(x6), ONE), x4)))
        x8 = tuple()
        for x9 in x5:
            x8 = x8 + (x3, x9)
        x8 = x8 + (x3,)
        x10 = repeat(FIVE, size(x3))
        x11 = x8 + repeat(x10, subtract(x6, size(x8)))
        x12 = _marker_row_b0f4d537(x1, F)
        x13 = _marker_row_b0f4d537(x1, T)
        x14 = list(repeat(repeat(ZERO, OUTPUT_WIDTH_B0F4D537), x6))
        x14[ZERO] = x12
        x14[NEG_ONE] = x12
        for x15 in x7:
            x14[x15] = x13
        x16 = tuple(x14)
        x17 = _expand_row_b0f4d537(x3, x1, OUTPUT_WIDTH_B0F4D537)
        x18 = tuple(_expand_row_b0f4d537(x19, x1, OUTPUT_WIDTH_B0F4D537) for x19 in x5)
        x19 = list(repeat(x17, x6))
        for x20, x21 in zip(x7, x18):
            x19[x20] = x21
        x20 = tuple(x19)
        x21 = canvas(FIVE, astuple(x6, ONE))
        x22 = choice((T, F))
        x23 = branch(x22, x11, x16)
        x24 = branch(x22, x16, x11)
        x25 = hconcat(hconcat(x23, x21), x24)
        if verify_b0f4d537(x25) != x20:
            continue
        return {"input": x25, "output": x20}
