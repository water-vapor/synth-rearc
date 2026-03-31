from synth_rearc.core import *

from .helpers import best_vertical_subset_8e5c0c38
from .verifier import verify_8e5c0c38


GRID_SHAPE_8E5C0C38 = astuple(22, 22)
PROFILE_SPECS_8E5C0C38 = {
    "large": ((SIX, 11), (THREE, SIX), (EIGHT, 22)),
    "medium": ((FOUR, NINE), (TWO, FIVE), (SIX, 18)),
    "small": ((THREE, SIX), (ONE, THREE), (FOUR, TEN)),
}
ROW_PATTERNS_8E5C0C38 = (
    ("upper", "upper", "lower"),
    ("upper", "middle", "lower"),
    ("upper", "lower", "lower"),
)
ROW_BANDS_8E5C0C38 = {
    "upper": (ONE, TEN),
    "middle": (FIVE, 14),
    "lower": (TEN, 18),
    "any": (ONE, 18),
}


def _mirror_half_8e5c0c38(
    patch: Indices,
    axis_col: Integer,
) -> Indices:
    x0 = set()
    for x1, x2 in patch:
        x0.add((x1, x2))
        x0.add((x1, subtract(double(axis_col), x2)))
    return frozenset(x0)


def _in_bounds_8e5c0c38(
    loc: IntegerTuple,
    dims: IntegerTuple,
) -> Boolean:
    x0, x1 = loc
    x2, x3 = dims
    return ZERO <= x0 < x2 and ZERO <= x1 < x3


def _orthopad_8e5c0c38(
    patch: Patch,
) -> Indices:
    x0 = set(toindices(patch))
    for x1 in toindices(patch):
        x0.update(dneighbors(x1))
    return frozenset(x0)


def _sample_half_patch_8e5c0c38(
    height_value: Integer,
    half_width: Integer,
    target: Integer,
) -> Indices:
    x0 = frozenset(product(interval(ZERO, height_value, ONE), interval(ZERO, half_width, ONE)))
    x1 = {
        (
            randint(ZERO, subtract(height_value, ONE)),
            randint(ZERO, subtract(half_width, ONE)),
        )
    }
    while len(x1) < target:
        x2 = set()
        for x3 in x1:
            for x4 in dneighbors(x3):
                if _in_bounds_8e5c0c38(x4, (height_value, half_width)) and x4 not in x1:
                    x2.add(x4)
        x5 = [x6 for x6 in x0 if x6 not in x1]
        if not x5:
            break
        if x2 and choice((True, True, False, False, False)):
            x6 = choice(tuple(x2))
        else:
            x6 = choice(tuple(x5))
        x1.add(x6)
        if choice((False, False, True)):
            x7 = choice((UP, DOWN, LEFT, RIGHT))
            x8 = add(x6, x7)
            if _in_bounds_8e5c0c38(x8, (height_value, half_width)):
                x1.add(x8)
    for _ in range(randint(ZERO, TWO)):
        x9 = randint(ZERO, subtract(height_value, ONE))
        x10 = randint(ZERO, subtract(half_width, ONE))
        x11 = randint(x10, subtract(half_width, ONE))
        for x12 in range(x10, increment(x11)):
            x1.add((x9, x12))
    for _ in range(randint(ZERO, TWO)):
        x13 = randint(ZERO, subtract(height_value, ONE))
        x14 = randint(ZERO, subtract(half_width, ONE))
        x15 = randint(x13, subtract(height_value, ONE))
        for x16 in range(x13, increment(x15)):
            x1.add((x16, x14))
    return frozenset(x1)


