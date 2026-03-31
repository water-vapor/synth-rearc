from __future__ import annotations

from synth_rearc.core import *

from .helpers import apply_rule_8b9c3697
from .helpers import oriented_shape_8b9c3697
from .helpers import patch_sort_key_8b9c3697
from .helpers import rectangle_patch_8b9c3697
from .helpers import route_specs_8b9c3697
from .helpers import scale_vector_8b9c3697
from .helpers import SIDE_TO_OUTWARD_8B9C3697


BACKGROUND_COLORS_8B9C3697 = (THREE, FOUR)
SHAPE_KINDS_8B9C3697 = ("a", "b")
SIDES_8B9C3697 = ("top", "right", "bottom", "left")
DECOY_SHAPES_8B9C3697 = (
    (ONE, ONE),
    (ONE, TWO),
    (TWO, ONE),
    (TWO, TWO),
    (TWO, THREE),
    (THREE, TWO),
)


def _shift_many_8b9c3697(
    patches: tuple[Patch, ...],
    offset: IntegerTuple,
) -> tuple[Indices, ...]:
    return tuple(shift(toindices(x0), offset) for x0 in patches)


def _bounded_halo_8b9c3697(
    patch: Patch,
    height_value: Integer,
    width_value: Integer,
    padding: Integer,
) -> Indices:
    x0 = max(ZERO, uppermost(patch) - padding)
    x1 = max(ZERO, leftmost(patch) - padding)
    x2 = min(height_value - ONE, lowermost(patch) + padding)
    x3 = min(width_value - ONE, rightmost(patch) + padding)
    return rectangle_patch_8b9c3697(x0, x1, x2 - x0 + ONE, x3 - x1 + ONE)


def _within_grid_8b9c3697(
    patch: Patch,
    height_value: Integer,
    width_value: Integer,
) -> Boolean:
    x0 = toindices(patch)
    return both(
        both(ZERO <= uppermost(x0), ZERO <= leftmost(x0)),
        both(lowermost(x0) < height_value, rightmost(x0) < width_value),
    )


def _choose_shape_params_8b9c3697() -> tuple[str, str, Integer, Integer]:
    x0 = choice(SHAPE_KINDS_8B9C3697)
    x1 = choice(SIDES_8B9C3697)
    if x0 == "a":
        x2 = ONE
        x3 = choice((ONE, TWO))
    else:
        x2 = choice((TWO, THREE))
        x3 = ONE
    return x0, x1, x2, x3


def _minimum_outward_steps_8b9c3697(
    final_patch: Patch,
    obj_patch: Patch,
    side: str,
) -> Integer:
    if side == "top":
        return uppermost(final_patch) - uppermost(obj_patch) + ONE
    if side == "bottom":
        return lowermost(obj_patch) - lowermost(final_patch) + ONE
    if side == "left":
        return leftmost(final_patch) - leftmost(obj_patch) + ONE
    return rightmost(obj_patch) - rightmost(final_patch) + ONE


def _sample_shape_bundle_8b9c3697(
    height_value: Integer,
    width_value: Integer,
    active: Boolean,
) -> tuple[Indices, Indices | None, str]:
    x0, x1, x2, x3 = _choose_shape_params_8b9c3697()
    x4, x5 = oriented_shape_8b9c3697(x0, x1, x2, x3)
    if not active:
        return x4, None, x1
    x6 = SIDE_TO_OUTWARD_8B9C3697[x1]
    x7 = _minimum_outward_steps_8b9c3697(x5, x4, x1)
    x8 = max(height(x4), width(x4))
    x9 = randint(x7 + TWO, x7 + x8 + FOUR)
    x10 = shift(x5, scale_vector_8b9c3697(x6, x9))
    x11 = x4 | x10
    x12 = invert(ulcorner(x11))
    x13, x14 = _shift_many_8b9c3697((x4, x10), x12)
    if not _within_grid_8b9c3697(x13, height_value, width_value):
        return _sample_shape_bundle_8b9c3697(height_value, width_value, active)
    if not _within_grid_8b9c3697(x14, height_value, width_value):
        return _sample_shape_bundle_8b9c3697(height_value, width_value, active)
    return x13, x14, x1


