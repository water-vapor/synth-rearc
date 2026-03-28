from synth_rearc.core import *


GRID_SIZES_E4941B18 = (7, 9, 11, 13, 15, 17, 19)


def _rectangle_patch_e4941b18(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    rows = interval(top, top + height_value, ONE)
    cols = interval(left, left + width_value, ONE)
    return product(rows, cols)


def generate_e4941b18(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        size_idx = unifint(diff_lb, diff_ub, (ZERO, len(GRID_SIZES_E4941B18) - ONE))
        grid_size = GRID_SIZES_E4941B18[size_idx]
        rect_height = unifint(diff_lb, diff_ub, (FOUR, grid_size - TWO))
        rect_width = unifint(diff_lb, diff_ub, (THREE, grid_size - ONE))
        rect_area = rect_height * rect_width
        if TWO * rect_area >= grid_size * grid_size - TWO:
            continue
        place_right = choice((T, F))
        if place_right:
            left_limit = grid_size - rect_width - ONE
            if left_limit < ZERO:
                continue
            rect_left = unifint(diff_lb, diff_ub, (ZERO, left_limit))
        else:
            left_limit = grid_size - rect_width
            if left_limit < ONE:
                continue
            rect_left = unifint(diff_lb, diff_ub, (ONE, left_limit))
        rect_top = grid_size - rect_height
        rect_right = rect_left + rect_width - ONE
        rect_patch = _rectangle_patch_e4941b18(rect_top, rect_left, rect_height, rect_width)
        marker_cols = sorted(sample(interval(rect_left, rect_right + ONE, ONE), TWO))
        if place_right:
            two_col = marker_cols[0]
            eight_col = marker_cols[1]
            target_col = rect_right + ONE
        else:
            eight_col = marker_cols[0]
            two_col = marker_cols[1]
            target_col = rect_left - ONE
        marker_row = rect_top - ONE
        two_loc = astuple(marker_row, two_col)
        eight_loc = astuple(marker_row, eight_col)
        target_loc = astuple(lowermost(rect_patch), target_col)
        gi = canvas(SEVEN, (grid_size, grid_size))
        gi = fill(gi, FIVE, rect_patch)
        gi = fill(gi, TWO, initset(two_loc))
        gi = fill(gi, EIGHT, initset(eight_loc))
        go = fill(gi, SEVEN, initset(two_loc))
        go = fill(go, SEVEN, initset(eight_loc))
        go = fill(go, TWO, initset(eight_loc))
        go = fill(go, EIGHT, initset(target_loc))
        return {"input": gi, "output": go}
