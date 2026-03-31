from synth_rearc.core import *


ROW_COLORS_291dc1e1 = (THREE, FOUR, FIVE, SIX, SEVEN, NINE)
VERTICAL_COLORS_291dc1e1 = difference(interval(ZERO, TEN, ONE), (ZERO, EIGHT))


def _solid_piece_291dc1e1(
    h: int,
    w: int,
    value: int,
) -> Grid:
    return canvas(value, (h, w))


def _rows_to_grid_291dc1e1(rows: tuple[tuple[int, int], ...]) -> Grid:
    return tuple(tuple(row) for row in rows)


def _center_piece_291dc1e1(
    piece: Grid,
    outw: int,
) -> Grid:
    x0 = width(piece)
    x1 = (outw - x0) // TWO
    x2 = canvas(EIGHT, (height(piece), outw))
    x3 = shift(asobject(piece), (ZERO, x1))
    return paint(x2, x3)


def _stack_pieces_291dc1e1(
    pieces: tuple[Grid, ...],
) -> Grid:
    x0 = maximum(tuple(width(x1) for x1 in pieces))
    x1 = tuple(_center_piece_291dc1e1(x2, x0) for x2 in pieces)
    x2 = tuple()
    for x3 in x1:
        x2 = x2 + x3
    return x2


