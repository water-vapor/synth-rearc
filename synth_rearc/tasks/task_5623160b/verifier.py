from synth_rearc.core import *


def verify_5623160b(I: Grid) -> Grid:
    def slide(x0: Object) -> Object:
        y0 = toindices(x0)
        y1 = intersection(y0, x1)
        y2 = positive(size(intersection(shift(y1, UP), x0_hub)))
        y3 = positive(size(intersection(shift(y1, DOWN), x0_hub)))
        y4 = positive(size(intersection(shift(y1, LEFT), x0_hub)))
        y5 = toivec(invert(uppermost(x0)))
        y6 = toivec(subtract(decrement(x2), lowermost(x0)))
        y7 = tojvec(invert(leftmost(x0)))
        y8 = tojvec(subtract(decrement(x3), rightmost(x0)))
        y9 = branch(y2, y6, branch(y3, y5, branch(y4, y8, y7)))
        return shift(x0, y9)

    x0_hub = ofcolor(I, NINE)
    x1 = mapply(dneighbors, x0_hub)
    x2 = height(I)
    x3 = width(I)
    x4 = objects(I, T, F, T)
    x5 = colorfilter(x4, NINE)
    x6 = difference(x4, x5)
    x7 = mapply(slide, x6)
    x8 = canvas(mostcolor(I), shape(I))
    x9 = paint(x8, merge(x5))
    x10 = paint(x9, x7)
    return x10
