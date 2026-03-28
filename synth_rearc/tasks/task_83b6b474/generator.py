from synth_rearc.core import *


def _hline_83b6b474(color_value: Integer, length: Integer) -> Object:
    x0 = frozenset((ZERO, j) for j in range(length))
    x1 = recolor(color_value, x0)
    return x1


def _vline_83b6b474(color_value: Integer, length: Integer) -> Object:
    x0 = frozenset((i, ZERO) for i in range(length))
    x1 = recolor(color_value, x0)
    return x1


def _tl_83b6b474(color_value: Integer, h: Integer, w: Integer) -> Object:
    x0 = frozenset((ZERO, j) for j in range(w))
    x1 = frozenset((i, ZERO) for i in range(h))
    x2 = recolor(color_value, combine(x0, x1))
    return x2


def _bl_83b6b474(color_value: Integer, h: Integer, w: Integer) -> Object:
    x0 = frozenset((h - ONE, j) for j in range(w))
    x1 = frozenset((i, ZERO) for i in range(h))
    x2 = recolor(color_value, combine(x0, x1))
    return x2


def _br_83b6b474(color_value: Integer, h: Integer, w: Integer) -> Object:
    x0 = frozenset((h - ONE, j) for j in range(w))
    x1 = frozenset((i, w - ONE) for i in range(h))
    x2 = recolor(color_value, combine(x0, x1))
    return x2


def _scatter_pieces_83b6b474(
    bg: Integer,
    pieces: tuple[Object, ...],
    out_shape: tuple[int, int],
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    x0 = len(pieces)
    x1 = max(height(piece) for piece in pieces)
    x2 = max(width(piece) for piece in pieces)
    x3 = out_shape[0] + out_shape[1] + x0
    x4 = min(20, max(x1 + THREE, unifint(diff_lb, diff_ub, (x3 - TWO, x3 + FOUR))))
    x5 = min(20, max(x2 + THREE, unifint(diff_lb, diff_ub, (x3 - TWO, x3 + FOUR))))
    x6 = tuple(sorted(pieces, key=lambda piece: (-len(piece), -height(piece), -width(piece), color(piece))))
    for _ in range(200):
        gi = canvas(bg, (x4, x5))
        reserved = frozenset()
        ok = T
        for piece in x6:
            locs = []
            ph = height(piece)
            pw = width(piece)
            for i in range(x4 - ph + ONE):
                for j in range(x5 - pw + ONE):
                    placed = shift(piece, (i, j))
                    halo = backdrop(outbox(placed))
                    if size(intersection(reserved, halo)) != ZERO:
                        continue
                    locs.append((placed, halo))
            if len(locs) == ZERO:
                ok = F
                break
            placed, halo = choice(locs)
            gi = paint(gi, placed)
            reserved = combine(reserved, halo)
        if ok and size(objects(gi, T, F, T)) == len(pieces):
            return gi
    raise RuntimeError("failed to scatter pieces")


def _build_case_ex1_83b6b474(
    bg: Integer,
    colors: tuple[Integer, ...],
    n: Integer,
) -> tuple[Grid, tuple[Object, ...]]:
    x0 = randint(TWO, n - TWO)
    x1 = n - x0
    x2 = randint(TWO, n - TWO)
    x3 = n - x2 - ONE
    x4 = _hline_83b6b474(colors[ZERO], n)
    x5 = _bl_83b6b474(colors[ONE], n - ONE, x0)
    x6 = _br_83b6b474(colors[TWO], x2, x1)
    x7 = _vline_83b6b474(colors[THREE], x3)
    x8 = shift(x4, (ZERO, ZERO))
    x9 = shift(x5, (ONE, ZERO))
    x10 = shift(x6, (n - x2, x0))
    x11 = shift(x7, (ONE, n - ONE))
    pieces = (x8, x9, x10, x11)
    go = canvas(bg, (n, n))
    for piece in pieces:
        go = paint(go, piece)
    return go, tuple(normalize(piece) for piece in pieces)


def _build_case_ex2_83b6b474(
    bg: Integer,
    colors: tuple[Integer, ...],
    n: Integer,
) -> tuple[Grid, tuple[Object, ...]]:
    x0 = randint(TWO, n - TWO)
    x1 = randint(TWO, n - TWO)
    x2 = randint(TWO, n - TWO)
    x3 = randint(TWO, n - TWO)
    x4 = n - x0
    x5 = n - x2
    x6 = n - x3 - ONE
    x7 = _tl_83b6b474(colors[ZERO], x0, x1)
    x8 = _hline_83b6b474(colors[ONE], n - x1)
    x9 = _vline_83b6b474(colors[TWO], x6)
    x10 = _bl_83b6b474(colors[THREE], x4, x2)
    x11 = _br_83b6b474(colors[FOUR], x3, x5)
    x12 = shift(x7, (ZERO, ZERO))
    x13 = shift(x8, (ZERO, x1))
    x14 = shift(x9, (ONE, n - ONE))
    x15 = shift(x10, (x0, ZERO))
    x16 = shift(x11, (n - x3, x2))
    pieces = (x12, x13, x14, x15, x16)
    go = canvas(bg, (n, n))
    for piece in pieces:
        go = paint(go, piece)
    return go, tuple(normalize(piece) for piece in pieces)


def _build_case_ex3_83b6b474(
    bg: Integer,
    colors: tuple[Integer, ...],
    n: Integer,
) -> tuple[Grid, tuple[Object, ...]]:
    x0 = randint(TWO, n - TWO)
    x1 = n - x0
    x2 = randint(TWO, n - TWO)
    x3 = n - x2 - ONE
    x4 = _hline_83b6b474(colors[ZERO], n - ONE)
    x5 = _vline_83b6b474(colors[ONE], x3)
    x6 = _bl_83b6b474(colors[TWO], x2, x1)
    x7 = _br_83b6b474(colors[THREE], n, x0)
    x8 = shift(x4, (ZERO, ZERO))
    x9 = shift(x5, (ONE, ZERO))
    x10 = shift(x6, (n - x2, ZERO))
    x11 = shift(x7, (ZERO, n - x0))
    pieces = (x8, x9, x10, x11)
    go = canvas(bg, (n, n))
    for piece in pieces:
        go = paint(go, piece)
    return go, tuple(normalize(piece) for piece in pieces)


def generate_83b6b474(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        n = unifint(diff_lb, diff_ub, (FOUR, EIGHT))
        template = choice(("ex1", "ex2", "ex3"))
        bg = randint(ZERO, NINE)
        ncolors = FOUR if template != "ex2" else FIVE
        palette_pool = tuple(c for c in range(TEN) if c != bg)
        colors = tuple(sample(palette_pool, ncolors))
        if template == "ex1":
            go, pieces = _build_case_ex1_83b6b474(bg, colors, n)
        elif template == "ex2":
            go, pieces = _build_case_ex2_83b6b474(bg, colors, n)
        else:
            go, pieces = _build_case_ex3_83b6b474(bg, colors, n)
        gi = _scatter_pieces_83b6b474(bg, pieces, shape(go), diff_lb, diff_ub)
        if mostcolor(gi) != bg:
            continue
        if gi == go:
            continue
        if not (FOUR <= height(go) <= EIGHT and FOUR <= width(go) <= EIGHT):
            continue
        return {"input": gi, "output": go}
