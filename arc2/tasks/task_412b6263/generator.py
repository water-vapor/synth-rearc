from arc2.core import *


RECT_HEIGHT_BOUNDS_412B6263 = (TWO, SEVEN)
RECT_WIDTH_BOUNDS_412B6263 = (TWO, FIVE)
GAP_BOUNDS_412B6263 = (ONE, THREE)


def _separator_row_412b6263(width_: Integer) -> Grid:
    x0 = canvas(ONE, (ONE, width_))
    x1 = fill(x0, SEVEN, initset(ORIGIN))
    x2 = decrement(width_)
    x3 = fill(x1, SEVEN, initset((ZERO, x2)))
    return x3


def _output_from_input_412b6263(grid: Grid) -> Grid:
    x0 = rot270(grid)
    x1 = height(x0)
    x2 = canvas(ONE, (x1, ONE))
    x3 = hconcat(x2, x0)
    x4 = hconcat(x3, x2)
    x5 = _separator_row_412b6263(width(x4))
    x6 = vconcat(x5, x4)
    x7 = vconcat(x6, x5)
    x8 = vconcat(x7, x4)
    x9 = vconcat(x8, x5)
    return x9


def generate_412b6263(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, RECT_HEIGHT_BOUNDS_412B6263)
        x1 = unifint(diff_lb, diff_ub, RECT_WIDTH_BOUNDS_412B6263)
        x2 = canvas(FIVE, (x0, x1))
        x3 = totuple(box(asindices(x2)))
        x4 = choice(x3)
        x5 = fill(x2, NINE, initset(x4))
        x6 = unifint(diff_lb, diff_ub, GAP_BOUNDS_412B6263)
        x7 = unifint(diff_lb, diff_ub, (ONE, add(x0, TWO)))
        x8 = add(x0, x7)
        x9 = add(add(x1, x1), x6)
        gi = canvas(SEVEN, (x8, x9))
        x10 = asobject(x5)
        x11 = paint(gi, x10)
        x12 = shift(x10, (x7, add(x1, x6)))
        gi = paint(x11, x12)
        go = _output_from_input_412b6263(gi)
        return {"input": gi, "output": go}
