from __future__ import annotations

from arc2.core import *


def endpoint_pair_d017b73f(
    patch: Patch,
) -> tuple[IntegerTuple, IntegerTuple]:
    x0 = frozenset(toindices(patch))
    x1 = []
    for x2 in x0:
        x3 = len(intersection(dneighbors(x2), x0))
        if x3 == ONE:
            x1.append(x2)
    if len(x1) == ZERO:
        x4 = ulcorner(x0)
        return (x4, x4)
    x5 = tuple(sorted(x1, key=lambda x6: (x6[1], x6[0])))
    return (first(x5), last(x5))


def left_endpoint_d017b73f(
    patch: Patch,
) -> IntegerTuple:
    return endpoint_pair_d017b73f(patch)[0]


def right_endpoint_d017b73f(
    patch: Patch,
) -> IntegerTuple:
    return endpoint_pair_d017b73f(patch)[1]


def ordered_objects_d017b73f(
    grid: Grid,
) -> tuple[Object, ...]:
    x0 = objects(grid, T, F, T)
    return tuple(sorted(x0, key=lambda x1: (leftmost(x1), uppermost(x1), size(x1), color(x1))))


def pack_objects_d017b73f(
    objs: tuple[Object, ...],
) -> tuple[Object, ...]:
    if len(objs) == ZERO:
        return tuple()
    x0 = shift(first(objs), (ZERO, -leftmost(first(objs))))
    x1 = [x0]
    x2 = right_endpoint_d017b73f(x0)
    for x3 in objs[1:]:
        x4 = left_endpoint_d017b73f(x3)
        x5 = subtract(add(x2, RIGHT), x4)
        x6 = shift(x3, x5)
        x1.append(x6)
        x2 = right_endpoint_d017b73f(x6)
    return tuple(x1)


def packed_grid_d017b73f(
    objs: tuple[Object, ...],
    h: Integer = THREE,
) -> Grid:
    x0 = pack_objects_d017b73f(objs)
    x1 = merge(x0)
    x2 = increment(rightmost(x1))
    x3 = canvas(ZERO, (h, x2))
    return paint(x3, x1)
