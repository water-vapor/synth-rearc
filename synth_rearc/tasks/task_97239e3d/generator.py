from synth_rearc.core import *

from .helpers import MARKER_COLORS_97239E3D
from .helpers import base_grid_97239e3d
from .helpers import region_patch_97239e3d


def _actual_bounds_97239e3d(
    region: tuple[int, int, int, int],
) -> tuple[int, int, int, int]:
    x0, x1, x2, x3 = region
    return (
        multiply(x0, FOUR),
        multiply(increment(x1), FOUR),
        multiply(x2, FOUR),
        multiply(increment(x3), FOUR),
    )


def _disjoint_regions_97239e3d(
    a: tuple[int, int, int, int],
    b: tuple[int, int, int, int],
) -> bool:
    x0, x1, x2, x3 = _actual_bounds_97239e3d(a)
    x4, x5, x6, x7 = _actual_bounds_97239e3d(b)
    return (
        x1 < x4
        or x5 < x0
        or x3 < x6
        or x7 < x2
    )


def _sample_region_97239e3d(
    diff_lb: float,
    diff_ub: float,
) -> tuple[int, int, int, int]:
    x0 = choice((ONE, ONE, TWO, TWO, THREE))
    x1 = choice((ONE, ONE, TWO, TWO, THREE))
    x2 = unifint(diff_lb, diff_ub, (ZERO, subtract(FOUR, x0)))
    x3 = unifint(diff_lb, diff_ub, (ZERO, subtract(FOUR, x1)))
    x4 = add(x2, decrement(x0))
    x5 = add(x3, decrement(x1))
    return (x2, x4, x3, x5)


def _marker_cells_97239e3d(
    region: tuple[int, int, int, int],
) -> frozenset[tuple[int, int]]:
    x0, x1, x2, x3 = region
    x4 = region_patch_97239e3d(x0, x1, x2, x3)
    x5, x6, x7, x8 = _actual_bounds_97239e3d(region)
    if choice((T, F)):
        x9 = tuple(
            x10
            for x10 in x4
            if either(
                both(x10[ZERO] == x5, x10[ONE] < add(x7, FOUR)),
                both(x10[ONE] == x7, x10[ZERO] < add(x5, FOUR)),
            )
        )
        x10 = tuple(
            x11
            for x11 in x4
            if either(
                both(x11[ZERO] == x6, x11[ONE] > subtract(x8, FOUR)),
                both(x11[ONE] == x8, x11[ZERO] > subtract(x6, FOUR)),
            )
        )
    else:
        x9 = tuple(
            x10
            for x10 in x4
            if either(
                both(x10[ZERO] == x5, x10[ONE] > subtract(x8, FOUR)),
                both(x10[ONE] == x8, x10[ZERO] < add(x5, FOUR)),
            )
        )
        x10 = tuple(
            x11
            for x11 in x4
            if either(
                both(x11[ZERO] == x6, x11[ONE] < add(x7, FOUR)),
                both(x11[ONE] == x7, x11[ZERO] > subtract(x6, FOUR)),
            )
        )
    x11 = {choice(x9), choice(x10)}
    x12 = tuple(x13 for x13 in x4 if x13 not in x11)
    x13 = min(FOUR, len(x4))
    x14 = randint(TWO, x13)
    x15 = subtract(x14, len(x11))
    if greater(x15, ZERO):
        x11 |= set(sample(x12, x15))
    return frozenset(x11)


def generate_97239e3d(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((ONE, TWO, TWO))
        x1 = sample(MARKER_COLORS_97239E3D, x0)
        x2 = []
        for _ in range(x0):
            for _ in range(100):
                x3 = _sample_region_97239e3d(diff_lb, diff_ub)
                if all(_disjoint_regions_97239e3d(x3, x4) for x4 in x2):
                    x2.append(x3)
                    break
            else:
                break
        if len(x2) != x0:
            continue

        x5 = base_grid_97239e3d()
        x6 = x5
        for x7, x8 in zip(x1, x2):
            x9 = _marker_cells_97239e3d(x8)
            x10 = region_patch_97239e3d(*x8)
            x5 = fill(x5, x7, x9)
            x6 = fill(x6, x7, x10)
        return {"input": x5, "output": x6}
