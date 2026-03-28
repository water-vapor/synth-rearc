from synth_rearc.core import *

from .verifier import verify_1d398264


GRID_BOUNDS_1D398264 = (TEN, 20)
OUTER_OFFSETS_1D398264 = (
    (-1, -1),
    (-1, ZERO),
    (-1, ONE),
    (ZERO, -1),
    (ZERO, ONE),
    (ONE, -1),
    (ONE, ZERO),
    (ONE, ONE),
)
COLOR_POOL_1D398264 = tuple(range(ONE, increment(NINE)))


def _sample_pattern_1d398264(
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]:
    x0 = choice(COLOR_POOL_1D398264)
    x1 = tuple(x2 for x2 in COLOR_POOL_1D398264 if x2 != x0)
    x2 = unifint(diff_lb, diff_ub, (THREE, FIVE))
    x3 = sample(x1, x2)
    x4 = [choice(x3) for _ in range(EIGHT)]
    x5 = tuple(x4[:THREE])
    x6 = (x4[THREE], x0, x4[FOUR])
    x7 = tuple(x4[FIVE:])
    x8 = set(x4)
    if len(x8) < THREE:
        x4[ZERO] = x3[ZERO]
        x4[THREE] = x3[ONE % len(x3)]
        x4[SEVEN] = x3[TWO % len(x3)]
        x5 = tuple(x4[:THREE])
        x6 = (x4[THREE], x0, x4[FOUR])
        x7 = tuple(x4[FIVE:])
    return x5, x6, x7


def _render_from_pattern_1d398264(
    dims: IntegerTuple,
    top_left: IntegerTuple,
    pattern: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]],
) -> dict:
    x0 = canvas(ZERO, dims)
    x1, x2 = top_left
    x3 = set()
    for x4, x5 in enumerate(pattern):
        for x6, x7 in enumerate(x5):
            x8 = add(x1, x4)
            x9 = add(x2, x6)
            x3.add((x7, (x8, x9)))
    x10 = frozenset(x3)
    x11 = paint(x0, x10)
    x12 = add(x1, ONE)
    x13 = add(x2, ONE)
    x14 = set(x10)
    for x15, x16 in OUTER_OFFSETS_1D398264:
        x17 = add(x12, x15)
        x18 = add(x13, x16)
        x19 = index(x11, (x17, x18))
        x20 = shoot((x17, x18), (x15, x16))
        x21 = recolor(x19, x20)
        x14 |= set(x21)
    x22 = paint(x0, frozenset(x14))
    return {"input": x11, "output": x22}


def generate_1d398264(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, GRID_BOUNDS_1D398264)
        x1 = astuple(x0, x0)
        x2 = subtract(x0, FOUR)
        x3 = randint(ONE, x2)
        x4 = randint(ONE, x2)
        x5 = _sample_pattern_1d398264(diff_lb, diff_ub)
        x6 = _render_from_pattern_1d398264(x1, (x3, x4), x5)
        x7 = palette(x6["input"])
        x8 = palette(x6["output"])
        if len(x7) < FOUR:
            continue
        if len(x8) < FOUR:
            continue
        if verify_1d398264(x6["input"]) != x6["output"]:
            continue
        return x6
