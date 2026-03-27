from arc2.core import *

from .helpers import (
    GRID_SHAPE_626C0BCC,
    MOTIF_COLORS_626C0BCC,
    Motif626c0bcc,
    motif_cells_626c0bcc,
)


def _candidate_motifs_626c0bcc(
    cells: frozenset[tuple[int, int]],
    cell: tuple[int, int],
) -> tuple[Motif626c0bcc, ...]:
    x0, x1 = cell
    x2: list[Motif626c0bcc] = []
    for x3 in range(x0 - ONE, x0 + ONE):
        for x4 in range(x1 - ONE, x1 + ONE):
            for x5 in MOTIF_COLORS_626C0BCC:
                x6 = (x5, x3, x4)
                x7 = motif_cells_626c0bcc(x6)
                if cell in x7 and x7 <= cells:
                    x2.append(x6)
    x2.sort(key=lambda motif: (motif[1], motif[2], motif[0]))
    return tuple(x2)


def _cover_motifs_626c0bcc(
    cells: frozenset[tuple[int, int]],
) -> tuple[Motif626c0bcc, ...] | None:
    if size(cells) == ZERO:
        return ()
    x0 = min(cells)
    x1 = _candidate_motifs_626c0bcc(cells, x0)
    for x2 in x1:
        x3 = motif_cells_626c0bcc(x2)
        x4 = frozenset(loc for loc in cells if loc not in x3)
        x5 = _cover_motifs_626c0bcc(x4)
        if x5 is not None:
            return (x2,) + x5
    return None


def verify_626c0bcc(I: Grid) -> Grid:
    x0 = ofcolor(I, EIGHT)
    x1 = _cover_motifs_626c0bcc(x0)
    x2 = canvas(ZERO, shape(I))
    if x1 is None:
        return x2
    x3 = x2
    for x4 in x1:
        x5 = x4[ZERO]
        x6 = motif_cells_626c0bcc(x4)
        x3 = fill(x3, x5, x6)
    return x3
