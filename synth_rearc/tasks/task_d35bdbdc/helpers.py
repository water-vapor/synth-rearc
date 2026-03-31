from __future__ import annotations

from collections import deque

from synth_rearc.core import *


def _patch_d35bdbdc(*cells: tuple[int, int]) -> Indices:
    return frozenset(cells)


NON_FIVE_COLORS_D35BDBDC = tuple(color for color in range(ONE, TEN) if color != FIVE)
GRID_DIMS_D35BDBDC = (TEN, TEN)


LAYOUT_FAMILIES_D35BDBDC = (
    {
        "kept_indices": (ZERO, TWO),
        "fives": _patch_d35bdbdc(
            (ONE, TWO), (ONE, THREE), (ONE, FOUR), (ONE, FIVE), (ONE, SIX),
            (TWO, ONE), (THREE, ONE), (FOUR, ZERO), (FIVE, ONE), (FIVE, SIX),
            (SIX, ONE), (SIX, TWO), (SIX, THREE), (SIX, FOUR), (SIX, FIVE),
        ),
        "motifs": (
            _patch_d35bdbdc(
                (ZERO, SEVEN), (ZERO, EIGHT), (ZERO, NINE),
                (ONE, SEVEN), (ONE, EIGHT), (ONE, NINE),
                (TWO, SEVEN), (TWO, EIGHT), (TWO, NINE),
            ),
            _patch_d35bdbdc(
                (THREE, TWO), (THREE, THREE), (THREE, FOUR),
                (FOUR, TWO), (FOUR, THREE), (FOUR, FOUR),
                (FIVE, TWO), (FIVE, THREE), (FIVE, FOUR),
            ),
            _patch_d35bdbdc(
                (FOUR, SEVEN), (FOUR, EIGHT), (FOUR, NINE),
                (FIVE, SEVEN), (FIVE, EIGHT), (FIVE, NINE),
                (SIX, SEVEN), (SIX, EIGHT), (SIX, NINE),
            ),
            _patch_d35bdbdc(
                (SEVEN, TWO), (SEVEN, THREE), (SEVEN, FOUR),
                (EIGHT, TWO), (EIGHT, THREE), (EIGHT, FOUR),
                (NINE, TWO), (NINE, THREE), (NINE, FOUR),
            ),
        ),
    },
    {
        "kept_indices": (TWO, THREE),
        "fives": _patch_d35bdbdc(
            (TWO, FOUR), (THREE, THREE), (THREE, FIVE), (THREE, SIX), (THREE, SEVEN),
            (THREE, EIGHT), (FOUR, FOUR), (FIVE, FIVE), (SIX, FOUR), (SEVEN, ONE),
            (SEVEN, THREE), (EIGHT, ONE), (EIGHT, TWO),
        ),
        "motifs": (
            _patch_d35bdbdc(
                (ZERO, ZERO), (ZERO, ONE), (ZERO, TWO),
                (ONE, ZERO), (ONE, ONE), (ONE, TWO),
                (TWO, ZERO), (TWO, ONE), (TWO, TWO),
            ),
            _patch_d35bdbdc(
                (ZERO, SIX), (ZERO, SEVEN), (ZERO, EIGHT),
                (ONE, SIX), (ONE, SEVEN), (ONE, EIGHT),
                (TWO, SIX), (TWO, SEVEN), (TWO, EIGHT),
            ),
            _patch_d35bdbdc(
                (FOUR, ZERO), (FOUR, ONE), (FOUR, TWO),
                (FIVE, ZERO), (FIVE, ONE), (FIVE, TWO),
                (SIX, ZERO), (SIX, ONE), (SIX, TWO),
            ),
            _patch_d35bdbdc(
                (FOUR, SEVEN), (FOUR, EIGHT), (FOUR, NINE),
                (FIVE, SEVEN), (FIVE, EIGHT), (FIVE, NINE),
                (SIX, SEVEN), (SIX, EIGHT), (SIX, NINE),
            ),
            _patch_d35bdbdc(
                (SEVEN, FOUR), (SEVEN, FIVE), (SEVEN, SIX),
                (EIGHT, FOUR), (EIGHT, FIVE), (EIGHT, SIX),
                (NINE, FOUR), (NINE, FIVE), (NINE, SIX),
            ),
        ),
    },
    {
        "kept_indices": (ZERO, FOUR),
        "fives": _patch_d35bdbdc(
            (TWO, FIVE), (THREE, ONE), (THREE, FOUR), (THREE, SIX), (FOUR, ONE),
            (FOUR, THREE), (FOUR, SEVEN), (FIVE, TWO), (FIVE, EIGHT), (SIX, EIGHT),
        ),
        "motifs": (
            _patch_d35bdbdc(
                (ZERO, ZERO), (ZERO, ONE), (ZERO, TWO),
                (ONE, ZERO), (ONE, ONE), (ONE, TWO),
                (TWO, ZERO), (TWO, ONE), (TWO, TWO),
            ),
            _patch_d35bdbdc(
                (ZERO, SEVEN), (ZERO, EIGHT), (ZERO, NINE),
                (ONE, SEVEN), (ONE, EIGHT), (ONE, NINE),
                (TWO, SEVEN), (TWO, EIGHT), (TWO, NINE),
            ),
            _patch_d35bdbdc(
                (FOUR, FOUR), (FOUR, FIVE), (FOUR, SIX),
                (FIVE, FOUR), (FIVE, FIVE), (FIVE, SIX),
                (SIX, FOUR), (SIX, FIVE), (SIX, SIX),
            ),
            _patch_d35bdbdc(
                (SEVEN, ZERO), (SEVEN, ONE), (SEVEN, TWO),
                (EIGHT, ZERO), (EIGHT, ONE), (EIGHT, TWO),
                (NINE, ZERO), (NINE, ONE), (NINE, TWO),
            ),
            _patch_d35bdbdc(
                (SEVEN, SEVEN), (SEVEN, EIGHT), (SEVEN, NINE),
                (EIGHT, SEVEN), (EIGHT, EIGHT), (EIGHT, NINE),
                (NINE, SEVEN), (NINE, EIGHT), (NINE, NINE),
            ),
        ),
    },
    {
        "kept_indices": (ZERO, FOUR),
        "fives": _patch_d35bdbdc(
            (THREE, SEVEN), (FOUR, SIX), (FIVE, SIX), (SIX, SIX), (SEVEN, SIX),
            (EIGHT, THREE), (EIGHT, FIVE), (NINE, ONE), (NINE, TWO), (NINE, FOUR),
        ),
        "motifs": (
            _patch_d35bdbdc((ZERO, SEVEN), (ONE, SIX), (ONE, SEVEN), (ONE, EIGHT), (TWO, SEVEN)),
            _patch_d35bdbdc((ONE, TWO), (TWO, ONE), (TWO, TWO), (TWO, THREE), (THREE, TWO)),
            _patch_d35bdbdc((FIVE, FOUR), (SIX, THREE), (SIX, FOUR), (SIX, FIVE), (SEVEN, FOUR)),
            _patch_d35bdbdc((FIVE, EIGHT), (SIX, SEVEN), (SIX, EIGHT), (SIX, NINE), (SEVEN, EIGHT)),
            _patch_d35bdbdc((SIX, ONE), (SEVEN, ZERO), (SEVEN, ONE), (SEVEN, TWO), (EIGHT, ONE)),
        ),
    },
    {
        "kept_indices": (ZERO, ONE),
        "fives": _patch_d35bdbdc(
            (ONE, TWO), (ONE, SIX), (TWO, TWO), (TWO, SIX), (THREE, THREE),
            (THREE, SIX), (THREE, SEVEN), (THREE, EIGHT), (THREE, NINE), (FOUR, TWO),
            (FOUR, NINE), (FIVE, ONE), (FIVE, SIX), (FIVE, SEVEN), (FIVE, EIGHT),
            (SIX, TWO), (SIX, SIX), (SEVEN, THREE), (SEVEN, SIX), (EIGHT, THREE),
            (EIGHT, FOUR), (EIGHT, FIVE), (EIGHT, SIX),
        ),
        "motifs": (
            _patch_d35bdbdc(
                (ZERO, THREE), (ZERO, FOUR), (ZERO, FIVE),
                (ONE, THREE), (ONE, FOUR), (ONE, FIVE),
                (TWO, THREE), (TWO, FOUR), (TWO, FIVE),
            ),
            _patch_d35bdbdc(
                (ZERO, SEVEN), (ZERO, EIGHT), (ZERO, NINE),
                (ONE, SEVEN), (ONE, EIGHT), (ONE, NINE),
                (TWO, SEVEN), (TWO, EIGHT), (TWO, NINE),
            ),
            _patch_d35bdbdc(
                (FOUR, THREE), (FOUR, FOUR), (FOUR, FIVE),
                (FIVE, THREE), (FIVE, FOUR), (FIVE, FIVE),
                (SIX, THREE), (SIX, FOUR), (SIX, FIVE),
            ),
            _patch_d35bdbdc(
                (SIX, SEVEN), (SIX, EIGHT), (SIX, NINE),
                (SEVEN, SEVEN), (SEVEN, EIGHT), (SEVEN, NINE),
                (EIGHT, SEVEN), (EIGHT, EIGHT), (EIGHT, NINE),
            ),
            _patch_d35bdbdc(
                (SEVEN, ZERO), (SEVEN, ONE), (SEVEN, TWO),
                (EIGHT, ZERO), (EIGHT, ONE), (EIGHT, TWO),
                (NINE, ZERO), (NINE, ONE), (NINE, TWO),
            ),
        ),
    },
    {
        "kept_indices": (ONE, FOUR),
        "fives": _patch_d35bdbdc(
            (THREE, ZERO), (THREE, ONE), (THREE, TWO), (THREE, THREE), (THREE, FOUR),
            (THREE, EIGHT), (FOUR, ZERO), (FOUR, FOUR), (FOUR, EIGHT), (FIVE, ZERO),
            (FIVE, FOUR), (FIVE, EIGHT), (SIX, ZERO), (SIX, FOUR), (SIX, NINE),
            (SEVEN, ONE), (SEVEN, TWO), (SEVEN, FOUR), (SEVEN, NINE), (EIGHT, FIVE),
            (EIGHT, SIX), (EIGHT, NINE), (NINE, SEVEN), (NINE, EIGHT),
        ),
        "motifs": (
            _patch_d35bdbdc(
                (ZERO, THREE), (ZERO, FOUR), (ZERO, FIVE),
                (ONE, THREE), (ONE, FOUR), (ONE, FIVE),
                (TWO, THREE), (TWO, FOUR), (TWO, FIVE),
            ),
            _patch_d35bdbdc(
                (ZERO, SEVEN), (ZERO, EIGHT), (ZERO, NINE),
                (ONE, SEVEN), (ONE, EIGHT), (ONE, NINE),
                (TWO, SEVEN), (TWO, EIGHT), (TWO, NINE),
            ),
            _patch_d35bdbdc(
                (FOUR, ONE), (FOUR, TWO), (FOUR, THREE),
                (FIVE, ONE), (FIVE, TWO), (FIVE, THREE),
                (SIX, ONE), (SIX, TWO), (SIX, THREE),
            ),
            _patch_d35bdbdc(
                (FIVE, FIVE), (FIVE, SIX), (FIVE, SEVEN),
                (SIX, FIVE), (SIX, SIX), (SIX, SEVEN),
                (SEVEN, FIVE), (SEVEN, SIX), (SEVEN, SEVEN),
            ),
            _patch_d35bdbdc(
                (EIGHT, ONE), (EIGHT, TWO), (EIGHT, THREE),
                (NINE, ONE), (NINE, TWO), (NINE, THREE),
            ),
        ),
    },
)


