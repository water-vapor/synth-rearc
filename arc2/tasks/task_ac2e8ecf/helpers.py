from arc2.core import *


def frame_patch_ac2e8ecf(box_h: int, box_w: int) -> Indices:
    x0 = canvas(ZERO, (box_h, box_w))
    x1 = asindices(x0)
    x2 = box(x1)
    return x2


def cross_patch_ac2e8ecf(
    box_h: int,
    box_w: int,
    row_idx: int,
    col_idx: int,
) -> Indices:
    x0 = connect((row_idx, ZERO), (row_idx, box_w - ONE))
    x1 = connect((ZERO, col_idx), (box_h - ONE, col_idx))
    x2 = combine(x0, x1)
    return x2


def is_hollow_frame_ac2e8ecf(obj: Object) -> Boolean:
    x0 = height(obj)
    x1 = width(obj)
    x2 = x0 > TWO and x1 > TWO
    x3 = toindices(obj) == box(obj)
    return x2 and x3


def order_key_ac2e8ecf(obj: Object) -> tuple[int, int, int, int, int]:
    return (
        uppermost(obj),
        leftmost(obj),
        lowermost(obj),
        rightmost(obj),
        color(obj),
    )


def reserve_box_ac2e8ecf(obj: Object, dims: IntegerTuple) -> Indices:
    grid_h, grid_w = dims
    top = max(ZERO, uppermost(obj) - ONE)
    bottom = min(grid_h - ONE, lowermost(obj) + ONE)
    left = max(ZERO, leftmost(obj) - ONE)
    right = min(grid_w - ONE, rightmost(obj) + ONE)
    return frozenset((i, j) for i in range(top, bottom + ONE) for j in range(left, right + ONE))


def column_overlap_ac2e8ecf(a: Patch, b: Patch) -> Boolean:
    return not (rightmost(a) < leftmost(b) or rightmost(b) < leftmost(a))


def _hits_placed_ac2e8ecf(obj: Object, placed: tuple[Object, ...]) -> Boolean:
    cells = toindices(obj)
    return any(len(intersection(cells, toindices(other))) > ZERO for other in placed)


def shift_up_ac2e8ecf(obj: Object, placed: tuple[Object, ...]) -> Object:
    current = obj
    while uppermost(current) > ZERO:
        candidate = shift(current, (-ONE, ZERO))
        if _hits_placed_ac2e8ecf(candidate, placed):
            break
        current = candidate
    return current


def shift_down_ac2e8ecf(
    obj: Object,
    placed: tuple[Object, ...],
    grid_h: int,
) -> Object:
    current = obj
    while lowermost(current) < grid_h - ONE:
        candidate = shift(current, (ONE, ZERO))
        if _hits_placed_ac2e8ecf(candidate, placed):
            break
        current = candidate
    return current


def pack_top_ac2e8ecf(objs: Container) -> tuple[Object, ...]:
    placed: tuple[Object, ...] = ()
    for obj in sorted(objs, key=order_key_ac2e8ecf):
        placed = placed + (shift_up_ac2e8ecf(obj, placed),)
    return placed


def pack_bottom_ac2e8ecf(objs: Container, grid_h: int) -> tuple[Object, ...]:
    placed: tuple[Object, ...] = ()
    for obj in sorted(objs, key=order_key_ac2e8ecf, reverse=True):
        placed = placed + (shift_down_ac2e8ecf(obj, placed, grid_h),)
    return placed


def paint_objects_ac2e8ecf(grid: Grid, objs: Container) -> Grid:
    canvas_grid = grid
    for obj in objs:
        canvas_grid = paint(canvas_grid, obj)
    return canvas_grid
