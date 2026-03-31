from __future__ import annotations

from collections import defaultdict
from itertools import permutations

from synth_rearc.core import *


Point35ab12c3 = tuple[int, int]
Outline35ab12c3 = dict[str, object]

OFFSETS_35AB12C3 = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


def sign_35ab12c3(n: int) -> int:
    return (n > 0) - (n < 0)


def connect_cells_35ab12c3(
    a: Point35ab12c3,
    b: Point35ab12c3,
) -> tuple[Point35ab12c3, ...]:
    ai, aj = a
    bi, bj = b
    if not (ai == bi or aj == bj or abs(ai - bi) == abs(aj - bj)):
        return ()
    di = sign_35ab12c3(bi - ai)
    dj = sign_35ab12c3(bj - aj)
    x0 = [a]
    x1 = a
    while x1 != b:
        x1 = (x1[0] + di, x1[1] + dj)
        x0.append(x1)
    return tuple(x0)


def normalize_points_35ab12c3(
    points: tuple[Point35ab12c3, ...],
) -> tuple[Point35ab12c3, ...]:
    x0 = min(i for i, _ in points)
    x1 = min(j for _, j in points)
    return tuple((i - x0, j - x1) for i, j in points)


def transform_points_35ab12c3(
    points: tuple[Point35ab12c3, ...],
    mode: int,
) -> tuple[Point35ab12c3, ...]:
    if mode == 0:
        x0 = tuple((i, j) for i, j in points)
    elif mode == 1:
        x0 = tuple((i, -j) for i, j in points)
    elif mode == 2:
        x0 = tuple((-i, j) for i, j in points)
    elif mode == 3:
        x0 = tuple((-i, -j) for i, j in points)
    elif mode == 4:
        x0 = tuple((j, i) for i, j in points)
    elif mode == 5:
        x0 = tuple((j, -i) for i, j in points)
    elif mode == 6:
        x0 = tuple((-j, i) for i, j in points)
    else:
        x0 = tuple((-j, -i) for i, j in points)
    return normalize_points_35ab12c3(x0)


def candidate_sequence_35ab12c3(
    order: tuple[Point35ab12c3, ...],
    cycle: bool,
) -> tuple[Point35ab12c3, ...] | None:
    x0 = []
    for x1, x2 in zip(order, order[1:]):
        x3 = connect_cells_35ab12c3(x1, x2)
        if len(x3) == 0:
            return None
        x0.append(x3)
    if cycle:
        x4 = connect_cells_35ab12c3(order[-1], order[0])
        if len(x4) == 0:
            return None
        x0.append(x4)
    x5: dict[Point35ab12c3, list[tuple[int, bool]]] = {}
    for x6, x7 in enumerate(x0):
        for x8, x9 in enumerate(x7):
            x10 = x8 in (0, len(x7) - 1)
            x5.setdefault(x9, []).append((x6, x10))
    x11 = len(x0)
    for x12 in x5.values():
        if len(x12) == 1:
            continue
        if any(not x13 for _, x13 in x12):
            return None
        x14 = sorted(x15 for x15, _ in x12)
        if len(x14) > 2:
            return None
        if len(x14) == 2 and not (x14[1] == x14[0] + 1 or (cycle and x14 == [0, x11 - 1])):
            return None
    x16 = []
    for x17, x18 in enumerate(x0):
        x16.extend(x18 if x17 == 0 else x18[1:])
    if cycle and x16[-1] == x16[0]:
        x16.pop()
    return tuple(x16)


def infer_outline_35ab12c3(
    points: tuple[Point35ab12c3, ...],
) -> Outline35ab12c3 | None:
    if len(points) < 2:
        return None
    x0: dict[frozenset[Point35ab12c3], tuple[tuple[Point35ab12c3, ...], tuple[Point35ab12c3, ...]]] = {}
    x1: dict[frozenset[Point35ab12c3], tuple[tuple[Point35ab12c3, ...], tuple[Point35ab12c3, ...]]] = {}
    for x2 in permutations(points):
        for x3 in (False, True):
            if x3 and len(points) < 3:
                continue
            x4 = candidate_sequence_35ab12c3(x2, x3)
            if x4 is None:
                continue
            if x3:
                x0[frozenset(x4)] = (x2, x4)
            else:
                x1[frozenset(x4)] = (x2, x4)
    if len(x0) > 0:
        x5, x6 = min(x0.values(), key=lambda item: len(item[1]))
        return {"cycle": True, "vertices": x5, "sequence": x6, "cells": frozenset(x6)}
    if len(x1) > 0:
        x7, x8 = min(x1.values(), key=lambda item: len(item[1]))
        return {"cycle": False, "vertices": x7, "sequence": x8, "cells": frozenset(x8)}
    return None


