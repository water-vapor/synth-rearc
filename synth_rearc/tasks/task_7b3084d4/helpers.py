from __future__ import annotations

from itertools import permutations
from math import isqrt

from synth_rearc.core import *


ROTATIONS_7B3084D4 = (
    identity,
    rot90,
    rot180,
    rot270,
)

OUTPUT_CORNERS_7B3084D4 = ("TL", "TR", "BL", "BR")
INPUT_CORNERS_7B3084D4 = ("TL", "TR", "BL", "BR")
COLOR_POOL_7B3084D4 = (ONE, TWO, THREE, FOUR, SIX, SEVEN, EIGHT, NINE)

CORNER_SEEDS_7B3084D4 = {
    "TL": ORIGIN,
    "TR": (ZERO, NEG_ONE),
    "BL": (NEG_ONE, ZERO),
    "BR": (NEG_ONE, NEG_ONE),
}


def _grid_nonzero_count_7b3084d4(
    grid: Grid,
) -> int:
    return sum(ONE for row in grid for value in row if value != ZERO)


def _corner_loc_7b3084d4(
    grid: Grid,
    corner_name: str,
) -> tuple[int, int]:
    if corner_name == "TL":
        return (ZERO, ZERO)
    if corner_name == "TR":
        return (ZERO, len(grid[ZERO]) - ONE)
    if corner_name == "BL":
        return (len(grid) - ONE, ZERO)
    return (len(grid) - ONE, len(grid[ZERO]) - ONE)


def _corner_value_7b3084d4(
    grid: Grid,
    corner_name: str,
) -> int:
    x0 = _corner_loc_7b3084d4(grid, corner_name)
    return index(grid, x0)


def _dedupe_rotations_7b3084d4(
    grids: list[Grid],
) -> tuple[Grid, ...]:
    x0: list[Grid] = []
    for x1 in grids:
        if x1 not in x0:
            x0.append(x1)
    return tuple(x0)


def _corner_rotations_7b3084d4(
    grid: Grid,
    corner_name: str,
    *,
    require_five: bool = False,
) -> tuple[Grid, ...]:
    x0 = _dedupe_rotations_7b3084d4([x1(grid) for x1 in ROTATIONS_7B3084D4])
    if require_five:
        return tuple(x2 for x2 in x0 if _corner_value_7b3084d4(x2, corner_name) == FIVE)
    return tuple(x3 for x3 in x0 if _corner_value_7b3084d4(x3, corner_name) != ZERO)


def _paint_grid_7b3084d4(
    base: Grid,
    grid: Grid,
    top: int,
    left: int,
) -> Grid | None:
    x0 = [list(x1) for x1 in base]
    x2 = len(base)
    x3 = len(base[ZERO])
    x4 = ZERO
    for x5, x6 in enumerate(grid):
        for x7, x8 in enumerate(x6):
            if x8 == ZERO:
                continue
            x9 = top + x5
            x10 = left + x7
            if not (ZERO <= x9 < x2 and ZERO <= x10 < x3):
                return None
            if x0[x9][x10] != ZERO:
                return None
            x0[x9][x10] = x8
            x4 += ONE
    return tuple(tuple(x11) for x11 in x0), x4


def _compose_square_7b3084d4(
    corner_grids: tuple[Grid, Grid, Grid, Grid],
    side_length: int,
) -> Grid | None:
    x0, x1, x2, x3 = corner_grids
    x4 = canvas(ZERO, (side_length, side_length))
    x5 = (
        (ZERO, ZERO),
        (ZERO, side_length - len(x1[ZERO])),
        (side_length - len(x2), ZERO),
        (side_length - len(x3), side_length - len(x3[ZERO])),
    )
    x6 = ZERO
    for x7, x8 in zip(corner_grids, x5):
        x9 = _paint_grid_7b3084d4(x4, x7, x8[ZERO], x8[ONE])
        if x9 is None:
            return None
        x4, x10 = x9
        x6 += x10
    return x4 if x6 == side_length * side_length else None


def _extract_source_grids_7b3084d4(
    grid: Grid,
) -> tuple[tuple[Grid, ...], int]:
    x0 = order(objects(grid, F, T, T), ulcorner)
    if len(x0) != FOUR:
        raise ValueError("expected four 8-connected foreground objects")
    x1 = tuple(subgrid(x2, grid) for x2 in x0)
    x3 = tuple(x4 for x4, x5 in enumerate(x1) if colorcount(x5, FIVE) == ONE)
    if len(x3) != ONE:
        raise ValueError("expected one marked source object")
    return x1, x3[ZERO]


