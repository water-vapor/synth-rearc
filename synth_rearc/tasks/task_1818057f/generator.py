from __future__ import annotations

from synth_rearc.core import *

from .verifier import verify_1818057f


DISTRACTOR_SHAPES_1818057F = (
    frozenset({(ZERO, ZERO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (TWO, ZERO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO), (ONE, ZERO)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (TWO, ZERO), (TWO, ONE)}),
    frozenset(
        {
            (ZERO, ZERO),
            (ZERO, ONE),
            (ZERO, TWO),
            (ONE, ZERO),
            (ONE, ONE),
            (ONE, TWO),
        }
    ),
)

STRUCTURED_ROWS_1818057F = (
    "plus",
    "plus",
    "tail",
    "tail",
    "square",
    "square",
    "domino_h",
    "domino_v",
    "bar3_h",
    "bar3_v",
    "el",
)

CELL_SHAPES_1818057F = {
    "square": frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE)}),
    "domino_h": frozenset({(ZERO, ZERO), (ZERO, ONE)}),
    "domino_v": frozenset({(ZERO, ZERO), (ONE, ZERO)}),
    "bar3_h": frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO)}),
    "bar3_v": frozenset({(ZERO, ZERO), (ONE, ZERO), (TWO, ZERO)}),
    "el": frozenset({(ZERO, ZERO), (ONE, ZERO), (TWO, ZERO), (TWO, ONE)}),
}


def _vec_add_1818057f(
    a: IntegerTuple,
    b: IntegerTuple,
) -> IntegerTuple:
    return (a[ZERO] + b[ZERO], a[ONE] + b[ONE])


def _vec_scale_1818057f(
    direction: IntegerTuple,
    amount: Integer,
) -> IntegerTuple:
    return (direction[ZERO] * amount, direction[ONE] * amount)


def _plus_patch_1818057f(
    center: IntegerTuple,
) -> Indices:
    return frozenset(
        {
            center,
            _vec_add_1818057f(center, UP),
            _vec_add_1818057f(center, DOWN),
            _vec_add_1818057f(center, LEFT),
            _vec_add_1818057f(center, RIGHT),
        }
    )


def _tail_component_1818057f(
    center: IntegerTuple,
    direction: IntegerTuple,
    tail_length: Integer,
) -> tuple[Indices, Indices]:
    x0 = _plus_patch_1818057f(center)
    x1 = _vec_add_1818057f(center, direction)
    x2 = _vec_add_1818057f(center, _vec_scale_1818057f(direction, tail_length + ONE))
    x3 = connect(x1, x2)
    x4 = combine(x0, x3)
    return x4, x0


def _chain_component_1818057f(
    start_center: IntegerTuple,
    direction: IntegerTuple,
    n_pluses: Integer,
    step: Integer,
    tail_length: Integer,
) -> tuple[Indices, Indices]:
    x0 = tuple(
        _vec_add_1818057f(start_center, _vec_scale_1818057f(direction, step * x1))
        for x1 in range(n_pluses)
    )
    x2 = frozenset()
    for x3 in x0:
        x4 = _plus_patch_1818057f(x3)
        x2 = combine(x2, x4)
    x5 = x2
    x6 = (-direction[ZERO], -direction[ONE])
    for x7, x8 in zip(x0, x0[ONE:]):
        x9 = _vec_add_1818057f(x7, direction)
        x10 = _vec_add_1818057f(x8, x6)
        x11 = connect(x9, x10)
        x5 = combine(x5, x11)
    if tail_length > ZERO:
        x12 = x0[-1]
        x13 = _vec_add_1818057f(x12, direction)
        x14 = _vec_add_1818057f(x12, _vec_scale_1818057f(direction, tail_length + ONE))
        x15 = connect(x13, x14)
        x5 = combine(x5, x15)
    return x5, x2


def _in_bounds_1818057f(
    patch: Indices,
    height_value: Integer,
    width_value: Integer,
) -> Boolean:
    return all(ZERO <= i < height_value and ZERO <= j < width_value for i, j in patch)


def _orthopad_1818057f(
    patch: Indices,
) -> Indices:
    x0 = set(patch)
    for x1 in patch:
        x0.update(dneighbors(x1))
    return frozenset(x0)


def _placeable_1818057f(
    patch: Indices,
    occupied: Indices,
    height_value: Integer,
    width_value: Integer,
) -> Boolean:
    if not _in_bounds_1818057f(patch, height_value, width_value):
        return False
    x0 = _orthopad_1818057f(occupied)
    return len(intersection(patch, x0)) == ZERO


def _shape_dims_1818057f(
    patch: Indices,
) -> IntegerTuple:
    x0 = max(i for i, _ in patch) + ONE
    x1 = max(j for _, j in patch) + ONE
    return (x0, x1)


