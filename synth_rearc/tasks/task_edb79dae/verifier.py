from __future__ import annotations

from synth_rearc.core import *

from .helpers import (
    PAIR_LEFT_EDB79DAE,
    PAIR_RIGHT_EDB79DAE,
    framed_canvas_edb79dae,
    paint_template_edb79dae,
)


def _outside_objects_edb79dae(
    objs: Objects,
    frame: Object,
) -> tuple[Object, ...]:
    x0, x1 = ulcorner(frame)
    x2, x3 = lrcorner(frame)
    x4 = []
    for x5 in objs:
        if x5 == frame:
            continue
        x6 = toindices(x5)
        if any(x0 <= x7 <= x2 and x1 <= x8 <= x3 for x7, x8 in x6):
            continue
        x4.append(x5)
    return tuple(x4)


def _mapping_and_templates_edb79dae(
    outside: tuple[Object, ...],
) -> tuple[dict[Integer, Integer], dict[Integer, Indices]]:
    x0: dict[Integer, Integer] = {}
    x1: dict[Integer, set[IntegerTuple]] = {}
    x2: dict[Integer, set[IntegerTuple]] = {}
    for x3 in outside:
        x4 = toindices(normalize(x3))
        if x4 != PAIR_LEFT_EDB79DAE:
            continue
        x5 = ulcorner(x3)
        x6 = lrcorner(x3)
        for x7 in outside:
            if toindices(normalize(x7)) != PAIR_RIGHT_EDB79DAE:
                continue
            x8 = ulcorner(x7)
            x9 = lrcorner(x7)
            if x8[0] != x5[0] or x9[0] != x6[0]:
                continue
            if x8[1] != x6[1]:
                continue
            x10 = color(x3)
            x11 = color(x7)
            x0[x10] = x11
            x1[x10] = set(toindices(x3))
            x2.setdefault(x11, set()).update(toindices(x7))
            break
    x12: dict[Integer, Indices] = {}
    for x13 in x0:
        x14: set[IntegerTuple] = set()
        for x15 in outside:
            if color(x15) != x13:
                continue
            x14.update(toindices(x15))
        x14 -= x1.get(x13, set())
        x14 -= x2.get(x13, set())
        x16 = min(x17 for x17, _ in x14)
        x18 = min(x19 for _, x19 in x14)
        x20 = frozenset((x21 - x16, x22 - x18) for x21, x22 in x14)
        x12[x13] = x20
    return x0, x12


def verify_edb79dae(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = tuple(x2 for x2 in x0 if toindices(x2) == box(x2))
    x2 = max(x1, key=len)
    x3 = subgrid(x2, I)
    x4 = objects(x3, T, F, T)
    x5 = next(x6 for x6 in x4 if toindices(x6) == box(x6))
    x6 = tuple(x7 for x7 in x4 if x7 != x5)
    x7 = _outside_objects_edb79dae(x0, x2)
    x8, x9 = _mapping_and_templates_edb79dae(x7)
    x10 = framed_canvas_edb79dae(mostcolor(x3), color(x5), shape(x3))
    for x11 in x6:
        x12 = color(x11)
        x13 = ulcorner(x11)
        x10 = paint_template_edb79dae(x10, x8[x12], x9[x12], x13)
    return x10
