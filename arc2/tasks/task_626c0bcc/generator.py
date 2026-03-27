from arc2.core import *

from .helpers import (
    GRID_SHAPE_626C0BCC,
    Motif626c0bcc,
    motif_cells_626c0bcc,
    render_input_626c0bcc,
    render_output_626c0bcc,
    shift_motifs_626c0bcc,
)
from .verifier import verify_626c0bcc


def _neighbors4_626c0bcc(loc: tuple[int, int]) -> frozenset[tuple[int, int]]:
    x0, x1 = loc
    return frozenset({(x0 - ONE, x1), (x0 + ONE, x1), (x0, x1 - ONE), (x0, x1 + ONE)})


def _occupied_cells_626c0bcc(motifs: tuple[Motif626c0bcc, ...]) -> frozenset[tuple[int, int]]:
    x0 = frozenset()
    for x1 in motifs:
        x0 = x0 | motif_cells_626c0bcc(x1)
    return x0


def _normalize_motifs_626c0bcc(motifs: tuple[Motif626c0bcc, ...]) -> tuple[Motif626c0bcc, ...]:
    x0 = _occupied_cells_626c0bcc(motifs)
    x1 = min(i for i, _ in x0)
    x2 = min(j for _, j in x0)
    return shift_motifs_626c0bcc(motifs, (-x1, -x2))


def _component_count_626c0bcc(cells: frozenset[tuple[int, int]]) -> int:
    x0 = set(cells)
    x1 = ZERO
    while len(x0) > ZERO:
        x1 += ONE
        x2 = [x0.pop()]
        while len(x2) > ZERO:
            x3 = x2.pop()
            for x4 in _neighbors4_626c0bcc(x3):
                if x4 in x0:
                    x0.remove(x4)
                    x2.append(x4)
    return x1


def _bbox_626c0bcc(cells: frozenset[tuple[int, int]]) -> tuple[int, int, int, int]:
    x0 = tuple(i for i, _ in cells)
    x1 = tuple(j for _, j in cells)
    return (min(x0), max(x0), min(x1), max(x1))


def _row_counts_626c0bcc(cells: frozenset[tuple[int, int]]) -> tuple[int, ...]:
    x0 = max(i for i, _ in cells)
    return tuple(sum(ONE for i, _ in cells if i == x1) for x1 in range(x0 + ONE))


def _row_run_counts_626c0bcc(cells: frozenset[tuple[int, int]]) -> tuple[int, ...]:
    x0 = max(i for i, _ in cells)
    x1 = []
    for x2 in range(x0 + ONE):
        x3 = sorted(j for i, j in cells if i == x2)
        x4 = ZERO
        x5 = None
        for x6 in x3:
            if x5 is None or x6 != x5 + ONE:
                x4 += ONE
            x5 = x6
        x1.append(x4)
    return tuple(x1)


def _shape_ok_626c0bcc(cells: frozenset[tuple[int, int]], ncomponents: int) -> bool:
    x0, x1, x2, x3 = _bbox_626c0bcc(cells)
    if x0 != ZERO:
        return False
    x4 = x1 + ONE
    x5 = x3 - x2 + ONE
    if x4 < FOUR or x4 > SIX or x5 < FOUR or x5 > SIX:
        return False
    x6 = tuple(sorted({i for i, _ in cells}))
    if x6 != tuple(range(x4)):
        return False
    x7 = _row_counts_626c0bcc(cells)
    if len(x7) < FOUR or len(x7) > SIX:
        return False
    if x7[ZERO] > x7[ONE] or x7[ONE] < FOUR:
        return False
    if len(x7) > TWO:
        for x8 in range(TWO, len(x7) - ONE):
            if x7[x8] < x7[x8 + ONE]:
                return False
    x9 = _row_run_counts_626c0bcc(cells)
    if max(x9) > TWO or x7[-ONE] > THREE:
        return False
    x10 = _component_count_626c0bcc(cells)
    return x10 == ncomponents


def _touches_626c0bcc(
    patch: frozenset[tuple[int, int]],
    cells: frozenset[tuple[int, int]],
) -> bool:
    return any(nei in cells for loc in patch for nei in _neighbors4_626c0bcc(loc))


