from synth_rearc.core import *


BASE_TILE_17B866BD = (
    (ZERO, EIGHT, EIGHT, EIGHT, EIGHT),
    (EIGHT, EIGHT, ZERO, ZERO, EIGHT),
    (EIGHT, ZERO, ZERO, ZERO, ZERO),
    (EIGHT, ZERO, ZERO, ZERO, ZERO),
    (EIGHT, EIGHT, ZERO, ZERO, EIGHT),
)

MARKER_COLORS_17B866BD = (ONE, FOUR, SEVEN, EIGHT, EIGHT)


def _fill_patch_17b866bd() -> Indices:
    x0 = connect((ONE, TWO), (ONE, THREE))
    x1 = connect((TWO, ONE), (TWO, FOUR))
    x2 = connect((THREE, ONE), (THREE, FOUR))
    x3 = connect((FOUR, TWO), (FOUR, THREE))
    x4 = combine(x0, x1)
    x5 = combine(x2, x3)
    x6 = combine(x4, x5)
    return x6


def _span_17b866bd(
    diff_lb: float,
    diff_ub: float,
    length: int,
) -> tuple[int, ...]:
    x0 = decrement(length)
    x1 = unifint(diff_lb, diff_ub, (ZERO, x0))
    x2 = unifint(diff_lb, diff_ub, (x1, x0))
    return tuple(range(x1, increment(x2)))


def _base_grid_17b866bd(
    nrows: int,
    ncols: int,
) -> Grid:
    x0 = add(multiply(FIVE, nrows), ONE)
    x1 = add(multiply(FIVE, ncols), ONE)
    x2 = canvas(ZERO, (x0, x1))
    x3 = asobject(BASE_TILE_17B866BD)
    x4 = interval(ZERO, x0, FIVE)
    x5 = interval(ZERO, x1, FIVE)
    x6 = product(x4, x5)
    x7 = lbind(shift, x3)
    x8 = apply(x7, x6)
    x9 = merge(x8)
    x10 = paint(x2, x9)
    return x10


def generate_17b866bd(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (THREE, FOUR))
    x1 = unifint(diff_lb, diff_ub, (THREE, FOUR))
    x2 = _base_grid_17b866bd(x0, x1)
    x3 = _fill_patch_17b866bd()
    x4 = tuple(range(x0))
    x5 = tuple(range(x1))
    x6: dict[IntegerTuple, Integer] = {}
    x7 = unifint(diff_lb, diff_ub, (ONE, min(FOUR, add(x0, x1))))
    for _ in range(x7):
        x8 = choice(("point", "row", "col", "rect", "rect"))
        x9 = choice(MARKER_COLORS_17B866BD)
        if x8 == "point":
            x10 = (choice(x4),)
            x11 = (choice(x5),)
        elif x8 == "row":
            x10 = (choice(x4),)
            x11 = _span_17b866bd(diff_lb, diff_ub, x1)
        elif x8 == "col":
            x10 = _span_17b866bd(diff_lb, diff_ub, x0)
            x11 = (choice(x5),)
        else:
            x10 = _span_17b866bd(diff_lb, diff_ub, x0)
            x11 = _span_17b866bd(diff_lb, diff_ub, x1)
        for x12 in x10:
            for x13 in x11:
                x14 = (multiply(FIVE, x12), multiply(FIVE, x13))
                x6[x14] = x9
    x15 = tuple((multiply(FIVE, i), multiply(FIVE, j)) for i in x4 for j in x5)
    x16 = tuple(x17 for x17 in x15 if x17 not in x6)
    x18 = branch(len(x16) == ZERO, ZERO, unifint(diff_lb, diff_ub, (ZERO, min(TWO, len(x16)))))
    if x18 > ZERO:
        for x19 in sample(x16, x18):
            x6[x19] = choice(MARKER_COLORS_17B866BD)
    if len(x6) == ZERO:
        x20 = (multiply(FIVE, choice(x4)), multiply(FIVE, choice(x5)))
        x6[x20] = choice(MARKER_COLORS_17B866BD)
    x21 = x2
    x22 = x2
    for x23, x24 in x6.items():
        x21 = fill(x21, x24, initset(x23))
        x25 = shift(x3, x23)
        x22 = fill(x22, x24, x25)
    return {"input": x21, "output": x22}
