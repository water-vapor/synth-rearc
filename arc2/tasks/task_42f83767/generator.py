from arc2.core import *


GRID_HEIGHT_42F83767 = 15
PALETTE_COLORS_42F83767 = (ONE, TWO, THREE, FOUR, EIGHT)
SEGMENT_LIBRARY_42F83767 = (
    ("top", "bottom", "ul", "ll", "ur", "lr"),
    ("top", "mid", "bottom", "ul", "ll"),
    ("top", "mid", "bottom", "ur", "lr"),
    ("top", "bottom", "center"),
    ("mid", "ul", "ll", "ur", "lr"),
    ("top", "ur", "lr"),
    ("top", "mid", "bottom", "ur", "ll"),
    ("top", "mid", "bottom", "ul", "lr"),
    ("top", "bottom", "ul", "ll", "center"),
    ("top", "bottom", "ur", "lr", "center"),
    ("top", "mid", "bottom", "ul", "lr", "center"),
    ("top", "mid", "bottom", "ul", "ll", "ur", "lr"),
)


def _glyph_from_segments_42f83767(size_: int, segments: tuple[str, ...]) -> Indices:
    x0 = set()
    x1 = size_ // TWO
    if "top" in segments:
        x0 |= {(ZERO, j) for j in range(size_)}
    if "mid" in segments:
        x0 |= {(x1, j) for j in range(size_)}
    if "bottom" in segments:
        x0 |= {(decrement(size_), j) for j in range(size_)}
    if "ul" in segments:
        x0 |= {(i, ZERO) for i in range(x1 + ONE)}
    if "ll" in segments:
        x0 |= {(i, ZERO) for i in range(x1, size_)}
    if "ur" in segments:
        x0 |= {(i, decrement(size_)) for i in range(x1 + ONE)}
    if "lr" in segments:
        x0 |= {(i, decrement(size_)) for i in range(x1, size_)}
    if "center" in segments:
        x0 |= {(i, x1) for i in range(size_)}
    return frozenset(x0)


def _sample_glyphs_42f83767(num_colors: int, glyph_size: int) -> tuple[Indices, ...]:
    x0 = list(SEGMENT_LIBRARY_42F83767)
    shuffle(x0)
    x1 = []
    x2 = set()
    for x3 in x0:
        x4 = _glyph_from_segments_42f83767(glyph_size, x3)
        x5 = tuple(sorted(x4))
        if x5 in x2:
            continue
        x1.append(x4)
        x2.add(x5)
        if len(x1) == num_colors:
            break
    return tuple(x1)


def _build_matrix_42f83767(colors: tuple[int, ...], size_: int) -> Grid:
    x0 = len(colors)
    for _ in range(24):
        x1 = randint(ZERO, TWO)
        x2 = randint(ZERO, decrement(x0))
        x3 = randint(ONE, decrement(x0)) if x0 > ONE else ONE
        x4 = choice((ZERO, THREE, FOUR))
        x5 = choice(colors)
        x6 = []
        for x7 in range(size_):
            x8 = tuple(colors[(x2 + x7 * x3 + j) % x0] for j in range(size_))
            if x1 == ONE and x7 % TWO == ONE:
                x8 = x8[::-1]
            elif x1 == TWO:
                x9 = min(x7, decrement(size_) - x7)
                x8 = tuple(colors[(x2 + x9 + j) % x0] for j in range(size_))
            if x4 and x7 % x4 == decrement(x4):
                x8 = tuple(x5 for _ in range(size_))
            x6.append(x8)
        x10 = tuple(x6)
        if palette(x10) == set(colors):
            return x10
    return tuple(tuple(colors[(i + j) % x0] for j in range(size_)) for i in range(size_))


def _render_output_42f83767(
    matrix: Grid,
    glyph_map: dict[int, Indices],
    glyph_size: int,
) -> Grid:
    x0 = canvas(ZERO, (height(matrix) * glyph_size, width(matrix) * glyph_size))
    x1 = x0
    for i, x2 in enumerate(matrix):
        for j, x3 in enumerate(x2):
            x4 = shift(glyph_map[x3], (i * glyph_size, j * glyph_size))
            x1 = fill(x1, x3, x4)
    return x1


def generate_42f83767(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (TWO, FOUR))
    x1 = tuple(sample(PALETTE_COLORS_42F83767, x0))
    x2 = min(SIX, (31 - FOUR * x0) // x0)
    x3 = unifint(diff_lb, diff_ub, (THREE, x2))
    x4 = min(SEVEN, 30 // x3, 14 - x3)
    x5 = unifint(diff_lb, diff_ub, (FOUR, x4))
    x6 = _sample_glyphs_42f83767(x0, x3)
    x7 = dict(zip(x1, x6))
    x8 = _build_matrix_42f83767(x1, x5)
    x9 = multiply(THREE, x0)
    x10 = x0 * x3 + decrement(x0)
    x11 = randint(add(x3, ONE), GRID_HEIGHT_42F83767 - x5)
    x12 = randint(TWO, FIVE)
    x13 = max(add(x9, x10), add(x12, x5))
    x14 = canvas(ZERO, (GRID_HEIGHT_42F83767, x13))
    x15 = x14
    for x16, x17 in enumerate(x1):
        x18 = multiply(THREE, x16)
        x19 = frozenset((i, j) for i in range(TWO) for j in range(x18, x18 + TWO))
        x15 = fill(x15, x17, x19)
    for x20, x21 in enumerate(x6):
        x22 = add(x9, multiply(x20, add(x3, ONE)))
        x23 = shift(x21, (ZERO, x22))
        x15 = fill(x15, FIVE, x23)
    for i, x24 in enumerate(x8):
        for j, x25 in enumerate(x24):
            x26 = frozenset({(x11 + i, x12 + j)})
            x15 = fill(x15, x25, x26)
    x27 = _render_output_42f83767(x8, x7, x3)
    return {"input": x15, "output": x27}
