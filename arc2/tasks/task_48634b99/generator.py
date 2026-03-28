from arc2.core import *

from .verifier import verify_48634b99


Bar48634b99 = tuple[str, int, int, int]
GRID_SHAPE_48634B99 = (16, 16)
SOURCE_LENGTHS_48634B99 = (TWO, FOUR, SIX, EIGHT)
STRUCTURAL_LENGTHS_48634B99 = (FOUR, SIX, EIGHT, TEN)
NOISE_BOUNDS_48634B99 = (FIVE, EIGHT)
MAX_PLACEMENT_TRIES_48634B99 = 400


def _bar_cells_48634b99(top: int, col: int, length: int) -> frozenset[tuple[int, int]]:
    return frozenset((i, col) for i in range(top, top + length))


def _can_place_48634b99(
    occupied: set[tuple[int, int]],
    top: int,
    col: int,
    length: int,
    height: int,
    width: int,
) -> bool:
    x0 = _bar_cells_48634b99(top, col, length)
    for x1 in x0:
        if x1 in occupied:
            return False
        for x2 in dneighbors(x1):
            x3, x4 = x2
            if 0 <= x3 < height and 0 <= x4 < width and x2 in occupied:
                return False
    return True


def _place_bar_48634b99(
    occupied: set[tuple[int, int]],
    length: int,
    height: int,
    width: int,
) -> tuple[int, int] | None:
    for _ in range(MAX_PLACEMENT_TRIES_48634B99):
        x0 = randint(ZERO, height - length)
        x1 = randint(ZERO, decrement(width))
        if not _can_place_48634b99(occupied, x0, x1, length, height, width):
            continue
        occupied.update(_bar_cells_48634b99(x0, x1, length))
        return (x0, x1)
    return None


def _paint_bar_48634b99(grid: Grid, top: int, col: int, length: int, value: int) -> Grid:
    return fill(grid, value, _bar_cells_48634b99(top, col, length))


def _marked_half_48634b99(top: int, length: int, marked_on_top: bool) -> tuple[int, int]:
    x0 = divide(length, TWO)
    x1 = branch(marked_on_top, top, top + length - x0)
    return x1, x0


def _render_input_48634b99(
    bars: tuple[Bar48634b99, ...],
    marked_on_top: bool,
    source_length: int,
) -> Grid:
    x0 = canvas(SEVEN, GRID_SHAPE_48634B99)
    x1 = x0
    for _, x2, x3, x4 in bars:
        x1 = _paint_bar_48634b99(x1, x2, x3, x4, EIGHT)
    x5 = extract(bars, lambda x: x[ZERO] == "source")
    x6 = x5[ONE]
    x7 = x5[TWO]
    x8, x9 = _marked_half_48634b99(x6, source_length, marked_on_top)
    x10 = fill(x1, NINE, _bar_cells_48634b99(x8, x7, x9))
    return x10


def _render_output_48634b99(
    bars: tuple[Bar48634b99, ...],
    marked_on_top: bool,
    target_length: int,
) -> Grid:
    x0 = canvas(SEVEN, GRID_SHAPE_48634B99)
    x1 = x0
    for _, x2, x3, x4 in bars:
        x1 = _paint_bar_48634b99(x1, x2, x3, x4, EIGHT)
    x5 = extract(bars, lambda x: both(equality(x[ZERO], "pure"), equality(x[THREE], target_length)))
    x6 = x5[ONE]
    x7 = x5[TWO]
    x8, x9 = _marked_half_48634b99(x6, target_length, marked_on_top)
    x10 = fill(x1, NINE, _bar_cells_48634b99(x8, x7, x9))
    return x10


def generate_48634b99(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0, x1 = GRID_SHAPE_48634B99
        x2 = choice(SOURCE_LENGTHS_48634B99)
        x3 = add(x2, TWO)
        x4 = tuple(x for x in STRUCTURAL_LENGTHS_48634B99 if x != x2)
        x5 = unifint(diff_lb, diff_ub, NOISE_BOUNDS_48634B99)
        x6: list[Bar48634b99] = [("source", ZERO, ZERO, x2)]
        x6.extend(("pure", ZERO, ZERO, x7) for x7 in x4)
        x6.extend(("noise", ZERO, ZERO, TWO) for _ in range(x5))
        x7 = sorted(x6, key=lambda x: (-x[THREE], x[ZERO] != "source"))
        x8: set[tuple[int, int]] = set()
        x9: list[Bar48634b99] = []
        x10 = True
        for x11, _, _, x12 in x7:
            x13 = _place_bar_48634b99(x8, x12, x0, x1)
            if x13 is None:
                x10 = False
                break
            x14, x15 = x13
            x9.append((x11, x14, x15, x12))
        if not x10:
            continue
        x16 = choice((T, F))
        x17 = tuple(x9)
        x18 = _render_input_48634b99(x17, x16, x2)
        x19 = _render_output_48634b99(x17, x16, x3)
        if verify_48634b99(x18) != x19:
            continue
        return {"input": x18, "output": x19}
