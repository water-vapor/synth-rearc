from __future__ import annotations

from arc2.core import *


def _cross_9720b24f(
    a: tuple[int, int],
    b: tuple[int, int],
    c: tuple[int, int],
) -> int:
    return (b[ZERO] - a[ZERO]) * (c[ONE] - a[ONE]) - (b[ONE] - a[ONE]) * (c[ZERO] - a[ZERO])


def convex_hull_vertices_9720b24f(
    patch: Patch,
) -> tuple[tuple[int, int], ...]:
    x0 = tuple(sorted({
        (i, j)
        for ii, jj in toindices(patch)
        for i, j in ((ii, jj), (ii + ONE, jj), (ii, jj + ONE), (ii + ONE, jj + ONE))
    }))
    if len(x0) <= TWO:
        return x0
    x1 = []
    for x2 in x0:
        while len(x1) >= TWO and _cross_9720b24f(x1[-TWO], x1[-ONE], x2) <= ZERO:
            x1.pop()
        x1.append(x2)
    x3 = []
    for x4 in reversed(x0):
        while len(x3) >= TWO and _cross_9720b24f(x3[-TWO], x3[-ONE], x4) <= ZERO:
            x3.pop()
        x3.append(x4)
    return tuple(x1[:-ONE] + x3[:-ONE])


def point_strictly_inside_hull_9720b24f(
    point: tuple[float, float],
    hull: tuple[tuple[int, int], ...],
) -> Boolean:
    if len(hull) < THREE:
        return F
    x0 = None
    x1 = len(hull)
    for x2 in range(x1):
        x3 = hull[x2]
        x4 = hull[(x2 + ONE) % x1]
        x5 = (x4[ZERO] - x3[ZERO]) * (point[ONE] - x3[ONE]) - (x4[ONE] - x3[ONE]) * (point[ZERO] - x3[ZERO])
        if x5 == 0:
            return F
        x6 = x5 > 0
        if x0 is None:
            x0 = x6
            continue
        if x6 != x0:
            return F
    return T


def interior_patch_9720b24f(
    patch: Patch,
    dims: IntegerTuple,
) -> Indices:
    x0 = convex_hull_vertices_9720b24f(patch)
    if len(x0) < THREE:
        return frozenset()
    x1, x2 = dims
    x3 = toindices(patch)
    x4 = max(ZERO, uppermost(patch))
    x5 = min(x1 - ONE, lowermost(patch))
    x6 = max(ZERO, leftmost(patch))
    x7 = min(x2 - ONE, rightmost(patch))
    x8 = {
        (i, j)
        for i in range(x4, x5 + ONE)
        for j in range(x6, x7 + ONE)
        if (i, j) not in x3 and point_strictly_inside_hull_9720b24f((i + 0.5, j + 0.5), x0)
    }
    return frozenset(x8)


def intruder_indices_9720b24f(
    grid: Grid,
) -> Indices:
    x0 = objects(grid, T, T, F)
    x1 = shape(grid)
    x2 = set()
    for x3 in x0:
        x4 = color(x3)
        if x4 == ZERO:
            continue
        x5 = interior_patch_9720b24f(x3, x1)
        x6 = {
            ij
            for ij in x5
            if index(grid, ij) not in (ZERO, x4)
        }
        x2 |= x6
    return frozenset(x2)


def _polyline_patch_9720b24f(
    vertices: tuple[IntegerTuple, ...],
) -> Indices:
    x0 = frozenset()
    for x1, x2 in zip(vertices, vertices[ONE:]):
        x0 = combine(x0, connect(x1, x2))
    return x0


def hook_outline_9720b24f(
    height_value: Integer,
    width_value: Integer,
    inset: Integer,
) -> Indices:
    x0 = astuple(ZERO, width_value - ONE)
    x1 = astuple(ZERO, inset)
    x2 = astuple(ONE, inset - ONE)
    x3 = astuple(height_value - TWO, inset - ONE)
    x4 = astuple(height_value - ONE, inset)
    x5 = astuple(height_value - ONE, width_value - TWO)
    x6 = (x0, x1, x2, x3, x4, x5)
    return _polyline_patch_9720b24f(x6)


def wedge_outline_9720b24f(
    radius: Integer,
) -> Indices:
    x0 = astuple(ZERO, radius)
    x1 = astuple(radius, ZERO)
    x2 = astuple(radius + ONE, ZERO)
    x3 = astuple(double(radius) + ONE, radius)
    x4 = astuple(double(radius) + ONE, radius + ONE)
    x5 = astuple(radius + ONE, double(radius) + ONE)
    x6 = (x0, x1, x2, x3, x4, x5)
    return _polyline_patch_9720b24f(x6)


def kite_outline_9720b24f(
    radius: Integer,
) -> Indices:
    x0 = astuple(ZERO, radius - ONE)
    x1 = astuple(ZERO, radius)
    x2 = astuple(radius, double(radius))
    x3 = astuple(double(radius), radius)
    x4 = astuple(radius, ZERO)
    x5 = (x0, x1, x2, x3, x4)
    return _polyline_patch_9720b24f(x5)


__all__ = [
    "convex_hull_vertices_9720b24f",
    "hook_outline_9720b24f",
    "interior_patch_9720b24f",
    "intruder_indices_9720b24f",
    "kite_outline_9720b24f",
    "point_strictly_inside_hull_9720b24f",
    "wedge_outline_9720b24f",
]
