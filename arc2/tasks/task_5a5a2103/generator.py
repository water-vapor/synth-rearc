from arc2.core import *

from .verifier import verify_5a5a2103


CELL_SIDE_5A5A2103 = FOUR
CELL_STRIDE_5A5A2103 = FIVE
GRID_COUNT_BOUNDS_5A5A2103 = (THREE, FIVE)
TEMPLATE_SIZE_BOUNDS_5A5A2103 = (FIVE, EIGHT)
MARKER_PATCH_5A5A2103 = frozenset({(ONE, ONE), (ONE, TWO), (TWO, ONE), (TWO, TWO)})
TEMPLATE_STEPS_5A5A2103 = (
    UP,
    DOWN,
    LEFT,
    RIGHT,
    NEG_UNITY,
    UP_RIGHT,
    DOWN_LEFT,
    UNITY,
)
AVAILABLE_COLORS_5A5A2103 = remove(ZERO, interval(ZERO, TEN, ONE))


def _cell_origin_5a5a2103(
    row: Integer,
    col: Integer,
) -> IntegerTuple:
    return astuple(multiply(row, CELL_STRIDE_5A5A2103), multiply(col, CELL_STRIDE_5A5A2103))


def _base_grid_5a5a2103(
    count: Integer,
    separator_color: Integer,
) -> Grid:
    x0 = subtract(multiply(count, CELL_STRIDE_5A5A2103), ONE)
    x1 = canvas(ZERO, astuple(x0, x0))
    x2 = interval(CELL_SIDE_5A5A2103, x0, CELL_STRIDE_5A5A2103)
    for x3 in x2:
        x1 = fill(x1, separator_color, hfrontier(toivec(x3)))
        x1 = fill(x1, separator_color, vfrontier(tojvec(x3)))
    return x1


def _random_template_5a5a2103(
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    x0 = unifint(diff_lb, diff_ub, TEMPLATE_SIZE_BOUNDS_5A5A2103)
    while True:
        x1 = {choice(tuple(product(interval(ZERO, CELL_SIDE_5A5A2103, ONE), interval(ZERO, CELL_SIDE_5A5A2103, ONE))))}
        while len(x1) < x0:
            x2 = set()
            for x3 in x1:
                for x4 in TEMPLATE_STEPS_5A5A2103:
                    x5 = add(x3, x4)
                    if 0 <= x5[ZERO] < CELL_SIDE_5A5A2103 and 0 <= x5[ONE] < CELL_SIDE_5A5A2103 and x5 not in x1:
                        x2.add(x5)
            if len(x2) == ZERO:
                break
            x1.add(choice(tuple(x2)))
        x6 = frozenset(x1)
        if len(x6) != x0:
            continue
        if height(x6) < THREE or width(x6) < THREE:
            continue
        if square(x6):
            continue
        return x6


def generate_5a5a2103(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, GRID_COUNT_BOUNDS_5A5A2103)
        x1 = choice(AVAILABLE_COLORS_5A5A2103)
        x2 = [x3 for x3 in AVAILABLE_COLORS_5A5A2103 if x3 != x1]
        shuffle(x2)
        x3 = tuple(x2[:x0])
        x4 = x2[x0]
        x5 = _random_template_5a5a2103(diff_lb, diff_ub)
        x6 = randint(ZERO, subtract(x0, ONE))
        x7 = randint(ONE, subtract(x0, ONE))
        x8 = _base_grid_5a5a2103(x0, x1)
        for x9, x10 in enumerate(x3):
            x11 = _cell_origin_5a5a2103(x9, ZERO)
            x12 = shift(MARKER_PATCH_5A5A2103, x11)
            x8 = fill(x8, x10, x12)
        x13 = _cell_origin_5a5a2103(x6, x7)
        x14 = shift(x5, x13)
        x15 = fill(x8, x4, x14)
        x16 = _base_grid_5a5a2103(x0, x1)
        for x17, x18 in enumerate(x3):
            for x19 in interval(ZERO, x0, ONE):
                x20 = _cell_origin_5a5a2103(x17, x19)
                x21 = shift(x5, x20)
                x16 = fill(x16, x18, x21)
        if verify_5a5a2103(x15) != x16:
            continue
        return {"input": x15, "output": x16}
