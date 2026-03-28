from synth_rearc.core import *

from .helpers import (
    AXIS_KINDS_ad3b40cf,
    COLOR_POOL_ad3b40cf,
    axis_patch_ad3b40cf,
    mirror_patch_ad3b40cf,
    padded_backdrop_ad3b40cf,
    sample_compact_patch_ad3b40cf,
)


def generate_ad3b40cf(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(AXIS_KINDS_ad3b40cf)
        if x0 in ("vertical", "horizontal"):
            x1 = tuple(range(NINE, 20, TWO))
        else:
            x1 = tuple(range(NINE, 20))
        x2 = choice(x1)
        x3, x4 = sample(COLOR_POOL_ad3b40cf, TWO)
        x5 = choice((-ONE, ONE))
        x6 = axis_patch_ad3b40cf(x2, x0)
        x7 = x6
        x8 = choice((ONE, TWO))
        x9 = []
        failed = F
        for _ in range(x8):
            x10 = sample_compact_patch_ad3b40cf(
                x2,
                x0,
                x5,
                x7,
                diff_lb,
                diff_ub,
                (THREE, FIVE),
            )
            if x10 is None:
                failed = T
                break
            x9.append(x10)
            x7 = combine(x7, padded_backdrop_ad3b40cf(backdrop(x10), x2))
        if failed:
            continue
        x11 = sum(len(x12) for x12 in x9)
        x13 = choice((ONE, TWO, TWO, THREE))
        x14 = []
        for _ in range(x13):
            x15 = sample_compact_patch_ad3b40cf(
                x2,
                x0,
                x5,
                x7,
                diff_lb,
                diff_ub,
                (ONE, SIX),
            )
            if x15 is None:
                failed = T
                break
            x14.append(x15)
            x7 = combine(x7, padded_backdrop_ad3b40cf(backdrop(x15), x2))
        if failed:
            continue
        x16 = sum(len(x17) for x17 in x14)
        if x16 <= x11:
            continue
        x18 = canvas(EIGHT, (x2, x2))
        x19 = fill(x18, ONE, x6)
        x20 = x19
        for x21 in x14:
            x19 = fill(x19, x4, x21)
            x20 = fill(x20, x4, x21)
        for x22 in x9:
            x19 = fill(x19, x3, x22)
            x20 = fill(x20, x3, x22)
            x23 = mirror_patch_ad3b40cf(x22, x2, x0)
            x20 = underfill(x20, x3, x23)
        if x19 == x20:
            continue
        return {"input": x19, "output": x20}
