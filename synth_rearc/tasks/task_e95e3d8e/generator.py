from synth_rearc.core import *

from .verifier import verify_e95e3d8e


GRID_SIZE_E95E3D8E = 22
PERIODS_E95E3D8E = (THREE, FIVE, SEVEN, EIGHT)
COLOR_POOL_E95E3D8E = remove(ZERO, interval(ZERO, EIGHT, ONE))
NCOLOR_OPTIONS_E95E3D8E = {
    THREE: (THREE,),
    FIVE: (FOUR, FIVE, FIVE),
    SEVEN: (FIVE, SIX, SEVEN, SEVEN),
    EIGHT: (FOUR, FOUR, FIVE, SIX),
}
RECTANGLE_COUNTS_E95E3D8E = {
    THREE: (FOUR, FIVE, SIX),
    FIVE: (FOUR, FIVE, SIX),
    SEVEN: (FOUR, FIVE),
    EIGHT: (FOUR, FIVE),
}
RECTANGLE_BOUNDS_E95E3D8E = {
    THREE: (TWO, FOUR),
    FIVE: (TWO, FIVE),
    SEVEN: (TWO, SIX),
    EIGHT: (TWO, FIVE),
}


def _exact_vertical_period_e95e3d8e(
    grid: Grid,
) -> Integer:
    x0 = height(grid)
    x1 = width(grid)
    for x2 in range(ONE, x0 + ONE):
        if all(grid[x3][x4] == grid[x3 + x2][x4] for x3 in range(x0 - x2) for x4 in range(x1)):
            return x2
    return x0


def _exact_horizontal_period_e95e3d8e(
    grid: Grid,
) -> Integer:
    x0 = height(grid)
    x1 = width(grid)
    for x2 in range(ONE, x1 + ONE):
        if all(grid[x3][x4] == grid[x3][x4 + x2] for x3 in range(x0) for x4 in range(x1 - x2)):
            return x2
    return x1


def _repeat_tile_e95e3d8e(
    tile: Grid,
) -> Grid:
    x0 = height(tile)
    x1 = width(tile)
    return tuple(
        tuple(tile[x2 % x0][x3 % x1] for x3 in range(GRID_SIZE_E95E3D8E))
        for x2 in range(GRID_SIZE_E95E3D8E)
    )


def _rectangle_patch_e95e3d8e(
    top: Integer,
    left: Integer,
    h: Integer,
    w: Integer,
) -> Indices:
    return frozenset(
        (x0, x1)
        for x0 in range(top, top + h)
        for x1 in range(left, left + w)
    )


def _protected_patch_e95e3d8e(
    period: Integer,
) -> Indices:
    x0 = tuple(range(ZERO, GRID_SIZE_E95E3D8E - period + ONE, period))
    x1 = choice(x0)
    x2 = choice(x0)
    return _rectangle_patch_e95e3d8e(x1, x2, period, period)


def _exact_sequence_period_e95e3d8e(
    seq: tuple[Integer, ...],
) -> Integer:
    x0 = len(seq)
    for x1 in range(ONE, x0 + ONE):
        if all(seq[x2] == seq[x2 + x1] for x2 in range(x0 - x1)):
            return x1
    return x0


def _state_sequence_e95e3d8e(
    period: Integer,
    ncolors: Integer,
) -> tuple[Integer, ...]:
    while True:
        x0 = tuple(randint(ZERO, ncolors - ONE) for _ in range(period))
        if len(set(x0)) != ncolors:
            continue
        if _exact_sequence_period_e95e3d8e(x0) != period:
            continue
        return x0


