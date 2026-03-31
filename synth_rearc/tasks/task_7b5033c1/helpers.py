from __future__ import annotations

from synth_rearc.core import *


def _advance_7b5033c1(
    loc: IntegerTuple,
    direction: IntegerTuple,
) -> IntegerTuple:
    return (loc[ZERO] + direction[ZERO], loc[ONE] + direction[ONE])


def _walk_segment_7b5033c1(
    patch: Indices,
    loc: IntegerTuple,
    direction: IntegerTuple,
    amount: Integer,
) -> tuple[Indices, IntegerTuple]:
    x0 = set(patch)
    x1 = loc
    for _ in range(amount):
        x1 = _advance_7b5033c1(x1, direction)
        x0.add(x1)
    return frozenset(x0), x1


def build_monotone_path_7b5033c1(
    start: IntegerTuple,
    end: IntegerTuple,
) -> Indices:
    x0 = subtract(end[ZERO], start[ZERO])
    x1 = subtract(end[ONE], start[ONE])
    x2 = DOWN if x0 > ZERO else UP
    x3 = RIGHT if x1 > ZERO else LEFT
    x4 = abs(x0)
    x5 = abs(x1)
    x6 = initset(start)
    x7 = start
    if x4 == ZERO:
        x8, _ = _walk_segment_7b5033c1(x6, x7, x3, x5)
        return x8
    if x5 == ZERO:
        x9, _ = _walk_segment_7b5033c1(x6, x7, x2, x4)
        return x9
    x10 = []
    if x4 > ONE:
        x10.extend(("vhv", "vhv"))
    if x5 > ONE:
        x10.extend(("hvh", "hvh"))
    x10.extend(("vh", "hv"))
    x11 = choice(tuple(x10))
    if x11 == "vh":
        x12, x13 = _walk_segment_7b5033c1(x6, x7, x2, x4)
        x14, _ = _walk_segment_7b5033c1(x12, x13, x3, x5)
        return x14
    if x11 == "hv":
        x15, x16 = _walk_segment_7b5033c1(x6, x7, x3, x5)
        x17, _ = _walk_segment_7b5033c1(x15, x16, x2, x4)
        return x17
    if x11 == "vhv":
        x18 = randint(ONE, decrement(x4))
        x19 = subtract(x4, x18)
        x20, x21 = _walk_segment_7b5033c1(x6, x7, x2, x18)
        x22, x23 = _walk_segment_7b5033c1(x20, x21, x3, x5)
        x24, _ = _walk_segment_7b5033c1(x22, x23, x2, x19)
        return x24
    x25 = randint(ONE, decrement(x5))
    x26 = subtract(x5, x25)
    x27, x28 = _walk_segment_7b5033c1(x6, x7, x3, x25)
    x29, x30 = _walk_segment_7b5033c1(x27, x28, x2, x4)
    x31, _ = _walk_segment_7b5033c1(x29, x30, x3, x26)
    return x31


def touching_cells_7b5033c1(
    patch: Indices,
    other: Patch,
) -> Indices:
    x0 = toindices(other)
    x1 = set()
    for x2 in patch:
        if len(intersection(dneighbors(x2), x0)) > ZERO:
            x1.add(x2)
    return frozenset(x1)


def render_output_7b5033c1(
    objs: tuple[Object, ...],
) -> Grid:
    x0 = sum(size(x1) for x1 in objs)
    x1 = canvas(ZERO, (x0, ONE))
    x2 = ZERO
    for x3 in objs:
        x4 = connect((x2, ZERO), (add(x2, decrement(size(x3))), ZERO))
        x1 = fill(x1, color(x3), x4)
        x2 = add(x2, size(x3))
    return x1
