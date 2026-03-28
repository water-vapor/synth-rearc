from synth_rearc.core import *

from .verifier import verify_c61be7dc


BG_C61BE7DC = SEVEN
SEP_C61BE7DC = ZERO
FG_C61BE7DC = FIVE


def _oddify_c61be7dc(value: Integer, upper: Integer) -> Integer:
    if even(value):
        if value < upper:
            return increment(value)
        return decrement(value)
    return value


def _centered_row_segment_c61be7dc(
    row: Integer,
    center_col: Integer,
    length: Integer,
) -> Indices:
    if even(length):
        x0 = divide(length, TWO)
        x1 = connect((row, subtract(center_col, x0)), (row, decrement(center_col)))
        x2 = connect((row, increment(center_col)), (row, add(center_col, x0)))
        return combine(x1, x2)
    x0 = divide(decrement(length), TWO)
    return connect((row, subtract(center_col, x0)), (row, add(center_col, x0)))


def _centered_col_segment_c61be7dc(
    center_row: Integer,
    col: Integer,
    length: Integer,
) -> Indices:
    if even(length):
        x0 = divide(length, TWO)
        x1 = connect((subtract(center_row, x0), col), (decrement(center_row), col))
        x2 = connect((increment(center_row), col), (add(center_row, x0), col))
        return combine(x1, x2)
    x0 = divide(decrement(length), TWO)
    return connect((subtract(center_row, x0), col), (add(center_row, x0), col))


def _block_profile_c61be7dc(
    side: Integer,
    span: Integer,
) -> tuple[Integer, ...] | None:
    x0 = tuple(v for v in range(ONE, span + ONE, TWO))
    x1 = choice(x0)
    x2 = min(FOUR, divide(subtract(side, x1), double(x1)))
    if x2 < ONE:
        return None
    x3 = randint(ONE, x2)
    return tuple(repeat(x1, add(double(x3), ONE)))


def _diamond_profile_c61be7dc(
    side: Integer,
    span: Integer,
) -> tuple[Integer, ...] | None:
    x0 = list(range(THREE, span + ONE, TWO))
    if len(x0) == ZERO:
        return None
    shuffle(x0)
    for x1 in x0:
        x2 = min(FOUR, divide(decrement(x1), TWO))
        if x2 < ONE:
            continue
        x3 = randint(ONE, x2)
        x4 = tuple(subtract(x1, double(subtract(x3, x5))) for x5 in range(ZERO, x3))
        x5 = tuple(x4) + (x1,) + tuple(reversed(x4))
        if size(x5) > side:
            continue
        if sum(x5) > side:
            continue
        return x5
    return None


def _lobed_profile_c61be7dc(
    side: Integer,
    span: Integer,
) -> tuple[Integer, ...] | None:
    x0 = choice(tuple(v for v in range(ONE, min(THREE, span) + ONE, TWO)))
    x1 = min(FOUR, divide(subtract(side, ONE), TWO))
    if x1 < TWO:
        return None
    x2 = randint(TWO, x1)
    x3 = []
    x4 = x0
    for _ in range(x2):
        x5 = tuple(v for v in range(x4, min(span, add(x4, TWO)) + ONE))
        x4 = choice(x5)
        x3.append(x4)
    x6 = tuple(reversed(x3)) + (x0,) + tuple(x3)
    if sum(x6) > side:
        return None
    return x6


def _sample_profile_c61be7dc(
    side: Integer,
    span: Integer,
) -> tuple[Integer, ...]:
    x0 = (
        _diamond_profile_c61be7dc,
        _block_profile_c61be7dc,
        _lobed_profile_c61be7dc,
        _lobed_profile_c61be7dc,
    )
    while True:
        x1 = choice(x0)
        x2 = x1(side, span)
        if x2 is None:
            continue
        if sum(x2) < FIVE:
            continue
        return x2


