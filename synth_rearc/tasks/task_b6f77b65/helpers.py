from __future__ import annotations

from synth_rearc.core import *


SegmentSpecB6F77B65 = tuple[str, int, int, int, str]
CaseSpecB6F77B65 = dict[str, object]


TEMPLATE_SEGMENTS_B6F77B65: dict[str, tuple[SegmentSpecB6F77B65, ...]] = {
    "A": (
        ("s1", 1, 8, 11, "outer_left"),
        ("s2", 2, 5, 7, "mid_left_left"),
        ("s3", 2, 8, 8, "outer_bar"),
        ("s4", 3, 5, 5, "mid_left_bar"),
        ("s5", 3, 8, 8, "outer_bar"),
        ("s6", 4, 2, 4, "shared_left"),
        ("s7", 4, 5, 5, "mid_left_bar"),
        ("s8", 4, 8, 8, "outer_bar"),
        ("s9", 5, 2, 2, "top_bar"),
        ("s10", 5, 5, 7, "mid_left_bar"),
        ("s11", 5, 8, 8, "outer_bar"),
        ("s12", 6, 2, 2, "top_bar"),
        ("s13", 6, 8, 8, "outer_bar"),
        ("s14", 7, 2, 2, "top_bar"),
        ("s15", 7, 5, 7, "shared_left"),
        ("s16", 7, 8, 8, "outer_bar"),
        ("s17", 8, 2, 4, "top_bar"),
        ("s18", 8, 5, 5, "shared_left"),
        ("s19", 8, 8, 8, "outer_bar"),
        ("s20", 9, 5, 7, "outer_right"),
        ("s21", 9, 8, 8, "outer_bar"),
        ("s22", 10, 8, 11, "outer_right"),
    ),
    "B": (
        ("t1", 1, 9, 11, "left_vert"),
        ("t2", 2, 6, 8, "left_mid_vert"),
        ("t3", 2, 9, 9, "shared_five"),
        ("t4", 3, 6, 6, "marker4"),
        ("t5", 3, 9, 11, "shared_five"),
        ("t6", 4, 6, 6, "marker4"),
        ("t7", 5, 2, 5, "top_left_vert"),
        ("t8", 5, 6, 6, "marker4"),
        ("t9", 5, 9, 11, "bottom_center_vert"),
        ("t10", 6, 2, 2, "shared_five"),
        ("t11", 6, 6, 9, "mid_right_l"),
        ("t12", 7, 2, 2, "shared_five"),
        ("t13", 7, 9, 9, "mid_right_l"),
        ("t14", 8, 2, 2, "shared_five"),
        ("t15", 8, 6, 8, "top_left_vert"),
        ("t16", 8, 9, 9, "mid_right_l"),
        ("t17", 9, 2, 5, "top_right_vert"),
        ("t18", 9, 6, 6, "right_bar"),
        ("t19", 9, 9, 9, "mid_right_l"),
        ("t20", 10, 6, 8, "right_bar"),
        ("t21", 10, 9, 11, "marker4"),
    ),
    "C": (
        ("u1", 1, 9, 11, "shared_three"),
        ("u2", 2, 2, 5, "top_left_left"),
        ("u3", 2, 6, 8, "mid_left_left"),
        ("u4", 2, 9, 9, "bottom_left_topright"),
        ("u4b", 3, 9, 9, "bottom_left_topright"),
        ("u5", 3, 2, 2, "shared_three"),
        ("u6", 3, 6, 6, "mid_left_barright"),
        ("u7", 4, 2, 5, "shared_three"),
        ("u8", 4, 6, 6, "mid_left_barright"),
        ("u9", 4, 9, 11, "bottom_left_topright"),
        ("u10", 5, 6, 6, "mid_left_barright"),
        ("u11", 6, 3, 5, "top_right_left"),
        ("u12", 6, 6, 6, "mid_left_barright"),
        ("u13", 6, 9, 11, "bottom_right_group"),
        ("u14", 7, 3, 3, "top_right_right"),
        ("u15", 7, 6, 8, "mid_left_barright"),
        ("u16", 7, 9, 9, "bottom_right_group"),
        ("u17", 8, 3, 3, "top_right_right"),
        ("u18", 8, 9, 9, "bottom_right_group"),
        ("u18b", 9, 9, 9, "bottom_right_group"),
        ("u19", 9, 3, 8, "top_right_right"),
        ("u20", 10, 9, 11, "bottom_right_right"),
    ),
}


