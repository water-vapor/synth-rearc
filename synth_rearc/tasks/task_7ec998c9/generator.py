from synth_rearc.core import *


SIDE_BOUNDS_7EC998C9 = (FIVE, TEN)
COLORS_7EC998C9 = remove(ONE, interval(ZERO, TEN, ONE))


def generate_7ec998c9(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    side = unifint(diff_lb, diff_ub, SIDE_BOUNDS_7EC998C9)
    marker_row = divide(decrement(side), TWO)
    candidate_cols = interval(TWO, subtract(side, TWO), ONE)
    center_col = divide(decrement(side), TWO)
    if flip(even(side)) and choice((T, F)):
        marker_col = center_col
    else:
        non_center_cols = remove(center_col, candidate_cols)
        marker_col = choice(non_center_cols if len(non_center_cols) > ZERO else candidate_cols)
    bgc, dotc = sample(COLORS_7EC998C9, TWO)

    gi = canvas(bgc, (side, side))
    gi = fill(gi, dotc, initset((marker_row, marker_col)))

    top_loc = (ZERO, marker_col)
    bottom_loc = (decrement(side), marker_col)
    top_right = (ZERO, decrement(side))
    bottom_left = (decrement(side), ZERO)
    bottom_right = (decrement(side), decrement(side))
    is_center_column = double(marker_col) == decrement(side)

    go = underfill(gi, ONE, connect(top_loc, bottom_loc))
    go = underfill(go, ONE, connect(branch(is_center_column, top_loc, ORIGIN), branch(is_center_column, top_right, top_loc)))
    go = underfill(
        go,
        ONE,
        connect(branch(is_center_column, bottom_left, bottom_loc), branch(is_center_column, bottom_loc, bottom_right)),
    )

    from .verifier import verify_7ec998c9

    if verify_7ec998c9(gi) != go:
        raise ValueError("generator produced an invalid example")
    return {"input": gi, "output": go}
