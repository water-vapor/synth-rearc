from arc2.core import *


CORNERS_22208ba4 = ("tl", "tr", "bl", "br")
COLORS_22208ba4 = remove(SEVEN, interval(ZERO, TEN, ONE))


def _corner_patch_22208ba4(
    h: int,
    w: int,
    size_value: int,
    corner: str,
) -> Indices:
    if corner == "tl":
        rows = interval(ZERO, size_value, ONE)
        cols = interval(ZERO, size_value, ONE)
    elif corner == "tr":
        rows = interval(ZERO, size_value, ONE)
        cols = interval(w - size_value, w, ONE)
    elif corner == "bl":
        rows = interval(h - size_value, h, ONE)
        cols = interval(ZERO, size_value, ONE)
    else:
        rows = interval(h - size_value, h, ONE)
        cols = interval(w - size_value, w, ONE)
    return product(rows, cols)


def _corner_offset_22208ba4(
    size_value: int,
    corner: str,
) -> tuple[int, int]:
    if corner == "tl":
        return (size_value, size_value)
    if corner == "tr":
        return (size_value, -size_value)
    if corner == "bl":
        return (-size_value, size_value)
    return (-size_value, -size_value)


def generate_22208ba4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (ONE, FOUR))
        x1 = max(THREE, x0)
        x2 = unifint(diff_lb, diff_ub, (x1, 30 - double(x0)))
        x3 = choice((T, F))
        x4 = branch(x3, x2, unifint(diff_lb, diff_ub, (x1, 30 - double(x0))))
        x5 = add(double(x0), x2)
        x6 = add(double(x0), x4)
        x7 = choice((TWO, TWO, THREE, THREE, FOUR))
        x8 = choice(COLORS_22208ba4)
        x9 = tuple(sample(CORNERS_22208ba4, x7))
        x10 = sample(remove(x8, COLORS_22208ba4), FOUR - x7)
        x11 = {}
        x12 = ZERO
        for x13 in CORNERS_22208ba4:
            if x13 in x9:
                x11[x13] = x8
            else:
                x11[x13] = x10[x12]
                x12 = increment(x12)
        x14 = canvas(SEVEN, (x5, x6))
        x15 = canvas(SEVEN, (x5, x6))
        for x16 in CORNERS_22208ba4:
            x17 = _corner_patch_22208ba4(x5, x6, x0, x16)
            x18 = x11[x16]
            x14 = fill(x14, x18, x17)
            x19 = branch(x16 in x9, shift(x17, _corner_offset_22208ba4(x0, x16)), x17)
            x15 = fill(x15, x18, x19)
        if mostcolor(x14) != SEVEN:
            continue
        return {"input": x14, "output": x15}
