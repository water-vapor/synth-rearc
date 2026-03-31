from __future__ import annotations

from synth_rearc.core import *

from .helpers import (
    BG_DD6B8C4B,
    CENTER_DD6B8C4B,
    FRAME_DD6B8C4B,
    MARK_DD6B8C4B,
    WALL_DD6B8C4B,
    analyze_structure_dd6b8c4b,
    transform_grid_dd6b8c4b,
)


SCAFFOLDS_DD6B8C4B = (
    (
        "77777777777",
        "76666666777",
        "76777776777",
        "76666666777",
        "77763336777",
        "77763236777",
        "77763336777",
        "77766766667",
        "77767777767",
        "77766666667",
        "77777777777",
    ),
    (
        "77777777777",
        "77777777777",
        "77777777777",
        "77766666666",
        "77763336777",
        "77763236777",
        "77763336777",
        "77767776777",
        "77767776777",
        "77767776777",
        "77777777777",
    ),
    (
        "77777777777",
        "77777777777",
        "77777777777",
        "77777777777",
        "77773337777",
        "77773237777",
        "77773337777",
        "77777777777",
        "77777777777",
        "77777777777",
        "77777777777",
    ),
    (
        "66777777766",
        "66666666666",
        "76777777767",
        "76766766767",
        "76763336767",
        "76773237767",
        "76763336767",
        "76766766767",
        "76777777767",
        "76666666766",
        "77777777766",
    ),
    (
        "77767776777",
        "77766666777",
        "77777777777",
        "66766766667",
        "77763336777",
        "76663236766",
        "77763336777",
        "66766676667",
        "77767776777",
        "76667666766",
        "77767776777",
    ),
)

TRANSFORMS_DD6B8C4B = (identity, hmirror, vmirror, rot180)
SELECTED_SIZE_CHOICES_DD6B8C4B = (ONE, TWO, TWO, THREE, THREE, FOUR)
NOISE_SIZE_CHOICES_DD6B8C4B = (ONE, ONE, TWO, TWO, THREE, FOUR)
SELECTED_COUNT_CHOICES_DD6B8C4B = (ONE, TWO, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)
NOISE_COUNT_CHOICES_DD6B8C4B = (ZERO, ZERO, ONE, ONE, TWO, TWO, THREE, FOUR, FIVE)


def _parse_scaffold_dd6b8c4b(
    rows: tuple[str, ...],
) -> Grid:
    return tuple(tuple(int(value) for value in row) for row in rows)


def _neighbors4_dd6b8c4b(
    loc: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    return ((loc[ZERO] - ONE, loc[ONE]), (loc[ZERO] + ONE, loc[ONE]), (loc[ZERO], loc[ONE] - ONE), (loc[ZERO], loc[ONE] + ONE))


def _grow_patch_dd6b8c4b(
    pool: set[IntegerTuple],
    target: Integer,
) -> frozenset[IntegerTuple]:
    start = choice(tuple(pool))
    patch = {start}
    frontier = {nxt for nxt in _neighbors4_dd6b8c4b(start) if nxt in pool}
    while len(patch) < target and len(frontier) > ZERO:
        nxt = choice(tuple(frontier))
        frontier.remove(nxt)
        if nxt not in pool or nxt in patch:
            continue
        patch.add(nxt)
        for other in _neighbors4_dd6b8c4b(nxt):
            if other in pool and other not in patch:
                frontier.add(other)
    return frozenset(patch)


def _choose_cells_dd6b8c4b(
    cells: frozenset[IntegerTuple],
    total: Integer,
    size_choices: tuple[Integer, ...],
) -> frozenset[IntegerTuple]:
    available = set(cells)
    chosen: set[IntegerTuple] = set()
    remaining = total
    while remaining > ZERO and len(available) > ZERO:
        block_size = min(remaining, choice(size_choices))
        patch = _grow_patch_dd6b8c4b(available, block_size)
        if len(patch) == ZERO:
            break
        chosen |= patch
        available -= patch
        remaining = total - len(chosen)
    if remaining > ZERO:
        leftovers = tuple(loc for loc in cells if loc not in chosen)
        chosen |= set(sample(leftovers, min(remaining, len(leftovers))))
    return frozenset(chosen)


def _paint_cells_dd6b8c4b(
    grid: list[list[Integer]],
    cells: frozenset[IntegerTuple],
    value: Integer,
) -> None:
    for i, j in cells:
        grid[i][j] = value


def _make_input_dd6b8c4b(
    scaffold: Grid,
    selected_cells: frozenset[IntegerTuple],
    noise_cells: frozenset[IntegerTuple],
) -> Grid:
    out = [list(row) for row in scaffold]
    _paint_cells_dd6b8c4b(out, selected_cells, MARK_DD6B8C4B)
    _paint_cells_dd6b8c4b(out, noise_cells, MARK_DD6B8C4B)
    return tuple(tuple(row) for row in out)


def _sample_scaffold_dd6b8c4b() -> Grid:
    base = _parse_scaffold_dd6b8c4b(choice(SCAFFOLDS_DD6B8C4B))
    return choice(TRANSFORMS_DD6B8C4B)(base)


def _motif_cells_dd6b8c4b() -> frozenset[IntegerTuple]:
    return frozenset((i, j) for i in range(FOUR, SEVEN) for j in range(FOUR, SEVEN))


def generate_dd6b8c4b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    motif_cells = _motif_cells_dd6b8c4b()
    for _ in range(300):
        scaffold = _sample_scaffold_dd6b8c4b()
        analysis = analyze_structure_dd6b8c4b(scaffold)
        ring_cells = analysis["ring_cells"]
        base_seen = analysis["base_seen"]
        safe_noise = analysis["safe_noise"]
        selectable = frozenset(
            loc
            for loc in base_seen
            if loc not in ring_cells and loc not in motif_cells and scaffold[loc[ZERO]][loc[ONE]] == BG_DD6B8C4B
        )
        noiseable = frozenset(
            loc
            for loc in safe_noise
            if loc not in ring_cells and scaffold[loc[ZERO]][loc[ONE]] == BG_DD6B8C4B
        )
        if len(selectable) == ZERO:
            continue
        selected_total = min(choice(SELECTED_COUNT_CHOICES_DD6B8C4B), len(selectable), NINE)
        if selected_total == ZERO:
            continue
        noise_total = min(choice(NOISE_COUNT_CHOICES_DD6B8C4B), len(noiseable))
        selected_cells = _choose_cells_dd6b8c4b(selectable, selected_total, SELECTED_SIZE_CHOICES_DD6B8C4B)
        noise_cells = _choose_cells_dd6b8c4b(noiseable, noise_total, NOISE_SIZE_CHOICES_DD6B8C4B)
        gi = _make_input_dd6b8c4b(scaffold, selected_cells, noise_cells)
        go = transform_grid_dd6b8c4b(gi)
        if gi == go:
            continue
        if any(gi[i][j] not in (BG_DD6B8C4B, WALL_DD6B8C4B, FRAME_DD6B8C4B, CENTER_DD6B8C4B, MARK_DD6B8C4B) for i in range(11) for j in range(11)):
            continue
        return {"input": gi, "output": go}
    raise RuntimeError("failed to generate dd6b8c4b example")
