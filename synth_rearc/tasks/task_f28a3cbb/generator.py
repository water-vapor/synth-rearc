from synth_rearc.core import *

from .helpers import candidate_sources_by_landing_f28a3cbb, is_diagonal_source_f28a3cbb, landing_cell_f28a3cbb
from .verifier import verify_f28a3cbb


BG_F28A3CBB = SIX
DIMS_F28A3CBB = (NINE, NINE)
ACTIVE_COLORS_F28A3CBB = remove(BG_F28A3CBB, interval(ZERO, TEN, ONE))
TOP_LEFT_ANCHOR_F28A3CBB = frozenset((i, j) for i in range(THREE) for j in range(THREE))
BOTTOM_RIGHT_ANCHOR_F28A3CBB = shift(TOP_LEFT_ANCHOR_F28A3CBB, (SIX, SIX))


def _split_candidates_f28a3cbb(
    anchor: Patch,
    groups: dict[IntegerTuple, tuple[IntegerTuple, ...]],
) -> tuple[dict[IntegerTuple, tuple[IntegerTuple, ...]], dict[IntegerTuple, tuple[IntegerTuple, ...]]]:
    aligned = {}
    diagonal = {}
    for landing, cells in groups.items():
        aligned_cells = tuple(cell for cell in cells if not is_diagonal_source_f28a3cbb(cell, anchor))
        diagonal_cells = tuple(cell for cell in cells if is_diagonal_source_f28a3cbb(cell, anchor))
        if len(aligned_cells) > ZERO:
            aligned[landing] = aligned_cells
        if len(diagonal_cells) > ZERO:
            diagonal[landing] = diagonal_cells
    return aligned, diagonal


def _central_fragment_options_f28a3cbb(
    anchor: Patch,
    aligned: dict[IntegerTuple, tuple[IntegerTuple, ...]],
) -> tuple[tuple[IntegerTuple, ...], ...]:
    options = tuple()
    anchor_cells = toindices(anchor)
    if ulcorner(anchor_cells) == ORIGIN:
        side_groups = (
            ((0, 3), (1, 3)),
            ((1, 3), (2, 3)),
            ((0, 3), (1, 3), (2, 3)),
        )
        for group in side_groups:
            if any(landing not in aligned for landing in group):
                continue
            cols = None
            for landing in group:
                landing_cols = {cell[1] for cell in aligned[landing] if cell[0] == landing[0]}
                cols = landing_cols if cols is None else cols & landing_cols
            if cols is None:
                continue
            for col in sorted(cols):
                options = options + (tuple((landing[0], col) for landing in group),)
    else:
        side_groups = (
            ((5, 6), (5, 7)),
            ((5, 7), (5, 8)),
            ((5, 6), (5, 7), (5, 8)),
        )
        for group in side_groups:
            if any(landing not in aligned for landing in group):
                continue
            rows = None
            for landing in group:
                landing_rows = {cell[0] for cell in aligned[landing] if cell[1] == landing[1]}
                rows = landing_rows if rows is None else rows & landing_rows
            if rows is None:
                continue
            for row in sorted(rows):
                options = options + (tuple((row, landing[1]) for landing in group),)
    return options


def _sample_sources_f28a3cbb(
    anchor: Patch,
    blocked: Indices,
    min_count: Integer,
    max_count: Integer,
) -> tuple[IntegerTuple, ...] | None:
    groups = candidate_sources_by_landing_f28a3cbb(anchor, DIMS_F28A3CBB, blocked)
    if len(groups) < min_count:
        return None
    aligned, diagonal = _split_candidates_f28a3cbb(anchor, groups)
    available = tuple(sorted(groups))
    count = randint(min_count, min(max_count, len(available)))
    fragment_sources = tuple()
    fragment_landings = tuple()
    fragment_options = tuple(
        option for option in _central_fragment_options_f28a3cbb(anchor, aligned) if len(option) <= count - TWO
    )
    if len(fragment_options) > ZERO and count >= FIVE and choice((T, F)):
        fragment_sources = choice(fragment_options)
        fragment_landings = tuple(
            landing_cell_f28a3cbb(source, anchor, DIMS_F28A3CBB) for source in fragment_sources
        )
    diag_count = ZERO
    remaining_count = count - len(fragment_sources)
    if len(diagonal) > ZERO and greater(remaining_count, TWO) and choice((T, F)):
        diag_count = ONE
    diag_landings = tuple()
    if diag_count > ZERO:
        diagonal_pool = tuple(sorted(landing for landing in diagonal if landing not in fragment_landings))
        if len(diagonal_pool) > ZERO:
            diag_landings = tuple(sample(diagonal_pool, min(diag_count, len(diagonal_pool))))
    remaining_pool = tuple(
        landing for landing in available if landing not in diag_landings and landing not in fragment_landings
    )
    chosen = diag_landings + tuple(sample(remaining_pool, remaining_count - len(diag_landings)))
    sources = fragment_sources
    for landing in chosen:
        if landing in diag_landings:
            source = choice(diagonal[landing])
        elif landing in aligned:
            source = choice(aligned[landing])
        else:
            source = choice(groups[landing])
        sources = sources + (source,)
    return tuple(sorted(sources))


def _landings_f28a3cbb(
    sources: tuple[IntegerTuple, ...],
    anchor: Patch,
) -> Indices:
    result = frozenset()
    for source in sources:
        landing = landing_cell_f28a3cbb(source, anchor, DIMS_F28A3CBB)
        if landing is None:
            raise ValueError(f"failed to land f28a3cbb source {source}")
        result = combine(result, frozenset({landing}))
    return result


def generate_f28a3cbb(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        color_a, color_b = sample(ACTIVE_COLORS_F28A3CBB, TWO)
        blocked = combine(TOP_LEFT_ANCHOR_F28A3CBB, BOTTOM_RIGHT_ANCHOR_F28A3CBB)
        top_sources = _sample_sources_f28a3cbb(TOP_LEFT_ANCHOR_F28A3CBB, blocked, THREE, FIVE)
        if top_sources is None:
            continue
        blocked = combine(blocked, frozenset(top_sources))
        bottom_sources = _sample_sources_f28a3cbb(BOTTOM_RIGHT_ANCHOR_F28A3CBB, blocked, THREE, SIX)
        if bottom_sources is None:
            continue
        top_landings = _landings_f28a3cbb(top_sources, TOP_LEFT_ANCHOR_F28A3CBB)
        bottom_landings = _landings_f28a3cbb(bottom_sources, BOTTOM_RIGHT_ANCHOR_F28A3CBB)
        gi = canvas(BG_F28A3CBB, DIMS_F28A3CBB)
        gi = fill(gi, color_a, TOP_LEFT_ANCHOR_F28A3CBB)
        gi = fill(gi, color_b, BOTTOM_RIGHT_ANCHOR_F28A3CBB)
        gi = fill(gi, color_a, frozenset(top_sources))
        gi = fill(gi, color_b, frozenset(bottom_sources))
        go = canvas(BG_F28A3CBB, DIMS_F28A3CBB)
        go = fill(go, color_a, combine(TOP_LEFT_ANCHOR_F28A3CBB, top_landings))
        go = fill(go, color_b, combine(BOTTOM_RIGHT_ANCHOR_F28A3CBB, bottom_landings))
        if verify_f28a3cbb(gi) != go:
            continue
        return {"input": gi, "output": go}
