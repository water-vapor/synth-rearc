from synth_rearc.core import *

from .helpers import hole_count_e3721c99


def verify_e3721c99(
    I: Grid,
) -> Grid:
    x0 = objects(I, T, F, F)
    x1 = sfilter(x0, compose(flip, matcher(color, ZERO)))
    x2 = colorfilter(x1, FIVE)
    x3 = sfilter(
        x1,
        lambda x4: both(
            flip(equality(color(x4), FIVE)),
            flip(bordering(x4, I)),
        ),
    )
    x4 = {hole_count_e3721c99(x5): color(x5) for x5 in x3}
    x5 = replace(I, FIVE, ZERO)
    for x6 in x2:
        x7 = hole_count_e3721c99(x6)
        if x7 not in x4:
            continue
        x8 = recolor(x4[x7], x6)
        x5 = paint(x5, x8)
    return x5
