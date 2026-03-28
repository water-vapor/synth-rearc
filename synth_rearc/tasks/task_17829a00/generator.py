from synth_rearc.core import *


MOTIFS_17829a00 = (
    frozenset({(ZERO, ZERO)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE)}),
    frozenset({(ZERO, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (TWO, ZERO)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, TWO), (TWO, ONE), (THREE, ONE)}),
    frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE), (ONE, TWO)}),
    frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE), (ONE, TWO), (TWO, ONE)}),
    frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE), (ONE, TWO), (TWO, ZERO), (TWO, TWO)}),
    frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE), (ONE, TWO), (TWO, ONE), (THREE, ONE)}),
)

MOTIF_POOL_17829a00 = (
    MOTIFS_17829a00[ZERO],
    MOTIFS_17829a00[ZERO],
    MOTIFS_17829a00[ONE],
    MOTIFS_17829a00[TWO],
    MOTIFS_17829a00[THREE],
    MOTIFS_17829a00[FOUR],
    MOTIFS_17829a00[FIVE],
    MOTIFS_17829a00[FIVE],
    MOTIFS_17829a00[SIX],
    MOTIFS_17829a00[SEVEN],
    MOTIFS_17829a00[EIGHT],
    MOTIFS_17829a00[NINE],
    MOTIFS_17829a00[TEN],
)


def _expand_17829a00(
    patch: Indices,
    dims: IntegerTuple,
) -> Indices:
    h, w = dims
    out = set()
    for i, j in patch:
        for di in (-ONE, ZERO, ONE):
            for dj in (-ONE, ZERO, ONE):
                ni = i + di
                nj = j + dj
                if ZERO <= ni < h and ZERO <= nj < w:
                    out.add((ni, nj))
    return frozenset(out)


def _place_output_components_17829a00(
    count: int,
    top_side: bool,
    dims: IntegerTuple,
) -> tuple[Indices, ...] | None:
    h, w = dims
    blocked = frozenset()
    out = []
    for _ in range(count):
        placed = F
        motifs = list(MOTIF_POOL_17829a00)
        shuffle(motifs)
        for motif in motifs:
            mh = height(motif)
            mw = width(motif)
            base_i = ONE if top_side else subtract(subtract(h, ONE), mh)
            js = list(range(subtract(w, mw) + ONE))
            shuffle(js)
            for j in js:
                if both(flip(top_side), both(equality(mw, ONE), both(greater(mh, TWO), equality(j, subtract(w, ONE))))):
                    continue
                patch = shift(motif, (base_i, j))
                if len(intersection(patch, blocked)) > ZERO:
                    continue
                out.append(patch)
                blocked = combine(blocked, _expand_17829a00(patch, dims))
                placed = T
                break
            if placed:
                break
        if flip(placed):
            return None
    return tuple(out)


def _place_input_components_17829a00(
    output_components: tuple[Indices, ...],
    top_side: bool,
    dims: IntegerTuple,
    occupied: Indices,
) -> tuple[tuple[Indices, ...], Indices] | None:
    h, _ = dims
    blocked = frozenset()
    inputs = []
    order = list(output_components)
    shuffle(order)
    for patch in order:
        if top_side:
            limit = subtract(subtract(h, TWO), lowermost(patch))
            offsets = list(range(ONE, limit + ONE))
        else:
            limit = subtract(uppermost(patch), ONE)
            offsets = list(range(ONE, limit + ONE))
            offsets = [-value for value in offsets]
        shuffle(offsets)
        placed = F
        for di in offsets:
            shifted = shift(patch, (di, ZERO))
            if len(intersection(shifted, occupied)) > ZERO:
                continue
            if len(intersection(shifted, blocked)) > ZERO:
                continue
            inputs.append(shifted)
            occupied = combine(occupied, shifted)
            blocked = combine(blocked, _expand_17829a00(shifted, dims))
            placed = T
            break
        if flip(placed):
            return None
    return tuple(inputs), occupied


def _paint_components_17829a00(
    grid: Grid,
    color_value: int,
    components: tuple[Indices, ...],
) -> Grid:
    out = grid
    for patch in components:
        out = fill(out, color_value, patch)
    return out


def generate_17829a00(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    dims = (16, 16)
    h, _ = dims
    palette_choices = tuple(value for value in range(TEN) if value != SEVEN)
    while True:
        top_color, bottom_color = sample(palette_choices, TWO)
        top_count = unifint(diff_lb, diff_ub, (THREE, FOUR))
        bottom_count = unifint(diff_lb, diff_ub, (THREE, FIVE))
        top_output = _place_output_components_17829a00(top_count, T, dims)
        bottom_output = _place_output_components_17829a00(bottom_count, F, dims)
        if either(equality(top_output, None), equality(bottom_output, None)):
            continue
        top_input_data = _place_input_components_17829a00(top_output, T, dims, frozenset())
        if equality(top_input_data, None):
            continue
        top_input, occupied = top_input_data
        bottom_input_data = _place_input_components_17829a00(bottom_output, F, dims, occupied)
        if equality(bottom_input_data, None):
            continue
        bottom_input, _ = bottom_input_data
        gi = canvas(SEVEN, dims)
        gi = fill(gi, top_color, hfrontier(ORIGIN))
        gi = fill(gi, bottom_color, hfrontier((subtract(h, ONE), ZERO)))
        gi = _paint_components_17829a00(gi, top_color, top_input)
        gi = _paint_components_17829a00(gi, bottom_color, bottom_input)
        go = canvas(SEVEN, dims)
        go = fill(go, top_color, hfrontier(ORIGIN))
        go = fill(go, bottom_color, hfrontier((subtract(h, ONE), ZERO)))
        go = _paint_components_17829a00(go, top_color, top_output)
        go = _paint_components_17829a00(go, bottom_color, bottom_output)
        if equality(gi, go):
            continue
        return {"input": gi, "output": go}
