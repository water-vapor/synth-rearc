from arc2.core import *


BACKGROUND_C6141B15 = 7

MOTIFS_C6141B15 = (
    {"patch": frozenset({(0, 0)}), "center": (0, 0)},
    {
        "patch": frozenset({(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)}),
        "center": (1, 1),
    },
    {
        "patch": frozenset({(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)}),
        "center": (1, 1),
    },
    {
        "patch": frozenset(
            {
                (0, 0),
                (0, 1),
                (0, 2),
                (1, 1),
                (2, 1),
                (3, 1),
                (4, 0),
                (4, 1),
                (4, 2),
            }
        ),
        "center": (2, 1),
    },
)


def _stamp_patch_c6141b15(
    patch: Patch,
    center: IntegerTuple,
    target: IntegerTuple,
) -> Patch:
    return shift(patch, subtract(target, center))


def _connection_patch_c6141b15(
    centers: tuple[IntegerTuple, ...],
) -> Indices:
    x0 = frozenset()
    for x1, x2 in enumerate(centers):
        for x3 in centers[x1 + ONE :]:
            x0 = combine(x0, connect(x2, x3))
    return x0


def _output_patterns_disjoint_c6141b15(
    motif_patch: Patch,
    motif_center: IntegerTuple,
    endpoints: tuple[IntegerTuple, IntegerTuple],
    connection_patch: Indices,
) -> Boolean:
    x0 = tuple(
        _stamp_patch_c6141b15(motif_patch, motif_center, x1)
        for x1 in endpoints
    )
    if any(size(intersection(x1, connection_patch)) for x1 in x0):
        return False
    return equality(size(intersection(x0[0], x0[1])), ZERO)


def _expanded_indices_c6141b15(indices: Indices) -> Indices:
    x0 = set(indices)
    for x1 in tuple(indices):
        x0 |= set(neighbors(x1))
    return frozenset(x0)


def _pattern_two_c6141b15(step: Integer) -> tuple[IntegerTuple, ...]:
    x0 = (
        lambda x1: ((0, 0), (0, x1)),
        lambda x1: ((0, 0), (x1, 0)),
        lambda x1: ((0, 0), (x1, x1)),
        lambda x1: ((0, x1), (x1, 0)),
    )
    return choice(x0)(step)


def _pattern_three_c6141b15(step: Integer) -> tuple[IntegerTuple, ...]:
    x0 = (
        lambda x1: ((0, 0), (0, x1), (x1, x1)),
        lambda x1: ((0, 0), (x1, 0), (x1, x1)),
        lambda x1: ((0, 0), (0, x1), (x1, 0)),
        lambda x1: ((x1, 0), (0, x1), (x1, x1)),
        lambda x1: ((0, 0), (x1, x1), (double(x1), 0)),
        lambda x1: ((0, 0), (x1, x1), (0, double(x1))),
        lambda x1: ((x1, 0), (0, x1), (x1, double(x1))),
        lambda x1: ((0, x1), (x1, 0), (double(x1), x1)),
    )
    return choice(x0)(step)


