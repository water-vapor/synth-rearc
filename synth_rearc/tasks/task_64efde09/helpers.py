from __future__ import annotations

from dataclasses import dataclass
from random import choice, sample

from synth_rearc.core import *


BG_64EFDE09 = EIGHT
CHANNEL_COUNT_64EFDE09 = THREE

FAMILY_A_64EFDE09 = "A"
FAMILY_B_64EFDE09 = "B"
FAMILY_C_64EFDE09 = "C"

DIR_LEFT_64EFDE09 = "left"
DIR_RIGHT_64EFDE09 = "right"
DIR_UP_64EFDE09 = "up"
DIR_DOWN_64EFDE09 = "down"


@dataclass(frozen=True)
class ProjectorTemplate64efde09:
    name: str
    family: str
    grid: Grid
    direction: str
    channels: tuple[int, int, int]
    global_order: tuple[int, int, int]


@dataclass(frozen=True)
class Projector64efde09:
    template: ProjectorTemplate64efde09
    ul: tuple[int, int]

    @property
    def lr(
        self,
    ) -> tuple[int, int]:
        x0 = self.template.grid
        return (self.ul[ZERO] + len(x0) - ONE, self.ul[ONE] + len(x0[ZERO]) - ONE)


TEMPLATE_A_LEFT_64EFDE09 = ProjectorTemplate64efde09(
    "A_left",
    FAMILY_A_64EFDE09,
    ((4, 4), (2, 4), (2, 3), (2, 3), (2, 3), (2, 3), (2, 4)),
    DIR_LEFT_64EFDE09,
    (1, 4, 5),
    (0, 1, 2),
)
TEMPLATE_A_RIGHT_64EFDE09 = ProjectorTemplate64efde09(
    "A_right",
    FAMILY_A_64EFDE09,
    ((4, 4), (4, 2), (3, 2), (3, 2), (3, 2), (3, 2), (4, 2)),
    DIR_RIGHT_64EFDE09,
    (1, 4, 5),
    (0, 1, 2),
)
TEMPLATE_A_DOWN_64EFDE09 = ProjectorTemplate64efde09(
    "A_down",
    FAMILY_A_64EFDE09,
    ((4, 3, 3, 3, 3, 4, 4), (2, 2, 2, 2, 2, 2, 4)),
    DIR_DOWN_64EFDE09,
    (1, 2, 5),
    (2, 1, 0),
)

TEMPLATE_B_LEFT_64EFDE09 = ProjectorTemplate64efde09(
    "B_left",
    FAMILY_B_64EFDE09,
    ((1, 4), (1, 4), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 4)),
    DIR_LEFT_64EFDE09,
    (1, 3, 5),
    (0, 1, 2),
)
TEMPLATE_B_RIGHT_64EFDE09 = ProjectorTemplate64efde09(
    "B_right",
    FAMILY_B_64EFDE09,
    ((4, 1), (4, 1), (2, 1), (2, 1), (2, 1), (2, 1), (2, 1), (2, 1), (4, 1)),
    DIR_RIGHT_64EFDE09,
    (1, 3, 5),
    (0, 1, 2),
)
TEMPLATE_B_UP_64EFDE09 = ProjectorTemplate64efde09(
    "B_up",
    FAMILY_B_64EFDE09,
    ((1, 1, 1, 1, 1, 1, 1, 1, 1), (4, 2, 2, 2, 2, 2, 2, 4, 4)),
    DIR_UP_64EFDE09,
    (3, 5, 7),
    (2, 1, 0),
)

TEMPLATE_C_LEFT_64EFDE09 = ProjectorTemplate64efde09(
    "C_left",
    FAMILY_C_64EFDE09,
    ((1, 1), (4, 1), (4, 2), (4, 2), (4, 2), (4, 2), (3, 3)),
    DIR_LEFT_64EFDE09,
    (1, 3, 5),
    (0, 1, 2),
)
TEMPLATE_C_RIGHT_64EFDE09 = ProjectorTemplate64efde09(
    "C_right",
    FAMILY_C_64EFDE09,
    ((3, 3), (2, 4), (2, 4), (2, 4), (2, 4), (1, 4), (1, 1)),
    DIR_RIGHT_64EFDE09,
    (1, 3, 5),
    (2, 1, 0),
)
TEMPLATE_C_DOWN_64EFDE09 = ProjectorTemplate64efde09(
    "C_down",
    FAMILY_C_64EFDE09,
    ((3, 2, 2, 2, 2, 1, 1), (3, 4, 4, 4, 4, 4, 1)),
    DIR_DOWN_64EFDE09,
    (1, 3, 5),
    (2, 1, 0),
)

