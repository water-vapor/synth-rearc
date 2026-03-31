from collections import defaultdict

from synth_rearc.core import *


ACTIVE_COLORS_9BBF930D = (ZERO, ONE, TWO, THREE, FOUR, FIVE, EIGHT, NINE)


def split_runs_9bbf930d(
    values: list[Integer],
) -> list[list[Integer]]:
    values = sorted(values)
    runs = []
    run = [values[ZERO]]
    for x0, x1 in zip(values, values[ONE:]):
        if x1 == x0 + ONE:
            run.append(x1)
        else:
            runs.append(run)
            run = [x1]
    runs.append(run)
    return runs


def tunnel_maps_9bbf930d(
    grid: Grid,
) -> tuple[
    dict[IntegerTuple, dict[Integer, set[IntegerTuple]]],
    dict[IntegerTuple, dict[Integer, set[IntegerTuple]]],
]:
    h, w = shape(grid)
    directions = defaultdict(lambda: defaultdict(set))
    for i in range(h):
        for j in range(w):
            if grid[i][j] != SEVEN:
                continue
            if (
                ZERO < i < h - ONE
                and grid[i - ONE][j] == grid[i + ONE][j]
                and grid[i - ONE][j] not in (SIX, SEVEN)
            ):
                x0 = grid[i - ONE][j]
                directions[(i, j)][x0].update((LEFT, RIGHT))
            if (
                ZERO < j < w - ONE
                and grid[i][j - ONE] == grid[i][j + ONE]
                and grid[i][j - ONE] not in (SIX, SEVEN)
            ):
                x1 = grid[i][j - ONE]
                directions[(i, j)][x1].update((UP, DOWN))
    horizontal = defaultdict(list)
    vertical = defaultdict(list)
    for x2, x3 in list(directions.items()):
        i, j = x2
        for x4, x5 in x3.items():
            if LEFT in x5:
                horizontal[(x4, i)].append(j)
            if UP in x5:
                vertical[(x4, j)].append(i)
    for x6, x7 in horizontal.items():
        x8, i = x6
        for x9 in split_runs_9bbf930d(x7):
            for j in (x9[ZERO] - ONE, x9[-ONE] + ONE):
                if ZERO <= j < w and grid[i][j] == SEVEN:
                    directions[(i, j)][x8].update((LEFT, RIGHT))
    for x10, x11 in vertical.items():
        x12, j = x10
        for x13 in split_runs_9bbf930d(x11):
            for i in (x13[ZERO] - ONE, x13[-ONE] + ONE):
                if ZERO <= i < h and grid[i][j] == SEVEN:
                    directions[(i, j)][x12].update((UP, DOWN))
    neighbors = defaultdict(lambda: defaultdict(set))
    for x14, x15 in directions.items():
        for x16, x17 in x15.items():
            for x18 in x17:
                x19 = add(x14, x18)
                if x18 in directions.get(x19, {}).get(x16, set()):
                    neighbors[x14][x16].add(x19)
    return directions, neighbors


def launch_entry_9bbf930d(
    grid: Grid,
    row: Integer,
    directions: dict[IntegerTuple, dict[Integer, set[IntegerTuple]]],
    neighbors: dict[IntegerTuple, dict[Integer, set[IntegerTuple]]],
) -> tuple[IntegerTuple, Integer] | None:
    w = width(grid)
    for j in range(ONE, w):
        if grid[row][j] != SEVEN:
            return None
        x0 = (row, j)
        for x1, x2 in directions.get(x0, {}).items():
            x3 = add(x0, RIGHT)
            if RIGHT in x2 and x3 in neighbors[x0][x1]:
                return x0, x1
    return None


def trace_launcher_9bbf930d(
    grid: Grid,
    row: Integer,
    directions: dict[IntegerTuple, dict[Integer, set[IntegerTuple]]],
    neighbors: dict[IntegerTuple, dict[Integer, set[IntegerTuple]]],
) -> IntegerTuple:
    h, w = shape(grid)
    x0 = launch_entry_9bbf930d(grid, row, directions, neighbors)
    if x0 is None:
        return (row, ZERO)
    x1, x2 = x0
    x3 = (row, x1[ONE] - ONE)
    x4 = RIGHT
    while True:
        x5 = add(x1, x4)
        if x5 in neighbors[x1][x2] and x5 != x3:
            x3, x1 = x1, x5
            continue
        x6 = tuple(x7 for x7 in neighbors[x1][x2] if x7 != x3)
        if len(x6) > ZERO:
            x8 = x6[ZERO]
            x4 = subtract(x8, x1)
            x3, x1 = x1, x8
            continue
        while True:
            x9 = add(x1, x4)
            if not (ZERO <= x9[ZERO] < h and ZERO <= x9[ONE] < w):
                return x1
            if index(grid, x9) != SEVEN:
                return x1
            x1 = x9
            x10 = add(x1, x4)
            x11 = tuple(
                x12
                for x12, x13 in directions.get(x1, {}).items()
                if x4 in x13 and x10 in neighbors[x1][x12]
            )
            if len(x11) == ZERO:
                continue
            x2 = x11[ZERO]
            x3 = subtract(x1, x4)
            break


