from arc2.core import *


COLORS = (TWO, FIVE, EIGHT, NINE)
SHAPES = (
    ("h", frozenset({(0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (2, 1)}), ONE, ONE, THREE, FOUR),
    ("h", frozenset({(0, 2), (1, 0), (1, 1), (1, 2), (1, 3), (2, 2)}), ONE, TWO, THREE, FOUR),
    ("v", frozenset({(0, 1), (1, 0), (1, 1), (1, 2), (2, 1), (3, 1)}), ONE, ONE, FOUR, THREE),
    ("v", frozenset({(0, 1), (1, 1), (2, 0), (2, 1), (2, 2), (3, 1)}), TWO, ONE, FOUR, THREE),
)


def _blank_grid() -> Grid:
    x0 = canvas(SEVEN, (11, 11))
    x1 = asindices(x0)
    x2 = box(x1)
    x3 = fill(x0, SIX, x2)
    return x3


def _placement_candidates(
    shape: tuple[str, Indices, int, int, int, int],
    occupied: Indices,
    used_rows: set[int],
    used_cols: set[int],
) -> list[tuple[Indices, int, int]]:
    kind, patch, row_offset, col_offset, height, width = shape
    cands = []
    for i in range(1, 11 - height):
        for j in range(1, 11 - width):
            main_row = i + row_offset
            main_col = j + col_offset
            if kind == "h":
                if main_row in used_rows or main_col == FIVE:
                    continue
            else:
                if main_col in used_cols or main_row == FIVE:
                    continue
            placed = shift(patch, (i, j))
            if len(intersection(placed, occupied)) != ZERO:
                continue
            cands.append((placed, main_row, main_col))
    return cands


def generate_689c358e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        gi = _blank_grid()
        occupied = frozenset({})
        used_rows: set[int] = set()
        used_cols: set[int] = set()
        placements = []
        failed = False
        for color in sample(COLORS, FOUR):
            shape = choice(SHAPES)
            cands = _placement_candidates(shape, occupied, used_rows, used_cols)
            if len(cands) == ZERO:
                failed = True
                break
            placed, main_row, main_col = choice(cands)
            kind = shape[0]
            gi = fill(gi, color, placed)
            occupied = combine(occupied, placed)
            placements.append((color, kind, main_row, main_col))
            if kind == "h":
                used_rows.add(main_row)
            else:
                used_cols.add(main_col)
        if failed:
            continue
        kinds = {kind for _, kind, _, _ in placements}
        if len(kinds) != TWO:
            continue
        go = gi
        for color, kind, main_row, main_col in placements:
            if kind == "h":
                near = (main_row, TEN) if main_col > FIVE else (main_row, ZERO)
                far = (main_row, ZERO) if main_col > FIVE else (main_row, TEN)
            else:
                near = (TEN, main_col) if main_row > FIVE else (ZERO, main_col)
                far = (ZERO, main_col) if main_row > FIVE else (TEN, main_col)
            go = fill(go, color, initset(near))
            go = fill(go, ZERO, initset(far))
        return {"input": gi, "output": go}
