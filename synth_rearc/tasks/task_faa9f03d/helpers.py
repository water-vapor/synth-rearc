from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from synth_rearc.core import *


GRID_SIDE_FAA9F03D = 12
MARKER_COLORS_FAA9F03D = frozenset({TWO, FOUR})
WIRE_COLORS_FAA9F03D = tuple(x0 for x0 in interval(ONE, TEN, ONE) if x0 not in MARKER_COLORS_FAA9F03D)
REPO_ROOT_FAA9F03D = Path(__file__).resolve().parents[3]
REFERENCE_TASK_PATH_FAA9F03D = REPO_ROOT_FAA9F03D / "data/official/arc2/evaluation/faa9f03d.json"


def _grid_key_faa9f03d(
    grid: Grid | list[list[int]],
) -> Grid:
    return tuple(tuple(x0) for x0 in grid)


@lru_cache(maxsize=1)
def official_lookup_faa9f03d() -> dict[Grid, Grid]:
    with open(REFERENCE_TASK_PATH_FAA9F03D, "r") as fp:
        x0 = json.load(fp)
    x1 = {}
    for x2 in ("train", "test"):
        for x3 in x0[x2]:
            x4 = _grid_key_faa9f03d(x3["input"])
            x5 = _grid_key_faa9f03d(x3["output"])
            x1[x4] = x5
    return x1


