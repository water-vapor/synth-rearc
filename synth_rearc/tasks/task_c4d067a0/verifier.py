from __future__ import annotations

from math import gcd

from synth_rearc.core import *

from .helpers import paint_macro_c4d067a0


def _source_matrix_c4d067a0(
    grid: Grid,
    objs: Objects,
    bg: Integer,
) -> Grid:
    x0 = tuple(obj for obj in objs if size(obj) == ONE)
    x1 = tuple(sorted({uppermost(obj) for obj in x0}))
    x2 = tuple(sorted({leftmost(obj) for obj in x0}))
    x3 = {value: idx for idx, value in enumerate(x1)}
    x4 = {value: idx for idx, value in enumerate(x2)}
    x5 = [[bg for _ in x2] for _ in x1]
    for x6 in x0:
        x7 = x3[uppermost(x6)]
        x8 = x4[leftmost(x6)]
        x5[x7][x8] = color(x6)
    return tuple(tuple(row) for row in x5)


def _macro_blocks_c4d067a0(
    objs: Objects,
) -> tuple[Object, ...]:
    return tuple(
        sorted(
            (obj for obj in objs if size(obj) > ONE),
            key=lambda obj: (uppermost(obj), leftmost(obj)),
        )
    )


def _stride_c4d067a0(
    values: tuple[int, ...],
) -> Integer:
    x0 = tuple(
        values[idx + ONE] - values[idx]
        for idx in range(len(values) - ONE)
        if values[idx + ONE] - values[idx] > ZERO
    )
    if len(x0) == ZERO:
        raise ValueError("could not infer macro stride")
    x1 = x0[ZERO]
    for x2 in x0[ONE:]:
        x1 = gcd(x1, x2)
    return x1


def _match_segment_c4d067a0(
    matrix: Grid,
    colors_: tuple[int, ...],
) -> tuple[int, int]:
    x0 = len(colors_)
    x1 = []
    for x2, x3 in enumerate(matrix):
        for x4 in range(len(x3) - x0 + ONE):
            if x3[x4 : x4 + x0] == colors_:
                x1.append((x2, x4))
    if len(x1) != ONE:
        raise ValueError("macro row does not match a unique sparse segment")
    return x1[ZERO]


def _aligned_c4d067a0(
    blocks: tuple[Object, ...],
    matrix: Grid,
    top: Integer,
    left: Integer,
    stride: Integer,
) -> Boolean:
    x0 = len(matrix)
    x1 = len(matrix[ZERO])
    for x2 in blocks:
        x3 = uppermost(x2) - top
        x4 = leftmost(x2) - left
        if x3 % stride != ZERO or x4 % stride != ZERO:
            return False
        x5 = x3 // stride
        x6 = x4 // stride
        if not (ZERO <= x5 < x0 and ZERO <= x6 < x1):
            return False
        if matrix[x5][x6] != color(x2):
            return False
    return True


def verify_c4d067a0(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = objects(I, T, F, T)
    x2 = _source_matrix_c4d067a0(I, x1, x0)
    x3 = _macro_blocks_c4d067a0(x1)
    x4 = tuple(leftmost(obj) for obj in x3)
    x5 = _stride_c4d067a0(x4)
    x6 = tuple(color(obj) for obj in x3)
    x7, x8 = _match_segment_c4d067a0(x2, x6)
    x9 = uppermost(x3[ZERO]) - x7 * x5
    x10 = leftmost(x3[ZERO]) - x8 * x5
    if not _aligned_c4d067a0(x3, x2, x9, x10, x5):
        raise ValueError("macro blocks do not align with sparse source")
    x11 = height(x3[ZERO])
    x12 = paint_macro_c4d067a0(I, x2, x0, x9, x10, x5, x11)
    return x12
