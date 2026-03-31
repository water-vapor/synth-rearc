from __future__ import annotations

from synth_rearc.core import *

from .helpers import ORIENTATION_POOL_B9E38DC0
from .helpers import _rotate_grid_b9e38dc0
from .helpers import format_grid_b9e38dc0
from .helpers import mutable_canvas_b9e38dc0
from .helpers import normalize_projector_b9e38dc0
from .helpers import paint_cells_b9e38dc0
from .helpers import project_beam_b9e38dc0


def _other_colors_b9e38dc0(
    bg: Integer,
) -> tuple[Integer, ...]:
    return tuple(x0 for x0 in interval(ZERO, TEN, ONE) if x0 != bg)


def _sample_seed_b9e38dc0(
    grid: list[list[Integer]],
    fill_color: Integer,
    bar_row: Integer,
    left_bound: Integer,
    right_bound: Integer,
    body_depth: Integer,
) -> None:
    x0 = len(grid)
    x1 = len(grid[ZERO])
    x2 = randint(add(bar_row, ONE), min(add(bar_row, THREE), add(bar_row, body_depth)))
    x3 = divide(add(left_bound, right_bound), TWO)
    x4 = choice(("dot", "dot", "bar", "el"))
    x5 = {(x2, x3)}
    if x4 == "bar":
        if both(x3 > ZERO, x3 < subtract(x1, ONE)):
            x5 = {(x2, subtract(x3, ONE)), (x2, x3), (x2, add(x3, ONE))}
    elif x4 == "el":
        if both(x2 < subtract(x0, ONE), x3 > ZERO):
            x5 = {(x2, x3), (add(x2, ONE), x3), (add(x2, ONE), subtract(x3, ONE))}
    x6 = {
        x7
        for x7 in x5
        if both(
            both(ZERO <= x7[ZERO] < x0, ZERO <= x7[ONE] < x1),
            grid[x7[ZERO]][x7[ONE]] != fill_color,
        )
    }
    x8 = {
        x9
        for x9 in x6
        if grid[x9[ZERO]][x9[ONE]] == mostcolor(format_grid_b9e38dc0(grid))
    }
    if len(x8) == ZERO:
        x8 = {(x2, x3)}
    paint_cells_b9e38dc0(grid, fill_color, x8)


def _random_walk_body_b9e38dc0(
    grid: list[list[Integer]],
    wall_color: Integer,
    bar_row: Integer,
    bar_left: Integer,
    bar_right: Integer,
    body_depth: Integer,
) -> None:
    x0 = len(grid[ZERO])
    x1 = subtract(bar_left, ONE) if bar_left > ZERO else None
    x2 = add(bar_right, ONE) if bar_right < subtract(x0, ONE) else None
    x3 = x1
    x4 = x2
    for x5 in range(add(bar_row, ONE), add(add(bar_row, body_depth), ONE)):
        if x3 is not None:
            x3 = min(subtract(x0, TWO), max(ZERO, add(x3, choice((-1, ZERO, ZERO, ONE)))))
        if x4 is not None:
            x4 = max(ONE, min(subtract(x0, ONE), add(x4, choice((-1, ZERO, ZERO, ONE)))))
        if both(x3 is not None, x4 is not None):
            if x3 >= x4:
                x3 = max(ZERO, subtract(x4, TWO))
        if x3 is not None:
            paint_cells_b9e38dc0(grid, wall_color, {(x5, x3)})
        if x4 is not None:
            paint_cells_b9e38dc0(grid, wall_color, {(x5, x4)})
        if both(x4 is not None, randint(ZERO, THREE) == ZERO):
            for x6 in range(ONE, randint(TWO, THREE)):
                x7 = subtract(x4, x6)
                if x3 is not None and x7 <= x3:
                    break
                paint_cells_b9e38dc0(grid, wall_color, {(x5, x7)})
        if both(x3 is not None, randint(ZERO, FIVE) == ZERO):
            for x6 in range(ONE, randint(TWO, THREE)):
                x7 = add(x3, x6)
                if x4 is not None and x7 >= x4:
                    break
                paint_cells_b9e38dc0(grid, wall_color, {(x5, x7)})


def _fill_rows_b9e38dc0(
    grid: Grid,
    fill_color: Integer,
) -> tuple[tuple[IntegerTuple, ...], ...]:
    x0 = []
    for x1, x2 in enumerate(grid):
        x3 = tuple((x1, x4) for x4, x5 in enumerate(x2) if x5 == fill_color)
        x0.append(x3)
    return tuple(x0)


