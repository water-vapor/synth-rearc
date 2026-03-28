from itertools import combinations

from synth_rearc.core import *


INPUT_DIMS_B1FC8B8E = (SIX, SIX)
OUTPUT_DIMS_B1FC8B8E = (FIVE, FIVE)

FULL_MOTIF_B1FC8B8E = frozenset({ORIGIN, RIGHT, DOWN, UNITY})
L_MOTIF_B1FC8B8E = frozenset({RIGHT, DOWN, UNITY})

MOTIFS_B1FC8B8E = (
    FULL_MOTIF_B1FC8B8E,
    L_MOTIF_B1FC8B8E,
)

OUTPUT_OFFSETS_B1FC8B8E = (
    ORIGIN,
    astuple(ZERO, THREE),
    astuple(THREE, ZERO),
    THREE_BY_THREE,
)


def _render_input_b1fc8b8e(
    motif: Indices,
    anchors: tuple[IntegerTuple, ...],
) -> Grid:
    gi = canvas(ZERO, INPUT_DIMS_B1FC8B8E)
    for anchor in anchors:
        gi = fill(gi, EIGHT, shift(motif, anchor))
    return gi


def _render_output_b1fc8b8e(
    motif: Indices,
) -> Grid:
    go = canvas(ZERO, OUTPUT_DIMS_B1FC8B8E)
    for offset in OUTPUT_OFFSETS_B1FC8B8E:
        go = fill(go, EIGHT, shift(motif, offset))
    return go


def _layouts_b1fc8b8e() -> tuple[tuple[Indices, tuple[IntegerTuple, ...]], ...]:
    layouts = []
    anchors = tuple((i, j) for i in range(FIVE) for j in range(FIVE))
    for motif in MOTIFS_B1FC8B8E:
        target_cells = multiply(FOUR, size(motif))
        for placement in combinations(anchors, FOUR):
            gi = _render_input_b1fc8b8e(motif, placement)
            if colorcount(gi, EIGHT) != target_cells:
                continue
            if size(objects(gi, T, F, T)) != ONE:
                continue
            layouts.append((motif, placement))
    key = lambda item: (size(item[0]), tuple(sorted(item[1])))
    return tuple(sorted(layouts, key=key))


LAYOUTS_B1FC8B8E = _layouts_b1fc8b8e()


def generate_b1fc8b8e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    motif, anchors = choice(LAYOUTS_B1FC8B8E)
    gi = _render_input_b1fc8b8e(motif, anchors)
    go = _render_output_b1fc8b8e(motif)
    return {"input": gi, "output": go}
