from arc2.core import *


Motif626c0bcc = tuple[int, int, int]

MOTIF_SHAPES_626C0BCC: dict[int, frozenset[tuple[int, int]]] = {
    ONE: frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE)}),
    TWO: frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE)}),
    THREE: frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ONE)}),
    FOUR: frozenset({(ZERO, ZERO), (ONE, ZERO), (ONE, ONE)}),
}

MOTIF_COLORS_626C0BCC = (ONE, TWO, THREE, FOUR)
GRID_SHAPE_626C0BCC = (SEVEN, SEVEN)


def motif_cells_626c0bcc(motif: Motif626c0bcc) -> frozenset[tuple[int, int]]:
    x0, x1, x2 = motif
    x3 = MOTIF_SHAPES_626C0BCC[x0]
    return frozenset((x1 + a, x2 + b) for a, b in x3)


def shift_motifs_626c0bcc(
    motifs: tuple[Motif626c0bcc, ...],
    offset: tuple[int, int],
) -> tuple[Motif626c0bcc, ...]:
    x0, x1 = offset
    return tuple((x2, x3 + x0, x4 + x1) for x2, x3, x4 in motifs)


def render_output_626c0bcc(
    motifs: tuple[Motif626c0bcc, ...],
    dimensions: tuple[int, int] = GRID_SHAPE_626C0BCC,
) -> Grid:
    x0 = canvas(ZERO, dimensions)
    x1 = x0
    for x2 in motifs:
        x3 = x2[ZERO]
        x4 = motif_cells_626c0bcc(x2)
        x1 = fill(x1, x3, x4)
    return x1


def render_input_626c0bcc(
    motifs: tuple[Motif626c0bcc, ...],
    dimensions: tuple[int, int] = GRID_SHAPE_626C0BCC,
) -> Grid:
    x0 = canvas(ZERO, dimensions)
    x1 = x0
    for x2 in motifs:
        x3 = motif_cells_626c0bcc(x2)
        x1 = fill(x1, EIGHT, x3)
    return x1