def _add_beam_obstacles_b9e38dc0(
    grid: list[list[Integer]],
    output_grid: Grid,
    bg: Integer,
    fill_color: Integer,
    extra_colors: tuple[Integer, ...],
    start_row: Integer,
) -> None:
    x0 = len(grid)
    x1 = len(grid[ZERO])
    x2 = _fill_rows_b9e38dc0(output_grid, fill_color)
    x3 = list(range(start_row, subtract(x0, ONE)))
    shuffle(x3)
    x4 = min(randint(ZERO, THREE), len(x3))
    for x5 in x3[:x4]:
        x6 = [x7[ONE] for x7 in x2[x5] if grid[x5][x7[ONE]] == bg]
        if len(x6) == ZERO:
            continue
        x8 = choice(extra_colors)
        x9 = choice(x6)
        x10 = choice((ONE, ONE, ONE, TWO))
        x11 = {(x5, x9)}
        if both(equality(x10, TWO), both(add(x9, ONE) < x1, (x5, add(x9, ONE)) in x2[x5])):
            if grid[x5][add(x9, ONE)] == bg:
                x11.add((x5, add(x9, ONE)))
        paint_cells_b9e38dc0(grid, x8, x11)


def _add_off_beam_distractors_b9e38dc0(
    grid: list[list[Integer]],
    output_grid: Grid,
    bg: Integer,
    fill_color: Integer,
    extra_colors: tuple[Integer, ...],
    bar_row: Integer,
) -> None:
    x0 = len(grid)
    x1 = len(grid[ZERO])
    x2 = {
        (x3, x4)
        for x3, x5 in enumerate(output_grid)
        for x4, x6 in enumerate(x5)
        if x6 == fill_color
    }
    for _ in range(randint(ZERO, TWO)):
        x3 = randint(add(bar_row, THREE), subtract(x0, ONE))
        x4 = randint(ZERO, subtract(x1, ONE))
        if grid[x3][x4] != bg:
            continue
        if (x3, x4) in x2:
            continue
        x5 = choice(extra_colors)
        paint_cells_b9e38dc0(grid, x5, {(x3, x4)})


def _sample_normalized_b9e38dc0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (12, 20))
        x1 = unifint(diff_lb, diff_ub, (10, 18))
        x2 = choice(interval(ZERO, TEN, ONE))
        x3 = list(_other_colors_b9e38dc0(x2))
        shuffle(x3)
        x4 = x3[ZERO]
        x5 = x3[ONE]
        x6 = tuple(x3[TWO:])
        x7 = min(SEVEN, subtract(x1, TWO))
        x8 = randint(THREE, x7)
        x9 = choice(("free", "free", "left", "right"))
        if both(x9 == "left", x8 < x1):
            x10 = ZERO
        elif both(x9 == "right", x8 < x1):
            x10 = subtract(x1, x8)
        else:
            x10 = randint(branch(x1 - x8 > TWO, ONE, ZERO), subtract(subtract(x1, x8), branch(x1 - x8 > TWO, ONE, ZERO)))
        x11 = subtract(add(x10, x8), ONE)
        x12 = randint(ONE, min(FOUR, divide(x0, FOUR)))
        x13 = min(subtract(subtract(x0, x12), FOUR), unifint(diff_lb, diff_ub, (FOUR, NINE)))
        if x13 < THREE:
            continue
        x14 = mutable_canvas_b9e38dc0(x2, (x0, x1))
        paint_cells_b9e38dc0(x14, x4, {(x12, x15) for x15 in range(x10, add(x11, ONE))})
        _random_walk_body_b9e38dc0(x14, x4, x12, x10, x11, x13)
        _sample_seed_b9e38dc0(x14, x5, x12, x10, x11, x13)
        x16 = format_grid_b9e38dc0(x14)
        x17 = project_beam_b9e38dc0(x16)
        _add_beam_obstacles_b9e38dc0(x14, x17, x2, x5, x6, add(add(x12, x13), ONE))
        x18 = format_grid_b9e38dc0(x14)
        x19 = project_beam_b9e38dc0(x18)
        _add_off_beam_distractors_b9e38dc0(x14, x19, x2, x5, x6, x12)
        x20 = format_grid_b9e38dc0(x14)
        x21 = project_beam_b9e38dc0(x20)
        x22 = sum(
            ONE
            for x23, x24 in zip(x20, x21)
            for x25, x26 in zip(x23, x24)
            if x25 != x26
        )
        if x22 < 8:
            continue
        x27 = sum(ONE for x28 in x20 for x29 in x28 if x29 == x4)
        x30 = sum(ONE for x31 in x20 for x32 in x31 if x32 == x5)
        if x27 <= x30:
            continue
        x31 = normalize_projector_b9e38dc0(x20)
        if x31["turns"] != ZERO:
            continue
        return {"input": x20, "output": x21}


def generate_b9e38dc0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = _sample_normalized_b9e38dc0(diff_lb, diff_ub)
    x1 = choice(ORIENTATION_POOL_B9E38DC0)
    x2 = _rotate_grid_b9e38dc0(x0["input"], x1)
    x3 = project_beam_b9e38dc0(x2)
    return {"input": x2, "output": x3}