def _cell_patch_1818057f(
    kind: str,
    origin: IntegerTuple,
) -> tuple[Indices, Indices]:
    if kind == "plus":
        x0 = _vec_add_1818057f(origin, (TWO, TWO))
        x1 = _plus_patch_1818057f(x0)
        return x1, x1
    if kind == "tail":
        x2 = _vec_add_1818057f(origin, (TWO, TWO))
        x3 = choice((UP, DOWN, LEFT, RIGHT))
        return _tail_component_1818057f(x2, x3, ONE)
    x4 = CELL_SHAPES_1818057F[kind]
    x5, x6 = _shape_dims_1818057f(x4)
    x7 = randint(ZERO, FIVE - x5)
    x8 = randint(ZERO, FIVE - x6)
    x9 = shift(x4, _vec_add_1818057f(origin, (x7, x8)))
    return x9, frozenset()


def _random_plus_component_1818057f(
    height_value: Integer,
    width_value: Integer,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Indices, Indices] | None:
    for _ in range(80):
        x0 = choice(("plus", "tail", "tail", "chain", "chain"))
        x1 = (randint(ONE, height_value - TWO), randint(ONE, width_value - TWO))
        if x0 == "plus":
            x2 = _plus_patch_1818057f(x1)
            if _in_bounds_1818057f(x2, height_value, width_value):
                return x2, x2
            continue
        if x0 == "tail":
            x3 = choice((UP, DOWN, LEFT, RIGHT))
            x4 = unifint(diff_lb, diff_ub, (ONE, THREE))
            x5, x6 = _tail_component_1818057f(x1, x3, x4)
            if _in_bounds_1818057f(x5, height_value, width_value):
                return x5, x6
            continue
        x7 = choice((DOWN, RIGHT))
        x8 = choice((TWO, TWO, THREE))
        x9 = choice((FOUR, FOUR, FIVE, SIX))
        x10 = choice((ZERO, ZERO, ONE, TWO))
        x11, x12 = _chain_component_1818057f(x1, x7, x8, x9, x10)
        if _in_bounds_1818057f(x11, height_value, width_value):
            return x11, x12
    return None


def _random_distractor_1818057f(
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    x0 = choice(DISTRACTOR_SHAPES_1818057F)
    x1, x2 = _shape_dims_1818057f(x0)
    x3 = randint(ZERO, height_value - x1)
    x4 = randint(ZERO, width_value - x2)
    return shift(x0, (x3, x4))


def _build_structured_1818057f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (TWO, FOUR))
    x1 = unifint(diff_lb, diff_ub, (TWO, FOUR))
    x2 = randint(ZERO, TWO)
    x3 = randint(ZERO, TWO)
    x4 = randint(ZERO, TWO)
    x5 = randint(ZERO, TWO)
    x6 = x2 + x4 + x0 * SIX - ONE
    x7 = x3 + x5 + x1 * SIX - ONE
    x8 = [choice(STRUCTURED_ROWS_1818057F) for _ in range(x0)]
    if not any(x9 in ("plus", "tail") for x9 in x8):
        x8[randint(ZERO, x0 - ONE)] = choice(("plus", "tail"))
    x10 = frozenset()
    x11 = frozenset()
    for x12, x13 in enumerate(x8):
        for x14 in range(x1):
            x15 = (x2 + x12 * SIX, x3 + x14 * SIX)
            x16, x17 = _cell_patch_1818057f(x13, x15)
            x10 = combine(x10, x16)
            x11 = combine(x11, x17)
    x18 = fill(canvas(TWO, (x6, x7)), FOUR, x10)
    x19 = fill(x18, EIGHT, x11)
    return {"input": x18, "output": x19}


def _build_freeform_1818057f(
    diff_lb: float,
    diff_ub: float,
) -> dict | None:
    x0 = unifint(diff_lb, diff_ub, (TEN, 22))
    x1 = unifint(diff_lb, diff_ub, (TEN, 22))
    x2 = frozenset()
    x3 = frozenset()
    x4 = unifint(diff_lb, diff_ub, (ONE, min(FOUR, max(TWO, max(x0, x1) // SIX))))
    for _ in range(x4):
        x5 = False
        for _ in range(100):
            x6 = _random_plus_component_1818057f(x0, x1, diff_lb, diff_ub)
            if x6 is None:
                continue
            x7, x8 = x6
            if not _placeable_1818057f(x7, x2, x0, x1):
                continue
            x2 = combine(x2, x7)
            x3 = combine(x3, x8)
            x5 = True
            break
        if not x5:
            return None
    x9 = max(THREE, min(12, x0 * x1 // 18))
    x10 = randint(THREE, x9)
    for _ in range(x10):
        for _ in range(80):
            x11 = _random_distractor_1818057f(x0, x1)
            if not _placeable_1818057f(x11, x2, x0, x1):
                continue
            x2 = combine(x2, x11)
            break
    x12 = fill(canvas(TWO, (x0, x1)), FOUR, x2)
    x13 = fill(x12, EIGHT, x3)
    return {"input": x12, "output": x13}


def generate_1818057f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(("freeform", "freeform", "structured"))
        x1 = _build_structured_1818057f(diff_lb, diff_ub) if x0 == "structured" else _build_freeform_1818057f(diff_lb, diff_ub)
        if x1 is None:
            continue
        x2 = x1["input"]
        x3 = x1["output"]
        if verify_1818057f(x2) != x3:
            continue
        if x2 == x3:
            continue
        return x1
