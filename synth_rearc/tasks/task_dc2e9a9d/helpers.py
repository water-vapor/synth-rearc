from synth_rearc.core import *


HORIZONTAL_SIDES_DC2E9A9D = frozenset((LEFT, RIGHT))
VERTICAL_SIDES_DC2E9A9D = frozenset((UP, DOWN))


def tab_side_dc2e9a9d(
    obj: Object,
) -> IntegerTuple:
    x0 = toindices(normalize(obj))
    x1 = decrement(height(obj))
    x2 = decrement(width(obj))
    x3 = sum(i == ZERO for i, _ in x0)
    x4 = sum(i == x1 for i, _ in x0)
    x5 = sum(j == ZERO for _, j in x0)
    x6 = sum(j == x2 for _, j in x0)
    if x5 == ONE:
        return LEFT
    if x6 == ONE:
        return RIGHT
    if x3 == ONE:
        return UP
    if x4 == ONE:
        return DOWN
    raise ValueError("object is not a tabbed hollow frame")


def copy_color_dc2e9a9d(
    side: IntegerTuple,
) -> Integer:
    if side in HORIZONTAL_SIDES_DC2E9A9D:
        return ONE
    return EIGHT


def mirrored_copy_dc2e9a9d(
    obj: Object,
) -> Object:
    x0 = tab_side_dc2e9a9d(obj)
    if x0 == LEFT:
        x1 = add(width(obj), ONE)
        x2 = vmirror(obj)
        x3 = shift(x2, astuple(ZERO, x1))
    elif x0 == RIGHT:
        x1 = add(width(obj), ONE)
        x2 = vmirror(obj)
        x3 = shift(x2, astuple(ZERO, invert(x1)))
    elif x0 == UP:
        x1 = add(height(obj), ONE)
        x2 = hmirror(obj)
        x3 = shift(x2, astuple(x1, ZERO))
    else:
        x1 = add(height(obj), ONE)
        x2 = hmirror(obj)
        x3 = shift(x2, astuple(invert(x1), ZERO))
    x4 = copy_color_dc2e9a9d(x0)
    return recolor(x4, x3)


def make_tabbed_frame_dc2e9a9d(
    top: Integer,
    left: Integer,
    side: IntegerTuple,
    frame_h: Integer,
    frame_w: Integer,
) -> Object:
    cells = set()
    for i in range(frame_h):
        cells.add((i, ZERO))
        cells.add((i, decrement(frame_w)))
    for j in range(frame_w):
        cells.add((ZERO, j))
        cells.add((decrement(frame_h), j))
    if side == LEFT:
        cells = {(i, increment(j)) for i, j in cells}
        cells.add((divide(frame_h, TWO), ZERO))
    elif side == RIGHT:
        cells.add((divide(frame_h, TWO), frame_w))
    elif side == UP:
        cells = {(increment(i), j) for i, j in cells}
        cells.add((ZERO, divide(frame_w, TWO)))
    else:
        cells.add((frame_h, divide(frame_w, TWO)))
    x0 = frozenset(cells)
    x1 = shift(x0, (top, left))
    return recolor(THREE, x1)


def object_dims_dc2e9a9d(
    side: IntegerTuple,
    frame_h: Integer,
    frame_w: Integer,
) -> IntegerTuple:
    if side in HORIZONTAL_SIDES_DC2E9A9D:
        return astuple(frame_h, increment(frame_w))
    return astuple(increment(frame_h), frame_w)
