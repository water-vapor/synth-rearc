from __future__ import annotations

from collections import Counter

from synth_rearc.core import *

from .helpers import assemble_output_446ef5d2


CANVAS_SIZE_446EF5D2 = 26
TWO_COL_TEMPLATE_446EF5D2 = (
    ((1, 1, 1, 1, 1), (1, 2, 2, 2, 2), (1, 2, 1, 2, 2)),
    ((1, 1, 1, 1, 1, 1), (2, 2, 2, 1, 2, 1), (2, 1, 2, 2, 2, 1)),
)
THREE_COL_TEMPLATE_446EF5D2 = (
    ((1, 1, 1, 1, 1), (1, 2, 1, 2, 2), (1, 2, 2, 2, 1), (1, 1, 1, 1, 1)),
    ((1, 1, 1), (2, 2, 2), (1, 1, 1)),
    ((1, 1, 1), (2, 2, 1), (1, 2, 1), (1, 1, 1)),
)
CORNER_TEMPLATE_446EF5D2 = (
    ((1, 1, 1), (1, 2, 2), (1, 2, 2)),
    ((1, 1, 1), (2, 2, 1), (2, 2, 1)),
    ((1, 2, 2), (1, 2, 1), (1, 1, 1)),
    ((2, 2, 1), (1, 1, 1), (1, 1, 1)),
)


def _freeze_grid_446ef5d2(
    rows: list[list[int]],
) -> Grid:
    return tuple(tuple(row) for row in rows)


def _recolor_template_446ef5d2(
    template: tuple[tuple[int, ...], ...],
    dom: Integer,
    sec: Integer,
) -> Grid:
    return tuple(tuple(dom if v == ONE else sec for v in row) for row in template)


def _two_col_fragments_446ef5d2(
    dom: Integer,
    sec: Integer,
) -> tuple[Grid, ...]:
    return (
        _recolor_template_446ef5d2(TWO_COL_TEMPLATE_446EF5D2[ZERO], dom, sec),
        _recolor_template_446ef5d2(TWO_COL_TEMPLATE_446EF5D2[ONE], dom, sec),
    )


def _three_col_fragments_446ef5d2(
    dom: Integer,
    sec: Integer,
) -> tuple[Grid, ...]:
    return tuple(_recolor_template_446ef5d2(t, dom, sec) for t in THREE_COL_TEMPLATE_446EF5D2)


def _corner_fragments_446ef5d2(
    dom: Integer,
    sec: Integer,
) -> tuple[Grid, ...]:
    return tuple(_recolor_template_446ef5d2(t, dom, sec) for t in CORNER_TEMPLATE_446EF5D2)


def _paint_piece_446ef5d2(
    canvas_: list[list[int]],
    piece: Grid,
    row: Integer,
    col: Integer,
) -> None:
    for i, prow in enumerate(piece):
        for j, value in enumerate(prow):
            canvas_[row + i][col + j] = value


def _scatter_panel_446ef5d2(
    canvas_: list[list[int]],
    pieces: tuple[Grid, ...],
    template_name: str,
    band_row: Integer,
    width_: Integer,
) -> None:
    if template_name == "two_col":
        x0 = pieces[ZERO]
        x1 = pieces[ONE]
        x2 = randint(THREE, FOUR)
        x3 = width_ - len(x1[ZERO]) - randint(THREE, FOUR)
        _paint_piece_446ef5d2(canvas_, x0, band_row, x2)
        _paint_piece_446ef5d2(canvas_, x1, band_row + randint(ZERO, ONE), x3)
        return
    if template_name == "three_col":
        x0 = pieces[ZERO]
        x1 = pieces[ONE]
        x2 = pieces[TWO]
        x3 = randint(THREE, FOUR)
        x4 = width_ // TWO - len(x1[ZERO]) // TWO + randint(-ONE, ONE)
        x5 = width_ - len(x2[ZERO]) - randint(THREE, FOUR)
        _paint_piece_446ef5d2(canvas_, x0, band_row + ONE, x3)
        _paint_piece_446ef5d2(canvas_, x1, band_row, x4)
        _paint_piece_446ef5d2(canvas_, x2, band_row + ONE, x5)
        return
    x0 = pieces[ZERO]
    x1 = pieces[ONE]
    x2 = pieces[TWO]
    x3 = pieces[THREE]
    x4 = randint(THREE, FOUR)
    x5 = width_ - len(x1[ZERO]) - randint(THREE, FOUR)
    x6 = band_row + FOUR
    _paint_piece_446ef5d2(canvas_, x0, band_row, x4)
    _paint_piece_446ef5d2(canvas_, x1, band_row, x5)
    _paint_piece_446ef5d2(canvas_, x2, x6, x4)
    _paint_piece_446ef5d2(canvas_, x3, x6, x5)


def _place_marker_446ef5d2(
    canvas_: list[list[int]],
    marker: Integer,
    corner_kind: str,
) -> None:
    x0 = len(canvas_)
    x1 = len(canvas_[ZERO])
    if corner_kind == "ul":
        x2 = ((ZERO, ZERO), (ZERO, ONE), (ONE, ZERO))
    elif corner_kind == "ur":
        x2 = ((ZERO, x1 - TWO), (ZERO, x1 - ONE), (ONE, x1 - ONE))
    elif corner_kind == "ll":
        x2 = ((x0 - TWO, ZERO), (x0 - ONE, ZERO), (x0 - ONE, ONE))
    else:
        x2 = ((x0 - TWO, x1 - ONE), (x0 - ONE, x1 - TWO), (x0 - ONE, x1 - ONE))
    for x3, x4 in x2:
        canvas_[x3][x4] = marker


def _valid_marker_counts_446ef5d2(
    grid: Grid,
    marker: Integer,
    bg: Integer,
) -> Boolean:
    x0 = Counter(v for row in grid for v in row if v != bg)
    return x0[marker] == THREE and min(x0.values()) == THREE and list(x0.values()).count(THREE) == ONE


def generate_446ef5d2(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = CANVAS_SIZE_446EF5D2
    x1 = ("two_col", "three_col", "corners")
    x2 = ("ul", "ur", "ll", "lr")
    while True:
        x3 = unifint(diff_lb, diff_ub, (ONE, THREE))
        x4 = sample(tuple(range(TEN)), x3 + THREE)
        x5 = x4[ZERO]
        x6 = x4[ONE]
        x7 = x4[TWO]
        x8 = x4[THREE:]
        x9 = [[x5 for _ in range(x0)] for _ in range(x0)]
        x10 = []
        for x11 in range(x3):
            x12 = x8[x11]
            x13 = choice(x1)
            if x13 == "two_col":
                x14 = _two_col_fragments_446ef5d2(x6, x12)
            elif x13 == "three_col":
                x14 = _three_col_fragments_446ef5d2(x6, x12)
            else:
                x14 = _corner_fragments_446ef5d2(x6, x12)
            x10.append((x13, x14))
        x15 = (THREE, TEN, 17)
        for x16, (x17, x18) in enumerate(x10):
            _scatter_panel_446ef5d2(x9, x18, x17, x15[x16], x0)
        x19 = choice(x2)
        _place_marker_446ef5d2(x9, x7, x19)
        x20 = _freeze_grid_446ef5d2(x9)
        if not _valid_marker_counts_446ef5d2(x20, x7, x5):
            continue
        x21 = assemble_output_446ef5d2(x20)
        if x21 == x20:
            continue
        return {"input": x20, "output": x21}
