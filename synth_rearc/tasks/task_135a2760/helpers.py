from __future__ import annotations

from dataclasses import dataclass

from synth_rearc.core import *


HORIZONTAL_MULTI_KINDS_135a2760 = (
    "h_block2",
    "h_checker",
    "h_notch",
    "h_altbar",
)

VERTICAL_KINDS_135a2760 = (
    "v_block2",
    "v_bounce4",
    "v_notch",
    "v_diamond",
)

KIND_PRIORITY_135a2760 = {
    "h_alt1": ZERO,
    "h_block2": ONE,
    "h_checker": TWO,
    "h_notch": THREE,
    "h_altbar": FOUR,
    "v_block2": FIVE,
    "v_bounce4": SIX,
    "v_notch": SEVEN,
    "v_diamond": EIGHT,
}

BOUNCE4_SEQUENCE_135a2760 = (ZERO, ONE, TWO, THREE, TWO, ONE)


@dataclass(frozen=True)
class PanelInfo135a2760:
    row0: int
    col0: int
    panel: Grid
    border: int
    fg: int


def _span_pairs_135a2760(
    indices: tuple[int, ...],
    size: int,
) -> tuple[tuple[int, int], ...]:
    spans = []
    prev = NEG_ONE
    for idx in indices + (size,):
        if idx - prev > ONE:
            spans.append((prev + ONE, idx - ONE))
        prev = idx
    return tuple(spans)


def _full_background_rows_135a2760(
    grid: Grid,
    bg: int,
) -> tuple[int, ...]:
    return tuple(i for i, row in enumerate(grid) if len(set(row)) == ONE and row[ZERO] == bg)


def _full_background_cols_135a2760(
    grid: Grid,
    bg: int,
) -> tuple[int, ...]:
    h = height(grid)
    w = width(grid)
    return tuple(j for j in range(w) if len({grid[i][j] for i in range(h)}) == ONE and grid[ZERO][j] == bg)


def panel_infos_135a2760(
    grid: Grid,
) -> tuple[int, tuple[PanelInfo135a2760, ...]]:
    bg = mostcolor(grid)
    x0 = _full_background_rows_135a2760(grid, bg)
    x1 = _full_background_cols_135a2760(grid, bg)
    x2 = _span_pairs_135a2760(x0, height(grid))
    x3 = _span_pairs_135a2760(x1, width(grid))
    infos = []
    for row0, row1 in x2:
        for col0, col1 in x3:
            dims = (row1 - row0 + ONE, col1 - col0 + ONE)
            panel = crop(grid, (row0, col0), dims)
            border = panel[ZERO][ZERO]
            colors = tuple(sorted(palette(panel) - frozenset({bg, border})))
            if len(colors) == ZERO:
                continue
            infos.append(PanelInfo135a2760(row0, col0, panel, border, colors[ZERO]))
    return bg, tuple(infos)


def candidate_kinds_135a2760(
    panel: Grid,
) -> tuple[str, ...]:
    x0 = height(panel) - TWO
    x1 = width(panel) - TWO
    if x0 == ONE:
        return ("h_alt1",)
    if x0 == TWO:
        return HORIZONTAL_MULTI_KINDS_135a2760
    if x1 == FOUR:
        return VERTICAL_KINDS_135a2760
    return ()


def _render_inner_135a2760(
    kind: str,
    long_dim: int,
    fg: int,
    bg: int,
) -> Grid:
    if kind == "h_alt1":
        return (tuple(fg if j % TWO == ZERO else bg for j in range(long_dim)),)
    if kind == "h_block2":
        row = tuple(fg if j % THREE != TWO else bg for j in range(long_dim))
        return (row, row)
    if kind == "h_checker":
        row0 = tuple(fg if j % TWO == ZERO else bg for j in range(long_dim))
        row1 = tuple(fg if j % TWO == ONE else bg for j in range(long_dim))
        return (row0, row1)
    if kind == "h_notch":
        row0 = []
        row1 = []
        for j in range(long_dim):
            mod = j % FOUR
            row0.append(fg if mod in (ZERO, TWO, THREE) else bg)
            row1.append(fg if mod in (ZERO, ONE, TWO) else bg)
        return (tuple(row0), tuple(row1))
    if kind == "h_altbar":
        row = tuple(fg if j % TWO == ZERO else bg for j in range(long_dim))
        return (row, row)
    if kind == "v_block2":
        return tuple(
            (bg, fg if i % THREE != ZERO else bg, fg if i % THREE != ZERO else bg, bg) for i in range(long_dim)
        )
    if kind == "v_bounce4":
        rows = []
        for i in range(long_dim):
            row = [bg] * FOUR
            row[BOUNCE4_SEQUENCE_135a2760[i % SIX]] = fg
            rows.append(tuple(row))
        return tuple(rows)
    if kind == "v_notch":
        motifs = (
            (fg, bg, bg, bg),
            (fg, fg, fg, fg),
            (bg, bg, bg, fg),
            (fg, fg, fg, fg),
        )
        return tuple(motifs[i % FOUR] for i in range(long_dim))
    if kind == "v_diamond":
        motifs = (
            (bg, bg, bg, bg),
            (bg, fg, bg, bg),
            (bg, fg, fg, bg),
            (bg, fg, bg, bg),
        )
        return tuple(motifs[i % FOUR] for i in range(long_dim))
    raise ValueError(f"unknown kind {kind}")


def wrap_inner_135a2760(
    inner: Grid,
    border: int,
) -> Grid:
    x0 = width(inner) + TWO
    x1 = tuple(border for _ in range(x0))
    rows = [x1]
    for row in inner:
        rows.append((border,) + row + (border,))
    rows.append(x1)
    return tuple(rows)


