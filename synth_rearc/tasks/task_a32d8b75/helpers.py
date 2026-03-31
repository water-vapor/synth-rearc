from synth_rearc.core import *


ROTATORS_A32D8B75 = (
    identity,
    rot90,
    rot180,
    rot270,
)


def crop_nonzero_a32d8b75(
    grid: Grid,
) -> tuple[Grid, IntegerTuple]:
    coords = [(i, j) for i, row in enumerate(grid) for j, value in enumerate(row) if value != ZERO]
    imin = min(i for i, _ in coords)
    imax = max(i for i, _ in coords)
    jmin = min(j for _, j in coords)
    jmax = max(j for _, j in coords)
    piece = tuple(tuple(row[jmin : jmax + ONE]) for row in grid[imin : imax + ONE])
    return piece, (imin, jmin)


def split_panels_a32d8b75(
    grid: Grid,
) -> tuple[Grid, ...]:
    h = height(grid)
    dividers = [j for j in range(width(grid)) if all(grid[i][j] == SIX for i in range(h))]
    starts = [ZERO] + [j + ONE for j in dividers]
    ends = dividers + [width(grid)]
    return tuple(tuple(tuple(row[a:b]) for row in grid) for a, b in zip(starts, ends))


def main_and_cues_a32d8b75(
    grid: Grid,
) -> tuple[Grid, tuple[Grid, ...]]:
    panels = split_panels_a32d8b75(grid)
    main_index = max(range(len(panels)), key=lambda idx: width(panels[idx]))
    main_panel = panels[main_index]
    cue_panels = tuple(panel for idx, panel in enumerate(panels) if idx != main_index)
    return main_panel, cue_panels


def split_pieces_a32d8b75(
    panel: Grid,
) -> tuple[tuple[IntegerTuple, Grid], ...]:
    normalized = replace(panel, SIX, ZERO)
    rows = [i for i, row in enumerate(normalized) if any(value != ZERO for value in row)]
    start = rows[ZERO]
    prev = rows[ZERO]
    chunks = []
    for row_index in rows[ONE:]:
        if row_index > prev + ONE:
            chunks.append((start, prev))
            start = row_index
        prev = row_index
    chunks.append((start, prev))
    pieces = []
    for top, bottom in chunks:
        chunk = tuple(normalized[top : bottom + ONE])
        piece, offset = crop_nonzero_a32d8b75(chunk)
        pieces.append(((top + offset[ZERO], offset[ONE]), piece))
    return tuple(pieces)


def swap_motif_a32d8b75(
    motif: Grid,
) -> Grid:
    colors = sorted({value for row in motif for value in row if value != ZERO})
    a, b = colors
    return tuple(
        tuple(b if value == a else a if value == b else value for value in row)
        for row in motif
    )


def stencil_mask_a32d8b75(
    stencil: Grid,
) -> Grid:
    return tuple(tuple(ONE if value != ZERO else ZERO for value in row) for row in stencil)


def cue_corner_a32d8b75(
    cue_pieces: tuple[tuple[IntegerTuple, Grid], ...],
) -> Integer:
    (offset0, piece0), (offset1, piece1) = cue_pieces
    if FOUR in palette(piece0):
        four_offset = offset0
        seven_offset = offset1
        seven_piece = piece1
    else:
        four_offset = offset1
        seven_offset = offset0
        seven_piece = piece0
    leftmost_col = min(four_offset[ONE], seven_offset[ONE])
    four_left = four_offset[ONE] == leftmost_col
    vertical = height(seven_piece) > width(seven_piece)
    if vertical:
        return ZERO if four_left else TWO
    return THREE if four_left else ONE


def cue_turn_a32d8b75(
    corner: Integer,
    cue_count: Integer,
) -> Integer:
    if cue_count > ONE:
        return (corner + TWO) % FOUR
    return corner


def stamp_dims_a32d8b75(
    motif: Grid,
    stencil_mask: Grid,
    turn: Integer,
) -> IntegerTuple:
    transformed = ROTATORS_A32D8B75[turn](stencil_mask)
    return (height(transformed) * height(motif), width(transformed) * width(motif))


def stamp_bounds_a32d8b75(
    base: Grid,
    motif: Grid,
    stencil_mask: Grid,
    corner: Integer,
    turn: Integer,
) -> tuple[Integer, Integer, Integer, Integer]:
    stamp_h, stamp_w = stamp_dims_a32d8b75(motif, stencil_mask, turn)
    h, w = shape(base)
    top = ZERO if corner in (ZERO, ONE) else h - stamp_h
    left = ZERO if corner in (ZERO, THREE) else w - stamp_w
    return (top, left, top + stamp_h, left + stamp_w)


def apply_stamp_a32d8b75(
    base: Grid,
    motif: Grid,
    stencil_mask: Grid,
    corner: Integer,
    turn: Integer,
) -> Grid:
    transformed = ROTATORS_A32D8B75[turn](stencil_mask)
    base_h, base_w = shape(base)
    motif_h, motif_w = shape(motif)
    stencil_h, stencil_w = shape(transformed)
    top = ZERO if corner in (ZERO, ONE) else base_h - stencil_h * motif_h
    left = ZERO if corner in (ZERO, THREE) else base_w - stencil_w * motif_w
    motif_obj = asobject(motif)
    out = base
    for si, row in enumerate(transformed):
        for sj, value in enumerate(row):
            if value == ZERO:
                continue
            origin = (top + si * motif_h, left + sj * motif_w)
            out = paint(out, shift(motif_obj, origin))
    return out
