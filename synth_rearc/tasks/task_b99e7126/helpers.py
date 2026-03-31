from __future__ import annotations

from synth_rearc.core import *


LOGICAL_SIZE_B99E7126 = SEVEN
TILE_SIZE_B99E7126 = THREE
STRIDE_B99E7126 = FOUR
GRID_SIZE_B99E7126 = 29

BACKGROUND_MASK_PROTOTYPES_B99E7126 = (
    ((ZERO, ZERO, ZERO), (ZERO, ONE, ZERO), (ZERO, ZERO, ZERO)),
    ((ONE, ONE, ONE), (ZERO, ONE, ZERO), (ONE, ONE, ONE)),
    ((ONE, ZERO, ONE), (ZERO, ONE, ZERO), (ONE, ZERO, ONE)),
    ((ONE, ZERO, ONE), (ZERO, ZERO, ZERO), (ONE, ONE, ONE)),
)

SPECIAL_MASK_PROTOTYPES_B99E7126 = (
    ((ONE, ZERO, ONE), (ONE, ZERO, ONE), (ONE, ONE, ONE)),
    ((ONE, ZERO, ONE), (ONE, ONE, ONE), (ONE, ZERO, ONE)),
    ((ZERO, ONE, ZERO), (ONE, ONE, ONE), (ONE, ZERO, ONE)),
    ((ZERO, ONE, ZERO), (ONE, ZERO, ONE), (ONE, ONE, ONE)),
)


def _d4_variants_b99e7126(
    mask: tuple[tuple[Integer, ...], ...],
) -> tuple[tuple[tuple[Integer, ...], ...], ...]:
    out: list[tuple[tuple[Integer, ...], ...]] = []
    cur = mask
    for _ in range(FOUR):
        for cand in (cur, vmirror(cur)):
            if cand not in out:
                out.append(cand)
        cur = rot90(cur)
    return tuple(out)


def mask_indices_b99e7126(
    mask: tuple[tuple[Integer, ...], ...],
) -> Indices:
    return frozenset((i, j) for i, row in enumerate(mask) for j, value in enumerate(row) if value == ONE)


def shift_indices_b99e7126(
    indices: Indices,
    offset: IntegerTuple,
) -> Indices:
    di, dj = offset
    return frozenset((i + di, j + dj) for i, j in indices)


def _subset_occurrences_b99e7126(
    mask_indices: Indices,
    subset: Indices,
) -> Integer:
    count = ZERO
    for di in range(-TWO, THREE):
        for dj in range(-TWO, THREE):
            shifted = shift_indices_b99e7126(subset, (di, dj))
            if all(ZERO <= i < THREE and ZERO <= j < THREE for i, j in shifted) and shifted.issubset(mask_indices):
                count += ONE
    return count


def seed_bands_b99e7126(
    mask: tuple[tuple[Integer, ...], ...],
) -> tuple[Indices, ...]:
    mask_indices = mask_indices_b99e7126(mask)
    candidates: list[Indices] = []
    for start in range(THREE):
        for span in (ONE, TWO):
            rows = set(range(start, min(THREE, start + span)))
            row_band = frozenset((i, j) for i, j in mask_indices if i in rows)
            if THREE <= len(row_band) <= FOUR and row_band != mask_indices:
                if _subset_occurrences_b99e7126(mask_indices, row_band) == ONE and row_band not in candidates:
                    candidates.append(row_band)
            cols = set(range(start, min(THREE, start + span)))
            col_band = frozenset((i, j) for i, j in mask_indices if j in cols)
            if THREE <= len(col_band) <= FOUR and col_band != mask_indices:
                if _subset_occurrences_b99e7126(mask_indices, col_band) == ONE and col_band not in candidates:
                    candidates.append(col_band)
    return tuple(candidates)


def _mask_bank_b99e7126(
    prototypes: tuple[tuple[tuple[Integer, ...], ...], ...],
) -> tuple[tuple[tuple[Integer, ...], ...], ...]:
    out: list[tuple[tuple[Integer, ...], ...]] = []
    for proto in prototypes:
        for variant in _d4_variants_b99e7126(proto):
            if variant not in out:
                out.append(variant)
    return tuple(out)


BACKGROUND_MASKS_B99E7126 = _mask_bank_b99e7126(BACKGROUND_MASK_PROTOTYPES_B99E7126)
SPECIAL_MASKS_B99E7126 = tuple(mask for mask in _mask_bank_b99e7126(SPECIAL_MASK_PROTOTYPES_B99E7126) if len(seed_bands_b99e7126(mask)) > ZERO)


def random_background_mask_b99e7126() -> tuple[tuple[Integer, ...], ...]:
    return choice(BACKGROUND_MASKS_B99E7126)


def random_special_mask_and_seed_b99e7126() -> tuple[tuple[tuple[Integer, ...], ...], Indices]:
    mask = choice(SPECIAL_MASKS_B99E7126)
    seed = choice(seed_bands_b99e7126(mask))
    return mask, seed


def make_background_tile_b99e7126(
    mask: tuple[tuple[Integer, ...], ...],
    keep_color: Integer,
    other_color: Integer,
) -> Grid:
    return tuple(
        tuple(keep_color if value == ONE else other_color for value in row)
        for row in mask
    )


def make_special_tile_b99e7126(
    mask: tuple[tuple[Integer, ...], ...],
    keep_color: Integer,
    special_color: Integer,
) -> Grid:
    return tuple(
        tuple(special_color if value == ONE else keep_color for value in row)
        for row in mask
    )


def render_grid_b99e7126(
    line_color: Integer,
    background_tile: Grid,
    special_tile: Grid,
    special_positions: Indices,
) -> Grid:
    grid = [list(row) for row in canvas(line_color, (GRID_SIZE_B99E7126, GRID_SIZE_B99E7126))]
    for i in range(LOGICAL_SIZE_B99E7126):
        for j in range(LOGICAL_SIZE_B99E7126):
            tile = special_tile if (i, j) in special_positions else background_tile
            top = ONE + STRIDE_B99E7126 * i
            left = ONE + STRIDE_B99E7126 * j
            for di in range(TILE_SIZE_B99E7126):
                for dj in range(TILE_SIZE_B99E7126):
                    grid[top + di][left + dj] = tile[di][dj]
    return tuple(tuple(row) for row in grid)
