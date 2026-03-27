from arc2.core import *


PANEL_SHAPE_31d5ba1a = (THREE, FIVE)
UNIVERSE_31d5ba1a = frozenset((i, j) for i in range(THREE) for j in range(FIVE))

COUNT_CHOICES_31d5ba1a = (
    (TWO, THREE, FIVE, FIVE),
    (TWO, THREE, SIX, FOUR),
    (TWO, THREE, SEVEN, THREE),
    (TWO, FOUR, FOUR, FIVE),
    (TWO, FOUR, FIVE, FOUR),
    (TWO, FOUR, SIX, THREE),
    (TWO, FIVE, THREE, FIVE),
    (TWO, FIVE, FOUR, FOUR),
    (TWO, FIVE, FIVE, THREE),
    (THREE, THREE, FIVE, FOUR),
    (THREE, THREE, SIX, THREE),
    (THREE, FOUR, FOUR, FOUR),
    (THREE, FOUR, FIVE, THREE),
    (THREE, FOUR, SIX, TWO),
)


def _row_counts_31d5ba1a(
    patch: frozenset[IntegerTuple],
) -> tuple[Integer, ...]:
    return tuple(sum((i, j) in patch for j in range(FIVE)) for i in range(THREE))


def _col_counts_31d5ba1a(
    patch: frozenset[IntegerTuple],
) -> tuple[Integer, ...]:
    return tuple(sum((i, j) in patch for i in range(THREE)) for j in range(FIVE))


def _patch_profile_ok_31d5ba1a(
    patch: frozenset[IntegerTuple],
    lower: Integer,
    upper: Integer,
    max_empty_rows: Integer,
) -> Boolean:
    x0 = len(patch)
    x1 = _row_counts_31d5ba1a(patch)
    x2 = _col_counts_31d5ba1a(patch)
    if not (lower <= x0 <= upper):
        return F
    if x1.count(ZERO) > max_empty_rows:
        return F
    if max(x1) > FOUR:
        return F
    if sum(count > ZERO for count in x2) < FOUR:
        return F
    return T


def generate_31d5ba1a(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (ZERO, len(COUNT_CHOICES_31d5ba1a) - ONE))
        top_only_count, bottom_only_count, both_count, _ = COUNT_CHOICES_31d5ba1a[x0]
        for _ in range(80):
            x1 = frozenset(sample(tuple(UNIVERSE_31d5ba1a), both_count))
            x2 = difference(UNIVERSE_31d5ba1a, x1)
            x3 = frozenset(sample(tuple(x2), top_only_count))
            x4 = difference(x2, x3)
            x5 = frozenset(sample(tuple(x4), bottom_only_count))
            x6 = combine(x1, x3)
            x7 = combine(x1, x5)
            x8 = combine(x3, x5)
            if not _patch_profile_ok_31d5ba1a(x6, FIVE, NINE, ONE):
                continue
            if not _patch_profile_ok_31d5ba1a(x7, EIGHT, TEN, ZERO):
                continue
            if not _patch_profile_ok_31d5ba1a(x8, FIVE, SEVEN, ZERO):
                continue
            x9 = canvas(ZERO, PANEL_SHAPE_31d5ba1a)
            x10 = fill(x9, NINE, x6)
            x11 = fill(x9, FOUR, x7)
            go = fill(x9, SIX, x8)
            gi = vconcat(x10, x11)
            return {"input": gi, "output": go}
