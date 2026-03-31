from __future__ import annotations

from synth_rearc.core import *


def _patch_from_cells_4c7dc4dd(cells: frozenset[tuple[int, int]]) -> frozenset[tuple[int, int]]:
    return frozenset(cells)


def _repeat_background_4c7dc4dd(height_: int, width_: int, tile: tuple[tuple[int, ...], ...]) -> Grid:
    x0 = len(tile)
    x1 = len(tile[ZERO])
    x2 = []
    for x3 in range(height_):
        x4 = []
        for x5 in range(width_):
            x4.append(tile[x3 % x0][x5 % x1])
        x2.append(tuple(x4))
    return tuple(x2)


def _background_4c7dc4dd(colors: tuple[int, ...]) -> Grid:
    x0 = colors[ZERO]
    x1 = colors[ONE]
    if choice((True, False)):
        x2 = (
            (x0, x1),
            (x1, x0),
        )
    else:
        x2 = (
            (x0, x1, x0),
            (x1, x0, x1),
        )
    return _repeat_background_4c7dc4dd(30, 30, x2)


def _side_cells_4c7dc4dd(top_left: tuple[int, int], size: int, side: str) -> frozenset[tuple[int, int]]:
    x0, x1 = top_left
    x2 = x0 + size - ONE
    x3 = x1 + size - ONE
    if side == "top":
        return frozenset((x0, x4) for x4 in range(x1, x3 + ONE))
    if side == "bottom":
        return frozenset((x2, x4) for x4 in range(x1, x3 + ONE))
    if side == "left":
        return frozenset((x4, x1) for x4 in range(x0, x2 + ONE))
    return frozenset((x4, x3) for x4 in range(x0, x2 + ONE))


def _ornament_4c7dc4dd(
    grid: Grid,
    top_left: tuple[int, int],
    outer: int,
    color: int,
) -> Grid:
    if choice((True, False)):
        x0 = choice(("left", "right"))
        x1 = _side_cells_4c7dc4dd(add(top_left, (-ONE, -ONE)), outer + TWO, x0)
        if choice((True, False)):
            x1 = combine(x1, _side_cells_4c7dc4dd(add(top_left, (-ONE, -ONE)), outer + TWO, choice(("top", "bottom"))))
        return fill(grid, color, x1)
    x0 = set()
    x1 = add(top_left, (-ONE, -ONE))
    x2 = ("top", "left", "bottom", "right")
    x3 = choice(tuple(x4 for x4 in x2))
    for x4 in x2:
        if x4 != x3:
            x0 |= _side_cells_4c7dc4dd(x1, outer + TWO, x4)
    return fill(grid, color, frozenset(x0))


def _paint_panel_4c7dc4dd(
    grid: Grid,
    top_left: tuple[int, int],
    inner: Grid,
    frame_color: int,
) -> Grid:
    x0 = len(inner)
    x1 = add(top_left, (ONE, ONE))
    x2 = fill(canvas(frame_color, (x0 + TWO, x0 + TWO)), frame_color, asindices(canvas(frame_color, (x0 + TWO, x0 + TWO))))
    x3 = paint(grid, shift(asobject(x2), top_left))
    return paint(x3, shift(asobject(inner), x1))


def _connect_axis_4c7dc4dd(a: tuple[int, int], b: tuple[int, int]) -> frozenset[tuple[int, int]]:
    x0, x1 = a
    x2, x3 = b
    if x0 == x2:
        x4 = ONE if x3 >= x1 else NEG_ONE
        return frozenset((x0, x5) for x5 in range(x1, x3 + x4, x4))
    x4 = ONE if x2 >= x0 else NEG_ONE
    return frozenset((x5, x1) for x5 in range(x0, x2 + x4, x4))


def _paint_points_4c7dc4dd(base: Grid, points: tuple[tuple[int, tuple[int, int]], ...]) -> Grid:
    return paint(base, frozenset(points))


