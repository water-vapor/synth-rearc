from synth_rearc.core import *


GRID_SHAPE_42F14C03 = astuple(16, 16)
PALETTE_42F14C03 = tuple(range(1, 10))


def _rectangle_42f14c03(
    height_: Integer,
    width_: Integer,
) -> Indices:
    return frozenset((i, j) for i in range(height_) for j in range(width_))


def _full_patch_42f14c03(
    dims: IntegerTuple,
) -> Indices:
    return _rectangle_42f14c03(dims[0], dims[1])


def _carved_patch_42f14c03(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Indices, tuple[Indices, Indices]]:
    x0 = choice(("horizontal", "vertical"))
    if x0 == "horizontal":
        x1 = unifint(diff_lb, diff_ub, (ONE, THREE))
        x2 = unifint(diff_lb, diff_ub, (ONE, THREE))
        x3 = unifint(diff_lb, diff_ub, (ONE, THREE))
        x4 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x5 = unifint(diff_lb, diff_ub, (ONE, TWO))
        x6 = unifint(diff_lb, diff_ub, (ONE, TWO))
        x7 = x1 + x2 + x3
        x8 = x4 + x5 + x6
        x9 = frozenset((i, j) for i in range(x1) for j in range(x5, x5 + x4))
        x10 = frozenset((i, j) for i in range(x7 - x2, x7) for j in range(x5, x5 + x4))
        x11 = _full_patch_42f14c03((x7, x8))
        return difference(difference(x11, x9), x10), (x9, x10)
    x1 = unifint(diff_lb, diff_ub, (TWO, FOUR))
    x2 = unifint(diff_lb, diff_ub, (ONE, THREE))
    x3 = unifint(diff_lb, diff_ub, (ONE, THREE))
    x4 = unifint(diff_lb, diff_ub, (ONE, THREE))
    x5 = unifint(diff_lb, diff_ub, (ONE, TWO))
    x6 = unifint(diff_lb, diff_ub, (ONE, TWO))
    x7 = x1 + x5 + x6
    x8 = x2 + x3 + x4
    x9 = frozenset((i, j) for i in range(x2, x2 + x1) for j in range(x5))
    x10 = frozenset((i, j) for i in range(x2, x2 + x1) for j in range(x7 - x6, x7))
    x11 = _full_patch_42f14c03((x8, x7))
    return difference(difference(x11, x9), x10), (x9, x10)


