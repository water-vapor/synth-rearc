from synth_rearc.core import *

from .verifier import verify_aab50785


NO_EIGHT_COLORS_AAB50785 = (
    ZERO,
    ZERO,
    ZERO,
    ZERO,
    ONE,
    TWO,
    THREE,
    FOUR,
    FIVE,
    SIX,
    SEVEN,
    NINE,
)


def _sample_row_layout_aab50785(
    npairs: Integer,
) -> tuple[tuple[Integer, ...], Integer]:
    x0 = max(TEN, add(multiply(TWO, npairs), SIX))
    x1 = min(18, add(multiply(TWO, npairs), TEN))
    while True:
        x2 = [randint(ZERO, FOUR)]
        for _ in range(npairs - ONE):
            x2.append(add(x2[-ONE], randint(THREE, FOUR)))
        x3 = add(add(x2[-ONE], TWO), randint(TWO, FIVE))
        if x0 <= x3 <= x1:
            return tuple(x2), x3


def generate_aab50785(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (ONE, FOUR))
        x1 = unifint(diff_lb, diff_ub, (THREE, SIX))
        x2, x3 = _sample_row_layout_aab50785(x0)
        x4 = unifint(
            diff_lb,
            diff_ub,
            (max(TEN, add(x1, FOUR)), min(18, add(x1, 13))),
        )
        x5 = subtract(subtract(x4, x1), FOUR)
        x6 = tuple(randint(ZERO, x5) for _ in range(x0))
        x7 = tuple(
            tuple(choice(NO_EIGHT_COLORS_AAB50785) for _ in range(x1))
            for _ in range(multiply(TWO, x0))
        )
        if equality(numcolors(x7), ONE):
            continue
        x8 = [
            [choice(NO_EIGHT_COLORS_AAB50785) for _ in range(x4)]
            for _ in range(x3)
        ]
        for x9, x10 in enumerate(x2):
            x11 = x6[x9]
            x12 = add(add(x11, x1), TWO)
            x13 = multiply(TWO, x9)
            for x14 in range(TWO):
                x15 = add(x10, x14)
                x8[x15][x11] = EIGHT
                x8[x15][increment(x11)] = EIGHT
                x8[x15][x12] = EIGHT
                x8[x15][increment(x12)] = EIGHT
                x16 = x7[add(x13, x14)]
                for x17, x18 in enumerate(x16):
                    x8[x15][add(add(x11, TWO), x17)] = x18
        x19 = tuple(tuple(x20) for x20 in x8)
        if verify_aab50785(x19) != x7:
            continue
        return {"input": x19, "output": x7}