TEMPLATES_64EFDE09 = (
    TEMPLATE_A_LEFT_64EFDE09,
    TEMPLATE_A_RIGHT_64EFDE09,
    TEMPLATE_A_DOWN_64EFDE09,
    TEMPLATE_B_LEFT_64EFDE09,
    TEMPLATE_B_RIGHT_64EFDE09,
    TEMPLATE_B_UP_64EFDE09,
    TEMPLATE_C_LEFT_64EFDE09,
    TEMPLATE_C_RIGHT_64EFDE09,
    TEMPLATE_C_DOWN_64EFDE09,
)

TEMPLATE_LOOKUP_64EFDE09 = {x0.grid: x0 for x0 in TEMPLATES_64EFDE09}

SOURCE_COLOR_POOL_64EFDE09 = {
    FAMILY_A_64EFDE09: (ONE, FIVE, SIX, SEVEN, NINE),
    FAMILY_B_64EFDE09: (THREE, FIVE, SIX, SEVEN, NINE),
    FAMILY_C_64EFDE09: (FIVE, SIX, SEVEN, NINE),
}


def _tuple_grid_64efde09(
    grid,
) -> Grid:
    return tuple(tuple(row) for row in grid)


def _projector_sort_key_64efde09(
    obj: Object,
) -> tuple[int, int]:
    return (uppermost(obj), leftmost(obj))


def _paint_template_64efde09(
    grid: Grid,
    projector: Projector64efde09,
) -> Grid:
    x0 = frozenset(
        (value, (projector.ul[ZERO] + i, projector.ul[ONE] + j))
        for i, row in enumerate(projector.template.grid)
        for j, value in enumerate(row)
    )
    return paint(grid, x0)


def _projector_rays_64efde09(
    projector: Projector64efde09,
    dims: tuple[int, int],
) -> tuple[frozenset[tuple[int, int]], ...]:
    x0 = projector.template.direction
    x1 = projector.template.channels
    x2 = projector.ul
    x3 = projector.lr
    if x0 == DIR_LEFT_64EFDE09:
        return tuple(
            frozenset((x2[ZERO] + row_offset, j) for j in range(x2[ONE]))
            for row_offset in x1
        )
    if x0 == DIR_RIGHT_64EFDE09:
        return tuple(
            frozenset((x2[ZERO] + row_offset, j) for j in range(x3[ONE] + ONE, dims[ONE]))
            for row_offset in x1
        )
    if x0 == DIR_UP_64EFDE09:
        return tuple(
            frozenset((i, x2[ONE] + col_offset) for i in range(x2[ZERO]))
            for col_offset in x1
        )
    return tuple(
        frozenset((i, x2[ONE] + col_offset) for i in range(x3[ZERO] + ONE, dims[ZERO]))
        for col_offset in x1
    )


def _discover_64efde09(
    grid: Grid,
) -> tuple[str, tuple[Projector64efde09, ...], tuple[Object, ...]]:
    x0 = objects(grid, F, F, T)
    x1 = tuple(sorted(x0, key=_projector_sort_key_64efde09))
    x2 = []
    x3 = []
    x4 = None
    for x5 in x1:
        if size(x5) == ONE:
            x3.append(x5)
            continue
        x6 = subgrid(x5, grid)
        x7 = TEMPLATE_LOOKUP_64EFDE09.get(x6)
        if x7 is None:
            raise ValueError(f"unrecognized projector template: {x6}")
        if x4 is None:
            x4 = x7.family
        elif x4 != x7.family:
            raise ValueError("mixed projector families are not supported")
        x2.append(Projector64efde09(x7, ulcorner(x5)))
    if x4 is None:
        raise ValueError("no projector objects found")
    return x4, tuple(x2), tuple(x3)


