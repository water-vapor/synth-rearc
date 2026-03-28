from synth_rearc.core import *

from .helpers import (
    NON_HOLE_COLORS_0934A4D8,
    SEED_SIZE_0934A4D8,
    VISIBLE_SIZE_0934A4D8,
    build_visible_board_0934a4d8,
    hide_rect_0934a4d8,
    visible_sources_0934a4d8,
)


def _seed_0934a4d8(
    palette_: tuple[int, ...],
) -> Grid:
    return tuple(
        tuple(choice(palette_) for _ in range(SEED_SIZE_0934A4D8))
        for _ in range(SEED_SIZE_0934A4D8)
    )


def _hole_candidates_0934a4d8(
    height_: int,
    width_: int,
) -> tuple[tuple[int, int], ...]:
    x0 = []
    for x1 in range(VISIBLE_SIZE_0934A4D8 - height_ + 1):
        for x2 in range(VISIBLE_SIZE_0934A4D8 - width_ + 1):
            x3 = visible_sources_0934a4d8(
                VISIBLE_SIZE_0934A4D8,
                x1,
                x2,
                height_,
                width_,
            )
            if len(x3) < TWO:
                continue
            if x1 + height_ <= SEED_SIZE_0934A4D8 and x2 + width_ <= SEED_SIZE_0934A4D8:
                continue
            x0.append((x1, x2))
    return tuple(x0)


def generate_0934a4d8(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = sample(NON_HOLE_COLORS_0934A4D8, unifint(diff_lb, diff_ub, (FOUR, EIGHT)))
        x1 = _seed_0934a4d8(x0)
        x2 = build_visible_board_0934a4d8(x1)
        x3 = unifint(diff_lb, diff_ub, (THREE, NINE))
        x4 = unifint(diff_lb, diff_ub, (THREE, SEVEN))
        x5 = _hole_candidates_0934a4d8(x3, x4)
        if len(x5) == ZERO:
            continue
        x6 = list(x5)
        shuffle(x6)
        for x7, x8 in x6:
            x9 = crop(x2, (x7, x8), (x3, x4))
            if numcolors(x9) < THREE:
                continue
            x10 = hide_rect_0934a4d8(x2, x7, x8, x3, x4)
            return {"input": x10, "output": x9}
