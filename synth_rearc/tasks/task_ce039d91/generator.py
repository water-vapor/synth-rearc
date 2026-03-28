from synth_rearc.core import *

from .verifier import verify_ce039d91


GRID_SHAPE_CE039D91 = (TEN, TEN)
HALF_SHAPE_CE039D91 = (TEN, FIVE)
PAIR_COMPONENT_TYPES_CE039D91 = (
    "interval",
    "interval",
    "interval",
    "column",
    "row",
)
PAIR_COL_POOL_CE039D91 = (ZERO, ONE, TWO, TWO, THREE, THREE, THREE, FOUR, FOUR, FOUR, FOUR, FOUR)
NOISE_COL_POOL_CE039D91 = (ONE, TWO, THREE, THREE, FOUR, FOUR, FIVE, FIVE, SIX, SIX, SEVEN, NINE)
NOISE_FRAGMENT_TYPES_CE039D91 = (
    "cell",
    "cell",
    "cell",
    "hseg",
    "vseg",
)


def _mirror_ce039d91(
    loc: IntegerTuple,
) -> IntegerTuple:
    return (loc[0], subtract(NINE, loc[1]))


def _expand_half_patch_ce039d91(
    patch: Indices,
) -> Indices:
    x0 = set()
    for x1 in patch:
        x0.add(x1)
        x0.add(_mirror_ce039d91(x1))
    return frozenset(x0)


def _sample_half_component_ce039d91(
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    x0 = choice(PAIR_COMPONENT_TYPES_CE039D91)
    if equality(x0, "row"):
        x1 = randint(ZERO, decrement(TEN))
        x2 = choice((ONE, ONE, TWO, TWO, THREE))
        x3 = []
        while len(x3) < x2:
            x4 = choice(PAIR_COL_POOL_CE039D91)
            if x4 not in x3:
                x3.append(x4)
        return frozenset((x1, x4) for x4 in x3)
    x5 = randint(ZERO, decrement(TEN))
    x6 = choice(PAIR_COL_POOL_CE039D91)
    if equality(x0, "column"):
        x7 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x8 = min(TEN, add(x5, x7))
        return frozenset((x9, x6) for x9 in range(x5, x8))
    x10 = unifint(diff_lb, diff_ub, (ONE, THREE))
    x11 = unifint(diff_lb, diff_ub, (ONE, THREE))
    x12 = min(TEN, add(x5, x10))
    x13 = add(ONE, min(x6, decrement(x11)))
    x14 = add(ONE, x6)
    x15 = range(subtract(x14, x13), x14)
    return frozenset((x16, x17) for x16 in range(x5, x12) for x17 in x15)


def _sample_noise_fragment_ce039d91() -> Indices:
    x0 = choice(NOISE_FRAGMENT_TYPES_CE039D91)
    x1 = randint(ZERO, decrement(TEN))
    x2 = choice(NOISE_COL_POOL_CE039D91)
    if equality(x0, "cell"):
        return frozenset({(x1, x2)})
    if equality(x0, "vseg"):
        x3 = choice((TWO, TWO, THREE))
        x4 = randint(ZERO, subtract(TEN, x3))
        return frozenset((add(x4, x5), x2) for x5 in range(x3))
    x6 = choice((TWO, TWO, THREE))
    x7 = randint(ZERO, subtract(TEN, x6))
    return frozenset((x1, add(x7, x8)) for x8 in range(x6))


def _valid_noise_fragment_ce039d91(
    frag: Indices,
    paired: Indices,
    noise: Indices,
) -> Boolean:
    x0 = toindices(paired)
    x1 = toindices(noise)
    for x2 in frag:
        x3 = _mirror_ce039d91(x2)
        if x2 in x0 or x2 in x1:
            return F
        if x3 in x0 or x3 in x1 or x3 in frag:
            return F
    return T


def generate_ce039d91(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = set()
        x1 = unifint(diff_lb, diff_ub, (TWO, FIVE))
        for _ in range(x1):
            x2 = _sample_half_component_ce039d91(diff_lb, diff_ub)
            x0 |= set(x2)
        x3 = any(equality(x4[1], FOUR) for x4 in x0)
        x4 = {x5: ZERO for x5 in range(TEN)}
        for x5, _ in x0:
            x4[x5] = increment(x4[x5])
        x7 = tuple(x4[x8] for x8 in range(TEN))
        if flip(x3):
            continue
        if any(greater(x8, THREE) for x8 in x7):
            continue
        x8 = _expand_half_patch_ce039d91(frozenset(x0))
        if len(x8) < EIGHT or len(x8) > 22:
            continue
        x9 = set()
        x10 = unifint(diff_lb, diff_ub, (THREE, SEVEN))
        x11 = ZERO
        while len(x9) < x10 and x11 < 120:
            x11 = increment(x11)
            x12 = _sample_noise_fragment_ce039d91()
            if flip(_valid_noise_fragment_ce039d91(x12, x8, frozenset(x9))):
                continue
            x9 |= set(x12)
        if len(x9) < THREE:
            continue
        x13 = combine(x8, frozenset(x9))
        x14 = {x15: ZERO for x15 in range(TEN)}
        for x15, _ in x13:
            x14[x15] = increment(x14[x15])
        x15 = tuple(x14[x16] for x16 in range(TEN))
        x16 = max(x15)
        x17 = sum(ONE for x18 in x15 if equality(x18, ZERO))
        if greater(x16, SIX):
            continue
        if greater(FOUR, x16):
            continue
        if x17 < ONE:
            continue
        x18 = canvas(ZERO, GRID_SHAPE_CE039D91)
        x19 = fill(x18, FIVE, x13)
        x20 = fill(x19, ONE, x8)
        if equality(x19, x20):
            continue
        if verify_ce039d91(x19) != x20:
            continue
        return {"input": x19, "output": x20}