def synthesize_output_7b3084d4(
    grid: Grid,
) -> Grid:
    x0, x1 = _extract_source_grids_7b3084d4(grid)
    x2 = sum(_grid_nonzero_count_7b3084d4(x3) for x3 in x0)
    x4 = isqrt(x2)
    if x4 * x4 != x2:
        raise ValueError("foreground area is not a square")
    x5 = _corner_rotations_7b3084d4(x0[x1], "TL", require_five=True)
    x6 = tuple(x7 for x7 in range(len(x0)) if x7 != x1)
    x8: list[Grid] = []
    for x9 in permutations(x6):
        x10 = _corner_rotations_7b3084d4(x0[x9[ZERO]], "TR")
        x11 = _corner_rotations_7b3084d4(x0[x9[ONE]], "BL")
        x12 = _corner_rotations_7b3084d4(x0[x9[TWO]], "BR")
        for x13 in x5:
            for x14 in x10:
                for x15 in x11:
                    for x16 in x12:
                        x17 = _compose_square_7b3084d4((x13, x14, x15, x16), x4)
                        if x17 is None:
                            continue
                        if x17 not in x8:
                            x8.append(x17)
    if len(x8) == ZERO:
        raise ValueError("no square tiling candidate found")
    if len(x8) > ONE:
        raise ValueError("ambiguous square tiling candidates found")
    return x8[ZERO]


def _sample_region_sizes_7b3084d4(
    total_cells: int,
    side_length: int,
) -> tuple[int, int, int, int]:
    x0 = max(THREE, side_length - ONE)
    x1 = total_cells - FOUR * x0
    x2 = [uniform(0.1, 1.0) for _ in range(FOUR)]
    x3 = sum(x2)
    x4 = [x0 + int(round(x1 * x5 / x3)) for x5 in x2]
    x6 = total_cells - sum(x4)
    while x6 != ZERO:
        x7 = randint(ZERO, THREE)
        if x6 > ZERO:
            x4[x7] += ONE
            x6 -= ONE
        elif x4[x7] > x0:
            x4[x7] -= ONE
            x6 += ONE
    return tuple(x4)


def _corner_distance_7b3084d4(
    location: tuple[int, int],
    corner_name: str,
    side_length: int,
) -> int:
    x0, x1 = location
    if corner_name == "TL":
        x2 = ORIGIN
    elif corner_name == "TR":
        x2 = (ZERO, side_length - ONE)
    elif corner_name == "BL":
        x2 = (side_length - ONE, ZERO)
    else:
        x2 = (side_length - ONE, side_length - ONE)
    return abs(x0 - x2[ZERO]) + abs(x1 - x2[ONE])


def _grow_partition_7b3084d4(
    side_length: int,
) -> dict[str, frozenset[tuple[int, int]]] | None:
    x0 = {x1: set() for x1 in OUTPUT_CORNERS_7B3084D4}
    x2 = {x3: set() for x3 in OUTPUT_CORNERS_7B3084D4}
    x4 = [[None for _ in range(side_length)] for _ in range(side_length)]
    x5 = _sample_region_sizes_7b3084d4(side_length * side_length, side_length)
    x6 = dict(zip(OUTPUT_CORNERS_7B3084D4, x5))
    x7 = {
        "TL": (ZERO, ZERO),
        "TR": (ZERO, side_length - ONE),
        "BL": (side_length - ONE, ZERO),
        "BR": (side_length - ONE, side_length - ONE),
    }
    for x8, x9 in x7.items():
        x0[x8].add(x9)
        x4[x9[ZERO]][x9[ONE]] = x8
    for x10, x11 in x7.items():
        for x12 in dneighbors(x11):
            if ZERO <= x12[ZERO] < side_length and ZERO <= x12[ONE] < side_length:
                if x4[x12[ZERO]][x12[ONE]] is None:
                    x2[x10].add(x12)
    x13 = side_length * side_length - FOUR
    while x13 > ZERO:
        x14 = [x15 for x15 in OUTPUT_CORNERS_7B3084D4 if len(x2[x15]) > ZERO]
        if len(x14) == ZERO:
            return None
        x16 = max(
            x14,
            key=lambda x17: (
                x6[x17] - len(x0[x17]),
                uniform(0.0, 1.0),
            ),
        )
        x18 = tuple(
            sorted(
                x2[x16],
                key=lambda x19: (
                    _corner_distance_7b3084d4(x19, x16, side_length),
                    uniform(0.0, 1.0),
                ),
            )
        )
        x20 = x18[ZERO]
        x0[x16].add(x20)
        x4[x20[ZERO]][x20[ONE]] = x16
        x13 -= ONE
        for x21 in OUTPUT_CORNERS_7B3084D4:
            x2[x21].discard(x20)
        for x22 in dneighbors(x20):
            if ZERO <= x22[ZERO] < side_length and ZERO <= x22[ONE] < side_length:
                if x4[x22[ZERO]][x22[ONE]] is None:
                    x2[x16].add(x22)
    x23 = {x24: frozenset(x25) for x24, x25 in x0.items()}
    x26 = tuple(len(x27) for x27 in x23.values())
    if minimum(x26) < THREE:
        return None
    if len(intersection(x23["TL"], frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE)}))) == ZERO:
        return None
    return x23


