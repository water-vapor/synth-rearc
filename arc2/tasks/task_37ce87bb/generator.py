from arc2.core import *


def _render_columns_37ce87bb(
    height_value: Integer,
    columns: tuple[tuple[Integer, Integer], ...],
) -> Grid:
    x0 = add(THREE, multiply(TWO, len(columns)))
    x1 = canvas(SEVEN, (height_value, x0))
    x2 = x1
    for x3, (x4, x5) in enumerate(columns):
        x6 = add(ONE, multiply(TWO, x3))
        x7 = subtract(height_value, x5)
        x8 = interval(x7, height_value, ONE)
        x9 = product(x8, initset(x6))
        x2 = fill(x2, x4, x9)
    return x2


def generate_37ce87bb(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (SIX, 12))
        x1 = unifint(diff_lb, diff_ub, (TWO, SEVEN))
        x2 = []
        x3 = ZERO
        x4 = ZERO
        for x5 in range(x1):
            x6 = unifint(diff_lb, diff_ub, (ONE, subtract(x0, ONE)))
            x7 = EIGHT if x5 == ZERO else choice((EIGHT, EIGHT, TWO))
            x2.append((x7, x6))
            if x7 == EIGHT:
                x3 = add(x3, x6)
            else:
                x4 = add(x4, x6)
        x8 = subtract(x3, x4)
        if x8 < ONE or x8 >= x0:
            continue
        x9 = tuple(x2)
        if x1 > TWO and size(dedupe(x9)) == ONE:
            continue
        gi = _render_columns_37ce87bb(x0, x9)
        x10 = subtract(width(gi), ONE)
        x11 = decrement(x10)
        x12 = interval(subtract(x0, x8), x0, ONE)
        x13 = product(x12, initset(x11))
        go = fill(gi, FIVE, x13)
        return {"input": gi, "output": go}
