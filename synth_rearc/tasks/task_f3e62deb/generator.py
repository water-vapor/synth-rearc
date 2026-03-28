from synth_rearc.core import *

from .verifier import verify_f3e62deb


FG_COLORS_F3E62DEB = (THREE, FOUR, SIX, EIGHT)


def _ring_patch_f3e62deb(
    top: Integer,
    left: Integer,
) -> Indices:
    x0 = interval(top, top + THREE, ONE)
    x1 = interval(left, left + THREE, ONE)
    x2 = product(x0, x1)
    x3 = box(x2)
    return x3


def _render_f3e62deb(
    dims: IntegerTuple,
    top: Integer,
    left: Integer,
    color: Integer,
) -> Grid:
    x0 = canvas(ZERO, dims)
    x1 = _ring_patch_f3e62deb(top, left)
    x2 = fill(x0, color, x1)
    return x2


def generate_f3e62deb(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (TEN, 30))
        x1 = astuple(x0, x0)
        x2 = subtract(x0, FOUR)
        x3 = choice(FG_COLORS_F3E62DEB)
        x4 = unifint(diff_lb, diff_ub, (ONE, x2))
        x5 = unifint(diff_lb, diff_ub, (ONE, x2))
        x6 = _render_f3e62deb(x1, x4, x5, x3)
        x7 = equality(x3, SIX)
        x8 = equality(x3, EIGHT)
        x9 = equality(x3, FOUR)
        x10 = subtract(x0, THREE)
        x11 = branch(x7, ZERO, branch(x9, x10, x4))
        x12 = branch(x8, x10, branch(equality(x3, THREE), ZERO, x5))
        x13 = _render_f3e62deb(x1, x11, x12, x3)
        if verify_f3e62deb(x6) != x13:
            continue
        return {"input": x6, "output": x13}
