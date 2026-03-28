from synth_rearc.core import *


NON_MARKER_COLORS_FBF15A0B = (ONE, TWO, THREE, FOUR, SIX, SEVEN, NINE)


def _anchor_columns_fbf15a0b(
    width_: Integer,
    parity: Integer,
) -> tuple[int, ...]:
    return tuple(range(parity, width_, TWO))


def _build_motif_fbf15a0b(
    width_: Integer,
    parity: Integer,
) -> tuple[int, ...]:
    anchors = _anchor_columns_fbf15a0b(width_, parity)
    nanchors = len(anchors)
    for _ in range(100):
        cursor = randint(ZERO, max(ZERO, nanchors - TWO))
        cells = set()
        nsegments = randint(ONE, min(THREE, max(ONE, nanchors // TWO)))
        for segidx in range(nsegments):
            if cursor > nanchors - TWO:
                break
            max_len = min(SIX, nanchors - cursor)
            seglen = randint(TWO, max_len)
            cells.update(anchors[cursor:cursor + seglen])
            cursor += seglen
            if segidx == nsegments - ONE or cursor > nanchors - TWO:
                break
            cursor += randint(ONE, min(THREE, nanchors - cursor - ONE))
        motif = tuple(sorted(cells))
        if len(motif) > ZERO:
            return motif
    return anchors


def _build_panel_fbf15a0b(
    height_: Integer,
    width_: Integer,
    color_: Integer,
    parity: Integer,
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    nmotifs = unifint(diff_lb, diff_ub, (ONE, THREE))
    motifs = tuple(_build_motif_fbf15a0b(width_, parity) for _ in range(nmotifs))
    min_rows = ONE if height_ <= FOUR else TWO
    max_rows = max(min_rows, min(height_, (double(height_) + ONE) // THREE))
    nrows = randint(min_rows, max_rows)
    rows = sorted(sample(tuple(range(height_)), nrows))
    grid = canvas(EIGHT, (height_, width_))
    for row in rows:
        motif = choice(tuple(motifs))
        patch = frozenset((row, col) for col in motif)
        grid = fill(grid, color_, patch)
    return grid


def _marker_patch_fbf15a0b(
    height_: Integer,
    width_: Integer,
    axis: str,
    selected_side: str,
    orth_side: str,
) -> Indices:
    if axis == "horizontal":
        rows = (ZERO, TWO) if selected_side == "top" else (height_ - THREE, height_ - ONE)
        col = ZERO if orth_side == "left" else width_ - ONE
        return frozenset((row, col) for row in rows)
    row = ZERO if orth_side == "top" else height_ - ONE
    cols = (ZERO, TWO) if selected_side == "left" else (width_ - THREE, width_ - ONE)
    return frozenset((row, col) for col in cols)


def _sample_dimensions_fbf15a0b(
    axis: str,
    diff_lb: float,
    diff_ub: float,
) -> IntegerTuple:
    if axis == "horizontal":
        return (
            unifint(diff_lb, diff_ub, (FOUR, 15)),
            unifint(diff_lb, diff_ub, (FOUR, 30)),
        )
    return (
        unifint(diff_lb, diff_ub, (FOUR, 30)),
        unifint(diff_lb, diff_ub, (FOUR, 15)),
    )


def generate_fbf15a0b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        axis = choice(("horizontal", "vertical"))
        height_, width_ = _sample_dimensions_fbf15a0b(axis, diff_lb, diff_ub)
        color_ = choice(NON_MARKER_COLORS_FBF15A0B)
        parity = choice((ZERO, ONE))
        output = _build_panel_fbf15a0b(height_, width_, color_, parity, diff_lb, diff_ub)
        distractor = _build_panel_fbf15a0b(height_, width_, color_, parity, diff_lb, diff_ub)
        if distractor == output:
            continue
        if axis == "horizontal":
            selected_side = choice(("top", "bottom"))
            orth_side = choice(("left", "right"))
        else:
            selected_side = choice(("left", "right"))
            orth_side = choice(("top", "bottom"))
        marker_patch = _marker_patch_fbf15a0b(height_, width_, axis, selected_side, orth_side)
        output = fill(output, EIGHT, marker_patch)
        row_counts = tuple(sum(value == color_ for value in row) for row in output)
        nonzero_row_counts = tuple(count for count in row_counts if count > ZERO)
        if colorcount(output, color_) < TWO:
            continue
        if len(nonzero_row_counts) == ZERO:
            continue
        if min(nonzero_row_counts) < TWO:
            continue
        selected_half = fill(output, FIVE, marker_patch)
        if axis == "horizontal":
            input_ = vconcat(selected_half, distractor) if selected_side == "top" else vconcat(distractor, selected_half)
        else:
            input_ = hconcat(selected_half, distractor) if selected_side == "left" else hconcat(distractor, selected_half)
        return {"input": input_, "output": output}