def horizontal_segment_9bbf930d(
    row: Integer,
    start: Integer,
    stop: Integer,
    color_: Integer,
) -> dict:
    return {
        "axis": "h",
        "row": row,
        "start": start,
        "stop": stop,
        "color": color_,
    }


def vertical_segment_9bbf930d(
    col: Integer,
    start: Integer,
    stop: Integer,
    direction: IntegerTuple,
    color_: Integer,
) -> dict:
    return {
        "axis": "v",
        "col": col,
        "start": start,
        "stop": stop,
        "direction": direction,
        "color": color_,
    }


def segment_cells_9bbf930d(
    segment: dict,
) -> set[IntegerTuple]:
    if segment["axis"] == "h":
        return {
            (segment["row"], j)
            for j in range(segment["start"], segment["stop"] + ONE)
        }
    return {
        (i, segment["col"])
        for i in range(segment["start"], segment["stop"] + ONE)
    }


def segment_openings_9bbf930d(
    segment: dict,
) -> set[IntegerTuple]:
    if segment["axis"] == "h":
        return {
            (segment["row"], segment["start"] - ONE),
            (segment["row"], segment["stop"] + ONE),
        }
    return {
        (segment["start"] - ONE, segment["col"]),
        (segment["stop"] + ONE, segment["col"]),
    }


def segment_walls_9bbf930d(
    segment: dict,
) -> set[tuple[Integer, Integer, Integer]]:
    x0 = segment["color"]
    if segment["axis"] == "h":
        return {
            (segment["row"] - ONE, j, x0)
            for j in range(segment["start"], segment["stop"] + ONE)
        } | {
            (segment["row"] + ONE, j, x0)
            for j in range(segment["start"], segment["stop"] + ONE)
        }
    return {
        (i, segment["col"] - ONE, x0)
        for i in range(segment["start"], segment["stop"] + ONE)
    } | {
        (i, segment["col"] + ONE, x0)
        for i in range(segment["start"], segment["stop"] + ONE)
    }


def entry_opening_9bbf930d(
    segment: dict,
) -> IntegerTuple:
    if segment["axis"] == "h":
        return (segment["row"], segment["start"] - ONE)
    if segment["direction"] == UP:
        return (segment["stop"] + ONE, segment["col"])
    return (segment["start"] - ONE, segment["col"])


def exit_opening_9bbf930d(
    segment: dict,
) -> IntegerTuple:
    if segment["axis"] == "h":
        return (segment["row"], segment["stop"] + ONE)
    if segment["direction"] == UP:
        return (segment["start"] - ONE, segment["col"])
    return (segment["stop"] + ONE, segment["col"])


def exit_direction_9bbf930d(
    segment: dict,
) -> IntegerTuple:
    if segment["axis"] == "h":
        return RIGHT
    return segment["direction"]


def path_endpoint_9bbf930d(
    path: dict,
    shape_: IntegerTuple,
) -> IntegerTuple:
    h, w = shape_
    x0 = path["segments"][-ONE]
    x1 = exit_opening_9bbf930d(x0)
    x2 = exit_direction_9bbf930d(x0)
    x3 = path.get("blocker")
    if x3 is not None:
        while add(x1, x2) != x3:
            x1 = add(x1, x2)
        return x1
    while True:
        x4 = add(x1, x2)
        if not (ZERO <= x4[ZERO] < h and ZERO <= x4[ONE] < w):
            return x1
        x1 = x4


def path_clear_cells_9bbf930d(
    path: dict,
    shape_: IntegerTuple,
) -> set[IntegerTuple]:
    h, w = shape_
    x0 = path["segments"]
    x1 = entry_opening_9bbf930d(x0[ZERO])[ONE]
    x2 = {(path["row"], j) for j in range(ONE, x1 + ONE)}
    for x3 in x0:
        x2 |= segment_cells_9bbf930d(x3)
        x2 |= segment_openings_9bbf930d(x3)
    x4 = exit_opening_9bbf930d(x0[-ONE])
    x5 = exit_direction_9bbf930d(x0[-ONE])
    x6 = path.get("blocker")
    while ZERO <= x4[ZERO] < h and ZERO <= x4[ONE] < w:
        x2.add(x4)
        x7 = add(x4, x5)
        if x6 is not None and x7 == x6:
            return x2
        if not (ZERO <= x7[ZERO] < h and ZERO <= x7[ONE] < w):
            return x2
        x4 = x7
    return x2


def path_wall_cells_9bbf930d(
    path: dict,
) -> set[tuple[Integer, Integer, Integer]]:
    x0 = set()
    for x1 in path["segments"]:
        x0 |= segment_walls_9bbf930d(x1)
    x2 = path.get("blocker")
    if x2 is not None:
        x0.add((x2[ZERO], x2[ONE], path["blocker_color"]))
    return x0
