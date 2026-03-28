from synth_rearc.core import *


WORK_SHAPE_516B51B7 = (24, 24)
RECT_COUNT_BOUNDS_516B51B7 = (2, 4)
RECT_BOUNDS_516B51B7 = (3, 10)
LARGE_RECT_BOUNDS_516B51B7 = (5, 10)
MARGIN_BOUNDS_516B51B7 = (0, 3)
MAX_LAYOUT_TRIES_516B51B7 = 200
GRID_TRANSFORMS_516B51B7 = (identity, rot90, rot180, rot270, hmirror, vmirror)


def _rectangle_patch_516b51b7(
    top: int,
    left: int,
    height_value: int,
    width_value: int,
) -> Indices:
    x0 = interval(top, top + height_value, ONE)
    x1 = interval(left, left + width_value, ONE)
    x2 = product(x0, x1)
    return x2


def _clip_patch_516b51b7(
    patch: Indices,
    shape_value: tuple[int, int],
) -> Indices:
    x0, x1 = shape_value
    x2 = frozenset((i, j) for i, j in patch if 0 <= i < x0 and 0 <= j < x1)
    return x2


def _paint_layered_rectangle_516b51b7(
    grid: Grid,
    top: int,
    left: int,
    height_value: int,
    width_value: int,
) -> Grid:
    x0 = grid
    x1 = (min(height_value, width_value) - ONE) // TWO
    for x2 in range(x1 + ONE):
        x3 = top + x2
        x4 = left + x2
        x5 = height_value - TWO * x2
        x6 = width_value - TWO * x2
        x7 = _rectangle_patch_516b51b7(x3, x4, x5, x6)
        if x2 == ZERO:
            x8 = ONE
        elif x2 % TWO == ONE:
            x8 = TWO
        else:
            x8 = THREE
        x0 = fill(x0, x8, x7)
    return x0


def _sample_layout_516b51b7(
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[tuple[int, int, int, int], ...], tuple[int, int]]:
    x0, x1 = WORK_SHAPE_516B51B7
    x2 = unifint(diff_lb, diff_ub, RECT_COUNT_BOUNDS_516B51B7)
    x3 = randint(ZERO, x2 - ONE)
    x4 = []
    x5 = frozenset()
    for x6 in range(x2):
        if x6 == x3:
            x7 = LARGE_RECT_BOUNDS_516B51B7
        else:
            x7 = RECT_BOUNDS_516B51B7
        x8 = F
        for _ in range(MAX_LAYOUT_TRIES_516B51B7):
            x9 = unifint(diff_lb, diff_ub, x7)
            x10 = unifint(diff_lb, diff_ub, x7)
            if x9 >= x0 or x10 >= x1:
                continue
            x11 = randint(ZERO, x0 - x9)
            x12 = randint(ZERO, x1 - x10)
            x13 = _rectangle_patch_516b51b7(x11, x12, x9, x10)
            if len(intersection(x13, x5)) > ZERO:
                continue
            x14 = _clip_patch_516b51b7(outbox(x13), WORK_SHAPE_516B51B7)
            x5 = combine(x5, combine(x13, x14))
            x4.append((x11, x12, x9, x10))
            x8 = T
            break
        if not x8:
            return (), ORIGIN
    x15 = frozenset((i, j) for x16, x17, x18, x19 in x4 for i, j in _rectangle_patch_516b51b7(x16, x17, x18, x19))
    x20 = len(x15)
    x21 = lowermost(x15) - uppermost(x15) + ONE
    x22 = rightmost(x15) - leftmost(x15) + ONE
    x23 = randint(*MARGIN_BOUNDS_516B51B7)
    x24 = randint(*MARGIN_BOUNDS_516B51B7)
    x25 = randint(*MARGIN_BOUNDS_516B51B7)
    x26 = randint(*MARGIN_BOUNDS_516B51B7)
    x27 = x21 + x23 + x24
    x28 = x22 + x25 + x26
    x29 = x20 / (x27 * x28)
    if x29 < 0.25 or x29 > 0.7:
        return (), ORIGIN
    x30 = x23 - uppermost(x15)
    x31 = x25 - leftmost(x15)
    x32 = tuple((x16 + x30, x17 + x31, x18, x19) for x16, x17, x18, x19 in x4)
    return x32, (x27, x28)


def generate_516b51b7(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0, x1 = _sample_layout_516b51b7(diff_lb, diff_ub)
        if len(x0) == ZERO:
            continue
        x2 = canvas(ZERO, x1)
        x3 = canvas(ZERO, x1)
        for x4, x5, x6, x7 in x0:
            x8 = _rectangle_patch_516b51b7(x4, x5, x6, x7)
            x2 = fill(x2, ONE, x8)
            x3 = _paint_layered_rectangle_516b51b7(x3, x4, x5, x6, x7)
        x9 = choice(GRID_TRANSFORMS_516B51B7)
        x10 = x9(x2)
        x11 = x9(x3)
        if x10 != x11:
            return {"input": x10, "output": x11}
