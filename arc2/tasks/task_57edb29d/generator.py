from __future__ import annotations

from arc2.core import *

from .helpers import render_panel_57edb29d
from .verifier import verify_57edb29d


NONZERO_COLORS_57edb29d = remove(ZERO, interval(ZERO, TEN, ONE))
BACKGROUND_COLOR_57edb29d = FOUR
MAX_PANEL_SIDE_57edb29d = 13


def _pair_neighbors_57edb29d(
    cell: IntegerTuple,
    limits: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    x0, x1 = cell
    x2, x3 = limits
    x4 = []
    for x5, x6 in ((NEG_ONE, ZERO), (ONE, ZERO), (ZERO, NEG_ONE), (ZERO, ONE)):
        x7 = x0 + x5
        x8 = x1 + x6
        if ONE <= x7 <= x2 and ONE <= x8 <= x3:
            x4.append((x7, x8))
    return tuple(x4)


def _pair_patch_57edb29d(
    diff_lb: float,
    diff_ub: float,
    limits: IntegerTuple,
) -> frozenset[IntegerTuple]:
    x0, x1 = limits
    x2 = x0 * x1
    x3 = unifint(diff_lb, diff_ub, (ONE, min(THREE, x2)))
    x4 = {(randint(ONE, x0), randint(ONE, x1))}
    while len(x4) < x3:
        x5 = []
        for x6 in tuple(x4):
            for x7 in _pair_neighbors_57edb29d(x6, limits):
                if x7 not in x4:
                    x5.append(x7)
        x4.add(choice(x5))
    return frozenset(x4)


def _output_dims_57edb29d(
    diff_lb: float,
    diff_ub: float,
    pairs: frozenset[IntegerTuple],
    decorated_count: Integer,
) -> IntegerTuple:
    x0 = maximum(apply(first, pairs))
    x1 = maximum(apply(last, pairs))
    x2 = max(FIVE, 2 * x0 + THREE)
    x3 = max(FIVE, 2 * x1 + THREE)
    if decorated_count == TWO and choice((T, F, F)):
        if choice((T, F)):
            x4 = unifint(diff_lb, diff_ub, (max(NINE, x2), MAX_PANEL_SIDE_57edb29d))
            x5 = unifint(diff_lb, diff_ub, (x3, min(12, MAX_PANEL_SIDE_57edb29d)))
            return (x4, x5)
        x6 = unifint(diff_lb, diff_ub, (x2, min(12, MAX_PANEL_SIDE_57edb29d)))
        x7 = unifint(diff_lb, diff_ub, (max(NINE, x3), MAX_PANEL_SIDE_57edb29d))
        return (x6, x7)
    x8 = unifint(diff_lb, diff_ub, (x2, min(12, MAX_PANEL_SIDE_57edb29d)))
    x9 = unifint(diff_lb, diff_ub, (x3, min(12, MAX_PANEL_SIDE_57edb29d)))
    return (x8, x9)


def _full_panel_dims_57edb29d(
    diff_lb: float,
    diff_ub: float,
    pairs: frozenset[IntegerTuple],
) -> IntegerTuple:
    x0 = maximum(apply(first, pairs))
    x1 = maximum(apply(last, pairs))
    x2 = max(FIVE, 2 * x0 + THREE)
    x3 = max(FIVE, 2 * x1 + THREE)
    x4 = unifint(diff_lb, diff_ub, (x2, MAX_PANEL_SIDE_57edb29d))
    x5 = unifint(diff_lb, diff_ub, (x3, MAX_PANEL_SIDE_57edb29d))
    return (x4, x5)


def _partial_panel_dims_57edb29d(
    diff_lb: float,
    diff_ub: float,
    pairs: frozenset[IntegerTuple],
) -> IntegerTuple:
    x0 = maximum(apply(first, pairs))
    x1 = maximum(apply(last, pairs))
    if x0 == ONE and x1 == ONE:
        return _full_panel_dims_57edb29d(diff_lb, diff_ub, pairs)
    while True:
        x2 = randint(ONE, x0)
        x3 = randint(ONE, x1)
        if x2 < x0 or x3 < x1:
            break
    if x2 < x0:
        x4 = choice((2 * x2 + ONE, 2 * x2 + TWO))
    else:
        x4 = unifint(diff_lb, diff_ub, (max(FIVE, 2 * x2 + THREE), MAX_PANEL_SIDE_57edb29d))
    if x3 < x1:
        x5 = choice((2 * x3 + ONE, 2 * x3 + TWO))
    else:
        x5 = unifint(diff_lb, diff_ub, (max(FIVE, 2 * x3 + THREE), MAX_PANEL_SIDE_57edb29d))
    return (x4, x5)


def _panel_density_ok_57edb29d(
    panel: Grid,
    marker: Integer,
) -> Boolean:
    x0 = colorcount(panel, marker)
    x1 = height(panel) * width(panel)
    return both(greater(x1, x0 * FOUR), greater(x0, ZERO))


def _layout_rows_57edb29d(
    panels: tuple[Grid, ...],
) -> Grid | None:
    x0 = list(panels)
    shuffle(x0)
    if len(x0) == THREE:
        x1 = choice(((ONE, TWO), (TWO, ONE)))
    else:
        x1 = (TWO, TWO)
    x2 = []
    x3 = ZERO
    for x4 in x1:
        x2.append(tuple(x0[x3:x3 + x4]))
        x3 += x4
    x5 = []
    x6 = []
    for x7 in x2:
        x8 = sum(width(x9) for x9 in x7) + (len(x7) - ONE)
        x10 = max(height(x11) for x11 in x7)
        x5.append(x8)
        x6.append(x10)
    x12 = sum(x6) + (len(x2) - ONE) + TWO
    x13 = max(x5) + TWO
    if x12 > 30 or x13 > 30:
        return None
    x14 = canvas(BACKGROUND_COLOR_57edb29d, (x12, x13))
    x15 = ONE
    for x16, x17 in enumerate(x2):
        x18 = ONE + randint(ZERO, x13 - TWO - x5[x16])
        for x19 in x17:
            x20 = x15 + randint(ZERO, x6[x16] - height(x19))
            x14 = paint(x14, shift(asobject(x19), (x20, x18)))
            x18 += width(x19) + ONE
        x15 += x6[x16] + ONE
    return x14


def generate_57edb29d(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((TWO, THREE))
        x1 = (choice((ONE, TWO, THREE)), choice((ONE, TWO, THREE)))
        x2 = _pair_patch_57edb29d(diff_lb, diff_ub, x1)
        x3 = _output_dims_57edb29d(diff_lb, diff_ub, x2, x0)
        x4 = tuple(x5 for x5 in NONZERO_COLORS_57edb29d if x5 != BACKGROUND_COLOR_57edb29d)
        x5 = choice(x4)
        x6 = [x7 for x7 in x4 if x7 != x5]
        shuffle(x6)
        x7 = x6[0]
        x8 = tuple(x6[1:1 + x0])
        if len(x8) != x0:
            continue
        x9 = render_panel_57edb29d(x7, x5, x3, x2)
        if not _panel_density_ok_57edb29d(x9, x5):
            continue
        x10 = [canvas(x7, x3)]
        x11 = render_panel_57edb29d(x8[0], x5, _full_panel_dims_57edb29d(diff_lb, diff_ub, x2), x2)
        if not _panel_density_ok_57edb29d(x11, x5):
            continue
        x10.append(x11)
        x12 = T
        for x13 in x8[1:]:
            x14 = render_panel_57edb29d(x13, x5, _partial_panel_dims_57edb29d(diff_lb, diff_ub, x2), x2)
            if not _panel_density_ok_57edb29d(x14, x5):
                x12 = F
                break
            x10.append(x14)
        if not x12:
            continue
        x15 = _layout_rows_57edb29d(tuple(x10))
        if x15 is None:
            continue
        if verify_57edb29d(x15) != x9:
            continue
        return {"input": x15, "output": x9}
