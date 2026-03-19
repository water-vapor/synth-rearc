from arc2.core import *

from .helpers import (
    HORIZONTAL_SIDES_DC2E9A9D,
    VERTICAL_SIDES_DC2E9A9D,
    make_tabbed_frame_dc2e9a9d,
    mirrored_copy_dc2e9a9d,
    object_dims_dc2e9a9d,
)


HORIZONTAL_FRAME_SPECS_DC2E9A9D = (
    (THREE, THREE),
    (THREE, FOUR),
    (THREE, FIVE),
    (FIVE, THREE),
    (FIVE, FOUR),
    (FIVE, FIVE),
)

VERTICAL_FRAME_SPECS_DC2E9A9D = (
    (THREE, THREE),
    (THREE, FIVE),
    (FOUR, THREE),
    (FOUR, FIVE),
)


def _placement_bounds_dc2e9a9d(
    grid_h: Integer,
    grid_w: Integer,
    side: IntegerTuple,
    obj_h: Integer,
    obj_w: Integer,
) -> Tuple[Integer, Integer, Integer, Integer]:
    if side == LEFT:
        return ZERO, subtract(grid_h, obj_h), ZERO, subtract(grid_w, add(add(obj_w, obj_w), ONE))
    if side == RIGHT:
        return ZERO, subtract(grid_h, obj_h), add(obj_w, ONE), subtract(grid_w, obj_w)
    if side == UP:
        return ZERO, subtract(grid_h, add(add(obj_h, obj_h), ONE)), ZERO, subtract(grid_w, obj_w)
    return add(obj_h, ONE), subtract(grid_h, obj_h), ZERO, subtract(grid_w, obj_w)


def _padded_footprint_dc2e9a9d(
    obj: Object,
    copy_obj: Object,
) -> Indices:
    x0 = combine(toindices(obj), toindices(copy_obj))
    x1 = interval(subtract(uppermost(x0), ONE), add(lowermost(x0), TWO), ONE)
    x2 = interval(subtract(leftmost(x0), ONE), add(rightmost(x0), TWO), ONE)
    return product(x1, x2)


def generate_dc2e9a9d(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        grid_h = unifint(diff_lb, diff_ub, (18, 30))
        grid_w = unifint(diff_lb, diff_ub, (18, 30))
        num_objects = unifint(diff_lb, diff_ub, (TWO, FOUR))
        sides = [
            choice(tuple(HORIZONTAL_SIDES_DC2E9A9D)),
            choice(tuple(VERTICAL_SIDES_DC2E9A9D)),
        ]
        while len(sides) < num_objects:
            sides.append(choice((LEFT, RIGHT, UP, DOWN)))
        shuffle(sides)
        occupied = frozenset()
        placed = []
        success = True
        for side in sides:
            specs = choice(HORIZONTAL_FRAME_SPECS_DC2E9A9D if side in HORIZONTAL_SIDES_DC2E9A9D else VERTICAL_FRAME_SPECS_DC2E9A9D)
            frame_h, frame_w = specs
            obj_h, obj_w = object_dims_dc2e9a9d(side, frame_h, frame_w)
            min_top, max_top, min_left, max_left = _placement_bounds_dc2e9a9d(grid_h, grid_w, side, obj_h, obj_w)
            if min_top > max_top or min_left > max_left:
                success = False
                break
            found = False
            for _ in range(multiply(grid_h, grid_w)):
                top = randint(min_top, max_top)
                left = randint(min_left, max_left)
                obj = make_tabbed_frame_dc2e9a9d(top, left, side, frame_h, frame_w)
                copy_obj = mirrored_copy_dc2e9a9d(obj)
                footprint = _padded_footprint_dc2e9a9d(obj, copy_obj)
                if intersection(footprint, occupied):
                    continue
                occupied = combine(occupied, footprint)
                placed.append((obj, copy_obj))
                found = True
                break
            if not found:
                success = False
                break
        if not success:
            continue
        gi = canvas(ZERO, (grid_h, grid_w))
        go = canvas(ZERO, (grid_h, grid_w))
        for obj, copy_obj in placed:
            gi = paint(gi, obj)
            go = paint(go, obj)
            go = paint(go, copy_obj)
        x0 = colorcount(gi, THREE)
        x1 = multiply(grid_h, grid_w)
        if x0 * 25 < x1:
            continue
        if x0 * SIX > x1:
            continue
        if colorcount(go, ONE) == ZERO or colorcount(go, EIGHT) == ZERO:
            continue
        return {"input": gi, "output": go}