def _path_seed_4c7dc4dd(n: int, main: int, accent: int) -> tuple[Grid, Grid]:
    while True:
        if choice((True, False)):
            x0 = randint(ONE, n - THREE)
            x1 = randint(ONE, n - THREE)
            x2 = randint(x0 + ONE, n - ONE)
            x3 = randint(x1 + ONE, n - ONE)
            x4 = ((x0, x1), (x0, x3), (x2, x3))
        else:
            x0 = randint(ONE, n - THREE)
            x1 = randint(TWO, n - ONE)
            x2 = randint(ONE, n - THREE)
            x3 = randint(x2 + ONE, n - ONE)
            x4 = ((x0, x1), (x3, x1), (x3, x2))
        if choice((True, False)):
            if x4[ZERO][ZERO] > ZERO:
                x5 = ((x4[ZERO][ZERO] - ONE, x4[ZERO][ONE]),) + x4
            elif x4[NEG_ONE][ONE] < n - ONE:
                x5 = x4 + ((x4[NEG_ONE][ZERO], x4[NEG_ONE][ONE] + ONE),)
            else:
                x5 = x4
        else:
            x5 = x4
        if len(set(x5)) != len(x5):
            continue
        x6 = canvas(ZERO, (n, n))
        x7 = x6
        for x8, x9 in zip(x5, x5[ONE:]):
            x7 = fill(x7, main, _connect_axis_4c7dc4dd(x8, x9))
        x10 = []
        for x11, x12 in enumerate(x5):
            x13 = accent if ZERO < x11 < len(x5) - ONE else main
            x10.append((x13, x12))
        x14 = _paint_points_4c7dc4dd(canvas(ZERO, (n, n)), tuple(x10))
        x15 = _paint_points_4c7dc4dd(x7, tuple(x10))
        if x14 != x15:
            return x14, x15


def _full_solid_4c7dc4dd(n: int, color: int) -> Grid:
    return canvas(color, (n, n))


def _complement_4c7dc4dd(full: Grid, seed: Grid) -> Grid:
    x0 = []
    for x1, x2 in zip(full, seed):
        x3 = []
        for x4, x5 in zip(x1, x2):
            x3.append(ZERO if x5 != ZERO else x4)
        x0.append(tuple(x3))
    return tuple(x0)


def _random_solid_seed_4c7dc4dd(n: int, color: int) -> Grid:
    x0 = canvas(ZERO, (n, n))
    x1 = randint(ONE, n - TWO)
    x2 = randint(ONE, n - TWO)
    x3 = choice(("el", "tee", "bar"))
    if x3 == "bar":
        if choice((True, False)):
            x4 = frozenset((x1, x5) for x5 in range(randint(ZERO, n - THREE), randint(TWO, n - ONE) + ONE))
        else:
            x4 = frozenset((x5, x2) for x5 in range(randint(ZERO, n - THREE), randint(TWO, n - ONE) + ONE))
    elif x3 == "tee":
        x4 = frozenset((x1, x5) for x5 in range(max(ZERO, x2 - ONE), min(n, x2 + TWO)))
        x4 = combine(x4, frozenset((x5, x2) for x5 in range(max(ZERO, x1 - ONE), min(n, x1 + TWO))))
    else:
        x5 = randint(ZERO, n - TWO)
        x6 = randint(ZERO, n - TWO)
        x7 = randint(x5 + ONE, n - ONE)
        x8 = randint(x6 + ONE, n - ONE)
        x4 = combine(frozenset((x5, x9) for x9 in range(x6, x8 + ONE)), frozenset((x9, x6) for x9 in range(x5, x7 + ONE)))
    return fill(x0, color, x4)


def _checkerboard_4c7dc4dd(n: int, a: int, b: int) -> Grid:
    x0 = []
    for x1 in range(n):
        x2 = []
        for x3 in range(n):
            x2.append(branch(even(x1 + x3), a, b))
        x0.append(tuple(x2))
    return tuple(x0)


def _plus_seed_4c7dc4dd(full: Grid) -> Grid:
    x0 = len(full)
    x1 = x0 // TWO
    x2 = frozenset({
        (x1 - ONE, x1),
        (x1, x1 - ONE),
        (x1, x1),
        (x1, x1 + ONE),
        (x1 + ONE, x1),
    })
    x3 = canvas(ZERO, (x0, x0))
    x4 = set()
    for x5, x6 in x2:
        x4.add((full[x5][x6], (x5, x6)))
    return paint(x3, frozenset(x4))


def _corner_seed_4c7dc4dd(n: int, main: int, accent: int, corner: str) -> tuple[Grid, Grid]:
    x0 = canvas(ZERO, (n, n))
    if corner == "tl":
        x1 = ((accent, (ZERO, ONE)), (accent, (ONE, ZERO)), (main, (ONE, ONE)))
    elif corner == "tr":
        x1 = ((accent, (ZERO, n - TWO)), (accent, (ONE, n - ONE)), (main, (ONE, n - TWO)))
    elif corner == "bl":
        x1 = ((accent, (n - TWO, ZERO)), (accent, (n - ONE, ONE)), (main, (n - TWO, ONE)))
    else:
        x1 = ((accent, (n - TWO, n - ONE)), (accent, (n - ONE, n - TWO)), (main, (n - TWO, n - TWO)))
    x2 = paint(x0, frozenset(x1))
    x3 = canvas(main, (n, n))
    x4 = frozenset({(ZERO, ZERO), (ZERO, n - ONE), (n - ONE, ZERO), (n - ONE, n - ONE)})
    x5 = frozenset({
        (ZERO, ONE),
        (ONE, ZERO),
        (ZERO, n - TWO),
        (ONE, n - ONE),
        (n - TWO, ZERO),
        (n - ONE, ONE),
        (n - TWO, n - ONE),
        (n - ONE, n - TWO),
    })
    x6 = fill(x3, ZERO, x4)
    x7 = fill(x6, accent, x5)
    return x2, x7


