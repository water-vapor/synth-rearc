from __future__ import annotations

from collections import Counter
from statistics import median

from synth_rearc.core import *


def _freeze_grid_446ef5d2(
    rows: list[list[int]],
) -> Grid:
    return tuple(tuple(row) for row in rows)


def _is_dom_row_446ef5d2(
    row: tuple[int, ...],
    dom: Integer,
) -> Boolean:
    return all(v == dom for v in row)


def _split_atomic_fragments_446ef5d2(
    grid: Grid,
    dom: Integer,
) -> tuple[Grid, ...]:
    x0 = len(grid)
    x1 = len(grid[ZERO])
    for x2 in range(ONE, x0):
        x3 = grid[x2]
        if _is_dom_row_446ef5d2(x3, dom):
            x4 = grid[:x2]
            x5 = grid[x2:]
            x6 = any(v != dom for row in x4 for v in row)
            x7 = any(v != dom for row in x5 for v in row)
            if x6 and x7:
                return _split_atomic_fragments_446ef5d2(x4, dom) + _split_atomic_fragments_446ef5d2(x5, dom)
    for x2 in range(ONE, x1):
        x3 = all(row[x2] == dom for row in grid)
        if x3:
            x4 = tuple(tuple(row[:x2]) for row in grid)
            x5 = tuple(tuple(row[x2:]) for row in grid)
            x6 = any(v != dom for row in x4 for v in row)
            x7 = any(v != dom for row in x5 for v in row)
            if x6 and x7:
                return _split_atomic_fragments_446ef5d2(x4, dom) + _split_atomic_fragments_446ef5d2(x5, dom)
    return (grid,)


def _pad_width_446ef5d2(
    grid: Grid,
    width_: Integer,
    dom: Integer,
    left_align: Boolean,
) -> Grid:
    x0 = width_ - len(grid[ZERO])
    if x0 <= ZERO:
        return grid
    if left_align:
        return tuple(tuple(list(row) + [dom] * x0) for row in grid)
    return tuple(tuple([dom] * x0 + list(row)) for row in grid)


def _pad_height_446ef5d2(
    grid: Grid,
    height_: Integer,
    dom: Integer,
    top_align: Boolean,
) -> Grid:
    x0 = height_ - len(grid)
    if x0 <= ZERO:
        return grid
    x1 = tuple(tuple(dom for _ in range(len(grid[ZERO]))) for _ in range(x0))
    if top_align:
        return x1 + grid
    return grid + x1


def _vcat_446ef5d2(
    parts: tuple[Grid, ...],
) -> Grid:
    x0: list[tuple[int, ...]] = []
    for x1 in parts:
        x0.extend(x1)
    return tuple(x0)


def _hcat_446ef5d2(
    parts: tuple[Grid, ...],
) -> Grid:
    x0: list[tuple[int, ...]] = []
    for x1 in zip(*parts):
        x2: list[int] = []
        for x3 in x1:
            x2.extend(x3)
        x0.append(tuple(x2))
    return tuple(x0)


def _vcat_align_446ef5d2(
    parts: tuple[Grid, ...],
    dom: Integer,
    side: str,
) -> Grid:
    x0 = max(len(p[ZERO]) for p in parts)
    x1 = side == "left"
    x2 = tuple(_pad_width_446ef5d2(p, x0, dom, x1) for p in parts)
    return _vcat_446ef5d2(x2)


def _edge_signature_446ef5d2(
    piece: Grid,
    dom: Integer,
) -> tuple[Boolean, Boolean, Boolean, Boolean]:
    x0 = _is_dom_row_446ef5d2(piece[ZERO], dom)
    x1 = _is_dom_row_446ef5d2(piece[-ONE], dom)
    x2 = all(row[ZERO] == dom for row in piece)
    x3 = all(row[-ONE] == dom for row in piece)
    return x0, x1, x2, x3


def _canonical_fragment_446ef5d2(
    piece: Grid,
    dom: Integer,
    sec: Integer,
    bg: Integer,
) -> Grid:
    x0 = [(i, j) for i, row in enumerate(piece) for j, v in enumerate(row) if v == sec]
    x1 = min(i for i, j in x0)
    x2 = max(i for i, j in x0)
    x3 = min(j for i, j in x0)
    x4 = max(j for i, j in x0)
    if x1 > ZERO and _is_dom_row_446ef5d2(piece[x1 - ONE], dom):
        x1 -= ONE
    if x2 + ONE < len(piece) and _is_dom_row_446ef5d2(piece[x2 + ONE], dom):
        x2 += ONE
    if x3 > ZERO and all(row[x3 - ONE] == dom for row in piece):
        x3 -= ONE
    if x4 + ONE < len(piece[ZERO]) and all(row[x4 + ONE] == dom for row in piece):
        x4 += ONE
    x5 = []
    for x6 in range(x1, x2 + ONE):
        x7 = []
        for x8 in range(x3, x4 + ONE):
            x9 = piece[x6][x8]
            x7.append(dom if x9 == bg else x9)
        x5.append(tuple(x7))
    return tuple(x5)


