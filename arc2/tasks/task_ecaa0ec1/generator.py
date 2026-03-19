from arc2.core import *

from .verifier import verify_ecaa0ec1


CORNER_OFFSETS_ECAA0EC1 = (
    ORIGIN,
    (ZERO, TWO),
    TWO_BY_TWO,
    (TWO, ZERO),
)
CORNER_DIRECTIONS_ECAA0EC1 = (
    (NEG_ONE, NEG_ONE),
    (NEG_ONE, ONE),
    (ONE, ONE),
    (ONE, NEG_ONE),
)
MOTIF_CELLS_ECAA0EC1 = asindices(canvas(ZERO, THREE_BY_THREE))


def _rotate_motif_ecaa0ec1(
    motif: Grid,
    turns: Integer,
) -> Grid:
    if turns == ZERO:
        return motif
    if turns == ONE:
        return rot90(motif)
    if turns == TWO:
        return rot180(motif)
    return rot270(motif)


def _corner_cell_ecaa0ec1(
    anchor: IntegerTuple,
    corner_idx: Integer,
) -> IntegerTuple:
    return add(anchor, CORNER_OFFSETS_ECAA0EC1[corner_idx])


def _corner_marker_ecaa0ec1(
    anchor: IntegerTuple,
    corner_idx: Integer,
) -> IntegerTuple:
    x0 = _corner_cell_ecaa0ec1(anchor, corner_idx)
    x1 = CORNER_DIRECTIONS_ECAA0EC1[corner_idx]
    return add(x0, x1)


def _target_scatter_ecaa0ec1(
    anchor: IntegerTuple,
    corner_idx: Integer,
) -> frozenset[IntegerTuple]:
    x0 = _corner_cell_ecaa0ec1(anchor, corner_idx)
    x1 = CORNER_DIRECTIONS_ECAA0EC1[corner_idx]
    return frozenset({
        add(x0, toivec(multiply(x1[0], TWO))),
        add(x0, tojvec(multiply(x1[1], TWO))),
        add(x0, multiply(x1, TWO)),
    })


def _sample_motif_ecaa0ec1() -> Grid:
    while True:
        x0 = randint(THREE, SIX)
        x1 = frozenset(sample(totuple(MOTIF_CELLS_ECAA0EC1), x0))
        x2 = fill(canvas(EIGHT, THREE_BY_THREE), ONE, x1)
        x3 = tuple(_rotate_motif_ecaa0ec1(x2, i) for i in range(FOUR))
        if len(set(x3)) == FOUR:
            return x2


def _render_input_ecaa0ec1(
    dims: IntegerTuple,
    anchor: IntegerTuple,
    motif: Grid,
    source_idx: Integer,
    target_idx: Integer,
) -> Grid:
    x0 = canvas(ZERO, dims)
    x1 = paint(x0, shift(asobject(motif), anchor))
    x2 = fill(x1, FOUR, frozenset({_corner_marker_ecaa0ec1(anchor, source_idx)}))
    x3 = fill(x2, FOUR, _target_scatter_ecaa0ec1(anchor, target_idx))
    return x3


def _render_output_ecaa0ec1(
    dims: IntegerTuple,
    anchor: IntegerTuple,
    motif: Grid,
    source_idx: Integer,
    target_idx: Integer,
) -> Grid:
    x0 = (target_idx - source_idx) % FOUR
    x1 = _rotate_motif_ecaa0ec1(motif, x0)
    x2 = canvas(ZERO, dims)
    x3 = paint(x2, shift(asobject(x1), anchor))
    x4 = fill(x3, FOUR, frozenset({_corner_marker_ecaa0ec1(anchor, target_idx)}))
    return x4


def generate_ecaa0ec1(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = unifint(diff_lb, diff_ub, (TEN, 13))
        w = unifint(diff_lb, diff_ub, (TEN, 13))
        top = randint(TWO, h - FIVE)
        left = randint(TWO, w - FIVE)
        anchor = astuple(top, left)
        motif = _sample_motif_ecaa0ec1()
        source_idx = randint(ZERO, THREE)
        target_idx = randint(ZERO, THREE)
        if source_idx == target_idx:
            continue
        gi = _render_input_ecaa0ec1((h, w), anchor, motif, source_idx, target_idx)
        go = _render_output_ecaa0ec1((h, w), anchor, motif, source_idx, target_idx)
        if verify_ecaa0ec1(gi) != go:
            continue
        return {"input": gi, "output": go}
