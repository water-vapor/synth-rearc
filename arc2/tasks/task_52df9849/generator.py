from arc2.core import *


GRID_SHAPE = (16, 16)
BG = 7
PALETTE = [1, 2, 3, 4, 5, 6, 8, 9]


def _rect_patch(top: int, left: int, height: int, width: int) -> Indices:
    return frozenset(
        (i, j)
        for i in range(top, top + height)
        for j in range(left, left + width)
    )


def _can_use(grid: Grid, patch: Indices) -> bool:
    return all(index(grid, loc) == BG for loc in patch)


def _paint_rect(grid: Grid, color: int, top: int, left: int, height: int, width: int) -> Grid:
    return fill(grid, color, _rect_patch(top, left, height, width))


def _take_color(colors: list[int]) -> int:
    return colors.pop()


def _add_l_rect(
    gi: Grid,
    go: Grid,
    colors: list[int],
    diff_lb: float,
    diff_ub: float,
):
    if len(colors) < 2:
        return gi, go, F
    for _ in range(200):
        x0 = unifint(diff_lb, diff_ub, (4, 7))
        x1 = unifint(diff_lb, diff_ub, (4, 7))
        x2 = randint(0, GRID_SHAPE[0] - x0)
        x3 = randint(0, GRID_SHAPE[1] - x1)
        x4 = randint(1, x0 - 1)
        x5 = randint(1, x1 - 1)
        x6 = choice(("tr", "tl", "br", "bl"))
        x7 = _rect_patch(x2, x3, x0, x1)
        if x6 == "tr":
            x8 = _rect_patch(x2 + x4, x3, x0 - x4, x1 - x5)
            x9 = x2 + x4
            x10 = x3 - randint(0, min(3, x3))
            x11 = x0 - x4 + randint(0, min(3, GRID_SHAPE[0] - (x2 + x0)))
            x12 = x1 - x5 + (x3 - x10)
        elif x6 == "tl":
            x8 = _rect_patch(x2 + x4, x3 + x5, x0 - x4, x1 - x5)
            x9 = x2 + x4
            x10 = x3 + x5
            x11 = x0 - x4 + randint(0, min(3, GRID_SHAPE[0] - (x2 + x0)))
            x12 = x1 - x5 + randint(0, min(3, GRID_SHAPE[1] - (x3 + x1)))
        elif x6 == "br":
            x8 = _rect_patch(x2, x3, x0 - x4, x1 - x5)
            x13 = randint(0, min(3, x2))
            x14 = randint(0, min(3, x3))
            x9 = x2 - x13
            x10 = x3 - x14
            x11 = x0 - x4 + x13
            x12 = x1 - x5 + x14
        else:
            x8 = _rect_patch(x2, x3 + x5, x0 - x4, x1 - x5)
            x13 = randint(0, min(3, x2))
            x9 = x2 - x13
            x10 = x3 + x5
            x11 = x0 - x4 + x13
            x12 = x1 - x5 + randint(0, min(3, GRID_SHAPE[1] - (x3 + x1)))
        x15 = _rect_patch(x9, x10, x11, x12)
        x16 = difference(x7, x8)
        x17 = combine(x7, x15)
        if x16 == x7 or not _can_use(go, x17):
            continue
        x18 = _take_color(colors)
        x19 = _take_color(colors)
        gi = fill(gi, x19, x15)
        go = fill(go, x19, x15)
        gi = fill(gi, x18, x16)
        go = fill(go, x18, x7)
        return gi, go, T
    return gi, go, F


def _split_intervals(span: int, count: int):
    for _ in range(100):
        x0 = []
        for _ in range(count):
            x1 = randint(1, min(3, span - 2))
            x2 = randint(1, max(1, span - x1 - 1))
            x3 = (x2, x2 + x1)
            if any(not (x3[1] <= y0 or y1 <= x3[0]) for y0, y1 in x0):
                break
            x0.append(x3)
        else:
            x0 = sorted(x0)
            if x0[0][0] > 0 and x0[-1][1] < span:
                return tuple(x0)
    return tuple()


def _add_band(
    gi: Grid,
    go: Grid,
    colors: list[int],
    diff_lb: float,
    diff_ub: float,
):
    if len(colors) < 3:
        return gi, go, F
    for _ in range(200):
        x0 = choice(("h", "v"))
        x1 = unifint(diff_lb, diff_ub, (2, 4))
        x2 = unifint(diff_lb, diff_ub, (10, 14))
        if x0 == "h":
            x3 = randint(0, GRID_SHAPE[0] - x1)
            x4 = randint(0, GRID_SHAPE[1] - x2)
        else:
            x3 = randint(0, GRID_SHAPE[0] - x2)
            x4 = randint(0, GRID_SHAPE[1] - x1)
        x5 = randint(1, min(3, len(colors) - 1))
        x6 = _split_intervals(x2, x5)
        if len(x6) != x5:
            continue
        if x0 == "h":
            x7 = _rect_patch(x3, x4, x1, x2)
            x8 = tuple(_rect_patch(x3, x4 + a, x1, b - a) for a, b in x6)
            x9 = []
            for a, b in x6:
                x10 = randint(0, min(4, x3))
                x11 = randint(0, min(4, GRID_SHAPE[0] - (x3 + x1)))
                x12 = _rect_patch(x3 - x10, x4 + a, x1 + x10 + x11, b - a)
                x9.append(x12)
        else:
            x7 = _rect_patch(x3, x4, x2, x1)
            x8 = tuple(_rect_patch(x3 + a, x4, b - a, x1) for a, b in x6)
            x9 = []
            for a, b in x6:
                x10 = randint(0, min(4, x4))
                x11 = randint(0, min(4, GRID_SHAPE[1] - (x4 + x1)))
                x12 = _rect_patch(x3 + a, x4 - x10, b - a, x1 + x10 + x11)
                x9.append(x12)
        x13 = merge(x8)
        x14 = difference(x7, x13)
        x15 = combine(x7, merge(x9))
        if not _can_use(go, x15):
            continue
        x16 = _take_color(colors)
        for x17 in x9:
            x18 = _take_color(colors)
            gi = fill(gi, x18, x17)
            go = fill(go, x18, x17)
        gi = fill(gi, x16, x14)
        go = fill(go, x16, x7)
        return gi, go, T
    return gi, go, F


