from arc2.core import *


GRID_SHAPE_AAECDB9A = (TEN, TEN)
SUMMARY_COLORS_AAECDB9A = (FIVE, TWO, EIGHT, NINE, SIX)

_PLUS_PATCH_AAECDB9A = frozenset(
    {
        (ZERO, ONE),
        (ONE, ZERO),
        (ONE, ONE),
        (ONE, TWO),
        (TWO, ONE),
    }
)
_X_PATCH_AAECDB9A = frozenset(
    {
        (ZERO, ZERO),
        (ZERO, TWO),
        (ONE, ONE),
        (TWO, ZERO),
        (TWO, TWO),
    }
)
_RING_PATCH_AAECDB9A = frozenset(
    (i, j) for i in range(THREE) for j in range(THREE) if (i, j) != (ONE, ONE)
)
_TRANSFORMS_AAECDB9A = (
    identity,
    hmirror,
    vmirror,
    compose(hmirror, vmirror),
    dmirror,
    cmirror,
    compose(hmirror, dmirror),
    compose(vmirror, dmirror),
)


def _rect_patch_aaecdb9a(
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    return frozenset((i, j) for i in range(height_value) for j in range(width_value))


def _line_patch_aaecdb9a(
    length_value: Integer,
    direction: IntegerTuple,
) -> Indices:
    return normalize(
        frozenset(
            (k * direction[ZERO], k * direction[ONE])
            for k in range(length_value)
        )
    )


def _elbow_patch_aaecdb9a(
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    x0 = {(i, ZERO) for i in range(height_value)}
    x1 = {(height_value - ONE, j) for j in range(width_value)}
    return frozenset(x0 | x1)


def _tee_patch_aaecdb9a(
    span_value: Integer,
    stem_value: Integer,
) -> Indices:
    x0 = span_value // TWO
    x1 = {(ZERO, j) for j in range(span_value)}
    x2 = {(i, x0) for i in range(stem_value)}
    return frozenset(x1 | x2)


def _step_patch_aaecdb9a(
    length_value: Integer,
) -> Indices:
    x0 = set()
    for x1 in range(length_value):
        x0.add((x1 // TWO, x1 - (x1 // TWO)))
    return normalize(frozenset(x0))


def _variant_patch_aaecdb9a(
    patch: Indices,
) -> Indices:
    x0 = []
    for x1 in _TRANSFORMS_AAECDB9A:
        x2 = normalize(x1(patch))
        if x2 not in x0:
            x0.append(x2)
    return choice(tuple(x0))


def sample_component_counts_aaecdb9a(
    diff_lb: float,
    diff_ub: float,
) -> dict[int, int]:
    while True:
        x0 = unifint(diff_lb, diff_ub, (TWO, SIX))
        x1 = FIVE if x0 <= FIVE else FOUR
        x2 = unifint(diff_lb, diff_ub, (TWO, x1))
        x3 = tuple(sample(SUMMARY_COLORS_AAECDB9A, x2))
        x4 = {x5: ZERO for x5 in SUMMARY_COLORS_AAECDB9A}
        x5 = choice(x3)
        x4[x5] = x0
        if x0 >= FOUR and x2 >= THREE and choice((T, F, F)) == T:
            x6 = choice(tuple(x7 for x7 in x3 if x7 != x5))
            x4[x6] = choice((x0, max(ONE, x0 - ONE)))
        x7 = tuple(
            x8
            for x8 in range(ONE, x0 + ONE)
            for _ in range(x0 - x8 + ONE)
        )
        for x8 in x3:
            if x4[x8] > ZERO:
                continue
            x4[x8] = choice(x7)
        x9 = tuple(x4[x10] for x10 in SUMMARY_COLORS_AAECDB9A)
        if sum(x9) <= 12 and maximum(x9) == x0:
            return x4


def sample_component_patch_aaecdb9a(
    component_count: Integer,
) -> Indices:
    x0 = (frozenset({(ZERO, ZERO)}),)
    x1 = (
        _line_patch_aaecdb9a(TWO, RIGHT),
        _line_patch_aaecdb9a(TWO, UNITY),
        _line_patch_aaecdb9a(THREE, RIGHT),
        _line_patch_aaecdb9a(THREE, UNITY),
        _elbow_patch_aaecdb9a(TWO, TWO),
        _rect_patch_aaecdb9a(TWO, TWO),
        _step_patch_aaecdb9a(THREE),
    )
    x2 = (
        _line_patch_aaecdb9a(FOUR, RIGHT),
        _line_patch_aaecdb9a(FOUR, UNITY),
        _line_patch_aaecdb9a(FIVE, RIGHT),
        _rect_patch_aaecdb9a(TWO, THREE),
        _elbow_patch_aaecdb9a(THREE, TWO),
        _elbow_patch_aaecdb9a(TWO, THREE),
        _tee_patch_aaecdb9a(THREE, THREE),
        _PLUS_PATCH_AAECDB9A,
        _X_PATCH_AAECDB9A,
    )
    x3 = (
        _line_patch_aaecdb9a(SIX, RIGHT),
        _line_patch_aaecdb9a(SEVEN, RIGHT),
        _rect_patch_aaecdb9a(TWO, FOUR),
        _rect_patch_aaecdb9a(THREE, THREE),
        _tee_patch_aaecdb9a(FOUR, THREE),
        _RING_PATCH_AAECDB9A,
    )
    if component_count >= FIVE:
        x4 = x0 + x1 + x1
    elif component_count == FOUR:
        x4 = x1 + x1 + x2
    elif component_count == THREE:
        x4 = x1 + x2 + x2
    elif component_count == TWO:
        x4 = x2 + x2 + x3
    else:
        x4 = x2 + x3 + x3
    return _variant_patch_aaecdb9a(choice(x4))


def compose_output_aaecdb9a(
    counts_by_color: dict[int, int],
) -> Grid:
    x0 = maximum(tuple(counts_by_color[x1] for x1 in SUMMARY_COLORS_AAECDB9A))
    x1 = canvas(SEVEN, (x0, FIVE))
    for x2, x3 in enumerate(SUMMARY_COLORS_AAECDB9A):
        x4 = counts_by_color[x3]
        if x4 == ZERO:
            continue
        x5 = frozenset((x6, x2) for x6 in range(x0 - x4, x0))
        x1 = fill(x1, x3, x5)
    return x1


def _touches_border_aaecdb9a(
    patch: Indices,
) -> Boolean:
    x0 = GRID_SHAPE_AAECDB9A[ZERO] - ONE
    x1 = GRID_SHAPE_AAECDB9A[ONE] - ONE
    return any(i in (ZERO, x0) or j in (ZERO, x1) for i, j in patch)


def _expand_patch_aaecdb9a(
    patch: Indices,
) -> Indices:
    x0 = set()
    x1 = GRID_SHAPE_AAECDB9A[ZERO]
    x2 = GRID_SHAPE_AAECDB9A[ONE]
    for x3, x4 in patch:
        for x5 in (-ONE, ZERO, ONE):
            for x6 in (-ONE, ZERO, ONE):
                x7 = x3 + x5
                x8 = x4 + x6
                if 0 <= x7 < x1 and 0 <= x8 < x2:
                    x0.add((x7, x8))
    return frozenset(x0)


def place_patch_aaecdb9a(
    blocked: Indices,
    patch: Indices,
) -> tuple[Indices | None, Indices]:
    x0 = GRID_SHAPE_AAECDB9A[ZERO]
    x1 = GRID_SHAPE_AAECDB9A[ONE]
    x2 = height(patch)
    x3 = width(patch)
    x4 = []
    for x5 in range(x0 - x2 + ONE):
        for x6 in range(x1 - x3 + ONE):
            x7 = shift(patch, (x5, x6))
            if blocked.isdisjoint(x7):
                x4.append(x7)
    if len(x4) == ZERO:
        return None, blocked
    x5 = tuple(x6 for x6 in x4 if _touches_border_aaecdb9a(x6))
    if len(x5) > ZERO and choice((T, T, F)) == T:
        x6 = choice(x5)
    else:
        x6 = choice(x4)
    return x6, blocked | _expand_patch_aaecdb9a(x6)
