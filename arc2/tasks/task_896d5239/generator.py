from arc2.core import *

from .helpers import (
    ORIENTS_896D5239,
    clipped_triangle_boundary_896d5239,
    clipped_triangle_cells_896d5239,
    triangle_cells_896d5239,
    visible_triangle_sides_896d5239,
)


GRID_HEIGHT_BOUNDS_896D5239 = (12, 18)
GRID_WIDTH_BOUNDS_896D5239 = (12, 18)
TRIANGLE_COUNT_BOUNDS_896D5239 = (TWO, THREE)
TRIANGLE_SIZE_BOUNDS_896D5239 = (TWO, THREE)
NOISE_COLORS_896D5239 = (ZERO, ONE)


def _chebyshev_896d5239(
    a: IntegerTuple,
    b: IntegerTuple,
) -> Integer:
    return max(abs(a[ZERO] - b[ZERO]), abs(a[ONE] - b[ONE]))


def _triangle_markers_896d5239(
    apex: IntegerTuple,
    radius: Integer,
    orient: str,
    dims: IntegerTuple,
) -> Indices | None:
    x0, x1 = visible_triangle_sides_896d5239(apex, radius, orient, dims)
    if len(x0) < len(x1):
        x0, x1 = x1, x0
    if len(x0) != radius + ONE:
        return None
    if len(x1) < TWO:
        return None
    x2 = ("double", "prefix")
    if radius == TWO and len(x1) == radius + ONE:
        x2 = x2 + ("vertices",)
    x3 = choice(x2)
    if x3 == "double":
        return frozenset(x0 + x1)
    if x3 == "vertices":
        return frozenset((x0[ZERO], x0[-ONE], x1[-ONE]))
    x4 = randint(TWO, len(x1))
    return frozenset(x0 + x1[:x4])


def _separated_896d5239(
    cells: Indices,
    marks: Indices,
    taken_cells: Indices,
    taken_marks: Indices,
) -> bool:
    if len(intersection(cells, taken_cells)) > ZERO:
        return False
    for x0 in cells:
        for x1 in taken_cells:
            if _chebyshev_896d5239(x0, x1) <= ONE:
                return False
    for x0 in marks:
        for x1 in taken_marks:
            if _chebyshev_896d5239(x0, x1) <= TWO:
                return False
    return True


def _sample_triangle_896d5239(
    dims: IntegerTuple,
    diff_lb: float,
    diff_ub: float,
    taken_cells: Indices,
    taken_marks: Indices,
) -> tuple[Indices, Indices] | None:
    x0 = dims
    x1 = max(dims)
    for _ in range(300):
        x2 = choice(ORIENTS_896D5239)
        x3 = unifint(diff_lb, diff_ub, TRIANGLE_SIZE_BOUNDS_896D5239)
        x4 = choice((F, F, T))
        x5 = (randint(ZERO, x0[ZERO] - ONE), randint(ZERO, x0[ONE] - ONE))
        x6 = triangle_cells_896d5239(x5, x3, x2)
        x7 = clipped_triangle_cells_896d5239(x5, x3, x2, x0)
        if len(x7) < SIX:
            continue
        x8 = len(x7) != len(x6)
        if x4 != x8:
            continue
        x9 = clipped_triangle_boundary_896d5239(x5, x3, x2, x0)
        if not len(x9) >= THREE:
            continue
        x10 = _triangle_markers_896d5239(x5, x3, x2, x0)
        if x10 is None:
            continue
        if not _separated_896d5239(x7, x10, taken_cells, taken_marks):
            continue
        return x7, x10
    return None


def generate_896d5239(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, GRID_HEIGHT_BOUNDS_896D5239)
        x1 = unifint(diff_lb, diff_ub, GRID_WIDTH_BOUNDS_896D5239)
        x2 = (x0, x1)
        x3 = unifint(diff_lb, diff_ub, TRIANGLE_COUNT_BOUNDS_896D5239)
        x4 = []
        x5 = frozenset()
        x6 = frozenset()
        for _ in range(x3):
            x7 = _sample_triangle_896d5239(x2, diff_lb, diff_ub, x5, x6)
            if x7 is None:
                break
            x8, x9 = x7
            x4.append(x7)
            x5 = combine(x5, x8)
            x6 = combine(x6, x9)
        if len(x4) != x3:
            continue
        x10 = tuple(tuple(choice(NOISE_COLORS_896D5239) for _ in range(x1)) for _ in range(x0))
        x11 = x10
        x12 = x10
        for x13, x14 in x4:
            x11 = fill(x11, THREE, x14)
            x15 = difference(x13, x14)
            x12 = fill(x12, EIGHT, x15)
        for x13, x14 in x4:
            x12 = fill(x12, THREE, x14)
        return {"input": x11, "output": x12}