def _channel_colors_64efde09(
    grid: Grid,
    projectors: tuple[Projector64efde09, ...],
    markers: tuple[Object, ...],
) -> tuple[int, int, int]:
    x0 = shape(grid)
    x1: dict[int, int] = {}
    for x2 in markers:
        x3 = ulcorner(x2)
        x4 = color(x2)
        x5 = []
        for x6 in projectors:
            x7 = _projector_rays_64efde09(x6, x0)
            for x8, x9 in enumerate(x7):
                if x3 in x9:
                    x5.append(x6.template.global_order[x8])
        if len(set(x5)) != ONE:
            raise ValueError(f"ambiguous channel source at {x3}: {x5}")
        x1[first(tuple(set(x5)))] = x4
    if set(x1) != {ZERO, ONE, TWO}:
        raise ValueError(f"incomplete channel assignment: {x1}")
    return (x1[ZERO], x1[ONE], x1[TWO])


def render_output_64efde09(
    grid: Grid,
) -> Grid:
    x0, x1, x2 = _discover_64efde09(grid)
    x3 = _channel_colors_64efde09(grid, x1, x2)
    x4 = shape(grid)
    x5 = grid
    for x6 in x1:
        x7 = _projector_rays_64efde09(x6, x4)
        for x8, x9 in enumerate(x7):
            x10 = x6.template.global_order[x8]
            x5 = fill(x5, x3[x10], x9)
    return x5


def _projector_64efde09(
    template: ProjectorTemplate64efde09,
    ul: tuple[int, int],
) -> Projector64efde09:
    return Projector64efde09(template, ul)


def _host_endpoint_64efde09(
    projector: Projector64efde09,
    local_idx: int,
    dims: tuple[int, int],
) -> tuple[int, int]:
    x0 = projector.template.direction
    x1 = projector.template.channels[local_idx]
    if x0 == DIR_LEFT_64EFDE09:
        return (projector.ul[ZERO] + x1, ZERO)
    if x0 == DIR_RIGHT_64EFDE09:
        return (projector.ul[ZERO] + x1, dims[ONE] - ONE)
    if x0 == DIR_UP_64EFDE09:
        return (ZERO, projector.ul[ONE] + x1)
    return (dims[ZERO] - ONE, projector.ul[ONE] + x1)


def _paint_sources_64efde09(
    grid: Grid,
    projectors: tuple[Projector64efde09, ...],
    source_specs: tuple[tuple[int, int, int], ...],
    colors: tuple[int, int, int],
    dims: tuple[int, int],
) -> Grid:
    x0 = grid
    for x1, x2, x3 in source_specs:
        x4 = _host_endpoint_64efde09(projectors[x1], x2, dims)
        x5 = colors[x3]
        x0 = fill(x0, x5, initset(x4))
    return x0


def _valid_input_64efde09(
    grid: Grid,
) -> bool:
    try:
        x0 = render_output_64efde09(grid)
    except ValueError:
        return False
    return grid != x0