TEMPLATE_CASES_B6F77B65: dict[str, dict[str, CaseSpecB6F77B65]] = {
    "A": {
        "outer_left": {
            "marker_probe": (8, 1),
            "removed_groups": frozenset({"outer_left"}),
            "segment_shifts": {
                "s2": 3,
                "s3": 3,
                "s4": 3,
                "s5": 3,
                "s6": 3,
                "s7": 3,
                "s8": 3,
                "s9": 3,
                "s10": 3,
                "s11": 3,
                "s12": 3,
                "s13": 3,
                "s14": 3,
                "s15": 3,
                "s16": 3,
                "s17": 3,
                "s18": 3,
                "s19": 3,
                "s20": 3,
                "s21": 3,
                "s22": 0,
            },
        },
        "outer_right": {
            "marker_probe": (8, 10),
            "removed_groups": frozenset({"outer_right"}),
            "segment_shifts": {
                "s1": 0,
                "s2": 3,
                "s3": 3,
                "s4": 3,
                "s5": 3,
                "s6": 3,
                "s7": 3,
                "s8": 3,
                "s9": 5,
                "s10": 3,
                "s11": 3,
                "s12": 5,
                "s13": 3,
                "s14": 5,
                "s15": 3,
                "s16": 3,
                "s17": 5,
                "s18": 5,
                "s19": 3,
                "s21": 3,
            },
        },
    },
    "B": {
        "marker4": {
            "marker_probe": (6, 3),
            "removed_groups": frozenset({"marker4"}),
            "segment_shifts": {
                "t1": 0,
                "t2": 0,
                "t3": 0,
                "t5": 0,
                "t7": 3,
                "t9": 0,
                "t10": 3,
                "t11": 2,
                "t12": 3,
                "t13": 2,
                "t14": 3,
                "t15": 2,
                "t16": 2,
                "t17": 3,
                "t18": 3,
                "t19": 2,
                "t20": 3,
            },
        },
        "left_vert": {
            "marker_probe": (9, 1),
            "removed_groups": frozenset({"left_vert"}),
            "segment_shifts": {
                "t2": 2,
                "t3": 2,
                "t4": 2,
                "t5": 0,
                "t6": 2,
                "t7": 2,
                "t8": 2,
                "t9": 0,
                "t10": 2,
                "t11": 0,
                "t12": 2,
                "t13": 0,
                "t14": 2,
                "t15": 0,
                "t16": 0,
                "t17": 0,
                "t18": 0,
                "t19": 0,
                "t20": 0,
                "t21": 0,
            },
        },
    },
    "C": {
        "top_right_right": {
            "marker_probe": (3, 7),
            "removed_groups": frozenset({"top_right_right"}),
            "segment_shifts": {},
        },
        "bottom_right_group": {
            "marker_probe": (9, 6),
            "removed_groups": frozenset({"bottom_right_group", "bottom_left_topright"}),
            "segment_shifts": {
                "u1": 0,
                "u2": 3,
                "u3": 3,
                "u5": 3,
                "u6": 3,
                "u7": 3,
                "u8": 3,
                "u10": 3,
                "u11": 3,
                "u12": 3,
                "u14": 3,
                "u15": 3,
                "u17": 3,
                "u19": 3,
                "u20": 0,
            },
        },
    },
}


TEMPLATE_PALETTE_GROUPS_B6F77B65: dict[str, tuple[str, ...]] = {
    "A": (
        "outer_left",
        "mid_left_left",
        "outer_bar",
        "mid_left_bar",
        "shared_left",
        "top_bar",
        "outer_right",
    ),
    "B": (
        "left_vert",
        "left_mid_vert",
        "shared_five",
        "marker4",
        "top_left_vert",
        "bottom_center_vert",
        "mid_right_l",
        "top_right_vert",
        "right_bar",
    ),
    "C": (
        "shared_three",
        "top_left_left",
        "mid_left_left",
        "bottom_left_topright",
        "mid_left_barright",
        "top_right_left",
        "top_right_right",
        "bottom_right_group",
        "bottom_right_right",
    ),
}


