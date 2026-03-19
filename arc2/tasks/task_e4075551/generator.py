from arc2.core import *


SIDE_COLORS_E4075551 = remove(FIVE, remove(TWO, remove(ZERO, interval(ZERO, TEN, ONE))))
GRID_BOUNDS_E4075551 = (14, 18)
RECT_H_BOUNDS_E4075551 = (8, 13)
RECT_W_BOUNDS_E4075551 = (8, 13)


def generate_e4075551(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = unifint(diff_lb, diff_ub, GRID_BOUNDS_E4075551)
        w = unifint(diff_lb, diff_ub, GRID_BOUNDS_E4075551)
        rect_h = unifint(diff_lb, diff_ub, (RECT_H_BOUNDS_E4075551[ZERO], min(RECT_H_BOUNDS_E4075551[ONE], h - TWO)))
        rect_w = unifint(diff_lb, diff_ub, (RECT_W_BOUNDS_E4075551[ZERO], min(RECT_W_BOUNDS_E4075551[ONE], w - TWO)))
        if rect_h < FIVE or rect_w < FIVE:
            continue
        top = randint(ONE, h - rect_h - ONE)
        left = randint(ONE, w - rect_w - ONE)
        bottom = top + rect_h - ONE
        right = left + rect_w - ONE
        inner_rows = interval(top + ONE, bottom, ONE)
        inner_cols = interval(left + ONE, right, ONE)
        center_row = choice(inner_rows)
        center_col = choice(inner_cols)
        top_col = center_col if choice((T, F)) else choice(inner_cols)
        bottom_col = center_col if choice((T, F)) else choice(inner_cols)
        left_row = center_row if choice((T, F)) else choice(inner_rows)
        right_row = center_row if choice((T, F)) else choice(inner_rows)
        colors = sample(SIDE_COLORS_E4075551, FOUR)
        gi = canvas(ZERO, (h, w))
        gi = fill(gi, colors[ZERO], initset((top, top_col)))
        gi = fill(gi, colors[ONE], initset((bottom, bottom_col)))
        gi = fill(gi, colors[TWO], initset((left_row, left)))
        gi = fill(gi, colors[THREE], initset((right_row, right)))
        gi = fill(gi, TWO, initset((center_row, center_col)))
        go = canvas(ZERO, (h, w))
        go = fill(go, colors[ZERO], connect((top, left), (top, right)))
        go = fill(go, colors[ONE], connect((bottom, left), (bottom, right)))
        go = fill(go, colors[TWO], connect((top + ONE, left), (bottom - ONE, left)))
        go = fill(go, colors[THREE], connect((top + ONE, right), (bottom - ONE, right)))
        go = fill(go, FIVE, connect((top + ONE, center_col), (bottom - ONE, center_col)))
        go = fill(go, FIVE, connect((center_row, left + ONE), (center_row, right - ONE)))
        go = paint(go, merge(objects(gi, T, F, T)))
        return {"input": gi, "output": go}
