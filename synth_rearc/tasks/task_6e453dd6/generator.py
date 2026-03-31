from synth_rearc.core import *

from .verifier import verify_6e453dd6


GLYPHS_6E453DD6 = (
    (
        (0, 1, 2, 3),
        (0, 1, 3),
        (1, 2, 3, 4),
        (0, 1, 2, 3, 4, 5),
        (3, 5),
        (3, 5),
        (3, 5),
        (3, 4, 5),
    ),
    (
        (0, 1, 2),
        (0, 2),
        (0, 2),
        (0, 1, 2),
    ),
    (
        (0, 1, 2),
        (0, 2),
        (0, 1, 2, 3),
        (1, 3),
        (1, 2, 3),
    ),
    (
        (0, 1, 2),
        (0, 2),
        (0, 1, 2),
        (0,),
        (0, 1, 2),
    ),
    (
        (0, 1, 2, 3, 4),
        (0, 4),
        (0, 1, 2, 3, 4),
    ),
    (
        (0, 1, 2, 3),
        (0, 3),
        (0, 3),
        (0, 1, 2, 3),
    ),
    (
        (0, 1),
        (0, 1),
    ),
    (
        (0, 1, 2, 3, 4),
        (0, 2, 4),
        (0, 1, 2, 3, 4),
    ),
    (
        (0, 1, 2, 3),
        (0, 3),
        (0, 1, 2, 3),
    ),
)


def _glyph_height_6e453dd6(
    glyph: tuple[tuple[int, ...], ...],
) -> int:
    return len(glyph)


def _glyph_width_6e453dd6(
    glyph: tuple[tuple[int, ...], ...],
) -> int:
    return max(max(row) for row in glyph) + ONE


def _trigger_rows_6e453dd6(
    glyph: tuple[tuple[int, ...], ...],
) -> tuple[int, ...]:
    x0 = _glyph_width_6e453dd6(glyph) - ONE
    x1 = []
    for x2, x3 in enumerate(glyph):
        x4 = tuple(sorted(x3))
        if last(x4) != x0:
            continue
        if size(x4) == last(x4) - first(x4) + ONE:
            continue
        x1.append(x2)
    return tuple(x1)


GLYPH_DATA_6E453DD6 = tuple(
    (
        glyph,
        _glyph_height_6e453dd6(glyph),
        _glyph_width_6e453dd6(glyph),
        _trigger_rows_6e453dd6(glyph),
    )
    for glyph in GLYPHS_6E453DD6
)


def _render_glyph_6e453dd6(
    glyph: tuple[tuple[int, ...], ...],
    top: int,
    left: int,
    color: int,
) -> Object:
    x0 = []
    for x1, x2 in enumerate(glyph):
        for x3 in x2:
            x0.append((color, (top + x1, left + x3)))
    return frozenset(x0)


def _stack_tops_6e453dd6(
    glyphs: tuple[tuple[tuple[int, ...], ...], ...],
    height: int,
) -> tuple[int, ...] | None:
    x0 = tuple(_glyph_height_6e453dd6(x1) for x1 in glyphs)
    x1 = sum(x0)
    x2 = size(glyphs) - ONE
    x3 = height - x1 - x2
    if x3 < ZERO:
        return None
    x4 = randint(ZERO, min(TWO, x3))
    x5 = x3 - x4
    x6 = []
    x7 = x4
    for x8, x9 in enumerate(x0):
        x6.append(x7)
        x7 += x9
        if x8 == size(x0) - ONE:
            break
        x10 = min(THREE, x5)
        x11 = ONE + randint(ZERO, x10)
        x7 += x11
        x5 -= x11 - ONE
    return tuple(x6)


def _make_input_6e453dd6(
    height: int,
    width: int,
    sep_col: int,
    placements: tuple[tuple[tuple[tuple[int, ...], ...], int, int], ...],
) -> Grid:
    x0 = canvas(SIX, (height, width))
    x1 = fill(x0, FIVE, frozenset((x2, sep_col) for x2 in range(height)))
    x2 = tuple(
        _render_glyph_6e453dd6(x3, x4, x5, ZERO)
        for x3, x4, x5 in placements
    )
    x3 = paint(x1, merge(x2))
    return x3


def _make_output_6e453dd6(
    height: int,
    width: int,
    sep_col: int,
    placements: tuple[tuple[tuple[tuple[int, ...], ...], int, int], ...],
) -> Grid:
    x0 = canvas(SIX, (height, width))
    x1 = fill(x0, FIVE, frozenset((x2, sep_col) for x2 in range(height)))
    x2 = []
    x3 = []
    for x4, x5, _ in placements:
        x6 = _glyph_width_6e453dd6(x4)
        x7 = sep_col - x6
        x2.append(_render_glyph_6e453dd6(x4, x5, x7, ZERO))
        x8 = _trigger_rows_6e453dd6(x4)
        for x9 in x8:
            x10 = x5 + x9
            x3.extend((x10, x11) for x11 in range(sep_col + ONE, width))
    x4 = paint(x1, merge(tuple(x2)))
    x5 = fill(x4, TWO, frozenset(x3))
    return x5


def generate_6e453dd6(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (14, 26))
        x1 = choice((TWO, THREE, FOUR))
        x2 = unifint(diff_lb, diff_ub, (6, 11))
        x3 = x2 + x1 + ONE
        x4 = tuple(x5 for x5 in GLYPH_DATA_6E453DD6 if x5[2] <= x2)
        if len(x4) < TWO:
            continue
        x5 = randint(TWO, min(SIX, max(TWO, x0 // THREE)))
        x6 = tuple(choice(x4) for _ in range(x5))
        x7 = tuple(x8[0] for x8 in x6)
        x8 = _stack_tops_6e453dd6(x7, x0)
        if x8 is None:
            continue
        x9 = []
        x10 = F
        x11 = F
        for x12, x13 in zip(x6, x8):
            x14, _, x15, x16 = x12
            x17 = x2 - x15
            if both(x17 > ZERO, choice((T, T, F))):
                x18 = randint(ZERO, x17 - ONE)
            else:
                x18 = x17
            if x18 != x17:
                x10 = T
            if len(x16) > ZERO:
                x11 = T
            x9.append((x14, x13, x18))
        if not either(x10, x11):
            continue
        if not x11:
            continue
        x19 = tuple(x9)
        x20 = _make_input_6e453dd6(x0, x3, x2, x19)
        x21 = _make_output_6e453dd6(x0, x3, x2, x19)
        if verify_6e453dd6(x20) != x21:
            continue
        return {"input": x20, "output": x21}