def infer_outlines_35ab12c3(
    points_by_color: dict[int, tuple[Point35ab12c3, ...]],
) -> dict[int, Outline35ab12c3]:
    x0 = {}
    for x1, x2 in points_by_color.items():
        x3 = infer_outline_35ab12c3(x2)
        if x3 is None:
            continue
        if len(x3["cells"]) <= len(x2):
            continue
        x0[x1] = x3
    return x0


def points_by_color_35ab12c3(
    grid: Grid,
) -> dict[int, tuple[Point35ab12c3, ...]]:
    x0: dict[int, list[Point35ab12c3]] = defaultdict(list)
    for x1, x2 in enumerate(grid):
        for x3, x4 in enumerate(x2):
            if x4 != ZERO:
                x0[x4].append((x1, x3))
    return {x5: tuple(x6) for x5, x6 in x0.items()}


def paint_cells_35ab12c3(
    grid: Grid,
    color_: int,
    cells: frozenset[Point35ab12c3] | tuple[Point35ab12c3, ...] | set[Point35ab12c3],
) -> Grid:
    return fill(grid, color_, frozenset(cells))


def all_subpaths_35ab12c3(
    sequence: tuple[Point35ab12c3, ...],
    cycle: bool,
):
    x0 = len(sequence)
    if cycle:
        x1 = (sequence, tuple(reversed(sequence)))
        for x2 in x1:
            for x3 in range(x0):
                x4 = []
                for x5 in range(1, x0 + 1):
                    x4.append(x2[(x3 + x5 - 1) % x0])
                    yield tuple(x4)
    else:
        x6 = (sequence, tuple(reversed(sequence)))
        for x7 in x6:
            for x8 in range(x0):
                x9 = []
                for x10 in range(x8, x0):
                    x9.append(x7[x10])
                    yield tuple(x9)


def best_generic_companion_35ab12c3(
    points: tuple[Point35ab12c3, ...],
    outlines: dict[int, Outline35ab12c3],
    occupied: frozenset[Point35ab12c3],
) -> frozenset[Point35ab12c3] | None:
    x0 = set(points)
    x1 = None
    for x2, x3 in outlines.items():
        for x4, x5 in OFFSETS_35AB12C3:
            for x6 in all_subpaths_35ab12c3(x3["sequence"], x3["cycle"]):
                x7 = tuple((i + x4, j + x5) for i, j in x6)
                x8 = frozenset(x7)
                if not x0 <= x8:
                    continue
                if len(x8) <= len(x0):
                    continue
                if len(x8 & occupied) > 0:
                    continue
                x9 = int(x7[0] in x0) + int(x7[-1] in x0)
                x10 = (len(x8), x9, -int(x3["cycle"]), x2, (x4, x5), x8)
                if x1 is None or x10 > x1:
                    x1 = x10
    if x1 is None:
        return None
    return x1[-1]


def is_rectangle_cycle_35ab12c3(
    outline: Outline35ab12c3,
) -> bool:
    if not outline["cycle"] or len(outline["vertices"]) != 4:
        return False
    x0 = {
        (sign_35ab12c3(b[0] - a[0]), sign_35ab12c3(b[1] - a[1]))
        for a, b in zip(outline["vertices"], outline["vertices"][1:] + outline["vertices"][:1])
    }
    return x0 == {(1, 0), (-1, 0), (0, 1), (0, -1)}


def special_rectangle_companion_35ab12c3(
    points: tuple[Point35ab12c3, ...],
    outlines: dict[int, Outline35ab12c3],
    occupied: frozenset[Point35ab12c3],
) -> frozenset[Point35ab12c3] | None:
    if len(points) != 1:
        return None
    x0 = points[0]
    for x1 in outlines.values():
        if not is_rectangle_cycle_35ab12c3(x1):
            continue
        x2 = x1["cells"]
        x3 = min(i for i, _ in x2)
        x4 = max(i for i, _ in x2)
        x5 = min(j for _, j in x2)
        x6 = max(j for _, j in x2)
        x7 = {(i - 1, j - 1) for i, j in x2}
        if x0 not in x7:
            continue
        x8 = set(x7)
        x8.discard((x3, x6 - 1))
        x8.discard((x4 - 1, x5))
        if len(x8 & occupied) == 0:
            return frozenset(x8)
    return None