def render_panel_135a2760(
    kind: str,
    long_dim: int,
    fg: int,
    border: int,
    bg: int,
) -> Grid:
    x0 = _render_inner_135a2760(kind, long_dim, fg, bg)
    return wrap_inner_135a2760(x0, border)


def _inner_mismatch_135a2760(
    panel: Grid,
    kind: str,
    fg: int,
    bg: int,
) -> int:
    x0 = height(panel) - TWO
    x1 = width(panel) - TWO
    x2 = crop(panel, UNITY, (x0, x1))
    x3 = x1 if x0 <= TWO else x0
    x4 = _render_inner_135a2760(kind, x3, fg, bg)
    return sum(a != b for rowa, rowb in zip(x2, x4) for a, b in zip(rowa, rowb))


def best_kind_135a2760(
    panel: Grid,
    bg: int,
    fg: int,
) -> str:
    x0 = candidate_kinds_135a2760(panel)
    x1 = (
        (_inner_mismatch_135a2760(panel, kind, fg, bg), KIND_PRIORITY_135a2760[kind], kind)
        for kind in x0
    )
    return min(x1)[-1]


def repair_panel_135a2760(
    panel: Grid,
    bg: int,
) -> Grid:
    x0 = panel[ZERO][ZERO]
    x1 = tuple(sorted(palette(panel) - frozenset({bg, x0})))
    x2 = x1[ZERO]
    x3 = best_kind_135a2760(panel, bg, x2)
    x4 = height(panel) - TWO
    x5 = width(panel) - TWO
    x6 = x5 if x4 <= TWO else x4
    return render_panel_135a2760(x3, x6, x2, x0, bg)


def repair_grid_135a2760(
    grid: Grid,
) -> Grid:
    x0, x1 = panel_infos_135a2760(grid)
    rows = [list(row) for row in grid]
    for info in x1:
        x2 = repair_panel_135a2760(info.panel, x0)
        for di, row in enumerate(x2):
            for dj, value in enumerate(row):
                rows[info.row0 + di][info.col0 + dj] = value
    return tuple(tuple(row) for row in rows)


def paste_subgrid_135a2760(
    grid: Grid,
    subgrid: Grid,
    loc: tuple[int, int],
) -> Grid:
    rows = [list(row) for row in grid]
    row0, col0 = loc
    for di, row in enumerate(subgrid):
        for dj, value in enumerate(row):
            rows[row0 + di][col0 + dj] = value
    return tuple(tuple(row) for row in rows)


def assemble_horizontal_135a2760(
    panels: tuple[Grid, ...],
    bg: int,
) -> Grid:
    panel_h = height(panels[ZERO])
    panel_w = width(panels[ZERO])
    grid_h = TWO + len(panels) * panel_h + (len(panels) - ONE)
    grid_w = panel_w + TWO
    grid = canvas(bg, (grid_h, grid_w))
    row0 = ONE
    for panel in panels:
        grid = paste_subgrid_135a2760(grid, panel, (row0, ONE))
        row0 += panel_h + ONE
    return grid


def assemble_vertical_135a2760(
    panels: tuple[Grid, ...],
    bg: int,
) -> Grid:
    panel_h = height(panels[ZERO])
    panel_w = width(panels[ZERO])
    grid_h = panel_h + TWO
    grid_w = TWO + len(panels) * panel_w + (len(panels) - ONE)
    grid = canvas(bg, (grid_h, grid_w))
    col0 = ONE
    for panel in panels:
        grid = paste_subgrid_135a2760(grid, panel, (ONE, col0))
        col0 += panel_w + ONE
    return grid


def _toggle_inner_cells_135a2760(
    inner: Grid,
    cells: frozenset[tuple[int, int]],
    fg: int,
    bg: int,
) -> Grid:
    rows = [list(row) for row in inner]
    for i, j in cells:
        rows[i][j] = bg if rows[i][j] == fg else fg
    return tuple(tuple(row) for row in rows)


def _random_local_cells_135a2760(
    dims: tuple[int, int],
) -> frozenset[tuple[int, int]]:
    h, w = dims
    i = randint(ZERO, h - ONE)
    j = randint(ZERO, w - ONE)
    cells = {(i, j)}
    if w > ONE and choice((T, F)):
        dj = choice((NEG_ONE, ONE))
        jj = min(max(ZERO, j + dj), w - ONE)
        cells.add((i, jj))
    if h > ONE and choice((T, F)):
        di = choice((NEG_ONE, ONE))
        ii = min(max(ZERO, i + di), h - ONE)
        cells.add((ii, j))
    return frozenset(cells)


def corrupt_panel_135a2760(
    panel: Grid,
    bg: int,
) -> Grid:
    border = panel[ZERO][ZERO]
    fg = tuple(sorted(palette(panel) - frozenset({bg, border})))[ZERO]
    inner = crop(panel, UNITY, (height(panel) - TWO, width(panel) - TWO))
    for _ in range(200):
        cells = _random_local_cells_135a2760(shape(inner))
        altered_inner = _toggle_inner_cells_135a2760(inner, cells, fg, bg)
        if altered_inner == inner:
            continue
        altered_panel = wrap_inner_135a2760(altered_inner, border)
        if repair_panel_135a2760(altered_panel, bg) == panel:
            return altered_panel
    raise RuntimeError("failed to corrupt panel without changing its recovered motif")


def odd_length_135a2760(
    diff_lb: float,
    diff_ub: float,
    bounds: tuple[int, int],
) -> int:
    x0 = unifint(diff_lb, diff_ub, bounds)
    if even(x0):
        x0 = x0 - ONE if x0 > bounds[ZERO] else x0 + ONE
    return x0
