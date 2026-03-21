from arc2.core import *

from .helpers import (
    pack_bottom_ac2e8ecf,
    pack_top_ac2e8ecf,
    paint_objects_ac2e8ecf,
)


def verify_ac2e8ecf(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = rbind(greater, TWO)
    x2 = compose(x1, height)
    x3 = compose(x1, width)
    x4 = fork(both, x2, x3)
    x5 = fork(equality, toindices, box)
    x6 = fork(both, x4, x5)
    x7 = sfilter(x0, x6)
    x8 = difference(x0, x7)
    x9 = pack_top_ac2e8ecf(x7)
    x10 = height(I)
    x11 = pack_bottom_ac2e8ecf(x8, x10)
    x12 = canvas(ZERO, shape(I))
    x13 = paint_objects_ac2e8ecf(x12, x9)
    x14 = paint_objects_ac2e8ecf(x13, x11)
    return x14