def _try_place_patch_8b9c3697(
    patch: Patch,
    height_value: Integer,
    width_value: Integer,
    reserved: Indices,
    padding: Integer,
) -> Indices | None:
    x0 = height(patch)
    x1 = width(patch)
    if x0 > height_value or x1 > width_value:
        return None
    x2 = tuple((i, j) for i in range(height_value - x0 + ONE) for j in range(width_value - x1 + ONE))
    x3 = sample(x2, len(x2))
    for x4 in x3:
        x5 = shift(patch, x4)
        x6 = _bounded_halo_8b9c3697(x5, height_value, width_value, padding)
        if len(intersection(x6, reserved)) != ZERO:
            continue
        return x5
    return None


def _paint_shape_8b9c3697(
    grid: Grid,
    patch: Patch,
    value: Integer,
) -> Grid:
    return paint(grid, recolor(value, patch))


def _paint_marker_8b9c3697(
    grid: Grid,
    patch: Patch,
) -> Grid:
    return fill(grid, TWO, patch)


def _route_marker_set_8b9c3697(
    grid: Grid,
) -> frozenset[Indices]:
    x0 = route_specs_8b9c3697(grid)
    return frozenset(x1 for x1, _, _, _ in x0)


def generate_8b9c3697(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = randint(19, 27)
        x1 = randint(22, 29)
        x2 = choice(BACKGROUND_COLORS_8B9C3697)
        x3 = tuple(x4 for x4 in remove(ZERO, interval(ZERO, TEN, ONE)) if x4 != TWO and x4 != x2)
        x4 = randint(TWO, THREE)
        x5 = tuple(choice((T, T, F)) for _ in range(x4))
        if not any(x5):
            x5 = (T,) + x5[ONE:]
        x6 = canvas(x2, (x0, x1))
        x7 = frozenset()
        x8 = []
        x9 = []
        x10 = T
        for x11 in x5:
            x12, x13, _ = _sample_shape_bundle_8b9c3697(x0, x1, x11)
            x14 = x12 if x13 is None else x12 | x13
            x15 = _try_place_patch_8b9c3697(x14, x0, x1, x7, ONE)
            if x15 is None:
                x10 = F
                break
            x16 = subtract(ulcorner(x15), ulcorner(x14))
            x17 = shift(x12, x16)
            x18 = None if x13 is None else shift(x13, x16)
            x19 = choice(x3)
            x6 = _paint_shape_8b9c3697(x6, x17, x19)
            x8.append(x17)
            x7 = x7 | _bounded_halo_8b9c3697(x17, x0, x1, ONE)
            if x18 is not None:
                x6 = _paint_marker_8b9c3697(x6, x18)
                x9.append(x18)
                x7 = x7 | _bounded_halo_8b9c3697(x18, x0, x1, ONE)
        if not x10:
            continue
        x20 = randint(THREE, EIGHT)
        for _ in range(x20):
            x21, x22 = choice(DECOY_SHAPES_8B9C3697)
            x23 = rectangle_patch_8b9c3697(ZERO, ZERO, x21, x22)
            x24 = _try_place_patch_8b9c3697(x23, x0, x1, x7, ONE)
            if x24 is None:
                continue
            x6 = _paint_marker_8b9c3697(x6, x24)
            x7 = x7 | _bounded_halo_8b9c3697(x24, x0, x1, ONE)
        x25 = _route_marker_set_8b9c3697(x6)
        x26 = frozenset(x27 for x27 in x9)
        if x25 != x26:
            continue
        x27 = apply_rule_8b9c3697(x6)
        if x27 == x6:
            continue
        if route_specs_8b9c3697(x6) == tuple():
            continue
        return {"input": x6, "output": x27}