def _add_cross_line(
    gi: Grid,
    go: Grid,
    colors: list[int],
):
    if len(colors) < 2:
        return gi, go, F
    for _ in range(200):
        x0 = choice(("h", "v"))
        if x0 == "h":
            x1 = randint(1, GRID_SHAPE[0] - 2)
            x2 = randint(0, GRID_SHAPE[1] - 10)
            x3 = randint(x2 + 7, min(GRID_SHAPE[1] - 1, x2 + 11))
            x4 = randint(x2 + 1, x3 - 1)
            x5 = randint(0, max(0, x1 - 5))
            x6 = randint(min(GRID_SHAPE[0] - 1, x1 + 5), GRID_SHAPE[0] - 1)
            x7 = frozenset((x1, j) for j in range(x2, x3 + 1))
            x8 = frozenset((i, x4) for i in range(x5, x6 + 1))
            x9 = difference(x7, frozenset({(x1, x4)}))
        else:
            x1 = randint(1, GRID_SHAPE[1] - 2)
            x2 = randint(0, GRID_SHAPE[0] - 10)
            x3 = randint(x2 + 7, min(GRID_SHAPE[0] - 1, x2 + 11))
            x4 = randint(x2 + 1, x3 - 1)
            x5 = randint(0, max(0, x1 - 5))
            x6 = randint(min(GRID_SHAPE[1] - 1, x1 + 5), GRID_SHAPE[1] - 1)
            x7 = frozenset((i, x1) for i in range(x2, x3 + 1))
            x8 = frozenset((x4, j) for j in range(x5, x6 + 1))
            x9 = difference(x7, frozenset({(x4, x1)}))
        x10 = combine(x7, x8)
        if not _can_use(go, x10):
            continue
        x11 = _take_color(colors)
        x12 = _take_color(colors)
        gi = fill(gi, x12, x8)
        go = fill(go, x12, x8)
        gi = fill(gi, x11, x9)
        go = fill(go, x11, x7)
        return gi, go, T
    return gi, go, F


def _add_diag_line(
    gi: Grid,
    go: Grid,
    colors: list[int],
):
    if len(colors) < 2:
        return gi, go, F
    for _ in range(200):
        x0 = randint(10, 14)
        x1 = choice(("dr", "dl"))
        if x1 == "dr":
            x2 = randint(0, GRID_SHAPE[0] - x0)
            x3 = randint(0, GRID_SHAPE[1] - x0)
            x4 = tuple((x2 + k, x3 + k) for k in range(x0))
        else:
            x2 = randint(0, GRID_SHAPE[0] - x0)
            x3 = randint(x0 - 1, GRID_SHAPE[1] - 1)
            x4 = tuple((x2 + k, x3 - k) for k in range(x0))
        x5 = randint(2, min(4, x0 - 4))
        x6 = randint(2, x0 - x5 - 2)
        x7 = frozenset(x4)
        x8 = frozenset(x4[x6:x6 + x5])
        x9 = minimum(frozenset(i for i, _ in x8))
        x10 = maximum(frozenset(i for i, _ in x8))
        x11 = minimum(frozenset(j for _, j in x8))
        x12 = maximum(frozenset(j for _, j in x8))
        x13 = randint(0, 1)
        x14 = randint(0, 1)
        x15 = max(0, x9 - x13)
        x16 = max(0, x11 - x14)
        x17 = min(GRID_SHAPE[0] - 1, x10 + x13)
        x18 = min(GRID_SHAPE[1] - 1, x12 + x14)
        x19 = _rect_patch(x15, x16, x17 - x15 + 1, x18 - x16 + 1)
        x20 = difference(x7, x19)
        x21 = combine(x7, x19)
        if x20 == x7 or not _can_use(go, x21):
            continue
        x22 = _take_color(colors)
        x23 = _take_color(colors)
        gi = fill(gi, x23, x19)
        go = fill(go, x23, x19)
        gi = fill(gi, x22, x20)
        go = fill(go, x22, x7)
        return gi, go, T
    return gi, go, F


def generate_52df9849(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = canvas(BG, GRID_SHAPE)
        x1 = x0
        x2 = list(PALETTE)
        shuffle(x2)
        x3 = [_add_l_rect, _add_band, _add_cross_line, _add_diag_line]
        shuffle(x3)
        x4 = unifint(diff_lb, diff_ub, (1, 2))
        x5 = []
        for x6 in x3:
            if len(x5) == x4:
                break
            if x6 is _add_l_rect or x6 is _add_band:
                x0, x1, x7 = x6(x0, x1, x2, diff_lb, diff_ub)
            else:
                x0, x1, x7 = x6(x0, x1, x2)
            if x7:
                x5.append(x6.__name__)
        if len(x5) == ZERO or x0 == x1:
            continue
        return {"input": x0, "output": x1}
