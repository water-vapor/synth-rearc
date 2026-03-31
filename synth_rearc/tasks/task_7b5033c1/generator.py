from __future__ import annotations

from synth_rearc.core import *

from .helpers import build_monotone_path_7b5033c1
from .helpers import render_output_7b5033c1
from .helpers import touching_cells_7b5033c1
from .verifier import verify_7b5033c1


GRID_SIZE_7B5033C1 = 16
OBJECT_COUNT_OPTIONS_7B5033C1 = (THREE, FOUR, FOUR, FIVE, FIVE, SIX)
SIZE_OPTIONS_7B5033C1 = (TWO, THREE, THREE, FOUR, FOUR, FIVE, FIVE, SIX, SIX, SEVEN, EIGHT)
NEXT_START_STEPS_7B5033C1 = (DOWN, DOWN, DOWN, RIGHT, RIGHT)


def _in_bounds_7b5033c1(
    loc: IntegerTuple,
) -> Boolean:
    i, j = loc
    return ZERO <= i < GRID_SIZE_7B5033C1 and ZERO <= j < GRID_SIZE_7B5033C1


def _choose_color_7b5033c1(
    bg: Integer,
    previous: Integer | None,
) -> Integer:
    x0 = [x1 for x1 in range(TEN) if x1 != bg and x1 != previous]
    return choice(tuple(x0))


def _sample_end_7b5033c1(
    start: IntegerTuple,
) -> IntegerTuple | None:
    x0 = choice(SIZE_OPTIONS_7B5033C1)
    x1 = subtract(x0, ONE)
    x2 = [x3 for x3 in range(min(FOUR, x1), NEG_ONE, NEG_ONE) if subtract(x1, x3) <= FOUR]
    x3 = [x4 for x4 in x2 if x4 > ZERO]
    if len(x3) > ZERO and choice((T, T, T, F)):
        x2 = x3
    x4 = choice(tuple(x2))
    x5 = subtract(x1, x4)
    x6 = []
    if x5 == ZERO:
        x6.append(ZERO)
    else:
        if add(start[ONE], x5) < GRID_SIZE_7B5033C1:
            x6.append(x5)
        if subtract(start[ONE], x5) >= ZERO:
            x6.append(invert(x5))
    if len(x6) == ZERO:
        return None
    x7 = choice(tuple(x6))
    x8 = add(start[ZERO], x4)
    x9 = add(start[ONE], x7)
    if x8 >= GRID_SIZE_7B5033C1:
        return None
    return (x8, x9)


def _next_start_options_7b5033c1(
    end: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    x0 = []
    for x1 in NEXT_START_STEPS_7B5033C1:
        x2 = (add(end[ZERO], x1[ZERO]), add(end[ONE], x1[ONE]))
        if _in_bounds_7b5033c1(x2):
            x0.append(x2)
    return tuple(x0)


def _path_is_valid_7b5033c1(
    patch: Indices,
    placed: tuple[Object, ...],
    start: IntegerTuple,
) -> Boolean:
    x0 = tuple(x1 for x1 in placed if len(intersection(patch, toindices(x1))) > ZERO)
    if len(x0) > ZERO:
        return False
    x2 = tuple(x3 for x3 in placed if adjacent(patch, x3))
    if len(placed) == ZERO:
        return len(x2) == ZERO
    if x2 != (placed[-1],):
        return False
    x4 = touching_cells_7b5033c1(patch, placed[-1])
    return x4 == initset(start)


def _choose_next_start_7b5033c1(
    end: IntegerTuple,
    patch: Indices,
    placed: tuple[Object, ...],
) -> IntegerTuple | None:
    x0 = list(_next_start_options_7b5033c1(end))
    shuffle(x0)
    for x1 in x0:
        if x1 in patch:
            continue
        if any(x1 in toindices(x2) for x2 in placed):
            continue
        return x1
    return None


def generate_7b5033c1(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = randint(ZERO, NINE)
        x1 = choice(OBJECT_COUNT_OPTIONS_7B5033C1)
        x2 = (randint(ONE, THREE), randint(ONE, FIVE))
        x3: list[Object] = []
        x4: list[Integer] = []
        x5 = x2
        x6 = False
        for x7 in range(x1):
            x8 = None
            for _ in range(200):
                x9 = _sample_end_7b5033c1(x5)
                if x9 is None:
                    continue
                x10 = build_monotone_path_7b5033c1(x5, x9)
                x11 = tuple(x3)
                if not _path_is_valid_7b5033c1(x10, x11, x5):
                    continue
                x12 = None
                if x7 < decrement(x1):
                    x12 = _choose_next_start_7b5033c1(x9, x10, x11)
                    if x12 is None:
                        continue
                x13 = _choose_color_7b5033c1(x0, x4[-1] if len(x4) > ZERO else None)
                x8 = (recolor(x13, x10), x13, x12)
                break
            if x8 is None:
                x6 = True
                break
            x14, x15, x16 = x8
            x3.append(x14)
            x4.append(x15)
            if x16 is not None:
                x5 = x16
        if x6:
            continue
        x17 = canvas(x0, (GRID_SIZE_7B5033C1, GRID_SIZE_7B5033C1))
        for x18 in x3:
            x17 = paint(x17, x18)
        x19 = render_output_7b5033c1(tuple(x3))
        x20 = height(x19)
        if x20 < 15 or x20 > 28:
            continue
        if verify_7b5033c1(x17) != x19:
            continue
        return {"input": x17, "output": x19}
