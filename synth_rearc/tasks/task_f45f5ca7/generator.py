from synth_rearc.core import *


COLORS_F45F5CA7 = (TWO, THREE, FOUR, EIGHT)


def _target_column_f45f5ca7(
    color_value: Integer,
) -> Integer:
    return {
        EIGHT: ONE,
        TWO: TWO,
        FOUR: THREE,
        THREE: FOUR,
    }[color_value]


def _render_grids_f45f5ca7(
    rows: tuple[Integer, ...],
    colors: tuple[Integer, ...],
) -> tuple[Grid, Grid]:
    x0 = canvas(ZERO, (TEN, TEN))
    x1 = canvas(ZERO, (TEN, TEN))
    for x2, x3 in zip(rows, colors):
        x4 = initset(astuple(x2, ZERO))
        x0 = fill(x0, x3, x4)
        x5 = initset(astuple(x2, _target_column_f45f5ca7(x3)))
        x1 = fill(x1, x3, x5)
    return x0, x1


def generate_f45f5ca7(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (SEVEN, EIGHT))
    x1 = tuple(sorted(sample(interval(ZERO, TEN, ONE), x0)))
    x2 = {x3: ONE for x3 in COLORS_F45F5CA7}
    x4 = subtract(x0, FOUR)
    for _ in range(x4):
        x5 = tuple(x6 for x6, x7 in x2.items() if x7 < THREE)
        x6 = choice(x5)
        x2[x6] = increment(x2[x6])
    x7 = []
    for x8 in COLORS_F45F5CA7:
        x7.extend(repeat(x8, x2[x8]))
    shuffle(x7)
    x9, x10 = _render_grids_f45f5ca7(x1, tuple(x7))
    return {"input": x9, "output": x10}
