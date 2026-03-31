from __future__ import annotations

from synth_rearc.core import *


BoundsD59B0160 = tuple[int, int, int, int]
IndexD59B0160 = tuple[int, int]


AVAILABLE_COLORS_D59B0160 = tuple(v for v in range(ONE, 10) if v not in (THREE, SEVEN))
CLUE_POSITIONS_D59B0160 = tuple((i, j) for i in range(THREE) for j in range(THREE))
CLUE_FRAME_D59B0160 = frozenset((THREE, j) for j in range(FOUR)) | frozenset((i, THREE) for i in range(FOUR))

TEMPLATES_D59B0160 = (
    (
        (ZERO, FOUR, 7, 9),
        (ONE, FIVE, 12, 14),
        (6, 9, THREE, 10),
        (7, 15, 14, 15),
        (11, 14, ZERO, 7),
        (11, 15, 9, 12),
    ),
    (
        (ONE, 6, 6, 8),
        (ONE, 7, 12, 14),
        (9, 13, ONE, 7),
        (11, 15, 11, 15),
    ),
    (
        (ONE, 7, 7, 15),
        (FIVE, 10, ONE, FIVE),
        (9, 13, 9, 12),
        (12, 14, TWO, 7),
        (12, 15, 14, 15),
    ),
    (
        (ZERO, 15, 6, 8),
        (ONE, THREE, 10, 14),
        (FIVE, 9, 10, 15),
        (FIVE, 15, ZERO, ONE),
        (6, 15, THREE, FOUR),
        (11, 13, 11, 15),
    ),
)


def rect_patch_d59b0160(bounds: BoundsD59B0160) -> frozenset[IndexD59B0160]:
    x0, x1, x2, x3 = bounds
    x4 = interval(x0, x1 + ONE, ONE)
    x5 = interval(x2, x3 + ONE, ONE)
    return product(x4, x5)


def sample_clue_positions_d59b0160() -> tuple[IndexD59B0160, ...]:
    while True:
        x0 = tuple(sample(CLUE_POSITIONS_D59B0160, THREE))
        x1 = set(CLUE_FRAME_D59B0160)
        x2 = [x3 for x3 in CLUE_FRAME_D59B0160]
        while len(x2) > ZERO:
            x3 = x2.pop()
            for x4 in dneighbors(x3):
                if x4 in x1 or x4 not in x0:
                    continue
                x1.add(x4)
                x2.append(x4)
        x5 = sum(ONE for x6 in x0 if x6 in x1)
        if x5 < THREE:
            return x0


def apply_clue_block_d59b0160(
    grid: Grid,
    clue_colors: tuple[int, int, int],
    clue_positions: tuple[IndexD59B0160, ...],
) -> Grid:
    x0 = fill(grid, THREE, CLUE_FRAME_D59B0160)
    x1 = frozenset((x2, x3) for x2, x3 in zip(clue_colors, clue_positions))
    x2 = paint(x0, x1)
    return x2


def sample_region_bounds_d59b0160(bounds: BoundsD59B0160) -> BoundsD59B0160:
    x0, x1, x2, x3 = bounds
    if choice((True, False)):
        return bounds
    x4 = x1 - x0 + ONE
    x5 = x3 - x2 + ONE
    x6 = randint(ZERO, min(ONE, x4 - TWO))
    x7 = randint(ZERO, min(ONE, x4 - x6 - TWO))
    x8 = randint(ZERO, min(ONE, x5 - TWO))
    x9 = randint(ZERO, min(ONE, x5 - x8 - TWO))
    return (x0 + x6, x1 - x7, x2 + x8, x3 - x9)


def choose_bad_slots_d59b0160(slot_count: int) -> frozenset[int]:
    if slot_count == FOUR:
        x0 = choice((ONE, ONE, TWO))
    elif slot_count == FIVE:
        x0 = choice((ONE, TWO, TWO))
    else:
        x0 = choice((TWO, TWO, THREE))
    return frozenset(sample(tuple(range(slot_count)), x0))


def decorate_region_d59b0160(
    grid: Grid,
    bounds: BoundsD59B0160,
    required: tuple[int, ...],
    allowed: tuple[int, ...],
    diff_lb: float,
    diff_ub: float,
    *,
    allow_blank: bool = False,
) -> Grid:
    x0 = rect_patch_d59b0160(bounds)
    x1 = fill(grid, ZERO, x0)
    x2 = tuple(sorted(x0))
    if allow_blank and choice((False, False, True)):
        return x1
    x3 = len(x2)
    x4 = len(required)
    x5 = min(max(ZERO, x3 - x4), 6)
    x6 = ZERO if x5 == ZERO else unifint(diff_lb, diff_ub, (ZERO, x5))
    x7 = x4 + x6
    x8 = list(sample(x2, x7))
    x9 = list(required)
    while len(x9) < x7:
        x9.append(choice(allowed))
    shuffle(x9)
    x10 = frozenset((x11, x12) for x11, x12 in zip(x9, x8))
    x11 = paint(x1, x10)
    return x11