def _neighbors8_d35bdbdc(loc: tuple[int, int]) -> tuple[tuple[int, int], ...]:
    i, j = loc
    return tuple(
        (i + di, j + dj)
        for di in (-ONE, ZERO, ONE)
        for dj in (-ONE, ZERO, ONE)
        if not both(equality(di, ZERO), equality(dj, ZERO))
    )


def _component_cells_d35bdbdc(cells: Indices) -> tuple[Indices, ...]:
    x0 = set(cells)
    x1 = set()
    x2 = []
    for x3 in sorted(x0):
        if x3 in x1:
            continue
        x4 = {x3}
        x5 = [x3]
        while len(x5) > ZERO:
            x6 = x5.pop()
            for x7 in _neighbors8_d35bdbdc(x6):
                if x7 in x0 and x7 not in x4:
                    x4.add(x7)
                    x5.append(x7)
        x1 |= x4
        x2.append(frozenset(x4))
    return tuple(sorted(x2, key=ulcorner))


def _extract_components_d35bdbdc(grid: Grid) -> tuple[Indices, ...]:
    h = len(grid)
    w = len(grid[ZERO])
    seen = set()
    out = []
    for i in range(h):
        for j in range(w):
            if (i, j) in seen:
                continue
            if grid[i][j] in (ZERO, FIVE):
                continue
            cells = {(i, j)}
            queue = [(i, j)]
            seen.add((i, j))
            while len(queue) > ZERO:
                ci, cj = queue.pop()
                for ni, nj in dneighbors((ci, cj)):
                    if not (ZERO <= ni < h and ZERO <= nj < w):
                        continue
                    if (ni, nj) in seen:
                        continue
                    if grid[ni][nj] in (ZERO, FIVE):
                        continue
                    seen.add((ni, nj))
                    cells.add((ni, nj))
                    queue.append((ni, nj))
            out.append(frozenset(cells))
    return tuple(sorted(out, key=ulcorner))


