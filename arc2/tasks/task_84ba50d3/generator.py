from arc2.core import *

from .helpers import (
    make_bar_stem_patch_84ba50d3,
    make_line_patch_84ba50d3,
    place_patch_84ba50d3,
)
from .verifier import verify_84ba50d3


def _sample_line_spec_84ba50d3(
    bar_row: Integer,
    grid_size: Integer,
) -> dict[str, Integer] | None:
    x0 = min(bar_row, subtract(subtract(grid_size, bar_row), ONE))
    if x0 < ONE:
        return None
    x1 = randint(ONE, min(SEVEN, x0))
    return {
        "kind": "line",
        "patch": make_line_patch_84ba50d3(x1),
        "width": ONE,
        "height": x1,
    }


def _sample_bar_stem_spec_84ba50d3(
    bar_row: Integer,
    grid_size: Integer,
) -> dict[str, Integer] | None:
    x0 = min(FOUR, max(TWO, min(FIVE, grid_size - ONE)))
    x1 = tuple(x2 for x2 in (TWO, TWO, THREE, THREE, FOUR) if x2 <= x0)
    if len(x1) == ZERO:
        return None
    x2 = choice(x1)
    x3 = min(FOUR, decrement(bar_row))
    x4 = min(FOUR, subtract(grid_size, bar_row))
    x5 = ["flat"]
    if x3 >= ONE:
        x5.extend(["up", "up", "up"])
    if x4 >= ONE:
        x5.extend(["down", "down", "down"])
    if both(greater(x3, ZERO), greater(x4, ZERO)):
        x5.extend(["both", "both"])
    x6 = choice(tuple(x5))
    if x6 == "flat":
        x7 = ZERO
        x8 = ZERO
    elif x6 == "up":
        x7 = randint(ONE, x3)
        x8 = ZERO
    elif x6 == "down":
        x7 = ZERO
        x8 = randint(ONE, x4)
    else:
        x7 = randint(ONE, x3)
        x8 = randint(ONE, x4)
    x9 = add(add(x7, x8), ONE)
    if x9 > bar_row:
        return None
    x10 = randint(ZERO, decrement(x2))
    return {
        "kind": "wide",
        "patch": make_bar_stem_patch_84ba50d3(x2, x7, x8, x10),
        "width": x2,
        "height": x9,
        "anchor": x7,
    }


def _sample_specs_84ba50d3(
    diff_lb: float,
    diff_ub: float,
    bar_row: Integer,
    grid_size: Integer,
) -> tuple[dict[str, object], ...]:
    x0 = min(FIVE, max(ONE, divide(grid_size, THREE)))
    while True:
        x1 = unifint(diff_lb, diff_ub, (ONE, x0))
        x2: list[dict[str, object]] = []
        x3 = ZERO
        x4 = F
        for _ in range(x1):
            x5 = choice(("wide", "wide", "wide", "line", "line"))
            if equality(x5, "line"):
                x6 = _sample_line_spec_84ba50d3(bar_row, grid_size)
            else:
                x6 = _sample_bar_stem_spec_84ba50d3(bar_row, grid_size)
            if x6 is None:
                x4 = T
                break
            x2.append(x6)
            x3 = add(x3, x6["width"])
        if x4:
            continue
        if add(x3, decrement(x1)) > grid_size:
            continue
        return tuple(x2)


def _sample_lefts_84ba50d3(
    specs: tuple[dict[str, object], ...],
    grid_size: Integer,
) -> tuple[Integer, ...]:
    x0 = len(specs)
    x1 = sum(x2["width"] for x2 in specs)
    x2 = subtract(subtract(grid_size, x1), decrement(x0))
    x3 = randint(ZERO, x2)
    x4 = [ZERO] * add(x0, ONE)
    for _ in range(x3):
        x5 = randint(ZERO, x0)
        x4[x5] = increment(x4[x5])
    x6 = tuple(spec["width"] for spec in specs)
    x7 = []
    x8 = x4[ZERO]
    for x9, x10 in enumerate(x6):
        x7.append(x8)
        x11 = branch(equality(x9, decrement(x0)), ZERO, ONE)
        x8 = add(add(add(x8, x10), x11), x4[increment(x9)])
    return tuple(x7)


def generate_84ba50d3(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (SEVEN, 18))
        x1 = (x0, x0)
        x2 = max(THREE, subtract(divide(x0, TWO), ONE))
        x3 = min(subtract(x0, FOUR), add(divide(x0, TWO), TWO))
        x4 = randint(x2, x3)
        x5 = _sample_specs_84ba50d3(diff_lb, diff_ub, x4, x0)
        x6 = list(x5)
        shuffle(x6)
        x7 = tuple(x6)
        x8 = _sample_lefts_84ba50d3(x7, x0)
        x9 = canvas(EIGHT, x1)
        x10 = fill(x9, TWO, connect((x4, ZERO), (x4, decrement(x0))))
        x11 = x10
        x12 = x10
        for x13, x14 in zip(x7, x8):
            x15 = x13["height"]
            x16 = randint(ZERO, subtract(x4, x15))
            x17 = place_patch_84ba50d3(x13["patch"], x16, x14)
            x11 = paint(x11, x17)
            if equality(x13["kind"], "line"):
                x18 = subtract(x0, x15)
                x19 = frozenset((x4, x20) for x20 in range(x14, add(x14, x13["width"])))
                x12 = fill(x12, EIGHT, x19)
            else:
                x18 = subtract(decrement(x4), x13["anchor"])
            x21 = shift(x17, toivec(subtract(x18, x16)))
            x12 = paint(x12, x21)
        x22 = colorfilter(objects(x11, T, F, T), ONE)
        if flip(equality(len(x22), len(x7))):
            continue
        if verify_84ba50d3(x11) != x12:
            continue
        return {"input": x11, "output": x12}
