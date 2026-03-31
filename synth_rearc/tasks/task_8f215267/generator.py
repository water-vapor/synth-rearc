from __future__ import annotations

from synth_rearc.core import *


FRAME_HEIGHT_8F215267 = FIVE
FRAME_WIDTH_8F215267 = 11
FRAME_GAP_8F215267 = ONE
GRID_WIDTH_8F215267 = 23
MAX_MARKS_8F215267 = FOUR

BASE_SHAPES_8F215267 = (
    ((ZERO, ZERO), (ZERO, ONE)),
    ((ZERO, ZERO), (ONE, ZERO)),
    ((ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE)),
    ((ZERO, ONE), (ONE, ZERO), (ONE, ONE)),
    ((ZERO, ONE), (ONE, ZERO), (ONE, ONE), (ONE, TWO), (TWO, ONE)),
    ((ZERO, TWO), (ONE, ZERO), (ONE, ONE), (ONE, TWO), (TWO, ONE)),
    ((ZERO, TWO), (ONE, ZERO), (ONE, ONE), (ONE, TWO), (ONE, THREE), (ONE, FOUR), (TWO, TWO)),
    ((ZERO, ONE), (ONE, ZERO), (ONE, ONE), (ONE, TWO), (TWO, ZERO), (TWO, ONE), (TWO, TWO), (THREE, ONE)),
    ((ZERO, ONE), (ZERO, TWO), (ONE, ZERO), (ONE, ONE), (ONE, TWO), (ONE, THREE), (TWO, ONE), (TWO, TWO)),
)


def _normalize_shape_8f215267(
    shape_: tuple[tuple[int, int], ...],
) -> tuple[tuple[int, int], ...]:
    x0 = min(x1 for x1, _ in shape_)
    x1 = min(x2 for _, x2 in shape_)
    return tuple(sorted((x2 - x0, x3 - x1) for x2, x3 in shape_))


def _shape_variants_8f215267(
    shape_: tuple[tuple[int, int], ...],
) -> tuple[tuple[tuple[int, int], ...], ...]:
    x0 = (
        lambda x1, x2: (x1, x2),
        lambda x1, x2: (x1, -x2),
        lambda x1, x2: (-x1, x2),
        lambda x1, x2: (-x1, -x2),
        lambda x1, x2: (x2, x1),
        lambda x1, x2: (x2, -x1),
        lambda x1, x2: (-x2, x1),
        lambda x1, x2: (-x2, -x1),
    )
    x1 = {
        _normalize_shape_8f215267(tuple(x2(i, j) for i, j in shape_))
        for x2 in x0
    }
    return tuple(sorted(x1))


SHAPE_VARIANTS_8F215267 = tuple(
    x0
    for x1 in BASE_SHAPES_8F215267
    for x0 in _shape_variants_8f215267(x1)
)


def _inflate_8f215267(
    indices: frozenset[tuple[int, int]],
) -> frozenset[tuple[int, int]]:
    return frozenset(
        (i + di, j + dj)
        for i, j in indices
        for di in (-ONE, ZERO, ONE)
        for dj in (-ONE, ZERO, ONE)
    )


def _frame_indices_8f215267(
    top: int,
    left: int,
) -> frozenset[tuple[int, int]]:
    x0 = frozenset({(top, left), (top + FRAME_HEIGHT_8F215267 - ONE, left + FRAME_WIDTH_8F215267 - ONE)})
    return box(x0)


def _render_frames_8f215267(
    bg: int,
    dims: tuple[int, int],
    frames: tuple[dict, ...],
) -> Grid:
    x0 = canvas(bg, dims)
    for x1 in frames:
        x2 = recolor(x1["color"], x1["indices"])
        x0 = paint(x0, x2)
    return x0


