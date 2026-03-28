from synth_rearc.core import *


def _rect_patch_d968ffd4(height_: Integer, width_: Integer) -> Indices:
    rows = interval(ZERO, height_, ONE)
    cols = interval(ZERO, width_, ONE)
    return product(rows, cols)


def _extend_gap_d968ffd4(grid: Grid, obj_a: Object, obj_b: Object) -> Grid:
    if hmatching(obj_a, obj_b):
        left = argmin((obj_a, obj_b), leftmost)
        right = argmax((obj_a, obj_b), leftmost)
        start = increment(rightmost(left))
        stop = leftmost(right)
        half = divide(subtract(stop, start), TWO)
        rows = interval(ZERO, height(grid), ONE)
        left_patch = product(rows, interval(start, add(start, half), ONE))
        right_patch = product(rows, interval(subtract(stop, half), stop, ONE))
        grid = fill(grid, color(left), left_patch)
        return fill(grid, color(right), right_patch)
    top = argmin((obj_a, obj_b), uppermost)
    bottom = argmax((obj_a, obj_b), uppermost)
    start = increment(lowermost(top))
    stop = uppermost(bottom)
    half = divide(subtract(stop, start), TWO)
    cols = interval(ZERO, width(grid), ONE)
    top_patch = product(interval(start, add(start, half), ONE), cols)
    bottom_patch = product(interval(subtract(stop, half), stop, ONE), cols)
    grid = fill(grid, color(top), top_patch)
    return fill(grid, color(bottom), bottom_patch)


def generate_d968ffd4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    bgc, cola, colb = sample(interval(ONE, TEN, ONE), THREE)
    horizontal = choice((T, F))
    if horizontal:
        marker_h = unifint(diff_lb, diff_ub, (TWO, FOUR))
        marker_w = unifint(diff_lb, diff_ub, (ONE, THREE))
        gap = unifint(diff_lb, diff_ub, (FIVE, 18))
        h = add(marker_h, TWO)
        w = add(add(double(marker_w), gap), TWO)
        left_patch = shift(_rect_patch_d968ffd4(marker_h, marker_w), (ONE, ONE))
        right_left = add(add(ONE, marker_w), gap)
        right_patch = shift(_rect_patch_d968ffd4(marker_h, marker_w), (ONE, right_left))
    else:
        marker_h = unifint(diff_lb, diff_ub, (ONE, THREE))
        marker_w = unifint(diff_lb, diff_ub, (TWO, SIX))
        gap = unifint(diff_lb, diff_ub, (FIVE, 18))
        h = add(add(double(marker_h), gap), TWO)
        w = add(marker_w, TWO)
        left_patch = shift(_rect_patch_d968ffd4(marker_h, marker_w), (ONE, ONE))
        right_top = add(add(ONE, marker_h), gap)
        right_patch = shift(_rect_patch_d968ffd4(marker_h, marker_w), (right_top, ONE))
    gi = canvas(bgc, (h, w))
    obj_a = recolor(cola, left_patch)
    obj_b = recolor(colb, right_patch)
    gi = paint(gi, obj_a)
    gi = paint(gi, obj_b)
    go = _extend_gap_d968ffd4(gi, obj_a, obj_b)
    return {"input": gi, "output": go}
