from synth_rearc.core import *


GRID_SHAPE = (21, 21)
GRID_HEIGHT = 21
GRID_WIDTH = 21
GRAY_SECTION = TWO
TASK_COLORS = (ONE, TWO, THREE, FOUR, SIX, SEVEN, EIGHT)


def _pick_layout(top_pad: int, bottom_pad: int) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    options = []
    for x0 in range(FOUR):
        for x1 in range(FOUR):
            for x2 in range(FOUR):
                counts = (x0, x1, x2)
                if max(counts) == ZERO:
                    continue
                x3 = tuple(x4 for x4 in counts if x4 > ZERO)
                x5 = min(x3)
                x6 = tuple(x7 for x7, x8 in enumerate(counts) if x8 == x5)
                if len(x6) > ONE and GRAY_SECTION not in x6:
                    continue
                x9 = tuple(THREE if x10 == ZERO else 2 * x10 + ONE for x10 in counts)
                x11 = 17 - top_pad - bottom_pad - sum(x9)
                x12 = sum(ONE for x13 in x9 if x13 < SEVEN)
                if ZERO <= x11 <= x12:
                    options.append((counts, x9, x11))
    x12 = choice(options)
    x13, x14, x15 = x12
    x16 = [ZERO, ZERO, ZERO]
    x17 = tuple(x18 for x18, x19 in enumerate(x14) if x19 < SEVEN)
    if x15 > ZERO:
        for x18 in sample(x17, x15):
            x16[x18] = ONE
    x18 = tuple(x19 + x20 for x19, x20 in zip(x14, x16))
    return x13, x18


def _draw_motif(grid: Grid, top: int, left: int, color_: int, count: int) -> Grid:
    if count == ZERO:
        return grid
    x0 = grid
    for x1 in range(2 * count + ONE):
        x2 = top + x1
        if x1 % TWO == ZERO:
            x3 = frozenset({(x2, left), (x2, left + TWO)})
        else:
            x3 = connect((x2, left), (x2, left + TWO))
        x0 = fill(x0, color_, x3)
    return x0


def _marker_row(counts: tuple[int, int, int]) -> int:
    x0 = tuple(x1 for x1 in counts if x1 > ZERO)
    x2 = min(x0)
    x3 = tuple(x4 for x4, x5 in enumerate(counts) if x5 == x2)
    return GRAY_SECTION if GRAY_SECTION in x3 else x3[ZERO]


def _render_output(colors: tuple[int, int, int], counts: tuple[int, int, int]) -> Grid:
    x0 = canvas(ZERO, (THREE, FIVE))
    for x1, x2, x3 in zip(interval(ZERO, THREE, ONE), colors, counts):
        x4 = product(initset(x1), interval(ZERO, x3, ONE))
        x0 = fill(x0, x2, x4)
    x5 = product(interval(ZERO, THREE, ONE), initset(THREE))
    x6 = fill(x0, NINE, x5)
    x7 = fill(x6, FIVE, initset((_marker_row(counts), FOUR)))
    return x7


def _gray_column(start: int, count: int, gap: int) -> int:
    x0 = frozenset()
    if count > ZERO and gap == 2 * count + ONE:
        x0 = frozenset({start, start + ONE, start + TWO})
    x1 = tuple(x2 for x2 in interval(TWO, GRID_WIDTH - TWO, ONE) if x2 not in x0)
    return choice(x1)


def generate_a1aa0c1e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (ONE, TWO))
        x1 = unifint(diff_lb, diff_ub, (ZERO, ONE))
        x2, x3 = _pick_layout(x0, x1)
        x4 = tuple(sample(TASK_COLORS, THREE))
        x5 = tuple(choice(interval(TWO, GRID_WIDTH - THREE, ONE)) for _ in range(THREE))
        x6 = []
        x7 = x0
        for x8 in x3:
            x6.append(x7)
            x7 += x8 + ONE
        x6.append(GRID_HEIGHT - ONE - x1)
        x9 = tuple(x6)
        if x9[NEG_ONE] != x7:
            continue
        break

    x10 = canvas(ZERO, GRID_SHAPE)
    for x11, x12 in zip(x9, x4 + (NINE,)):
        x13 = connect((x11, ZERO), (x11, GRID_WIDTH - ONE))
        x10 = fill(x10, x12, x13)
    for x14, x15, x16, x17 in zip(x9[:THREE], x4, x2, x5):
        x10 = _draw_motif(x10, x14 + ONE, x17, x15, x16)
    x18 = x9[NEG_ONE] - ONE
    x19 = _gray_column(x5[GRAY_SECTION], x2[GRAY_SECTION], x3[GRAY_SECTION])
    x20 = fill(x10, FIVE, initset((x18, x19)))
    x21 = _render_output(x4, x2)
    return {"input": x20, "output": x21}
