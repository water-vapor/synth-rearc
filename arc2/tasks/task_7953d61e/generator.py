from arc2.core import *


COUNT_PROFILES_7953d61e = (
    (THREE, FOUR, FOUR, FIVE),
    (THREE, THREE, FOUR, SIX),
    (TWO, THREE, FIVE, SIX),
    (TWO, THREE, FOUR, SEVEN),
    (ONE, THREE, SIX, SIX),
)

COLORS_7953d61e = (ONE, TWO, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)


def _assemble_7953d61e(gi: Grid) -> Grid:
    x0 = rot270(gi)
    x1 = rot180(gi)
    x2 = rot90(gi)
    x3 = hconcat(gi, x0)
    x4 = hconcat(x1, x2)
    return vconcat(x3, x4)


def generate_7953d61e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    rotfs = (identity, rot90, rot180, rot270)
    while True:
        colors = sample(COLORS_7953d61e, FOUR)
        profidx = unifint(diff_lb, diff_ub, (ZERO, len(COUNT_PROFILES_7953d61e) - ONE))
        counts = list(COUNT_PROFILES_7953d61e[profidx])
        shuffle(counts)
        cells = []
        for color_value, count in zip(colors, counts):
            cells.extend([color_value] * count)
        shuffle(cells)
        gi = tuple(tuple(cells[FOUR * i:FOUR * (i + ONE)]) for i in range(FOUR))
        gi = choice(rotfs)(gi)
        if gi == rot90(gi):
            continue
        if gi == rot180(gi):
            continue
        if gi == rot270(gi):
            continue
        go = _assemble_7953d61e(gi)
        return {"input": gi, "output": go}
