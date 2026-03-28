from synth_rearc.core import *


def route_f8f52ecc(
    a: IntegerTuple,
    b: IntegerTuple,
    barriers: Indices,
) -> Indices:
    x0, x1 = a
    x2, x3 = b
    if x0 == x2 or x1 == x3:
        return connect(a, b)
    x4 = astuple(x0, x3)
    x5 = astuple(x2, x1)
    x6 = combine(connect(a, x4), connect(x4, b))
    x7 = combine(connect(a, x5), connect(x5, b))
    x8 = branch(greater(x3, x1), x7, x6)
    x9 = branch(greater(x3, x1), x6, x7)
    if len(intersection(x8, barriers)) == ZERO:
        return x8
    return x9
