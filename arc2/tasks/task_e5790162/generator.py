from functools import lru_cache

from arc2.core import *


def _edge_distance_e5790162(
    location: IntegerTuple,
    direction: IntegerTuple,
    shape_: IntegerTuple,
) -> Integer:
    i, j = location
    h, w = shape_
    if direction == RIGHT:
        return w - ONE - j
    if direction == LEFT:
        return j
    if direction == DOWN:
        return h - ONE - i
    return i


def _edge_endpoint_e5790162(
    location: IntegerTuple,
    direction: IntegerTuple,
    shape_: IntegerTuple,
) -> IntegerTuple:
    i, j = location
    h, w = shape_
    if direction == RIGHT:
        return (i, w - ONE)
    if direction == LEFT:
        return (i, ZERO)
    if direction == DOWN:
        return (h - ONE, j)
    return (ZERO, j)


def _marker_options_e5790162(
    location: IntegerTuple,
    direction: IntegerTuple,
    shape_: IntegerTuple,
) -> tuple[tuple[IntegerTuple, Integer, IntegerTuple, IntegerTuple], ...]:
    i, j = location
    h, w = shape_
    options = []
    steps = interval(THREE, SIX, ONE)
    if direction == RIGHT:
        for step in steps:
            marker_col = j + step
            if marker_col >= w:
                continue
            endpoint = (i, marker_col - ONE)
            if i > ZERO:
                options.append(((i, marker_col), EIGHT, endpoint, UP))
            if i < h - ONE:
                options.append(((i, marker_col), SIX, endpoint, DOWN))
    elif direction == UP:
        for step in steps:
            marker_row = i - step
            if marker_row < ZERO:
                continue
            endpoint = (marker_row + ONE, j)
            options.append(((marker_row, j), SIX, endpoint, RIGHT))
    else:
        for step in steps:
            marker_row = i + step
            if marker_row >= h:
                continue
            endpoint = (marker_row - ONE, j)
            options.append(((marker_row, j), EIGHT, endpoint, RIGHT))
    return tuple(options)


@lru_cache(maxsize=None)
def _can_finish_e5790162(
    location: IntegerTuple,
    direction: IntegerTuple,
    remaining_markers: Integer,
    shape_: IntegerTuple,
) -> Boolean:
    if remaining_markers == ZERO:
        return _edge_distance_e5790162(location, direction, shape_) >= ONE
    x0 = _marker_options_e5790162(location, direction, shape_)
    return any(
        _can_finish_e5790162(endpoint, next_direction, remaining_markers - ONE, shape_)
        for _, _, endpoint, next_direction in x0
    )


def _max_markers_e5790162(
    location: IntegerTuple,
    shape_: IntegerTuple,
) -> Integer:
    for remaining_markers in range(SIX, ZERO, NEG_ONE):
        if _can_finish_e5790162(location, RIGHT, remaining_markers, shape_):
            return remaining_markers
    return ZERO


def generate_e5790162(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = unifint(diff_lb, diff_ub, (SIX, TEN))
        w = unifint(diff_lb, diff_ub, (SIX, 12))
        start = (randint(ONE, h - TWO), ZERO)
        shape_ = (h, w)
        max_markers = _max_markers_e5790162(start, shape_)
        if max_markers == ZERO:
            continue
        n_markers = unifint(diff_lb, diff_ub, (ONE, max_markers))
        if not _can_finish_e5790162(start, RIGHT, n_markers, shape_):
            continue
        gi = fill(canvas(ZERO, shape_), THREE, {start})
        go = gi
        x0 = start
        x1 = RIGHT
        x2 = n_markers
        while x2 > ZERO:
            x3 = _marker_options_e5790162(x0, x1, shape_)
            x4 = tuple(
                option
                for option in x3
                if _can_finish_e5790162(option[TWO], option[THREE], x2 - ONE, shape_)
            )
            if len(x4) == ZERO:
                break
            x5, x6, x7, x8 = choice(x4)
            gi = fill(gi, x6, {x5})
            go = fill(go, x6, {x5})
            go = fill(go, THREE, connect(x0, x7))
            x0 = x7
            x1 = x8
            x2 = x2 - ONE
        if x2 != ZERO:
            continue
        x9 = _edge_endpoint_e5790162(x0, x1, shape_)
        go = fill(go, THREE, connect(x0, x9))
        return {"input": gi, "output": go}
