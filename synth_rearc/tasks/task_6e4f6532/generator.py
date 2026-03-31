from __future__ import annotations

from collections import defaultdict

from synth_rearc.core import *

from .helpers import (
    TEMPLATE_SPECS_6E4F6532,
    TRANSFORMS_6E4F6532,
    object_bbox_6e4f6532,
    object_cells_6e4f6532,
    padded_patch_6e4f6532,
    render_output_6e4f6532,
    render_template_object_6e4f6532,
    shift_object_6e4f6532,
    template_roles_6e4f6532,
    template_shape_class_6e4f6532,
    transform_object_6e4f6532,
)


LAYOUT_CHOICES_6E4F6532 = (
    "vertical_triptych",
    "frame",
    "frame",
    "frame_mid",
    "left_frame",
)


def _rows_patch_6e4f6532(
    row_start: Integer,
    row_stop: Integer,
    width_value: Integer,
) -> Indices:
    return frozenset(
        (x0, x1)
        for x0 in range(row_start, row_stop)
        for x1 in range(width_value)
    )


def _cols_patch_6e4f6532(
    col_start: Integer,
    col_stop: Integer,
    row_start: Integer,
    row_stop: Integer,
) -> Indices:
    return frozenset(
        (x0, x1)
        for x0 in range(row_start, row_stop)
        for x1 in range(col_start, col_stop)
    )


def _build_layout_6e4f6532(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Grid, tuple[dict, ...]]:
    while True:
        x0 = choice(LAYOUT_CHOICES_6E4F6532)
        if x0 == "vertical_triptych":
            x1 = unifint(diff_lb, diff_ub, (13, 20))
            x2 = unifint(diff_lb, diff_ub, (22, 30))
            x3 = ZERO
            x4 = ZERO
            x5 = tuple(sample(tuple(x6 for x6 in range(TEN) if x6 not in (EIGHT, NINE)), FOUR))
            x6, x7, x8, x9 = x5
            x10 = randint(SEVEN, x2 - NINE)
            x11 = (
                {"col": ZERO, "color": x7},
                {"col": x10, "color": x8},
                {"col": x2 - TWO, "color": x9},
            )
        elif x0 == "frame":
            x1 = unifint(diff_lb, diff_ub, (20, 30))
            x2 = unifint(diff_lb, diff_ub, (18, 30))
            x3 = TWO
            x4 = TWO
            x5 = tuple(sample(tuple(x6 for x6 in range(TEN) if x6 not in (EIGHT, NINE)), FIVE))
            x6, x7, x8, x9, x10 = x5
            x11 = (
                {"col": ZERO, "color": x9},
                {"col": x2 - TWO, "color": x10},
            )
        elif x0 == "frame_mid":
            x1 = unifint(diff_lb, diff_ub, (20, 30))
            x2 = unifint(diff_lb, diff_ub, (24, 30))
            x3 = TWO
            x4 = TWO
            x5 = tuple(sample(tuple(x6 for x6 in range(TEN) if x6 not in (EIGHT, NINE)), SIX))
            x6, x7, x8, x9, x10, x11a = x5
            x12 = randint(SEVEN, x2 - NINE)
            x11 = (
                {"col": ZERO, "color": x9},
                {"col": x12, "color": x10},
                {"col": x2 - TWO, "color": x11a},
            )
        else:
            x1 = unifint(diff_lb, diff_ub, (20, 30))
            x2 = unifint(diff_lb, diff_ub, (16, 24))
            x3 = TWO
            x4 = TWO
            x5 = tuple(sample(tuple(x6 for x6 in range(TEN) if x6 not in (EIGHT, NINE)), FOUR))
            x6, x7, x8, x9 = x5
            x11 = ({"col": ZERO, "color": x9},)
        x12 = canvas(x6, (x1, x2))
        if x3:
            x12 = fill(x12, x7, _rows_patch_6e4f6532(ZERO, x3, x2))
        if x4:
            x12 = fill(x12, x8, _rows_patch_6e4f6532(x1 - x4, x1, x2))
        x13 = x3
        x14 = x1 - x4
        for x15 in x11:
            x12 = fill(x12, x15["color"], _cols_patch_6e4f6532(x15["col"], x15["col"] + TWO, x13, x14))
        x16 = []
        x17 = ZERO
        x18 = None
        x19 = tuple(sorted(x11, key=lambda x20: x20["col"]))
        for x20 in x19:
            if x17 < x20["col"]:
                x16.append(
                    {
                        "r0": x13,
                        "r1": x14 - ONE,
                        "c0": x17,
                        "c1": x20["col"] - ONE,
                        "roles": {
                            "L": x18,
                            "R": x20["color"],
                            "T": x7 if x3 else None,
                            "B": x8 if x4 else None,
                        },
                    }
                )
            x17 = x20["col"] + TWO
            x18 = x20["color"]
        if x17 < x2:
            x16.append(
                {
                    "r0": x13,
                    "r1": x14 - ONE,
                    "c0": x17,
                    "c1": x2 - ONE,
                    "roles": {
                        "L": x18,
                        "R": None,
                        "T": x7 if x3 else None,
                        "B": x8 if x4 else None,
                    },
                }
            )
        x21 = tuple(
            x22
            for x22 in x16
            if x22["r1"] - x22["r0"] + ONE >= FOUR and x22["c1"] - x22["c0"] + ONE >= FOUR
        )
        if len(x21) > ZERO:
            return x12, x21


