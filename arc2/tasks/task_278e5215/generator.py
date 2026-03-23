from __future__ import annotations

from arc2.core import *

from .verifier import verify_278e5215


NONZERO_COLORS_278e5215 = remove(ZERO, interval(ZERO, TEN, ONE))
MASK_HEIGHT_BOUNDS_278e5215 = (FIVE, TEN)
MASK_WIDTH_BOUNDS_278e5215 = (FIVE, TEN)
TOTAL_HEIGHT_BOUNDS_278e5215 = (14, 20)
TOTAL_WIDTH_EXTRA_BOUNDS_278e5215 = (FOUR, NINE)
VERTICAL_GAP_BOUNDS_278e5215 = (ONE, FOUR)
MARGIN_BOUNDS_278e5215 = (ZERO, FOUR)


def _split_total_278e5215(
    total: Integer,
    parts: Integer,
) -> tuple[Integer, ...]:
    if parts == ONE:
        return (total,)
    x0 = sorted(sample(range(ONE, total), parts - ONE))
    x1 = []
    x2 = ZERO
    for x3 in x0 + [total]:
        x1.append(x3 - x2)
        x2 = x3
    return tuple(x1)


def _neighbors_278e5215(
    cell: IntegerTuple,
    dims: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    x0, x1 = cell
    x2, x3 = dims
    x4 = []
    for x5, x6 in ((NEG_ONE, ZERO), (ONE, ZERO), (ZERO, NEG_ONE), (ZERO, ONE)):
        x7 = x0 + x5
        x8 = x1 + x6
        if 0 <= x7 < x2 and 0 <= x8 < x3:
            x4.append((x7, x8))
    return tuple(x4)


def _connected_278e5215(
    cells: Indices,
    dims: IntegerTuple,
) -> Boolean:
    if len(cells) == ZERO:
        return F
    x0 = {next(iter(cells))}
    x1 = set()
    while x0:
        x2 = x0.pop()
        if x2 in x1:
            continue
        x1.add(x2)
        for x3 in _neighbors_278e5215(x2, dims):
            if x3 in cells and x3 not in x1:
                x0.add(x3)
    return len(x1) == len(cells)


def _coverage_ok_278e5215(
    cells: Indices,
    dims: IntegerTuple,
) -> Boolean:
    x0, x1 = dims
    x2 = [ZERO for _ in range(x0)]
    x3 = [ZERO for _ in range(x1)]
    for x4, x5 in cells:
        x2[x4] += ONE
        x3[x5] += ONE
    if any(x6 < TWO for x6 in x2):
        return F
    if any(x7 == ZERO for x7 in x3):
        return F
    return T


def _anchored_paths_278e5215(
    dims: IntegerTuple,
    anchor: IntegerTuple,
) -> Indices:
    x0, x1 = dims
    x2, x3 = anchor
    x4 = [None for _ in range(x1)]
    x4[x3] = x2
    for x5 in range(x3 - ONE, NEG_ONE, NEG_ONE):
        x6 = x4[x5 + ONE] + choice((NEG_ONE, ZERO, ZERO, ONE))
        x4[x5] = min(max(x6, ZERO), x0 - ONE)
    for x7 in range(x3 + ONE, x1):
        x8 = x4[x7 - ONE] + choice((NEG_ONE, ZERO, ZERO, ONE))
        x4[x7] = min(max(x8, ZERO), x0 - ONE)
    x9 = [None for _ in range(x0)]
    x9[x2] = x3
    for x10 in range(x2 - ONE, NEG_ONE, NEG_ONE):
        x11 = x9[x10 + ONE] + choice((NEG_ONE, ZERO, ZERO, ONE))
        x9[x10] = min(max(x11, ZERO), x1 - ONE)
    for x12 in range(x2 + ONE, x0):
        x13 = x9[x12 - ONE] + choice((NEG_ONE, ZERO, ZERO, ONE))
        x9[x12] = min(max(x13, ZERO), x1 - ONE)
    x14 = {(x4[x15], x15) for x15 in range(x1)}
    x15 = {(x16, x9[x16]) for x16 in range(x0)}
    return frozenset(x14 | x15)


def _mask_patch_278e5215(
    diff_lb: float,
    diff_ub: float,
    dims: IntegerTuple,
) -> Indices | None:
    x0, x1 = dims
    x2 = x0 * x1
    x3 = max(TWO * x0, (11 * x2 + 19) // 20)
    x4 = min(x2 - ONE, (18 * x2) // 25)
    if x3 > x4:
        return None
    x5 = unifint(diff_lb, diff_ub, (x3, x4))
    x6 = (randint(ZERO, x0 - ONE), randint(ZERO, x1 - ONE))
    x7 = _anchored_paths_278e5215(dims, x6)
    x8 = frozenset((i, j) for i in range(x0) for j in range(x1))
    x9 = set(x8 - x7)
    x10 = set(x8)
    x11 = list(x9)
    shuffle(x11)
    for x12 in x11:
        if len(x10) <= x5:
            break
        x13 = frozenset(x10 - {x12})
        if not _coverage_ok_278e5215(x13, dims):
            continue
        if not _connected_278e5215(x13, dims):
            continue
        x10.remove(x12)
    x14 = frozenset(x10)
    if len(x14) < x3 or len(x14) > x4:
        return None
    if len(x14) == x2:
        return None
    return x14


def _template_row_278e5215(
    diff_lb: float,
    diff_ub: float,
    width: Integer,
    bg: Integer,
) -> tuple[Integer, ...]:
    x0 = tuple(x1 for x1 in NONZERO_COLORS_278e5215 if x1 != bg)
    x1 = unifint(diff_lb, diff_ub, (THREE, min(FIVE, width)))
    x2 = tuple(sample(x0, x1))
    x3 = unifint(diff_lb, diff_ub, (x1, min(width, x1 + TWO)))
    x4 = list(x2)
    while len(x4) < x3:
        x4.append(choice(x2))
    while True:
        shuffle(x4)
        if all(x4[x5] != x4[x5 + ONE] for x5 in range(x3 - ONE)):
            break
    x5 = _split_total_278e5215(width, x3)
    x6 = []
    for x7, x8 in zip(x4, x5):
        x6.extend(repeat(x7, x8))
    return tuple(x6)


def _render_output_278e5215(
    mask: Grid,
    fg_row: tuple[Integer, ...],
    bg: Integer,
) -> Grid:
    x0 = vupscale((fg_row,), height(mask))
    x1 = ofcolor(mask, ZERO)
    return fill(x0, bg, x1)


def _build_input_278e5215(
    diff_lb: float,
    diff_ub: float,
    mask: Grid,
    template: Grid,
) -> Grid | None:
    x0 = height(mask)
    x1 = width(mask)
    x2 = choice((T, F))
    x3 = unifint(diff_lb, diff_ub, VERTICAL_GAP_BOUNDS_278e5215)
    x4 = unifint(diff_lb, diff_ub, MARGIN_BOUNDS_278e5215)
    x5 = unifint(diff_lb, diff_ub, MARGIN_BOUNDS_278e5215)
    x6 = x4 + x5 + x3 + x0 + THREE
    x7, x8 = TOTAL_HEIGHT_BOUNDS_278e5215
    if x6 < x7 or x6 > x8:
        return None
    x9 = x1 + unifint(diff_lb, diff_ub, TOTAL_WIDTH_EXTRA_BOUNDS_278e5215)
    x10 = randint(ZERO, x9 - x1)
    x11 = randint(ZERO, x9 - x1)
    if x2:
        x12 = x4
        x13 = x4 + THREE + x3
    else:
        x13 = x4
        x12 = x4 + x0 + x3
    x14 = canvas(ZERO, (x6, x9))
    x15 = shift(asobject(template), (x12, x10))
    x16 = shift(asobject(mask), (x13, x11))
    x17 = paint(x14, x15)
    return paint(x17, x16)


def generate_278e5215(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, MASK_HEIGHT_BOUNDS_278e5215)
        x1 = unifint(diff_lb, diff_ub, MASK_WIDTH_BOUNDS_278e5215)
        x2 = (x0, x1)
        x3 = _mask_patch_278e5215(diff_lb, diff_ub, x2)
        if x3 is None:
            continue
        x4 = fill(canvas(ZERO, x2), FIVE, x3)
        x5 = choice(NONZERO_COLORS_278e5215)
        x6 = _template_row_278e5215(diff_lb, diff_ub, x1, x5)
        x7 = repeat(x5, x1)
        x8 = (x6, x6, x7)
        x9 = _render_output_278e5215(x4, x6, x5)
        x10 = _build_input_278e5215(diff_lb, diff_ub, x4, x8)
        if x10 is None:
            continue
        if verify_278e5215(x10) != x9:
            continue
        return {"input": x10, "output": x9}