def _majority_color_d35bdbdc(values: tuple[int, ...]) -> int:
    counts = {}
    for value in values:
        counts[value] = counts.get(value, ZERO) + ONE
    return max(sorted(counts), key=lambda value: (counts[value], value))


def motif_center_d35bdbdc(patch: Indices) -> tuple[int, int]:
    return center(patch)


def paint_motif_d35bdbdc(
    grid: Grid,
    patch: Indices,
    outer_color: int,
    center_color: int,
) -> Grid:
    x0 = fill(grid, outer_color, patch)
    x1 = motif_center_d35bdbdc(patch)
    return fill(x0, center_color, initset(x1))


def extract_motifs_d35bdbdc(grid: Grid) -> tuple[dict[str, object], ...]:
    x0 = _extract_components_d35bdbdc(grid)
    x1 = []
    for x2 in x0:
        x3 = motif_center_d35bdbdc(x2)
        x4 = tuple(grid[i][j] for i, j in sorted(x2) if not equality((i, j), x3))
        x5 = grid[x3[ZERO]][x3[ONE]]
        x6 = _majority_color_d35bdbdc(x4) if len(x4) > ZERO else x5
        x1.append(
            {
                "patch": x2,
                "center": x3,
                "center_color": x5,
                "outer_color": x6,
            }
        )
    return tuple(x1)


