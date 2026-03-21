from arc2.core import *

from .verifier import verify_afe3afe9


_RING_PATCH_AFE3AFE9 = frozenset({
    (0, 0), (0, 1), (0, 2),
    (1, 0),         (1, 2),
    (2, 0), (2, 1), (2, 2),
})
_PALETTE_AFE3AFE9 = (TWO, THREE, FOUR, SIX, SEVEN, EIGHT, NINE)
_SIDE_TO_SHAPE_AFE3AFE9 = {
    "top": (7, 6),
    "bottom": (7, 6),
    "left": (6, 7),
    "right": (6, 7),
}
_SIDE_TO_ROWS_AFE3AFE9 = {
    "top": (2, 6, 10, 14, 18, 22, 26),
    "bottom": (1, 5, 9, 13, 17, 21, 25),
    "left": (1, 5, 9, 17, 21, 25),
    "right": (1, 5, 9, 17, 21, 25),
}
_SIDE_TO_COLS_AFE3AFE9 = {
    "top": (1, 5, 9, 17, 21, 25),
    "bottom": (1, 5, 9, 17, 21, 25),
    "left": (2, 6, 10, 14, 18, 22, 26),
    "right": (1, 5, 9, 13, 17, 21, 25),
}


def _neighbors_afe3afe9(
    cell: tuple[Integer, Integer],
    h: Integer,
    w: Integer,
) -> tuple[tuple[Integer, Integer], ...]:
    i, j = cell
    out = []
    for di, dj in (UP, DOWN, LEFT, RIGHT):
        ii = i + di
        jj = j + dj
        if 0 <= ii < h and 0 <= jj < w:
            out.append((ii, jj))
    return tuple(out)


def _grow_patch_afe3afe9(
    cells: frozenset[tuple[Integer, Integer]],
    target: Integer,
) -> frozenset[tuple[Integer, Integer]]:
    if len(cells) == ZERO:
        return frozenset()
    h = max(i for i, _ in cells) + ONE
    w = max(j for _, j in cells) + ONE
    patch = {choice(tuple(cells))}
    while len(patch) < target:
        frontier = {
            nbr
            for cell in patch
            for nbr in _neighbors_afe3afe9(cell, h, w)
            if nbr in cells and nbr not in patch
        }
        if len(frontier) == ZERO:
            break
        patch.add(choice(tuple(frontier)))
    return frozenset(patch)


def _sample_panel_afe3afe9(
    h: Integer,
    w: Integer,
    colors: tuple[Integer, ...],
    diff_lb: float,
    diff_ub: float,
) -> dict[tuple[Integer, Integer], Integer]:
    cells = frozenset(product(interval(ZERO, h, ONE), interval(ZERO, w, ONE)))
    free = set(cells)
    panel: dict[tuple[Integer, Integer], Integer] = {}
    if len(colors) == ONE:
        sizes = (unifint(diff_lb, diff_ub, (9, 15)),)
    else:
        a = unifint(diff_lb, diff_ub, (7, 11))
        b = unifint(diff_lb, diff_ub, (4, 8))
        if a + b > 18:
            b = 18 - a
        sizes = (a, max(3, b))
    for color_value, target in zip(colors, sizes):
        patch = _grow_patch_afe3afe9(frozenset(free), target)
        for cell in patch:
            panel[cell] = color_value
        free -= set(patch)
    extras = unifint(diff_lb, diff_ub, (1, 4))
    for _ in range(extras):
        if len(free) == ZERO:
            break
        cell = choice(tuple(free))
        color_value = choice(colors)
        panel[cell] = color_value
        free.remove(cell)
    if w == THREE:
        used = {j for _, j in panel}
        for j in range(w):
            if j in used:
                continue
            i = randint(ZERO, h - ONE)
            panel[(i, j)] = choice(colors)
            free.discard((i, j))
    if h == THREE:
        used = {i for i, _ in panel}
        for i in range(h):
            if i in used:
                continue
            j = randint(ZERO, w - ONE)
            panel[(i, j)] = choice(colors)
            free.discard((i, j))
    return panel