def _symmetric_tile_e95e3d8e(
    period: Integer,
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    del diff_lb, diff_ub
    x0 = choice(NCOLOR_OPTIONS_E95E3D8E[period])
    x1 = sample(COLOR_POOL_E95E3D8E, x0)
    x2 = _state_sequence_e95e3d8e(period, x0)
    x3 = _state_sequence_e95e3d8e(period, x0)
    x4 = choice(("sum", "distance", "product", "product"))
    x5 = tuple(
        tuple(
            x1[
                (
                    x2[x6]
                    + x2[x7]
                    + (
                        x3[(x6 + x7) % period]
                        if x4 == "sum"
                        else x3[abs(x6 - x7)]
                        if x4 == "distance"
                        else x3[(x6 * x7) % period]
                    )
                )
                % x0
            ]
            for x7 in range(period)
        )
        for x6 in range(period)
    )
    return x5


def _zero_components_e95e3d8e(
    grid: Grid,
) -> tuple[frozenset[tuple[Integer, Integer]], ...]:
    x0 = height(grid)
    x1 = width(grid)
    x2 = set()
    x3 = []
    for x4 in range(x0):
        for x5 in range(x1):
            if grid[x4][x5] != ZERO or (x4, x5) in x2:
                continue
            x6 = {(x4, x5)}
            x7 = [(x4, x5)]
            while len(x7) > ZERO:
                x8, x9 = x7.pop()
                for x10, x11 in ((ONE, ZERO), (-ONE, ZERO), (ZERO, ONE), (ZERO, -ONE)):
                    x12 = x8 + x10
                    x13 = x9 + x11
                    if (
                        0 <= x12 < x0
                        and 0 <= x13 < x1
                        and grid[x12][x13] == ZERO
                        and (x12, x13) not in x6
                    ):
                        x6.add((x12, x13))
                        x7.append((x12, x13))
            x2.update(x6)
            x3.append(frozenset(x6))
    return tuple(x3)


def _separated_patch_e95e3d8e(
    patch: Indices,
    occupied: Indices,
) -> Boolean:
    if len(intersection(patch, occupied)) > ZERO:
        return F
    for x0, x1 in patch:
        for x2, x3 in ((ONE, ZERO), (-ONE, ZERO), (ZERO, ONE), (ZERO, -ONE)):
            if (x0 + x2, x1 + x3) in occupied:
                return F
    return T


def generate_e95e3d8e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(PERIODS_E95E3D8E)
        x1 = _symmetric_tile_e95e3d8e(x0, diff_lb, diff_ub)
        if _exact_vertical_period_e95e3d8e(x1) != x0:
            continue
        if _exact_horizontal_period_e95e3d8e(x1) != x0:
            continue
        x2 = tuple(colorcount(x1, x3) for x3 in palette(x1))
        if len(x2) < max(THREE, x0 // TWO):
            continue
        if minimum(x2) < TWO:
            continue
        if maximum(x2) > ((x0 * x0) * THREE) // FIVE:
            continue
        x4 = _repeat_tile_e95e3d8e(x1)
        x5 = _protected_patch_e95e3d8e(x0)
        x6 = x4
        x7 = choice(RECTANGLE_COUNTS_E95E3D8E[x0])
        x8, x9 = RECTANGLE_BOUNDS_E95E3D8E[x0]
        x10 = frozenset({})
        for _ in range(x7):
            x11 = unifint(diff_lb, diff_ub, (x8, x9))
            x12 = unifint(diff_lb, diff_ub, (x8, x9))
            x13 = randint(ZERO, GRID_SIZE_E95E3D8E - x11)
            x14 = randint(ZERO, GRID_SIZE_E95E3D8E - x12)
            x15 = difference(_rectangle_patch_e95e3d8e(x13, x14, x11, x12), x5)
            if len(x15) == ZERO:
                continue
            if not _separated_patch_e95e3d8e(x15, x10):
                continue
            x6 = fill(x6, ZERO, x15)
            x10 = combine(x10, x15)
        x16 = colorcount(x6, ZERO)
        if x16 < 35 or x16 > 80:
            continue
        x17 = _zero_components_e95e3d8e(x6)
        x18 = tuple(len(x19) for x19 in x17)
        if len(x17) < FOUR or len(x17) > SIX:
            continue
        if minimum(x18) < FOUR or maximum(x18) > 40:
            continue
        if x6 == x4:
            continue
        if verify_e95e3d8e(x6) != x4:
            continue
        return {"input": x6, "output": x4}