def _contact_cells_d35bdbdc(
    patch: Indices,
    fives: Indices,
) -> Indices:
    x0 = set()
    for x1 in fives:
        if any(x2 in patch for x2 in dneighbors(x1)):
            x0.add(x1)
    return frozenset(x0)


def _bfs_distances_d35bdbdc(
    cells: Indices,
    start: tuple[int, int],
) -> dict[tuple[int, int], int]:
    x0 = deque([start])
    x1 = {start: ZERO}
    while len(x0) > ZERO:
        x2 = x0.popleft()
        for x3 in _neighbors8_d35bdbdc(x2):
            if x3 not in cells or x3 in x1:
                continue
            x1[x3] = x1[x2] + ONE
            x0.append(x3)
    return x1


def _farthest_cell_d35bdbdc(distances: dict[tuple[int, int], int]) -> tuple[int, int]:
    return max(sorted(distances), key=lambda loc: (distances[loc], loc[ZERO], loc[ONE]))


def diameter_endpoints_d35bdbdc(
    fives: Indices,
) -> tuple[tuple[int, int], tuple[int, int], dict[tuple[int, int], int], dict[tuple[int, int], int]]:
    x0 = min(fives)
    x1 = _farthest_cell_d35bdbdc(_bfs_distances_d35bdbdc(fives, x0))
    x2 = _bfs_distances_d35bdbdc(fives, x1)
    x3 = _farthest_cell_d35bdbdc(x2)
    x4 = tuple(sorted((x1, x3)))
    x5 = _bfs_distances_d35bdbdc(fives, x4[ZERO])
    x6 = _bfs_distances_d35bdbdc(fives, x4[ONE])
    return x4[ZERO], x4[ONE], x5, x6


