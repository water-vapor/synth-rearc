from __future__ import annotations

from synth_rearc.core import *

from .helpers import connected_dbff022c
from .helpers import hole_indices_dbff022c


def _shift_indices_dbff022c(
    indices: Indices,
    offset: IntegerTuple,
) -> Indices:
    return frozenset((i + offset[ZERO], j + offset[ONE]) for i, j in indices)


def _bbox_halo_dbff022c(
    indices: Indices,
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = dims
    x2 = max(ZERO, uppermost(indices) - ONE)
    x3 = max(ZERO, leftmost(indices) - ONE)
    x4 = min(x0 - ONE, lowermost(indices) + ONE)
    x5 = min(x1 - ONE, rightmost(indices) + ONE)
    return frozenset((i, j) for i in range(x2, x4 + ONE) for j in range(x3, x5 + ONE))


def _solid_rows_dbff022c(
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    for _ in range(200):
        x0 = choice(("rect", "left", "right", "double"))
        x1 = [ZERO]
        x2 = [width_value - ONE]
        for x3 in range(ONE, height_value):
            x4 = x1[-ONE]
            x5 = x2[-ONE]
            if x0 == "left":
                x4 = min(x5 - ONE, x4 + choice((ZERO, ZERO, ONE)))
            elif x0 == "right":
                x5 = max(x4 + ONE, x5 - choice((ZERO, ZERO, ONE)))
            elif x0 == "double":
                x4 = min(x5 - ONE, x4 + choice((ZERO, ZERO, ONE)))
                x5 = max(x4 + ONE, x5 - choice((ZERO, ZERO, ONE)))
            x1.append(x4)
            x2.append(x5)
        x6 = frozenset((i, j) for i, (x7, x8) in enumerate(zip(x1, x2)) for j in range(x7, x8 + ONE))
        if choice((T, F)):
            x6 = vmirror(x6)
        if choice((T, F)):
            x6 = hmirror(x6)
        x6 = normalize(x6)
        x9 = frozenset(
            (i, j)
            for i, j in x6
            if frozenset({(i - ONE, j), (i + ONE, j), (i, j - ONE), (i, j + ONE)}) <= x6
        )
        if len(x9) > ZERO:
            return x6
    raise RuntimeError("failed to create solid dbff022c shape")


def _interior_cells_dbff022c(
    solid: Indices,
) -> Indices:
    return frozenset(
        (i, j)
        for i, j in solid
        if frozenset({(i - ONE, j), (i + ONE, j), (i, j - ONE), (i, j + ONE)}) <= solid
    )


def _rect_hole_candidates_dbff022c(
    interior: Indices,
) -> tuple[Indices, ...]:
    if len(interior) == ZERO:
        return tuple()
    x0 = []
    x1 = uppermost(interior)
    x2 = lowermost(interior)
    x3 = leftmost(interior)
    x4 = rightmost(interior)
    for x5 in range(x1, x2 + ONE):
        for x6 in range(x3, x4 + ONE):
            for x7 in range(ONE, x2 - x5 + TWO):
                for x8 in range(ONE, x4 - x6 + TWO):
                    x9 = frozenset((i, j) for i in range(x5, x5 + x7) for j in range(x6, x6 + x8))
                    if x9 <= interior:
                        x0.append(x9)
    return tuple(sorted(x0, key=lambda patch: (size(patch), height(patch), width(patch))))


def _grow_hole_dbff022c(
    interior: Indices,
    size_cap: Integer,
) -> Indices:
    x0 = choice(tuple(interior))
    x1 = {x0}
    x2 = [x0]
    x3 = randint(ONE, min(size_cap, len(interior)))
    while len(x1) < x3:
        x4 = frozenset(x5 for x6 in x2 for x5 in dneighbors(x6) if x5 in interior and x5 not in x1)
        if len(x4) == ZERO:
            break
        x5 = choice(tuple(x4))
        x1.add(x5)
        x2.append(x5)
    return frozenset(x1)


def _choose_holes_dbff022c(
    solid: Indices,
) -> tuple[Indices, ...]:
    x0 = _interior_cells_dbff022c(solid)
    x1 = list(sorted(x0))
    x2 = _rect_hole_candidates_dbff022c(x0)
    for _ in range(200):
        x3 = choice(("rect", "points", "cluster", "mixed"))
        if x3 == "rect" and len(x2) > ZERO:
            x4 = choice(x2)
            x5 = (x4,)
        elif x3 == "points":
            x4 = min(choice((ONE, TWO, TWO, THREE)), len(x1))
            x6 = []
            x7 = list(x1)
            shuffle(x7)
            for x8 in x7:
                if all(manhattan(frozenset({x8}), frozenset({x9})) > ONE for x9 in x6):
                    x6.append(x8)
                if len(x6) == x4:
                    break
            x5 = tuple(frozenset({x8}) for x8 in x6)
        elif x3 == "cluster":
            x5 = (_grow_hole_dbff022c(x0, FOUR),)
        else:
            x4 = _grow_hole_dbff022c(x0, THREE)
            x6 = tuple(x7 for x7 in x1 if manhattan(frozenset({x7}), x4) > ONE)
            x5 = (x4,) if len(x6) == ZERO else (x4, frozenset({choice(x6)}))
        x8 = merge(x5) if len(x5) > ZERO else frozenset()
        if len(x8) == ZERO:
            continue
        x9 = difference(solid, x8)
        if not connected_dbff022c(x9):
            continue
        if hole_indices_dbff022c(x9) != x8:
            continue
        return tuple(sorted(x5, key=lambda patch: (size(patch), uppermost(patch), leftmost(patch))))
    raise RuntimeError("failed to carve dbff022c holes")


def _legend_pair_count_dbff022c(
    dims: IntegerTuple,
    side: str,
    mapped_count: Integer,
) -> Integer:
    x0, x1 = dims
    x2 = min(FIVE, subtract(x0, TWO)) if side == "left-top" else min(FIVE, subtract(x1, TWO))
    x3 = max(mapped_count, THREE) if side == "left-top" else max(mapped_count, TWO)
    return randint(x3, x2)


def _mapped_indices_dbff022c(
    count: Integer,
    mapped_count: Integer,
) -> tuple[Integer, ...]:
    x0 = list(range(count))
    shuffle(x0)
    return tuple(sorted(x0[:mapped_count]))


def _shape_spec_dbff022c() -> tuple[Indices, tuple[Indices, ...], Indices]:
    for _ in range(200):
        x0 = randint(THREE, SIX)
        x1 = randint(THREE, SIX)
        x2 = _solid_rows_dbff022c(x0, x1)
        x3 = _choose_holes_dbff022c(x2)
        x4 = difference(x2, merge(x3))
        if len(x4) == ZERO:
            continue
        return x2, x3, x4
    raise RuntimeError("failed to create dbff022c shape spec")


def _place_patch_dbff022c(
    dims: IntegerTuple,
    occupied: set[IntegerTuple],
    patch: Indices,
) -> IntegerTuple | None:
    x0, x1 = dims
    x2 = height(patch)
    x3 = width(patch)
    for _ in range(400):
        x4 = randint(ZERO, x0 - x2)
        x5 = randint(ZERO, x1 - x3)
        x6 = _shift_indices_dbff022c(patch, (x4, x5))
        x7 = _bbox_halo_dbff022c(x6, dims)
        if x7 & occupied:
            continue
        return (x4, x5)
    return None


def _legend_indices_dbff022c(
    dims: IntegerTuple,
    side: str,
    count: Integer,
) -> tuple[tuple[IntegerTuple, ...], tuple[IntegerTuple, ...]]:
    x0, x1 = dims
    if side == "top-left":
        x2 = tuple((ZERO, j) for j in range(count))
        x3 = tuple((ONE, j) for j in range(count))
        return x2, x3
    if side == "top-right":
        x2 = tuple((ZERO, j) for j in range(x1 - count, x1))
        x3 = tuple((ONE, j) for j in range(x1 - count, x1))
        return x2, x3
    if side == "bottom-left":
        x2 = tuple((x0 - ONE, j) for j in range(count))
        x3 = tuple((x0 - TWO, j) for j in range(count))
        return x2, x3
    x2 = tuple((i, ZERO) for i in range(count))
    x3 = tuple((i, ONE) for i in range(count))
    return x2, x3


def _paint_pairs_dbff022c(
    grid: Grid,
    source_cells: tuple[IntegerTuple, ...],
    target_cells: tuple[IntegerTuple, ...],
    pairs: tuple[tuple[Integer, Integer], ...],
) -> Grid:
    x0 = grid
    for x1, x2, (x3, x4) in zip(source_cells, target_cells, pairs):
        x0 = fill(x0, x3, frozenset({x1}))
        x0 = fill(x0, x4, frozenset({x2}))
    return x0


def generate_dbff022c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = randint(10, 18)
        x1 = randint(10, 18)
        x2 = (x0, x1)
        x3 = canvas(ZERO, x2)
        x4 = choice(("top-left", "top-right", "bottom-left", "left-top"))
        x5 = randint(TWO, FOUR)
        x6 = _mapped_indices_dbff022c(x5, randint(ONE, x5))
        x7 = _legend_pair_count_dbff022c(x2, x4, len(x6))
        x8, x9 = _legend_indices_dbff022c(x2, x4, x7)
        x10 = frozenset(x8) | frozenset(x9)
        x11 = set(_bbox_halo_dbff022c(x10, x2))
        x12 = tuple(_shape_spec_dbff022c() for _ in range(x5))
        x13 = [x14 for x14 in range(ONE, TEN)]
        shuffle(x13)
        x14 = tuple(x13[:x5])
        x15 = set(x14[i] for i in x6)
        x16 = [x17 for x17 in range(ONE, TEN) if x17 not in x14]
        shuffle(x16)
        if len(x16) < x7 - len(x15):
            continue
        x17 = list(x15) + x16[: x7 - len(x15)]
        shuffle(x17)
        x18 = {}
        x19 = [x20 for x20 in range(ONE, TEN)]
        shuffle(x19)
        for x20 in x17:
            if x20 in x15 and choice((T, F, F)):
                x18[x20] = x20
            else:
                x18[x20] = choice(x19)
        x21 = tuple((x20, x18[x20]) for x20 in x17)
        x22 = []
        x23 = x3
        x24 = x3
        x25 = set(x11)
        for x26, (x27, x28, x29) in zip(x14, x12):
            x30 = _place_patch_dbff022c(x2, x25, x29)
            if x30 is None:
                x22 = []
                break
            x31 = _shift_indices_dbff022c(x27, x30)
            x32 = tuple(_shift_indices_dbff022c(x33, x30) for x33 in x28)
            x33 = _shift_indices_dbff022c(x29, x30)
            x34 = merge(x32)
            x23 = fill(x23, x26, x33)
            x24 = fill(x24, x26, x33)
            if x26 in x18:
                x24 = fill(x24, x18[x26], x34)
            x25 |= set(_bbox_halo_dbff022c(x31, x2))
            x22.append((x26, x31, x32))
        if len(x22) != x5:
            continue
        x23 = _paint_pairs_dbff022c(x23, x8, x9, x21)
        x24 = _paint_pairs_dbff022c(x24, x8, x9, x21)
        if x23 == x24:
            continue
        return {"input": x23, "output": x24}
