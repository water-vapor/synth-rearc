from synth_rearc.core import *

from .verifier import verify_58e15b12


GRID_HEIGHT_BOUNDS_58E15B12 = (20, 28)
GRID_WIDTH_BOUNDS_58E15B12 = (17, 22)
PAIR_HEIGHT_CHOICES_58E15B12 = (ONE, TWO, TWO, THREE, THREE, FOUR, FOUR, FIVE)
PAIR_SPAN_CHOICES_58E15B12 = (TWO, TWO, THREE, THREE, FOUR, FOUR, FIVE)
REQUIRE_OVERLAP_CHOICES_58E15B12 = (T, T, F)


def _pair_indices_58e15b12(
    top: Integer,
    left: Integer,
    right: Integer,
    length: Integer,
) -> Indices:
    x0 = add(top, decrement(length))
    x1 = connect((top, left), (x0, left))
    x2 = connect((top, right), (x0, right))
    return combine(x1, x2)


def _trail_indices_58e15b12(
    top: Integer,
    left: Integer,
    right: Integer,
    length: Integer,
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = dims
    x2 = set()
    x3 = max(x0, x1)
    for x4 in range(x3):
        x5 = (ZERO,) if x4 == ZERO else (-ONE, ONE)
        for x6 in x5:
            x7 = top + (x6 * x4 * length)
            x8 = max(ZERO, x7)
            x9 = min(x0, x7 + length)
            if x8 >= x9:
                continue
            for x10 in (left - x4, right + x4):
                if ZERO <= x10 < x1:
                    x11 = connect((x8, x10), (decrement(x9), x10))
                    x2 |= set(x11)
    return frozenset(x2)


def _render_input_58e15b12(
    specs: tuple[tuple[Integer, Integer, Integer, Integer, Integer], ...],
    dims: IntegerTuple,
) -> Grid:
    x0 = canvas(ZERO, dims)
    for x1, x2, x3, x4, x5 in specs:
        x6 = _pair_indices_58e15b12(x2, x3, x4, x5)
        x0 = fill(x0, x1, x6)
    return x0


def _render_output_58e15b12(
    specs: tuple[tuple[Integer, Integer, Integer, Integer, Integer], ...],
    dims: IntegerTuple,
) -> Grid:
    x0 = {}
    for x1, x2, x3, x4, x5 in specs:
        x6 = _trail_indices_58e15b12(x2, x3, x4, x5, dims)
        for x7 in x6:
            x0.setdefault(x7, set()).add(x1)
    x1 = frozenset({x2 for x2, x3 in x0.items() if x3 == {THREE}})
    x2 = frozenset({x3 for x3, x4 in x0.items() if x4 == {EIGHT}})
    x3 = frozenset({x4 for x4, x5 in x0.items() if len(x5) > ONE})
    x4 = canvas(ZERO, dims)
    x5 = fill(x4, THREE, x1)
    x6 = fill(x5, EIGHT, x2)
    x7 = fill(x6, SIX, x3)
    return x7


def _sample_column_pairs_58e15b12(
    width_value: Integer,
) -> tuple[tuple[Integer, Integer], tuple[Integer, Integer]] | None:
    for _ in range(80):
        x0 = choice(PAIR_SPAN_CHOICES_58E15B12)
        x1 = choice(PAIR_SPAN_CHOICES_58E15B12)
        x2 = max(ONE, (width_value // TWO) - x0 - TWO)
        x3 = min(width_value - x1 - TWO, (width_value // TWO) + ONE)
        x4 = width_value - x1 - TWO
        if x2 < ONE or x3 > x4:
            continue
        x5 = randint(ONE, x2)
        x6 = randint(x3, x4)
        x7 = x5 + x0
        x8 = x6 + x1
        if x6 - x7 < TWO:
            continue
        return ((x5, x7), (x6, x8))
    return None


def _sample_row_pairs_58e15b12(
    height_value: Integer,
    upper_length: Integer,
    lower_length: Integer,
) -> tuple[Integer, Integer] | None:
    x0 = min(height_value - upper_length - lower_length - THREE, (height_value // THREE) + THREE)
    if x0 < ONE:
        return None
    for _ in range(80):
        x1 = randint(ONE, x0)
        x2 = height_value - lower_length - x1 - upper_length - ONE
        if x2 < TWO:
            continue
        x3 = randint(TWO, x2)
        x4 = x1 + upper_length + x3
        if x4 + lower_length >= height_value:
            continue
        return (x1, x4)
    return None


def generate_58e15b12(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, GRID_HEIGHT_BOUNDS_58E15B12)
        x1 = unifint(diff_lb, diff_ub, GRID_WIDTH_BOUNDS_58E15B12)
        x2 = _sample_column_pairs_58e15b12(x1)
        if x2 is None:
            continue
        x3 = choice(PAIR_HEIGHT_CHOICES_58E15B12)
        x4 = choice(PAIR_HEIGHT_CHOICES_58E15B12)
        x5 = choice(REQUIRE_OVERLAP_CHOICES_58E15B12)
        x6 = sample((THREE, EIGHT), TWO)
        x7 = choice((ZERO, ONE))
        x8 = _sample_row_pairs_58e15b12(x0, x3 if x7 == ZERO else x4, x4 if x7 == ZERO else x3)
        if x8 is None:
            continue
        x9, x10 = x2
        x11, x12 = x8
        if x7 == ZERO:
            x13 = (
                (x6[ZERO], x11, x9[ZERO], x9[ONE], x3),
                (x6[ONE], x12, x10[ZERO], x10[ONE], x4),
            )
        else:
            x13 = (
                (x6[ZERO], x12, x9[ZERO], x9[ONE], x3),
                (x6[ONE], x11, x10[ZERO], x10[ONE], x4),
            )
        x14 = _render_input_58e15b12(x13, (x0, x1))
        x15 = _render_output_58e15b12(x13, (x0, x1))
        x16 = colorcount(x15, SIX)
        if x5 and x16 == ZERO:
            continue
        if flip(x5) and x16 != ZERO:
            continue
        if greater(x16, TEN):
            continue
        if x14 == x15:
            continue
        if verify_58e15b12(x14) != x15:
            continue
        return {"input": x14, "output": x15}
