from synth_rearc.core import *

from .helpers import (
    ACTIVE_COLORS_9BBF930D,
    entry_opening_9bbf930d,
    exit_direction_9bbf930d,
    exit_opening_9bbf930d,
    horizontal_segment_9bbf930d,
    path_clear_cells_9bbf930d,
    path_endpoint_9bbf930d,
    path_wall_cells_9bbf930d,
    trace_launcher_9bbf930d,
    tunnel_maps_9bbf930d,
    vertical_segment_9bbf930d,
)
from .verifier import verify_9bbf930d


def _wall_index_9bbf930d(
    walls: set[tuple[Integer, Integer, Integer]],
) -> set[IntegerTuple]:
    return {(i, j) for i, j, _ in walls}


def _sample_rows_9bbf930d(
    h: Integer,
    n_rows: Integer,
) -> list[Integer]:
    x0 = list(range(ONE, h - ONE, TWO))
    shuffle(x0)
    x1 = []
    for x2 in sorted(x0):
        if all(abs(x2 - x3) >= FOUR for x3 in x1):
            x1.append(x2)
    shuffle(x1)
    return sorted(x1[:n_rows])


def _make_path_9bbf930d(
    row: Integer,
    color_: Integer,
    shape_: IntegerTuple,
) -> dict:
    h, w = shape_
    x0 = randint(TWO, min(FOUR, w - EIGHT))
    x1 = randint(x0 + FOUR, w - FIVE)
    x2 = [horizontal_segment_9bbf930d(row, x0, x1, color_)]
    if uniform(ZERO, ONE) < 0.6:
        x3 = x1 + ONE
        x4 = []
        if row >= FOUR:
            x4.append(UP)
        if row <= h - FIVE:
            x4.append(DOWN)
        if len(x4) > ZERO:
            x5 = choice(x4)
            if x5 == UP:
                x6 = randint(ONE, row - TWO)
                x2.append(vertical_segment_9bbf930d(x3, x6, row - ONE, UP, color_))
            else:
                x7 = randint(row + ONE, h - TWO)
                x2.append(vertical_segment_9bbf930d(x3, row + ONE, x7, DOWN, color_))
    x8 = {"row": row, "color": color_, "segments": x2}
    if uniform(ZERO, ONE) < 0.4:
        x9 = exit_opening_9bbf930d(x2[-ONE])
        x10 = exit_direction_9bbf930d(x2[-ONE])
        x11 = []
        x12 = x9
        while True:
            x13 = add(x12, x10)
            x14 = add(x13, x10)
            if not (ZERO <= x14[ZERO] < h and ZERO <= x14[ONE] < w):
                break
            x11.append(x13)
            x12 = x13
        if len(x11) >= TWO:
            x8["blocker"] = choice(x11[:-ONE])
            x8["blocker_color"] = choice(
                tuple(x15 for x15 in ACTIVE_COLORS_9BBF930D if x15 != color_)
            )
    return x8


def _valid_path_9bbf930d(
    path: dict,
    shape_: IntegerTuple,
    reserved_clear: set[IntegerTuple],
    reserved_walls: set[tuple[Integer, Integer, Integer]],
) -> Boolean:
    h, w = shape_
    x0 = path_clear_cells_9bbf930d(path, shape_)
    x1 = path_wall_cells_9bbf930d(path)
    x2 = _wall_index_9bbf930d(reserved_walls)
    if any(not (ZERO <= i < h and ZERO <= j < w) for i, j in x0):
        return False
    if any(not (ZERO <= i < h and ZERO <= j < w) or j == ZERO for i, j, _ in x1):
        return False
    if len(x0 & reserved_clear) > ZERO:
        return False
    if any((i, j) in reserved_clear for i, j, _ in x1):
        return False
    if any((i, j) in x2 for i, j in x0):
        return False
    for x3, x4, x5 in x1:
        for x6, x7, x8 in reserved_walls:
            if (x3, x4) == (x6, x7) and x5 != x8:
                return False
    return True


