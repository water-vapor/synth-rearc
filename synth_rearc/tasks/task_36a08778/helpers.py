from synth_rearc.core import *


def row_runs_36a08778(
    row: tuple[Integer, ...],
) -> tuple[tuple[Integer, Integer], ...]:
    out = []
    j = ZERO
    w = len(row)
    while j < w:
        if row[j] == TWO:
            k = j
            while k < w and row[k] == TWO:
                k += ONE
            out.append((j, k - ONE))
            j = k
        else:
            j += ONE
    return tuple(out)


def row_gap_components_36a08778(
    runs: tuple[tuple[Integer, Integer], ...],
) -> tuple[tuple[tuple[Integer, Integer], ...], ...]:
    if len(runs) == ZERO:
        return ()
    out = [[runs[ZERO]]]
    for run in runs[ONE:]:
        prev = out[-ONE][-ONE]
        if run[ZERO] - prev[ONE] - ONE == ONE:
            out[-ONE].append(run)
        else:
            out.append([run])
    return tuple(tuple(component) for component in out)


def row_hit_36a08778(
    row: tuple[Integer, ...],
    col: Integer,
    ignore_run: tuple[Integer, Integer] | None = None,
) -> tuple[str, Integer, Integer] | None:
    x0 = row_runs_36a08778(row)
    x1 = tuple(run for run in x0 if run != ignore_run)
    for x2, x3 in x1:
        if x2 <= col <= x3:
            return ("solid", x2, x3)
    x4 = row_gap_components_36a08778(x1)
    x5 = len(row) - ONE
    for x6 in x4:
        x7 = x6[ZERO][ZERO]
        x8 = x6[-ONE][ONE]
        if x7 <= col <= x8 and x7 > ZERO and x8 < x5:
            return ("gap", x7, x8)
    return None


def seed_fronts_36a08778(
    I: Grid,
) -> tuple[tuple[Integer, Integer], ...]:
    h, w = shape(I)
    out = []
    for j in range(w):
        if I[ZERO][j] != SIX:
            continue
        i = ZERO
        while i + ONE < h and I[i + ONE][j] == SIX:
            i += ONE
        out.append((j, i + ONE))
    return tuple(out)


def trace_guides_36a08778(
    I: Grid,
) -> Grid:
    h, w = shape(I)
    out = [list(row) for row in I]
    x0 = seed_fronts_36a08778(I)
    x1 = set()

    def paint_cell(i: Integer, j: Integer) -> None:
        if out[i][j] == SEVEN:
            out[i][j] = SIX

    def paint_column(col: Integer, start: Integer, stop: Integer) -> None:
        for i in range(start, stop):
            paint_cell(i, col)

    def paint_span(row: Integer, left: Integer, right: Integer) -> None:
        for j in range(left, right + ONE):
            paint_cell(row, j)

    def branch(
        col: Integer,
        start_row: Integer,
        ignore_row: Integer | None = None,
        ignore_run: tuple[Integer, Integer] | None = None,
    ) -> None:
        key = (col, start_row, ignore_row, ignore_run)
        if key in x1:
            return
        x1.add(key)
        if not (ZERO <= col < w and ZERO <= start_row < h):
            return
        row = start_row
        first = True
        while row < h:
            x2 = ignore_run if first and row == ignore_row else None
            x3 = row_hit_36a08778(I[row], col, x2)
            if x3 is None:
                paint_cell(row, col)
                row += ONE
                first = False
                continue
            kind, left, right = x3
            if kind == "solid":
                paint_column(col, start_row, row)
                spread_row = row - ONE
                if ZERO <= spread_row < h:
                    x4 = max(ZERO, left - ONE)
                    x5 = min(w - ONE, right + ONE)
                    paint_span(spread_row, x4, x5)
                    if left > ZERO:
                        branch(left - ONE, spread_row + ONE, row, (left, right))
                    if right + ONE < w:
                        branch(right + ONE, spread_row + ONE, row, (left, right))
            else:
                paint_column(col, start_row, row + ONE)
                spread_row = row + ONE
                if ZERO <= spread_row < h:
                    x4 = max(ZERO, left - ONE)
                    x5 = min(w - ONE, right + ONE)
                    paint_span(spread_row, x4, x5)
                    if left > ZERO:
                        branch(left - ONE, spread_row + ONE)
                    if right + ONE < w:
                        branch(right + ONE, spread_row + ONE)
            return

    for x2, x3 in x0:
        branch(x2, x3)
    return tuple(tuple(row) for row in out)
