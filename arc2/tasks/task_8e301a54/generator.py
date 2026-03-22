from arc2.core import *


GRID_SHAPE = (10, 10)
BACKGROUND = SEVEN


def _patch(cells: tuple[tuple[int, int], ...]) -> Indices:
    return frozenset(cells)


def _variants(patch: Indices) -> tuple[Indices, ...]:
    variants = []
    candidates = (
        patch,
        hmirror(patch),
        vmirror(patch),
        dmirror(patch),
        cmirror(patch),
        hmirror(dmirror(patch)),
        vmirror(dmirror(patch)),
        hmirror(cmirror(patch)),
    )
    for candidate in candidates:
        normalized = normalize(candidate)
        if normalized not in variants:
            variants.append(normalized)
    return tuple(variants)


def _shifted(patch: Indices) -> Indices:
    return shift(patch, toivec(size(patch)))


def _visible(patch: Indices) -> Indices:
    h, w = GRID_SHAPE
    return frozenset((i, j) for i, j in patch if 0 <= i < h and 0 <= j < w)


def _reserve(patch: Indices) -> Indices:
    return combine(patch, mapply(neighbors, patch))


H2 = _patch(((0, 0), (0, 1)))
H3 = _patch(((0, 0), (0, 1), (0, 2)))
V2 = _patch(((0, 0), (1, 0)))
V3 = _patch(((0, 0), (1, 0), (2, 0)))
V4 = _patch(((0, 0), (1, 0), (2, 0), (3, 0)))
PLUS5 = _patch(((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)))
L3 = _patch(((0, 0), (0, 1), (1, 1)))
L4 = _patch(((0, 0), (0, 1), (0, 2), (1, 2)))
L5 = _patch(((0, 0), (0, 1), (0, 2), (0, 3), (1, 3)))

TWO_PATCHES = (
    H2,
    H2,
    H3,
    H3,
    V2,
    V2,
    V3,
    V3,
    PLUS5,
)
FIVE_PATCHES = (
    _patch(((0, 0),)),
    _patch(((0, 0),)),
    _patch(((0, 0),)),
    V2,
    V2,
    V3,
)
NINE_PATCHES = (
    H2,
    H2,
    H3,
    H3,
    V3,
    V4,
    *_variants(L3),
    *_variants(L4),
    *_variants(L5),
)

PATCH_OPTIONS = {
    TWO: TWO_PATCHES,
    FIVE: FIVE_PATCHES,
    NINE: NINE_PATCHES,
}

SLOT_STARTS = {
    ZERO: (ZERO, THREE),
    ONE: (TWO, FIVE),
    TWO: (SIX, NINE),
}


def _row_bounds(color: int, patch: Indices) -> tuple[int, int]:
    amount = size(patch)
    if color == FIVE:
        lo = max(amount, THREE)
        hi = NINE
    else:
        lo = max(amount + ONE, FOUR)
        hi = EIGHT
    return lo, hi


def _candidates(
    color: int,
    patch: Indices,
    slot: int,
    input_reserved: Indices,
    output_reserved: Indices,
) -> list[tuple[Indices, Indices]]:
    candidates = []
    h, w = shape(patch)
    row_lo, row_hi = _row_bounds(color, patch)
    col_lo, col_hi = SLOT_STARTS[slot]
    for out_top in range(row_lo, row_hi + ONE):
        in_top = out_top - size(patch)
        if in_top < ZERO or in_top + h > GRID_SHAPE[0]:
            continue
        for start_col in range(col_lo, col_hi + ONE):
            if start_col < ZERO or start_col + w > GRID_SHAPE[1]:
                continue
            placed = shift(patch, (in_top, start_col))
            if len(intersection(placed, input_reserved)) > ZERO:
                continue
            shifted = _shifted(placed)
            visible = _visible(shifted)
            if len(visible) == ZERO:
                continue
            if len(intersection(visible, output_reserved)) > ZERO:
                continue
            candidates.append((placed, visible))
    return candidates


def generate_8e301a54(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        gi = canvas(BACKGROUND, GRID_SHAPE)
        go = canvas(BACKGROUND, GRID_SHAPE)
        slot_order = sample((ZERO, ONE, TWO), THREE)
        color_order = sample((TWO, FIVE, NINE), THREE)
        chosen = {color: choice(PATCH_OPTIONS[color]) for color in (TWO, FIVE, NINE)}
        placements = {}
        input_reserved = frozenset({})
        output_reserved = frozenset({})
        failed = F

        for color in order(color_order, lambda value: -size(chosen[value])):
            patch = chosen[color]
            slot = slot_order[color_order.index(color)]
            options = _candidates(color, patch, slot, input_reserved, output_reserved)
            if len(options) == ZERO:
                failed = T
                break
            placed, visible = choice(options)
            placements[color] = placed
            input_reserved = combine(input_reserved, _reserve(placed))
            output_reserved = combine(output_reserved, visible)

        if failed:
            continue

        for color in (TWO, FIVE, NINE):
            patch = placements[color]
            gi = fill(gi, color, patch)
            go = fill(go, color, _shifted(patch))

        if gi == go:
            continue
        return {"input": gi, "output": go}
