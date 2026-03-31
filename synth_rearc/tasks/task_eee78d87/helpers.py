from __future__ import annotations

from itertools import product as cartesian_product

from synth_rearc.core import *


FULL_LINE_COORDS_EEE78D87 = frozenset({0, 3, 6, 9, 12, 15})
CENTER_LINE_COORDS_EEE78D87 = frozenset({6, 9})


def _feature_patch_eee78d87(
    rows: range,
    cols: range,
    line_rows: frozenset[Integer],
    line_cols: frozenset[Integer],
    *,
    row_is_line: bool,
    col_is_line: bool,
) -> Indices:
    return frozenset(
        (i, j)
        for i in rows
        for j in cols
        if (i in line_rows) == row_is_line and (j in line_cols) == col_is_line
    )


FULL_FEATURE_PATCHES_EEE78D87 = (
    _feature_patch_eee78d87(range(16), range(16), FULL_LINE_COORDS_EEE78D87, FULL_LINE_COORDS_EEE78D87, row_is_line=F, col_is_line=F),
    _feature_patch_eee78d87(range(16), range(16), FULL_LINE_COORDS_EEE78D87, FULL_LINE_COORDS_EEE78D87, row_is_line=F, col_is_line=T),
    _feature_patch_eee78d87(range(16), range(16), FULL_LINE_COORDS_EEE78D87, FULL_LINE_COORDS_EEE78D87, row_is_line=T, col_is_line=F),
    _feature_patch_eee78d87(range(16), range(16), FULL_LINE_COORDS_EEE78D87, FULL_LINE_COORDS_EEE78D87, row_is_line=T, col_is_line=T),
)

CENTER_FEATURE_PATCHES_EEE78D87 = (
    _feature_patch_eee78d87(range(5, 11), range(5, 11), CENTER_LINE_COORDS_EEE78D87, CENTER_LINE_COORDS_EEE78D87, row_is_line=F, col_is_line=F),
    _feature_patch_eee78d87(range(5, 11), range(5, 11), CENTER_LINE_COORDS_EEE78D87, CENTER_LINE_COORDS_EEE78D87, row_is_line=F, col_is_line=T),
    _feature_patch_eee78d87(range(5, 11), range(5, 11), CENTER_LINE_COORDS_EEE78D87, CENTER_LINE_COORDS_EEE78D87, row_is_line=T, col_is_line=F),
    _feature_patch_eee78d87(range(5, 11), range(5, 11), CENTER_LINE_COORDS_EEE78D87, CENTER_LINE_COORDS_EEE78D87, row_is_line=T, col_is_line=T),
)


def _valid_pattern_bits_eee78d87(
    bits: tuple[bool, bool, bool, bool],
) -> bool:
    corners_on, vertical_on, horizontal_on, _ = bits
    x0 = any(bits)
    x1 = all(bits)
    x2 = corners_on or vertical_on
    x3 = corners_on or horizontal_on
    return x0 and not x1 and x2 and x3


VALID_PATTERN_BITS_EEE78D87 = tuple(
    bits
    for bits in cartesian_product((F, T), repeat=4)
    if _valid_pattern_bits_eee78d87(bits)
)

PATTERN_BITS_BY_ACTIVE_COUNT_EEE78D87 = {
    count: tuple(bits for bits in VALID_PATTERN_BITS_EEE78D87 if sum(bits) == count)
    for count in range(1, 4)
}


def pattern_bits_from_stencil_eee78d87(
    stencil: Grid,
    bg_color: Integer,
) -> tuple[bool, bool, bool, bool]:
    x0 = any(stencil[i][j] != bg_color for i, j in ((0, 0), (0, 2), (2, 0), (2, 2)))
    x1 = any(stencil[i][1] != bg_color for i in (0, 2))
    x2 = any(stencil[1][j] != bg_color for j in (0, 2))
    x3 = stencil[1][1] != bg_color
    return (x0, x1, x2, x3)


def pattern_patch_eee78d87(
    bits: tuple[bool, bool, bool, bool],
) -> Indices:
    corners_on, vertical_on, horizontal_on, center_on = bits
    cells = set()
    if corners_on:
        cells.update({(0, 0), (0, 2), (2, 0), (2, 2)})
    if vertical_on:
        cells.update({(0, 1), (2, 1)})
    if horizontal_on:
        cells.update({(1, 0), (1, 2)})
    if center_on:
        cells.add((1, 1))
    return frozenset(cells)


def render_output_from_bits_eee78d87(
    bits: tuple[bool, bool, bool, bool],
    bg_color: Integer = SEVEN,
) -> Grid:
    x0 = canvas(ZERO, (16, 16))
    x1 = x0
    for bit, patch in zip(bits, CENTER_FEATURE_PATCHES_EEE78D87):
        if bit:
            x1 = fill(x1, NINE, patch)
    for bit, patch in zip(bits, FULL_FEATURE_PATCHES_EEE78D87):
        if not bit:
            x1 = fill(x1, bg_color, patch)
    return x1
