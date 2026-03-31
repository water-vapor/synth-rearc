from synth_rearc.core import *

from .verifier import verify_58f5dbd5


INPUT_HEIGHT_58F5DBD5 = 19
LAYOUTS_58F5DBD5 = (
    (ONE, THREE),
    (TWO, TWO),
    (THREE, ONE),
    (THREE, TWO),
    (TWO, THREE),
)
BIG_BLOCK_PATCH_58F5DBD5 = frozenset(
    (i, j) for i in range(FIVE) for j in range(FIVE)
)


def _build_glyph_library_58f5dbd5() -> tuple[Indices, ...]:
    x0 = []
    for x1 in range(ONE, TWO ** NINE):
        x2 = frozenset(
            (x3, x4)
            for x3 in range(THREE)
            for x4 in range(THREE)
            if (x1 >> (x3 * THREE + x4)) & ONE
        )
        x5 = size(x2)
        if x5 < FOUR or x5 > SEVEN:
            continue
        if height(x2) != THREE or width(x2) != THREE:
            continue
        x6 = size(delta(x2))
        if x6 < TWO or x6 > FIVE:
            continue
        x0.append(x2)
    return tuple(x0)


GLYPH_LIBRARY_58F5DBD5 = _build_glyph_library_58f5dbd5()


def _choose_input_width_58f5dbd5(
    rows: int,
    cols: int,
) -> int:
    if (rows, cols) in ((ONE, THREE), (THREE, ONE)):
        return 19
    return 23


def _render_large_tile_58f5dbd5(
    color_value: int,
    glyph: Indices,
    top_left: IntegerTuple,
) -> Object:
    x0 = shift(box(BIG_BLOCK_PATCH_58F5DBD5), top_left)
    x1 = shift(delta(glyph), add(top_left, UNITY))
    x2 = combine(x0, x1)
    return recolor(color_value, x2)


def _rectangles_too_close_58f5dbd5(
    a_top: int,
    a_left: int,
    a_bottom: int,
    a_right: int,
    b_top: int,
    b_left: int,
    b_bottom: int,
    b_right: int,
) -> bool:
    return not (
        a_bottom + ONE < b_top
        or b_bottom + ONE < a_top
        or a_right + ONE < b_left
        or b_right + ONE < a_left
    )


def _choose_glyph_positions_58f5dbd5(
    height_: int,
    width_: int,
    forbidden_rect: tuple[int, int, int, int],
    n_glyphs: int,
) -> tuple[IntegerTuple, ...] | None:
    x0 = tuple(
        (x1, x2)
        for x1 in range(ONE, height_ - THREE)
        for x2 in range(ONE, width_ - THREE)
    )
    x1 = list(x0)
    shuffle(x1)
    x2: list[tuple[int, int, int, int]] = []
    x3: list[IntegerTuple] = []
    for x4, x5 in x1:
        x6 = x4 + TWO
        x7 = x5 + TWO
        x8 = _rectangles_too_close_58f5dbd5(x4, x5, x6, x7, *forbidden_rect)
        if x8:
            continue
        x9 = any(
            _rectangles_too_close_58f5dbd5(x4, x5, x6, x7, *x10)
            for x10 in x2
        )
        if x9:
            continue
        x2.append((x4, x5, x6, x7))
        x3.append((x4, x5))
        if len(x3) == n_glyphs:
            return tuple(x3)
    return None


def generate_58f5dbd5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(LAYOUTS_58F5DBD5)
        x1, x2 = x0
        x3 = x1 * SIX + ONE
        x4 = x2 * SIX + ONE
        x5 = INPUT_HEIGHT_58F5DBD5
        x6 = _choose_input_width_58f5dbd5(x1, x2)
        x7 = x1 * x2
        x8 = min(FOUR, NINE - x7)
        x9 = unifint(diff_lb, diff_ub, (TWO, x8))
        x10 = choice(tuple(range(TEN)))
        x11 = tuple(x12 for x12 in range(TEN) if x12 != x10)
        x12 = sample(x11, x7 + x9)
        x13 = x12[:x7]
        x14 = x12[x7:]
        x15 = sample(GLYPH_LIBRARY_58F5DBD5, x7 + x9)
        x16 = [ONE] if x3 == x5 else [ONE, x5 - x3 + ONE]
        x17 = [ONE] if x4 == x6 else [ONE, x6 - x4 + ONE]
        x18 = choice(tuple(x16))
        x19 = choice(tuple(x17))
        x20 = tuple(
            (x18 + SIX * x21, x19 + SIX * x22)
            for x21 in range(x1)
            for x22 in range(x2)
        )
        x21 = tuple(
            (ONE + SIX * x22, ONE + SIX * x23)
            for x22 in range(x1)
            for x23 in range(x2)
        )
        x22 = x18 - ONE
        x23 = x19 - ONE
        x24 = x22 + x3 - ONE
        x25 = x23 + x4 - ONE
        x26 = _choose_glyph_positions_58f5dbd5(x5, x6, (x22, x23, x24, x25), x7 + x9)
        if x26 is None:
            continue
        x27 = canvas(x10, (x5, x6))
        x28 = canvas(x10, (x3, x4))
        for x29, x30 in zip(x13, x20):
            x31 = recolor(x29, shift(BIG_BLOCK_PATCH_58F5DBD5, x30))
            x27 = paint(x27, x31)
        for x32, x33, x34 in zip(combine(x13, x14), x15, x26):
            x35 = recolor(x32, shift(x33, x34))
            x27 = paint(x27, x35)
        for x36, x37, x38 in zip(x13, x15[:x7], x21):
            x39 = _render_large_tile_58f5dbd5(x36, x37, x38)
            x28 = paint(x28, x39)
        if verify_58f5dbd5(x27) != x28:
            continue
        return {"input": x27, "output": x28}
