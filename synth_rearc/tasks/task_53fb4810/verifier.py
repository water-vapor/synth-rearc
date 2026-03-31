from synth_rearc.core import *


def _strip_step_53fb4810(
    x0: Object,
    x1: Object,
) -> IntegerTuple:
    if lowermost(x1) < uppermost(x0):
        return (-height(x1), ZERO)
    if uppermost(x1) > lowermost(x0):
        return (height(x1), ZERO)
    if rightmost(x1) < leftmost(x0):
        return (ZERO, -width(x1))
    return (ZERO, width(x1))


def verify_53fb4810(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = colorfilter(objects(I, T, F, T), ONE)
    x2 = I
    x3 = interval(ONE, add(maximum(shape(I)), ONE), ONE)
    for x4 in x0:
        x5 = extract(x1, lambda x: positive(size(intersection(toindices(x), toindices(x4)))))
        x6 = difference(toindices(x4), toindices(x5))
        x7 = toobject(x6, I)
        x8 = _strip_step_53fb4810(x5, x7)
        for x9 in x3:
            x10 = shift(x7, multiply(x8, x9))
            x2 = paint(x2, x10)
    return x2
