from arc2.core import *

from .helpers import (
    compose_output_9f669b64,
    rect_patch_9f669b64,
    solve_9f669b64,
    taper_patch_9f669b64,
    tee_patch_9f669b64,
)


BG_9F669B64 = 7


def _paint_family_9f669b64(
    destination_patch: Indices,
    mover_patch: Indices,
    static_patch: Indices,
    destination_color: Integer,
    mover_color: Integer,
    static_color: Integer,
) -> dict:
    dims = (10, 10)
    destination = recolor(destination_color, destination_patch)
    mover = recolor(mover_color, mover_patch)
    static = recolor(static_color, static_patch)
    gi = canvas(BG_9F669B64, dims)
    gi = paint(gi, destination)
    gi = paint(gi, mover)
    gi = paint(gi, static)
    go = compose_output_9f669b64(destination, mover, static, dims, BG_9F669B64)
    return {"input": gi, "output": go}


def _rect_stack_family_9f669b64(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    width_value = choice((4, 6))
    left = unifint(diff_lb, diff_ub, (1, 10 - width_value - 1))
    top_destination = choice((2, 6))
    destination_patch = rect_patch_9f669b64(top_destination, left, 2, width_value)
    mover_left = left + width_value // 2 - 1
    if top_destination <= 2:
        mover_top = top_destination + 2
        static_top = mover_top + 2
    else:
        static_top = max(0, top_destination - 6)
        mover_top = static_top + 4
    mover_patch = rect_patch_9f669b64(mover_top, mover_left, 2, 2)
    static_patch = rect_patch_9f669b64(static_top, mover_left, 4, 2)
    colors = tuple(sorted(sample(remove(BG_9F669B64, interval(0, 10, 1)), 3)))
    return _paint_family_9f669b64(
        destination_patch,
        mover_patch,
        static_patch,
        last(colors),
        first(colors),
        colors[1],
    )


def _tee_stack_family_9f669b64(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    width_value = choice((4, 6))
    left = unifint(diff_lb, diff_ub, (1, 10 - width_value - 1))
    mover_height = choice((2, 3))
    top_destination = choice((0, 6))
    destination_patch = rect_patch_9f669b64(top_destination, left, 4, width_value)
    mover_left = left + width_value // 2 - 1
    if top_destination == 0:
        mover_top = 4
        static_top = mover_top + mover_height
    else:
        mover_top = top_destination - mover_height
        static_top = mover_top - 3
    mover_patch = rect_patch_9f669b64(mover_top, mover_left, mover_height, 2)
    static_patch = tee_patch_9f669b64(static_top, mover_left - (width_value // 2 - 1), width_value)
    colors = tuple(sample(remove(BG_9F669B64, interval(0, 10, 1)), 3))
    return _paint_family_9f669b64(
        destination_patch,
        mover_patch,
        static_patch,
        colors[0],
        colors[1],
        colors[2],
    )


def _wedge_family_9f669b64(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    height_value = choice((4, 6))
    width_value = choice((1, 2))
    wedge_width = choice((2, 4))
    top_choices = (1, 3) if height_value == 4 else (2,)
    top_destination = choice(top_choices)
    destination_on_right = choice((True, False))
    mover_top = top_destination + height_value // 2 - 1
    if destination_on_right:
        destination_left = 8
        mover_left = wedge_width
        wedge_left = 0
        wedge_point_side = "left"
    else:
        destination_left = 1
        mover_left = 8 - wedge_width
        wedge_left = 10 - wedge_width
        wedge_point_side = "right"
    mover_patch = rect_patch_9f669b64(mover_top, mover_left, 2, 2)
    destination_patch = rect_patch_9f669b64(top_destination, destination_left, height_value, width_value)
    wedge_top = mover_top - 2
    static_patch = taper_patch_9f669b64(wedge_top, wedge_left, wedge_width, wedge_point_side)
    colors = tuple(sample(remove(BG_9F669B64, interval(0, 10, 1)), 3))
    return _paint_family_9f669b64(
        destination_patch,
        mover_patch,
        static_patch,
        colors[0],
        colors[1],
        colors[2],
    )


def generate_9f669b64(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    families = (
        _rect_stack_family_9f669b64,
        _tee_stack_family_9f669b64,
        _wedge_family_9f669b64,
    )
    while True:
        example = choice(families)(diff_lb, diff_ub)
        if example["input"] == example["output"]:
            continue
        if solve_9f669b64(example["input"]) != example["output"]:
            continue
        return example