def _candidate_motifs_626c0bcc(
    color: int,
    occupied: frozenset[tuple[int, int]],
    require_touch: bool,
) -> tuple[Motif626c0bcc, ...]:
    x0 = []
    for x1 in range(SIX):
        for x2 in range(SIX):
            x3 = (color, x1, x2)
            x4 = motif_cells_626c0bcc(x3)
            if x4 & occupied:
                continue
            if require_touch and not _touches_626c0bcc(x4, occupied):
                continue
            x5 = occupied | x4
            x6, x7, x8, x9 = _bbox_626c0bcc(x5)
            if x7 - x6 + ONE > SIX or x9 - x8 + ONE > SIX:
                continue
            x0.append(x3)
    return tuple(x0)


def _placement_score_626c0bcc(
    occupied: frozenset[tuple[int, int]],
    motif: Motif626c0bcc,
) -> tuple[int, int, int]:
    x0 = occupied | motif_cells_626c0bcc(motif)
    x1, x2, x3, x4 = _bbox_626c0bcc(x0)
    x5 = (x2 - x1 + ONE) * (x4 - x3 + ONE)
    return (x5, x2, x4)


def _build_component_626c0bcc(colors: tuple[int, ...]) -> tuple[Motif626c0bcc, ...] | None:
    x0 = frozenset()
    x1: list[Motif626c0bcc] = []
    for x2, x3 in enumerate(colors):
        x4 = _candidate_motifs_626c0bcc(x3, x0, x2 > ZERO)
        if len(x4) == ZERO:
            return None
        x5 = sorted(x4, key=lambda motif: _placement_score_626c0bcc(x0, motif))
        x6 = min(len(x5), 18)
        x7 = choice(x5[:x6])
        x1.append(x7)
        x0 = x0 | motif_cells_626c0bcc(x7)
    return _normalize_motifs_626c0bcc(tuple(x1))


def _color_sequence_626c0bcc() -> tuple[int, ...]:
    x0 = [ONE, TWO, THREE, FOUR]
    if choice((ZERO, ONE)) == ONE:
        x0.append(choice((ONE, ONE, TWO)))
    shuffle(x0)
    return tuple(x0)


def _build_single_layout_626c0bcc(colors: tuple[int, ...]) -> tuple[Motif626c0bcc, ...] | None:
    x0 = _build_component_626c0bcc(colors)
    if x0 is None:
        return None
    x1 = _occupied_cells_626c0bcc(x0)
    if not _shape_ok_626c0bcc(x1, ONE):
        return None
    x2 = max(j for _, j in x1) + ONE
    x3 = randint(ZERO, GRID_SHAPE_626C0BCC[ONE] - x2)
    return shift_motifs_626c0bcc(x0, (ZERO, x3))


def _build_split_layout_626c0bcc(colors: tuple[int, ...]) -> tuple[Motif626c0bcc, ...] | None:
    if len(colors) != FIVE:
        return None
    x0 = choice(((THREE, TWO), (TWO, THREE)))
    x1 = _build_component_626c0bcc(colors[:x0[ZERO]])
    x2 = _build_component_626c0bcc(colors[x0[ZERO]:])
    if x1 is None or x2 is None:
        return None
    x3 = _occupied_cells_626c0bcc(x1)
    x4 = _occupied_cells_626c0bcc(x2)
    x5 = max(j for _, j in x3) + ONE
    x6 = max(j for _, j in x4) + ONE
    x7 = choice((ONE, TWO))
    if x5 + x7 + x6 > GRID_SHAPE_626C0BCC[ONE]:
        return None
    x8 = shift_motifs_626c0bcc(x1, (ZERO, ZERO))
    x9 = shift_motifs_626c0bcc(x2, (ZERO, x5 + x7))
    x10 = x8 + x9
    x11 = _occupied_cells_626c0bcc(x10)
    if not _shape_ok_626c0bcc(x11, TWO):
        return None
    return x10


def generate_626c0bcc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _color_sequence_626c0bcc()
        x1 = unifint(diff_lb, diff_ub, (ZERO, NINE))
        x2 = _build_split_layout_626c0bcc(x0) if both(equality(len(x0), FIVE), greater(x1, SIX)) else None
        x3 = x2 if x2 is not None else _build_single_layout_626c0bcc(x0)
        if x3 is None:
            continue
        x4 = render_input_626c0bcc(x3)
        x5 = render_output_626c0bcc(x3)
        if verify_626c0bcc(x4) != x5:
            continue
        return {"input": x4, "output": x5}
