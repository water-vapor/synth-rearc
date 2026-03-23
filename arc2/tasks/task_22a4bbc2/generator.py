from __future__ import annotations

from arc2.core import *


Component22A4BBC2 = tuple[Integer, Integer, Integer, Integer, Integer]

WIDTH_BOUNDS_22A4BBC2 = (THREE, FIVE)
COMPONENT_COUNT_BOUNDS_22A4BBC2 = (EIGHT, 13)
TOTAL_HEIGHT_BOUNDS_22A4BBC2 = (14, 24)
COMPONENT_HEIGHT_BAG_22A4BBC2 = (ONE, ONE, ONE, TWO, TWO, TWO, THREE)
GAP_BAG_22A4BBC2 = (ZERO, ZERO, ZERO, ONE, ONE)
START_COLORS_22A4BBC2 = (ONE, EIGHT)


def _rect_patch_22a4bbc2(
    top: Integer,
    left: Integer,
    height: Integer,
    width: Integer,
) -> Indices:
    return frozenset(
        (i, j)
        for i in range(top, top + height)
        for j in range(left, left + width)
    )


def _span_bag_22a4bbc2(width: Integer) -> tuple[Integer, ...]:
    x0 = []
    for x1 in range(TWO, width + ONE):
        x0.extend(repeat(x1, x1 - ONE))
    return tuple(x0)


def _sample_components_22a4bbc2(
    width: Integer,
    count: Integer,
) -> tuple[tuple[Component22A4BBC2, ...], Integer]:
    x0 = choice(START_COLORS_22A4BBC2)
    x1 = other(START_COLORS_22A4BBC2, x0)
    x2 = _span_bag_22a4bbc2(width)
    x3 = []
    x4 = ZERO
    for x5 in range(count):
        x6 = choice(COMPONENT_HEIGHT_BAG_22A4BBC2)
        x7 = choice(x2)
        x8 = randint(ZERO, width - x7)
        x9 = x0 if x5 % TWO == ZERO else x1
        x3.append((x9, x4, x8, x6, x7))
        x10 = ZERO if x5 == count - ONE else choice(GAP_BAG_22A4BBC2)
        x4 += x6 + x10
    return tuple(x3), x4


def _valid_components_22a4bbc2(
    width: Integer,
    total_height: Integer,
    components: tuple[Component22A4BBC2, ...],
) -> Boolean:
    x0, x1 = TOTAL_HEIGHT_BOUNDS_22A4BBC2
    if total_height < x0 or total_height > x1:
        return F
    x2 = tuple(x3[THREE] for x3 in components)
    x3 = tuple(x4[FOUR] for x4 in components)
    x4 = tuple(x5[TWO] for x5 in components)
    x5 = tuple(
        components[x6 + ONE][ONE] - (components[x6][ONE] + components[x6][THREE])
        for x6 in range(len(components) - ONE)
    )
    if max(x2) == ONE:
        return F
    if max(x3) != width:
        return F
    if min(x3) == width:
        return F
    if all(x6 == ZERO for x6 in x4):
        return F
    if ZERO not in x5 or ONE not in x5:
        return F
    x6 = {(x7[ZERO], x7[TWO], x7[FOUR]) for x7 in components}
    if len(x6) == len(components):
        return F
    return T


def _paint_pair_22a4bbc2(
    width: Integer,
    total_height: Integer,
    components: tuple[Component22A4BBC2, ...],
) -> tuple[Grid, Grid]:
    x0 = canvas(ZERO, (total_height, width))
    x1 = canvas(ZERO, (total_height, width))
    for x2, (x3, x4, x5, x6, x7) in enumerate(components):
        x8 = _rect_patch_22a4bbc2(x4, x5, x6, x7)
        x0 = fill(x0, x3, x8)
        x9 = TWO if x2 % THREE == ZERO else x3
        x1 = fill(x1, x9, x8)
    return x0, x1


def generate_22a4bbc2(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, WIDTH_BOUNDS_22A4BBC2)
        x1 = unifint(diff_lb, diff_ub, COMPONENT_COUNT_BOUNDS_22A4BBC2)
        x2, x3 = _sample_components_22a4bbc2(x0, x1)
        if not _valid_components_22a4bbc2(x0, x3, x2):
            continue
        x4, x5 = _paint_pair_22a4bbc2(x0, x3, x2)
        return {"input": x4, "output": x5}
