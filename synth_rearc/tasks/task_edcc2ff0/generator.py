from synth_rearc.core import *


HEADER_ROWS_EDCC2FF0 = (ONE, THREE, FIVE)
LOWER_SHAPE_EDCC2FF0 = (13, TEN)
ACTIVE_HEIGHT_EDCC2FF0 = 11
ACTIVE_WIDTH_EDCC2FF0 = 8

BASE_MOTIFS_EDCC2FF0 = (
    frozenset({(0, 0)}),
    frozenset({(0, 0)}),
    frozenset({(0, 0), (0, 1)}),
    frozenset({(0, 0), (0, 1)}),
    frozenset({(0, 0), (0, 1), (0, 2)}),
    frozenset({(0, 0), (0, 1), (0, 2), (0, 3)}),
    frozenset({(0, 0), (1, 0), (1, 1), (0, 1)}),
    frozenset({(0, 0), (0, 1), (1, 0)}),
)

SMALL_MOTIFS_EDCC2FF0 = BASE_MOTIFS_EDCC2FF0[:6]


def _motif_variants_edcc2ff0(
    patch: Indices,
) -> tuple[Indices, ...]:
    x0 = (
        normalize(patch),
        normalize(hmirror(patch)),
        normalize(vmirror(patch)),
        normalize(dmirror(patch)),
        normalize(cmirror(patch)),
        normalize(vmirror(dmirror(patch))),
        normalize(hmirror(dmirror(patch))),
        normalize(hmirror(vmirror(patch))),
    )
    return dedupe(x0)


def _halo_edcc2ff0(
    patch: Indices,
) -> frozenset[tuple[int, int]]:
    x0 = set()
    for x1 in patch:
        x0.add(x1)
        x0.update(neighbors(x1))
    return frozenset(
        (i, j)
        for i, j in x0
        if ZERO <= i < LOWER_SHAPE_EDCC2FF0[ZERO] and ZERO <= j < LOWER_SHAPE_EDCC2FF0[ONE]
    )


def _candidate_placements_edcc2ff0(
    patch: Indices,
    blocked: frozenset[tuple[int, int]],
) -> tuple[Indices, ...]:
    x0 = []
    x1 = ACTIVE_HEIGHT_EDCC2FF0 - height(patch) + TWO
    x2 = ACTIVE_WIDTH_EDCC2FF0 - width(patch) + TWO
    for x3 in range(ONE, x1):
        for x4 in range(ONE, x2):
            x5 = shift(patch, (x3, x4))
            if any(x6 in blocked for x6 in x5):
                continue
            x0.append(x5)
    return tuple(x0)


def _sample_object_patch_edcc2ff0(
    blocked: frozenset[tuple[int, int]],
    total_objects: int,
) -> Indices | None:
    x0 = branch(greater(total_objects, SEVEN), SMALL_MOTIFS_EDCC2FF0, BASE_MOTIFS_EDCC2FF0)
    x1 = list(x0)
    shuffle(x1)
    for x2 in x1:
        x3 = list(_motif_variants_edcc2ff0(x2))
        shuffle(x3)
        for x4 in x3:
            x5 = _candidate_placements_edcc2ff0(x4, blocked)
            if len(x5) == ZERO:
                continue
            return choice(x5)
    return None


def _render_header_input_edcc2ff0(
    colors: tuple[int, int, int],
) -> Grid:
    x0 = canvas(ZERO, astuple(SEVEN, TEN))
    for x1, x2 in zip(HEADER_ROWS_EDCC2FF0, colors):
        x0 = fill(x0, x2, frozenset({(x1, ZERO)}))
    return x0


def _render_header_output_edcc2ff0(
    colors: tuple[int, int, int],
    counts: tuple[int, int, int],
) -> Grid:
    x0 = canvas(ZERO, astuple(SEVEN, TEN))
    for x1, x2, x3 in zip(HEADER_ROWS_EDCC2FF0, colors, counts):
        x4 = frozenset((x1, x5) for x5 in range(x3))
        x0 = fill(x0, x2, x4)
    return x0


def generate_edcc2ff0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        x0 = choice(cols)
        x1 = remove(x0, cols)
        x2 = tuple(sample(x1, THREE))
        x3 = tuple(unifint(diff_lb, diff_ub, (ZERO, FIVE)) for _ in range(THREE))
        if sum(x4 > ZERO for x4 in x3) < TWO:
            continue
        if sum(x3) < FOUR:
            continue
        x5 = remove(ONE, interval(ONE, FOUR, ONE))
        x6 = choice(x5)
        x7 = tuple(sample(difference(x1, x2), x6))
        x8 = tuple(unifint(diff_lb, diff_ub, (ONE, TWO)) for _ in range(x6))
        x9 = sum(x3) + sum(x8)
        if x9 > TEN:
            continue
        x10 = []
        for x11, x12 in zip(x2, x3):
            x10.extend((x11, T) for _ in range(x12))
        for x13, x14 in zip(x7, x8):
            x10.extend((x13, F) for _ in range(x14))
        shuffle(x10)
        x15 = frozenset()
        x16 = []
        for x17, x18 in x10:
            x19 = _sample_object_patch_edcc2ff0(x15, x9)
            if x19 is None:
                x16 = []
                break
            x16.append((x17, x19, x18))
            x15 = combine(x15, _halo_edcc2ff0(x19))
        if len(x16) != len(x10):
            continue
        x20 = canvas(x0, LOWER_SHAPE_EDCC2FF0)
        x21 = canvas(x0, LOWER_SHAPE_EDCC2FF0)
        for x22, x23, x24 in x16:
            x20 = fill(x20, x22, x23)
            if x24:
                x21 = fill(x21, x22, x23)
        x25 = _render_header_input_edcc2ff0(x2)
        x26 = _render_header_output_edcc2ff0(x2, x3)
        gi = vconcat(x25, x20)
        go = vconcat(x26, x21)
        return {"input": gi, "output": go}
