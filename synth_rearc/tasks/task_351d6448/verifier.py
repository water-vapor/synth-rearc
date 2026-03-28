from synth_rearc.core import *


FRAME_ROWS_351D6448 = (ZERO, FOUR, EIGHT, 12)
FRAME_SHAPE_351D6448 = (THREE, 13)


def _extract_frames_351d6448(I: Grid) -> tuple[Grid, ...]:
    return tuple(crop(I, (row, ZERO), FRAME_SHAPE_351D6448) for row in FRAME_ROWS_351D6448)


def _shift_frame_351d6448(frame: Grid, dj: Integer) -> Grid:
    return paint(canvas(ZERO, shape(frame)), shift(asobject(frame), (ZERO, dj)))


def _predict_shift_351d6448(frames: tuple[Grid, ...]) -> Grid | None:
    width = len(frames[ZERO][ZERO])
    for dj in range(ONE, width):
        if _shift_frame_351d6448(frames[ZERO], dj) != frames[ONE]:
            continue
        if _shift_frame_351d6448(frames[ONE], dj) != frames[TWO]:
            continue
        if _shift_frame_351d6448(frames[TWO], dj) != frames[THREE]:
            continue
        return _shift_frame_351d6448(frames[THREE], dj)
    return None


def _single_run_351d6448(frame: Grid) -> tuple[Integer, Integer, Integer, Integer] | None:
    rows = []
    for i, row in enumerate(frame):
        cols = tuple(j for j, value in enumerate(row) if value != ZERO)
        if size(cols) == ZERO:
            continue
        values = {row[j] for j in cols}
        if size(values) != ONE:
            return None
        if cols != tuple(range(cols[ZERO], cols[-ONE] + ONE)):
            return None
        rows.append((i, cols[ZERO], size(cols), next(iter(values))))
    if size(rows) != ONE:
        return None
    return rows[ZERO]


def _predict_growing_bar_351d6448(frames: tuple[Grid, ...]) -> Grid | None:
    runs = tuple(_single_run_351d6448(frame) for frame in frames)
    if any(run is None for run in runs):
        return None
    row = runs[ZERO][ZERO]
    start = runs[ZERO][ONE]
    color = runs[ZERO][THREE]
    if any(run[ZERO] != row for run in runs):
        return None
    if any(run[ONE] != start for run in runs):
        return None
    if any(run[THREE] != color for run in runs):
        return None
    lengths = tuple(run[TWO] for run in runs)
    diffs = tuple(b - a for a, b in zip(lengths, lengths[ONE:]))
    if not all(diff > ZERO for diff in diffs):
        return None
    if size(set(diffs)) != ONE:
        return None
    outlen = lengths[-ONE] + diffs[ZERO]
    width = len(frames[ZERO][ZERO])
    if start + outlen > width:
        return None
    out = canvas(ZERO, shape(frames[ZERO]))
    return fill(out, color, connect((row, start), (row, start + outlen - ONE)))


def _palette_351d6448(frames: tuple[Grid, ...]) -> tuple[Integer, ...]:
    values = []
    for frame in frames:
        for row in frame:
            for value in row:
                if value != ZERO and value not in values:
                    values.append(value)
    return tuple(values)


def _indices_of_351d6448(frame: Grid, value: Integer) -> frozenset[tuple[Integer, Integer]]:
    return frozenset(
        (i, j)
        for i, row in enumerate(frame)
        for j, cell in enumerate(row)
        if cell == value
    )


def _nonzero_indices_351d6448(frame: Grid) -> frozenset[tuple[Integer, Integer]]:
    return frozenset(
        (i, j)
        for i, row in enumerate(frame)
        for j, value in enumerate(row)
        if value != ZERO
    )


def _predict_recolor_351d6448(frames: tuple[Grid, ...]) -> Grid | None:
    supports = tuple(_nonzero_indices_351d6448(frame) for frame in frames)
    if size(set(supports)) != ONE:
        return None
    support = supports[ZERO]
    palette = _palette_351d6448(frames)
    if size(palette) != TWO:
        return None
    for new_color in palette:
        old_color = other(palette, new_color)
        grown = frozenset()
        thresholds = []
        valid = True
        for frame in frames:
            new_cells = _indices_of_351d6448(frame, new_color)
            old_cells = _indices_of_351d6448(frame, old_color)
            if old_cells | new_cells != support:
                valid = False
                break
            if not grown.issubset(new_cells):
                valid = False
                break
            if size(new_cells) == ZERO:
                valid = False
                break
            threshold = max(j for _, j in new_cells)
            expected = frozenset((i, j) for i, j in support if j <= threshold)
            if new_cells != expected:
                valid = False
                break
            thresholds.append(threshold)
            grown = new_cells
        if not valid:
            continue
        diffs = tuple(b - a for a, b in zip(thresholds, thresholds[ONE:]))
        if not all(diff > ZERO for diff in diffs):
            continue
        if size(set(diffs)) != ONE:
            continue
        next_threshold = thresholds[-ONE] + diffs[ZERO]
        out = canvas(ZERO, shape(frames[ZERO]))
        out = fill(out, old_color, support)
        reveal = frozenset((i, j) for i, j in support if j <= next_threshold)
        return fill(out, new_color, reveal)
    return None


def verify_351d6448(I: Grid) -> Grid:
    x0 = _extract_frames_351d6448(I)
    x1 = _predict_shift_351d6448(x0)
    if x1 is not None:
        return x1
    x2 = _predict_growing_bar_351d6448(x0)
    if x2 is not None:
        return x2
    x3 = _predict_recolor_351d6448(x0)
    if x3 is not None:
        return x3
    raise ValueError("unsupported 351d6448 progression")