def _pick_layout_4c7dc4dd(n: int) -> tuple[tuple[int, int], ...]:
    x0 = n + TWO
    x1 = randint(TWO, SIX)
    x2 = randint(TWO, SIX)
    x3 = randint(max(TEN, x1 + x0 + FOUR), 30 - x0 - TWO)
    x4 = randint(max(TEN, x2 + x0 + FOUR), 30 - x0 - TWO)
    x5 = (x1, x2)
    x6 = (x1 + randint(NEG_ONE, ONE), x4)
    x7 = (x3, x2 + randint(NEG_ONE, ONE))
    x8 = (x3 + randint(NEG_ONE, ONE), x4 + randint(NEG_ONE, ONE))
    return (x5, x6, x7, x8)


def _quadrant_assignment_4c7dc4dd() -> tuple[tuple[int, int], int, int]:
    if choice((True, False)):
        x0 = choice((ZERO, ONE))
        x1 = (x0, ZERO)
        x2 = (x0, ONE)
        x3 = choice((ZERO, ONE))
        x4 = (ONE - x0, x3)
    else:
        x0 = choice((ZERO, ONE))
        x1 = (ZERO, x0)
        x2 = (ONE, x0)
        x3 = choice((ZERO, ONE))
        x4 = (x3, ONE - x0)
    x5 = {(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE)}
    x6 = next(iter(x5 - {x1, x2, x4}))
    return (x1, x2, x4, x6)


def _to_index_4c7dc4dd(pos: tuple[int, int]) -> int:
    return pos[ZERO] * TWO + pos[ONE]


def _find_panels_generated_4c7dc4dd(I: Grid) -> tuple[int, tuple[Grid, ...]]:
    x0 = height(I)
    x1 = width(I)
    x2 = []
    for x3 in range(TWO, min(x0, x1) - ONE):
        x4 = x3 + TWO
        for x5 in range(x0 - x4 + ONE):
            for x6 in range(x1 - x4 + ONE):
                x7 = (
                    [(x5, x8) for x8 in range(x6, x6 + x4)] +
                    [(x5 + x4 - ONE, x8) for x8 in range(x6, x6 + x4)] +
                    [(x8, x6) for x8 in range(x5 + ONE, x5 + x4 - ONE)] +
                    [(x8, x6 + x4 - ONE) for x8 in range(x5 + ONE, x5 + x4 - ONE)]
                )
                x9 = {I[x10][x11] for x10, x11 in x7}
                if len(x9) == ONE and next(iter(x9)) != ZERO:
                    x2.append((x3, x5, x6))
    x10 = max(x11 for x11, _, _ in x2)
    x12 = sorted((x13, x14) for x11, x13, x14 in x2 if x11 == x10)
    x15 = tuple(crop(I, (x16 + ONE, x17 + ONE), (x10, x10)) for x16, x17 in x12)
    return x10, x15


def _valid_input_4c7dc4dd(I: Grid, inner_size: int) -> bool:
    try:
        x0, x1 = _find_panels_generated_4c7dc4dd(I)
    except Exception:
        return False
    if x0 != inner_size or len(x1) != FOUR:
        return False
    x2 = tuple(_nonzero_indices_4c7dc4dd(x3) for x3 in x1)
    x3 = tuple(tuple(sorted({x4 for x5 in x6 for x4 in x5 if x4 != ZERO})) for x6 in x1)
    x4 = tuple(x5 for x5, x6 in enumerate(x2) if len(x6) > ZERO)
    if len(x4) != THREE:
        return False
    for x5 in range(len(x4)):
        for x6 in range(x5 + ONE, len(x4)):
            if x3[x4[x5]] == x3[x4[x6]]:
                return True
    return False


