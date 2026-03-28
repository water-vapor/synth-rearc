from arc2.core import *

from .helpers import render_table_6165ea8f, shape_signature_6165ea8f


def verify_6165ea8f(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = decrement(x1)
    x3 = interval(ZERO, x0, ONE)
    x4 = rbind(astuple, x2)
    x5 = apply(x4, x3)
    x6 = lbind(index, I)
    x7 = matcher(x6, ZERO)
    x8 = compose(flip, x7)
    x9 = sfilter(x5, x8)
    x10 = apply(x6, x9)
    x11 = objects(I, T, F, T)
    x12 = matcher(size, ONE)
    x13 = matcher(rightmost, x2)
    x14 = fork(both, x12, x13)
    x15 = sfilter(x11, x14)
    x16 = difference(x11, x15)
    x17 = lbind(colorfilter, x16)
    x18 = apply(x17, x10)
    x19 = apply(first, x18)
    x20 = apply(shape_signature_6165ea8f, x19)
    x21 = render_table_6165ea8f(x10, x20)
    return x21