HEADER_EXTRAS_B6F77B65: dict[tuple[str, str], tuple[tuple[int, int, str], ...]] = {
    ("C", "bottom_right_group"): ((0, 1, "bottom_left_topright"),),
}


def _occupancy_for_template_b6f77b65(
    template: str,
) -> frozenset[tuple[int, int]]:
    return frozenset(
        (row, col)
        for _, col, top, bottom, _ in TEMPLATE_SEGMENTS_B6F77B65[template]
        for row in range(top, bottom + ONE)
    )


TEMPLATE_OCCUPANCIES_B6F77B65 = {
    template: _occupancy_for_template_b6f77b65(template)
    for template in TEMPLATE_SEGMENTS_B6F77B65
}


def detect_template_b6f77b65(
    grid: Grid,
) -> str | None:
    x0 = frozenset(
        (i, j)
        for i, row in enumerate(grid)
        for j, value in enumerate(row)
        if i > ZERO and value != ZERO
    )
    for x1, x2 in TEMPLATE_OCCUPANCIES_B6F77B65.items():
        if x0 == x2:
            return x1
    return None


def identify_case_b6f77b65(
    grid: Grid,
    template: str,
) -> str:
    x0 = grid[ZERO][ZERO]
    x1 = TEMPLATE_CASES_B6F77B65[template]
    for x2, x3 in x1.items():
        x4, x5 = x3["marker_probe"]
        if grid[x4][x5] == x0:
            return x2
    return "identity"


def render_template_input_b6f77b65(
    template: str,
    palette: dict[str, int],
    marker_group: str | None,
) -> Grid:
    x0 = [[ZERO] * 12 for _ in range(12)]
    if marker_group is None:
        x2 = tuple(value for value in range(ONE, TEN) if value not in palette.values())
        x1 = choice(x2)
    else:
        x1 = palette[marker_group]
    x0[ZERO][ZERO] = x1
    x2 = HEADER_EXTRAS_B6F77B65.get((template, marker_group or "identity"), tuple())
    for x3, x4, x5 in x2:
        x0[x3][x4] = palette[x5]
    for _, x3, x4, x5, x6 in TEMPLATE_SEGMENTS_B6F77B65[template]:
        x7 = palette[x6]
        for x8 in range(x4, x5 + ONE):
            x0[x8][x3] = x7
    return tuple(tuple(row) for row in x0)


def transform_grid_b6f77b65(
    grid: Grid,
) -> Grid:
    x0 = detect_template_b6f77b65(grid)
    if x0 is None:
        return grid
    x1 = identify_case_b6f77b65(grid, x0)
    if x1 == "identity":
        return grid
    x2 = TEMPLATE_CASES_B6F77B65[x0][x1]
    x3 = x2["removed_groups"]
    x4 = x2["segment_shifts"]
    x5 = [[ZERO] * len(grid[ZERO]) for _ in range(len(grid))]
    for x6, x7 in enumerate(grid[ZERO]):
        if x7 != ZERO:
            x5[ZERO][x6] = x7
    for x6, x7, x8, x9, x10 in TEMPLATE_SEGMENTS_B6F77B65[x0]:
        if x10 in x3:
            continue
        x11 = x4.get(x6, ZERO)
        for x12 in range(x8, x9 + ONE):
            x5[x12 + x11][x7] = grid[x12][x7]
    return tuple(tuple(row) for row in x5)


def _sample_palette_b6f77b65(
    template: str,
) -> dict[str, int]:
    x0 = TEMPLATE_PALETTE_GROUPS_B6F77B65[template]
    x1 = sample(tuple(range(ONE, TEN)), len(x0))
    return {group: value for group, value in zip(x0, x1)}


def generate_input_b6f77b65(
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    x0 = choice(("A", "A", "B", "B", "C"))
    x1 = _sample_palette_b6f77b65(x0)
    x2 = tuple(TEMPLATE_CASES_B6F77B65[x0].keys())
    x3 = choice(x2)
    return render_template_input_b6f77b65(x0, x1, x3)
