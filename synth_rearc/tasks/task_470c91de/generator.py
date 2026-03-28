from synth_rearc.core import *


GRID_SIZES_470C91DE = (TEN, TEN, 11, 11)
DIRECTIONS_470C91DE = (NEG_UNITY, UP_RIGHT, DOWN_LEFT, UNITY)
HEIGHT_OPTIONS_470C91DE = (TWO, THREE, THREE, FOUR, FOUR, FIVE, FIVE, SIX)
WIDTH_OPTIONS_470C91DE = (TWO, THREE, THREE, FOUR, FOUR, FIVE)
COLOR_OPTIONS_470C91DE = tuple(
    value for value in interval(ONE, TEN, ONE) if value not in (SEVEN, EIGHT)
)


def _rectangle_patch_470c91de(
    height_value: Integer,
    width_value: Integer,
    loc: IntegerTuple,
) -> Indices:
    x0 = canvas(ZERO, (height_value, width_value))
    x1 = asindices(x0)
    return shift(x1, loc)


def _orth_halo_470c91de(
    patch: Indices,
) -> Indices:
    x0 = mapply(dneighbors, patch)
    return combine(patch, x0)


def _corner_index_470c91de(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
    direction: IntegerTuple,
) -> IntegerTuple:
    x0 = first(direction)
    x1 = last(direction)
    x2 = branch(equality(x0, NEG_ONE), top, add(top, decrement(height_value)))
    x3 = branch(equality(x1, NEG_ONE), left, add(left, decrement(width_value)))
    return astuple(x2, x3)


def _biased_axis_470c91de(
    lower_bound: Integer,
    upper_bound: Integer,
) -> Integer:
    if lower_bound == upper_bound:
        return lower_bound
    return choice(
        (
            lower_bound,
            lower_bound,
            upper_bound,
            upper_bound,
            randint(lower_bound, upper_bound),
        )
    )


def generate_470c91de(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(GRID_SIZES_470C91DE)
        x1 = choice((TWO, THREE, THREE, FOUR if x0 == 11 else THREE))
        x2 = sample(COLOR_OPTIONS_470C91DE, x1)
        x3 = []
        for x4 in x2:
            x5 = FOUR if x1 == FOUR else SIX
            x6 = FOUR if x1 == FOUR else FIVE
            x7 = tuple(
                value for value in HEIGHT_OPTIONS_470C91DE if value <= x5 and value <= x0 - TWO
            )
            x8 = tuple(
                value for value in WIDTH_OPTIONS_470C91DE if value <= x6 and value <= x0 - TWO
            )
            x9 = choice(x7)
            x10 = choice(x8)
            x11 = choice(DIRECTIONS_470C91DE)
            x12 = multiply(x9, x10)
            x3.append((x12, x4, x9, x10, x11))
        x3 = sorted(x3, reverse=True)
        x13 = []
        x14 = []
        x15 = []
        x16 = T
        for _, x17, x18, x19, x20 in x3:
            x21 = first(x20)
            x22 = last(x20)
            x23 = max(ZERO, invert(x21))
            x24 = min(subtract(x0, x18), subtract(subtract(x0, x18), x21))
            x25 = max(ZERO, invert(x22))
            x26 = min(subtract(x0, x19), subtract(subtract(x0, x19), x22))
            if x23 > x24 or x25 > x26:
                x16 = F
                break
            x27 = F
            for _ in range(200):
                x28 = _biased_axis_470c91de(x23, x24)
                x29 = _biased_axis_470c91de(x25, x26)
                x30 = _rectangle_patch_470c91de(x18, x19, (x28, x29))
                x31 = shift(x30, x20)
                x32 = _orth_halo_470c91de(x30)
                x33 = _orth_halo_470c91de(x31)
                if any(x32 & x34 for x34 in x13):
                    continue
                if any(x33 & x35 for x35 in x14):
                    continue
                x36 = _corner_index_470c91de(x28, x29, x18, x19, x20)
                x15.append((x17, x30, x31, x36))
                x13.append(x32)
                x14.append(x33)
                x27 = T
                break
            if not x27:
                x16 = F
                break
        if not x16:
            continue
        x37 = canvas(SEVEN, (x0, x0))
        x38 = canvas(SEVEN, (x0, x0))
        for x39, x40, x41, x42 in x15:
            x37 = fill(x37, x39, x40)
            x37 = fill(x37, EIGHT, frozenset({x42}))
            x38 = fill(x38, x39, x41)
        return {"input": x37, "output": x38}
