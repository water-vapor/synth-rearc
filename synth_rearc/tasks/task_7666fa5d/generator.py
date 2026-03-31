from synth_rearc.core import *

from .verifier import verify_7666fa5d


GRID_SIDE_7666FA5D = 16
GRID_SHAPE_7666FA5D = (GRID_SIDE_7666FA5D, GRID_SIDE_7666FA5D)
MARKER_COLOR_CHOICES_7666FA5D = (THREE, FOUR, NINE)
GAP_CHOICES_7666FA5D = (FOUR, FOUR, FIVE, FIVE, SIX, SEVEN, EIGHT)
TEMPLATE_CHOICES_7666FA5D = ("single", "single", "double")


def _segment_patch_7666fa5d(
    sum_value: Integer,
    top_row: Integer,
    bottom_row: Integer,
) -> Indices:
    return frozenset((x0, subtract(sum_value, x0)) for x0 in range(top_row, add(bottom_row, ONE)))


def _cluster_fill_patch_7666fa5d(
    specs: tuple[tuple[Integer, Integer, Integer], ...],
) -> Indices:
    x0 = tuple(sorted(specs, key=lambda x1: x1[ZERO]))
    x1 = tuple(subtract(double(x2[ONE]), x2[ZERO]) for x2 in x0)
    x2 = tuple(subtract(double(x3[TWO]), x3[ZERO]) for x3 in x0)
    x3 = []
    x4 = []
    x5 = 99
    x6 = -99
    for x7, x8 in zip(x1, x2):
        x5 = min(x5, x7)
        x6 = max(x6, x8)
        x3.append(x5)
        x4.append(x6)
    x7 = [99] * len(x0)
    x8 = [-99] * len(x0)
    x9 = 99
    x10 = -99
    for x11 in range(decrement(len(x0)), NEG_ONE, NEG_ONE):
        x12 = x1[x11]
        x13 = x2[x11]
        x9 = min(x9, x12)
        x10 = max(x10, x13)
        x7[x11] = x9
        x8[x11] = x10
    x11 = set()
    for x12 in range(decrement(len(x0))):
        x13 = x0[x12][ZERO]
        x14 = x0[increment(x12)][ZERO]
        x15 = max(x3[x12], x7[increment(x12)])
        x16 = min(x4[x12], x8[increment(x12)])
        if x15 > x16:
            continue
        for x17 in range(increment(x13), increment(x14)):
            for x18 in range(x15, increment(x16)):
                if (x17 + x18) % TWO != ZERO:
                    continue
                x19 = divide(add(x17, x18), TWO)
                x20 = divide(subtract(x17, x18), TWO)
                if 0 <= x19 < GRID_SIDE_7666FA5D and 0 <= x20 < GRID_SIDE_7666FA5D:
                    x11.add((x19, x20))
    return frozenset(x11)


def _interval_chain_3_7666fa5d(
    row_lo: Integer,
    row_hi: Integer,
) -> tuple[tuple[Integer, Integer], ...] | None:
    if subtract(row_hi, row_lo) < FIVE:
        return None
    for _ in range(80):
        x0 = randint(row_lo, subtract(row_hi, FOUR))
        x1 = randint(add(x0, ONE), min(subtract(row_hi, TWO), add(x0, THREE)))
        x2 = randint(max(row_lo, subtract(x0, ONE)), min(subtract(row_hi, TWO), add(x0, TWO)))
        x3a = max(add(x2, TWO), x1)
        x3b = min(subtract(row_hi, ONE), add(x1, FOUR))
        if x3a > x3b:
            continue
        x3 = randint(x3a, x3b)
        x4a = max(x2, subtract(x3, THREE))
        x4b = min(subtract(row_hi, ONE), add(x2, THREE))
        if x4a > x4b:
            continue
        x4 = randint(x4a, x4b)
        x5a = max(add(x4, ONE), add(x3, ONE))
        if x5a > row_hi:
            continue
        x5 = randint(x5a, row_hi)
        x6 = ((x0, x1), (x2, x3), (x4, x5))
        if len({x7[ZERO] for x7 in x6}) == ONE:
            continue
        return x6
    return None


def _interval_chain_4_7666fa5d(
    row_lo: Integer,
    row_hi: Integer,
) -> tuple[tuple[Integer, Integer], ...] | None:
    if subtract(row_hi, row_lo) < EIGHT:
        return None
    for _ in range(120):
        x0 = randint(row_lo, subtract(row_hi, SEVEN))
        x1 = randint(add(x0, ONE), min(subtract(row_hi, FIVE), add(x0, FOUR)))
        x2 = randint(max(row_lo, subtract(x0, TWO)), min(subtract(row_hi, FOUR), add(x0, TWO)))
        x3a = max(add(x2, TWO), x1)
        x3b = min(subtract(row_hi, THREE), add(x1, FOUR))
        if x3a > x3b:
            continue
        x3 = randint(x3a, x3b)
        x4a = max(x2, subtract(x3, ONE))
        x4b = min(subtract(row_hi, TWO), add(x3, ONE))
        if x4a > x4b:
            continue
        x4 = randint(x4a, x4b)
        x5a = max(add(x4, THREE), x3)
        x5b = min(subtract(row_hi, ONE), add(x4, SEVEN))
        if x5a > x5b:
            continue
        x5 = randint(x5a, x5b)
        x6a = max(x4, subtract(x5, THREE))
        x6b = min(subtract(row_hi, ONE), add(x4, THREE))
        if x6a > x6b:
            continue
        x6 = randint(x6a, x6b)
        x7a = max(add(x6, TWO), subtract(x5, ONE))
        if x7a > row_hi:
            continue
        x7 = randint(x7a, row_hi)
        x8 = ((x0, x1), (x2, x3), (x4, x5), (x6, x7))
        if len({x9[ZERO] for x9 in x8}) == ONE:
            continue
        return x8
    return None


