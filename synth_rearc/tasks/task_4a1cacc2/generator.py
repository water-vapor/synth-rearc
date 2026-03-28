from synth_rearc.core import *


_SEED_COLORS_4A1CACC2 = (FOUR, SIX, NINE)
_CORNERS_4A1CACC2 = ("tl", "tr", "bl", "br")


def generate_4a1cacc2(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = multiply(TWO, unifint(diff_lb, diff_ub, (TWO, SIX)))
        w = multiply(TWO, unifint(diff_lb, diff_ub, (TWO, SIX)))
        rect_h = unifint(diff_lb, diff_ub, (ONE, divide(h, TWO)))
        rect_w = unifint(diff_lb, diff_ub, (ONE, divide(w, TWO)))
        if both(equality(rect_h, ONE), equality(rect_w, ONE)):
            continue
        corner = choice(_CORNERS_4A1CACC2)
        last_i = subtract(h, ONE)
        last_j = subtract(w, ONE)
        if corner == "tl":
            anchor = ORIGIN
            seed = (subtract(rect_h, ONE), subtract(rect_w, ONE))
        elif corner == "tr":
            anchor = (ZERO, last_j)
            seed = (subtract(rect_h, ONE), subtract(w, rect_w))
        elif corner == "bl":
            anchor = (last_i, ZERO)
            seed = (subtract(h, rect_h), subtract(rect_w, ONE))
        else:
            anchor = (last_i, last_j)
            seed = (subtract(h, rect_h), subtract(w, rect_w))
        color0 = choice(_SEED_COLORS_4A1CACC2)
        gi = canvas(EIGHT, (h, w))
        gi = fill(gi, color0, initset(seed))
        patch = backdrop(insert(anchor, initset(seed)))
        go = fill(gi, color0, patch)
        return {"input": gi, "output": go}
