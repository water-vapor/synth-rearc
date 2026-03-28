from synth_rearc.core import *


def _pattern_to_indices_e41c6fd3(
    rows: tuple[str, ...],
) -> Indices:
    return frozenset(
        (i, j)
        for i, row in enumerate(rows)
        for j, value in enumerate(row)
        if value == "#"
    )


_TEMPLATES_E41C6FD3 = (
    _pattern_to_indices_e41c6fd3((
        "..##..",
        "#.##.#",
        "######",
        "##..##",
    )),
    _pattern_to_indices_e41c6fd3((
        ".##.",
        "####",
        "####",
        "####",
        "#..#",
    )),
    _pattern_to_indices_e41c6fd3((
        ".##.",
        "####",
        ".##.",
        "####",
    )),
    _pattern_to_indices_e41c6fd3((
        "#####",
        "..#..",
        ".###.",
        "#####",
        "..#..",
    )),
)


def generate_e41c6fd3(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = choice(_TEMPLATES_E41C6FD3)
    x1 = height(x0)
    x2 = width(x0)
    if x2 == SIX:
        x3 = choice((THREE, FOUR, FOUR))
    elif x2 == FIVE:
        x3 = choice((THREE, FOUR, FOUR))
    else:
        x3 = choice((THREE, FOUR, FOUR, FIVE))
    x4 = sample((ONE, TWO, THREE, FOUR, SIX), x3 - ONE)
    x5 = list(tuple(x4) + (EIGHT,))
    shuffle(x5)
    x6 = tuple(x5)
    while True:
        x7 = randint(ZERO, FOUR)
        x8 = tuple(choice((ZERO, ZERO, ONE, ONE, TWO, THREE)) for _ in range(x3 - ONE))
        x9 = randint(ZERO, THREE)
        x10 = x7 + x3 * x2 + sum(x8) + x9
        if 23 <= x10 <= 30:
            break
    x11 = []
    x12 = x7
    for x13 in range(x3):
        x11.append(x12)
        if x13 < x3 - ONE:
            x12 += x2 + x8[x13]
    x14 = tuple(x11)
    while True:
        x15 = unifint(diff_lb, diff_ub, (13, 17))
        x16 = tuple(range(ONE, x15 - x1 + ONE))
        x17 = tuple(sample(x16, x3))
        if max(x17) - min(x17) >= TWO:
            break
    x18 = x17[x6.index(EIGHT)]
    x19 = canvas(ZERO, (x15, x10))
    x20 = canvas(ZERO, (x15, x10))
    for x21, x22, x23 in zip(x6, x17, x14):
        x24 = shift(x0, (x22, x23))
        x25 = recolor(x21, x24)
        x19 = paint(x19, x25)
        x26 = shift(x0, (x18, x23))
        x27 = recolor(x21, x26)
        x20 = paint(x20, x27)
    return {"input": x19, "output": x20}