def _make_vertical_piece_291dc1e1(
    h: int,
    dominant: int,
    accents: tuple[int, ...],
    top_color: int,
    side_color: int,
) -> Grid:
    x0 = (
        "solid",
        "lead",
        "tail",
        "swap",
        "cross",
        "diamond",
    )
    x1 = ("solid",) if h == TWO else x0
    x2 = choice(x1)
    if x2 == "solid":
        return _solid_piece_291dc1e1(h, TWO, dominant)
    if x2 == "lead":
        x3 = accents[ZERO]
        x4 = accents[ONE] if len(accents) > ONE else top_color
        x5 = ((x3, dominant), (x4, dominant))
        x6 = tuple((dominant, dominant) for _ in range(h - TWO))
        return _rows_to_grid_291dc1e1(x5 + x6)
    if x2 == "tail":
        x3 = accents[ZERO]
        x4 = tuple((x3, dominant) for _ in range(h - TWO))
        x5 = tuple((x3, x3) for _ in range(TWO))
        return _rows_to_grid_291dc1e1(x4 + x5)
    if x2 == "swap":
        x3 = accents[ZERO]
        x4 = ((dominant, x3), (x3, dominant))
        x5 = tuple((x3, x3) for _ in range(h - TWO))
        return _rows_to_grid_291dc1e1(x4 + x5)
    if x2 == "cross":
        x3 = accents[ZERO]
        x4 = tuple((dominant, dominant) for _ in range(h - THREE))
        x5 = ((dominant, x3), (x3, dominant), (x3, dominant))
        return _rows_to_grid_291dc1e1(x4 + x5)
    x3 = accents[ZERO]
    x4 = dominant if h <= FOUR else side_color
    x5 = tuple((dominant, dominant) for _ in range((h - FOUR) // TWO))
    x6 = ((dominant, dominant), (dominant, x3), (x3, x4), (dominant, dominant))
    x7 = tuple((dominant, dominant) for _ in range(h - len(x5) - len(x6)))
    return _rows_to_grid_291dc1e1(x5 + x6 + x7)


def _bordered_canvas_291dc1e1(
    h: int,
    w: int,
    corner_right: bool,
    top_color: int,
    side_color: int,
) -> Grid:
    x0 = canvas(EIGHT, (h, w))
    x1 = fill(x0, top_color, connect((ZERO, ZERO), (ZERO, w - ONE)))
    if corner_right:
        x2 = connect((ONE, w - ONE), (h - ONE, w - ONE))
        x3 = fill(x1, side_color, x2)
        x4 = fill(x3, ZERO, initset((ZERO, w - ONE)))
        return x4
    x2 = connect((ONE, ZERO), (h - ONE, ZERO))
    x3 = fill(x1, side_color, x2)
    x4 = fill(x3, ZERO, initset((ZERO, ZERO)))
    return x4


def _paint_piece_291dc1e1(
    grid: Grid,
    piece: Grid,
    loc: tuple[int, int],
) -> Grid:
    x0 = shift(asobject(piece), loc)
    return paint(grid, x0)


def _build_row_major_291dc1e1(
    diff_lb: float,
    diff_ub: float,
    corner_right: bool,
) -> dict:
    while True:
        x0 = choice((FOUR, SIX, EIGHT))
        x1 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x2 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x3 = [choice(tuple(range(TWO, x0 + ONE, TWO))) for _ in range(x1)]
        x4 = [choice(tuple(range(TWO, x0 + ONE, TWO))) for _ in range(x2)]
        if randint(ZERO, ONE) == ZERO:
            x3[randint(ZERO, x1 - ONE)] = x0
        else:
            x4[randint(ZERO, x2 - ONE)] = x0
        x3 = tuple(x3)
        x4 = tuple(x4)
        x5 = sum(x3) + double(x1 - ONE)
        x6 = sum(x4) + double(x2 - ONE)
        x7 = max(x5, x6)
        if x7 <= 26:
            break
    x8 = randint(ZERO, 30 - (TWO + x7))
    x9 = TWO + x7 + x8
    x10 = _bordered_canvas_291dc1e1(EIGHT, x9, corner_right, ONE, TWO)
    x11 = tuple(choice(ROW_COLORS_291dc1e1) for _ in range(x1))
    x12 = tuple(choice(ROW_COLORS_291dc1e1) for _ in range(x2))
    x13 = tuple(_solid_piece_291dc1e1(TWO, w, c) for w, c in zip(x3, x11))
    x14 = tuple(_solid_piece_291dc1e1(TWO, w, c) for w, c in zip(x4, x12))
    x15 = x13 + x14
    if corner_right:
        x16 = x9 - THREE
        for x17 in (TWO, FIVE):
            x18 = x13 if x17 == TWO else x14
            x19 = x16
            for x20 in x18:
                x19 = x19 - width(x20) + ONE
                x10 = _paint_piece_291dc1e1(x10, x20, (x17, x19))
                x19 = x19 - THREE
    else:
        x16 = TWO
        for x17 in (TWO, FIVE):
            x18 = x13 if x17 == TWO else x14
            x19 = x16
            for x20 in x18:
                x10 = _paint_piece_291dc1e1(x10, x20, (x17, x19))
                x19 = x19 + width(x20) + TWO
    x21 = _stack_pieces_291dc1e1(x15)
    return {"input": x10, "output": x21}


def _build_vertical_tracks_291dc1e1(
    diff_lb: float,
    diff_ub: float,
    top_color: int,
    side_color: int,
) -> tuple[tuple[Grid, ...], tuple[Grid, ...]]:
    x0 = choice((SIX, EIGHT))
    while True:
        x1 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x2 = unifint(diff_lb, diff_ub, (TWO, FIVE))
        x3 = [choice(tuple(range(TWO, x0 + ONE, TWO))) for _ in range(x1 + x2)]
        x4 = randint(ZERO, len(x3) - ONE)
        x3[x4] = x0
        x5 = tuple(x3[:x1])
        x6 = tuple(x3[x1:])
        x7 = TWO + sum(x5) + double(x1)
        x8 = TWO + sum(x6) + double(x2)
        if max(x7, x8) <= 30:
            break
    x9 = []
    for x10 in x5:
        x11 = choice(VERTICAL_COLORS_291dc1e1)
        x12 = tuple(sample(remove(x11, VERTICAL_COLORS_291dc1e1), min(TWO, len(remove(x11, VERTICAL_COLORS_291dc1e1)))))
        x9.append(_make_vertical_piece_291dc1e1(x10, x11, x12, top_color, side_color))
    x13 = []
    for x14 in x6:
        x15 = choice(VERTICAL_COLORS_291dc1e1)
        x16 = tuple(sample(remove(x15, VERTICAL_COLORS_291dc1e1), min(TWO, len(remove(x15, VERTICAL_COLORS_291dc1e1)))))
        x13.append(_make_vertical_piece_291dc1e1(x14, x15, x16, top_color, side_color))
    return tuple(x9), tuple(x13)


def _build_column_major_291dc1e1(
    diff_lb: float,
    diff_ub: float,
    corner_right: bool,
) -> dict:
    x0 = _build_vertical_tracks_291dc1e1(diff_lb, diff_ub, TWO, ONE)
    x1, x2 = x0
    x3 = TWO
    x4 = TWO
    x5 = tuple(height(x6) for x6 in x1)
    x6 = tuple(height(x7) for x7 in x2)
    x7 = TWO + sum(x5) + double(len(x5))
    x8 = TWO + sum(x6) + double(len(x6))
    x9 = max(x7, x8)
    x10 = _bordered_canvas_291dc1e1(x9, EIGHT, corner_right, TWO, ONE)
    x11 = (ONE, FOUR) if corner_right else (TWO, FIVE)
    x12 = x3
    for x13 in x1:
        x10 = _paint_piece_291dc1e1(x10, x13, (x12, x11[ZERO]))
        x12 = x12 + height(x13) + x4
    x14 = x3
    for x15 in x2:
        x10 = _paint_piece_291dc1e1(x10, x15, (x14, x11[ONE]))
        x14 = x14 + height(x15) + x4
    x16 = (x2 + x1) if corner_right else (x1 + x2)
    x17 = tuple(rot270(x18) for x18 in x16)
    x18 = _stack_pieces_291dc1e1(x17)
    return {"input": x10, "output": x18}


def generate_291dc1e1(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = choice((T, F))
    x1 = choice((T, F))
    x2 = _build_column_major_291dc1e1 if x0 else _build_row_major_291dc1e1
    return x2(diff_lb, diff_ub, x1)
