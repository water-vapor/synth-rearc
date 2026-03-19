from itertools import product as iterproduct
from typing import FrozenSet, Tuple

from arc2.core import *


ROW_STARTS_D94C3B52 = (1, 5, 9, 13)
COL_STARTS_D94C3B52 = (1, 5, 9, 13, 17, 21)
SLOT_COORDS_D94C3B52 = tuple(iterproduct(range(4), range(6)))


def _motif_patch_d94c3b52(rows: Tuple[Tuple[int, int, int], ...]) -> Indices:
    return frozenset(
        (i, j)
        for i, row in enumerate(rows)
        for j, value in enumerate(row)
        if value != ZERO
    )


PLUS_PATCH_D94C3B52 = _motif_patch_d94c3b52(((0, 1, 0), (1, 1, 1), (0, 1, 0)))
DIAMOND_PATCH_D94C3B52 = _motif_patch_d94c3b52(((1, 0, 1), (1, 1, 1), (1, 0, 1)))
X_PATCH_D94C3B52 = _motif_patch_d94c3b52(((1, 0, 1), (0, 1, 0), (1, 0, 1)))
RING_PATCH_D94C3B52 = _motif_patch_d94c3b52(((1, 1, 1), (1, 0, 1), (1, 1, 1)))
FULL_PATCH_D94C3B52 = _motif_patch_d94c3b52(((1, 1, 1), (1, 1, 1), (1, 1, 1)))
HOURGLASS_PATCH_D94C3B52 = _motif_patch_d94c3b52(((1, 1, 1), (0, 1, 0), (1, 1, 1)))
DOT_PATCH_D94C3B52 = _motif_patch_d94c3b52(((0, 0, 0), (0, 1, 0), (0, 0, 0)))
U_PATCH_D94C3B52 = _motif_patch_d94c3b52(((1, 0, 1), (1, 0, 1), (1, 1, 1)))
CHEVRON_PATCH_D94C3B52 = _motif_patch_d94c3b52(((1, 1, 0), (1, 1, 1), (0, 1, 1)))
SLASH_PATCH_D94C3B52 = _motif_patch_d94c3b52(((1, 0, 0), (1, 1, 1), (0, 0, 1)))
P_PATCH_D94C3B52 = _motif_patch_d94c3b52(((1, 1, 1), (1, 0, 1), (1, 0, 1)))
HOOK_PATCH_D94C3B52 = _motif_patch_d94c3b52(((1, 0, 1), (0, 1, 0), (0, 1, 0)))

MOTIFS_D94C3B52 = (
    PLUS_PATCH_D94C3B52,
    DIAMOND_PATCH_D94C3B52,
    X_PATCH_D94C3B52,
    RING_PATCH_D94C3B52,
    FULL_PATCH_D94C3B52,
    SLASH_PATCH_D94C3B52,
    HOURGLASS_PATCH_D94C3B52,
    DOT_PATCH_D94C3B52,
    U_PATCH_D94C3B52,
    CHEVRON_PATCH_D94C3B52,
    P_PATCH_D94C3B52,
    HOOK_PATCH_D94C3B52,
)

MOTIF_WEIGHT_MAP_D94C3B52 = {
    PLUS_PATCH_D94C3B52: 17,
    DIAMOND_PATCH_D94C3B52: 8,
    X_PATCH_D94C3B52: 8,
    RING_PATCH_D94C3B52: 7,
    FULL_PATCH_D94C3B52: 5,
    SLASH_PATCH_D94C3B52: 5,
    HOURGLASS_PATCH_D94C3B52: 4,
    DOT_PATCH_D94C3B52: 4,
    U_PATCH_D94C3B52: 4,
    CHEVRON_PATCH_D94C3B52: 4,
    P_PATCH_D94C3B52: 3,
    HOOK_PATCH_D94C3B52: 3,
}

TEMPLATE_MOTIFS_D94C3B52 = (
    PLUS_PATCH_D94C3B52,
    DIAMOND_PATCH_D94C3B52,
    X_PATCH_D94C3B52,
    RING_PATCH_D94C3B52,
    FULL_PATCH_D94C3B52,
    SLASH_PATCH_D94C3B52,
    HOURGLASS_PATCH_D94C3B52,
    U_PATCH_D94C3B52,
    CHEVRON_PATCH_D94C3B52,
    P_PATCH_D94C3B52,
    HOOK_PATCH_D94C3B52,
)


