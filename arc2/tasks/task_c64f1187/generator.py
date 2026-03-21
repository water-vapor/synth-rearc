from arc2.core import *


NONZERO_COLORS_C64F1187 = tuple(value for value in interval(TWO, TEN, ONE) if value != FIVE)
LEGEND_PATTERNS_C64F1187 = (
    ((ONE, ONE), (ONE, ONE)),
    ((ONE, ONE), (ONE, ZERO)),
    ((ONE, ONE), (ZERO, ONE)),
    ((ONE, ZERO), (ONE, ONE)),
)
GRAY_TILE_C64F1187 = canvas(FIVE, (TWO, TWO))
LATTICE_TOP_C64F1187 = SEVEN


def _paint_piece_c64f1187(
    grid: Grid,
    piece: Grid,
    origin: tuple[int, int],
) -> Grid:
    return paint(grid, shift(asobject(piece), origin))


def _output_shape_c64f1187(
    n_tile_rows: int,
    n_tile_cols: int,
) -> tuple[int, int]:
    return (THREE * n_tile_rows - ONE, THREE * n_tile_cols - ONE)


def _legend_starts_c64f1187(
    n_colors: int,
    left: int,
    gap: int,
) -> tuple[int, ...]:
    return tuple(left + k * (THREE + gap) for k in range(n_colors))


def _sample_marked_tiles_c64f1187(
    n_tile_rows: int,
    n_tile_cols: int,
    colors: tuple[int, ...],
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[tuple[int, int], int], ...]:
    x0 = tuple(product(interval(ZERO, n_tile_rows, ONE), interval(ZERO, n_tile_cols, ONE)))
    x1 = max(len(colors), (n_tile_rows * n_tile_cols) // TWO)
    x2 = unifint(diff_lb, diff_ub, (x1, n_tile_rows * n_tile_cols - ONE))
    while True:
        x3 = tuple(sample(x0, x2))
        if len({x4[ZERO] for x4 in x3}) == n_tile_rows:
            break
    x5 = list(tuple(sample(colors, len(colors))) + tuple(choice(colors) for _ in range(x2 - len(colors))))
    shuffle(x5)
    return tuple((x6, x7) for x6, x7 in zip(x3, x5))


def generate_c64f1187(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (THREE, FOUR))
    x1 = tuple(sample(NONZERO_COLORS_C64F1187, x0))
    x2 = tuple(sample(LEGEND_PATTERNS_C64F1187, x0))
    x3 = {x4: x5 for x4, x5 in zip(x1, x2)}
    x4 = choice((ONE, TWO))
    x5 = choice((ZERO, ONE))
    x6 = unifint(diff_lb, diff_ub, (ZERO, TWO))
    x7 = _legend_starts_c64f1187(x0, x6, x4)
    x8 = unifint(diff_lb, diff_ub, (THREE, FOUR))
    x9 = unifint(diff_lb, diff_ub, (FOUR, FIVE))
    x10 = _output_shape_c64f1187(x8, x9)
    x11 = unifint(diff_lb, diff_ub, (ZERO, FOUR))
    x12 = choice((TWO, THREE))
    x13 = choice((TWO, THREE))
    x14 = max(x7[-ONE] + TWO, x11 + x10[ONE] - ONE)
    x15 = astuple(LATTICE_TOP_C64F1187 + x10[ZERO] + x12, x14 + x13 + ONE)
    x16 = _sample_marked_tiles_c64f1187(x8, x9, x1, diff_lb, diff_ub)

    gi = canvas(ZERO, x15)
    for x17, x18, x19 in zip(x1, x2, x7):
        gi = fill(gi, x17, initset((x5, x19)))
        gi = _paint_piece_c64f1187(gi, x18, (x5 + ONE, x19 + ONE))

    for x20 in range(x8):
        for x21 in range(x9):
            x22 = (LATTICE_TOP_C64F1187 + THREE * x20, x11 + THREE * x21)
            gi = _paint_piece_c64f1187(gi, GRAY_TILE_C64F1187, x22)

    go = canvas(ZERO, x10)
    for x23, x24 in x16:
        x25, x26 = x23
        x27 = (LATTICE_TOP_C64F1187 + THREE * x25, x11 + THREE * x26)
        x28 = (THREE * x25, THREE * x26)
        gi = fill(gi, x24, initset(add(x27, UNITY)))
        go = _paint_piece_c64f1187(go, replace(x3[x24], ONE, x24), x28)

    return {"input": gi, "output": go}