def _choose_sums_7666fa5d(
    intervals: tuple[tuple[Integer, Integer], ...],
) -> tuple[Integer, ...] | None:
    x0 = tuple(choice(GAP_CHOICES_7666FA5D) for _ in range(decrement(len(intervals))))
    x1 = [None] * len(intervals)
    x2 = sum(x0)
    x3 = max(intervals[ZERO][ONE], ZERO)
    x4 = subtract(add(intervals[ZERO][ZERO], decrement(GRID_SIDE_7666FA5D)), x2)
    if x3 > x4:
        return None
    x1[ZERO] = randint(x3, x4)
    for x5 in range(ONE, len(intervals)):
        x6 = sum(x0[x5:])
        x7 = max(intervals[x5][ONE], add(x1[decrement(x5)], x0[decrement(x5)]))
        x8 = subtract(add(intervals[x5][ZERO], decrement(GRID_SIDE_7666FA5D)), x6)
        if x7 > x8:
            return None
        x1[x5] = randint(x7, x8)
    return tuple(x1)


def _cluster_specs_7666fa5d(
    row_lo: Integer,
    row_hi: Integer,
    count: Integer,
) -> tuple[tuple[Integer, Integer, Integer], ...] | None:
    for _ in range(80):
        x0 = (
            _interval_chain_3_7666fa5d(row_lo, row_hi)
            if count == THREE
            else _interval_chain_4_7666fa5d(row_lo, row_hi)
        )
        if x0 is None:
            continue
        x1 = _choose_sums_7666fa5d(x0)
        if x1 is None:
            continue
        x2 = tuple((x3, x4[ZERO], x4[ONE]) for x3, x4 in zip(x1, x0))
        x3 = tuple(
            sorted(
                x2,
                key=lambda x4: (x4[ONE], x4[TWO], x4[ZERO]),
            )
        )
        x4 = x3[ZERO][TWO]
        x5 = T
        for x6 in x3[ONE:]:
            if x6[ONE] > add(x4, ONE):
                x5 = F
                break
            x4 = max(x4, x6[TWO])
        if flip(x5):
            continue
        return x2
    return None


def _paint_segments_7666fa5d(
    grid: Grid,
    specs: tuple[tuple[Integer, Integer, Integer], ...],
    color_value: Integer,
) -> Grid:
    x0 = grid
    for x1, x2, x3 in specs:
        x4 = _segment_patch_7666fa5d(x1, x2, x3)
        x0 = fill(x0, color_value, x4)
    return x0


def _layout_single_7666fa5d() -> tuple[tuple[tuple[Integer, Integer, Integer], ...], ...] | None:
    for _ in range(80):
        x0 = randint(ZERO, FOUR)
        x1 = randint(add(x0, TEN), decrement(GRID_SIDE_7666FA5D))
        x2 = _cluster_specs_7666fa5d(x0, x1, FOUR)
        if x2 is not None:
            return (x2,)
    return None


def _layout_double_7666fa5d() -> tuple[tuple[tuple[Integer, Integer, Integer], ...], ...] | None:
    for _ in range(80):
        x0 = randint(FOUR, SIX)
        x1 = randint(EIGHT, TEN)
        if x1 <= add(x0, ONE):
            continue
        x2 = _cluster_specs_7666fa5d(ZERO, x0, THREE)
        x3 = _cluster_specs_7666fa5d(x1, decrement(GRID_SIDE_7666FA5D), THREE)
        if both(x2 is not None, x3 is not None):
            return (x2, x3)
    return None


def generate_7666fa5d(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(TEMPLATE_CHOICES_7666FA5D)
        x1 = _layout_single_7666fa5d() if x0 == "single" else _layout_double_7666fa5d()
        if x1 is None:
            continue
        x2 = choice(MARKER_COLOR_CHOICES_7666FA5D)
        x3 = canvas(EIGHT, GRID_SHAPE_7666FA5D)
        x4 = frozenset()
        x5 = 0
        for x6 in x1:
            x3 = _paint_segments_7666fa5d(x3, x6, x2)
            x7 = _cluster_fill_patch_7666fa5d(x6)
            x4 = frozenset(x4 | x7)
            x5 += len(x7)
        if x5 < FOUR:
            continue
        x6 = underfill(x3, TWO, x4)
        x7 = colorfilter(objects(x6, T, T, T), TWO)
        if x0 == "single" and len(x7) != ONE:
            continue
        if x0 == "double" and len(x7) < TWO:
            continue
        if x6 == x3:
            continue
        if verify_7666fa5d(x3) != x6:
            continue
        return {"input": x3, "output": x6}
