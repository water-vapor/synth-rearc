from arc2.core import *


GRID_SHAPE_AA300DC3 = (TEN, TEN)
INTERIOR_RANGE_AA300DC3 = tuple(range(ONE, NINE))
BACKGROUND_AA300DC3 = FIVE
FOREGROUND_AA300DC3 = ZERO
MARKER_AA300DC3 = EIGHT
WIDTH_TEMPLATES_AA300DC3 = (
    (FIVE, SIX, EIGHT, SEVEN, SIX, EIGHT, SIX, TWO),
    (FOUR, SIX, EIGHT, SEVEN, FIVE, EIGHT, SIX, THREE),
    (THREE, FOUR, SEVEN, SEVEN, EIGHT, FOUR, FOUR, TWO),
    (FIVE, SIX, FIVE, SEVEN, SEVEN, SIX, SIX, THREE),
    (FOUR, FIVE, SEVEN, EIGHT, SEVEN, SIX, FIVE, THREE),
    (THREE, FIVE, SIX, SEVEN, SEVEN, SIX, FIVE, TWO),
)


def _diagonal_runs_aa300dc3(
    cells: Indices,
    anti: Boolean,
) -> tuple[Indices, ...]:
    if len(cells) == ZERO:
        return tuple()
    x0: dict[Integer, list[IntegerTuple]] = dict()
    for x1 in cells:
        x2, x3 = x1
        x4 = x2 + x3 if anti else x2 - x3
        if x4 not in x0:
            x0[x4] = []
        x0[x4].append(x1)
    x5 = tuple()
    for x6 in sorted(x0):
        x7 = sorted(x0[x6])
        x8 = [x7[ZERO]]
        for x9, x10 in x7[ONE:]:
            x11, x12 = x8[-ONE]
            x13 = (x11 + ONE, x12 - ONE) if anti else (x11 + ONE, x12 + ONE)
            if (x9, x10) == x13:
                x8.append((x9, x10))
                continue
            x5 = x5 + (frozenset(x8),)
            x8 = [(x9, x10)]
        x5 = x5 + (frozenset(x8),)
    return x5


def _run_sort_key_aa300dc3(
    run: Indices,
    cells: Indices,
    anti: Boolean,
) -> tuple[Integer, Integer, IntegerTuple]:
    x0 = uppermost(cells)
    x1 = lowermost(cells)
    x2 = leftmost(cells)
    x3 = rightmost(cells)
    x4, x5 = first(sorted(run))
    x6 = x4 + x5 if anti else x4 - x5
    x7 = x0 + x1 + x2 + x3 if anti else x0 + x1 - x2 - x3
    x8 = abs(double(x6) - x7)
    return (x8, x6, ulcorner(run))


def _best_diagonal_aa300dc3(
    cells: Indices,
) -> Indices:
    x0 = _diagonal_runs_aa300dc3(cells, F)
    x1 = _diagonal_runs_aa300dc3(cells, T)
    x2 = valmax(x0, size)
    x3 = valmax(x1, size)
    x4 = tuple(x5 for x5 in x0 if size(x5) == x2)
    x5 = tuple(x6 for x6 in x1 if size(x6) == x3)
    x6 = first(sorted(x4, key=lambda x7: _run_sort_key_aa300dc3(x7, cells, F)))
    x7 = first(sorted(x5, key=lambda x8: _run_sort_key_aa300dc3(x8, cells, T)))
    x8 = _run_sort_key_aa300dc3(x6, cells, F)
    x9 = _run_sort_key_aa300dc3(x7, cells, T)
    if x2 > x3:
        return x6
    if x3 > x2:
        return x7
    return x6 if x8 <= x9 else x7


def _connected_aa300dc3(
    cells: Indices,
) -> Boolean:
    if len(cells) == ZERO:
        return False
    x0 = first(cells)
    x1 = {x0}
    x2 = [x0]
    x3 = set(cells)
    while len(x2) > ZERO:
        x4 = x2.pop()
        for x5 in dneighbors(x4):
            if x5 not in x3 or x5 in x1:
                continue
            x1.add(x5)
            x2.append(x5)
    return len(x1) == len(x3)


def _diagonal_line_aa300dc3(
    anti: Boolean,
    start_col: Integer,
) -> Indices:
    x0 = set()
    x1 = ONE
    x2 = start_col
    x3 = NEG_ONE if anti else ONE
    while x1 <= EIGHT and ONE <= x2 <= EIGHT:
        x0.add((x1, x2))
        x1 += ONE
        x2 += x3
    return frozenset(x0)


def _row_centers_aa300dc3(
    anti: Boolean,
    start_col: Integer,
) -> tuple[Integer, ...]:
    x0 = []
    x1 = start_col
    x2 = NEG_ONE if anti else ONE
    for _ in INTERIOR_RANGE_AA300DC3:
        x0.append(max(ONE, min(EIGHT, x1)))
        x1 += x2
    return tuple(x0)


