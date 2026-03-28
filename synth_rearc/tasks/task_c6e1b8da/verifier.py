from synth_rearc.core import *


def _row_map_c6e1b8da(patch: Patch) -> dict[Integer, tuple[Integer, ...]]:
    out = {}
    for i, j in toindices(patch):
        if i not in out:
            out[i] = []
        out[i].append(j)
    return {i: tuple(sorted(js)) for i, js in out.items()}


def _col_map_c6e1b8da(patch: Patch) -> dict[Integer, tuple[Integer, ...]]:
    out = {}
    for i, j in toindices(patch):
        if j not in out:
            out[j] = []
        out[j].append(i)
    return {j: tuple(sorted(iset)) for j, iset in out.items()}


def _bottom_tail_c6e1b8da(
    row_map: dict[Integer, tuple[Integer, ...]],
    r0: Integer,
    r1: Integer,
    c0: Integer,
    c1: Integer,
) -> Integer:
    col = None
    span = ZERO
    for i in range(r1, r0 - ONE, -ONE):
        cols = row_map[i]
        if len(cols) != ONE:
            break
        j = cols[ZERO]
        if col is None:
            col = j
        if j != col:
            break
        span += ONE
    if span == ZERO or span == r1 - r0 + ONE:
        return ZERO
    if not c0 < col < c1:
        return ZERO
    rr1 = r1 - span
    for i in range(r0, rr1 + ONE):
        cols = row_map[i]
        if not cols[ZERO] <= col <= cols[-ONE]:
            return ZERO
    return span


def _top_tail_c6e1b8da(
    row_map: dict[Integer, tuple[Integer, ...]],
    r0: Integer,
    r1: Integer,
    c0: Integer,
    c1: Integer,
) -> Integer:
    col = None
    span = ZERO
    for i in range(r0, r1 + ONE):
        cols = row_map[i]
        if len(cols) != ONE:
            break
        j = cols[ZERO]
        if col is None:
            col = j
        if j != col:
            break
        span += ONE
    if span == ZERO or span == r1 - r0 + ONE:
        return ZERO
    if not c0 < col < c1:
        return ZERO
    rr0 = r0 + span
    for i in range(rr0, r1 + ONE):
        cols = row_map[i]
        if not cols[ZERO] <= col <= cols[-ONE]:
            return ZERO
    return span


def _right_tail_c6e1b8da(
    col_map: dict[Integer, tuple[Integer, ...]],
    r0: Integer,
    r1: Integer,
    c0: Integer,
    c1: Integer,
) -> Integer:
    row = None
    span = ZERO
    for j in range(c1, c0 - ONE, -ONE):
        rows = col_map[j]
        if len(rows) != ONE:
            break
        i = rows[ZERO]
        if row is None:
            row = i
        if i != row:
            break
        span += ONE
    if span == ZERO or span == c1 - c0 + ONE:
        return ZERO
    if not r0 < row < r1:
        return ZERO
    cc1 = c1 - span
    for j in range(c0, cc1 + ONE):
        rows = col_map[j]
        if not rows[ZERO] <= row <= rows[-ONE]:
            return ZERO
    return span


def _left_tail_c6e1b8da(
    col_map: dict[Integer, tuple[Integer, ...]],
    r0: Integer,
    r1: Integer,
    c0: Integer,
    c1: Integer,
) -> Integer:
    row = None
    span = ZERO
    for j in range(c0, c1 + ONE):
        rows = col_map[j]
        if len(rows) != ONE:
            break
        i = rows[ZERO]
        if row is None:
            row = i
        if i != row:
            break
        span += ONE
    if span == ZERO or span == c1 - c0 + ONE:
        return ZERO
    if not r0 < row < r1:
        return ZERO
    cc0 = c0 + span
    for j in range(cc0, c1 + ONE):
        rows = col_map[j]
        if not rows[ZERO] <= row <= rows[-ONE]:
            return ZERO
    return span


def _describe_object_c6e1b8da(
    obj: Object,
) -> tuple[Integer, Object, IntegerTuple, IntegerTuple]:
    x0 = color(obj)
    x1 = uppermost(obj)
    x2 = lowermost(obj)
    x3 = leftmost(obj)
    x4 = rightmost(obj)
    x5 = _row_map_c6e1b8da(obj)
    x6 = _col_map_c6e1b8da(obj)
    x7 = _bottom_tail_c6e1b8da(x5, x1, x2, x3, x4)
    x8 = _top_tail_c6e1b8da(x5, x1, x2, x3, x4)
    x9 = _right_tail_c6e1b8da(x6, x1, x2, x3, x4)
    x10 = _left_tail_c6e1b8da(x6, x1, x2, x3, x4)
    x11 = (
        (x7, DOWN, (x1, x3), (x2 - x1 - x7 + ONE, x4 - x3 + ONE)),
        (x8, UP, (x1 + x8, x3), (x2 - x1 - x8 + ONE, x4 - x3 + ONE)),
        (x9, RIGHT, (x1, x3), (x2 - x1 + ONE, x4 - x3 - x9 + ONE)),
        (x10, LEFT, (x1, x3 + x10), (x2 - x1 + ONE, x4 - x3 - x10 + ONE)),
    )
    x12 = tuple(item for item in x11 if item[ZERO] > ZERO)
    if len(x12) == ZERO:
        x13 = (x1, x3)
        x14 = (x2 - x1 + ONE, x4 - x3 + ONE)
        x15 = ORIGIN
    else:
        x13 = max(x12, key=lambda item: item[ZERO])[TWO]
        x14 = max(x12, key=lambda item: item[ZERO])[THREE]
        x16 = max(x12, key=lambda item: item[ZERO])
        x15 = multiply(x16[ONE], x16[ZERO])
    x17 = interval(x13[ZERO], x13[ZERO] + x14[ZERO], ONE)
    x18 = interval(x13[ONE], x13[ONE] + x14[ONE], ONE)
    x19 = product(x17, x18)
    x20 = recolor(x0, x19)
    return (x0, x20, x15, x13)


def verify_c6e1b8da(I: Grid) -> Grid:
    x0 = fgpartition(I)
    x1 = tuple(_describe_object_c6e1b8da(obj) for obj in x0)
    x2 = tuple(item for item in x1 if item[TWO] == ORIGIN)
    x3 = tuple(item for item in x1 if item[TWO] != ORIGIN)
    x4 = tuple(sorted(x2, key=lambda item: (item[THREE][ZERO], item[THREE][ONE], item[ZERO])))
    x5 = tuple(sorted(x3, key=lambda item: (item[THREE][ZERO], item[THREE][ONE], item[ZERO])))
    x6 = canvas(ZERO, shape(I))
    for _, obj, _, _ in x4:
        x6 = paint(x6, obj)
    for _, obj, vec, _ in x5:
        x6 = paint(x6, shift(obj, vec))
    return x6