def _solid_patch_42f14c03(
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    x0 = unifint(diff_lb, diff_ub, (TWO, FOUR))
    x1 = unifint(diff_lb, diff_ub, (TWO, FIVE))
    return _full_patch_42f14c03((x0, x1))


def _neighbors8_42f14c03(
    loc: IntegerTuple,
) -> Indices:
    x0 = loc[0]
    x1 = loc[1]
    return frozenset((x0 + i, x1 + j) for i in (-ONE, ZERO, ONE) for j in (-ONE, ZERO, ONE))


def _halo_42f14c03(
    patch: Indices,
) -> Indices:
    x0 = set()
    for x1 in patch:
        x0.update(_neighbors8_42f14c03(x1))
    return frozenset(x0)


def _placements_42f14c03(
    patch: Indices,
    blocked: Indices,
) -> tuple[Indices, ...]:
    x0 = GRID_SHAPE_42F14C03[0] - height(patch) + ONE
    x1 = GRID_SHAPE_42F14C03[1] - width(patch) + ONE
    x2 = []
    for x3 in range(x0):
        for x4 in range(x1):
            x5 = shift(patch, (x3, x4))
            if len(intersection(x5, blocked)) == ZERO:
                x2.append(x5)
    return tuple(x2)


def _place_patch_42f14c03(
    patch: Indices,
    blocked: Indices,
) -> Indices | None:
    x0 = _placements_42f14c03(patch, blocked)
    if len(x0) == ZERO:
        return None
    return choice(x0)


def _shape_key_42f14c03(
    patch: Indices,
) -> Indices:
    return normalize(patch)


def _candidate_count_42f14c03(
    grid: Grid,
) -> Integer:
    x0 = objects(grid, T, F, T)
    x1 = tuple(x0)
    x2 = ZERO
    for x3 in x1:
        x4 = delta(x3)
        if len(x4) == ZERO:
            continue
        x5 = shift(x4, invert(ulcorner(x3)))
        x6 = fill(canvas(ZERO, shape(x3)), ONE, x5)
        x7 = tuple(objects(x6, T, F, T))
        if len(x7) == ZERO:
            continue
        x8 = {}
        for x9 in x1:
            if x9 == x3:
                continue
            x10 = normalize(toindices(x9))
            x8[x10] = x8.get(x10, ZERO) + ONE
        x11 = {}
        for x12 in x7:
            x13 = normalize(toindices(x12))
            x11[x13] = x11.get(x13, ZERO) + ONE
        x14 = T
        for x15, x16 in x11.items():
            if x8.get(x15, ZERO) < x16:
                x14 = F
                break
        if x14:
            x2 = increment(x2)
    return x2


def generate_42f14c03(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(PALETTE_42F14C03)
        x1 = tuple(x2 for x2 in PALETTE_42F14C03 if x2 != x0)
        x2 = _carved_patch_42f14c03(diff_lb, diff_ub)
        x3 = x2[ZERO]
        x4 = x2[ONE]
        x5 = _shape_key_42f14c03(x4[ZERO])
        x6 = _shape_key_42f14c03(x4[ONE])
        x7 = choice(x1)
        if x5 == x6:
            x8 = (x7, x7)
            x9 = tuple(x10 for x10 in x1 if x10 != x7)
        else:
            x8 = tuple(sample(x1, TWO))
            x9 = tuple(x10 for x10 in x1 if x10 not in x8)
        x10 = choice(x9)
        x11 = canvas(x10, shape(x3))
        x11 = fill(x11, x8[ZERO], x4[ZERO])
        x11 = fill(x11, x8[ONE], x4[ONE])
        x12 = []
        x13 = tuple(x14 for x14 in x9 if x14 != x10)
        x14 = unifint(diff_lb, diff_ub, (ONE, THREE))
        shuffle_pool = list(x13)
        shuffle(shuffle_pool)
        x15 = tuple(shuffle_pool[:x14])
        for x16, x17 in enumerate(x15):
            x18 = "carved" if x16 == ZERO else choice(("carved", "carved", "solid"))
            if x18 == "solid":
                x19 = _solid_patch_42f14c03(diff_lb, diff_ub)
            else:
                x19 = _carved_patch_42f14c03(diff_lb, diff_ub)[ZERO]
            x12.append((x17, x19))
        x19 = []
        for x20, x21 in zip(x8, x4):
            x22 = _shape_key_42f14c03(x21)
            x19.append((x20, x22))
        x23 = sorted(
            [(x10, x3)] + x12 + x19,
            key=lambda x24: size(x24[ONE]),
            reverse=True,
        )
        x24 = frozenset()
        x25 = []
        x26 = T
        for x27, x28 in x23:
            x29 = _place_patch_42f14c03(x28, x24)
            if x29 is None:
                x26 = F
                break
            x25.append((x27, x29))
            x24 = combine(x24, _halo_42f14c03(x29))
        if flip(x26):
            continue
        x30 = canvas(x0, GRID_SHAPE_42F14C03)
        for x31, x32 in x25:
            x30 = fill(x30, x31, x32)
        if _candidate_count_42f14c03(x30) != ONE:
            continue
        from .verifier import verify_42f14c03

        try:
            x33 = verify_42f14c03(x30)
        except Exception:
            continue
        if x33 != x11:
            continue
        return {"input": x30, "output": x11}