def _find_target_placement_6e4f6532(
    obj: Object,
    region: dict,
    blocked: Indices,
) -> Object | None:
    x0 = object_bbox_6e4f6532(obj)
    x1 = x0[2] - x0[0] + ONE
    x2 = x0[3] - x0[1] + ONE
    x3 = region["r1"] - region["r0"] + ONE
    x4 = region["c1"] - region["c0"] + ONE
    if x1 > x3 or x2 > x4:
        return None
    x5 = [
        (x6, x7)
        for x6 in range(region["r0"], region["r1"] - x1 + TWO)
        for x7 in range(region["c0"], region["c1"] - x2 + TWO)
    ]
    shuffle(x5)
    for x6, x7 in x5:
        x8 = shift_object_6e4f6532(obj, (x6, x7))
        if len(padded_patch_6e4f6532(x8) & blocked) == ZERO:
            return x8
    return None


def _find_source_placement_6e4f6532(
    obj: Object,
    regions: tuple[dict, ...],
    blocked: Indices,
) -> Object | None:
    x0 = object_bbox_6e4f6532(obj)
    x1 = x0[2] - x0[0] + ONE
    x2 = x0[3] - x0[1] + ONE
    x3 = list(regions)
    shuffle(x3)
    for x4 in x3:
        x5 = x4["r1"] - x4["r0"] + ONE
        x6 = x4["c1"] - x4["c0"] + ONE
        if x5 < x1 + TWO or x6 < x2 + TWO:
            continue
        x7 = [
            (x8, x9)
            for x8 in range(x4["r0"] + ONE, x4["r1"] - x1 + ONE)
            for x9 in range(x4["c0"] + ONE, x4["c1"] - x2 + ONE)
        ]
        shuffle(x7)
        for x8, x9 in x7:
            x10 = shift_object_6e4f6532(obj, (x8, x9))
            if len(padded_patch_6e4f6532(x10) & blocked) == ZERO:
                return x10
    return None


def _feasible_templates_6e4f6532(
    regions: tuple[dict, ...],
) -> tuple[tuple[dict, dict], ...]:
    x0 = []
    for x1 in TEMPLATE_SPECS_6E4F6532:
        x2 = template_roles_6e4f6532(x1)
        for x3 in regions:
            if all(x3["roles"].get(x4) is not None for x4 in x2):
                x0.append((x1, x3))
    return tuple(x0)


def _compose_example_6e4f6532(
    diff_lb: float,
    diff_ub: float,
) -> dict | None:
    x0, x1 = _build_layout_6e4f6532(diff_lb, diff_ub)
    x2 = _feasible_templates_6e4f6532(x1)
    x3 = defaultdict(list)
    for x4, x5 in x2:
        x3[template_shape_class_6e4f6532(x4)].append((x4, x5))
    x4 = tuple(x5 for x5 in x3 if len(x3[x5]) > ZERO)
    if len(x4) < TWO:
        return None
    x5 = choice((TWO, TWO, THREE))
    x5 = min(x5, len(x4))
    x6 = tuple(sample(x4, x5))
    x7 = x0
    x8 = x0
    x9 = frozenset()
    x10 = frozenset()
    x11 = []
    for x12 in x6:
        x13, x14 = choice(tuple(x3[x12]))
        x15 = {x16: x14["roles"][x16] for x16 in template_roles_6e4f6532(x13)}
        x16 = render_template_object_6e4f6532(x13, x15)
        x17 = _find_target_placement_6e4f6532(x16, x14, x9)
        if x17 is None:
            return None
        x18 = frozenset(loc for x19, loc in x17 if x19 == NINE)
        x7 = paint(x7, x17)
        x8 = paint(x8, recolor(NINE, x18))
        x9 |= padded_patch_6e4f6532(x17)
        x10 |= padded_patch_6e4f6532(x18)
        x11.append((x16, x17))
    for x12, _ in x11:
        x13 = choice(tuple(x14 for x14 in TRANSFORMS_6E4F6532 if x14 != "id"))
        x14 = transform_object_6e4f6532(x12, x13)
        x15 = _find_source_placement_6e4f6532(x14, x1, x10)
        if x15 is None:
            return None
        x8 = paint(x8, x15)
        x10 |= padded_patch_6e4f6532(x15)
    try:
        x12 = render_output_6e4f6532(x8)
    except ValueError:
        return None
    if x12 != x7:
        return None
    if x8 == x7:
        return None
    return {"input": x8, "output": x7}


def generate_6e4f6532(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _compose_example_6e4f6532(diff_lb, diff_ub)
        if x0 is None:
            continue
        try:
            x1 = render_output_6e4f6532(x0["input"])
        except ValueError:
            continue
        if x1 != x0["output"]:
            continue
        return x0
