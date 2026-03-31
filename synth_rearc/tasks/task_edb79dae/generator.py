from __future__ import annotations

from synth_rearc.core import *

from .helpers import (
    embed_grid_edb79dae,
    paint_template_edb79dae,
    pair_objects_edb79dae,
    render_boards_edb79dae,
)


ALL_COLORS_EDB79DAE = tuple(range(ONE, TEN))
RIGHT_GAP_EDB79DAE = TWO
RIGHT_STRIP_WIDTH_EDB79DAE = SEVEN


def _sample_template_edb79dae(
    motif_size: Integer,
) -> Indices:
    x0 = {(x1, x2) for x1 in range(motif_size) for x2 in range(motif_size)}
    x3 = max(motif_size + TWO, (TWO * motif_size * motif_size) // THREE)
    x4 = max(ONE, min(TWO * motif_size, motif_size * motif_size - x3))
    x5 = tuple(x0)
    for _ in range(80):
        x6 = set(x0)
        x7 = list(x5)
        shuffle(x7)
        x8 = randint(ONE, x4)
        x9 = ZERO
        for x10, x11 in x7:
            if x9 == x8:
                break
            x12 = sum((x10, x13) in x6 for x13 in range(motif_size))
            x14 = sum((x15, x11) in x6 for x15 in range(motif_size))
            if x12 == ONE or x14 == ONE:
                continue
            if randint(ZERO, 99) < 35 and (x10 in (ZERO, motif_size - ONE) or x11 in (ZERO, motif_size - ONE)):
                continue
            x6.remove((x10, x11))
            x9 += ONE
        if len(x6) >= x3 and len(x6) < motif_size * motif_size:
            return frozenset(x6)
    x16 = set(x0)
    x17 = list(x5)
    shuffle(x17)
    for x18, x19 in x17:
        if len(x16) == x3:
            break
        x20 = sum((x18, x21) in x16 for x21 in range(motif_size))
        x22 = sum((x23, x19) in x16 for x23 in range(motif_size))
        if x20 == ONE or x22 == ONE:
            continue
        x16.remove((x18, x19))
    return frozenset(x16)


def _sample_colors_edb79dae(
    color_count: Integer,
    bg_color: Integer,
    border_color: Integer,
) -> tuple[tuple[Integer, ...], dict[Integer, Integer]]:
    x0 = [x1 for x1 in ALL_COLORS_EDB79DAE if x1 not in (bg_color, border_color)]
    shuffle(x0)
    x2 = tuple(x0[:color_count])
    x3 = list(x0)
    while True:
        shuffle(x3)
        x4 = tuple(x3[:color_count])
        if len(set(x4)) != color_count:
            continue
        if any(x5 == x6 for x5, x6 in zip(x2, x4)):
            continue
        return x2, {x7: x8 for x7, x8 in zip(x2, x4)}


def _sample_placements_edb79dae(
    row_count: Integer,
    col_count: Integer,
    sources: tuple[Integer, ...],
) -> tuple[tuple[Integer, Integer, Integer], ...]:
    x0 = [(x1, x2) for x1 in range(row_count) for x2 in range(col_count)]
    shuffle(x0)
    x3 = len(x0)
    x4 = len(sources)
    x5 = x4 if x3 == x4 else randint(x4, x3 - ONE)
    x6 = x0[:x5]
    x7 = list(sources)
    while len(x7) < x5:
        x7.append(choice(sources))
    shuffle(x7)
    return tuple((x8, x9[0], x9[1]) for x8, x9 in zip(x7, x6))


def _expand_rect_edb79dae(
    origin: IntegerTuple,
    dims: IntegerTuple,
    full_dims: IntegerTuple,
) -> set[IntegerTuple]:
    x0, x1 = origin
    x2, x3 = dims
    x4, x5 = full_dims
    x6 = max(ZERO, x0 - ONE)
    x7 = max(ZERO, x1 - ONE)
    x8 = min(x4, x0 + x2 + ONE)
    x9 = min(x5, x1 + x3 + ONE)
    return {(x10, x11) for x10 in range(x6, x8) for x11 in range(x7, x9)}


def _pack_rectangles_edb79dae(
    full_dims: IntegerTuple,
    board_origin: IntegerTuple,
    board_dims: IntegerTuple,
    rects: tuple[tuple[tuple[str, Integer], IntegerTuple], ...],
) -> dict[tuple[str, Integer], IntegerTuple] | None:
    x0 = set(_expand_rect_edb79dae(board_origin, board_dims, full_dims))
    x1: dict[tuple[str, Integer], IntegerTuple] = {}
    for x2, x3 in rects:
        x4, x5 = x3
        x6, x7 = full_dims
        x8 = []
        for x9 in range(x6 - x4 + ONE):
            for x10 in range(x7 - x5 + ONE):
                x11 = _expand_rect_edb79dae((x9, x10), x3, full_dims)
                if x11 & x0:
                    continue
                x8.append((x9, x10))
        if len(x8) == ZERO:
            return None
        x12 = choice(tuple(x8))
        x1[x2] = x12
        x0 |= _expand_rect_edb79dae(x12, x3, full_dims)
    return x1


def generate_edb79dae(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (THREE, FIVE))
        x1 = max(TWO, 18 // (x0 + ONE))
        x2 = unifint(diff_lb, diff_ub, (TWO, x1))
        x3 = unifint(diff_lb, diff_ub, (TWO, x1))
        x4 = x2 * x3
        x5 = min(FIVE, x4 - ONE)
        if x5 < TWO:
            continue
        x6 = unifint(diff_lb, diff_ub, (TWO, x5))
        x7 = choice(ALL_COLORS_EDB79DAE)
        x8 = choice(tuple(x9 for x9 in ALL_COLORS_EDB79DAE if x9 != x7))
        x9, x10 = _sample_colors_edb79dae(x6, x7, x8)
        x11: dict[Integer, Indices] = {}
        x12 = set()
        for x13 in x9:
            for _ in range(40):
                x14 = _sample_template_edb79dae(x0)
                if x14 in x12:
                    continue
                x11[x13] = x14
                x12.add(x14)
                break
        if len(x11) != x6:
            continue
        x15 = _sample_placements_edb79dae(x2, x3, x9)
        x16, x17 = render_boards_edb79dae(x7, x8, x2, x3, x0, x15, x11, x10)
        x18 = shape(x16)
        x19 = randint(x0 + TWO, x0 + FOUR)
        x20 = choice((ZERO, ZERO, ONE))
        x21 = x19 + x18[0] + x20
        x22 = max(ZERO, 30 - (RIGHT_GAP_EDB79DAE + RIGHT_STRIP_WIDTH_EDB79DAE + x18[1]))
        x23 = randint(ZERO, min(FIVE, x22))
        x24 = x23 + x18[1] + RIGHT_GAP_EDB79DAE + RIGHT_STRIP_WIDTH_EDB79DAE
        if x21 > 30 or x24 > 30:
            continue
        x25 = (x21 - x18[0] - x20, x23)
        x26: list[tuple[tuple[str, Integer], IntegerTuple]] = []
        for x27 in x9:
            x26.append((("template", x27), (x0, x0)))
            x26.append((("pair", x27), (THREE, FOUR)))
        shuffle(x26)
        x28 = tuple(sorted(x26, key=lambda x29: x29[1][0] * x29[1][1], reverse=True))
        x30 = _pack_rectangles_edb79dae((x21, x24), x25, x18, x28)
        if x30 is None:
            continue
        x31 = canvas(x7, (x21, x24))
        x31 = embed_grid_edb79dae(x31, x16, x25)
        for x32 in x9:
            x33 = x30[("template", x32)]
            x31 = paint_template_edb79dae(x31, x32, x11[x32], x33)
            x34 = x30[("pair", x32)]
            x35, x36 = pair_objects_edb79dae(x32, x10[x32], x34)
            x31 = paint(x31, x35)
            x31 = paint(x31, x36)
        if x31 == x17:
            continue
        return {"input": x31, "output": x17}
