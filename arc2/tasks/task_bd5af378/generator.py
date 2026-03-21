from arc2.core import *


BD5AF378_COLORS = (ONE, THREE, FIVE, SIX, SEVEN, NINE)


def _make_example_bd5af378(
    dims: IntegerTuple,
    corner: IntegerTuple,
    border_color: Integer,
    interior_color: Integer,
) -> dict:
    x0 = astuple(dims[0] - ONE - corner[0], dims[1] - ONE - corner[1])
    x1 = sign(subtract(x0, corner))
    x2 = add(corner, x1)
    x3 = add(x2, x1)
    x4 = astuple(corner[0], dims[1] - ONE - corner[1])
    x5 = astuple(dims[0] - ONE - corner[0], corner[1])
    x6 = astuple(x2[0], dims[1] - ONE - corner[1])
    x7 = astuple(dims[0] - ONE - corner[0], x2[1])
    x8 = combine(connect(corner, x4), connect(corner, x5))
    x9 = combine(connect(x2, x6), connect(x2, x7))
    x10 = canvas(interior_color, dims)
    x11 = fill(x10, border_color, x8)
    x12 = asindices(x10)
    x13 = intersection(shoot(x3, x1), x12)
    x14 = canvas(EIGHT, dims)
    x15 = fill(x14, interior_color, x8)
    x16 = fill(x15, border_color, x9)
    x17 = fill(x16, EIGHT, initset(corner))
    x18 = fill(x17, EIGHT, initset(x2))
    x19 = fill(x18, interior_color, x13)
    return {"input": x11, "output": x19}


def generate_bd5af378(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (FIVE, TEN))
    x1 = unifint(diff_lb, diff_ub, (FIVE, TEN))
    x2 = astuple(x0, x1)
    x3 = choice((ZERO, x0 - ONE))
    x4 = choice((ZERO, x1 - ONE))
    x5 = astuple(x3, x4)
    x6 = sample(BD5AF378_COLORS, TWO)
    x7 = x6[0]
    x8 = x6[1]
    return _make_example_bd5af378(x2, x5, x7, x8)
