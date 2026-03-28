from __future__ import annotations

from synth_rearc.core import *


ORIENTS_896D5239 = ("down", "up", "right", "left")


def _in_bounds_896d5239(
    loc: IntegerTuple,
    dims: IntegerTuple,
) -> bool:
    return ZERO <= loc[ZERO] < dims[ZERO] and ZERO <= loc[ONE] < dims[ONE]


def triangle_sides_896d5239(
    apex: IntegerTuple,
    radius: Integer,
    orient: str,
) -> tuple[tuple[IntegerTuple, ...], tuple[IntegerTuple, ...]]:
    ai, aj = apex
    x0 = range(radius + ONE)
    if orient == "down":
        x1 = tuple((ai + d, aj - d) for d in x0)
        x2 = tuple((ai + d, aj + d) for d in x0)
        return x1, x2
    if orient == "up":
        x1 = tuple((ai - d, aj - d) for d in x0)
        x2 = tuple((ai - d, aj + d) for d in x0)
        return x1, x2
    if orient == "right":
        x1 = tuple((ai - d, aj + d) for d in x0)
        x2 = tuple((ai + d, aj + d) for d in x0)
        return x1, x2
    x1 = tuple((ai - d, aj - d) for d in x0)
    x2 = tuple((ai + d, aj - d) for d in x0)
    return x1, x2


def triangle_cells_896d5239(
    apex: IntegerTuple,
    radius: Integer,
    orient: str,
) -> Indices:
    ai, aj = apex
    out = set()
    x0 = range(radius + ONE)
    if orient == "down":
        for d in x0:
            x1 = ai + d
            for x2 in range(aj - d, aj + d + ONE):
                out.add((x1, x2))
        return frozenset(out)
    if orient == "up":
        for d in x0:
            x1 = ai - d
            for x2 in range(aj - d, aj + d + ONE):
                out.add((x1, x2))
        return frozenset(out)
    if orient == "right":
        for d in x0:
            x1 = aj + d
            for x2 in range(ai - d, ai + d + ONE):
                out.add((x2, x1))
        return frozenset(out)
    for d in x0:
        x1 = aj - d
        for x2 in range(ai - d, ai + d + ONE):
            out.add((x2, x1))
    return frozenset(out)


def clipped_triangle_cells_896d5239(
    apex: IntegerTuple,
    radius: Integer,
    orient: str,
    dims: IntegerTuple,
) -> Indices:
    x0 = triangle_cells_896d5239(apex, radius, orient)
    return frozenset(x1 for x1 in x0 if _in_bounds_896d5239(x1, dims))


def clipped_triangle_boundary_896d5239(
    apex: IntegerTuple,
    radius: Integer,
    orient: str,
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = triangle_sides_896d5239(apex, radius, orient)
    x2 = tuple(x3 for x3 in x0 if _in_bounds_896d5239(x3, dims))
    x3 = tuple(x4 for x4 in x1 if _in_bounds_896d5239(x4, dims))
    return frozenset(x2 + x3)


def visible_triangle_sides_896d5239(
    apex: IntegerTuple,
    radius: Integer,
    orient: str,
    dims: IntegerTuple,
) -> tuple[tuple[IntegerTuple, ...], tuple[IntegerTuple, ...]]:
    x0, x1 = triangle_sides_896d5239(apex, radius, orient)
    x2 = tuple(x3 for x3 in x0 if _in_bounds_896d5239(x3, dims))
    x3 = tuple(x4 for x4 in x1 if _in_bounds_896d5239(x4, dims))
    return x2, x3


def cluster_markers_896d5239(
    marks: Indices,
) -> tuple[Indices, ...]:
    x0 = set(marks)
    out = []
    while len(x0) > ZERO:
        x1 = min(x0)
        x0.remove(x1)
        x2 = {x1}
        x3 = [x1]
        while len(x3) > ZERO:
            x4 = x3.pop()
            x5 = tuple(
                x6 for x6 in x0
                if max(abs(x4[ZERO] - x6[ZERO]), abs(x4[ONE] - x6[ONE])) <= TWO
            )
            for x6 in x5:
                x0.remove(x6)
                x2.add(x6)
                x3.append(x6)
        out.append(frozenset(x2))
    out.sort(key=min)
    return tuple(out)


def fit_cluster_triangle_896d5239(
    cluster: Indices,
    dims: IntegerTuple,
) -> tuple[IntegerTuple, Integer, str, Indices, Indices]:
    x0 = {x1: x2 for x2, x1 in enumerate(ORIENTS_896D5239)}
    x1 = max(dims)
    x2 = None
    for x3 in sorted(cluster):
        for x4 in ORIENTS_896D5239:
            for x5 in range(ONE, x1 + ONE):
                x6 = clipped_triangle_boundary_896d5239(x3, x5, x4, dims)
                if not cluster <= x6:
                    continue
                x7 = clipped_triangle_cells_896d5239(x3, x5, x4, dims)
                x8 = (len(x7), x5, x0[x4], x3[ZERO], x3[ONE])
                if x2 is None or x8 < x2[ZERO]:
                    x2 = (x8, x3, x5, x4, x7, x6)
    if x2 is None:
        raise ValueError(f"could not fit triangle for cluster {sorted(cluster)}")
    return x2[ONE], x2[TWO], x2[THREE], x2[FOUR], x2[FIVE]
