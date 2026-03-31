from __future__ import annotations

from synth_rearc.core import *

from .helpers import transform_grid_8b7bacbf


def _pad_8b7bacbf(
    patch: Indices,
) -> Indices:
    x0 = set(patch)
    for x1 in patch:
        x0.update(neighbors(x1))
    return frozenset(x0)


def _in_bounds_8b7bacbf(
    patch: Indices,
    h: Integer,
    w: Integer,
) -> Boolean:
    return all(ZERO <= x0 < h and ZERO <= x1 < w for x0, x1 in patch)


def _king_path_8b7bacbf(
    start: IntegerTuple,
    stop: IntegerTuple,
) -> Indices:
    x0 = {start}
    x1 = start
    while x1 != stop:
        x2 = sign(stop[ZERO] - x1[ZERO])
        x3 = sign(stop[ONE] - x1[ONE])
        x1 = (x1[ZERO] + x2, x1[ONE] + x3)
        x0.add(x1)
    return frozenset(x0)


def _ring_from_attach_8b7bacbf(
    attach: IntegerTuple,
    inner_h: Integer,
    inner_w: Integer,
    color_value: Integer,
    attach_side: str,
) -> dict:
    if attach_side == "right":
        x0 = attach[ZERO] - (inner_h // TWO + ONE)
        x1 = attach[ONE] - inner_w - TWO
    else:
        x0 = attach[ZERO] - inner_h - TWO
        x1 = attach[ONE] - (inner_w // TWO + ONE)
    x2 = frozenset((x0, x1 + x3) for x3 in range(ONE, inner_w + ONE))
    x3 = frozenset((x0 + inner_h + ONE, x1 + x4) for x4 in range(ONE, inner_w + ONE))
    x4 = frozenset((x0 + x5, x1) for x5 in range(ONE, inner_h + ONE))
    x5 = frozenset((x0 + x6, x1 + inner_w + ONE) for x6 in range(ONE, inner_h + ONE))
    x6 = combine(combine(x2, x3), combine(x4, x5))
    x7 = frozenset(
        (x0 + x8, x1 + x9)
        for x8 in range(ONE, inner_h + ONE)
        for x9 in range(ONE, inner_w + ONE)
    )
    return {
        "cells": recolor(color_value, x6),
        "fill": x7,
        "attach": attach,
        "bbox": frozenset({(x0, x1), (x0 + inner_h + ONE, x1 + inner_w + ONE)}),
    }


def _random_selected_loop_8b7bacbf(
    current: IntegerTuple,
    h: Integer,
    w: Integer,
    occupied: Indices,
    diff_lb: float,
    diff_ub: float,
    outline_colors: tuple[Integer, ...],
) -> dict | None:
    for _ in range(80):
        x0 = choice(("right", "right", "bottom"))
        x1 = unifint(diff_lb, diff_ub, (TWO, THREE))
        x2 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x3 = unifint(diff_lb, diff_ub, (THREE, SEVEN))
        x4 = unifint(diff_lb, diff_ub, (TWO, SEVEN))
        x5 = (max(TWO, current[ZERO] - x3), max(TWO, current[ONE] - x4))
        x6 = _ring_from_attach_8b7bacbf(x5, x1, x2, choice(outline_colors), x0)
        x7 = toindices(x6["cells"])
        x8 = x6["fill"]
        x9 = _king_path_8b7bacbf(current, x5)
        x10 = remove(current, x9)
        if not _in_bounds_8b7bacbf(combine(combine(x7, x8), x10), h, w):
            continue
        if len(intersection(combine(combine(x7, x8), x10), occupied)) > ZERO:
            continue
        return {
            "loop": x6,
            "path": x9,
        }
    return None


def _random_distractor_8b7bacbf(
    h: Integer,
    w: Integer,
    blocked: Indices,
    guide_color: Integer,
    marker_color: Integer,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Object, Indices] | None:
    x0 = tuple(x1 for x1 in interval(ONE, TEN, ONE) if x1 not in (guide_color, marker_color))
    for _ in range(80):
        x1 = unifint(diff_lb, diff_ub, (TWO, THREE))
        x2 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x3 = randint(ONE, h - x1 - TWO)
        x4 = randint(ONE, w - x2 - TWO)
        x5 = choice(("loop_only", "network"))
        x6 = choice(x0)
        x7 = _ring_from_attach_8b7bacbf((x3 + x1 + ONE, x4 + x2 + ONE), x1, x2, x6, "bottom")
        x8 = toindices(x7["cells"])
        x9 = x7["fill"]
        x10 = x8
        if x5 == "network":
            x11 = choice(tuple(x12 for x12 in x0 if x12 != x6))
            x12 = (x3 + x1 + TWO, x4 + x2 + ONE)
            x13 = (
                min(h - TWO, x12[ZERO] + unifint(diff_lb, diff_ub, (TWO, FOUR))),
                max(ONE, x12[ONE] - unifint(diff_lb, diff_ub, (TWO, FIVE))),
            )
            x14 = _king_path_8b7bacbf(x12, x13)
            x10 = combine(x10, x14)
            x15 = recolor(x11, x14)
        else:
            x15 = frozenset()
        if not _in_bounds_8b7bacbf(combine(x10, x9), h, w):
            continue
        if len(intersection(combine(x10, x9), blocked)) > ZERO:
            continue
        return combine(x7["cells"], x15), combine(x10, x9)
    return None


def _apply_transform_8b7bacbf(
    grid: Grid,
    code: Integer,
) -> Grid:
    if code == ZERO:
        return grid
    if code == ONE:
        return rot90(grid)
    if code == TWO:
        return rot180(grid)
    if code == THREE:
        return rot270(grid)
    if code == FOUR:
        return hmirror(grid)
    if code == FIVE:
        return vmirror(grid)
    if code == SIX:
        return dmirror(grid)
    return cmirror(grid)


def generate_8b7bacbf(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = tuple(interval(ONE, TEN, ONE))
    for _ in range(600):
        x1 = unifint(diff_lb, diff_ub, (14, 28))
        x2 = unifint(diff_lb, diff_ub, (14, 28))
        x3 = choice(x0)
        x4 = choice(tuple(x5 for x5 in x0 if x5 != x3))
        x5 = tuple(x6 for x6 in x0 if x6 not in (x3, x4))
        x6 = canvas(ZERO, (x1, x2))
        x7 = (x1 - TWO, x2 - ONE)
        x8 = (x1 - ONE, x2 - ONE)
        x9 = frozenset({x7})
        x10 = recolor(x4, x9)
        x11 = frozenset({x8})
        x12 = recolor(x3, x11)
        x13 = frozenset()
        x14 = frozenset({x7, x8})
        x15 = unifint(diff_lb, diff_ub, (ONE, FOUR))
        x16: list[Indices] = []
        x17 = x7
        x18 = True
        for _ in range(x15):
            x19 = _random_selected_loop_8b7bacbf(x17, x1, x2, x14, diff_lb, diff_ub, x5)
            if x19 is None:
                x18 = False
                break
            x20 = x19["loop"]
            x21 = toindices(x20["cells"])
            x22 = x20["fill"]
            x23 = x19["path"]
            x24 = recolor(x4, x23)
            x10 = combine(x10, x24)
            x13 = combine(x13, x20["cells"])
            x14 = combine(x14, combine(x21, combine(x22, x23)))
            x16.append(x22)
            x17 = x20["attach"]
        if not x18 or len(x16) == ZERO:
            continue
        x25 = choice((ZERO, ONE))
        x26 = frozenset()
        x27 = _pad_8b7bacbf(combine(toindices(x10), combine(toindices(x12), toindices(x13))))
        for _ in range(unifint(diff_lb, diff_ub, (ONE, FOUR))):
            x28 = x4 if x25 == ONE and choice((True, False)) else choice(tuple(x29 for x29 in x5 if x29 != x4))
            x30 = _random_distractor_8b7bacbf(x1, x2, x27, x28, x3, diff_lb, diff_ub)
            if x30 is None:
                continue
            x31, x32 = x30
            x26 = combine(x26, x31)
            x27 = combine(x27, _pad_8b7bacbf(x32))
        x32 = paint(x6, x13)
        x33 = paint(x32, x10)
        x34 = paint(x33, x26)
        x35 = paint(x34, x12)
        x36 = x35
        for x37 in x16:
            x36 = fill(x36, x3, x37)
        x37 = randint(ZERO, SEVEN)
        x38 = _apply_transform_8b7bacbf(x35, x37)
        x39 = _apply_transform_8b7bacbf(x36, x37)
        if transform_grid_8b7bacbf(x38) != x39:
            continue
        return {"input": x38, "output": x39}
    raise RuntimeError("failed to generate task 8b7bacbf")