def _single_bar_9bbf930d(
    shape_: IntegerTuple,
    paths: tuple[dict, ...],
    reserved_clear: set[IntegerTuple],
    reserved_walls: set[tuple[Integer, Integer, Integer]],
    color_: Integer,
) -> set[tuple[Integer, Integer, Integer]]:
    h, w = shape_
    x0 = {x1["row"] for x1 in paths}
    for _ in range(100):
        if uniform(ZERO, ONE) < 0.5:
            x2 = choice(tuple(i for i in range(ONE, h - ONE) if i not in x0))
            x3 = randint(TWO, w - SIX)
            x4 = randint(x3 + THREE, w - TWO)
            x5 = {(x2, j, color_) for j in range(x3, x4 + ONE)}
        else:
            x6 = randint(TWO, w - TWO)
            x7 = randint(ONE, h - SIX)
            x8 = randint(x7 + THREE, h - TWO)
            x5 = {(i, x6, color_) for i in range(x7, x8 + ONE)}
        if any((i, j) in reserved_clear for i, j, _ in x5):
            continue
        if any((i, j) in _wall_index_9bbf930d(reserved_walls) for i, j, _ in x5):
            continue
        return x5
    return set()


def generate_9bbf930d(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = unifint(diff_lb, diff_ub, (15, 24))
        w = unifint(diff_lb, diff_ub, (15, 24))
        x0 = min((h - ONE) // FOUR, unifint(diff_lb, diff_ub, (THREE, FIVE)))
        if x0 < TWO:
            continue
        x1 = _sample_rows_9bbf930d(h, x0)
        if len(x1) < TWO:
            continue
        x2 = sample(ACTIVE_COLORS_9BBF930D, len(x1))
        x3 = (h, w)
        x4 = {(i, ZERO) for i in range(h)}
        x5 = set()
        x6 = []
        x7 = True
        for x8, x9 in zip(x1, x2):
            x10 = False
            for _ in range(100):
                x11 = _make_path_9bbf930d(x8, x9, x3)
                if not _valid_path_9bbf930d(x11, x3, x4, x5):
                    continue
                x6.append(x11)
                x4 |= path_clear_cells_9bbf930d(x11, x3)
                x5 |= path_wall_cells_9bbf930d(x11)
                x10 = True
                break
            if not x10:
                x7 = False
                break
        if not x7 or len(x6) < TWO:
            continue
        x12 = tuple(x6)
        x13 = tuple(x14 for x14 in ACTIVE_COLORS_9BBF930D if x14 not in x2)
        shuffle(x15 := list(x13))
        for x16 in x15[: randint(ONE, min(TWO, len(x15))) if len(x15) > ZERO else ZERO]:
            x17 = _single_bar_9bbf930d(x3, x12, x4, x5, x16)
            if len(x17) == ZERO:
                continue
            x5 |= x17
        x18 = [list(x19) for x19 in canvas(SEVEN, x3)]
        for i in range(h):
            x18[i][ZERO] = SIX
        for i, j, x20 in x5:
            x18[i][j] = x20
        x21 = tuple(tuple(x22) for x22 in x18)
        x23, x24 = tunnel_maps_9bbf930d(x21)
        x25 = [
            x26
            for x26 in range(h)
            if trace_launcher_9bbf930d(x21, x26, x23, x24) != (x26, ZERO)
        ]
        if x25 != x1:
            continue
        x27 = [list(x28) for x28 in x21]
        for x29 in x1:
            x27[x29][ZERO] = SEVEN
        for x30 in x12:
            x31 = path_endpoint_9bbf930d(x30, x3)
            x27[x31[ZERO]][x31[ONE]] = SIX
        x32 = tuple(tuple(x33) for x33 in x27)
        if verify_9bbf930d(x21) != x32:
            continue
        return {"input": x21, "output": x32}