def _sample_core_8e5c0c38(
    profile: str,
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    x0, x1, x2 = PROFILE_SPECS_8E5C0C38[profile]
    for _ in range(200):
        x3 = unifint(diff_lb, diff_ub, x0)
        x4 = unifint(diff_lb, diff_ub, x1)
        x5 = increment(x4)
        x6 = min(
            multiply(x3, x5),
            unifint(diff_lb, diff_ub, x2),
        )
        x7 = _sample_half_patch_8e5c0c38(x3, x5, x6)
        x8 = normalize(_mirror_half_8e5c0c38(x7, x4))
        if height(x8) < THREE or width(x8) < THREE or len(x8) < FIVE:
            continue
        x9, _ = best_vertical_subset_8e5c0c38(x8)
        if x9 != x8:
            continue
        return x8
    raise RuntimeError(f"failed to sample symmetric core for profile {profile}")


def _embed_core_8e5c0c38(
    core: Indices,
) -> tuple[Indices, IntegerTuple]:
    x0 = height(core)
    x1 = width(core)
    x2 = randint(ZERO, TWO)
    x3 = randint(ZERO, TWO)
    x4 = randint(ZERO, TWO)
    x5 = randint(ZERO, TWO)
    if x2 == x3 == x4 == x5 == ZERO:
        x2 = ONE
    x6 = shift(core, (x2, x4))
    return x6, (add(add(x0, x2), x3), add(add(x1, x4), x5))


def _eligible_extra_8e5c0c38(
    loc: IntegerTuple,
    patch: Indices,
    axis_twice: Integer,
) -> Boolean:
    if double(loc[ONE]) == axis_twice:
        return False
    return (loc[ZERO], subtract(axis_twice, loc[ONE])) not in patch


def _augment_core_8e5c0c38(
    core: Indices,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Indices, Indices]:
    for _ in range(200):
        x0, x1 = _embed_core_8e5c0c38(core)
        x2 = add(leftmost(x0), rightmost(x0))
        x3 = set(x0)
        x4 = unifint(diff_lb, diff_ub, (ONE, FOUR))
        for _ in range(x4):
            x5 = set()
            for x6 in x3:
                for x7 in dneighbors(x6):
                    if not _in_bounds_8e5c0c38(x7, x1):
                        continue
                    if x7 in x3 or not _eligible_extra_8e5c0c38(x7, x3, x2):
                        continue
                    x5.add(x7)
            if not x5:
                continue
            for _ in range(30):
                x6 = choice(tuple(x5))
                x7 = {x6}
                x8 = x6
                x9 = unifint(diff_lb, diff_ub, (ONE, THREE))
                for _ in range(decrement(x9)):
                    x10 = []
                    for x11 in dneighbors(x8):
                        if not _in_bounds_8e5c0c38(x11, x1):
                            continue
                        if x11 in x3 or x11 in x7:
                            continue
                        if not _eligible_extra_8e5c0c38(x11, combine(frozenset(x3), frozenset(x7)), x2):
                            continue
                        x10.append(x11)
                    if not x10:
                        break
                    x8 = choice(tuple(x10))
                    x7.add(x8)
                x11 = frozenset(x3 | x7)
                x12, _ = best_vertical_subset_8e5c0c38(x11)
                if x12 == x0:
                    x3 |= x7
                    break
        x5 = frozenset(x3)
        if x5 == x0:
            continue
        x6 = invert(ulcorner(x5))
        x7 = shift(x5, x6)
        x8 = shift(x0, x6)
        x9, _ = best_vertical_subset_8e5c0c38(x7)
        if x9 != x8:
            continue
        return x7, x8
    raise RuntimeError("failed to augment symmetric core")


def _sample_partition_8e5c0c38(
    profile: str,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Indices, Indices]:
    x0 = _sample_core_8e5c0c38(profile, diff_lb, diff_ub)
    return _augment_core_8e5c0c38(x0, diff_lb, diff_ub)


def _place_patch_8e5c0c38(
    patch: Indices,
    occupied: Indices,
    band_name: str,
) -> IntegerTuple | None:
    x0 = height(patch)
    x1 = width(patch)
    x2, x3 = GRID_SHAPE_8E5C0C38
    x4 = _orthopad_8e5c0c38(occupied)
    x5, x6 = ROW_BANDS_8E5C0C38[band_name]
    x7 = max(ONE, x5)
    x8 = min(subtract(subtract(x2, x0), ONE), x6)
    x9 = subtract(subtract(x3, x1), ONE)
    if x8 < x7 or x9 < ONE:
        return None
    for _ in range(80):
        x10 = randint(x7, x8)
        x11 = randint(ONE, x9)
        x12 = shift(patch, (x10, x11))
        if len(intersection(toindices(x12), x4)) == ZERO:
            return (x10, x11)
    if band_name != "any":
        return _place_patch_8e5c0c38(patch, occupied, "any")
    return None


def generate_8e5c0c38(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(
            (
                ("large", "medium", "medium"),
                ("large", "medium", "small"),
                ("medium", "medium", "small"),
            )
        )
        x1 = [_sample_partition_8e5c0c38(x2, diff_lb, diff_ub) for x2 in x0]
        x2 = sorted(
            x1,
            key=lambda x3: len(x3[ZERO]),
            reverse=True,
        )
        x3 = choice(ROW_PATTERNS_8E5C0C38)
        x4 = []
        x5 = frozenset()
        for x6, x7 in zip(x2, x3):
            x8 = _place_patch_8e5c0c38(x6[ZERO], x5, x7)
            if x8 is None:
                x4 = []
                break
            x9 = shift(x6[ZERO], x8)
            x10 = shift(x6[ONE], x8)
            x4.append((x9, x10))
            x5 = combine(x5, x9)
        if len(x4) != THREE:
            continue
        x6 = [center(x7[ZERO]) for x7 in x4]
        x7 = [x8[ZERO] for x8 in x6]
        if subtract(max(x7), min(x7)) < FOUR:
            continue
        x8 = randint(ZERO, NINE)
        x9 = tuple(x10 for x10 in interval(ZERO, TEN, ONE) if x10 != x8)
        x10 = sample(x9, THREE)
        gi = canvas(x8, GRID_SHAPE_8E5C0C38)
        go = canvas(x8, GRID_SHAPE_8E5C0C38)
        for x11, (x12, x13) in zip(x10, x4):
            gi = fill(gi, x11, x12)
            go = fill(go, x11, x13)
        if verify_8e5c0c38(gi) != go:
            continue
        return {"input": gi, "output": go}
