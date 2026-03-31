from __future__ import annotations

from synth_rearc.core import *

from .verifier import verify_b0039139


LAYOUT_PATCHES_B0039139 = (
    frozenset({(ZERO, ZERO), (ZERO, ONE)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO)}),
)


def _connected_template_b0039139(
    h: Integer,
    w: Integer,
) -> Indices:
    x0 = h * w
    x1 = max(h + w - ONE, (x0 + ONE) // TWO)
    x2 = x0 - ONE
    while True:
        x3 = randint(x1, x2)
        x4 = {(randint(ZERO, h - ONE), randint(ZERO, w - ONE))}
        while len(x4) < x3:
            x5 = set()
            for x6 in x4:
                for x7 in dneighbors(x6):
                    if both(x7[ZERO] >= ZERO, x7[ONE] >= ZERO) and both(x7[ZERO] < h, x7[ONE] < w):
                        if x7 not in x4:
                            x5.add(x7)
            if len(x5) == ZERO:
                break
            x4.add(choice(tuple(x5)))
        if len(x4) != x3:
            continue
        x8 = {x9[ZERO] for x9 in x4}
        x9 = {x10[ONE] for x10 in x4}
        if len(x8) != h or len(x9) != w:
            continue
        return frozenset(x4)


def _paint_index_patch_b0039139(
    grid: Grid,
    patch: Indices,
    value: Integer,
) -> Grid:
    return fill(grid, value, patch)


def _repeat_horizontal_b0039139(
    tile: Grid,
    copies: Integer,
    value: Integer,
) -> Grid:
    x0 = canvas(value, (height(tile), ONE))
    x1 = tile
    for _ in range(decrement(copies)):
        x1 = hconcat(x1, x0)
        x1 = hconcat(x1, tile)
    return x1


def _layout_section_b0039139(
    total_h: Integer,
    copies: Integer,
) -> Grid:
    while True:
        x0 = choice((ONE, ONE, TWO))
        x1 = [randint(ZERO, total_h - TWO)] if x0 == ONE else sorted(sample(tuple(range(total_h - ONE)), TWO))
        if x0 == TWO and x1[ONE] <= x1[ZERO] + ONE:
            continue
        x2 = tuple(
            x3 for x3 in LAYOUT_PATCHES_B0039139 if height(x3) <= total_h
        )
        x3 = randint(ONE, TWO)
        x4 = []
        x5 = randint(ONE, TWO)
        x6 = ZERO
        for x7 in range(copies):
            x8 = choice(x2)
            x9 = choice(x1)
            if x9 + height(x8) > total_h:
                x9 = total_h - height(x8)
            if len(x4) > ZERO and x0 == TWO and randint(ZERO, ONE) == ONE:
                x10 = last(x4)
                x11 = rightmost(x10) + randint(ZERO, ONE)
            else:
                x11 = x5 + x6
            x12 = shift(x8, (x9, x11))
            x4.append(x12)
            x6 = rightmost(x12) + x3 - x5 + ONE
        x7 = merge(x4)
        x8 = len(x7)
        x9 = rightmost(x7) + randint(ONE, TWO) + ONE
        x10 = max(x9, x8 * TWO // total_h + TWO)
        x11 = canvas(ZERO, (total_h, x10))
        x12 = _paint_index_patch_b0039139(x11, x7, THREE)
        if mostcolor(x12) != ZERO:
            continue
        return x12


def _template_section_b0039139(
    total_h: Integer,
    patch: Indices,
) -> Grid:
    x0 = len(patch)
    x1 = width(patch)
    x2 = max(x1 + randint(TWO, FOUR), x0 * TWO // total_h + TWO)
    x3 = randint(ZERO, total_h - height(patch))
    x4 = randint(ONE, x2 - width(patch) - ONE)
    x5 = canvas(ZERO, (total_h, x2))
    x6 = shift(patch, (x3, x4))
    x7 = _paint_index_patch_b0039139(x5, x6, FOUR)
    return x7


def _horizontal_case_b0039139(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Grid, Grid]:
    while True:
        x0 = unifint(diff_lb, diff_ub, (FOUR, EIGHT))
        x1 = randint(TWO, min(FIVE, x0 - ONE))
        x2 = randint(TWO, FIVE)
        x3 = _connected_template_b0039139(x1, x2)
        x4 = width(x3)
        x5 = 31 // increment(x4)
        x6 = randint(TWO, min(FIVE, x5))
        x7, x8 = sample(tuple(range(TWO, TEN)), TWO)
        x9 = _template_section_b0039139(x0, x3)
        x10 = _layout_section_b0039139(x0, x6)
        x11 = randint(THREE, SIX)
        x12 = randint(THREE, SIX)
        x13 = canvas(x7, (x0, x11))
        x14 = canvas(x8, (x0, x12))
        x15 = canvas(ONE, (x0, ONE))
        x16 = x9
        for x17 in (x10, x13, x14):
            x16 = hconcat(x16, x15)
            x16 = hconcat(x16, x17)
        if width(x16) > 30:
            continue
        x17 = fill(canvas(x8, (x1, x2)), x7, x3)
        x18 = _repeat_horizontal_b0039139(x17, x6, x8)
        if width(x18) > 30:
            continue
        return x16, x18


def generate_b0039139(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0, x1 = _horizontal_case_b0039139(diff_lb, diff_ub)
        if choice((T, F)):
            x0 = dmirror(x0)
            x1 = dmirror(x1)
        if verify_b0039139(x0) != x1:
            continue
        return {"input": x0, "output": x1}
