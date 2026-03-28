from synth_rearc.core import *


def verify_84db8fc4(
    I: Grid,
) -> Grid:
    x0 = objects(I, T, F, F)
    x1 = colorfilter(x0, ZERO)
    x2 = rbind(bordering, I)
    x3 = sfilter(x1, x2)
    x4 = merge(x3)
    x5 = fill(I, TWO, x4)
    x6 = compose(flip, x2)
    x7 = sfilter(x1, x6)
    x8 = merge(x7)
    x9 = fill(x5, FIVE, x8)
    return x9