def _best_contact_score_d35bdbdc(
    contact: Indices,
    distances: dict[tuple[int, int], int],
) -> tuple[int, int, int, int]:
    x0 = _component_cells_d35bdbdc(contact)
    return min(
        (
            min(distances[x1] for x1 in x2),
            max(distances[x3] for x3 in x2),
            len(x2),
            len(contact),
        )
        for x2 in x0
    )


def select_terminal_motif_indices_d35bdbdc(
    motifs: tuple[dict[str, object], ...],
    fives: Indices,
) -> tuple[int, ...]:
    if len(motifs) == ZERO or len(fives) == ZERO:
        return tuple()
    x0, x1, x2, x3 = diameter_endpoints_d35bdbdc(fives)
    del x0, x1
    x4 = []
    for x5, x6 in enumerate(motifs):
        x7 = _contact_cells_d35bdbdc(x6["patch"], fives)
        if len(x7) == ZERO:
            continue
        x8 = _best_contact_score_d35bdbdc(x7, x2)
        x9 = _best_contact_score_d35bdbdc(x7, x3)
        x4.append((x5, x8, x9))
    if len(x4) == ZERO:
        return tuple()
    x10 = None
    x11 = None
    for x12, x13, x14 in x4:
        for x15, x16, x17 in x4:
            if equality(x12, x15):
                continue
            x18 = (x13, x17, tuple(sorted((x12, x15))))
            if x10 is None or x18 < x10:
                x10 = x18
                x11 = tuple(sorted((x12, x15)))
    if x11 is not None:
        return x11
    x19 = min(x4, key=lambda item: (item[ONE], item[TWO], item[ZERO]))
    return (x19[ZERO],)


def apply_variant_grid_d35bdbdc(
    grid: Grid,
    variant: int,
) -> Grid:
    if equality(variant, ZERO):
        return grid
    if equality(variant, ONE):
        return rot90(grid)
    if equality(variant, TWO):
        return rot180(grid)
    if equality(variant, THREE):
        return rot270(grid)
    if equality(variant, FOUR):
        return hmirror(grid)
    if equality(variant, FIVE):
        return vmirror(grid)
    if equality(variant, SIX):
        return dmirror(grid)
    return cmirror(grid)


def build_layout_grids_d35bdbdc(
    layout: dict[str, object],
    outer_colors: tuple[int, ...],
    center_colors: tuple[int, ...],
    target_map: dict[int, int],
) -> tuple[Grid, Grid]:
    x0 = canvas(ZERO, GRID_DIMS_D35BDBDC)
    x1 = fill(x0, FIVE, layout["fives"])
    x2 = x1
    for x3, x4 in enumerate(layout["motifs"]):
        x1 = paint_motif_d35bdbdc(x1, x4, outer_colors[x3], center_colors[x3])
    for x5 in layout["kept_indices"]:
        x6 = layout["motifs"][x5]
        x7 = center_colors[target_map[x5]]
        x2 = paint_motif_d35bdbdc(x2, x6, outer_colors[x5], x7)
    return x1, x2
