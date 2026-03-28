from synth_rearc.core import *


L_SHAPE_AD38A9D0 = frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ONE)})
S_SHAPE_AD38A9D0 = frozenset(
    {(ZERO, ZERO), (ZERO, ONE), (ONE, ONE), (ONE, TWO)}
)
PLUS_SHAPE_AD38A9D0 = frozenset(
    {
        (ZERO, ONE),
        (ONE, ZERO),
        (ONE, ONE),
        (ONE, TWO),
        (TWO, ONE),
    }
)
LINE_SHAPE_AD38A9D0 = frozenset({(ZERO, ZERO), (ONE, ZERO), (TWO, ZERO)})
DOMINO_SHAPE_AD38A9D0 = frozenset({(ZERO, ZERO), (ONE, ZERO)})
RECT_SHAPE_AD38A9D0 = frozenset(
    {
        (ZERO, ZERO),
        (ZERO, ONE),
        (ZERO, TWO),
        (ONE, ZERO),
        (ONE, ONE),
        (ONE, TWO),
    }
)

SHAPE_TO_COLOR_AD38A9D0 = {
    L_SHAPE_AD38A9D0: FOUR,
    S_SHAPE_AD38A9D0: EIGHT,
    PLUS_SHAPE_AD38A9D0: THREE,
    LINE_SHAPE_AD38A9D0: TWO,
    DOMINO_SHAPE_AD38A9D0: NINE,
    RECT_SHAPE_AD38A9D0: FIVE,
}

GRID_SHAPE_AD38A9D0 = (NINE, NINE)


def _reserved_cells_ad38a9d0(occupied: Indices) -> Indices:
    if len(occupied) == ZERO:
        return occupied
    return combine(occupied, mapply(dneighbors, occupied))


def _candidate_placements_ad38a9d0(
    patch: Indices,
    reserved: Indices,
) -> tuple[Indices, ...]:
    h = height(patch)
    w = width(patch)
    placements = []
    for i in interval(ZERO, GRID_SHAPE_AD38A9D0[ZERO] - h + ONE, ONE):
        for j in interval(ZERO, GRID_SHAPE_AD38A9D0[ONE] - w + ONE, ONE):
            candidate = shift(patch, (i, j))
            if len(intersection(candidate, reserved)) != ZERO:
                continue
            placements.append(candidate)
    return tuple(placements)


def _shape_multiset_ad38a9d0(
    diff_lb: float,
    diff_ub: float,
) -> list[Indices]:
    nl = unifint(diff_lb, diff_ub, (ONE, TWO))
    nv = unifint(diff_lb, diff_ub, (ONE, TWO))
    shapes = [
        PLUS_SHAPE_AD38A9D0,
        S_SHAPE_AD38A9D0,
        DOMINO_SHAPE_AD38A9D0,
        RECT_SHAPE_AD38A9D0,
    ]
    shapes.extend([L_SHAPE_AD38A9D0] * nl)
    shapes.extend([LINE_SHAPE_AD38A9D0] * nv)
    shuffle(shapes)
    shapes.sort(key=lambda patch: (-size(patch), height(patch), width(patch)))
    return shapes


def generate_ad38a9d0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        shapes = _shape_multiset_ad38a9d0(diff_lb, diff_ub)
        gi = canvas(SEVEN, GRID_SHAPE_AD38A9D0)
        go = canvas(SEVEN, GRID_SHAPE_AD38A9D0)
        occupied = frozenset()
        failed = F
        for patch in shapes:
            reserved = _reserved_cells_ad38a9d0(occupied)
            candidates = _candidate_placements_ad38a9d0(patch, reserved)
            if len(candidates) == ZERO:
                failed = T
                break
            placed = choice(candidates)
            occupied = combine(occupied, placed)
            gi = fill(gi, SIX, placed)
            go = fill(go, SHAPE_TO_COLOR_AD38A9D0[patch], placed)
        if failed:
            continue
        x0 = tuple(objects(gi, T, F, T))
        if len(x0) != len(shapes):
            continue
        x1 = sum(ONE for obj in x0 if bordering(obj, gi))
        if x1 < TWO:
            continue
        if x1 == len(x0):
            continue
        return {"input": gi, "output": go}
