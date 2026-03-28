from synth_rearc.core import *

from .verifier import verify_c7d4e6ad


FG_COLORS_C7D4E6AD = remove(FIVE, remove(ZERO, interval(ZERO, TEN, ONE)))


def _neighbors4_c7d4e6ad(
    cell: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    i, j = cell
    return ((i - ONE, j), (i + ONE, j), (i, j - ONE), (i, j + ONE))


def _connected_c7d4e6ad(
    cells: frozenset[IntegerTuple],
) -> bool:
    if len(cells) == ZERO:
        return False
    pending = [next(iter(cells))]
    seen = set()
    cellset = set(cells)
    while len(pending) > ZERO:
        cell = pending.pop()
        if cell in seen:
            continue
        seen.add(cell)
        for nb in _neighbors4_c7d4e6ad(cell):
            if nb in cellset and nb not in seen:
                pending.append(nb)
    return len(seen) == len(cells)


def _flatten_rows_c7d4e6ad(
    row_cells: dict[Integer, set[Integer]],
) -> frozenset[IntegerTuple]:
    return frozenset((i, j) for i, cols in row_cells.items() for j in cols)


def _sample_row_colors_c7d4e6ad(
    rows: tuple[Integer, ...],
) -> dict[Integer, Integer]:
    nrows = len(rows)
    nblocks = min(choice((TWO, THREE, THREE, FOUR)), nrows)
    if nblocks == ONE:
        nblocks = TWO
    cuts = sorted(sample(tuple(range(ONE, nrows)), nblocks - ONE))
    bounds = (ZERO,) + tuple(cuts) + (nrows,)
    colors = sample(FG_COLORS_C7D4E6AD, nblocks)
    out = {}
    for color_value, start, stop in zip(colors, bounds, bounds[ONE:]):
        for row in rows[start:stop]:
            out[row] = color_value
    return out


def _sample_gray_shape_c7d4e6ad(
    rows: tuple[Integer, ...],
) -> frozenset[IntegerTuple]:
    left_bound = THREE
    right_bound = choice((FIVE, SIX, SEVEN))
    row_cells = {}
    prev_anchor = None
    for idx, row in enumerate(rows):
        if idx == ZERO:
            curr_anchor = randint(left_bound + ONE, right_bound)
        else:
            step = choice((-ONE, ZERO, ZERO, ONE))
            curr_anchor = max(left_bound, min(right_bound, prev_anchor + step))
        core_lo = curr_anchor if prev_anchor is None else min(prev_anchor, curr_anchor)
        core_hi = curr_anchor if prev_anchor is None else max(prev_anchor, curr_anchor)
        pad_left = choice((ZERO, ZERO, ONE))
        pad_right = choice((ZERO, ZERO, ONE))
        lo = max(left_bound, core_lo - pad_left)
        hi = min(right_bound, core_hi + pad_right)
        row_cells[row] = set(range(lo, hi + ONE))
        prev_anchor = curr_anchor
    removable_rows = list(rows[ONE:-ONE])
    shuffle(removable_rows)
    ncuts = choice((ZERO, ZERO, ONE, ONE, TWO))
    cuts_done = ZERO
    for row in removable_rows:
        if cuts_done >= ncuts or len(row_cells[row]) < THREE:
            continue
        cells = sorted(row_cells[row])[ONE:-ONE]
        shuffle(cells)
        for col in cells:
            candidate_rows = {i: set(cols) for i, cols in row_cells.items()}
            candidate_rows[row].remove(col)
            candidate = _flatten_rows_c7d4e6ad(candidate_rows)
            if _connected_c7d4e6ad(candidate):
                row_cells[row].remove(col)
                cuts_done += ONE
                break
    return _flatten_rows_c7d4e6ad(row_cells)


def generate_c7d4e6ad(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    del diff_lb, diff_ub
    while True:
        top = randint(ONE, TWO)
        bottom = randint(SEVEN, EIGHT)
        rows = tuple(range(top, bottom + ONE))
        row_colors = _sample_row_colors_c7d4e6ad(rows)
        gray = _sample_gray_shape_c7d4e6ad(rows)
        if not _connected_c7d4e6ad(gray):
            continue
        if len(gray) < len(rows) + TWO:
            continue
        if width(gray) < TWO:
            continue
        gi = canvas(ZERO, (TEN, TEN))
        for row in rows:
            gi = fill(gi, row_colors[row], frozenset({(row, ZERO)}))
        gi = fill(gi, FIVE, gray)
        go = gi
        for row in rows:
            row_gray = frozenset((i, j) for i, j in gray if i == row)
            go = fill(go, row_colors[row], row_gray)
        if gi == go:
            continue
        try:
            valid = verify_c7d4e6ad(gi) == go
        except Exception:
            valid = False
        if not valid:
            continue
        return {"input": gi, "output": go}
