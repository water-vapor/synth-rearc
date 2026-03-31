from synth_rearc.core import *


NON_HOST_CORNERS_F560132C = ("tr", "bl", "br")
INPUT_QUADRANTS_F560132C = ("ur", "bl", "br")


def rot90_patch_f560132c(
    patch: Indices,
) -> Indices:
    return frozenset(normalize(vmirror(dmirror(patch))))


def rot180_patch_f560132c(
    patch: Indices,
) -> Indices:
    return frozenset(normalize(hmirror(vmirror(patch))))


def rot270_patch_f560132c(
    patch: Indices,
) -> Indices:
    return frozenset(normalize(hmirror(dmirror(patch))))


def shape_variants_f560132c(
    patch: Indices,
) -> tuple[Indices, ...]:
    x0 = (
        identity,
        hmirror,
        vmirror,
        dmirror,
        cmirror,
        rot90_patch_f560132c,
        rot180_patch_f560132c,
        rot270_patch_f560132c,
    )
    x1 = []
    x2 = set()
    for x3 in x0:
        x4 = frozenset(normalize(x3(patch)))
        if x4 in x2:
            continue
        x2.add(x4)
        x1.append(x4)
    return tuple(x1)


def place_patch_in_square_corner_f560132c(
    patch: Indices,
    side: int,
    corner: str,
) -> Indices:
    x0 = frozenset(normalize(patch))
    x1 = height(x0)
    x2 = width(x0)
    if corner == "tl":
        return x0
    if corner == "tr":
        return shift(x0, (ZERO, side - x2))
    if corner == "bl":
        return shift(x0, (side - x1, ZERO))
    return shift(x0, (side - x1, side - x2))


def square_indices_f560132c(
    side: int,
) -> Indices:
    return asindices(canvas(ZERO, (side, side)))


def connected_patch_f560132c(
    patch: Indices,
) -> bool:
    if len(patch) == ZERO:
        return F
    x0 = first(patch)
    x1 = [x0]
    x2 = {x0}
    while len(x1) > ZERO:
        x3 = x1.pop()
        for x4 in dneighbors(x3):
            if x4 not in patch or x4 in x2:
                continue
            x2.add(x4)
            x1.append(x4)
    return len(x2) == len(patch)


def key_block_options_f560132c(
    host: Indices,
) -> tuple[Indices, ...]:
    x0 = frozenset(normalize(host))
    x1 = []
    x2 = height(x0)
    x3 = width(x0)
    for x4 in range(ONE, x2 - ONE):
        for x5 in range(ONE, x3 - ONE):
            x6 = frozenset({
                (x4, x5),
                (x4 + ONE, x5),
                (x4, x5 + ONE),
                (x4 + ONE, x5 + ONE),
            })
            if x6 <= x0 and connected_patch_f560132c(x0 - x6):
                x1.append(x6)
    return tuple(x1)


def _in_bounds_f560132c(
    loc: IntegerTuple,
    side: int,
) -> bool:
    return ZERO <= loc[0] < side and ZERO <= loc[1] < side


def _corner_seed_f560132c(
    side: int,
    corner: str,
) -> IntegerTuple:
    if corner == "tr":
        return (ZERO, side - ONE)
    if corner == "bl":
        return (side - ONE, ZERO)
    if corner == "br":
        return (side - ONE, side - ONE)
    return ORIGIN


def _corner_distance_f560132c(
    loc: IntegerTuple,
    side: int,
    corner: str,
) -> int:
    x0, x1 = loc
    x2 = side - ONE
    if corner == "tr":
        return x0 + (x2 - x1)
    if corner == "bl":
        return (x2 - x0) + x1
    if corner == "br":
        return (x2 - x0) + (x2 - x1)
    return x0 + x1


def _center_distance_f560132c(
    loc: IntegerTuple,
    side: int,
) -> int:
    x0 = side - ONE
    return abs(TWO * loc[0] - x0) + abs(TWO * loc[1] - x0)