def _profile_patch_vertical_c61be7dc(
    center: IntegerTuple,
    profile: tuple[Integer, ...],
) -> Indices:
    x0, x1 = center
    x2 = divide(decrement(size(profile)), TWO)
    x3 = set()
    for x4, x5 in enumerate(profile):
        x6 = add(subtract(x0, x2), x4)
        x7 = _centered_row_segment_c61be7dc(x6, x1, x5)
        x3 |= x7
    return frozenset(x3)


def _profile_patch_horizontal_c61be7dc(
    center: IntegerTuple,
    profile: tuple[Integer, ...],
) -> Indices:
    x0, x1 = center
    x2 = divide(decrement(size(profile)), TWO)
    x3 = set()
    for x4, x5 in enumerate(profile):
        x6 = add(subtract(x1, x2), x4)
        x7 = _centered_col_segment_c61be7dc(x0, x6, x5)
        x3 |= x7
    return frozenset(x3)


def _render_input_c61be7dc(
    side: Integer,
    orientation: str,
    gap: Integer,
    profile: tuple[Integer, ...],
) -> Grid:
    x0 = divide(side, TWO)
    x1 = (x0, x0)
    x2 = canvas(BG_C61BE7DC, (side, side))
    if orientation == "v":
        x3 = connect((ZERO, subtract(x0, gap)), (decrement(side), subtract(x0, gap)))
        x4 = connect((ZERO, add(x0, gap)), (decrement(side), add(x0, gap)))
        x5 = connect((x0, ZERO), (x0, decrement(side)))
        x6 = _profile_patch_vertical_c61be7dc(x1, profile)
    else:
        x3 = connect((subtract(x0, gap), ZERO), (subtract(x0, gap), decrement(side)))
        x4 = connect((add(x0, gap), ZERO), (add(x0, gap), decrement(side)))
        x5 = connect((ZERO, x0), (decrement(side), x0))
        x6 = _profile_patch_horizontal_c61be7dc(x1, profile)
    x7 = fill(x2, SEP_C61BE7DC, x3)
    x8 = fill(x7, SEP_C61BE7DC, x4)
    x9 = fill(x8, SEP_C61BE7DC, x5)
    return fill(x9, FG_C61BE7DC, x6)


def _render_output_c61be7dc(
    side: Integer,
    orientation: str,
    count: Integer,
) -> Grid:
    x0 = divide(side, TWO)
    x1 = canvas(BG_C61BE7DC, (side, side))
    x2 = divide(decrement(count), TWO)
    if orientation == "v":
        x3 = connect((ZERO, decrement(x0)), (decrement(side), decrement(x0)))
        x4 = connect((ZERO, increment(x0)), (decrement(side), increment(x0)))
        x5 = connect((x0, ZERO), (x0, decrement(side)))
        x6 = connect((subtract(x0, x2), x0), (add(x0, x2), x0))
    else:
        x3 = connect((decrement(x0), ZERO), (decrement(x0), decrement(side)))
        x4 = connect((increment(x0), ZERO), (increment(x0), decrement(side)))
        x5 = connect((ZERO, x0), (decrement(side), x0))
        x6 = connect((x0, subtract(x0, x2)), (x0, add(x0, x2)))
    x7 = fill(x1, SEP_C61BE7DC, x3)
    x8 = fill(x7, SEP_C61BE7DC, x4)
    x9 = fill(x8, SEP_C61BE7DC, x5)
    return fill(x9, FG_C61BE7DC, x6)


def generate_c61be7dc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _oddify_c61be7dc(unifint(diff_lb, diff_ub, (NINE, 29)), 29)
        x1 = choice(("v", "h"))
        x2 = divide(x0, TWO)
        x3 = min(SIX, subtract(x2, TWO))
        if x3 < TWO:
            continue
        x4 = unifint(diff_lb, diff_ub, (TWO, x3))
        x5 = subtract(double(x4), ONE)
        x6 = _sample_profile_c61be7dc(x0, x5)
        x7 = sum(x6)
        x8 = _render_input_c61be7dc(x0, x1, x4, x6)
        x9 = _render_output_c61be7dc(x0, x1, x7)
        if verify_c61be7dc(x8) != x9:
            continue
        return {"input": x8, "output": x9}
