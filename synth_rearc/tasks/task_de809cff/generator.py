from __future__ import annotations

from synth_rearc.core import *

from .helpers import (
    carvable_centers_de809cff,
    dominant_colors_de809cff,
    rect_patch_de809cff,
    stamp_centers_de809cff,
    transform_grid_de809cff,
)


GRID_BOUNDS_DE809CFF = (18, 30)
HOLE_COUNT_BOUNDS_DE809CFF = (3, 8)


def _available_color_pair_de809cff() -> tuple[Integer, Integer]:
    x0 = sample((ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, NINE), TWO)
    return x0[ZERO], x0[ONE]


def _rand_between_de809cff(
    lo: Integer,
    hi: Integer,
) -> Integer:
    return lo if hi <= lo else randint(lo, hi)


def _paint_regions_de809cff(
    h: Integer,
    w: Integer,
    a: Integer,
    b: Integer,
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    x0 = canvas(ZERO, (h, w))
    x1 = x0

    x2 = _rand_between_de809cff(ZERO, max(ZERO, subtract(divide(h, FIVE), ONE)))
    x3 = _rand_between_de809cff(ZERO, max(ZERO, subtract(divide(w, SIX), ONE)))
    x4 = _rand_between_de809cff(max(SIX, divide(h, FOUR)), min(12, subtract(h, x2)))
    x5 = _rand_between_de809cff(max(SIX, divide(w, THREE)), min(14, subtract(w, x3)))
    x1 = fill(x1, a, rect_patch_de809cff(x2, x3, x4, x5))

    if both(choice((T, T, F)), subtract(h, add(x2, x4)) >= FIVE):
        x6 = _rand_between_de809cff(max(add(x2, x4), divide(h, TWO)), subtract(h, FIVE))
        x7 = _rand_between_de809cff(ZERO, max(ZERO, divide(w, FOUR)))
        x8 = _rand_between_de809cff(FOUR, min(EIGHT, subtract(h, x6)))
        x9 = _rand_between_de809cff(max(SIX, divide(w, FOUR)), min(add(x5, THREE), subtract(w, x7)))
        x1 = fill(x1, a, rect_patch_de809cff(x6, x7, x8, x9))

    x10 = _rand_between_de809cff(max(FOUR, subtract(divide(h, TWO), TWO)), subtract(h, SIX))
    x11 = _rand_between_de809cff(max(FOUR, subtract(divide(w, TWO), TWO)), subtract(w, SIX))
    x12 = _rand_between_de809cff(max(SIX, divide(h, THREE)), min(14, subtract(h, x10)))
    x13 = _rand_between_de809cff(max(SIX, divide(w, THREE)), min(14, subtract(w, x11)))
    x1 = fill(x1, b, rect_patch_de809cff(x10, x11, x12, x13))

    if both(choice((T, F)), x11 > FOUR):
        x14 = _rand_between_de809cff(ZERO, max(ZERO, subtract(divide(h, FOUR), ONE)))
        x15 = _rand_between_de809cff(max(add(x11, divide(x13, TWO)), divide(w, TWO)), subtract(w, FOUR))
        x16 = _rand_between_de809cff(FOUR, min(EIGHT, subtract(h, x14)))
        x17 = _rand_between_de809cff(FOUR, min(EIGHT, subtract(w, x15)))
        x1 = fill(x1, b, rect_patch_de809cff(x14, x15, x16, x17))

    return x1


def _choose_centers_de809cff(
    grid: Grid,
    color: Integer,
    count_lb: Integer,
    count_ub: Integer,
) -> tuple[tuple[Integer, Integer], ...]:
    x0 = list(carvable_centers_de809cff(grid, color))
    if len(x0) < count_lb:
        return tuple()
    shuffle(x0)
    x1 = []
    x2 = randint(count_lb, min(count_ub, len(x0)))
    while both(len(x0) > ZERO, len(x1) < x2):
        x3 = x0.pop()
        x4 = choice((T, T, T, F))
        if x4:
            if any(max(abs(subtract(x3[ZERO], x5[ZERO])), abs(subtract(x3[ONE], x5[ONE]))) <= ONE for x5 in x1):
                continue
        x1.append(x3)
    return tuple(x1)


def _carve_centers_de809cff(
    grid: Grid,
    centers: tuple[tuple[Integer, Integer], ...],
) -> Grid:
    x0 = grid
    for x1, x2 in centers:
        x0 = fill(x0, ZERO, initset((x1, x2)))
    return x0


def _background_slots_de809cff(
    grid: Grid,
) -> list[tuple[Integer, Integer]]:
    x0 = []
    x1 = len(grid)
    x2 = len(grid[ZERO])
    for x3 in range(ONE, subtract(x1, ONE)):
        for x4 in range(ONE, subtract(x2, ONE)):
            if grid[x3][x4] != ZERO:
                continue
            x5 = (
                grid[add(x3, ONE)][x4],
                grid[subtract(x3, ONE)][x4],
                grid[x3][add(x4, ONE)],
                grid[x3][subtract(x4, ONE)],
            )
            if any(x6 != ZERO for x6 in x5):
                continue
            x0.append((x3, x4))
    shuffle(x0)
    return x0


def _add_singletons_de809cff(
    grid: Grid,
    colors: tuple[Integer, Integer],
) -> Grid:
    x0 = grid
    x1 = _background_slots_de809cff(x0)
    if len(x1) == ZERO:
        return x0
    x2 = randint(ONE, min(FOUR, len(x1)))
    for x3 in range(x2):
        x4 = x1[x3]
        x5 = choice(colors)
        x0 = fill(x0, x5, initset(x4))
    return x0


def _spike_targets_de809cff(
    grid: Grid,
    color: Integer,
) -> list[tuple[tuple[Integer, Integer], tuple[Integer, Integer]]]:
    x0 = []
    x1 = len(grid)
    x2 = len(grid[ZERO])
    for x3 in range(ONE, subtract(x1, ONE)):
        for x4 in range(ONE, subtract(x2, ONE)):
            if grid[x3][x4] != color:
                continue
            for x5, x6 in ((ONE, ZERO), (NEG_ONE, ZERO), (ZERO, ONE), (ZERO, NEG_ONE)):
                x7 = add(x3, x5)
                x8 = add(x4, x6)
                if grid[x7][x8] != ZERO:
                    continue
                x9 = []
                for x10, x11 in ((ONE, ZERO), (NEG_ONE, ZERO), (ZERO, ONE), (ZERO, NEG_ONE)):
                    x12 = add(x7, x10)
                    x13 = add(x8, x11)
                    if both(x12 == x3, x13 == x4):
                        continue
                    if not (ZERO <= x12 < x1 and ZERO <= x13 < x2):
                        continue
                    x9.append(grid[x12][x13])
                if all(x10 == ZERO for x10 in x9):
                    x0.append(((x3, x4), (x7, x8)))
    shuffle(x0)
    return x0


def _add_background_spikes_de809cff(
    grid: Grid,
    colors: tuple[Integer, Integer],
) -> Grid:
    x0 = grid
    x1 = []
    for x2 in colors:
        x1.extend((x2, x3) for x3 in _spike_targets_de809cff(x0, x2))
    if len(x1) == ZERO:
        return x0
    shuffle(x1)
    x2 = randint(ZERO, min(TWO, len(x1)))
    for x3 in range(x2):
        x4, x5 = x1[x3]
        x0 = fill(x0, x4, initset(x5[ONE]))
    return x0


def _zigzag_slots_de809cff(
    grid: Grid,
) -> list[tuple[str, Integer, Integer]]:
    x0 = []
    x1 = len(grid)
    x2 = len(grid[ZERO])
    for x3 in range(TWO, subtract(x1, TWO)):
        for x4 in range(TWO, subtract(x2, TWO)):
            x5 = tuple(grid[x6][x7] for x6 in range(subtract(x3, ONE), add(x3, TWO)) for x7 in range(subtract(x4, ONE), add(x4, TWO)))
            if all(x6 == ZERO for x6 in x5):
                x0.append(("h", x3, x4))
                x0.append(("v", x3, x4))
    shuffle(x0)
    return x0


def _paint_horizontal_zigzag_de809cff(
    grid: Grid,
    center: tuple[Integer, Integer],
    a: Integer,
    b: Integer,
) -> Grid:
    x0, x1 = center
    x2 = fill(grid, a, frozenset((subtract(x0, ONE), x3) for x3 in range(subtract(x1, ONE), add(x1, TWO))))
    x2 = fill(x2, b, initset((x0, subtract(x1, ONE))))
    x2 = fill(x2, a, initset((x0, x1)))
    x2 = fill(x2, b, initset((x0, add(x1, ONE))))
    x2 = fill(x2, b, frozenset((add(x0, ONE), x3) for x3 in range(subtract(x1, ONE), add(x1, TWO))))
    return x2


def _paint_vertical_zigzag_de809cff(
    grid: Grid,
    center: tuple[Integer, Integer],
    a: Integer,
    b: Integer,
) -> Grid:
    x0, x1 = center
    x2 = fill(grid, a, frozenset((x3, subtract(x1, ONE)) for x3 in range(subtract(x0, ONE), add(x0, TWO))))
    x2 = fill(x2, b, initset((subtract(x0, ONE), x1)))
    x2 = fill(x2, a, initset((x0, x1)))
    x2 = fill(x2, b, initset((add(x0, ONE), x1)))
    x2 = fill(x2, b, frozenset((x3, add(x1, ONE)) for x3 in range(subtract(x0, ONE), add(x0, TWO))))
    return x2


def _add_zigzags_de809cff(
    grid: Grid,
    a: Integer,
    b: Integer,
) -> Grid:
    x0 = grid
    x1 = _zigzag_slots_de809cff(x0)
    x2 = randint(ZERO, min(TWO, len(x1)))
    for x3 in range(x2):
        x4, x5, x6 = x1[x3]
        if x4 == "h":
            x0 = _paint_horizontal_zigzag_de809cff(x0, (x5, x6), a, b)
        else:
            x0 = _paint_vertical_zigzag_de809cff(x0, (x5, x6), a, b)
    return x0


def generate_de809cff(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    for _ in range(300):
        x0 = unifint(diff_lb, diff_ub, GRID_BOUNDS_DE809CFF)
        x1 = unifint(diff_lb, diff_ub, GRID_BOUNDS_DE809CFF)
        x2, x3 = _available_color_pair_de809cff()
        x4 = _paint_regions_de809cff(x0, x1, x2, x3, diff_lb, diff_ub)
        x4 = _add_zigzags_de809cff(x4, x2, x3)
        x5 = _choose_centers_de809cff(x4, x2, *HOLE_COUNT_BOUNDS_DE809CFF)
        if len(x5) == ZERO:
            continue
        x6 = _carve_centers_de809cff(x4, x5)
        x7 = _choose_centers_de809cff(x6, x3, *HOLE_COUNT_BOUNDS_DE809CFF)
        if len(x7) == ZERO:
            continue
        x8 = _carve_centers_de809cff(x6, x7)
        x8 = _add_singletons_de809cff(x8, (x2, x3))
        x8 = _add_background_spikes_de809cff(x8, (x2, x3))
        x9 = stamp_centers_de809cff(x8)
        if len(x9) < SIX:
            continue
        if len({x10[TWO] for x10 in x9}) != TWO:
            continue
        x10 = dominant_colors_de809cff(x8)
        if set(x10) != {x2, x3}:
            continue
        x11 = transform_grid_de809cff(x8)
        if x11 == x8:
            continue
        if colorcount(x11, EIGHT) != len(x9):
            continue
        return {"input": x8, "output": x11}
    raise RuntimeError("failed to generate de809cff example")
