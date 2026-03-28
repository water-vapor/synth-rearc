from synth_rearc.core import *

from .verifier import verify_72207abc


WIDTH_OPTIONS_72207ABC = (19, 19, 29)
SEED_COUNT_OPTIONS_72207ABC = (TWO, TWO, THREE)
COLOR_POOL_72207ABC = remove(ZERO, interval(ZERO, TEN, ONE))


def _seed_positions_72207abc(
    seed_count: int,
) -> tuple[int, ...]:
    if seed_count == TWO:
        return (ZERO, ONE)
    return (ZERO, ONE, THREE)


def _render_row_72207abc(
    colors: tuple[int, ...],
    width_value: int,
) -> tuple[int, ...]:
    x0 = [ZERO] * width_value
    x1 = _seed_positions_72207abc(len(colors))
    for x2, x3 in zip(x1, colors):
        x0[x2] = x3
    x4 = x1[-1]
    x5 = len(colors)
    x6 = ZERO
    while True:
        x4 += x5
        if x4 >= width_value:
            break
        x0[x4] = colors[x6 % len(colors)]
        x5 += ONE
        x6 += ONE
    return tuple(x0)


def _render_input_72207abc(
    colors: tuple[int, ...],
    width_value: int,
) -> Grid:
    x0 = [ZERO] * width_value
    x1 = _seed_positions_72207abc(len(colors))
    for x2, x3 in zip(x1, colors):
        x0[x2] = x3
    x4 = tuple(ZERO for _ in range(width_value))
    return (x4, tuple(x0), x4)


def generate_72207abc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(WIDTH_OPTIONS_72207ABC)
        x1 = choice(SEED_COUNT_OPTIONS_72207ABC)
        x2 = tuple(sample(COLOR_POOL_72207ABC, x1))
        x3 = _render_input_72207abc(x2, x0)
        x4 = tuple(ZERO for _ in range(x0))
        x5 = (x4, _render_row_72207abc(x2, x0), x4)
        if x3 == x5:
            continue
        if verify_72207abc(x3) != x5:
            continue
        return {"input": x3, "output": x5}