def special_pentagon_companion_35ab12c3(
    points: tuple[Point35ab12c3, ...],
    outlines: dict[int, Outline35ab12c3],
    occupied: frozenset[Point35ab12c3],
) -> frozenset[Point35ab12c3] | None:
    if len(points) != 1:
        return None
    x0 = points[0]
    for x1 in outlines.values():
        if not x1["cycle"] or len(x1["vertices"]) != 5:
            continue
        x2 = {(i, j - 1) for i, j in x1["cells"]}
        if x0 not in x2:
            continue
        x3: dict[int, list[int]] = defaultdict(list)
        for x4, x5 in x2:
            x3[x4].append(x5)
        x6 = min(x3)
        x7 = max(x3)
        x8 = set(x2)
        for x9 in x3[x6]:
            if x9 != min(x3[x6]):
                x8.discard((x6, x9))
        for x10 in x3[x7]:
            if x10 != min(x3[x7]):
                x8.discard((x7, x10))
        if len(x8 & occupied) == 0:
            return frozenset(x8)
    return None


def template_vertices_35ab12c3(
    name: str,
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[Point35ab12c3, ...], bool]:
    if name == "segment":
        x0 = unifint(diff_lb, diff_ub, (4, 10))
        return ((0, 0), (0, x0 - 1)), False
    if name == "vshape":
        x1 = unifint(diff_lb, diff_ub, (3, 6))
        x2 = unifint(diff_lb, diff_ub, (3, 6))
        return ((x1, 0), (0, x1), (x2, x1 + x2)), False
    if name == "corner":
        x3 = unifint(diff_lb, diff_ub, (4, 8))
        x4 = unifint(diff_lb, diff_ub, (2, 5))
        x5 = unifint(diff_lb, diff_ub, (2, 5))
        return ((x3, 0), (0, 0), (0, x4), (x5, x4 + x5)), False
    if name == "rectangle":
        x6 = unifint(diff_lb, diff_ub, (5, 9))
        x7 = unifint(diff_lb, diff_ub, (5, 9))
        return ((0, 0), (0, x7), (x6, x7), (x6, 0)), True
    x8 = unifint(diff_lb, diff_ub, (1, 3))
    x9 = unifint(diff_lb, diff_ub, (2, 5))
    return ((0, 0), (0, x8), (x9, x8 + x9), (2 * x9, x8), (2 * x9, 0), (x9, -x9)), True


def make_outline_from_template_35ab12c3(
    name: str,
    diff_lb: float,
    diff_ub: float,
    mode: int,
) -> Outline35ab12c3:
    x0, x1 = template_vertices_35ab12c3(name, diff_lb, diff_ub)
    x2 = transform_points_35ab12c3(x0, mode)
    x3 = candidate_sequence_35ab12c3(x2, x1)
    return {"cycle": x1, "vertices": x2, "sequence": x3, "cells": frozenset(x3)}


def bbox_35ab12c3(
    cells: frozenset[Point35ab12c3] | set[Point35ab12c3] | tuple[Point35ab12c3, ...],
) -> tuple[int, int, int, int]:
    return (
        min(i for i, _ in cells),
        max(i for i, _ in cells),
        min(j for _, j in cells),
        max(j for _, j in cells),
    )


def shift_cells_35ab12c3(
    cells: frozenset[Point35ab12c3] | set[Point35ab12c3] | tuple[Point35ab12c3, ...],
    offset: Point35ab12c3,
) -> frozenset[Point35ab12c3]:
    return frozenset((i + offset[0], j + offset[1]) for i, j in cells)


def shifted_subpath_35ab12c3(
    outline: Outline35ab12c3,
    offset: Point35ab12c3,
    start: int,
    length: int,
) -> tuple[Point35ab12c3, ...]:
    x0 = outline["sequence"]
    x1 = x0 if choice((True, False)) else tuple(reversed(x0))
    x2 = tuple(x1[start:start + length])
    return tuple((i + offset[0], j + offset[1]) for i, j in x2)


def isolated_distractor_points_35ab12c3(
    count_: int,
    occupied: frozenset[Point35ab12c3],
    height_: int,
    width_: int,
) -> tuple[Point35ab12c3, ...] | None:
    x0 = []
    x1 = 0
    while len(x0) < count_ and x1 < 200:
        x1 += 1
        x2 = (randint(0, height_ - 1), randint(0, width_ - 1))
        if x2 in occupied:
            continue
        x3 = True
        for x4 in x0:
            if x2[0] == x4[0] or x2[1] == x4[1] or abs(x2[0] - x4[0]) == abs(x2[1] - x4[1]):
                x3 = False
                break
        if x3:
            x0.append(x2)
    if len(x0) != count_:
        return None
    return tuple(x0)
