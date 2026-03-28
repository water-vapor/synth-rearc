from synth_rearc.core import *


HORIZONTAL_LAYOUTS_0607CE86 = (
    (THREE, SIX, FOUR),
    (THREE, SIX, FOUR),
    (TWO, EIGHT, SIX),
)

VERTICAL_LAYOUTS_0607CE86 = (
    (FIVE, ONE, THREE),
    (FIVE, TWO, THREE),
    (FIVE, TWO, FOUR),
    (FOUR, TWO, FIVE),
)

VERTICAL_LAYOUTS_WIDE_0607CE86 = (
    (FIVE, TWO, THREE),
    (FIVE, TWO, FOUR),
)

ROW_TEMPLATES_0607CE86 = {
    FOUR: (
        (ZERO, ONE, TWO, THREE),
        (ZERO, ONE, TWO, TWO),
    ),
    FIVE: (
        (ZERO, ZERO, ZERO, ZERO, ONE),
        (ZERO, ONE, ONE, ONE, ONE),
        (ZERO, ONE, ONE, TWO, TWO),
        (ZERO, ONE, TWO, TWO, THREE),
    ),
}


def _segment_0607ce86(
    width_value: Integer,
    colors: Tuple,
) -> Tuple:
    x0 = sample(colors, THREE)
    x1, x2, x3 = x0
    if width_value == SIX:
        x4 = (
            (ZERO, x1, x1, x1, x1, x1),
            (ZERO, x1, x1, x1, x1, ZERO),
            (ZERO, x1, x1, x2, x2, x3),
            (ZERO, x1, x2, x2, x3, x3),
            (ZERO, x1, x2, x2, x3, ZERO),
            (ZERO, x1, x2, x3, x3, x3),
            (ZERO, x1, x2, x2, x1, x1),
        )
        return choice(x4)
    x4 = (
        (ZERO, ZERO, x1, x1, x1, x1, x1, x1),
        (ZERO, ZERO, x1, x1, x2, x2, x1, x1),
        (ZERO, ZERO, x1, x1, x1, x2, x2, x2),
        (ZERO, ZERO, x1, x2, x2, x1, x1, x2),
        (ZERO, ZERO, x1, x1, x2, x3, x3, x2),
    )
    return choice(x4)


def _has_smaller_period_0607ce86(
    motif: Grid,
    width_value: Integer,
) -> Boolean:
    for x0 in range(ONE, width_value):
        if width_value % x0 != ZERO:
            continue
        x1 = T
        for x2 in motif:
            if x2 != x2[:x0] * (width_value // x0):
                x1 = F
                break
        if x1:
            return T
    return F


def _motif_0607ce86(
    height_value: Integer,
    width_value: Integer,
    colors: Tuple,
) -> Grid:
    if width_value == EIGHT:
        x0 = sample(colors, THREE)
        x1, x2, x3 = x0
        x4 = (ZERO, ZERO, x1, x1, x1, x1, x1, x1)
        x5 = (ZERO, ZERO, x2, x2, x3, x3, x2, x2)
        x6 = (
            (x4, x5, x5, x5, x5),
            (x4, x4, x5, x5, x5),
        )
        return choice(x6)
    while True:
        x0 = choice(ROW_TEMPLATES_0607CE86[height_value])
        x1 = len(set(x0))
        x2 = []
        while len(x2) < x1:
            x3 = _segment_0607ce86(width_value, colors)
            if x3 in x2:
                continue
            x2.append(x3)
        x4 = tuple(x2[x5] for x5 in x0)
        x6 = {x7 for x8 in x4 for x7 in x8 if x7 != ZERO}
        if len(x6) < TWO:
            continue
        if _has_smaller_period_0607ce86(x4, width_value):
            continue
        return x4


def _build_output_0607ce86(
    motif: Grid,
    horizontal_copies: Integer,
    tail_width: Integer,
    gap_height: Integer,
    bottom_height: Integer,
) -> tuple[Grid, Tuple]:
    x0 = tuple(x1 * horizontal_copies + (ZERO,) * tail_width for x1 in motif)
    x1 = height(motif)
    x2 = (
        ONE,
        ONE + x1 + gap_height,
        ONE + (x1 + gap_height) * TWO,
    )
    x3 = x2[-ONE] + x1 + bottom_height
    x4 = [[ZERO] * 22 for _ in range(x3)]
    for x5 in x2:
        for x6, x7 in enumerate(x0):
            x4[x5 + x6] = list(x7)
    x8 = tuple(tuple(x9) for x9 in x4)
    return x8, x2


def _corrupt_input_0607ce86(
    go: Grid,
    motif: Grid,
    starts: Tuple,
    horizontal_copies: Integer,
    width_value: Integer,
    palette_values: Tuple,
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    x0 = [list(x1) for x1 in go]
    x1 = height(go)
    x2 = width(go)
    x3 = height(motif)
    x4 = horizontal_copies * width_value
    x5 = {
        (x6 + x7, x8)
        for x6 in starts
        for x7 in range(x3)
        for x8 in range(x4)
    }
    x6 = [(x7, x8) for x7 in range(x3) for x8 in range(width_value)]
    shuffle(x6)
    x7 = min(len(x6) - ONE, max(x3 + ONE, x3 * width_value // TWO))
    x8 = unifint(diff_lb, diff_ub, (x3 + ONE, x7))
    for x9, x10 in x6[:x8]:
        x11 = []
        for x12 in starts:
            for x13 in range(horizontal_copies):
                x11.append((x12 + x9, x13 * width_value + x10))
        x14, x15 = choice(x11)
        x16 = motif[x9][x10]
        x17 = tuple(x18 for x18 in palette_values if x18 != x16)
        x0[x14][x15] = choice(x17)
    x18 = [(x19, x20) for x19 in range(x1) for x20 in range(x2) if (x19, x20) not in x5]
    shuffle(x18)
    x19 = {}
    x20 = min(len(x18), x3 + 12)
    x21 = unifint(diff_lb, diff_ub, (x3 + TWO, x20))
    x22 = ZERO
    for x23, x24 in x18:
        if x22 == x21:
            break
        if x19.get(x23, ZERO) >= FOUR:
            continue
        x0[x23][x24] = choice(palette_values)
        x19[x23] = x19.get(x23, ZERO) + ONE
        x22 += ONE
    return tuple(tuple(x25) for x25 in x0)


def generate_0607ce86(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        x1, x2, x3 = choice(HORIZONTAL_LAYOUTS_0607CE86)
        x4, x5, x6 = choice(VERTICAL_LAYOUTS_WIDE_0607CE86 if x2 == EIGHT else VERTICAL_LAYOUTS_0607CE86)
        x7 = choice((THREE, THREE, FOUR))
        x8 = tuple(sample(x0, x7))
        x9 = _motif_0607ce86(x4, x2, x8)
        go, x10 = _build_output_0607ce86(x9, x1, x3, x5, x6)
        gi = _corrupt_input_0607ce86(go, x9, x10, x1, x2, x8, diff_lb, diff_ub)
        if gi == go:
            continue
        return {"input": gi, "output": go}
