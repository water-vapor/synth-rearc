from arc2.core import *


def _bar_patch_f3cdc58f(
    height_: Integer,
    col: Integer,
    count: Integer,
) -> Indices:
    x0 = interval(subtract(height_, count), height_, ONE)
    return product(x0, (col,))


def _render_output_f3cdc58f(
    counts: tuple[Integer, Integer, Integer, Integer],
) -> Grid:
    x0, x1, x2, x3 = counts
    x4 = canvas(ZERO, (TEN, TEN))
    x5 = fill(x4, ONE, _bar_patch_f3cdc58f(TEN, ZERO, x0))
    x6 = fill(x5, TWO, _bar_patch_f3cdc58f(TEN, ONE, x1))
    x7 = fill(x6, THREE, _bar_patch_f3cdc58f(TEN, TWO, x2))
    x8 = fill(x7, FOUR, _bar_patch_f3cdc58f(TEN, THREE, x3))
    return x8


def generate_f3cdc58f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = tuple(product(interval(ZERO, TEN, ONE), interval(ZERO, TEN, ONE)))
    while True:
        x1 = unifint(diff_lb, diff_ub, (TWO, EIGHT))
        x2 = unifint(diff_lb, diff_ub, (TWO, EIGHT))
        x3 = unifint(diff_lb, diff_ub, (TWO, EIGHT))
        x4 = unifint(diff_lb, diff_ub, (TWO, EIGHT))
        x5 = add(add(x1, x2), add(x3, x4))
        if x5 < 12 or x5 > 28:
            continue
        if len({x1, x2, x3, x4}) == ONE:
            continue
        x6 = tuple(sample(x0, x5))
        x7 = list(
            repeat(ONE, x1)
            + repeat(TWO, x2)
            + repeat(THREE, x3)
            + repeat(FOUR, x4)
        )
        shuffle(x7)
        x8 = canvas(ZERO, (TEN, TEN))
        for x9, x10 in zip(x6, x7):
            x8 = fill(x8, x10, initset(x9))
        x11 = _render_output_f3cdc58f((x1, x2, x3, x4))
        return {"input": x8, "output": x11}
