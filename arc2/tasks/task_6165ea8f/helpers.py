from typing import Sequence

from arc2.core import *


TABLE_STEP_6165EA8F = THREE
INPUT_COLORS_6165EA8F = (ONE, THREE, FOUR, SIX, SEVEN, EIGHT, NINE)


def block_patch_6165ea8f(
    row_block: Integer,
    col_block: Integer,
) -> Indices:
    top = TABLE_STEP_6165EA8F * row_block
    left = TABLE_STEP_6165EA8F * col_block
    return frozenset(
        (top + di, left + dj)
        for di in range(TWO)
        for dj in range(TWO)
    )


def normalize_patch_6165ea8f(
    patch: Patch,
) -> Indices:
    x0 = toindices(patch)
    if len(x0) == ZERO:
        return frozenset()
    return frozenset(normalize(x0))


def rot90_patch_6165ea8f(
    patch: Patch,
) -> Indices:
    x0 = normalize_patch_6165ea8f(patch)
    x1 = height(x0)
    x2 = frozenset((j, x1 - ONE - i) for i, j in x0)
    return normalize_patch_6165ea8f(x2)


def dihedral_variants_6165ea8f(
    patch: Patch,
) -> tuple[Indices, ...]:
    x0 = normalize_patch_6165ea8f(patch)
    x1 = []
    x2 = x0
    for _ in range(FOUR):
        x1.append(x2)
        x1.append(normalize_patch_6165ea8f(vmirror(x2)))
        x2 = rot90_patch_6165ea8f(x2)
    x3 = []
    x4 = set()
    for x5 in x1:
        x6 = tuple(sorted(x5))
        if x6 in x4:
            continue
        x4.add(x6)
        x3.append(x5)
    return tuple(x3)


def shape_signature_6165ea8f(
    patch: Patch,
) -> tuple[IntegerTuple, ...]:
    return min(tuple(sorted(x0)) for x0 in dihedral_variants_6165ea8f(patch))


def transform_patch_6165ea8f(
    patch: Patch,
    turns: Integer,
    mirrored: Boolean,
) -> Indices:
    x0 = normalize_patch_6165ea8f(patch)
    for _ in range(turns % FOUR):
        x0 = rot90_patch_6165ea8f(x0)
    if mirrored:
        x0 = normalize_patch_6165ea8f(vmirror(x0))
    return x0


def render_table_6165ea8f(
    colors: Sequence[Integer],
    signatures: Sequence[tuple[IntegerTuple, ...]],
) -> Grid:
    ncolors = len(colors)
    dims = (
        TABLE_STEP_6165EA8F * ncolors + TWO,
        TABLE_STEP_6165EA8F * ncolors + TWO,
    )
    grid = canvas(ZERO, dims)
    for idx, value in enumerate(colors):
        grid = fill(grid, value, block_patch_6165ea8f(ZERO, idx + ONE))
        grid = fill(grid, value, block_patch_6165ea8f(idx + ONE, ZERO))
    for i, sig_i in enumerate(signatures):
        for j, sig_j in enumerate(signatures):
            if i == j:
                continue
            value = TWO if sig_i == sig_j else FIVE
            grid = fill(grid, value, block_patch_6165ea8f(i + ONE, j + ONE))
    return grid
