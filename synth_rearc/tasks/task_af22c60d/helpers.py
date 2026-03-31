from __future__ import annotations

from synth_rearc.core import *


GRID_SIDE_AF22C60D = 30
SEED_SIDE_AF22C60D = 16
BLOCK_SIDE_AF22C60D = 8
MIRROR_SUM_AF22C60D = 31
PALETTE_AF22C60D = tuple(remove(ZERO, interval(ZERO, TEN, ONE)))


def orbit_af22c60d(
    loc: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    i, j = loc
    x0 = {(i, j)}
    if i >= TWO:
        x0.add((MIRROR_SUM_AF22C60D - i, j))
    if j >= TWO:
        x0.add((i, MIRROR_SUM_AF22C60D - j))
    if i >= TWO and j >= TWO:
        x0.add((MIRROR_SUM_AF22C60D - i, MIRROR_SUM_AF22C60D - j))
    return tuple(sorted(x0))


def _block_orbit_af22c60d(
    loc: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    i, j = loc
    n = BLOCK_SIDE_AF22C60D
    x0 = {
        (i, j),
        (j, i),
        (n - ONE - i, j),
        (i, n - ONE - j),
        (n - ONE - j, n - ONE - i),
        (n - ONE - i, n - ONE - j),
        (j, n - ONE - i),
        (n - ONE - j, i),
    }
    return tuple(sorted(x0))


CANONICAL_BLOCK_REPS_AF22C60D = tuple(
    sorted(
        {
            min(_block_orbit_af22c60d((i, j)))
            for i in range(BLOCK_SIDE_AF22C60D)
            for j in range(BLOCK_SIDE_AF22C60D)
        },
        key=lambda x0: (x0[0] + x0[1], x0[0], x0[1]),
    )
)


def _neighbor_colors_af22c60d(
    loc: IntegerTuple,
    assigned: dict[IntegerTuple, Integer],
) -> list[Integer]:
    i, j = loc
    x0 = []
    for (a, b), col in assigned.items():
        if max(abs(i - a), abs(j - b)) <= ONE:
            x0.append(col)
    return x0


def make_block_af22c60d(
    colors: tuple[Integer, Integer, Integer],
) -> Grid:
    x0 = list(colors)
    shuffle(x0)
    dominant, middle, accent = x0
    x1 = {dominant: 6, middle: 3, accent: 2}
    x2: dict[IntegerTuple, Integer] = {}
    for x3 in CANONICAL_BLOCK_REPS_AF22C60D:
        x4 = (
            [dominant] * x1[dominant]
            + [middle] * x1[middle]
            + [accent] * x1[accent]
        )
        x5 = _neighbor_colors_af22c60d(x3, x2)
        for x6 in x5:
            x4.extend([x6, x6])
        x2[x3] = choice(x4)
    x7 = [x3 for x3 in reversed(CANONICAL_BLOCK_REPS_AF22C60D)]
    x8 = set(x2.values())
    for x9 in colors:
        if x9 in x8:
            continue
        for x10 in x7:
            if x2[x10] != x9:
                x2[x10] = x9
                x8.add(x9)
                break
    x11 = [[ZERO for _ in range(BLOCK_SIDE_AF22C60D)] for _ in range(BLOCK_SIDE_AF22C60D)]
    for x12, x13 in x2.items():
        for x14, x15 in _block_orbit_af22c60d(x12):
            x11[x14][x15] = x13
    return tuple(tuple(x12) for x12 in x11)


def build_seed_af22c60d(
    block_a: Grid,
    block_b: Grid,
    block_c: Grid,
) -> Grid:
    x0 = []
    for x1 in range(BLOCK_SIDE_AF22C60D):
        x0.append(tuple(block_a[x1] + block_b[x1]))
    for x1 in range(BLOCK_SIDE_AF22C60D):
        x0.append(tuple(block_b[x1] + block_c[x1]))
    return tuple(x0)


def extend_seed_af22c60d(
    seed: Grid,
) -> Grid:
    x0 = []
    for x1 in range(GRID_SIDE_AF22C60D):
        x2 = x1 if x1 < SEED_SIDE_AF22C60D else MIRROR_SUM_AF22C60D - x1
        x3 = []
        for x4 in range(GRID_SIDE_AF22C60D):
            x5 = x4 if x4 < SEED_SIDE_AF22C60D else MIRROR_SUM_AF22C60D - x4
            x3.append(seed[x2][x5])
        x0.append(tuple(x3))
    return tuple(x0)


def orbit_covered_af22c60d(
    grid: Grid,
) -> Boolean:
    for x0 in range(SEED_SIDE_AF22C60D):
        for x1 in range(SEED_SIDE_AF22C60D):
            x2 = orbit_af22c60d((x0, x1))
            if all(grid[x3][x4] == ZERO for x3, x4 in x2):
                return F
    return T


def zero_component_count_af22c60d(
    grid: Grid,
) -> Integer:
    x0 = {(i, j) for i in range(GRID_SIDE_AF22C60D) for j in range(GRID_SIDE_AF22C60D) if grid[i][j] == ZERO}
    x1 = set()
    x2 = ZERO
    for x3 in x0:
        if x3 in x1:
            continue
        x2 += ONE
        x4 = [x3]
        x1.add(x3)
        while x4:
            i, j = x4.pop()
            for di, dj in ((ONE, ZERO), (-ONE, ZERO), (ZERO, ONE), (ZERO, -ONE)):
                x5 = (i + di, j + dj)
                if x5 in x0 and x5 not in x1:
                    x1.add(x5)
                    x4.append(x5)
    return x2


def _rectangles_af22c60d(
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[Integer, Integer, Integer, Integer], ...]:
    x0 = []
    x1 = unifint(diff_lb, diff_ub, (TWO, FIVE))
    for x2 in range(x1):
        x3 = (4, 10) if x2 == ZERO else (2, 7)
        x4 = unifint(diff_lb, diff_ub, x3)
        x5 = unifint(diff_lb, diff_ub, x3)
        x6 = randint(ZERO, GRID_SIDE_AF22C60D - x4)
        x7 = randint(ZERO, GRID_SIDE_AF22C60D - x5)
        x0.append((x6, x7, x4, x5))
    return tuple(x0)


def carve_input_af22c60d(
    output: Grid,
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    while True:
        x0 = [list(x1) for x1 in output]
        for x1, x2, x3, x4 in _rectangles_af22c60d(diff_lb, diff_ub):
            for x5 in range(x1, x1 + x3):
                for x6 in range(x2, x2 + x4):
                    x0[x5][x6] = ZERO
        x7 = tuple(tuple(x1) for x1 in x0)
        x8 = sum(x1 == ZERO for x2 in x7 for x1 in x2)
        if x8 < 25 or x8 > 140:
            continue
        x9 = zero_component_count_af22c60d(x7)
        if x9 < TWO or x9 > FIVE:
            continue
        if not orbit_covered_af22c60d(x7):
            continue
        return x7
