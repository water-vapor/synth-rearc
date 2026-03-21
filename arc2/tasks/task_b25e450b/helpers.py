from arc2.core import *


def rectangle_indices_b25e450b(
    start: IntegerTuple,
    dims: IntegerTuple,
) -> Indices:
    return frozenset(
        (i, j)
        for i in range(start[0], start[0] + dims[0])
        for j in range(start[1], start[1] + dims[1])
    )


def attached_rectangle_b25e450b(
    side: str,
    start: int,
    span: int,
    depth: int,
    grid_shape: IntegerTuple,
) -> Object:
    h, w = grid_shape
    if side == "top":
        x0 = rectangle_indices_b25e450b((ZERO, start), (depth, span))
    elif side == "bottom":
        x0 = rectangle_indices_b25e450b((h - depth, start), (depth, span))
    elif side == "left":
        x0 = rectangle_indices_b25e450b((start, ZERO), (span, depth))
    else:
        x0 = rectangle_indices_b25e450b((start, w - depth), (span, depth))
    return recolor(ZERO, x0)


def interval_is_clear_b25e450b(
    start: int,
    span: int,
    reserved: list[tuple[int, int]],
) -> bool:
    x0 = start + span - ONE
    return all(x0 < x1 - ONE or start > x2 + ONE for x1, x2 in reserved)


def move_to_opposite_border_b25e450b(
    obj: Object,
    grid_shape: IntegerTuple,
) -> Object:
    h, w = grid_shape
    if uppermost(obj) == ZERO:
        return shift(obj, (h - height(obj), ZERO))
    if lowermost(obj) == h - ONE:
        return shift(obj, (-uppermost(obj), ZERO))
    if leftmost(obj) == ZERO:
        return shift(obj, (ZERO, w - width(obj)))
    return shift(obj, (ZERO, -leftmost(obj)))


def corridor_b25e450b(
    source: Patch,
    destination: Patch,
) -> Indices:
    return backdrop(toindices(source) | toindices(destination))


def sort_key_b25e450b(
    obj: Object,
) -> tuple[int, int, int, int]:
    return (uppermost(obj), leftmost(obj), lowermost(obj), rightmost(obj))
