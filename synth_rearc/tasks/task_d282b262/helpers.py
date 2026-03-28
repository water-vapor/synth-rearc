from synth_rearc.core import *


def checkerboard_object_d282b262(
    obj_size: Integer,
    colors: Tuple,
    loc: IntegerTuple,
) -> Object:
    x0 = []
    for i in range(obj_size):
        for j in range(obj_size):
            x1 = colors[(i + j) % TWO]
            x0.append((x1, (loc[0] + i, loc[1] + j)))
    return frozenset(x0)


def _expanded_patch_d282b262(
    loc: IntegerTuple,
    obj_size: Integer,
    side: Integer,
) -> Patch:
    rows = range(max(ZERO, loc[0] - ONE), min(side, loc[0] + obj_size + ONE))
    cols = range(max(ZERO, loc[1] - ONE), min(side, loc[1] + obj_size + ONE))
    return frozenset((i, j) for i in rows for j in cols)


def _row_intervals_overlap_d282b262(
    loc_a: IntegerTuple,
    size_a: Integer,
    loc_b: IntegerTuple,
    size_b: Integer,
) -> Boolean:
    x0 = loc_a[0] + size_a - ONE
    x1 = loc_b[0] + size_b - ONE
    return not (x0 < loc_b[0] or x1 < loc_a[0])


def has_row_interaction_d282b262(
    locs: Tuple,
    sizes: Tuple,
) -> Boolean:
    for x0, x1 in enumerate(locs):
        for x2 in range(x0 + ONE, len(locs)):
            if _row_intervals_overlap_d282b262(x1, sizes[x0], locs[x2], sizes[x2]):
                return T
    return F


def has_ambiguous_order_d282b262(
    locs: Tuple,
    sizes: Tuple,
) -> Boolean:
    for x0, x1 in enumerate(locs):
        x2 = x1[1] + sizes[x0] - ONE
        for x3 in range(x0 + ONE, len(locs)):
            if not _row_intervals_overlap_d282b262(x1, sizes[x0], locs[x3], sizes[x3]):
                continue
            x4 = locs[x3][1] + sizes[x3] - ONE
            if x2 == x4:
                return T
    return F


def place_squares_d282b262(
    sizes: Tuple,
    side: Integer,
    max_right: Integer,
) -> Tuple | None:
    x0 = list(range(len(sizes)))
    shuffle(x0)
    x0.sort(key=lambda idx: sizes[idx], reverse=True)
    x1 = [None] * len(sizes)
    x2 = frozenset()
    for x3 in x0:
        x4 = sizes[x3]
        x5 = min(side - x4, max_right - x4 + ONE)
        if x5 < ZERO:
            return None
        x6 = []
        for x7 in range(side - x4 + ONE):
            for x8 in range(x5 + ONE):
                x9 = frozenset(
                    (ii, jj)
                    for ii in range(x7, x7 + x4)
                    for jj in range(x8, x8 + x4)
                )
                if len(intersection(x9, x2)) == ZERO:
                    x6.append((x7, x8))
        if len(x6) == ZERO:
            return None
        x10 = choice(x6)
        x1[x3] = x10
        x2 = combine(x2, _expanded_patch_d282b262(x10, x4, side))
    return tuple(x1)


def _row_right_profile_d282b262(
    obj: Object,
) -> dict[int, int]:
    x0 = {}
    for _, x1 in obj:
        x2 = x0.get(x1[0], -ONE)
        if x1[1] > x2:
            x0[x1[0]] = x1[1]
    return x0


def _row_left_profile_d282b262(
    obj: Object,
) -> dict[int, int]:
    x0 = {}
    for _, x1 in obj:
        x2 = x0.get(x1[0], 30)
        if x1[1] < x2:
            x0[x1[0]] = x1[1]
    return x0


def pack_objects_right_d282b262(
    objects_seq: Tuple,
    width_value: Integer,
) -> Tuple | None:
    x0 = list(range(len(objects_seq)))
    x0.sort(
        key=lambda idx: (
            rightmost(objects_seq[idx]),
            leftmost(objects_seq[idx]),
            uppermost(objects_seq[idx]),
            lowermost(objects_seq[idx]),
        )
    )
    x1 = [None] * len(objects_seq)
    x2 = ()
    for x3 in x0[::-1]:
        x4 = objects_seq[x3]
        x5 = subtract(subtract(width_value, ONE), rightmost(x4))
        x6 = _row_right_profile_d282b262(x4)
        for x7 in x2:
            x8 = _row_left_profile_d282b262(x7)
            for x9, x10 in x6.items():
                if x9 in x8:
                    x11 = subtract(subtract(x8[x9], x10), ONE)
                    x5 = minimum((x5, x11))
        if x5 < ZERO:
            return None
        x12 = shift(x4, (ZERO, x5))
        x1[x3] = x12
        x2 = x2 + (x12,)
    return tuple(x1)
