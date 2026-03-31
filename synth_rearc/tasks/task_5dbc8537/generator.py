from __future__ import annotations

from synth_rearc.core import *

from .helpers import (
    MASK_SIDES_5DBC8537,
    build_connected_hole_5dbc8537,
    combine_regions_5dbc8537,
    layout_inventory_5dbc8537,
    render_output_5dbc8537,
    sample_piece_set_5dbc8537,
)
from .verifier import verify_5dbc8537


def _dimension_bank_5dbc8537(
    total_area: Integer,
    objs: tuple[Object, ...],
    side: str,
) -> tuple[IntegerTuple, IntegerTuple] | None:
    x0 = max(height(x1) for x1 in objs)
    x1 = max(width(x2) for x2 in objs)
    if side in ("left", "right"):
        x2 = tuple(
            x3
            for x3 in range(max(add(x0, THREE), TEN), 25)
            if multiply(x3, SEVEN) >= add(total_area, TEN)
        )
        if len(x2) == ZERO:
            return None
        x4 = choice(x2)
        x5 = tuple(
            x6
            for x6 in range(max(add(x1, TWO), SEVEN), min(15, subtract(30, SEVEN)) + ONE)
            if multiply(x4, x6) >= add(total_area, SIX)
        )
        if len(x5) == ZERO:
            return None
        x7 = choice(x5)
        x8 = tuple(
            x9
            for x9 in range(max(add(x1, TWO), SEVEN), subtract(30, x7) + ONE)
            if multiply(x4, x9) >= add(add(total_area, total_area), multiply(TWO, len(objs)))
        )
        if len(x8) == ZERO:
            return None
        x10 = choice(x8)
        return (x4, x7), (x4, x10)
    x11 = tuple(
        x12
        for x12 in range(max(add(x1, THREE), TEN), 25)
        if multiply(SEVEN, x12) >= add(total_area, TEN)
    )
    if len(x11) == ZERO:
        return None
    x13 = choice(x11)
    x14 = tuple(
        x15
        for x15 in range(max(add(x0, TWO), SEVEN), min(15, subtract(30, SEVEN)) + ONE)
        if multiply(x15, x13) >= add(total_area, SIX)
    )
    if len(x14) == ZERO:
        return None
    x16 = choice(x14)
    x17 = tuple(
        x18
        for x18 in range(max(add(x0, TWO), SEVEN), subtract(30, x16) + ONE)
        if multiply(x18, x13) >= add(add(total_area, total_area), multiply(TWO, len(objs)))
    )
    if len(x17) == ZERO:
        return None
    x19 = choice(x17)
    return (x16, x13), (x19, x13)


def generate_5dbc8537(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(tuple(range(ONE, TEN)))
        x1 = choice(tuple(x2 for x2 in range(TEN) if x2 != x0))
        x2 = tuple(x3 for x3 in range(TEN) if x3 not in (x0, x1))
        x3 = sample_piece_set_5dbc8537(diff_lb, diff_ub, x2)
        x4 = sum(size(x5) for x5 in x3)
        x5 = choice(MASK_SIDES_5DBC8537)
        x6 = _dimension_bank_5dbc8537(x4, x3, x5)
        if x6 is None:
            continue
        x7, x8 = x6
        x9 = build_connected_hole_5dbc8537(x3, x7)
        if x9 is None:
            continue
        x10 = fill(canvas(x1, x7), x0, x9)
        x11 = layout_inventory_5dbc8537(x3, x8, x0)
        if x11 is None:
            continue
        try:
            x12 = render_output_5dbc8537(x10, x11, x0, x1)
        except ValueError:
            continue
        x13 = combine_regions_5dbc8537(x10, x11, x5)
        if x13 == x12:
            continue
        try:
            x14 = verify_5dbc8537(x13)
        except ValueError:
            continue
        if x14 != x12:
            continue
        return {"input": x13, "output": x12}