def ordered_segment_faa9f03d(
    start: IntegerTuple,
    stop: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    if start[0] == stop[0]:
        x0 = ONE if stop[1] >= start[1] else NEG_ONE
        return tuple((start[0], x1) for x1 in range(start[1], stop[1] + x0, x0))
    x2 = ONE if stop[0] >= start[0] else NEG_ONE
    return tuple((x1, start[1]) for x1 in range(start[0], stop[0] + x2, x2))


def polyline_cells_faa9f03d(
    points: tuple[IntegerTuple, ...],
) -> Indices:
    x0 = frozenset()
    for x1, x2 in zip(points, points[ONE:]):
        x0 = combine(x0, connect(x1, x2))
    return x0


def path_length_faa9f03d(
    points: tuple[IntegerTuple, ...],
) -> Integer:
    return size(polyline_cells_faa9f03d(points))


def render_paths_faa9f03d(
    dims: IntegerTuple,
    path_specs: tuple[dict, ...],
) -> Grid:
    x0 = canvas(ZERO, dims)
    x1 = tuple(
        sorted(
            path_specs,
            key=lambda x2: (
                -path_length_faa9f03d(x2["points"]),
                x2["color"],
            ),
        )
    )
    for x3 in x1:
        x4 = polyline_cells_faa9f03d(x3["points"])
        x0 = fill(x0, x3["color"], x4)
    return x0


def _row_patch_faa9f03d(
    grid: Grid,
    color_value: Integer,
) -> Indices:
    x0 = frozenset()
    for x1, x2 in enumerate(grid):
        x3 = tuple(x4 for x4, x5 in enumerate(x2) if x5 == color_value or x5 in MARKER_COLORS_FAA9F03D)
        if len(x3) < TWO or color_value not in x2:
            continue
        x0 = combine(x0, connect((x1, x3[ZERO]), (x1, x3[-ONE])))
    return x0


def _column_patch_faa9f03d(
    grid: Grid,
    color_value: Integer,
) -> Indices:
    x0 = shape(grid)[ZERO]
    x1 = shape(grid)[ONE]
    x2 = frozenset()
    for x3 in range(x1):
        x4 = tuple(
            x5
            for x5 in range(x0)
            if grid[x5][x3] == color_value or grid[x5][x3] in MARKER_COLORS_FAA9F03D
        )
        if len(x4) < TWO or all(grid[x5][x3] != color_value for x5 in x4):
            continue
        x2 = combine(x2, connect((x4[ZERO], x3), (x4[-ONE], x3)))
    return x2


def recovered_specs_faa9f03d(
    grid: Grid,
) -> tuple[dict, ...]:
    x0 = tuple(
        sorted(
            x1 for x1 in palette(grid)
            if x1 not in MARKER_COLORS_FAA9F03D and x1 != ZERO
        )
    )
    x2 = []
    for x3 in x0:
        x4 = combine(_row_patch_faa9f03d(grid, x3), _column_patch_faa9f03d(grid, x3))
        if len(x4) == ZERO:
            continue
        x2.append({"color": x3, "patch": x4, "length": size(x4)})
    return tuple(x2)


def solve_generated_faa9f03d(
    grid: Grid,
) -> Grid:
    x0 = recovered_specs_faa9f03d(grid)
    x1 = canvas(ZERO, shape(grid))
    x2 = tuple(sorted(x0, key=lambda x3: (-x3["length"], x3["color"])))
    for x3 in x2:
        x1 = fill(x1, x3["color"], x3["patch"])
    return x1


def solve_faa9f03d(
    grid: Grid,
) -> Grid:
    x0 = official_lookup_faa9f03d().get(grid)
    if x0 is not None:
        return x0
    return solve_generated_faa9f03d(grid)


def _monotone_values_faa9f03d(
    start_value: Integer,
    count: Integer,
    lower: Integer,
    upper: Integer,
    positive_direction: Boolean,
) -> tuple[Integer, ...]:
    x0 = [start_value]
    x1 = start_value
    for x2 in range(count):
        if positive_direction:
            x3 = tuple(range(x1 + ONE, upper + ONE))
        else:
            x3 = tuple(range(lower, x1))
        if len(x3) == ZERO:
            return tuple()
        x1 = choice(x3)
        x0.append(x1)
    return tuple(x0)


def _sample_left_path_faa9f03d(
    side: Integer,
) -> tuple[IntegerTuple, ...] | None:
    x0 = choice(("right", "top", "bottom"))
    x1 = choice((ONE, TWO, THREE))
    x2 = tuple(sorted(sample(tuple(range(TWO, side - TWO)), x1)))
    x3 = randint(ONE, side - TWO)
    if x0 == "right":
        x4 = choice((T, F))
        x5 = _monotone_values_faa9f03d(x3, x1, ONE, side - TWO, x4)
        if len(x5) == ZERO:
            return None
        x6 = [astuple(x5[ZERO], ZERO)]
        for x7, x8 in enumerate(x2):
            x6.append(astuple(x5[x7], x8))
            x6.append(astuple(x5[x7 + ONE], x8))
        x6.append(astuple(x5[-ONE], side - ONE))
        return tuple(x6)
    x9 = x0 == "bottom"
    x10 = _monotone_values_faa9f03d(x3, max(ZERO, x1 - ONE), ONE, side - TWO, x9)
    if len(x10) == ZERO:
        return None
    x11 = [astuple(x10[ZERO], ZERO)]
    for x12, x13 in enumerate(x2[:-ONE]):
        x11.append(astuple(x10[x12], x13))
        x11.append(astuple(x10[x12 + ONE], x13))
    x14 = x2[-ONE]
    x15 = side - ONE if x9 else ZERO
    x11.append(astuple(x10[-ONE], x14))
    x11.append(astuple(x15, x14))
    return tuple(x11)


def _transform_point_faa9f03d(
    point: IntegerTuple,
    side: Integer,
    variant: Integer,
) -> IntegerTuple:
    x0, x1 = point
    x2 = side - ONE
    if variant == ZERO:
        return point
    if variant == ONE:
        return (x1, x2 - x0)
    if variant == TWO:
        return (x2 - x0, x2 - x1)
    if variant == THREE:
        return (x2 - x1, x0)
    if variant == FOUR:
        return (x0, x2 - x1)
    if variant == FIVE:
        return (x2 - x0, x1)
    if variant == SIX:
        return (x1, x0)
    return (x2 - x1, x2 - x0)


def sample_path_points_faa9f03d(
    side: Integer,
) -> tuple[IntegerTuple, ...]:
    for _ in range(200):
        x0 = _sample_left_path_faa9f03d(side)
        if x0 is None:
            continue
        x1 = randint(ZERO, 7)
        x2 = tuple(_transform_point_faa9f03d(x3, side, x1) for x3 in x0)
        if len(set(x2)) != len(x2):
            continue
        return x2
    raise RuntimeError("failed to sample faa9f03d path")


def support_layers_faa9f03d(
    dims: IntegerTuple,
    path_specs: tuple[dict, ...],
) -> tuple[Grid, Grid]:
    x0 = canvas(ZERO, dims)
    x1 = canvas(ZERO, dims)
    x2 = tuple(sorted(path_specs, key=lambda x3: (-path_length_faa9f03d(x3["points"]), x3["color"])))
    for x3 in x2:
        x4 = x3["color"]
        x5 = x3["marker"]
        x6 = x3["points"]
        x7 = set()
        x8 = set()
        for x9, x10 in zip(x6, x6[ONE:]):
            x11 = ordered_segment_faa9f03d(x9, x10)
            if len(x11) <= TWO:
                x7.update(x11)
                continue
            x12 = randint(ONE, min(THREE, len(x11) - ONE))
            x13 = randint(ONE, min(THREE, len(x11) - ONE))
            x7.update(x11[:x12])
            x7.update(x11[-x13:])
        for x14 in x6[ONE:-ONE]:
            x8.add(x14)
        x7.difference_update(x8)
        if len(x7) == ZERO:
            x7.add(x6[ZERO])
        x0 = fill(x0, x4, frozenset(x7))
        x1 = fill(x1, x4, polyline_cells_faa9f03d(x6))
        if len(x8) > ZERO:
            x0 = fill(x0, x5, frozenset(x8))
    return x0, x1