def _grid_from_patch_7b3084d4(
    patch: frozenset[tuple[int, int]],
    value: int,
) -> Grid:
    x0 = normalize(patch)
    x1 = canvas(ZERO, shape(x0))
    return fill(x1, value, x0)


def sample_output_and_corner_grids_7b3084d4(
    side_length: int,
    colors: tuple[int, int, int, int],
) -> tuple[Grid, tuple[Grid, Grid, Grid, Grid]] | None:
    x0 = _grow_partition_7b3084d4(side_length)
    if x0 is None:
        return None
    x1 = canvas(ZERO, (side_length, side_length))
    x2 = fill(x1, FIVE, frozenset({ORIGIN}))
    x3 = fill(x2, colors[ZERO], remove((ZERO, ZERO), x0["TL"]))
    x4 = fill(x3, colors[ONE], x0["TR"])
    x5 = fill(x4, colors[TWO], x0["BL"])
    x6 = fill(x5, colors[THREE], x0["BR"])
    x7 = normalize(x0["TL"])
    x8 = canvas(ZERO, shape(x7))
    x9 = fill(x8, colors[ZERO], remove(ORIGIN, x7))
    x10 = fill(x9, FIVE, frozenset({ORIGIN}))
    x7 = (
        x10,
        _grid_from_patch_7b3084d4(x0["TR"], colors[ONE]),
        _grid_from_patch_7b3084d4(x0["BL"], colors[TWO]),
        _grid_from_patch_7b3084d4(x0["BR"], colors[THREE]),
    )
    return x6, x7


def _all_rotations_7b3084d4(
    grid: Grid,
) -> tuple[Grid, ...]:
    return _dedupe_rotations_7b3084d4([x0(grid) for x0 in ROTATIONS_7B3084D4])


def _absolute_cells_7b3084d4(
    grid: Grid,
    top: int,
    left: int,
) -> tuple[tuple[int, tuple[int, int]], ...]:
    x0 = []
    for x1, x2 in enumerate(grid):
        for x3, x4 in enumerate(x2):
            if x4 != ZERO:
                x0.append((x4, (top + x1, left + x3)))
    return tuple(x0)


def _corner_position_7b3084d4(
    corner_name: str,
    dimensions: tuple[int, int],
    offsets: tuple[int, int],
    canvas_side: int,
) -> tuple[int, int]:
    x0, x1 = dimensions
    x2, x3 = offsets
    if corner_name == "TL":
        return x2, x3
    if corner_name == "TR":
        return x2, canvas_side - x1 - x3
    if corner_name == "BL":
        return canvas_side - x0 - x2, x3
    return canvas_side - x0 - x2, canvas_side - x1 - x3


def _can_place_cells_7b3084d4(
    cells: tuple[tuple[int, tuple[int, int]], ...],
    blocked: set[tuple[int, int]],
    canvas_side: int,
) -> bool:
    for _, (x0, x1) in cells:
        if not (ZERO <= x0 < canvas_side and ZERO <= x1 < canvas_side):
            return False
        if (x0, x1) in blocked:
            return False
    return True


def _expand_blocked_7b3084d4(
    cells: tuple[tuple[int, tuple[int, int]], ...],
    blocked: set[tuple[int, int]],
    canvas_side: int,
) -> None:
    for _, x0 in cells:
        x1 = insert(x0, neighbors(x0))
        for x2 in x1:
            if ZERO <= x2[ZERO] < canvas_side and ZERO <= x2[ONE] < canvas_side:
                blocked.add(x2)


def place_corner_objects_in_input_7b3084d4(
    corner_grids: tuple[Grid, Grid, Grid, Grid],
    canvas_side: int = 20,
) -> Grid | None:
    x0 = list(INPUT_CORNERS_7B3084D4)
    shuffle(x0)
    x1 = tuple(choice(_all_rotations_7b3084d4(x2)) for x2 in corner_grids)
    x3 = canvas(ZERO, (canvas_side, canvas_side))
    x4: set[tuple[int, int]] = set()
    for x5, x6 in zip(x1, x0):
        x7 = len(x5)
        x8 = len(x5[ZERO])
        x9 = tuple(
            (x10, x11)
            for x10 in range(ZERO, FIVE)
            for x11 in range(ZERO, FIVE)
        )
        x12 = list(x9)
        shuffle(x12)
        x13 = False
        for x14 in x12:
            x15 = _corner_position_7b3084d4(x6, (x7, x8), x14, canvas_side)
            x16 = _absolute_cells_7b3084d4(x5, x15[ZERO], x15[ONE])
            if not _can_place_cells_7b3084d4(x16, x4, canvas_side):
                continue
            x17 = paint(x3, frozenset(x16))
            x3 = x17
            _expand_blocked_7b3084d4(x16, x4, canvas_side)
            x13 = True
            break
        if not x13:
            return None
    return x3