def _assemble_output_afe3afe9(
    side: str,
    colors: tuple[Integer, ...],
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    h, w = _SIDE_TO_SHAPE_AFE3AFE9[side]
    grid = [[ZERO for _ in range(w)] for _ in range(h)]
    split = choice((ONE, TWO)) if len(colors) == THREE else ONE
    panel_a_colors = colors[:split]
    panel_b_colors = colors[split:]
    if side in ("top", "bottom"):
        panel_a = _sample_panel_afe3afe9(h, THREE, panel_a_colors, diff_lb, diff_ub)
        panel_b = _sample_panel_afe3afe9(h, THREE, panel_b_colors, diff_lb, diff_ub)
        for (i, j), value in panel_a.items():
            grid[i][j] = value
        for (i, j), value in panel_b.items():
            grid[i][j + THREE] = value
    else:
        panel_a = _sample_panel_afe3afe9(THREE, w, panel_a_colors, diff_lb, diff_ub)
        panel_b = _sample_panel_afe3afe9(THREE, w, panel_b_colors, diff_lb, diff_ub)
        for (i, j), value in panel_a.items():
            grid[i][j] = value
        for (i, j), value in panel_b.items():
            grid[i + THREE][j] = value
    target = unifint(diff_lb, diff_ub, (24, 34))
    while sum(v != ZERO for row in grid for v in row) < target:
        empties = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == ZERO]
        if len(empties) == ZERO:
            break
        i, j = choice(empties)
        grid[i][j] = choice(colors)
    while sum(v != ZERO for row in grid for v in row) > target:
        filled = [
            (i, j)
            for i in range(h)
            for j in range(w)
            if grid[i][j] != ZERO
            and sum(grid[i][jj] != ZERO for jj in range(w)) > ONE
            and sum(grid[ii][j] != ZERO for ii in range(h)) > ONE
            and sum(v == grid[i][j] for row in grid for v in row) > TWO
        ]
        if len(filled) == ZERO:
            break
        i, j = choice(filled)
        grid[i][j] = ZERO
    for i in range(h):
        if any(grid[i][j] != ZERO for j in range(w)):
            continue
        j = randint(ZERO, w - ONE)
        grid[i][j] = choice(colors)
    for j in range(w):
        if any(grid[i][j] != ZERO for i in range(h)):
            continue
        i = randint(ZERO, h - ONE)
        grid[i][j] = choice(colors)
    return tuple(tuple(row) for row in grid)


def _pack_row_afe3afe9(
    row: tuple[Integer, ...],
    to_right: Boolean,
) -> tuple[Integer, ...]:
    vals = tuple(v for v in row if v != ZERO)
    pad = repeat(ZERO, len(row) - len(vals))
    return branch(to_right, pad + vals, vals + pad)


def _pack_rows_afe3afe9(
    G: Grid,
    to_right: Boolean,
) -> Grid:
    return tuple(_pack_row_afe3afe9(row, to_right) for row in G)


def _pack_cols_afe3afe9(
    G: Grid,
    to_bottom: Boolean,
) -> Grid:
    x0 = dmirror(G)
    x1 = _pack_rows_afe3afe9(x0, to_bottom)
    x2 = dmirror(x1)
    return x2


def _pack_grid_afe3afe9(
    G: Grid,
    side: str,
) -> Grid:
    if side == "top":
        return _pack_rows_afe3afe9(G, T)
    if side == "bottom":
        return _pack_rows_afe3afe9(G, F)
    if side == "left":
        return _pack_cols_afe3afe9(G, F)
    return _pack_cols_afe3afe9(G, T)


def _expand_input_afe3afe9(
    side: str,
    compact: Grid,
) -> Grid:
    rows = _SIDE_TO_ROWS_AFE3AFE9[side]
    cols = _SIDE_TO_COLS_AFE3AFE9[side]
    gi = canvas(ZERO, (30, 30))
    for i, row in enumerate(compact):
        for j, value in enumerate(row):
            if value == ZERO:
                continue
            patch = shift(_RING_PATCH_AFE3AFE9, (rows[i], cols[j]))
            gi = paint(gi, recolor(value, patch))
    if side == "top":
        gi = fill(gi, ONE, connect((ZERO, ZERO), (ZERO, 29)))
    elif side == "bottom":
        gi = fill(gi, ONE, connect((29, ZERO), (29, 29)))
    elif side == "left":
        gi = fill(gi, ONE, connect((ZERO, ZERO), (29, ZERO)))
    else:
        gi = fill(gi, ONE, connect((ZERO, 29), (29, 29)))
    return gi


def generate_afe3afe9(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        side = choice(("top", "bottom", "left", "right"))
        ncolors = choice((TWO, THREE, THREE))
        colors = tuple(sample(_PALETTE_AFE3AFE9, ncolors))
        compact = _assemble_output_afe3afe9(side, colors, diff_lb, diff_ub)
        go = _pack_grid_afe3afe9(compact, side)
        gi = _expand_input_afe3afe9(side, compact)
        if gi == go:
            continue
        if verify_afe3afe9(gi) != go:
            continue
        return {"input": gi, "output": go}