def _build_family_a_64efde09(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (25, 30))
        x1 = unifint(diff_lb, diff_ub, (26, 30))
        x2 = randint(x1 - EIGHT, x1 - SIX)
        x3_lb = max(EIGHT, x1 // TWO - THREE)
        x3_ub = min(x2 - EIGHT, x1 // TWO + ONE)
        if x3_lb > x3_ub:
            continue
        x3 = randint(x3_lb, x3_ub)
        x4 = randint(ONE, THREE)
        x5_lb = max(EIGHT, x3 - THREE)
        x5_ub = min(x2 - NINE, x1 - 16)
        if x5_lb > x5_ub:
            continue
        x5 = randint(x5_lb, x5_ub)
        x6 = randint(ZERO, TWO)
        x7 = randint(SIX, min(10, x0 - 14))
        x8_lb = max(x7 + FIVE, x0 // TWO)
        x8_ub = min(x0 - 10, x7 + EIGHT)
        if x8_lb > x8_ub:
            continue
        x8 = randint(x8_lb, x8_ub)
        x9_lb = max(x8 + ONE, x0 // TWO + ONE)
        x9_ub = x0 - EIGHT
        if x9_lb > x9_ub:
            continue
        x9 = randint(x9_lb, x9_ub)
        x10 = (
            _projector_64efde09(TEMPLATE_A_LEFT_64EFDE09, (x6, x3)),
            _projector_64efde09(TEMPLATE_A_DOWN_64EFDE09, (x7, x4)),
            _projector_64efde09(TEMPLATE_A_DOWN_64EFDE09, (x8, x5)),
            _projector_64efde09(TEMPLATE_A_RIGHT_64EFDE09, (x9, x2)),
        )
        x11 = canvas(BG_64EFDE09, (x0, x1))
        for x12 in x10:
            x11 = _paint_template_64efde09(x11, x12)
        x13 = tuple(sample(SOURCE_COLOR_POOL_64EFDE09[FAMILY_A_64EFDE09], CHANNEL_COUNT_64EFDE09))
        x14 = (
            (THREE, ZERO, ZERO),
            (ONE, ONE, ONE),
            (TWO, ZERO, TWO),
        )
        x15 = _paint_sources_64efde09(x11, x10, x14, x13, (x0, x1))
        if not _valid_input_64efde09(x15):
            continue
        return {"input": x15, "output": render_output_64efde09(x15)}


def _build_family_b_64efde09(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (20, 24))
        x1 = unifint(diff_lb, diff_ub, (24, 30))
        x2 = randint(FOUR, SIX)
        x3 = randint(max(11, x1 - 15), x1 - 11)
        x4 = randint(x1 - NINE, x1 - SEVEN)
        x5 = randint(ZERO, TWO)
        x6 = randint(TWO, FOUR)
        x7_lb = max(x6 + SEVEN, x0 // TWO)
        x7_ub = x0 - 10
        if x7_lb > x7_ub:
            continue
        x7 = randint(x7_lb, x7_ub)
        x8 = (
            _projector_64efde09(TEMPLATE_B_LEFT_64EFDE09, (x5, x2)),
            _projector_64efde09(TEMPLATE_B_UP_64EFDE09, (x6, x3)),
            _projector_64efde09(TEMPLATE_B_RIGHT_64EFDE09, (x7, x4)),
        )
        x9 = canvas(BG_64EFDE09, (x0, x1))
        for x10 in x8:
            x9 = _paint_template_64efde09(x9, x10)
        x11 = tuple(sample(SOURCE_COLOR_POOL_64EFDE09[FAMILY_B_64EFDE09], CHANNEL_COUNT_64EFDE09))
        x12 = (
            (ZERO, ZERO, ZERO),
            (ONE, ONE, ONE),
            (ZERO, TWO, TWO),
        )
        x13 = _paint_sources_64efde09(x9, x8, x12, x11, (x0, x1))
        if not _valid_input_64efde09(x13):
            continue
        return {"input": x13, "output": render_output_64efde09(x13)}


def _build_family_c_64efde09(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (27, 30))
        x1 = unifint(diff_lb, diff_ub, (28, 30))
        x2 = randint(FOUR, SIX)
        x3 = randint(max(12, x1 - 12), x1 - TEN)
        x4 = randint(x1 - FIVE, x1 - FOUR)
        x5 = randint(SEVEN, TEN)
        x6 = randint(ZERO, TWO)
        x7 = randint(TWO, FOUR)
        x8 = randint(10, min(13, x0 - 12))
        x9 = randint(x0 - EIGHT, x0 - SEVEN)
        x10 = (
            _projector_64efde09(TEMPLATE_C_LEFT_64EFDE09, (x6, x2)),
            _projector_64efde09(TEMPLATE_C_DOWN_64EFDE09, (x7, x3)),
            _projector_64efde09(TEMPLATE_C_RIGHT_64EFDE09, (x8, x4)),
            _projector_64efde09(TEMPLATE_C_LEFT_64EFDE09, (x9, x5)),
        )
        x11 = canvas(BG_64EFDE09, (x0, x1))
        for x12 in x10:
            x11 = _paint_template_64efde09(x11, x12)
        x13 = tuple(sample(SOURCE_COLOR_POOL_64EFDE09[FAMILY_C_64EFDE09], CHANNEL_COUNT_64EFDE09))
        x14 = (
            (ZERO, ZERO, ZERO),
            (ONE, ONE, ONE),
            (TWO, ZERO, TWO),
        )
        x15 = _paint_sources_64efde09(x11, x10, x14, x13, (x0, x1))
        if not _valid_input_64efde09(x15):
            continue
        return {"input": x15, "output": render_output_64efde09(x15)}


def build_example_64efde09(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = choice((FAMILY_A_64EFDE09, FAMILY_B_64EFDE09, FAMILY_C_64EFDE09))
    if x0 == FAMILY_A_64EFDE09:
        return _build_family_a_64efde09(diff_lb, diff_ub)
    if x0 == FAMILY_B_64EFDE09:
        return _build_family_b_64efde09(diff_lb, diff_ub)
    return _build_family_c_64efde09(diff_lb, diff_ub)
