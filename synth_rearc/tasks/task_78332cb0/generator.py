from synth_rearc.core import *

from .helpers import (
    FG_COLOR_CHOICES_78332CB0,
    _assemble_input_layout_78332cb0,
    _assemble_output_78332cb0,
    _output_is_horizontal_78332cb0,
    _panel_sort_key_78332cb0,
    _random_connected_patch_78332cb0,
    _render_panel_78332cb0,
)
from .verifier import verify_78332cb0


MIDDLE_BOXES_78332CB0 = (
    (ONE, THREE, ZERO, THREE),
    (ONE, THREE, ZERO, FOUR),
    (ONE, THREE, ONE, FOUR),
)
BOTTOM_BOXES_78332CB0 = (
    (ONE, FOUR, ONE, THREE),
    (ONE, FOUR, ZERO, THREE),
    (ONE, FOUR, ONE, FOUR),
    (TWO, FOUR, ONE, THREE),
    (THREE, FOUR, ONE, THREE),
)
FULL_BOXES_78332CB0 = (
    (ZERO, FOUR, ONE, TWO),
    (ZERO, FOUR, ONE, THREE),
    (ZERO, FOUR, TWO, TWO),
    (ZERO, FOUR, TWO, THREE),
)
TOP_BOXES_78332CB0 = (
    (ZERO, ONE, ONE, THREE),
    (ZERO, ONE, TWO, TWO),
    (ZERO, TWO, ONE, THREE),
    (ZERO, THREE, ONE, THREE),
    (ZERO, THREE, ONE, TWO),
    (ZERO, THREE, TWO, THREE),
)


def _size_bounds_78332cb0(
    box_spec: tuple[Integer, Integer, Integer, Integer],
) -> tuple[Integer, Integer]:
    x0, x1, x2, x3 = box_spec
    x4 = x1 - x0 + ONE
    x5 = x3 - x2 + ONE
    x6 = max(FOUR, x4 + x5 - TWO)
    x7 = min(TEN, x4 * x5)
    return (x6, x7)


def _sample_panel_from_box_78332cb0(
    box_spec: tuple[Integer, Integer, Integer, Integer],
    color_value: Integer,
) -> Grid | None:
    x0, x1, x2, x3 = box_spec
    x4, x5 = _size_bounds_78332cb0(box_spec)
    x6 = _random_connected_patch_78332cb0(x0, x1, x2, x3, x4, x5)
    if x6 is None:
        return None
    return _render_panel_78332cb0(x6, color_value)


def _sample_colors_78332cb0(
    count: Integer,
) -> tuple[Integer, ...]:
    x0 = [choice(FG_COLOR_CHOICES_78332CB0) for _ in range(count)]
    if len(set(x0)) == count and choice((T, F, F)):
        x1 = randint(ZERO, count - ONE)
        x2 = randint(ZERO, count - ONE)
        while x2 == x1:
            x2 = randint(ZERO, count - ONE)
        x0[x2] = x0[x1]
    return tuple(x0)


def _middle_family_panels_78332cb0(
    count: Integer,
) -> tuple[Grid, ...] | None:
    x0 = _sample_colors_78332cb0(count)
    x1 = (
        (MIDDLE_BOXES_78332CB0[ZERO], MIDDLE_BOXES_78332CB0[ONE], MIDDLE_BOXES_78332CB0[TWO])
        if count == THREE
        else (
            MIDDLE_BOXES_78332CB0[ZERO],
            MIDDLE_BOXES_78332CB0[ONE],
            MIDDLE_BOXES_78332CB0[ONE],
            MIDDLE_BOXES_78332CB0[TWO],
        )
    )
    x2 = []
    for x3, x4 in zip(x1, x0):
        x5 = _sample_panel_from_box_78332cb0(x3, x4)
        if x5 is None:
            return None
        x2.append(x5)
    x6 = tuple(x2)
    x7 = tuple(_panel_sort_key_78332cb0(x8) for x8 in x6)
    if len(set(x7)) != count:
        return None
    if not _output_is_horizontal_78332cb0(x6):
        return None
    return x6


def _mixed_family_panels_78332cb0(
    count: Integer,
) -> tuple[Grid, ...] | None:
    x0 = _sample_colors_78332cb0(count)
    x1 = [choice(BOTTOM_BOXES_78332CB0), choice(FULL_BOXES_78332CB0)]
    if count == FOUR:
        x1.append(choice(FULL_BOXES_78332CB0))
    x1.append(choice(TOP_BOXES_78332CB0))
    x2 = []
    for x3, x4 in zip(x1, x0):
        x5 = _sample_panel_from_box_78332cb0(x3, x4)
        if x5 is None:
            return None
        x2.append(x5)
    x6 = tuple(x2)
    x7 = tuple(_panel_sort_key_78332cb0(x8) for x8 in x6)
    if len(set(x7)) != count:
        return None
    if _output_is_horizontal_78332cb0(x6):
        return None
    return x6


def generate_78332cb0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(("middle", "middle", "mixed", "mixed", "mixed"))
        x1 = choice((THREE, FOUR))
        if x0 == "middle":
            x2 = _middle_family_panels_78332cb0(x1)
            if x2 is None:
                continue
            x3 = "v" if x1 == THREE else "q"
        else:
            x2 = _mixed_family_panels_78332cb0(x1)
            if x2 is None:
                continue
            if x1 == THREE:
                x3 = "h"
            else:
                x3 = choice(("v", "q"))
        x4 = list(x2)
        shuffle(x4)
        x4 = tuple(x4)
        x5 = tuple(sorted(x2, key=_panel_sort_key_78332cb0))
        if x4 == x5:
            continue
        gi = _assemble_input_layout_78332cb0(x4, x3)
        go = _assemble_output_78332cb0(x4)
        if verify_78332cb0(gi) != go:
            continue
        return {"input": gi, "output": go}
