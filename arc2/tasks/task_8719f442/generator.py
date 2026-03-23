from arc2.core import *

from .verifier import verify_8719f442


INPUT_DIMS_8719F442 = (THREE, THREE)
INPUT_CENTER_8719F442 = (ONE, ONE)
CELL_COUNT_BOUNDS_8719F442 = (THREE, FIVE)
CELL_OPTIONS_8719F442 = tuple(product(interval(ZERO, THREE, ONE), interval(ZERO, THREE, ONE)))
FOREGROUND_COLOR_8719F442 = FIVE


def generate_8719f442(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = FOREGROUND_COLOR_8719F442
        x1 = unifint(diff_lb, diff_ub, CELL_COUNT_BOUNDS_8719F442)
        x2 = sample(CELL_OPTIONS_8719F442, x1)
        if all(equality(x3, INPUT_CENTER_8719F442) for x3 in x2):
            continue
        x4 = fill(canvas(ZERO, INPUT_DIMS_8719F442), x0, x2)
        x5 = asobject(x4)
        x6 = asobject(canvas(x0, INPUT_DIMS_8719F442))
        x7 = subtract(double(INPUT_DIMS_8719F442), ONE)
        x8 = multiply(INPUT_DIMS_8719F442, x7)
        x9 = canvas(ZERO, x8)
        for x10 in x2:
            x11 = subtract(x10, INPUT_CENTER_8719F442)
            x12 = sign(x11)
            x13 = add(x10, INPUT_CENTER_8719F442)
            if not equality(x12[ZERO], ZERO):
                x14 = add(x13, toivec(x12[ZERO]))
                x15 = multiply(x14, INPUT_DIMS_8719F442)
                x16 = shift(x5, x15)
                x9 = paint(x9, x16)
            if not equality(x12[ONE], ZERO):
                x17 = add(x13, tojvec(x12[ONE]))
                x18 = multiply(x17, INPUT_DIMS_8719F442)
                x19 = shift(x5, x18)
                x9 = paint(x9, x19)
        x20 = x9
        for x21 in x2:
            x22 = add(x21, INPUT_CENTER_8719F442)
            x23 = multiply(x22, INPUT_DIMS_8719F442)
            x24 = shift(x6, x23)
            x20 = paint(x20, x24)
        if verify_8719f442(x4) != x20:
            continue
        return {"input": x4, "output": x20}
