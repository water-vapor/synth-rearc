from __future__ import annotations

from synth_rearc.core import *


def _object_key_9385bd28(
    obj: Object,
) -> tuple[Integer, Integer, Integer, Integer]:
    return (uppermost(obj), leftmost(obj), lowermost(obj), rightmost(obj))


def legend_objects_9385bd28(
    grid: Grid,
) -> tuple[Object, ...]:
    x0 = objects(grid, T, F, T)
    x1 = tuple(x2 for x2 in x0 if size(x2) <= TWO)
    return tuple(sorted(x1, key=_object_key_9385bd28))


def legend_cells_9385bd28(
    grid: Grid,
) -> Indices:
    x0 = legend_objects_9385bd28(grid)
    return frozenset(index for obj in x0 for _, index in obj)


def legend_origin_9385bd28(
    grid: Grid,
) -> IntegerTuple:
    x0 = legend_cells_9385bd28(grid)
    if len(x0) == ZERO:
        return ORIGIN
    return ulcorner(x0)


def legend_mapping_9385bd28(
    grid: Grid,
) -> tuple[tuple[Integer, Integer | None], ...]:
    x0 = mostcolor(grid)
    x1 = legend_cells_9385bd28(grid)
    if len(x1) == ZERO:
        return tuple()
    x2, x3 = ulcorner(x1)
    x4 = lowermost(x1)
    x5 = []
    for x6 in range(x2, add(x4, ONE)):
        x7 = index(grid, (x6, x3))
        x8 = index(grid, (x6, add(x3, ONE)))
        if either(x7 is None, x7 == x0):
            continue
        if either(x8 is None, x8 == x0):
            x5.append((x7, None))
        else:
            x5.append((x7, x8))
    return tuple(x5)


def main_color_patches_9385bd28(
    grid: Grid,
) -> tuple[tuple[Integer, Indices], ...]:
    x0 = mostcolor(grid)
    x1 = legend_cells_9385bd28(grid)
    x2 = fill(grid, x0, x1)
    x3 = fgpartition(x2)
    x4 = tuple((color(x5), toindices(x5)) for x5 in x3)
    return tuple(sorted(x4, key=lambda item: (size(backdrop(item[1])), item[0])))


def corner_shape_9385bd28(
    corner_name: str,
) -> Indices:
    if corner_name == "tl":
        return frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO)})
    if corner_name == "tr":
        return frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ONE)})
    if corner_name == "bl":
        return frozenset({(ZERO, ZERO), (ONE, ZERO), (ONE, ONE)})
    return frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE)})


def place_corner_shape_9385bd28(
    upper_left: IntegerTuple,
    corner_name: str,
    color_value: Integer,
) -> Object:
    x0 = corner_shape_9385bd28(corner_name)
    x1 = shift(x0, upper_left)
    return recolor(color_value, x1)


def rectangle_indices_9385bd28(
    upper_left: IntegerTuple,
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = upper_left
    x2, x3 = dims
    return frozenset(
        (i, j)
        for i in range(x0, add(x0, x2))
        for j in range(x1, add(x1, x3))
    )