def _place_centers_c6141b15(
    dims: IntegerTuple,
    motif_patch: Patch,
    motif_center: IntegerTuple,
    count: Integer,
) -> tuple[tuple[IntegerTuple, ...], Indices] | None:
    x0, x1 = dims
    x2, x3 = shape(motif_patch)
    x4 = motif_center[0]
    x5 = decrement(x2) - motif_center[0]
    x6 = motif_center[1]
    x7 = decrement(x3) - motif_center[1]
    x8 = max(FOUR, increment(max(x2, x3)))
    x9 = min(x0 // TWO + TWO, decrement(x0))
    if x9 < x8:
        return None
    for _ in range(200):
        x10 = randint(x8, x9)
        x11 = _pattern_two_c6141b15(x10) if count == TWO else _pattern_three_c6141b15(x10)
        x12 = minimum(tuple(x13 for x13, _ in x11))
        x13 = maximum(tuple(x14 for x14, _ in x11))
        x14 = minimum(tuple(x15 for _, x15 in x11))
        x15 = maximum(tuple(x16 for _, x16 in x11))
        x16 = x4 - x12
        x17 = decrement(x0) - x5 - x13
        x18 = x6 - x14
        x19 = decrement(x1) - x7 - x15
        if either(greater(x16, x17), greater(x18, x19)):
            continue
        x20 = astuple(randint(x16, x17), randint(x18, x19))
        x21 = tuple(add(x20, x22) for x22 in x11)
        x22 = frozenset()
        for x23 in x21:
            x22 = combine(
                x22,
                _stamp_patch_c6141b15(motif_patch, motif_center, x23),
            )
        x23 = canvas(BACKGROUND_C6141B15, dims)
        x24 = fill(x23, ONE, x22)
        if equality(size(objects(x24, T, T, T)), count):
            return x21, x22
    return None


def _place_line_c6141b15(
    dims: IntegerTuple,
    motif_patch: Patch,
    motif_center: IntegerTuple,
    blocked: Indices,
    connection_patch: Indices,
) -> tuple[Indices, IntegerTuple, IntegerTuple] | None:
    x0, x1 = dims
    x2, x3 = shape(motif_patch)
    x4 = motif_center[0]
    x5 = decrement(x2) - motif_center[0]
    x6 = motif_center[1]
    x7 = decrement(x3) - motif_center[1]
    x8 = (
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
    )
    x9 = _expanded_indices_c6141b15(blocked)
    for _ in range(400):
        x10 = choice(x8)
        x11 = max(FIVE, increment(max(x2, x3)))
        x12 = SEVEN if x0 == 11 else TEN
        x13 = randint(x11, x12)
        x14, x15 = x10
        x16 = x4 + max(ZERO, -multiply(decrement(x13), x14))
        x17 = decrement(x0) - x5 - max(ZERO, multiply(decrement(x13), x14))
        x18 = x6 + max(ZERO, -multiply(decrement(x13), x15))
        x19 = decrement(x1) - x7 - max(ZERO, multiply(decrement(x13), x15))
        if either(greater(x16, x17), greater(x18, x19)):
            continue
        x20 = astuple(randint(x16, x17), randint(x18, x19))
        x21 = add(
            x20,
            multiply(decrement(x13), x10),
        )
        x22 = connect(x20, x21)
        if equality(size(intersection(x22, x9)), ZERO) and _output_patterns_disjoint_c6141b15(
            motif_patch,
            motif_center,
            (x20, x21),
            connection_patch,
        ):
            return x22, x20, x21
    return None


def generate_c6141b15(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((11, 16, 16))
        x1 = astuple(x0, x0)
        x2 = sample(tuple(x3 for x3 in range(TEN) if x3 != BACKGROUND_C6141B15), TWO)
        x3, x4 = x2
        x5 = choice(MOTIFS_C6141B15)
        x6 = x5["patch"]
        x7 = x5["center"]
        x8 = TWO if randint(ZERO, 99) < 28 else THREE
        x9 = _place_centers_c6141b15(x1, x6, x7, x8)
        if x9 is None:
            continue
        x10, x11 = x9
        x12 = _connection_patch_c6141b15(x10)
        x13 = _place_line_c6141b15(x1, x6, x7, x11, x12)
        if x13 is None:
            continue
        x14, x15, x16 = x13
        x17 = recolor(x4, x6)
        x18 = canvas(BACKGROUND_C6141B15, x1)
        for x19 in x10:
            x20 = shift(x17, subtract(x19, x7))
            x18 = paint(x18, x20)
        x18 = fill(x18, x3, x14)
        x21 = canvas(BACKGROUND_C6141B15, x1)
        x21 = fill(x21, x3, x12)
        for x19 in (x15, x16):
            x20 = shift(x17, subtract(x19, x7))
            x21 = paint(x21, x20)
        if x18 != x21:
            return {"input": x18, "output": x21}
