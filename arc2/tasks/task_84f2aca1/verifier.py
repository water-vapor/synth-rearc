from arc2.core import *


def verify_84f2aca1(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = lambda x: both(greater(height(x), TWO), greater(width(x), TWO))
    x2 = lambda x: equality(toindices(x), box(x))
    x3 = lbind(index, I)
    x4 = matcher(x3, ZERO)
    x5 = lambda x: sfilter(delta(x), x4)
    x6 = lambda x: both(
        contained(size(x5(x)), (ONE, TWO)),
        equality(size(delta(x)), size(x5(x))),
    )
    x7 = fork(both, x1, x2)
    x8 = sfilter(x0, fork(both, x7, x6))
    x9 = I
    for x10 in x8:
        x11 = x5(x10)
        x12 = branch(equality(size(x11), ONE), FIVE, SEVEN)
        x9 = fill(x9, x12, x11)
    return x9