def grow_corner_region_f560132c(
    side: int,
    corner: str,
    target: int,
    occupied: Indices,
) -> Indices:
    if target < ONE:
        return frozenset()
    x0 = _corner_seed_f560132c(side, corner)
    if x0 in occupied:
        return frozenset()
    x1 = {x0}
    x2 = {
        x3 for x3 in dneighbors(x0)
        if _in_bounds_f560132c(x3, side) and x3 not in occupied
    }
    while len(x1) < target:
        x3 = [x4 for x4 in x2 if x4 not in x1 and x4 not in occupied]
        if len(x3) == ZERO:
            return frozenset()
        x3 = sorted(
            x3,
            key=lambda x4: (
                _corner_distance_f560132c(x4, side, corner),
                -sum(ONE for x5 in dneighbors(x4) if x5 in x1),
                _center_distance_f560132c(x4, side),
            ),
        )
        x4 = choice(x3[:min(FIVE, len(x3))])
        x1.add(x4)
        x2.discard(x4)
        for x5 in dneighbors(x4):
            if _in_bounds_f560132c(x5, side) and x5 not in occupied and x5 not in x1:
                x2.add(x5)
    return frozenset(x1)


def sample_partition_f560132c(
    diff_lb: float,
    diff_ub: float,
) -> tuple[int, Indices, dict[str, Indices], Indices]:
    for _ in range(400):
        x0 = unifint(diff_lb, diff_ub, (EIGHT, 12))
        x1 = x0 * x0
        x2 = max(FOUR, x0 - THREE)
        x3 = max(EIGHT, x0)
        x4 = x1 - x3
        x5 = []
        x6 = T
        for x7 in range(THREE):
            x8 = (TWO - x7) * x2
            x9 = x2
            x10 = min(x1 // TWO, x4 - x8)
            if x10 < x9:
                x6 = F
                break
            x11 = randint(x9, x10)
            x5.append(x11)
            x4 = x4 - x11
        if flip(x6):
            continue
        shuffle(x5)
        x12 = list(NON_HOST_CORNERS_F560132C)
        shuffle(x12)
        x13 = frozenset()
        x14 = {}
        x15 = T
        for x16, x17 in zip(x12, x5):
            x18 = grow_corner_region_f560132c(x0, x16, x17, x13)
            if len(x18) != x17:
                x15 = F
                break
            x14[x16] = x18
            x13 = frozenset(set(x13) | set(x18))
        if flip(x15):
            continue
        if size(x14["tr"]) <= size(x14["bl"]):
            continue
        x19 = frozenset(square_indices_f560132c(x0) - x13)
        if len(x19) < x3 or flip(connected_patch_f560132c(x19)):
            continue
        x20 = key_block_options_f560132c(x19)
        if len(x20) == ZERO:
            continue
        x20 = tuple(sorted(x20, key=lambda x21: (uppermost(x21), leftmost(x21))))
        x21 = choice(x20[:min(FOUR, len(x20))])
        return x0, x19, x14, x21
    raise RuntimeError("failed to sample a square partition for f560132c")


def input_canvas_dims_f560132c(
    host_patch: Indices,
    ur_patch: Indices,
    bl_patch: Indices,
    br_patch: Indices,
    side: int,
) -> IntegerTuple:
    x0 = max(height(host_patch) + height(bl_patch) + SIX, height(ur_patch) + height(br_patch) + SIX, side * TWO + FOUR)
    x1 = max(width(host_patch) + width(ur_patch) + SIX, width(bl_patch) + width(br_patch) + SIX, side * TWO + FOUR)
    x2 = min(30, max(x0, side * TWO + SIX))
    x3 = min(30, max(x1, side * TWO + SIX))
    return (randint(x0, x2), randint(x1, x3))


def input_quadrant_shift_f560132c(
    patch: Indices,
    dims: IntegerTuple,
    quadrant: str,
) -> IntegerTuple:
    x0, x1 = dims
    x2 = height(patch)
    x3 = width(patch)
    if quadrant == "ul":
        return (randint(ONE, THREE), randint(ONE, THREE))
    if quadrant == "ur":
        return (randint(ONE, THREE), x1 - x3 - randint(ONE, THREE))
    if quadrant == "bl":
        return (x0 - x2 - randint(ONE, THREE), randint(ONE, THREE))
    return (x0 - x2 - randint(ONE, THREE), x1 - x3 - randint(ONE, THREE))
