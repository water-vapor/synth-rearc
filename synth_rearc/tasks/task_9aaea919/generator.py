from synth_rearc.core import *

from .verifier import verify_9aaea919


COLUMN_LEFTS_9aaea919 = (3, 9, 15, 21)
STACK_ROWS_9aaea919 = (25, 21, 17, 13, 9, 5, 1)
BAR_ROW_9aaea919 = 29
CAPSULE_OFFSETS_9aaea919 = (
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 0),
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (2, 1),
    (2, 2),
    (2, 3),
)
AVAILABLE_COLORS_9aaea919 = remove(FIVE, interval(ZERO, TEN, ONE))
AVAILABLE_BACKGROUNDS_9aaea919 = remove(THREE, remove(TWO, AVAILABLE_COLORS_9aaea919))


def _capsule_object_9aaea919(
    value: int,
    top: int,
    left: int,
) -> Object:
    return frozenset((value, (top + di, left + dj)) for di, dj in CAPSULE_OFFSETS_9aaea919)


def _paint_stack_9aaea919(
    grid: Grid,
    value: int,
    left: int,
    count: int,
) -> Grid:
    x0 = grid
    for x1 in STACK_ROWS_9aaea919[:count]:
        x2 = _capsule_object_9aaea919(value, x1, left)
        x0 = paint(x0, x2)
    return x0


def _bar_patch_9aaea919(
    left: int,
) -> Indices:
    return connect((BAR_ROW_9aaea919, left), (BAR_ROW_9aaea919, left + FOUR))


def _sample_layout_9aaea919(
    diff_lb: float,
    diff_ub: float,
) -> tuple[int, tuple[int, ...], tuple[int, ...], tuple[int, ...], int]:
    while True:
        x0 = choice(AVAILABLE_BACKGROUNDS_9aaea919)
        x1 = tuple(sample(remove(x0, AVAILABLE_COLORS_9aaea919), FOUR))
        x2 = randint(ZERO, len(COLUMN_LEFTS_9aaea919) - ONE)
        x3 = tuple(x4 for x4 in range(len(COLUMN_LEFTS_9aaea919)) if x4 != x2)
        x4 = unifint(diff_lb, diff_ub, (ONE, FOUR))
        x5 = ONE if x4 <= TWO else TWO
        x6 = tuple(sorted(sample(x3, x5)))
        x7 = []
        for _ in COLUMN_LEFTS_9aaea919:
            x8 = unifint(diff_lb, diff_ub, (ONE, THREE))
            x7.append(x8)
        x7 = tuple(x7)
        x8 = sum(x7[x9] for x9 in x6)
        x9 = len(STACK_ROWS_9aaea919) - x7[x2]
        if x8 <= x9:
            return x0, x1, x7, x6, x2


def _render_input_9aaea919(
    bg: int,
    colors: tuple[int, ...],
    counts: tuple[int, ...],
    recolor_cols: tuple[int, ...],
    grow_col: int,
) -> Grid:
    x0 = canvas(bg, (30, 30))
    for x1, x2 in enumerate(COLUMN_LEFTS_9aaea919):
        x0 = _paint_stack_9aaea919(x0, colors[x1], x2, counts[x1])
    for x1 in recolor_cols:
        x2 = _bar_patch_9aaea919(COLUMN_LEFTS_9aaea919[x1])
        x0 = fill(x0, TWO, x2)
    x1 = _bar_patch_9aaea919(COLUMN_LEFTS_9aaea919[grow_col])
    x0 = fill(x0, THREE, x1)
    return x0


def _render_output_9aaea919(
    bg: int,
    colors: tuple[int, ...],
    counts: tuple[int, ...],
    recolor_cols: tuple[int, ...],
    grow_col: int,
) -> Grid:
    x0 = canvas(bg, (30, 30))
    x1 = sum(counts[x2] for x2 in recolor_cols)
    for x2, x3 in enumerate(COLUMN_LEFTS_9aaea919):
        x4 = FIVE if contained(x2, recolor_cols) else colors[x2]
        x5 = counts[x2]
        if x2 == grow_col:
            x5 = x5 + x1
        x0 = _paint_stack_9aaea919(x0, x4, x3, x5)
    return x0


def generate_9aaea919(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0, x1, x2, x3, x4 = _sample_layout_9aaea919(diff_lb, diff_ub)
        x5 = _render_input_9aaea919(x0, x1, x2, x3, x4)
        x6 = _render_output_9aaea919(x0, x1, x2, x3, x4)
        if verify_9aaea919(x5) != x6:
            continue
        return {"input": x5, "output": x6}