def _absolute_patch_d94c3b52(patch: Indices, slot: Tuple[int, int]) -> Indices:
    row_start = ROW_STARTS_D94C3B52[slot[ZERO]]
    col_start = COL_STARTS_D94C3B52[slot[ONE]]
    return shift(patch, (row_start, col_start))


def _between_slots_d94c3b52(template_slots: FrozenSet[Tuple[int, int]]) -> FrozenSet[Tuple[int, int]]:
    between_slots = frozenset()
    ordered_slots = tuple(template_slots)
    for index, slot_a in enumerate(ordered_slots):
        for slot_b in ordered_slots[index + ONE:]:
            same_row = slot_a[ZERO] == slot_b[ZERO]
            same_col = slot_a[ONE] == slot_b[ONE]
            if same_row or same_col:
                endpoints = frozenset({slot_a, slot_b})
                between_slots = combine(between_slots, difference(connect(slot_a, slot_b), endpoints))
    return difference(between_slots, template_slots)


def _valid_template_slots_d94c3b52(template_slots: FrozenSet[Tuple[int, int]]) -> bool:
    row_groups = {}
    col_groups = {}
    for slot in template_slots:
        row_groups.setdefault(slot[ZERO], []).append(slot[ONE])
        col_groups.setdefault(slot[ONE], []).append(slot[ZERO])
    if any(len(cols) > TWO for cols in row_groups.values()):
        return False
    if any(len(rows) > TWO for rows in col_groups.values()):
        return False
    has_row_segment = any(len(cols) == TWO and abs(cols[ZERO] - cols[ONE]) > ONE for cols in row_groups.values())
    has_col_segment = any(len(rows) == TWO and abs(rows[ZERO] - rows[ONE]) > ONE for rows in col_groups.values())
    between_slots = _between_slots_d94c3b52(template_slots)
    return both(has_row_segment, both(has_col_segment, 3 <= len(between_slots) <= 8))


def _sample_template_slots_d94c3b52(diff_lb: float, diff_ub: float) -> FrozenSet[Tuple[int, int]]:
    while True:
        count = unifint(diff_lb, diff_ub, (THREE, SIX))
        template_slots = frozenset(sample(SLOT_COORDS_D94C3B52, count))
        if _valid_template_slots_d94c3b52(template_slots):
            return template_slots


def _weighted_pool_d94c3b52(motifs: Tuple[Indices, ...]) -> Tuple[Indices, ...]:
    pool = []
    for motif in motifs:
        pool.extend(repeat(motif, MOTIF_WEIGHT_MAP_D94C3B52[motif]))
    return tuple(pool)


def generate_d94c3b52(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        template_motif = choice(TEMPLATE_MOTIFS_D94C3B52)
        template_slots = _sample_template_slots_d94c3b52(diff_lb, diff_ub)
        between_slots = _between_slots_d94c3b52(template_slots)
        distractor_count = unifint(diff_lb, diff_ub, (THREE, FIVE))
        distractor_choices = tuple(motif for motif in MOTIFS_D94C3B52 if motif != template_motif)
        distractor_motifs = tuple(sample(distractor_choices, distractor_count))
        distractor_pool = _weighted_pool_d94c3b52(distractor_motifs)
        remaining_slots = tuple(slot for slot in SLOT_COORDS_D94C3B52 if slot not in template_slots)
        slot_to_motif = {slot: template_motif for slot in template_slots}
        seeded_slots = tuple(sample(remaining_slots, distractor_count))
        for slot, motif in zip(seeded_slots, distractor_motifs):
            slot_to_motif[slot] = motif
        for slot in remaining_slots:
            if slot not in slot_to_motif:
                slot_to_motif[slot] = choice(distractor_pool)
        if not 4 <= len(set(slot_to_motif.values())) <= 6:
            continue
        marked_slot = choice(tuple(template_slots))
        gi = canvas(ZERO, (17, 25))
        go = canvas(ZERO, (17, 25))
        for slot in SLOT_COORDS_D94C3B52:
            motif = slot_to_motif[slot]
            patch = _absolute_patch_d94c3b52(motif, slot)
            input_color = EIGHT if slot == marked_slot else ONE
            output_color = ONE
            if slot in template_slots:
                output_color = EIGHT
            elif slot in between_slots:
                output_color = SEVEN
            gi = fill(gi, input_color, patch)
            go = fill(go, output_color, patch)
        if gi == go:
            continue
        return {"input": gi, "output": go}