def _render_output_8f215267(
    bg: int,
    dims: tuple[int, int],
    frames: tuple[dict, ...],
) -> Grid:
    x0 = _render_frames_8f215267(bg, dims, frames)
    for x1 in frames:
        x2 = x1["count"]
        if x2 == ZERO:
            continue
        x3 = x1["top"] + TWO
        x4 = x1["left"] + FRAME_WIDTH_8F215267 - ONE
        x5 = frozenset((x3, x4 - TWO * x6) for x6 in range(ONE, x2 + ONE))
        x0 = fill(x0, x1["color"], x5)
    return x0


def _sample_counts_8f215267(
    nframes: int,
    diff_lb: float,
    diff_ub: float,
) -> tuple[int, ...]:
    while True:
        x0 = tuple(unifint(diff_lb, diff_ub, (ZERO, MAX_MARKS_8F215267)) for _ in range(nframes))
        x1 = sum(x0)
        if ONE <= x1 <= EIGHT:
            return x0


def _choose_distractor_colors_8f215267(
    bg: int,
    frame_colors: tuple[int, ...],
    diff_lb: float,
    diff_ub: float,
) -> tuple[int, ...]:
    x0 = tuple(x1 for x1 in range(ONE, TEN) if x1 != bg and x1 not in frame_colors)
    x1 = unifint(diff_lb, diff_ub, (ONE, THREE))
    return tuple(choice(x0) for _ in range(x1))


def _place_noise_8f215267(
    grid: Grid,
    frames: tuple[dict, ...],
    colors: tuple[int, ...],
    clutter_left: int,
) -> Grid | None:
    x0 = set()
    for x1 in frames:
        x0 |= _inflate_8f215267(x1["indices"])
    x1, x2 = shape(grid)
    x3 = grid
    x4 = list(colors)
    shuffle(x4)
    for x5 in x4:
        x6 = False
        for _ in range(400):
            x7 = choice(SHAPE_VARIANTS_8F215267)
            x8 = max(i for i, _ in x7) + ONE
            x9 = max(j for _, j in x7) + ONE
            if clutter_left + x9 > x2:
                continue
            x10 = randint(ZERO, x1 - x8)
            x11 = randint(clutter_left, x2 - x9)
            x12 = frozenset((x10 + i, x11 + j) for i, j in x7)
            if any(x13 in x0 for x13 in x12):
                continue
            x13 = _inflate_8f215267(x12)
            x0 |= x13
            x3 = fill(x3, x5, x12)
            x6 = True
            break
        if not x6:
            return None
    return x3


def generate_8f215267(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (THREE, FOUR))
        x1 = unifint(diff_lb, diff_ub, (ONE, TWO))
        x2 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x3 = x1 + x0 * FRAME_HEIGHT_8F215267 + (x0 - ONE) * FRAME_GAP_8F215267 + x2
        x4 = GRID_WIDTH_8F215267
        x5 = choice(tuple(range(ONE, TEN)))
        x6 = sample(tuple(x7 for x7 in range(ONE, TEN) if x7 != x5), x0)
        x7 = _sample_counts_8f215267(x0, diff_lb, diff_ub)
        x8 = unifint(diff_lb, diff_ub, (ONE, TWO))
        x9 = tuple(
            {
                "top": x1 + x10 * (FRAME_HEIGHT_8F215267 + FRAME_GAP_8F215267),
                "left": x8,
                "color": x6[x10],
                "count": x7[x10],
                "indices": _frame_indices_8f215267(
                    x1 + x10 * (FRAME_HEIGHT_8F215267 + FRAME_GAP_8F215267),
                    x8,
                ),
            }
            for x10 in range(x0)
        )
        x10 = _render_frames_8f215267(x5, (x3, x4), x9)
        x11 = x8 + FRAME_WIDTH_8F215267 + TWO
        x12 = tuple(
            x13["color"]
            for x13 in x9
            for _ in range(x13["count"])
        )
        x13 = _choose_distractor_colors_8f215267(x5, tuple(x6), diff_lb, diff_ub)
        x14 = _place_noise_8f215267(x10, x9, x12 + x13, x11)
        if x14 is None:
            continue
        x15 = _render_output_8f215267(x5, (x3, x4), x9)
        if x14 == x15:
            continue
        return {"input": x14, "output": x15}
