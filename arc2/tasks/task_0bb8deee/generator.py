from arc2.core import *


MOTIFS_0BB8DEEE = (
    frozenset({(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 1)}),
    frozenset({(0, 0), (1, 1), (1, 2), (2, 1)}),
    frozenset({(0, 2), (1, 0), (1, 1), (1, 2), (2, 1)}),
    frozenset({(0, 0), (0, 2), (1, 1), (2, 0)}),
    frozenset({(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)}),
    frozenset({(0, 1), (0, 2), (1, 0), (1, 1), (2, 1)}),
    frozenset({(0, 1), (1, 0), (1, 2), (2, 1)}),
    frozenset({(0, 0), (0, 1), (1, 1), (2, 2)}),
    frozenset({(0, 1), (0, 2), (1, 0), (1, 2), (2, 1)}),
    frozenset({(0, 1), (0, 2), (1, 0), (2, 1)}),
    frozenset({(0, 0), (1, 0), (1, 1), (1, 2), (2, 1)}),
    frozenset({(0, 1), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)}),
)


def generate_0bb8deee(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        top_h = unifint(diff_lb, diff_ub, (3, 9))
        bottom_h = unifint(diff_lb, diff_ub, (3, 11))
        left_w = unifint(diff_lb, diff_ub, (3, 7))
        right_w = unifint(diff_lb, diff_ub, (3, 8))
        sep_r = top_h
        sep_c = left_w
        gi = canvas(ZERO, (top_h + bottom_h + ONE, left_w + right_w + ONE))
        colors = sample(cols, FIVE)
        sep_col = colors[ZERO]
        quad_cols = colors[ONE:]
        gi = fill(gi, sep_col, hfrontier((sep_r, ZERO)))
        gi = fill(gi, sep_col, vfrontier((ZERO, sep_c)))
        motifs = sample(MOTIFS_0BB8DEEE, FOUR)
        out_quads = []
        specs = (
            (ZERO, ZERO, top_h, left_w),
            (ZERO, increment(sep_c), top_h, right_w),
            (increment(sep_r), ZERO, bottom_h, left_w),
            (increment(sep_r), increment(sep_c), bottom_h, right_w),
        )
        for x0, x1, x2, x3 in specs:
            motif = motifs[len(out_quads)]
            color_value = quad_cols[len(out_quads)]
            top = x0 + randint(ZERO, x2 - THREE)
            left = x1 + randint(ZERO, x3 - THREE)
            patch = shift(motif, (top, left))
            gi = fill(gi, color_value, patch)
            go_quad = fill(canvas(ZERO, (THREE, THREE)), color_value, motif)
            out_quads.append(go_quad)
        if mostcolor(gi) != ZERO:
            continue
        go = vconcat(
            hconcat(out_quads[ZERO], out_quads[ONE]),
            hconcat(out_quads[TWO], out_quads[THREE]),
        )
        return {"input": gi, "output": go}
