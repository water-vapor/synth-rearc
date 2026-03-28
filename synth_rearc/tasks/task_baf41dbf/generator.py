from synth_rearc.core import *

from .verifier import verify_baf41dbf


INPUT_HEIGHT_BOUNDS_BAF41DBF = (THREE, SIX)
INPUT_WIDTH_BOUNDS_BAF41DBF = (THREE, SIX)
BOTTOM_GAP_BOUNDS_BAF41DBF = (TWO, EIGHT)
SIDE_GAP_BOUNDS_BAF41DBF = (TWO, SIX)
TOP_MARGIN_BOUNDS_BAF41DBF = (ONE, FOUR)
LEFT_MARGIN_BOUNDS_BAF41DBF = (ONE, FOUR)
BOTTOM_PAD_BAF41DBF = (ONE, FOUR)
RIGHT_PAD_BAF41DBF = (ONE, FOUR)
LEFT_ONLY_BAF41DBF = (T, F)
RIGHT_ONLY_BAF41DBF = (F, T)
BOTH_SIDES_BAF41DBF = (T, T)
SIDE_PATTERNS_BAF41DBF = (
    LEFT_ONLY_BAF41DBF,
    RIGHT_ONLY_BAF41DBF,
    BOTH_SIDES_BAF41DBF,
)


def _stroke_grid_baf41dbf(
    dims: Tuple,
    rows: Tuple,
    cols: Tuple,
    top: Integer,
    bottom: Integer,
    left: Integer,
    right: Integer,
    markers: Tuple,
) -> Grid:
    x0 = canvas(ZERO, dims)
    for x1 in rows:
        x2 = connect((x1, left), (x1, right))
        x0 = fill(x0, THREE, x2)
    for x3 in cols:
        x4 = connect((top, x3), (bottom, x3))
        x0 = fill(x0, THREE, x4)
    for x5 in markers:
        x0 = fill(x0, SIX, frozenset({x5}))
    return x0


def _choose_inner_row_baf41dbf(
    top: Integer,
    bottom: Integer,
) -> Tuple:
    x0 = bottom - top + ONE
    if x0 < FIVE or choice((T, F, F)) == F:
        return tuple()
    x1 = randint(top + ONE, bottom - ONE)
    return (x1,)


def _choose_inner_col_baf41dbf(
    left: Integer,
    right: Integer,
) -> Tuple:
    x0 = right - left + ONE
    if x0 < FIVE or choice((T, F, F)) == F:
        return tuple()
    x1 = randint(left + ONE, right - ONE)
    return (x1,)


def _right_marker_row_baf41dbf(
    top: Integer,
    input_bottom: Integer,
    output_bottom: Integer,
) -> Integer:
    if output_bottom > input_bottom and choice((T, F, F, F)) == T:
        return randint(input_bottom + ONE, output_bottom)
    return randint(top, input_bottom)


def generate_baf41dbf(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(SIDE_PATTERNS_BAF41DBF)
        x1 = x0[ZERO]
        x2 = x0[ONE]
        x3 = randint(*TOP_MARGIN_BOUNDS_BAF41DBF)
        x4 = randint(*LEFT_MARGIN_BOUNDS_BAF41DBF)
        x5 = unifint(diff_lb, diff_ub, INPUT_HEIGHT_BOUNDS_BAF41DBF)
        x6 = unifint(diff_lb, diff_ub, INPUT_WIDTH_BOUNDS_BAF41DBF)
        x7 = unifint(diff_lb, diff_ub, BOTTOM_GAP_BOUNDS_BAF41DBF)
        x8 = unifint(diff_lb, diff_ub, SIDE_GAP_BOUNDS_BAF41DBF) if x1 else ZERO
        x9 = unifint(diff_lb, diff_ub, SIDE_GAP_BOUNDS_BAF41DBF) if x2 else ZERO
        x10 = x3
        x11 = x10 + x5 - ONE + x7
        x12 = x4
        x13 = x12 + x6 - ONE + x8 + x9
        x14 = x11 - x7
        x15 = x12 + x8
        x16 = x13 - x9
        x17 = _choose_inner_row_baf41dbf(x10, x14)
        x18 = _choose_inner_col_baf41dbf(x15, x16)
        x19 = (x10,) + x17 + (x14,)
        x20 = (x15,) + x18 + (x16,)
        x21 = ((x11 + ONE, randint(x15, x16)),)
        if x1:
            x22 = randint(x10, x14)
            x21 = x21 + ((x22, x12 - ONE),)
        if x2:
            x23 = _right_marker_row_baf41dbf(x10, x14, x11)
            x21 = x21 + ((x23, x13 + ONE),)
        x24 = x11 + randint(*BOTTOM_PAD_BAF41DBF) + TWO
        x25 = x13 + randint(*RIGHT_PAD_BAF41DBF) + TWO
        x26 = (x24, x25)
        x27 = _stroke_grid_baf41dbf(x26, x19, x20, x10, x14, x15, x16, x21)
        x28 = (x10,) + x17 + (x11,)
        x29 = (x12,) + x18 + (x13,)
        x30 = _stroke_grid_baf41dbf(x26, x28, x29, x10, x11, x12, x13, x21)
        if x30 != verify_baf41dbf(x27):
            continue
        return {"input": x27, "output": x30}
