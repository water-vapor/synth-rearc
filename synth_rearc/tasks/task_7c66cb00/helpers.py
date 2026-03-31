from __future__ import annotations

from synth_rearc.core import *


GRID_SHAPE_7C66CB00 = (30, 24)


def rectangle_indices_7c66cb00(
    upper_left: IntegerTuple,
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = upper_left
    x2, x3 = dims
    return frozenset(
        (i, j)
        for i in range(x0, add(x0, x2))
        for j in range(x1, add(x1, x3))
    )


def render_input_7c66cb00(
    bg: Integer,
    bands: tuple[tuple[Integer, Integer, Integer, Integer], ...],
    motifs: tuple[Object, ...],
) -> Grid:
    x0 = canvas(bg, GRID_SHAPE_7C66CB00)
    x1, x2 = GRID_SHAPE_7C66CB00
    for x3, x4, x5, x6 in bands:
        x7 = rectangle_indices_7c66cb00((x3, ZERO), (subtract(x4, x3) + ONE, x2))
        x8 = frozenset((i, ZERO) for i in range(x3, add(x4, ONE)))
        x9 = frozenset((i, subtract(x2, ONE)) for i in range(x3, add(x4, ONE)))
        x0 = fill(x0, x5, x7)
        x0 = fill(x0, x6, combine(x8, x9))
    for x10 in motifs:
        x0 = paint(x0, x10)
    return x0


def render_output_7c66cb00(
    grid: Grid,
    bg: Integer,
    bands: tuple[tuple[Integer, Integer, Integer, Integer], ...],
    motifs: tuple[Object, ...],
) -> Grid:
    x0 = grid
    for x1 in motifs:
        x0 = fill(x0, bg, x1)
    for _, x2, x3, x4 in bands:
        for x5 in motifs:
            x6 = sfilter(x5, matcher(first, x3))
            if len(x6) == ZERO:
                continue
            x7 = subtract(x2, lowermost(x6))
            x8 = shift(x6, (x7, ZERO))
            x0 = fill(x0, x4, x8)
    return x0


def padded_bbox_7c66cb00(
    obj: Object,
) -> tuple[Integer, Integer, Integer, Integer]:
    x0, x1 = ulcorner(obj)
    x2, x3 = lrcorner(obj)
    x4, x5 = GRID_SHAPE_7C66CB00
    return (
        max(ZERO, subtract(x0, ONE)),
        max(ZERO, subtract(x1, ONE)),
        min(subtract(x4, ONE), add(x2, ONE)),
        min(subtract(x5, ONE), add(x3, ONE)),
    )


def padded_indices_7c66cb00(
    obj: Object,
) -> Indices:
    x0, x1, x2, x3 = padded_bbox_7c66cb00(obj)
    return rectangle_indices_7c66cb00((x0, x1), (subtract(x2, x0) + ONE, subtract(x3, x1) + ONE))


def place_motif_7c66cb00(
    obj: Object,
    max_bottom: Integer,
    occupied: Indices,
) -> tuple[Object, Indices] | None:
    x0 = height(obj)
    x1 = width(obj)
    if max_bottom < x0:
        return None
    x2 = subtract(max_bottom, x0) + ONE
    x3 = subtract(subtract(GRID_SHAPE_7C66CB00[1], x1), ONE)
    if either(x2 < ONE, x3 < ONE):
        return None
    for _ in range(200):
        x4 = randint(ONE, x2)
        x5 = randint(ONE, x3)
        x6 = shift(obj, (x4, x5))
        x7 = padded_indices_7c66cb00(x6)
        if len(intersection(x7, occupied)) > ZERO:
            continue
        return x6, x7
    return None


def _solid_motif_7c66cb00(
    color_value: Integer,
    height_cap: Integer,
) -> Object:
    x0 = randint(TWO, min(FOUR, height_cap))
    x1 = randint(TWO, FOUR)
    x2 = rectangle_indices_7c66cb00(ORIGIN, (x0, x1))
    return recolor(color_value, x2)


def _diamond_motif_7c66cb00(
    color_value: Integer,
    height_cap: Integer,
) -> Object:
    if height_cap >= FIVE and choice((T, F)):
        x0 = frozenset(
            (i, j)
            for i in range(FIVE)
            for j in range(FIVE)
            if abs(subtract(i, TWO)) + abs(subtract(j, TWO)) <= TWO
        )
        return recolor(color_value, x0)
    x0 = frozenset(
        {
            (ZERO, ONE),
            (ZERO, TWO),
            (ONE, ZERO),
            (ONE, ONE),
            (ONE, TWO),
            (ONE, THREE),
            (TWO, ONE),
            (TWO, TWO),
        }
    )
    return recolor(color_value, x0)


def _notched_rect_motif_7c66cb00(
    color_value: Integer,
    height_cap: Integer,
) -> Object:
    x0 = randint(THREE, min(FOUR, height_cap))
    x1 = randint(FIVE, SEVEN)
    x2 = set(rectangle_indices_7c66cb00(ORIGIN, (x0, x1)))
    x3 = randint(ONE, TWO)
    for _ in range(x3):
        x4 = randint(ONE, subtract(x1, TWO))
        x5 = choice((subtract(x0, ONE), subtract(x0, TWO) if x0 > THREE else subtract(x0, ONE)))
        x2.discard((x5, x4))
    if len(x2) == ZERO:
        x2.add((ZERO, ZERO))
    return recolor(color_value, frozenset(x2))


def _ring_motif_7c66cb00(
    colors: tuple[Integer, Integer],
    height_cap: Integer,
) -> Object:
    x0, x1 = colors
    x2 = randint(THREE, min(FIVE, height_cap))
    x3 = randint(THREE, FIVE)
    x4 = set()
    for i in range(x2):
        for j in range(x3):
            x5 = x0 if either(either(i == ZERO, i == subtract(x2, ONE)), either(j == ZERO, j == subtract(x3, ONE))) else x1
            x4.add((x5, (i, j)))
    return frozenset(x4)


def _stripe_motif_7c66cb00(
    colors: tuple[Integer, Integer],
    height_cap: Integer,
) -> Object:
    x0, x1 = colors
    x2 = randint(THREE, min(FIVE, height_cap))
    x3 = randint(FOUR, SEVEN)
    x4 = {(x0, (i, j)) for i in range(x2) for j in range(x3)}
    if choice((T, F)):
        x5 = randint(ONE, subtract(x2, TWO))
        x6 = randint(ONE, max(ONE, subtract(x3, THREE)))
        x7 = randint(add(x6, ONE), subtract(x3, ONE))
        for j in range(x6, x7):
            x4.discard((x0, (x5, j)))
            x4.add((x1, (x5, j)))
    else:
        x5 = randint(ONE, subtract(x3, TWO))
        x6 = randint(ONE, max(ONE, subtract(x2, THREE)))
        x7 = randint(add(x6, ONE), subtract(x2, ONE))
        for i in range(x6, x7):
            x4.discard((x0, (i, x5)))
            x4.add((x1, (i, x5)))
    return frozenset(x4)


def _windows_motif_7c66cb00(
    colors: tuple[Integer, Integer],
    height_cap: Integer,
) -> Object:
    x0, x1 = colors
    x2 = randint(FOUR, min(FIVE, height_cap))
    x3 = randint(SIX, EIGHT)
    x4 = {(x0, (i, j)) for i in range(x2) for j in range(x3)}
    x5 = randint(ONE, max(ONE, subtract(x2, THREE)))
    x6 = subtract(x2, ONE)
    x7 = randint(ONE, TWO)
    x8 = add(x7, TWO)
    x9 = subtract(x3, THREE)
    x10 = subtract(x3, ONE)
    for i in range(x5, x6):
        for j in range(x7, x8):
            x4.discard((x0, (i, j)))
            x4.add((x1, (i, j)))
        for j in range(x9, x10):
            x4.discard((x0, (i, j)))
            x4.add((x1, (i, j)))
    return frozenset(x4)


def make_motif_7c66cb00(
    colors: tuple[Integer, ...],
    height_cap: Integer,
) -> Object:
    if len(colors) == ONE:
        x0 = choice(("solid", "solid", "diamond", "notched"))
        if x0 == "diamond":
            return _diamond_motif_7c66cb00(colors[0], max(THREE, height_cap))
        if x0 == "notched":
            return _notched_rect_motif_7c66cb00(colors[0], max(THREE, height_cap))
        return _solid_motif_7c66cb00(colors[0], max(TWO, height_cap))
    x0 = (colors[0], colors[1])
    x1 = choice(("ring", "stripe", "windows"))
    if x1 == "ring":
        return _ring_motif_7c66cb00(x0, max(THREE, height_cap))
    if x1 == "windows":
        return _windows_motif_7c66cb00(x0, max(FOUR, height_cap))
    return _stripe_motif_7c66cb00(x0, max(THREE, height_cap))
