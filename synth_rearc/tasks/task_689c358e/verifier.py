from synth_rearc.core import *


def verify_689c358e(I: Grid) -> Grid:
    def project(x0: Object) -> Object:
        y0 = toindices(x0)
        y1 = uppermost(x0)
        y2 = matcher(first, y1)
        y3 = sfilter(y0, y2)
        y4 = leftmost(y3)
        y5 = leftmost(x0)
        y6 = matcher(last, y5)
        y7 = sfilter(y0, y6)
        y8 = uppermost(y7)
        y9 = portrait(x0)
        y10 = color(x0)
        y11 = greater(y8, FIVE)
        y12 = greater(y4, FIVE)
        y13 = branch(y11, (TEN, y4), (ZERO, y4))
        y14 = branch(y11, (ZERO, y4), (TEN, y4))
        y15 = branch(y12, (y8, TEN), (y8, ZERO))
        y16 = branch(y12, (y8, ZERO), (y8, TEN))
        y17 = branch(y9, y13, y15)
        y18 = branch(y9, y14, y16)
        return frozenset({(y10, y17), (ZERO, y18)})

    x0 = fgpartition(I)
    x1 = matcher(color, SIX)
    x2 = compose(flip, x1)
    x3 = sfilter(x0, x2)
    x4 = mapply(project, x3)
    x5 = paint(I, x4)
    return x5