def generate_4c7dc4dd(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(("path", "solid", "checker", "corner"))
        if x0 == "checker":
            x1 = choice((FIVE, SEVEN))
        elif x0 == "corner":
            x1 = unifint(diff_lb, diff_ub, (FIVE, SEVEN))
        else:
            x1 = unifint(diff_lb, diff_ub, (FOUR, SIX))
        x2 = tuple(x3 for x3 in interval(ONE, TEN, ONE))
        x3 = sample(x2, NINE)
        x4 = tuple(x3[:TWO])
        x5 = _background_4c7dc4dd(x4)
        x6 = tuple(x3[len(x4):])
        x7, x8, x9, x10 = _quadrant_assignment_4c7dc4dd()
        x11 = _pick_layout_4c7dc4dd(x1)
        x12 = [canvas(ZERO, (x1, x1)) for _ in range(FOUR)]
        x13 = {
            _to_index_4c7dc4dd((ZERO, ZERO)): x6[-THREE],
            _to_index_4c7dc4dd((ZERO, ONE)): x6[-TWO],
            _to_index_4c7dc4dd((ONE, ZERO)): x6[-ONE],
            _to_index_4c7dc4dd((ONE, ONE)): x6[-THREE],
        }
        if x0 == "path":
            x14 = x6[ZERO]
            x15 = x6[ONE]
            x16 = x6[TWO]
            x17, x18 = _path_seed_4c7dc4dd(x1, x14, x15)
            x19, x20 = _path_seed_4c7dc4dd(x1, x16, x15)
            x12[_to_index_4c7dc4dd(x7)] = branch(choice((True, False)), x17, x18)
            x12[_to_index_4c7dc4dd(x8)] = branch(x12[_to_index_4c7dc4dd(x7)] == x17, x18, x17)
            x12[_to_index_4c7dc4dd(x9)] = x19
            x12[_to_index_4c7dc4dd(x10)] = canvas(ZERO, (x1, x1))
            x21 = x20
        elif x0 == "solid":
            x14 = x6[ZERO]
            x15 = x6[ONE]
            x16 = _random_solid_seed_4c7dc4dd(x1, x14)
            x17 = _complement_4c7dc4dd(_full_solid_4c7dc4dd(x1, x14), x16)
            x18 = _random_solid_seed_4c7dc4dd(x1, x15)
            x19 = _complement_4c7dc4dd(_full_solid_4c7dc4dd(x1, x15), x18)
            if choice((True, False)):
                x12[_to_index_4c7dc4dd(x7)] = x16
                x12[_to_index_4c7dc4dd(x8)] = x17
            else:
                x12[_to_index_4c7dc4dd(x7)] = x17
                x12[_to_index_4c7dc4dd(x8)] = x16
            x12[_to_index_4c7dc4dd(x9)] = x18
            x12[_to_index_4c7dc4dd(x10)] = canvas(ZERO, (x1, x1))
            x21 = x19
        elif x0 == "checker":
            x14 = x6[ZERO]
            x15 = x6[ONE]
            x16 = x6[TWO]
            x17 = x6[THREE]
            x18 = _checkerboard_4c7dc4dd(x1, x14, x15)
            x19 = _plus_seed_4c7dc4dd(x18)
            x20 = _complement_4c7dc4dd(x18, x19)
            x21 = _checkerboard_4c7dc4dd(x1, x16, x17)
            x22 = _plus_seed_4c7dc4dd(x21)
            if choice((True, False)):
                x12[_to_index_4c7dc4dd(x7)] = x19
                x12[_to_index_4c7dc4dd(x8)] = x20
            else:
                x12[_to_index_4c7dc4dd(x7)] = x20
                x12[_to_index_4c7dc4dd(x8)] = x19
            x12[_to_index_4c7dc4dd(x9)] = x22
            x12[_to_index_4c7dc4dd(x10)] = canvas(ZERO, (x1, x1))
            x21 = _complement_4c7dc4dd(x21, x22)
        else:
            x14 = x6[ZERO]
            x15 = x6[ONE]
            x16 = x6[TWO]
            x17 = x6[THREE]
            x18 = choice(("tl", "tr", "bl", "br"))
            x19 = choice(tuple(x20 for x20 in ("tl", "tr", "bl", "br") if x20 != x18))
            x20, x21 = _corner_seed_4c7dc4dd(x1, x14, x15, x18)
            x22, x23 = _corner_seed_4c7dc4dd(x1, x16, x17, x19)
            if choice((True, False)):
                x12[_to_index_4c7dc4dd(x7)] = x21
                x12[_to_index_4c7dc4dd(x8)] = x20
            else:
                x12[_to_index_4c7dc4dd(x7)] = x20
                x12[_to_index_4c7dc4dd(x8)] = x21
            x12[_to_index_4c7dc4dd(x9)] = x22
            x12[_to_index_4c7dc4dd(x10)] = canvas(ZERO, (x1, x1))
            x21 = x23
        x22 = x5
        for x23, x24 in enumerate(x11):
            x22 = _paint_panel_4c7dc4dd(x22, x24, x12[x23], x13[x23])
        x23 = x12[_to_index_4c7dc4dd(x10)]
        if len(_nonzero_indices_4c7dc4dd(x23)) != ZERO:
            continue
        if not _valid_input_4c7dc4dd(x22, x1):
            continue
        return {"input": x22, "output": x21}


def _nonzero_indices_4c7dc4dd(G: Grid) -> frozenset[tuple[int, int]]:
    return frozenset((x0, x1) for x0, x2 in enumerate(G) for x1, x3 in enumerate(x2) if x3 != ZERO)