def _count_trailing_dom_rows_446ef5d2(
    panel: Grid,
    dom: Integer,
) -> Integer:
    x0 = ZERO
    for x1 in reversed(panel):
        if _is_dom_row_446ef5d2(x1, dom):
            x0 += ONE
        else:
            break
    return x0


def _missing_corner_446ef5d2(
    grid: Grid,
    marker: Integer,
) -> tuple[Integer, Integer]:
    x0 = [(i, j) for i, row in enumerate(grid) for j, v in enumerate(row) if v == marker]
    x1 = min(i for i, j in x0)
    x2 = max(i for i, j in x0)
    x3 = min(j for i, j in x0)
    x4 = max(j for i, j in x0)
    for x5 in range(x1, x2 + ONE):
        for x6 in range(x3, x4 + ONE):
            if (x5, x6) not in x0:
                return x5, x6
    raise ValueError("marker triomino is malformed")


def extract_task_state_446ef5d2(
    I: Grid,
) -> dict:
    x0 = tuple(tuple(row) for row in I)
    x1 = [v for row in x0 for v in row]
    x2 = Counter(x1)
    x3 = x2.most_common(ONE)[ZERO][ZERO]
    x4 = min((v for v in x2 if v != x3), key=x2.get)
    x5 = Counter(v for row in x0 for v in row if v not in (x3, x4)).most_common(ONE)[ZERO][ZERO]
    x6 = tuple(v for v, _ in Counter(v for row in x0 for v in row if v not in (x3, x4, x5)).most_common())
    x7 = tuple(tuple(x3 if v == x4 else v for v in row) for row in x0)
    x8 = []
    for x9 in objects(x7, False, False, True):
        x10 = subgrid(x9, x7)
        x8.extend(_split_atomic_fragments_446ef5d2(x10, x5))
    x11 = _missing_corner_446ef5d2(x0, x4)
    return {
        "grid": x0,
        "background": x3,
        "marker": x4,
        "dominant": x5,
        "secondaries": x6,
        "atomic": tuple(x8),
        "corner": x11,
    }


def build_panel_446ef5d2(
    pieces: tuple[Grid, ...],
    dom: Integer,
    sec: Integer,
) -> Grid:
    if len(pieces) == FIVE:
        return tuple(
            tuple(row)
            for row in (
                (dom, dom, dom, dom, dom, dom, dom, dom, dom, dom),
                (dom, dom, sec, sec, sec, sec, sec, sec, sec, dom),
                (dom, dom, sec, dom, dom, dom, dom, dom, sec, dom),
                (dom, dom, sec, dom, dom, dom, dom, dom, sec, dom),
                (dom, dom, sec, sec, sec, sec, sec, sec, sec, dom),
                (dom, dom, dom, dom, dom, dom, dom, dom, dom, dom),
            )
        )
    x0 = []
    for x1 in pieces:
        x2, x3, x4, x5 = _edge_signature_446ef5d2(x1, dom)
        x6 = "top" if x2 and not x3 else "bottom" if x3 and not x2 else "neutral"
        x7 = "left" if x4 and not x5 else "right" if x5 and not x4 else "middle"
        x0.append((x1, x6, x7))
    x8 = [x for x in x0 if x[TWO] == "left"]
    x9 = [x for x in x0 if x[TWO] == "right"]
    x10 = [x for x in x0 if x[TWO] == "middle"]
    x11 = {"top": ZERO, "neutral": ONE, "bottom": TWO}
    x12 = []
    if x8:
        x13 = tuple(x[ZERO] for x in sorted(x8, key=lambda z: (x11[z[ONE]], -len(z[ZERO]))))
        x12.append((_vcat_align_446ef5d2(x13, dom, "left"), "left"))
    x14 = [x for x in x10 if _edge_signature_446ef5d2(x[ZERO], dom)[:TWO] == (True, True)]
    x15 = [x for x in x10 if x not in x14]
    for x16 in sorted(x14, key=lambda z: (-len(z[ZERO][ZERO]), len(z[ZERO]))):
        x12.append((x16[ZERO], "standalone"))
    if x15:
        x16 = tuple(x[ZERO] for x in sorted(x15, key=lambda z: (x11[z[ONE]], -len(z[ZERO]))))
        x12.append((_vcat_align_446ef5d2(x16, dom, "stacked"), "stacked"))
    if x9:
        x16 = tuple(x[ZERO] for x in sorted(x9, key=lambda z: (x11[z[ONE]], -len(z[ZERO]))))
        x12.append((_vcat_align_446ef5d2(x16, dom, "right"), "right"))
    x17 = max(len(x[ZERO]) for x in x12)
    x18 = sum(ONE for _, kind in x12 if kind == "standalone")
    x19 = []
    for x20, x21 in x12:
        x22, x23, _, _ = _edge_signature_446ef5d2(x20, dom)
        if x21 == "stacked":
            x24 = True
        elif x21 == "standalone" and len(x20) < x17:
            x24 = x18 > ONE
        else:
            x24 = (not x22) and x23
        x19.append(_pad_height_446ef5d2(x20, x17, dom, x24))
    return _hcat_446ef5d2(tuple(x19))


