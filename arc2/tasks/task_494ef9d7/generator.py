from arc2.core import *


NONZERO_COLORS_494EF9D7 = remove(FIVE, interval(ONE, TEN, ONE))
TARGET_SETS_494EF9D7 = (
    frozenset({FOUR, SEVEN}),
    frozenset({ONE, EIGHT}),
)
TARGET_PAIRS_494EF9D7 = (
    (FOUR, SEVEN),
    (SEVEN, FOUR),
    (ONE, EIGHT),
    (EIGHT, ONE),
)


def _pair_positions_494ef9d7(width: Integer) -> tuple[Integer, Integer]:
    x0 = randint(ZERO, width - THREE)
    x1 = randint(x0 + TWO, width - ONE)
    return x0, x1


def _paint_pair_494ef9d7(
    grid: Grid,
    row: Integer,
    left: Integer,
    right: Integer,
    left_color: Integer,
    right_color: Integer,
) -> Grid:
    x0 = fill(grid, left_color, frozenset({(row, left)}))
    x1 = fill(x0, right_color, frozenset({(row, right)}))
    return x1


def generate_494ef9d7(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (THREE, TEN))
        x1 = unifint(diff_lb, diff_ub, (FOUR, TEN))
        x2 = randint(ZERO, min(TWO, x0 - THREE))
        x3 = x0 - x2
        x4 = randint(ONE, min(FOUR, x3 - ONE))
        x5 = list(range(x0))
        shuffle(x5)
        x6 = tuple(x5[:x4])
        x7 = tuple(x5[x4:x3])
        x8 = tuple(choice(TARGET_PAIRS_494EF9D7) for _ in x6)
        x9 = sorted({x10 for x11 in x8 for x10 in x11})
        x12 = max(FOUR, len(x9) + ONE)
        x13 = randint(x12, EIGHT)
        x14 = [x15 for x15 in NONZERO_COLORS_494EF9D7 if x15 not in x9]
        shuffle(x14)
        x15 = tuple(x9) + tuple(x14[: x13 - len(x9)])
        gi = canvas(ZERO, (x0, x1))
        go = canvas(ZERO, (x0, x1))
        for x16, x17 in zip(x6, x8):
            x18, x19 = _pair_positions_494ef9d7(x1)
            gi = _paint_pair_494ef9d7(gi, x16, x18, x19, x17[ZERO], x17[ONE])
            go = _paint_pair_494ef9d7(go, x16, x18, increment(x18), x17[ZERO], x17[ONE])
        for x20 in x7:
            x21, x22 = _pair_positions_494ef9d7(x1)
            while True:
                x23, x24 = sample(x15, TWO)
                if not contained(frozenset({x23, x24}), TARGET_SETS_494EF9D7):
                    break
            gi = _paint_pair_494ef9d7(gi, x20, x21, x22, x23, x24)
            go = _paint_pair_494ef9d7(go, x20, x21, x22, x23, x24)
        return {"input": gi, "output": go}
