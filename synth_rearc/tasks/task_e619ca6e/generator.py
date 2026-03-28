from synth_rearc.core import *


RECT_DIMS_E619CA6E = (
    (TWO, THREE),
    (TWO, THREE),
    (THREE, THREE),
    (FOUR, TWO),
    (FOUR, TWO),
    (TWO, FIVE),
)


def _rectangle_patch_e619ca6e(
    top: Integer,
    left: Integer,
    obj_h: Integer,
    obj_w: Integer,
) -> Indices:
    rows = interval(top, add(top, obj_h), ONE)
    cols = interval(left, add(left, obj_w), ONE)
    return product(rows, cols)


def _padded_patch_e619ca6e(
    top: Integer,
    left: Integer,
    obj_h: Integer,
    obj_w: Integer,
) -> Indices:
    rows = interval(subtract(top, ONE), add(add(top, obj_h), ONE), ONE)
    cols = interval(subtract(left, ONE), add(add(left, obj_w), ONE), ONE)
    return product(rows, cols)


def _paint_cascade_e619ca6e(
    grid: Grid,
    patch: Indices,
) -> Grid:
    grid = fill(grid, THREE, patch)
    step_down = height(patch)
    step_side = width(patch)
    left_step = astuple(step_down, invert(step_side))
    right_step = astuple(step_down, step_side)
    for step in interval(ONE, increment(height(grid)), ONE):
        grid = fill(grid, THREE, shift(patch, multiply(left_step, step)))
        grid = fill(grid, THREE, shift(patch, multiply(right_step, step)))
    return grid


def generate_e619ca6e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        grid_h = unifint(diff_lb, diff_ub, (22, 30))
        grid_w = unifint(diff_lb, diff_ub, (22, 30))
        num_objects = unifint(diff_lb, diff_ub, (ONE, THREE))
        gi = canvas(ZERO, (grid_h, grid_w))
        occupied = frozenset()
        patches = []
        success = True
        for _ in range(num_objects):
            placed = False
            for _ in range(TWO * grid_h * grid_w):
                obj_h, obj_w = choice(RECT_DIMS_E619CA6E)
                max_top = min(subtract(divide(grid_h, TWO), ONE), subtract(subtract(grid_h, multiply(THREE, obj_h)), ONE))
                if max_top < ONE:
                    continue
                min_left = obj_w
                max_left = subtract(grid_w, multiply(TWO, obj_w))
                if min_left > max_left:
                    continue
                top = randint(ONE, max_top)
                left = randint(min_left, max_left)
                patch = _rectangle_patch_e619ca6e(top, left, obj_h, obj_w)
                padded = _padded_patch_e619ca6e(top, left, obj_h, obj_w)
                if intersection(padded, occupied):
                    continue
                gi = fill(gi, THREE, patch)
                occupied = combine(occupied, padded)
                patches.append(patch)
                placed = True
                break
            if not placed:
                success = False
                break
        if not success:
            continue
        go = canvas(ZERO, (grid_h, grid_w))
        for patch in patches:
            go = _paint_cascade_e619ca6e(go, patch)
        occ = colorcount(go, THREE)
        area = multiply(grid_h, grid_w)
        if occ * 20 < area:
            continue
        if occ * FIVE > multiply(area, TWO):
            continue
        return {"input": gi, "output": go}
