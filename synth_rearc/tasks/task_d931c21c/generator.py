from synth_rearc.core import *

from .helpers import cycle_bands_d931c21c
from .helpers import make_cycle_patch_d931c21c
from .helpers import make_open_patch_d931c21c


def _shape_steps_d931c21c(
    height_value: Integer,
    width_value: Integer,
    diff_lb: float,
    diff_ub: float,
) -> Integer:
    x0 = max(ONE, subtract(add(height_value, width_value), FIVE))
    x1 = min(add(x0, THREE), multiply(TWO, minimum((height_value, width_value))))
    return unifint(diff_lb, diff_ub, (ONE, x1))


def _cycle_footprint_d931c21c(
    patch: Patch,
) -> Indices:
    x0, x1 = cycle_bands_d931c21c(patch)
    return frozenset(combine(toindices(patch), combine(x0, x1)))


def _expand_footprint_d931c21c(
    patch: Patch,
) -> Indices:
    x0 = set(toindices(patch))
    for x1 in tuple(x0):
        for x2 in neighbors(x1):
            x0.add(x2)
    return frozenset(x0)


def _clip_patch_d931c21c(
    patch: Patch,
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = dims
    return frozenset(
        (x2, x3) for x2, x3 in toindices(patch) if ZERO <= x2 < x0 and ZERO <= x3 < x1
    )


def _sample_anchor_d931c21c(
    limit: Integer,
) -> Integer:
    if limit <= ZERO:
        return ZERO
    if randint(ZERO, FOUR) == ZERO:
        return choice((ZERO, limit))
    return randint(ZERO, limit)


def _shape_spec_d931c21c(
    diff_lb: float,
    diff_ub: float,
    kind: str,
) -> tuple[Indices, Boolean]:
    while True:
        x0 = unifint(diff_lb, diff_ub, (THREE, TEN))
        x1 = unifint(diff_lb, diff_ub, (THREE, TEN))
        x2 = _shape_steps_d931c21c(x0, x1, diff_lb, diff_ub)
        if kind == "cycle":
            x3 = make_cycle_patch_d931c21c(x0, x1, x2)
            return x3, T
        if kind == "open":
            x4 = make_open_patch_d931c21c(x0, x1, x2)
            return x4, F
        return frozenset({(ZERO, ZERO)}), F


def _place_shapes_d931c21c(
    dims: IntegerTuple,
    specs: Tuple,
) -> Tuple:
    x0, x1 = dims
    x2 = set()
    x3 = []
    for x4, x5 in specs:
        x6 = _cycle_footprint_d931c21c(x4) if x5 else toindices(x4)
        x7 = _expand_footprint_d931c21c(x6)
        x8, x9 = shape(x4)
        x10 = subtract(x0, x8)
        x11 = subtract(x1, x9)
        x12 = F
        for _ in range(400):
            x13 = _sample_anchor_d931c21c(x10)
            x14 = _sample_anchor_d931c21c(x11)
            x15 = shift(x4, (x13, x14))
            x16 = _clip_patch_d931c21c(shift(x7, (x13, x14)), dims)
            if any(x17 in x2 for x17 in x16):
                continue
            x2 |= set(x16)
            x3.append((x15, x5))
            x12 = T
            break
        if not x12:
            return ()
    return tuple(x3)


def _build_input_d931c21c(
    dims: IntegerTuple,
    placed: Tuple,
) -> Grid:
    x0 = canvas(ZERO, dims)
    for x1, _ in placed:
        x0 = fill(x0, ONE, x1)
    return x0


def _build_output_d931c21c(
    gi: Grid,
    placed: Tuple,
) -> Grid:
    x0 = gi
    x1 = ofcolor(gi, ZERO)
    for x2, x3 in placed:
        if not x3:
            continue
        x4, x5 = cycle_bands_d931c21c(x2)
        x6 = ulcorner(x2)
        x7 = shift(x4, x6)
        x8 = shift(x5, x6)
        x9 = intersection(x7, x1)
        x10 = difference(intersection(x8, x1), x9)
        x0 = fill(x0, THREE, x9)
        x0 = fill(x0, TWO, x10)
    return x0


def generate_d931c21c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (10, 30))
        x1 = unifint(diff_lb, diff_ub, (10, 30))
        x2 = unifint(diff_lb, diff_ub, (ONE, THREE))
        x3 = unifint(diff_lb, diff_ub, (ZERO, THREE))
        x4 = randint(ZERO, ONE)
        x5 = [("cycle",) for _ in range(x2)]
        x5.extend(("open",) for _ in range(x3))
        x5.extend(("dot",) for _ in range(x4))
        shuffle(x5)
        x6 = []
        for x7, in x5:
            x6.append(_shape_spec_d931c21c(diff_lb, diff_ub, x7))
        x8 = _place_shapes_d931c21c((x0, x1), tuple(x6))
        if len(x8) == ZERO:
            continue
        gi = _build_input_d931c21c((x0, x1), x8)
        go = _build_output_d931c21c(gi, x8)
        x9 = colorcount(go, TWO)
        x10 = colorcount(go, THREE)
        x11 = multiply(x0, x1)
        if x9 == ZERO or x10 == ZERO:
            continue
        if add(x9, x10) * SIX > x11 * FIVE:
            continue
        if colorcount(gi, ONE) * EIGHT < add(x9, x10):
            continue
        return {"input": gi, "output": go}