def _interval_aa300dc3(
    center: Integer,
    width_value: Integer,
    left_weight: Integer,
) -> tuple[Integer, Integer]:
    x0 = center - ONE
    x1 = EIGHT - center
    x2 = width_value - ONE
    x3 = divide(add(multiply(x2, left_weight), THREE), SEVEN)
    x4 = min(x0, max(ZERO, x3 + choice((NEG_ONE, ZERO, ONE))))
    x5 = x2 - x4
    if x5 > x1:
        x6 = x5 - x1
        x5 = x1
        x4 = min(x0, x4 + x6)
    if x4 > x0:
        x6 = x4 - x0
        x4 = x0
        x5 = min(x1, x5 + x6)
    return (center - x4, center + x5)


def _build_band_aa300dc3(
    anti: Boolean,
    start_col: Integer,
    widths: tuple[Integer, ...],
) -> Indices:
    x0 = _row_centers_aa300dc3(anti, start_col)
    x1 = set()
    for x2, x3 in enumerate(widths, start=ONE):
        x4 = x0[x2 - ONE]
        x5 = EIGHT - x2 if anti else x2 - ONE
        x6, x7 = _interval_aa300dc3(x4, x3, x5)
        for x8 in range(x6, x7 + ONE):
            x1.add((x2, x8))
    return frozenset(x1)


def _notch_candidates_aa300dc3(
    cells: Indices,
    line: Indices,
) -> tuple[Indices, ...]:
    x0 = []
    for x1 in INTERIOR_RANGE_AA300DC3:
        x2 = sorted(x3[ONE] for x3 in cells if x3[ZERO] == x1)
        if len(x2) < FOUR:
            continue
        x3 = x2[ZERO]
        x4 = [x3]
        x5 = []
        for x6 in x2[ONE:]:
            if x6 == x4[-ONE] + ONE:
                x4.append(x6)
                continue
            x5.append(tuple(x4))
            x4 = [x6]
        x5.append(tuple(x4))
        for x6 in x5:
            if len(x6) < FOUR:
                continue
            for x7 in (ONE, TWO):
                for x8 in range(ONE, len(x6) - x7):
                    x9 = frozenset((x1, x10) for x10 in x6[x8:x8 + x7])
                    if len(intersection(x9, line)) > ZERO:
                        continue
                    x0.append(x9)
    return tuple(x0)


def _carve_notches_aa300dc3(
    cells: Indices,
    line: Indices,
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    x0 = set(cells)
    x1 = unifint(diff_lb, diff_ub, (ONE, FOUR))
    for _ in range(x1):
        x2 = _notch_candidates_aa300dc3(frozenset(x0), line)
        if len(x2) == ZERO:
            break
        x3 = choice(x2)
        x4 = frozenset(x0 - set(x3))
        if not _connected_aa300dc3(x4):
            continue
        if uppermost(x4) != ONE or lowermost(x4) != EIGHT:
            continue
        if leftmost(x4) != ONE or rightmost(x4) != EIGHT:
            continue
        if any(len(tuple(x5 for x5 in x4 if x5[ZERO] == x6)) == ZERO for x6 in INTERIOR_RANGE_AA300DC3):
            continue
        x0 = set(x4)
    return frozenset(x0)


def _sample_widths_aa300dc3(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, ...]:
    x0 = choice(WIDTH_TEMPLATES_AA300DC3)
    x1 = []
    for x2, x3 in enumerate(x0):
        x4 = x3 + choice((NEG_ONE, ZERO, ONE))
        x5 = max(TWO, min(EIGHT, x4))
        if x2 == ZERO:
            x5 = max(THREE, x5)
        if x2 == len(x0) - ONE:
            x5 = max(TWO, min(FOUR, x5))
        x1.append(x5)
    if choice((T, F)):
        x2 = unifint(diff_lb, diff_ub, (THREE, SIX))
        x1[x2] = min(EIGHT, x1[x2] + ONE)
    return tuple(x1)


def generate_aa300dc3(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    for _ in range(900):
        x0 = choice((F, F, F, T, T))
        x1 = choice((ONE, TWO, THREE)) if not x0 else choice((SIX, SEVEN, EIGHT))
        x2 = _diagonal_line_aa300dc3(x0, x1)
        x3 = _sample_widths_aa300dc3(diff_lb, diff_ub)
        x4 = _build_band_aa300dc3(x0, x1, x3)
        x5 = frozenset(set(x4) | set(x2))
        if not _connected_aa300dc3(x5):
            continue
        x6 = _carve_notches_aa300dc3(x5, x2, diff_lb, diff_ub)
        if not _connected_aa300dc3(x6):
            continue
        if uppermost(x6) != ONE or lowermost(x6) != EIGHT:
            continue
        if leftmost(x6) != ONE or rightmost(x6) != EIGHT:
            continue
        if size(x6) < 36 or size(x6) > 50:
            continue
        if _best_diagonal_aa300dc3(x6) != x2:
            continue
        x7 = canvas(BACKGROUND_AA300DC3, GRID_SHAPE_AA300DC3)
        x8 = fill(x7, FOREGROUND_AA300DC3, x6)
        x9 = fill(x8, MARKER_AA300DC3, x2)
        if x8 == x9:
            continue
        return {"input": x8, "output": x9}
    raise ValueError("failed to generate aa300dc3 example")
