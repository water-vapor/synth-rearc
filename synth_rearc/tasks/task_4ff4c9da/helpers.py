from synth_rearc.core import *


def _full_rows_4ff4c9da(
    grid: Grid,
    value: Integer,
) -> tuple[int, ...]:
    return tuple(i for i, row in enumerate(grid) if all(cell == value for cell in row))


def _full_cols_4ff4c9da(
    grid: Grid,
    value: Integer,
) -> tuple[int, ...]:
    h = len(grid)
    w = len(grid[ZERO])
    return tuple(j for j in range(w) if all(grid[i][j] == value for i in range(h)))


def _bands_4ff4c9da(
    indices: tuple[int, ...],
    limit: Integer,
) -> tuple[tuple[int, int], ...]:
    x0 = (-ONE,) + indices + (limit,)
    return tuple((a + ONE, b) for a, b in zip(x0, x0[ONE:]) if b - a > ONE)


def _row_bands_4ff4c9da(grid: Grid) -> tuple[tuple[int, int], ...]:
    x0 = mostcolor(grid)
    x1 = _full_rows_4ff4c9da(grid, x0)
    x2 = _bands_4ff4c9da(x1, len(grid))
    return x2


def _col_bands_4ff4c9da(grid: Grid) -> tuple[tuple[int, int], ...]:
    x0 = mostcolor(grid)
    x1 = _full_cols_4ff4c9da(grid, x0)
    x2 = _bands_4ff4c9da(x1, len(grid[ZERO]))
    return x2


def _normalize_patch_4ff4c9da(
    patch: Indices,
) -> Indices:
    if len(patch) == ZERO:
        return frozenset()
    return frozenset(normalize(patch))


def _tile_signature_4ff4c9da(
    tile: Grid,
    separator: Integer,
) -> tuple[Indices, Indices, Indices]:
    x0 = frozenset(
        (i, j)
        for i, row in enumerate(tile)
        for j, value in enumerate(row)
        if value == EIGHT
    )
    x1 = frozenset(
        (i, j)
        for i, row in enumerate(tile)
        for j, value in enumerate(row)
        if value not in (ZERO, EIGHT, separator)
    )
    x2 = _normalize_patch_4ff4c9da(x0)
    x3 = _normalize_patch_4ff4c9da(x1)
    return x2, x1, x3


def _render_template_4ff4c9da(
    template: tuple[str, ...],
    separator: Integer,
    accent: Integer,
) -> Grid:
    x0 = {
        "0": ZERO,
        "s": separator,
        "a": accent,
        "8": EIGHT,
    }
    return tuple(tuple(x0[cell] for cell in row) for row in template)


def _assemble_tiles_4ff4c9da(
    tiles: tuple[tuple[Grid, ...], ...],
    separator: Integer,
) -> Grid:
    x0 = []
    for row in tiles:
        x1 = row[ZERO]
        for tile in row[ONE:]:
            x2 = canvas(separator, (height(x1), ONE))
            x1 = hconcat(x1, x2)
            x1 = hconcat(x1, tile)
        x0.append(x1)
    x3 = x0[ZERO]
    for row in x0[ONE:]:
        x4 = canvas(separator, (ONE, width(x3)))
        x3 = vconcat(x3, x4)
        x3 = vconcat(x3, row)
    return x3
