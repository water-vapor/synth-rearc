from synth_rearc.core import *


COLOR_POOL_782B5218 = remove(TWO, interval(ONE, TEN, ONE))
PROFILE_MODES_782B5218 = ("flat", "zigzag", "stair")


def _flat_profile_782b5218(
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    x0 = unifint(diff_lb, diff_ub, (2, 5))
    x1 = tuple(x0 for _ in range(TEN))
    return x1, x1


def _zigzag_profile_782b5218(
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    x0 = [unifint(diff_lb, diff_ub, (2, 6))]
    for _ in range(TEN - ONE):
        x1 = x0[-ONE]
        x2 = choice((NEG_ONE, ZERO, ONE))
        x3 = min(max(x1 + x2, 2), 7)
        x0.append(x3)
    x4 = unifint(diff_lb, diff_ub, (1, 4))
    x5 = tuple(
        value - ONE if value > ZERO and randint(ZERO, 4) < x4 else value
        for value in x0
    )
    return tuple(x0), x5


def _stair_profile_782b5218(
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    x0 = [unifint(diff_lb, diff_ub, (1, 3))]
    x1 = unifint(diff_lb, diff_ub, (7, TEN))
    for _ in range(x1 - ONE):
        x2 = x0[-ONE]
        if x2 == NINE:
            if len(x0) >= 8 and randint(ZERO, ONE) == ZERO:
                break
            x0.append(NINE)
            continue
        x3 = choice((ZERO, ONE, ONE))
        x0.append(min(NINE, x2 + x3))
    x4 = [max(ZERO, value - ONE) for value in x0]
    if x0[-ONE] == NINE:
        x4[-ONE] = NINE
    return tuple(x0), tuple(x4)


def _sample_profile_782b5218(
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    x0 = choice(PROFILE_MODES_782B5218)
    if x0 == "flat":
        return _flat_profile_782b5218(diff_lb, diff_ub)
    if x0 == "zigzag":
        return _zigzag_profile_782b5218(diff_lb, diff_ub)
    return _stair_profile_782b5218(diff_lb, diff_ub)


def _noise_grid_782b5218(
    color_value: int,
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    x0 = unifint(diff_lb, diff_ub, (3, 7))
    x1 = frozenset(
        (i, j)
        for i in range(TEN)
        for j in range(TEN)
        if randint(ZERO, NINE) < x0
    )
    x2 = canvas(ZERO, (TEN, TEN))
    x3 = fill(x2, color_value, x1)
    return x3


def generate_782b5218(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(COLOR_POOL_782B5218)
        x1, x2 = _sample_profile_782b5218(diff_lb, diff_ub)
        x3 = _noise_grid_782b5218(x0, diff_lb, diff_ub)
        x4 = frozenset(
            (i, j)
            for j, x5 in enumerate(x1)
            for i in range(x2[j], x5 + ONE)
        )
        x5 = fill(x3, TWO, x4)
        x6 = frozenset(
            (i, j)
            for j, x7 in enumerate(x1)
            for i in range(x7 + ONE, TEN)
        )
        x7 = canvas(ZERO, (TEN, TEN))
        x8 = fill(x7, x0, x6)
        x9 = fill(x8, TWO, x4)
        x10 = palette(x5)
        if ZERO not in x10 or x0 not in x10:
            continue
        if colorcount(x5, TWO) < 5:
            continue
        return {"input": x5, "output": x9}