def panel_specs_446ef5d2(
    I: Grid,
) -> tuple[tuple[float, Integer, Grid, tuple[Grid, ...], Boolean], ...]:
    x0 = extract_task_state_446ef5d2(I)
    x1 = x0["grid"]
    x2 = x0["background"]
    x3 = x0["dominant"]
    x4 = x0["secondaries"]
    x5 = x0["atomic"]
    x6 = []
    for x7 in x4:
        x8 = tuple(_canonical_fragment_446ef5d2(p, x3, x7, x2) for p in x5 if any(v == x7 for row in p for v in row))
        x9 = build_panel_446ef5d2(x8, x3, x7)
        x10 = [i for i, row in enumerate(x1) for _, v in enumerate(row) if v == x7]
        x11 = all(_edge_signature_446ef5d2(p, x3)[:TWO] == (True, True) for p in x8)
        x6.append((median(x10), x7, x9, x8, x11))
    return tuple(sorted(x6, key=lambda z: z[ZERO]))


def assemble_output_446ef5d2(
    I: Grid,
) -> Grid:
    x0 = extract_task_state_446ef5d2(I)
    x1 = x0["background"]
    x2 = x0["dominant"]
    x3 = x0["corner"]
    x4 = panel_specs_446ef5d2(I)
    x5 = []
    for x6, x7, x8, x9, x10 in x4:
        x11 = any(_edge_signature_446ef5d2(p, x2) == (True, False, True, False) for p in x9)
        x12 = len(x5) > ZERO and _is_dom_row_446ef5d2(x8[ZERO], x2) and (len(x9) == FIVE or (len(x9) == FOUR and not x11))
        if len(x5) > ZERO and x10 and _is_dom_row_446ef5d2(x8[ZERO], x2):
            x8 = x8[ONE:]
        elif x12:
            x8 = x8[ONE:] + (tuple(x2 for _ in range(len(x8[ZERO]))),)
        x5.append((x7, x8, x10))
    x13: list[tuple[int, ...]] = []
    for x14, (_, x15, _) in enumerate(x5):
        if x14 < len(x5) - ONE:
            x16 = x5[x14 + ONE]
            if x16[TWO]:
                x17 = ONE
            else:
                x17 = ONE if _is_dom_row_446ef5d2(x16[ONE][ZERO], x2) else TWO
            x18 = max(ZERO, x17 - _count_trailing_dom_rows_446ef5d2(x15, x2))
            if x18:
                x19 = tuple(tuple(x2 for _ in range(len(x15[ZERO]))) for _ in range(x18))
                x15 = x15 + x19
        x13.extend(x15)
    x20 = max(len(row) for row in x13)
    x21 = x3[ONE] < len(x0["grid"][ZERO]) // TWO
    x22 = []
    for x23 in x13:
        x24 = x20 - len(x23)
        if x21:
            x22.append(tuple(list(x23) + [x2] * x24))
        else:
            x22.append(tuple([x2] * x24 + list(x23)))
    x25 = tuple(x22)
    x26 = len(x25)
    x27 = len(x25[ZERO])
    x28 = len(x0["grid"])
    x29 = len(x0["grid"][ZERO])
    x30 = x3[ZERO] < x28 // TWO
    x31 = x3[ZERO] if x30 else x3[ZERO] - x26 + ONE
    x32 = x3[ONE] if x21 else x3[ONE] - x27 + ONE
    x33 = [[x1 for _ in range(x29)] for _ in range(x28)]
    for x34, row in enumerate(x25):
        for x35, v in enumerate(row):
            x33[x31 + x34][x32 + x35] = v
    return _freeze_grid_446ef5d2(x33)
