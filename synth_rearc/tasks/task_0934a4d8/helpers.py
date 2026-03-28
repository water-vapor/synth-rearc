from typing import Callable

from synth_rearc.core import *


VISIBLE_SIZE_0934A4D8 = 30
VIRTUAL_SIZE_OFFSET_0934A4D8 = 2
SEED_SIZE_0934A4D8 = 16
NON_HOLE_COLORS_0934A4D8 = (ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, NINE)


def _rect_indices_0934a4d8(
    top: int,
    left: int,
    height_: int,
    width_: int,
) -> Indices:
    return frozenset(
        (i, j)
        for i in range(top, top + height_)
        for j in range(left, left + width_)
    )


def hole_rect_0934a4d8(
    grid: Grid,
) -> tuple[int, int, int, int]:
    x0 = ofcolor(grid, EIGHT)
    return uppermost(x0), leftmost(x0), height(x0), width(x0)


def orbit_sources_0934a4d8(
    top: int,
    left: int,
    height_: int,
    width_: int,
    size_: int,
) -> tuple[tuple[str, tuple[int, int], Callable], ...]:
    x0 = add(size_, VIRTUAL_SIZE_OFFSET_0934A4D8)
    return (
        ("hmirror", (subtract(subtract(x0, height_), top), left), hmirror),
        ("vmirror", (top, subtract(subtract(x0, width_), left)), vmirror),
        (
            "rot180",
            (
                subtract(subtract(x0, height_), top),
                subtract(subtract(x0, width_), left),
            ),
            rot180,
        ),
    )


def visible_sources_0934a4d8(
    size_: int,
    top: int,
    left: int,
    height_: int,
    width_: int,
) -> tuple[tuple[str, tuple[int, int], Callable], ...]:
    x0 = _rect_indices_0934a4d8(top, left, height_, width_)
    x1 = []
    for x2, (x3, x4), x5 in orbit_sources_0934a4d8(top, left, height_, width_, size_):
        if x3 < ZERO or x4 < ZERO or x3 + height_ > size_ or x4 + width_ > size_:
            continue
        x6 = _rect_indices_0934a4d8(x3, x4, height_, width_)
        if len(intersection(x0, x6)) != ZERO:
            continue
        x1.append((x2, (x3, x4), x5))
    return tuple(x1)


def fallback_sources_0934a4d8(
    size_: int,
    top: int,
    left: int,
    height_: int,
    width_: int,
) -> tuple[tuple[str, tuple[int, int], tuple[int, int], Callable], ...]:
    x0 = add(size_, VIRTUAL_SIZE_OFFSET_0934A4D8)
    x1 = (
        (
            "rot90",
            (left, subtract(subtract(x0, height_), top)),
            (width_, height_),
            rot270,
        ),
        (
            "rot270",
            (subtract(subtract(x0, width_), left), top),
            (width_, height_),
            rot90,
        ),
        (
            "dmirror",
            (left, top),
            (width_, height_),
            dmirror,
        ),
        (
            "cmirror",
            (
                subtract(subtract(x0, width_), left),
                subtract(subtract(x0, height_), top),
            ),
            (width_, height_),
            cmirror,
        ),
    )
    x2 = []
    x3 = _rect_indices_0934a4d8(top, left, height_, width_)
    for x4, (x5, x6), (x7, x8), x9 in x1:
        if x5 < ZERO or x6 < ZERO or x5 + x7 > size_ or x6 + x8 > size_:
            continue
        x10 = _rect_indices_0934a4d8(x5, x6, x7, x8)
        if len(intersection(x3, x10)) != ZERO:
            continue
        x2.append((x4, (x5, x6), (x7, x8), x9))
    return tuple(x2)


def candidate_outputs_0934a4d8(
    grid: Grid,
) -> tuple[Grid, ...]:
    x0, x1, x2, x3 = hole_rect_0934a4d8(grid)
    x4 = []
    for _, (x5, x6), x7 in visible_sources_0934a4d8(height(grid), x0, x1, x2, x3):
        x8 = crop(grid, (x5, x6), (x2, x3))
        if contained(EIGHT, palette(x8)):
            continue
        x4.append(x7(x8))
    if len(x4) != ZERO:
        return tuple(x4)
    for _, (x8, x9), (x10, x11), x12 in fallback_sources_0934a4d8(height(grid), x0, x1, x2, x3):
        x13 = crop(grid, (x8, x9), (x10, x11))
        if contained(EIGHT, palette(x13)):
            continue
        x4.append(x12(x13))
    return tuple(x4)


def build_visible_board_0934a4d8(
    seed: Grid,
) -> Grid:
    x0 = hconcat(seed, vmirror(seed))
    x1 = hconcat(hmirror(seed), rot180(seed))
    x2 = vconcat(x0, x1)
    return crop(x2, ORIGIN, (VISIBLE_SIZE_0934A4D8, VISIBLE_SIZE_0934A4D8))


def hide_rect_0934a4d8(
    grid: Grid,
    top: int,
    left: int,
    height_: int,
    width_: int,
) -> Grid:
    x0 = _rect_indices_0934a4d8(top, left, height_, width_)
    return fill(grid, EIGHT, x0)
