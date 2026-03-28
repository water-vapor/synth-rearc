from arc2.core import *


def _holecount_37d3e8b2(
    grid: Grid,
    obj: Object,
) -> Integer:
    x0 = subgrid(obj, grid)
    x1 = objects(x0, T, F, F)
    x2 = colorfilter(x1, ZERO)
    x3 = rbind(bordering, x0)
    x4 = compose(flip, x3)
    x5 = sfilter(x2, x4)
    return size(x5)


def _holecolor_37d3e8b2(
    count: Integer,
) -> Integer:
    x0 = equality(count, ONE)
    x1 = equality(count, TWO)
    x2 = equality(count, THREE)
    x3 = branch(x2, THREE, SEVEN)
    x4 = branch(x1, TWO, x3)
    x5 = branch(x0, ONE, x4)
    return x5


def verify_37d3e8b2(
    I: Grid,
) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = canvas(ZERO, shape(I))
    for x2 in x0:
        x3 = _holecount_37d3e8b2(I, x2)
        x4 = _holecolor_37d3e8b2(x3)
        x5 = recolor(x4, x2)
        x1 = paint(x1, x5)
    return x1
