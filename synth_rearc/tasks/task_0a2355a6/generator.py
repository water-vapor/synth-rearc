from synth_rearc.core import *

from .helpers import (
    PIECE_TRANSFORMS_0a2355a6,
    MOTIF_BANK_0a2355a6,
    color_for_holes_0a2355a6,
    crop_pair_0a2355a6,
    transformed_patch_0a2355a6,
)


HOLE_BAG_0a2355a6 = (
    ONE,
    ONE,
    ONE,
    ONE,
    TWO,
    TWO,
    THREE,
    FOUR,
)


def _pick_counts_0a2355a6(nobj: Integer) -> tuple[Integer, ...]:
    while True:
        counts = tuple(choice(HOLE_BAG_0a2355a6) for _ in range(nobj))
        if maximum(counts) == ONE:
            continue
        if counts.count(FOUR) > ONE:
            continue
        return counts


def _pick_patch_0a2355a6(nholes: Integer) -> Patch:
    x0 = choice(MOTIF_BANK_0a2355a6[nholes])
    x1 = transformed_patch_0a2355a6(x0)
    return x1


def generate_0a2355a6(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        nobj = unifint(diff_lb, diff_ub, (THREE, FOUR))
        counts = _pick_counts_0a2355a6(nobj)
        patches = tuple(_pick_patch_0a2355a6(nholes) for nholes in counts)
        if nobj == THREE:
            row_sizes = choice(((TWO, ONE), (ONE, TWO)))
        else:
            row_sizes = (TWO, TWO)
        rows = []
        start = ZERO
        for cnt in row_sizes:
            stop = start + cnt
            rows.append(tuple(zip(counts[start:stop], patches[start:stop])))
            start = stop
        top = randint(ZERO, ONE)
        left_margin = randint(ZERO, ONE)
        placements = []
        width_ub = ZERO
        for row in rows:
            rowh = max(height(patch) for _, patch in row)
            left = left_margin + randint(ZERO, ONE)
            for nholes, patch in row:
                slack = rowh - height(patch)
                voff = randint(ZERO, slack) if positive(slack) else ZERO
                placements.append((nholes, patch, (top + voff, left)))
                left += width(patch) + unifint(diff_lb, diff_ub, (ONE, THREE))
            width_ub = max(width_ub, left)
            top += rowh + unifint(diff_lb, diff_ub, (ONE, THREE))
        height_ub = top + randint(ZERO, ONE)
        width_ub += randint(ZERO, ONE)
        if greater(height_ub, 20) or greater(width_ub, 20):
            continue
        gi = canvas(ZERO, (height_ub, width_ub))
        go = canvas(ZERO, (height_ub, width_ub))
        reserved = frozenset()
        failed = F
        for nholes, patch, loc in placements:
            placed = shift(patch, loc)
            halo = backdrop(outbox(placed))
            if size(intersection(reserved, halo)) != ZERO:
                failed = T
                break
            reserved = combine(reserved, halo)
            gi = fill(gi, EIGHT, placed)
            go = fill(go, color_for_holes_0a2355a6(nholes), placed)
        if failed:
            continue
        transform = choice(PIECE_TRANSFORMS_0a2355a6)
        gi = transform(gi)
        go = transform(go)
        gi, go = crop_pair_0a2355a6(gi, go)
        if not (NINE <= height(gi) <= 17 and 11 <= width(gi) <= 18):
            continue
        if size(objects(gi, T, F, T)) != nobj:
            continue
        return {"input": gi, "output": go}
