from __future__ import annotations

from synth_rearc.core import *


SIDE_TO_APPROACH_8B9C3697 = {
    "top": (ONE, ZERO),
    "bottom": (-ONE, ZERO),
    "left": (ZERO, ONE),
    "right": (ZERO, -ONE),
}

SIDE_TO_OUTWARD_8B9C3697 = {
    "top": (-ONE, ZERO),
    "bottom": (ONE, ZERO),
    "left": (ZERO, -ONE),
    "right": (ZERO, ONE),
}


def patch_sort_key_8b9c3697(
    patch: Patch,
) -> tuple[int, int, int, int]:
    x0 = toindices(patch)
    return (uppermost(x0), leftmost(x0), lowermost(x0), rightmost(x0))


def rectangle_patch_8b9c3697(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    return frozenset(
        (i, j)
        for i in range(top, top + height_value)
        for j in range(left, left + width_value)
    )


def scale_vector_8b9c3697(
    direction: IntegerTuple,
    amount: Integer,
) -> IntegerTuple:
    return (direction[ZERO] * amount, direction[ONE] * amount)


def normalize_pair_8b9c3697(
    first: Patch,
    second: Patch,
) -> tuple[Indices, Indices]:
    x0 = toindices(first) | toindices(second)
    x1 = invert(ulcorner(x0))
    return shift(toindices(first), x1), shift(toindices(second), x1)


def rotate90_patch_8b9c3697(
    patch: Patch,
) -> Indices:
    x0 = normalize(toindices(patch))
    x1 = height(x0)
    return frozenset((j, x1 - ONE - i) for i, j in x0)


def rotate_patch_8b9c3697(
    patch: Patch,
    turns: Integer,
) -> Indices:
    x0 = normalize(toindices(patch))
    for _ in range(turns % FOUR):
        x0 = rotate90_patch_8b9c3697(x0)
    return normalize(x0)


def canonical_shape_a_8b9c3697(
    arm_width: Integer,
    gap_width: Integer,
) -> tuple[Indices, Indices]:
    x0 = add(add(arm_width, double(gap_width)), FOUR)
    x1 = rectangle_patch_8b9c3697(ZERO, ZERO, ONE, x0)
    x2 = rectangle_patch_8b9c3697(ONE, ONE, THREE, ONE)
    x3 = rectangle_patch_8b9c3697(ONE, subtract(x0, TWO), THREE, ONE)
    x4 = add(gap_width, TWO)
    x5 = rectangle_patch_8b9c3697(ONE, x4, ONE, arm_width)
    x6 = rectangle_patch_8b9c3697(TWO, x4, ONE, arm_width)
    x7 = x1 | x2 | x3 | x5
    return x7, x6


def canonical_shape_b_8b9c3697(
    arm_width: Integer,
    gap_width: Integer,
) -> tuple[Indices, Indices]:
    x0 = add(add(arm_width, double(gap_width)), FOUR)
    x1 = rectangle_patch_8b9c3697(ZERO, ONE, THREE, ONE)
    x2 = rectangle_patch_8b9c3697(ZERO, subtract(x0, TWO), THREE, ONE)
    x3 = add(gap_width, TWO)
    x4 = rectangle_patch_8b9c3697(TWO, x3, ONE, arm_width)
    x5 = rectangle_patch_8b9c3697(THREE, ZERO, ONE, x0)
    x6 = rectangle_patch_8b9c3697(ZERO, x3, TWO, arm_width)
    x7 = x1 | x2 | x4 | x5
    return x7, x6


def oriented_shape_8b9c3697(
    kind: str,
    side: str,
    arm_width: Integer,
    gap_width: Integer,
) -> tuple[Indices, Indices]:
    if kind == "a":
        x0, x1 = canonical_shape_a_8b9c3697(arm_width, gap_width)
        x2 = {"bottom": ZERO, "right": ONE, "top": TWO, "left": THREE}[side]
    else:
        x0, x1 = canonical_shape_b_8b9c3697(arm_width, gap_width)
        x2 = {"top": ZERO, "right": ONE, "bottom": TWO, "left": THREE}[side]
    x3 = rotate_patch_8b9c3697(x0, x2)
    x4 = rotate_patch_8b9c3697(x1, x2)
    return normalize_pair_8b9c3697(x3, x4)


def _touching_sides_8b9c3697(
    patch: Patch,
    bounds: tuple[int, int, int, int],
) -> tuple[str, ...]:
    x0 = toindices(patch)
    x1, x2, x3, x4 = bounds
    x5 = []
    if any(i == x1 for i, _ in x0):
        x5.append("top")
    if any(i == x3 for i, _ in x0):
        x5.append("bottom")
    if any(j == x2 for _, j in x0):
        x5.append("left")
    if any(j == x4 for _, j in x0):
        x5.append("right")
    return tuple(x5)


def single_side_cavity_8b9c3697(
    patch: Patch,
) -> tuple[str, Indices] | None:
    x0 = toindices(patch)
    x1 = delta(x0)
    if len(x1) == ZERO:
        return None
    x2 = (
        uppermost(x0),
        leftmost(x0),
        lowermost(x0),
        rightmost(x0),
    )
    x3 = set()
    x4 = []
    for cell in x1:
        if cell in x3:
            continue
        x5 = [cell]
        x3.add(cell)
        x6 = set()
        while x5:
            x7 = x5.pop()
            x6.add(x7)
            for x8 in dneighbors(x7):
                if x8 in x1 and x8 not in x3:
                    x3.add(x8)
                    x5.append(x8)
        x9 = _touching_sides_8b9c3697(frozenset(x6), x2)
        if len(x9) == ONE:
            x4.append((x9[ZERO], frozenset(x6)))
    if len(x4) != ONE:
        return None
    return x4[ZERO]


def _overlap_8b9c3697(
    a0: Integer,
    a1: Integer,
    b0: Integer,
    b1: Integer,
) -> Boolean:
    return not (a1 < b0 or a0 > b1)


def candidate_route_8b9c3697(
    marker: Patch,
    shape_patch: Patch,
) -> tuple[IntegerTuple, Integer, Indices] | None:
    x0 = toindices(marker)
    x1 = toindices(shape_patch)
    x2 = single_side_cavity_8b9c3697(x1)
    if x2 is None:
        return None
    x3, x4 = x2
    x5, x6, x7, x8 = (
        uppermost(x0),
        leftmost(x0),
        lowermost(x0),
        rightmost(x0),
    )
    x9, x10, x11, x12 = (
        uppermost(x1),
        leftmost(x1),
        lowermost(x1),
        rightmost(x1),
    )
    if x3 == "top":
        x13 = both(x7 < x9, _overlap_8b9c3697(x6, x8, x10, x12))
    elif x3 == "bottom":
        x13 = both(x5 > x11, _overlap_8b9c3697(x6, x8, x10, x12))
    elif x3 == "left":
        x13 = both(x8 < x10, _overlap_8b9c3697(x5, x7, x9, x11))
    else:
        x13 = both(x6 > x12, _overlap_8b9c3697(x5, x7, x9, x11))
    if not x13:
        return None
    x14 = SIDE_TO_APPROACH_8B9C3697[x3]
    x15 = x0
    x16 = ZERO
    while not adjacent(x15, x1):
        x16 = increment(x16)
        x15 = shift(x15, x14)
        if x16 > 42:
            return None
        if len(intersection(x15, x1)) != ZERO:
            return None
    if not x15 <= x4:
        return None
    return x14, x16, x15


def route_specs_8b9c3697(
    grid: Grid,
) -> tuple[tuple[Indices, IntegerTuple, Integer, Indices], ...]:
    x0 = objects(grid, T, F, T)
    x1 = tuple(
        sorted(
            (toindices(x2) for x2 in colorfilter(x0, TWO)),
            key=patch_sort_key_8b9c3697,
        )
    )
    x3 = tuple(
        sorted(
            (toindices(x4) for x4 in x0 if color(x4) != TWO),
            key=patch_sort_key_8b9c3697,
        )
    )
    x5 = []
    for x6 in x1:
        x7 = []
        for x8 in x3:
            x9 = candidate_route_8b9c3697(x6, x8)
            if x9 is not None:
                x7.append((x6, x9[ZERO], x9[ONE], x9[TWO]))
        if len(x7) == ONE:
            x5.append(x7[ZERO])
    return tuple(sorted(x5, key=lambda x10: patch_sort_key_8b9c3697(x10[ZERO])))


def erase_markers_8b9c3697(
    grid: Grid,
) -> Grid:
    x0 = objects(grid, T, F, T)
    x1 = colorfilter(x0, TWO)
    x2 = frozenset()
    for x3 in x1:
        x2 = x2 | toindices(x3)
    return fill(grid, mostcolor(grid), x2)


def paint_routes_8b9c3697(
    grid: Grid,
    routes: tuple[tuple[Indices, IntegerTuple, Integer, Indices], ...],
) -> Grid:
    x0 = grid
    for x1, x2, x3, x4 in routes:
        for x5 in range(x3):
            x6 = scale_vector_8b9c3697(x2, x5)
            x7 = shift(x1, x6)
            x0 = fill(x0, ZERO, x7)
        x0 = fill(x0, TWO, x4)
    return x0


def apply_rule_8b9c3697(
    grid: Grid,
) -> Grid:
    x0 = route_specs_8b9c3697(grid)
    x1 = erase_markers_8b9c3697(grid)
    return paint_routes_8b9c3697(x1, x0)
